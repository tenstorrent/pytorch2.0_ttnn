import torch
import ttnn
from torch.fx.passes.infra.pass_base import PassBase, PassResult
from torch_ttnn.passes.lowering.add_data_move_pass import is_tt_data_move, is_tt_compute
from torch_ttnn.utils import TtnnDevice

import json
import os
from pathlib import Path

# Configs
device_name = "wormhole"
cores = 120
SRAM_LIMIT = 104857600 # 100 * 1024 * 1024 bytes (100 MB)
L1_mem = 1048576 # 1 MB
circular_buffer = 20 * 1048576 # 20 MB

# This will manage all memory related operations & data
class MemoryManager:
    def __init__(self, device, cores, L1_mem, circular_buffer):
        self.device = device
        self.cores = cores
        self.L1_mem = L1_mem
        self.total_sram_limit = self.cores * self.L1_mem
        self.circular_buffer = circular_buffer
        self.free_sram = self.total_sram_limit - self.circular_buffer
        self.used_sram = 0
    
    def set_mem_data(self, mem_data):
        self.mem_data = mem_data

    def set_ops_mem_usage(self, ops_mem_usage):
        self.ops_mem_usage = ops_mem_usage
    
    def set_node_to_tid_map(self, node_to_tid_map):
        self.node_to_tid_map = node_to_tid_map

    def set_tid_to_addr_map(self, tid_to_addr_map):
        self.tid_to_addr_map = tid_to_addr_map


# This holds op related information one can query from
class OpRegistry:
    def get_size(self, shape, dtype):
        size = 1
        if dtype is torch.bfloat16:
            size = 2
        for val in list(shape):
            size = val * size
        return size

    def get_shape(self, node):
        if is_tt_data_move(node):
            assert len(node.all_input_nodes) == 1, "Data movement operators can't have more than one input!"
            return self.get_shape(node.all_input_nodes[0])
        else:
            # TODO: What if meta of nth output of the node is requested?
            if isinstance(node.meta["val"], tuple):
                return node.meta["val"][0].size()
            else:
                return node.meta["val"].size()

    def get_dtype(self, node):
        if is_tt_data_move(node):
            assert len(node.all_input_nodes) == 1, "Data movement operators can't have more than one input!"
            return self.get_dtype(node.all_input_nodes[0])
        else:
            # TODO: What if meta of nth output of the node is requested?
            if isinstance(node.meta["val"], tuple):
                return node.meta["val"][0].dtype
            else:
                return node.meta["val"].dtype
   
    def is_input_tensor_on_device(self, node):
        if node.target == ttnn.from_torch:
            if "device" in node.kwargs and isinstance(node.kwargs["device"], TtnnDevice):
                return True
        if node.target is ttnn.to_device or is_tt_compute(node):
            return True
        # This is a data move op which propagates shape of input tensor
        if node.target == ttnn.Shape or node.target == ttnn.from_device:
            return False
        # Considers cases like ttnn op --> to_layout
        if is_tt_data_move(node):
            return self.is_input_tensor_on_device(node.all_input_nodes[0])
        else:
            return False



def memory_footprint(gm: torch.fx.GraphModule) -> torch.fx.GraphModule:

    mm = MemoryManager(
        device_name,
        cores,
        L1_mem,
        circular_buffer
    )

    op_registry = OpRegistry()

    print("Track memory footprint for each of the ops:")
    nodes = list(gm.graph.nodes)

    # Each node's output tensor will be assigned a unique tensor ID
    node_to_tid_map = {}
    # Tensor ID to address map
    tid_to_addr_map_in_L1 = {}
    # Tensor ID allocation tracker
    last_assigned_tid = 0
    # Memory address allocation tracker
    last_assigned_addr = 0
    # List of already executed nodes on device
    computed_nodes = []
    # Data points containing info of on device tensors allocation & deallocation for ttnn ops
    # Useful for visualization by plotting in a chart
    data_points = {}
    # On device tensors info
    on_device_meta = []
    # Each ops memory usage on device
    ops_mem_usage = {}

    # Tensor IDs allocation for ttnn ops input & output
    tt_compute_count = 0
    for node in nodes:
        if is_tt_compute(node):
            tt_compute_count += 1
            # For inputs
            for input_node in node.all_input_nodes:
                if input_node not in node_to_tid_map:
                    node_to_tid_map[input_node] = last_assigned_tid
                    last_assigned_tid += 1
            # For output
            if node not in node_to_tid_map:
                node_to_tid_map[node] = last_assigned_tid
                last_assigned_tid += 1
    
    mm.set_node_to_tid_map(node_to_tid_map)

    # print(f"Tensor IDs for nodes on device:")
    # for key, value in node_to_tid_map.items():
    #     print(f"Node: {key} - {value}")

    # Tracks the total compute memory of the model
    print(f"Total tt compute nodes: {tt_compute_count}")
    i = 0
    overflow_ops = []

    for node in nodes:
        on_device = False
        # Has to be a ttnn op
        if is_tt_compute(node):
            print(f"tt compute node numbered: {i}")
            i += 1
            # Exception: Full node has no input
            # Assumption: Full node outputs a tensor on device
            if node.target == ttnn.full:
                on_device = True
            total_input_size = 0
            for input_node in node.all_input_nodes:
                # If input tensor on device or coming as output from another ttnn on device op
                if op_registry.is_input_tensor_on_device(input_node):
                    on_device = True
                    input_shape = op_registry.get_shape(input_node)
                    input_dtype = op_registry.get_dtype(input_node)
                    input_size = op_registry.get_size(input_shape, input_dtype)
                    total_input_size += input_size
                    
                    assert input_node in node_to_tid_map, "Tensor ID not allocated for one of the inputs!"

                    tid = node_to_tid_map[input_node]
                    start_addr = last_assigned_addr
                    last_assigned_addr += input_size
                    end_addr = last_assigned_addr
                    tid_to_addr_map_in_L1[tid] = (start_addr, end_addr)

                    if (tid, input_size) not in on_device_meta:
                        on_device_meta.append((tid, input_size))


            if on_device:
                output_shape = op_registry.get_shape(node)
                output_dtype = op_registry.get_dtype(node)
                output_size = op_registry.get_size(output_shape, output_dtype)

                mm.used_sram += total_input_size + output_size
                mm.free_sram -= (total_input_size + output_size)
                ops_mem_usage[node.name] = total_input_size + output_size

                assert node in node_to_tid_map, "Tensor ID not allocated for one of the inputs!"

                tid = node_to_tid_map[node]
                start_addr = last_assigned_addr
                last_assigned_addr += output_size
                end_addr = last_assigned_addr
                tid_to_addr_map_in_L1[tid] = (start_addr, end_addr)

                if (tid, output_size) not in on_device_meta:
                    on_device_meta.append((tid, output_size))

                data_points[(node.name, "to_device")] = on_device_meta.copy()

                if mm.used_sram >= SRAM_LIMIT:
                    overflow_ops.append(node)

                print("\n---------------------------------------------------")
                print(f"op execution on device: {node.name}")
                print(f"input size: {total_input_size} bytes")
                print(f"output size: {output_size} bytes")
                print(f"total compute memory parked in L1: {mm.used_sram} bytes")

                # This part of code is to assess whether we can swap out output tensor from device
                node_users = list(node.users.keys())
                # Are any users of current node a ttnn op?
                is_follow_up_tt_compute = False
                 # Is from device op a user of the node?
                is_follow_up_from_device = False
                for user in node_users:
                    if is_tt_compute(user):
                        is_follow_up_tt_compute = True
                    if user.target in set(
                        [
                        ttnn.from_device,
                        ttnn.to_torch,
                        ttnn.to_layout
                        ]
                    ):
                        is_follow_up_from_device = True
  
                # If no follow up ttnn op using the output of current node
                # and if one of the users is a from device operation,
                # then swap out output tensor from device
                if not is_follow_up_tt_compute and is_follow_up_from_device:
                    mm.used_sram -= output_size
                    mm.free_sram += output_size

                    on_device_meta.remove((tid, output_size))
                    
                    print(f"op removed from device: {node.name}")
                    print(f"output size: {output_size} bytes")
                    print(f"total compute memory parked in L1: {mm.used_sram} bytes")
                # Once current node's input & output tensor processing is over, mark it as computed
                computed_nodes.append(node)
                # Swap out input tensors from device if its usage is completed
                # i.e there are no ttnn ops on device which uses the tensor
                for input_node in node.all_input_nodes:
                    # Exception: Shape node is just like a parameter containing shape of input tensor
                    if input_node.target == ttnn.Shape:
                        continue
                    keep_on_device = False
                    input_node_users = list(input_node.users.keys())
                    for user in input_node_users:
                        if user not in computed_nodes and is_tt_compute(user):
                            keep_on_device = True
                    if keep_on_device is False:
                        input_size = op_registry.get_size(
                            op_registry.get_shape(input_node),
                            op_registry.get_dtype(input_node)
                        )
                        mm.used_sram -= input_size
                        mm.free_sram += input_size
                        tid = node_to_tid_map[input_node]
                        on_device_meta.remove((tid, input_size))

                        print(f"input tensor removed from device: {input_size} bytes")
                        print(f"total compute memory parked in L1: {mm.used_sram} bytes")
                
                data_points[(node.name, "from_device")] = on_device_meta.copy()
    
    mm.set_ops_mem_usage(ops_mem_usage)
    mm.set_tid_to_addr_map(tid_to_addr_map_in_L1)

    print(f"Tensor IDs to address map in SRAM:")
    print(f"{tid_to_addr_map_in_L1}")
    print(f"----------------------------------------------------------------")
    print(f"These ttnn ops overflow the L1 buffer:")
    for op in overflow_ops:
        print(op)
    print(f"Data captured for plotting on a chart:")
    for key, value in data_points.items():
        print(f"{key}: {value}")
    # Save the data points to a file
    p = Path(f"data/memory")
    os.makedirs(p, exist_ok=True)
    # Convert dictionary keys to strings
    data_str_keys = {str(key): value for key, value in data_points.items()}
    mm.set_mem_data(data_str_keys)

    with open("./data/memory/memory_footprint.txt", 'w') as f:
        json.dump(data_str_keys, f)

    return gm, mm


class MemoryPass(PassBase):
    def call(self, gm: torch.fx.GraphModule):
        gm, self.memory_manager = memory_footprint(gm)
        return PassResult(gm, True)
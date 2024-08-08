import torch
import ttnn
from torch.fx.passes.infra.pass_base import PassBase, PassResult
from torch_ttnn.passes.lowering.add_data_move_pass import is_tt_data_move, is_tt_compute

from torch_ttnn.mem_utils import *

import json
import os
from pathlib import Path


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

    # Tensor ID allocation tracker
    last_assigned_tid = 1
    # Memory address allocation tracker
    last_assigned_addr = 0
    # List of already executed nodes on device
    computed_nodes = []
    # Data points containing info of on device tensors allocation & deallocation for ttnn ops
    # Useful for visualization by plotting in a chart
    data_points = {}
    # On device tensors info
    on_device_meta = []

    # Tensor IDs allocation for ttnn ops input & output
    tt_compute_count = 0
    for node in nodes:
        if is_tt_compute(node):
            tt_compute_count += 1
            # For inputs
            for input_node in node.all_input_nodes:
                if input_node not in mm.node_to_tid_map:
                    mm.node_to_tid_map[input_node] = last_assigned_tid
                    last_assigned_tid += 1
            # For output
            if node not in mm.node_to_tid_map:
                mm.node_to_tid_map[node] = last_assigned_tid
                last_assigned_tid += 1
    

    # print(f"Tensor IDs for nodes on device:")
    # for key, value in mm.node_to_tid_map.items():
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
            # Input & Output tensor IDs for ttnn op
            ttnn_ops_tids = []
            for input_node in node.all_input_nodes:
                # If input tensor on device or coming as output from another ttnn on device op
                if op_registry.is_input_tensor_on_device(input_node):
                    on_device = True
                    input_shape = op_registry.get_shape(input_node)
                    input_dtype = op_registry.get_dtype(input_node)
                    input_size = op_registry.get_size(input_shape, input_dtype)
                    total_input_size += input_size
                    
                    assert input_node in mm.node_to_tid_map, "Tensor ID not allocated for one of the inputs!"
                    
                    tid = mm.node_to_tid_map[input_node]
                    ttnn_ops_tids.append(tid)
                    mm.tensor_size_of[tid] = input_size

                    start_addr = last_assigned_addr
                    last_assigned_addr += input_size
                    end_addr = last_assigned_addr
                    mm.tid_to_addr_map_in_sram[tid] = (start_addr, end_addr)

                    if tid not in mm.tensors_on_device:
                        mm.used_sram += input_size
                        mm.free_sram -= input_size
                        mm.tensors_on_device.append(tid)

                    if (tid, input_size) not in on_device_meta:
                        on_device_meta.append((tid, input_size))

            if on_device:
                output_shape = op_registry.get_shape(node)
                output_dtype = op_registry.get_dtype(node)
                output_size = op_registry.get_size(output_shape, output_dtype)

                mm.ops_mem_usage[node.name] = total_input_size + output_size

                assert node in mm.node_to_tid_map, "Tensor ID not allocated for one of the inputs!"

                tid = mm.node_to_tid_map[node]
                ttnn_ops_tids.append(tid)
                mm.ttnn_ops_tids[node.name] = ttnn_ops_tids
                mm.tensor_size_of[tid] = output_size

                start_addr = last_assigned_addr
                last_assigned_addr += output_size
                end_addr = last_assigned_addr
                mm.tid_to_addr_map_in_sram[tid] = (start_addr, end_addr)

                mm.used_sram += output_size
                mm.free_sram -= output_size
                mm.tensors_on_device.append(tid)
                mm.tids_in_sram_at[node.name] = mm.tensors_on_device.copy()
                mm.sram_usage_at[node.name] = mm.used_sram

                if (tid, output_size) not in on_device_meta:
                    on_device_meta.append((tid, output_size))

                data_points[(node.name, tid, "to_device")] = on_device_meta.copy()

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
                    mm.tensors_on_device.remove(tid)

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
                        tid = mm.node_to_tid_map[input_node]
                        mm.tensors_on_device.remove(tid)
                        on_device_meta.remove((tid, input_size))

                        print(f"input tensor removed from device: {input_size} bytes")
                        print(f"total compute memory parked in L1: {mm.used_sram} bytes")
                
                # data_points[(node.name, "from_device")] = on_device_meta.copy()
        
    

    print(f"Tensor IDs to address map in SRAM:")
    print(f"{mm.tid_to_addr_map_in_sram}")
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
    mm.data_points = data_str_keys

    with open("./data/memory/memory_footprint.txt", 'w') as f:
        json.dump(data_str_keys, f)

    return gm, mm


class MemoryPass(PassBase):
    def call(self, gm: torch.fx.GraphModule):
        gm, self.memory_manager = memory_footprint(gm)
        return PassResult(gm, True)
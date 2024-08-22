import torch
import ttnn
from torch.fx.passes.infra.pass_base import PassBase, PassResult
from torch_ttnn.passes.lowering.add_data_move_pass import is_tt_compute

from torch_ttnn import mem_utils


class MemoryPass(PassBase):
    def __init__(self, verbose=True):
        self.verbose = verbose
        self.mm = mem_utils.MemoryManager(
            mem_utils.device_name,
            mem_utils.cores,
            mem_utils.L1_mem,
            mem_utils.circular_buffer,
        )
        self.op_registry = mem_utils.OpRegistry()

    # Tensor IDs allocation for ttnn ops input & output
    def assign_tensor_ids(self, gm: torch.fx.GraphModule):
        # Tensor ID allocation tracker
        last_assigned_tid = 1
        tt_compute_count = 0
        nodes = list(gm.graph.nodes)
        for node in nodes:
            if is_tt_compute(node):
                tt_compute_count += 1
                # For inputs
                for input_node in node.all_input_nodes:
                    if input_node not in self.mm.node_to_tid_map:
                        self.mm.node_to_tid_map[input_node] = last_assigned_tid
                        last_assigned_tid += 1
                # For output
                if node not in self.mm.node_to_tid_map:
                    self.mm.node_to_tid_map[node] = last_assigned_tid
                    last_assigned_tid += 1

        self.mm.log(f"Tensor IDs for nodes on device:\n")
        for key, value in self.mm.node_to_tid_map.items():
            self.mm.log(f"Node: {key} - {value}\n")
        return tt_compute_count

    def allocate(self, node: torch.fx.node.Node):
        tensor_shape, tensor_dtype = self.op_registry.get_tensor_shape_and_dtype(node)
        tensor_size = mem_utils.get_tensor_size(tensor_shape, tensor_dtype)

        assert (
            node in self.mm.node_to_tid_map
        ), "Tensor ID is not assigned for one of the inputs of ttnn op!"

        tid = self.mm.node_to_tid_map[node]
        self.mm.tensor_size_of[tid] = tensor_size

        start_addr = self.mm.last_assigned_addr
        self.mm.last_assigned_addr += tensor_size
        end_addr = self.mm.last_assigned_addr
        self.mm.tid_to_addr_map_in_sram[tid] = (start_addr, end_addr)

        if tid not in self.mm.tensors_on_device:
            self.mm.used_sram += tensor_size
            self.mm.free_sram -= tensor_size
            self.mm.tensors_on_device.append(tid)
        return (tid, tensor_size)

    def deallocate(self, node: torch.fx.node.Node):
        (
            tensor_shape,
            tensor_dtype,
        ) = self.op_registry.get_tensor_shape_and_dtype(node)
        tensor_size = mem_utils.get_tensor_size(
            tensor_shape,
            tensor_dtype,
        )
        self.mm.used_sram -= tensor_size
        self.mm.free_sram += tensor_size
        tid = self.mm.node_to_tid_map[node]
        self.mm.tensors_on_device.remove(tid)
        return (tid, tensor_size)

    def memory_footprint(
        self, gm: torch.fx.GraphModule, verbose=True
    ) -> torch.fx.GraphModule:
        self.mm = mem_utils.MemoryManager(
            mem_utils.device_name,
            mem_utils.cores,
            mem_utils.L1_mem,
            mem_utils.circular_buffer,
        )
        op_registry = mem_utils.OpRegistry()
        self.mm.log("Track memory footprint for each of the ops:\n")

        # List of already executed nodes on device
        computed_nodes = []
        # Data points containing info of on device tensors allocation & deallocation for ttnn ops
        # Useful for visualization by plotting in a chart
        data_points = {}
        # On device tensors info
        on_device_meta = []

        tt_compute_count = self.assign_tensor_ids(gm)
        self.mm.log(f"Total tt compute nodes: {tt_compute_count}\n")
        i = 0
        overflow_ops = []

        nodes = list(gm.graph.nodes)
        for node in nodes:
            on_device = False
            # Has to be a ttnn op
            if is_tt_compute(node):
                self.mm.log("---------------------------------------------------\n")
                self.mm.log(f"tt compute node numbered: {i}\n")
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
                        tid, tensor_size = self.allocate(input_node)

                        ttnn_ops_tids.append(tid)
                        total_input_size += tensor_size
                        if (tid, tensor_size) not in on_device_meta:
                            on_device_meta.append((tid, tensor_size))

                if on_device:
                    tid, output_size = self.allocate(node)

                    self.mm.ops_mem_usage[node.name] = total_input_size + output_size
                    ttnn_ops_tids.append(tid)
                    self.mm.ttnn_ops_tids[node.name] = ttnn_ops_tids
                    self.mm.tids_in_sram_at[
                        node.name
                    ] = self.mm.tensors_on_device.copy()
                    self.mm.sram_usage_at[node.name] = self.mm.used_sram

                    if (tid, output_size) not in on_device_meta:
                        on_device_meta.append((tid, output_size))

                    data_points[(node.name, tid)] = on_device_meta.copy()

                    if self.mm.used_sram >= self.mm.usable_sram_limit:
                        overflow_ops.append(node)

                    self.mm.log(f"op execution on device: {node.name}\n")
                    self.mm.log(f"input size: {total_input_size} bytes\n")
                    self.mm.log(f"output size: {output_size} bytes\n")
                    self.mm.log(f"total SRAM usage: {self.mm.used_sram} bytes\n")

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
                            [ttnn.from_device, ttnn.to_torch, ttnn.to_layout]
                        ):
                            is_follow_up_from_device = True

                    # If no follow up ttnn op using the output of current node
                    # and if one of the users is a from device operation,
                    # then swap out output tensor from device
                    if not is_follow_up_tt_compute and is_follow_up_from_device:
                        tid, output_size = self.deallocate(node)
                        on_device_meta.remove((tid, output_size))

                        self.mm.log(f"op removed from device: {node.name}\n")
                        self.mm.log(f"output size: {output_size} bytes\n")
                        self.mm.log(f"total SRAM usage: {self.mm.used_sram} bytes\n")

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
                            tid, tensor_size = self.deallocate(input_node)
                            on_device_meta.remove((tid, tensor_size))

                            self.mm.log(
                                f"input tensor removed from device: {tensor_size} bytes\n"
                            )
                            self.mm.log(
                                f"total SRAM usage: {self.mm.used_sram} bytes\n"
                            )

                    # data_points[(node.name, "from_device")] = on_device_meta.copy()

        self.mm.set_peak_sram_usage()

        self.mm.log(f"Tensor IDs to address map in SRAM:\n")
        self.mm.log(f"{self.mm.tid_to_addr_map_in_sram}\n")
        self.mm.log(
            f"----------------------------------------------------------------\n"
        )
        self.mm.log(f"These ttnn ops overflow the SRAM buffer:\n")
        for op in overflow_ops:
            self.mm.log(f"{op}, ")

        self.mm.log(f"\nData captured for plotting on a chart:\n")
        for key, value in data_points.items():
            self.mm.log(f"{key}: {value}\n")

        # Convert dictionary keys to strings
        data_str_keys = {str(key): value for key, value in data_points.items()}
        self.mm.data_points = data_str_keys

        if verbose:
            print(self.mm.logs)

        return gm

    def call(self, gm: torch.fx.GraphModule):
        gm = self.memory_footprint(gm, self.verbose)
        return PassResult(gm, True)

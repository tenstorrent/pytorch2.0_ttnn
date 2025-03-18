# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
from torch_ttnn.passes.lowering.add_data_move_pass import is_tt_data_move, is_tt_compute
from torch_ttnn.utils import TtnnDevice
import ttnn
import torch

# Configs
device_name = "wormhole"
cores = 120
L1_mem = 1048576  # 1 MB
circular_buffer = 20 * 1048576  # 20 MB
# SRAM_LIMIT = cores * L1_mem - circular_buffer (100 MB in this case)


# This will manage all memory related operations & data
class MemoryManager:
    def __init__(self, device, cores, L1_mem, circular_buffer, verbose=True):
        # Config
        self.device = device
        self.cores = cores
        self.L1_mem = L1_mem
        self.circular_buffer = circular_buffer
        self.verbose = verbose
        self.total_sram_limit = self.cores * self.L1_mem
        self.free_sram = self.total_sram_limit - self.circular_buffer
        self.usable_sram_limit = self.total_sram_limit - self.circular_buffer
        self.used_sram = 0

        # Tensor memory address allocation tracker
        self.last_assigned_addr = 0
        # Tracks tensors currently in SRAM memory
        self.tensors_on_device = []
        # Each ttnn op's input & output tensor ids
        self.ttnn_ops_tids = {}
        # Current usage of SRAM memory at each step of ttnn op execution timeline
        self.sram_usage_at = {}
        # Keep tally of tensors in SRAM memory at each step of ttnn op execution timeline
        self.tids_in_sram_at = {}
        # Tensor size of respective tensors
        self.tensor_size_of = {}
        # Map of each node with its output tensor id
        self.node_to_tid_map = {}
        # Sum of input & output tensor sizes for each ttnn op
        self.ops_mem_usage = {}
        # Memory address of each tensor id in SRAM
        self.tid_to_addr_map_in_sram = {}
        # Maximum usage of SRAM during lifetime of model execution
        self.peak_sram_usage = 0
        # Data for plotting on a chart
        self.data_points = {}
        # Logs generated during memory analysis
        self.logs = ""

    def has_sram_overflow(self):
        for _, sram_usage in self.sram_usage_at.items():
            if sram_usage >= self.usable_sram_limit:
                return True
        return False

    def set_peak_sram_usage(self):
        peak_sram_usage = 0
        for _, sram_usage in self.sram_usage_at.items():
            if sram_usage > peak_sram_usage:
                peak_sram_usage = sram_usage
        self.peak_sram_usage = peak_sram_usage

    def max_evictions_required(self):
        max_evictions = 0
        for _, sram_usage in self.sram_usage_at.items():
            if sram_usage >= self.usable_sram_limit:
                max_evictions += 1
        return max_evictions

    def log(self, message: str):
        self.logs += message
        if self.verbose:
            print(message)


# This holds op related information one can query from
class OpRegistry:
    def get_tensor_shape_and_dtype(self, node):
        if is_tt_data_move(node):
            assert len(node.all_input_nodes) == 1, "Data movement operators can't have more than one input!"
            return self.get_tensor_shape_and_dtype(node.all_input_nodes[0])
        else:
            # TODO: What if meta of nth output of the node is requested?
            if isinstance(node.meta["val"], tuple):
                return (node.meta["val"][0].size(), node.meta["val"][0].dtype)
            else:
                return (node.meta["val"].size(), node.meta["val"].dtype)

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


def check_sram_overflow(mm: MemoryManager) -> bool:
    return mm.has_sram_overflow()


def which_tensors_to_evict(mm: MemoryManager) -> tuple:
    sram_usage = 0
    tensors_to_evict = []
    potential_tensors_to_evict = []
    for node_name, sram_used in mm.sram_usage_at.items():
        if sram_used >= mm.usable_sram_limit:
            sram_usage = sram_used

            # Checks if the ttnn op itself can fit in SRAM or not.
            if mm.ops_mem_usage[node_name] >= mm.usable_sram_limit:
                print(f"Splitting required, {node_name} op doesn't fit in SRAM!")
                return (node_name, -1)

            # Removes tids of current ttnn op from list of potential tensors that can be evicted
            current_op_tids = mm.ttnn_ops_tids[node_name]
            potential_tensors_to_evict = mm.tids_in_sram_at[node_name]
            for tid in current_op_tids:
                if tid in potential_tensors_to_evict:
                    potential_tensors_to_evict.remove(tid)

            # Convert list of potential tensors to evict to dict with tensor's memory size
            potential_tensors_to_evict = {tid: mm.tensor_size_of[tid] for tid in potential_tensors_to_evict}
            # Sort the dict as per tensor memory size (in decreasing order)
            potential_tensors_to_evict = {
                k: v
                for k, v in sorted(
                    potential_tensors_to_evict.items(),
                    key=lambda item: item[1],
                    reverse=True,
                )
            }
            break

    if len(potential_tensors_to_evict) > 0:
        for tid, tensor_size in potential_tensors_to_evict.items():
            sram_usage -= tensor_size
            tensors_to_evict.append(tid)
            if sram_usage < mm.usable_sram_limit:
                break

    return (node_name, tensors_to_evict)


def get_dtype_size(dtype):
    if dtype in [torch.float, torch.float32, torch.int, torch.int32]:
        return 4
    elif dtype in [torch.float64, torch.double, torch.int64, torch.long]:
        return 8
    elif dtype in [torch.float16, torch.half, torch.bfloat16, torch.int16, torch.short]:
        return 2
    else:
        assert False, "Invalid datatype! This is not supported yet."


def get_tensor_size(shape, dtype):
    size = get_dtype_size(dtype)
    for val in list(shape):
        size = val * size
    return size

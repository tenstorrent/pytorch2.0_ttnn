from torch_ttnn.passes.lowering.add_data_move_pass import is_tt_data_move, is_tt_compute
from torch_ttnn.utils import TtnnDevice
import ttnn
import torch

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
        self.circular_buffer = circular_buffer

        self.total_sram_limit = self.cores * self.L1_mem
        self.free_sram = self.total_sram_limit - self.circular_buffer
        self.usable_sram_limit = self.total_sram_limit - self.circular_buffer
        self.used_sram = 0
        self.tensors_on_device = []
        self.ttnn_ops_tids = {}
        self.sram_usage_at = {}
        self.tids_in_sram_at = {}
        self.tensor_size_of = {}
        self.node_to_tid_map = {}
        self.ops_mem_usage = {}
        self.tid_to_addr_map_in_sram = {}
        self.data_points = {}

    def has_sram_overflow(self):
        for node_name, sram_usage in self.sram_usage_at.items():
            if sram_usage >= self.usable_sram_limit:
                return True
        return False


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



def check_sram_overflow(mm: MemoryManager) -> bool:
    return mm.has_sram_overflow()


def which_tensors_to_evict(mm: MemoryManager) -> tuple:
    sram_usage = 0
    tensors_to_evict = []
    for node_name, sram_used in mm.sram_usage_at.items():
        if sram_used >= mm.usable_sram_limit:
            sram_usage = sram_used

            # Checks if the ttnn op itself can fit in SRAM or not.
            if mm.ops_mem_usage[node_name] >= mm.usable_sram_limit:
                assert False, f"Splitting required, {node_name} op doesn't fit in SRAM!"

            # Removes tids of current ttnn op from list of potential tensors that can be evicted
            current_op_tids = mm.ttnn_ops_tids[node_name]
            potential_tensors_to_evict = mm.tids_in_sram_at[node_name]
            for tid in current_op_tids:
                if tid in potential_tensors_to_evict:
                    potential_tensors_to_evict.remove(tid)

            # Convert list of potential tensors to evict to dict with tensor's memory size
            potential_tensors_to_evict = { tid: mm.tensor_size_of[tid] for tid in potential_tensors_to_evict }
            # Sort the dict as per tensor memory size (in decreasing order)
            potential_tensors_to_evict = {k: v for k, v in sorted(potential_tensors_to_evict.items(), key=lambda item: item[1], reverse=True)}
            break
    
    if len(potential_tensors_to_evict) > 0:
        for tid, tensor_size in potential_tensors_to_evict.items():
            sram_usage -= tensor_size
            tensors_to_evict.append(tid)
            if sram_usage < mm.usable_sram_limit:
                break
            
    return (node_name, tensors_to_evict)
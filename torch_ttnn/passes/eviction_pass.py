import torch
import ttnn
from torch.fx.passes.infra.pass_base import PassBase, PassResult
from torch_ttnn.passes.lowering.add_data_move_pass import is_tt_data_move, is_tt_compute

from torch_ttnn.mem_utils import *


def evict_tensors_from_device(gm: torch.fx.GraphModule, mm: MemoryManager, tensors_to_evict: list) -> torch.fx.GraphModule:

    nodes = list(gm.graph.nodes)
    print(nodes)
    for node in nodes:
        g= node.graph
        if is_tt_compute(node):
            # breakpoint()
            with g.inserting_after(node):
                tid = mm.node_to_tid_map[node]
                if tid in tensors_to_evict:
                    from_device_node = g.call_function(ttnn.from_device, (node,))
                    node.append(from_device_node)

    
    return gm


class EvictionPass(PassBase):
    def __init__(self, mm, tensors_to_evict):
        self.mm = mm
        self.tensors_to_evict = tensors_to_evict

    def call(self, gm: torch.fx.GraphModule):
        gm = evict_tensors_from_device(gm, self.mm, self.tensors_to_evict)
        return PassResult(gm, True)
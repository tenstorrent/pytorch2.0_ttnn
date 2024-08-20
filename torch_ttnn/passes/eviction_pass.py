import torch
import ttnn
from torch.fx.passes.infra.pass_base import PassBase, PassResult
from torch_ttnn.passes.lowering.add_data_move_pass import is_tt_data_move, is_tt_compute

from torch_ttnn.mem_utils import *


def evict_tensors_from_device(
    gm: torch.fx.GraphModule, mm: MemoryManager, guilty_op: str, tensors_to_evict: list
) -> torch.fx.GraphModule:
    assert len(tensors_to_evict) != 0, "Tensors to be evicted list must not be empty."
    topo_sorted_nodelist = list(gm.graph.nodes)
    print(topo_sorted_nodelist)

    for node in topo_sorted_nodelist:
        # The node whose output tensor needs to be evicted
        tid = -1  # For init
        # breakpoint()
        if node in mm.node_to_tid_map:
            tid = mm.node_to_tid_map[node]
        if tid in tensors_to_evict:
            assert (
                node.name != guilty_op
            ), "Op which overflows the SRAM can't have its output tensor evicted from device"
            evict_node = node
            evict_node_users = list(evict_node.users.keys())

        g = node.graph

        if is_tt_compute(node) and node.name == guilty_op:
            with g.inserting_before(node):
                from_device_node = g.call_function(ttnn.from_device, args=(evict_node,))

            with g.inserting_after(node):
                device = TtnnDevice()
                to_device_node = g.call_function(
                    ttnn.to_device, (from_device_node, device)
                )

            assert (
                evict_node is not None and evict_node_users != []
            ), "Evicted node should be there."
            # For users of evict node, if it topologically comes after the evict node:
            # then update the user's argument (input) to be "to_device node"
            for user in evict_node_users:
                if topo_sorted_nodelist.index(user) > topo_sorted_nodelist.index(node):
                    for input in user.all_input_nodes:
                        if input == evict_node:
                            index = user.all_input_nodes.index(input)
                            user.update_arg(index, to_device_node)
            evict_node = None
            evict_node_users = []

    print(list(gm.graph.nodes))
    return gm


class EvictionPass(PassBase):
    def __init__(self, mm, guilty_op, tensors_to_evict):
        self.mm = mm
        self.guilty_op = guilty_op
        self.tensors_to_evict = tensors_to_evict

    def call(self, gm: torch.fx.GraphModule):
        gm = evict_tensors_from_device(
            gm, self.mm, self.guilty_op, self.tensors_to_evict
        )
        return PassResult(gm, True)

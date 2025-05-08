# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import ttnn
from torch.fx.passes.infra.pass_base import PassBase, PassResult
from torch.fx.node import Node, map_arg
from .lowering import target_wrappers
import operator

from typing import Dict, List


@torch.fx.wrap
def deallocate(tensor):
    if isinstance(tensor, ttnn.Tensor):
        tensor.deallocate()
    return None


class TrackUnusedValues:
    """
    Adapted from CodeGen._gen_python_code in pytorch/torch/fx/graph.py
    Given a graph, tracks the last uses of each node in order to
    deallocate them appropriately. This is important for TTNN graphs because
    of limited L1 memory.

    Methods
    -------
    get_nodes_to_delete(user=""):
        Given a user, returns a list of nodes to deallocate

    Usage
    unused_values = TrackUnusedValues(graph)
    for node in graph.nodes:
        to_delete_nodes = unused_values.get_nodes_to_delete(node)
    """

    def __init__(self, graph):
        node_to_last_use: Dict[Node, Node] = {}
        self._user_to_last_uses: Dict[Node, List[Node]] = {}

        def register_last_uses(n: Node, user: Node):
            if n not in node_to_last_use:
                node_to_last_use[n] = user
                self._user_to_last_uses.setdefault(user, []).append(n)

        for node in reversed(graph.nodes):
            map_arg(node.args, lambda n: register_last_uses(n, node))
            map_arg(node.kwargs, lambda n: register_last_uses(n, node))

    def get_nodes_to_delete(self, user: Node):
        """
        Delete values after their last use. This ensures that values that are
        not used in the remainder of the code are freed and the memory usage
        of the code is optimal. Returns a string of all the values to delete.
        Returns an empty string if none.
        """
        if user.op == "placeholder":
            return None
        if user.op == "output":
            return None
        nodes_to_delete = self._user_to_last_uses.get(user, [])

        if len(user.users.keys()) == 0:
            # This node is not used by any others. however it's also not
            # removed by DCE since side-effect. We want to free it's outputs
            # right after its execution done to save memory.
            nodes_to_delete.append(user)

        if len(nodes_to_delete):
            return nodes_to_delete
        else:
            return None


class DeallocationPass(PassBase):
    def __init__(self):
        super().__init__()

    def call(self, gm: torch.fx.GraphModule):
        graph = gm.graph

        unused_values = TrackUnusedValues(graph)

        modified = False

        # Because we are inserting new nodes after the target node, we cannot iterate
        # through the graph nodes directly. Otherwise, we will get an infinite loop.
        # Instead we create a new list and iterate through that.
        node_list = list(graph.nodes)
        for node in node_list:
            if (to_delete_nodes := unused_values.get_nodes_to_delete(node)) is not None:
                for n in to_delete_nodes:
                    # Skip nodes that are references to other nodes
                    # We don't want to delete these too early
                    if node.target in [target_wrappers.pack_to_tuple, operator.getitem]:
                        continue
                    with graph.inserting_after(node):
                        new_node = graph.call_function(deallocate, args=(n,))
                        modified = True

        if modified:
            # Becareful about dead code elimination at this point
            gm.graph.lint()
            gm.recompile()

        return PassResult(gm, True)

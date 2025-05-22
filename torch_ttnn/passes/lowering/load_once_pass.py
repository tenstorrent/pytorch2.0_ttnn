# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import pickle
import torch
from torch_ttnn.passes.analysis.graph_module_analysis_pass import ModelType
from torch_ttnn.passes.analysis.input_analysis_pass import PrimalTag
from torch_ttnn.utils import GraphCleanup
from operator import getitem

from torch.fx.passes.infra.pass_base import PassBase, PassResult
from . import target_wrappers


def mark_nodes_invariant(nodes):
    seen_nodes = set()

    def mark_descendants_varied(node):
        if node in seen_nodes:
            return

        node.meta["iteration_invariant"] = False
        seen_nodes.add(node)

        for user in node.users:
            mark_descendants_varied(user)

    for node in nodes:
        node.meta["iteration_invariant"] = True
    for node in filter(lambda n: n.op == "placeholder" and n.meta.get("primal_tag") == PrimalTag.ARGUMENT, nodes):
        # mark all descendents as not iteration_invariant
        mark_descendants_varied(node)
    for node in filter(lambda n: n.op == "output", nodes):
        # make sure all output nodes are marked as variable
        node.meta["iteration_invariant"] = False


class NodeMover:
    def __init__(self, graph):
        self.graph = graph
        self.node_to_run_once_idx = dict()
        self.node_to_returned_idx = dict()
        self.run_once_inputs = []

        nodes = self.graph.nodes
        self.first_node = [node for node in nodes if node.op != "placeholder"][0]

    def move(self, node):
        assert node.meta.get("iteration_invariant") == True
        if node.op == "placeholder":
            return 0

        self.node_to_run_once_idx[node] = len(self.node_to_run_once_idx)
        # if any users are variable, return too
        should_return = False
        if any([n.meta.get("iteration_invariant", False) == False for n in node.users]):
            should_return = True
            self.node_to_returned_idx[node] = len(self.node_to_returned_idx)

        run_once_idx = target_wrappers.RunOnceIdx(self.node_to_run_once_idx[node])
        run_once_idx = pickle.dumps(run_once_idx)
        users = node.users.copy()
        for user in users:
            if user.meta.get("iteration_invariant") != True:
                continue
            if node in user.args:
                user_idx = user.args.index(node)
                new_args = list(user.args)
                new_args[user_idx] = run_once_idx
                user.args = tuple(new_args)

            new_kwargs = user.kwargs.copy()
            for k, v in user.kwargs.items():
                if v == node:
                    new_kwargs[k] = run_once_idx
            user.kwargs = new_kwargs

        if hasattr(node.target, "python_fully_qualified_name"):
            fn_call = node.target.python_fully_qualified_name
        elif node.target.__module__ == "torch_ttnn.passes.lowering.target_wrappers":
            fn_call = node.target.__qualname__
        else:
            fn_call = f"{node.target.__module__}.{node.target.__qualname__}"

        self.run_once_inputs.append((should_return, fn_call, node.args, node.kwargs))
        return 1

    def rewrite_users(self, ttnn_inputs):
        with self.graph.inserting_before(self.first_node):
            for node, idx in self.node_to_returned_idx.items():
                getitem_call = self.graph.call_function(getitem, (ttnn_inputs, idx))
                getitem_call.meta["is_cached"] = True
                # replace all varying users with getitem call
                node.replace_all_uses_with(
                    getitem_call, delete_user_cb=lambda node: node.meta.get("iteration_invariant") == False
                )

    def create_load_once(self):
        if len(self.run_once_inputs) == 0:
            return

        with self.graph.inserting_before(self.first_node):
            ttnn_inputs = self.graph.call_function(
                target_wrappers.run_once,
                tuple(self.run_once_inputs),
            )

        self.rewrite_users(ttnn_inputs)


class LoadOncePass(PassBase):
    """Pass that moves as many operations as possible into the load_once function so they will be cached for later runs.

    This pass only runs for end to end inference models.

    :param is_end_to_end: Whether the input GraphModule is converted end to end.
    """

    def __init__(self, is_end_to_end):
        self.is_end_to_end = is_end_to_end

    def call(self, gm: torch.fx.GraphModule):
        if (not self.is_end_to_end) or gm.meta.get("graph_type") != ModelType.INFERENCE:
            modified = False
            return PassResult(gm, modified)

        modifications_count = 0

        # first make sure all nodes are marked as constant or variable (infected by arguments)
        nodes = list(gm.graph.nodes)
        mark_nodes_invariant(nodes)

        # move all constant nodes into run_once and rewrite users
        node_mover = NodeMover(gm.graph)
        for constant_node in filter(lambda n: n.meta.get("iteration_invariant", False), nodes):
            modifications_count += node_mover.move(constant_node)
        node_mover.create_load_once()

        modified = modifications_count > 0
        GraphCleanup(gm)
        return PassResult(gm, modified)

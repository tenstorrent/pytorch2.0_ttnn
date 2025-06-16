# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import inspect
import pickle
import torch
import ttnn
from torch_ttnn.passes.analysis.graph_module_analysis_pass import ModelType
from torch_ttnn.passes.analysis.input_analysis_pass import PrimalTag
from torch_ttnn.passes.deallocation_pass import deallocate
from torch_ttnn.utils import GraphCleanup, TtnnDevice, TtnnBfloat16, TtnnUint32, TtnnTileLayout, get_dtype
from torch_ttnn import mem_utils
from operator import getitem

from torch.fx.passes.infra.pass_base import PassBase, PassResult
from . import target_wrappers


def mark_nodes_invariant(nodes):
    seen_nodes = set()

    def mark_descendants_varied(node_list):
        while len(node_list) > 0:
            node = node_list[-1]
            node_list = node_list[:-1]
            if node in seen_nodes:
                continue

            node.meta["iteration_invariant"] = False
            seen_nodes.add(node)

            node_list += node.users

    for node in nodes:
        node.meta["iteration_invariant"] = True
    for node in filter(lambda n: n.op == "placeholder" and n.meta.get("primal_tag") == PrimalTag.ARGUMENT, nodes):
        # mark all descendents as not iteration_invariant
        mark_descendants_varied([node])
    for node in filter(lambda n: n.op in ["output", "get_attr", "root"], nodes):
        # make sure all outputs, roots, and get_attr nodes are marked as variable
        mark_descendants_varied([node])

    # mark deallocations variable if we will return a given node so they aren't moved into run_once
    for node in filter(lambda n: n.meta.get("iteration_invariant") == True, nodes):
        will_return = any([n.meta.get("iteration_invariant", False) == False for n in node.users])
        if will_return:
            dealloc_nodes = filter(lambda n: n.op == "call_function" and n.target == deallocate, node.users)
            for dealloc_node in dealloc_nodes:
                dealloc_node.meta["iteration_invariant"] = False


def check_dram_overflow(nodes, device):
    # TODO: this implementation is very naive (doesn't model memory fragmentation for example). It should be a better proxy for memory usage, should model DRAM and SRAM, should model memory padding, and should maybe be made into its own reusable pass in the future

    used_dram = 0
    dram_size = mem_utils.get_dram_size(device)
    max_dram_usage = 0

    op_registry = mem_utils.OpRegistry()

    def update_dram_usage(node, used_dram, max_dram_usage):
        if node.op == "get_attr":
            return (used_dram, max_dram_usage)

        tensor_shape, tensor_dtype = op_registry.get_tensor_shape_and_dtype(node)
        tensor_size = mem_utils.get_tensor_size(tensor_shape, tensor_dtype)
        if node.op == "call_function" and node.target == deallocate:
            used_dram -= tensor_size
        else:
            used_dram += tensor_size
        max_dram_usage = max(max_dram_usage, used_dram)
        return (used_dram, max_dram_usage)

    # first, mark all nodes that will return as live
    for node in filter(lambda n: n.meta.get("iteration_invariant") == True, nodes):
        used_dram, max_dram_usage = update_dram_usage(node, used_dram, max_dram_usage)

    # early check to skip further liveness analysis
    if max_dram_usage > dram_size:
        return True

    # next, model liveness of nodes that are not iteration_invariant (alloc and dealloc)
    for node in filter(lambda n: n.meta.get("iteration_invariant", False) == False, nodes):
        if node.op in ["output", "root", "get_attr"]:
            # assume these do not contribute to usage
            continue
        used_dram, max_dram_usage = update_dram_usage(node, used_dram, max_dram_usage)

    return max_dram_usage > dram_size


class NodeMover:
    def __init__(self, graph):
        self.graph = graph
        self.node_to_run_once_idx = dict()
        self.node_to_returned_idx = dict()
        self.run_once_inputs = []

        nodes = self.graph.nodes
        self.first_node = next(
            filter(
                lambda node: node.op != "placeholder"
                and (node.op != "call_function" or node.target != ttnn.from_torch),
                nodes,
            )
        )

    def move(self, node):
        assert node.meta.get("iteration_invariant") == True
        if node.op in ["placeholder", "get_attr", "output", "root"]:
            return 0

        self.node_to_run_once_idx[node] = len(self.node_to_run_once_idx)
        # if any users are variable, return too
        should_return = False
        if any([n.meta.get("iteration_invariant", False) == False for n in node.users]):
            should_return = True
            self.node_to_returned_idx[node] = len(self.node_to_returned_idx)

        run_once_idx = target_wrappers.RunOnceIdx(self.node_to_run_once_idx[node])
        run_once_idx = pickle.dumps(run_once_idx)
        node.replace_all_uses_with(
            run_once_idx, delete_user_cb=lambda node: node.meta.get("iteration_invariant") == True
        )

        if hasattr(node.target, "python_fully_qualified_name"):
            fn_call = node.target.python_fully_qualified_name
        elif node.target.__module__ in [
            "torch_ttnn.passes.lowering.target_wrappers",
            "torch_ttnn.passes.deallocation_pass",
        ]:
            fn_call = node.target.__qualname__
        elif node.target.__module__ == "torch._ops.aten":
            fn_call = f"torch.ops.aten.{node.target.__name__}"
        elif node.target.__module__ == "ttnn.distributed.distributed":
            fn_call = f"ttnn.{node.target.__name__}"
        elif inspect.isbuiltin(node.target):
            fn_call = node.target.__name__
        else:
            fn_call = f"{node.target.__module__}.{node.target.__qualname__}"

        self.run_once_inputs.append((should_return, fn_call, node.args, node.kwargs))
        return 1

    def move_conv(self, node):
        new_args = list(node.args)
        modified_count = 0

        # rewrite input because otherwise it is not defined when run_once is called
        input_node = node.args[0]
        tensor_shape = list(input_node.meta["val"].shape)
        spec_dtype = TtnnBfloat16
        if get_dtype(input_node) in [torch.int32, torch.int64]:
            spec_dtype = TtnnUint32
        # currently, all conv inputs are tiled and on device. If this changes, may need further analysis here
        mocked_input_node = (
            False,
            "ttnn.ones",
            (),
            {"shape": tensor_shape, "device": TtnnDevice(), "dtype": spec_dtype(), "layout": TtnnTileLayout()},
        )
        mocked_input_node_idx = len(self.run_once_inputs)
        self.run_once_inputs.append(mocked_input_node)
        input_node_idx = target_wrappers.RunOnceIdx(mocked_input_node_idx)
        new_args[0] = pickle.dumps(input_node_idx)

        should_preprocess = False

        # rewrite weight and optional bias as RunOnceIdx values
        weight_node = node.args[1]
        if weight_node.meta.get("iteration_invariant", False):
            should_preprocess = True
            weight_node_idx = target_wrappers.RunOnceIdx(self.node_to_run_once_idx[weight_node])
            new_args[1] = pickle.dumps(weight_node_idx)
            modified_count += 1

        bias_node = node.args[2]
        if bias_node is not None and bias_node.meta.get("iteration_invariant", False):
            should_preprocess = True
            bias_node_idx = target_wrappers.RunOnceIdx(self.node_to_run_once_idx[bias_node])
            new_args[2] = pickle.dumps(bias_node_idx)
            modified_count += 1

        if not should_preprocess:
            # only preprocess if weight or optional bias are iteration invariant
            return 0

        new_args = tuple(new_args)

        # update kwargs to return weights and bias
        new_kwargs = node.kwargs.copy()
        new_kwargs["return_weights_and_bias"] = True

        should_return = False
        fn_call = "conv"

        self.run_once_inputs.append((should_return, fn_call, new_args, new_kwargs))
        return modified_count

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

        global run_once_count
        target_wrappers.run_once_count = 0

        if len(self.run_once_inputs) > 0:
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

    def __init__(self, option):
        self.option = option

    def call(self, gm: torch.fx.GraphModule):
        if (
            (not self.option._is_end_to_end)
            or (not self.option.load_params_once)
            or self.option.graph_type != ModelType.INFERENCE
        ):
            modified = False
            return PassResult(gm, modified)

        modifications_count = 0

        # first make sure all nodes are marked as constant or variable (infected by arguments)
        nodes = list(gm.graph.nodes)
        mark_nodes_invariant(nodes)

        # guard against DRAM overflow - return if we would
        if check_dram_overflow(nodes, self.option.device):
            return PassResult(gm, modified=False)

        # move all constant nodes into run_once and rewrite users
        node_mover = NodeMover(gm.graph)
        for constant_node in filter(lambda n: n.meta.get("iteration_invariant", False), nodes):
            modifications_count += node_mover.move(constant_node)

        # add convolutions to preprocess weights and biases
        for conv_node in filter(lambda n: n.op == "call_function" and n.target == target_wrappers.conv, nodes):
            modifications_count += node_mover.move_conv(conv_node)

        node_mover.create_load_once()

        modified = modifications_count > 0
        GraphCleanup(gm)
        return PassResult(gm, modified)

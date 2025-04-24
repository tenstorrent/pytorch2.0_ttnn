# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
from torch._guards import detect_fake_mode
from torch.fx.passes.infra.pass_base import PassBase, PassResult
from torch_ttnn.passes.lowering import target_wrappers
from torch_ttnn.passes.analysis.input_analysis_pass import PrimalTag

import math

import ttnn


class GraphWrapper:
    def __init__(self, gm, node, device):
        self.graph = node.graph

    def call_function(self, target, args=(), kwargs={}):
        new_node = self.graph.call_function(target, args, kwargs)
        return new_node

    def inserting_before(self, node):
        return self.graph.inserting_before(node)

    def inserting_after(self, node):
        return self.graph.inserting_after(node)


class MultiDevicePass(PassBase):
    def __init__(self, device, example_inputs):
        super().__init__()

        self.device = device
        self.example_inputs = example_inputs

    def replicate_to_mesh(self, graph_wrapper: GraphWrapper, node):
        with graph_wrapper.inserting_after(node):
            new_node = graph_wrapper.call_function(target_wrappers.replicate_tensor, (node,))
            node.replace_all_uses_with(new_node, delete_user_cb=lambda node: node != new_node and node.op != "output")

    def shard_to_mesh(self, graph_wrapper: GraphWrapper, node):
        batch_dimension = 0
        with graph_wrapper.inserting_after(node):
            new_node = graph_wrapper.call_function(
                target_wrappers.shard_tensor, (node, batch_dimension, self.device.get_num_devices())
            )
            node.replace_all_uses_with(new_node, delete_user_cb=lambda node: node != new_node)

    def concat_to_tensor(self, graph_wrapper: GraphWrapper, node):
        new_arg_list = []
        batch_dimension = 0
        with graph_wrapper.inserting_before(node):
            for arg_node in node.args[0]:
                # only concat sharded nodes
                if arg_node.meta.get("is_sharded", False) is False:
                    new_arg = arg_node
                else:
                    new_arg = graph_wrapper.call_function(
                        target_wrappers.concat_tensor, (arg_node, batch_dimension, self.device.get_num_devices())
                    )
                new_arg_list.append(new_arg)

            new_node = graph_wrapper.graph.create_node("output", target="output", args=(new_arg_list,))
            node.replace_all_uses_with(new_node)
        graph_wrapper.graph.erase_node(node)

    def rewrite_const_args(self, node):
        if node.meta.get("is_sharded", False) == False:
            return

        def get_sharded_size(concat_dim_size, node):
            num_devices = self.device.get_num_devices()
            # handle case where we have combined dimensions (in torch.view for example)
            shard_dim_size = concat_dim_size / node.meta["concat_size"]
            num_shards_per_device = math.ceil(node.meta["concat_size"] / num_devices)
            return int(shard_dim_size * num_shards_per_device)

        new_args = list(node.args)
        rewrite_arg_idx = 1
        output_dim = new_args[rewrite_arg_idx].copy()
        output_dim[node.meta["shard_dim"]] = get_sharded_size(output_dim[node.meta["shard_dim"]], node)
        new_args[rewrite_arg_idx] = output_dim

        node.args = tuple(new_args)

    def call(self, graph_module: torch.fx.GraphModule):
        if not isinstance(self.device, ttnn.MeshDevice) or self.device.get_num_devices() == 1:
            modified = False
            return PassResult(graph_module, modified)

        node_list = list(graph_module.graph.nodes)
        for node in node_list:
            wrapper = GraphWrapper(graph_module, node, self.device)
            if node.op == "placeholder":
                try:
                    if (node.meta["primal_tag"] == PrimalTag.PARAMETER) or (
                        node.meta["primal_tag"] == PrimalTag.BUFFER
                    ):
                        self.replicate_to_mesh(wrapper, node)
                    elif node.meta["primal_tag"] == PrimalTag.ARGUMENT:
                        self.shard_to_mesh(wrapper, node)
                except Exception as e:
                    print(f"Warning: Could not distribute node {node.name}: {e}")

            elif node.op == "output":
                try:
                    self.concat_to_tensor(wrapper, node)
                except Exception as e:
                    print(f"Warning: Could not concat node {node.name}: {e}")

            elif node.op == "call_function":
                if node.target == torch.ops.aten.view.default:
                    self.rewrite_const_args(node)
                elif node.target == torch.ops.aten._unsafe_view.default:
                    self.rewrite_const_args(node)
                elif node.target == torch.ops.aten.expand.default:
                    self.rewrite_const_args(node)

        fake_mode = detect_fake_mode(self.example_inputs)
        # propagate meta["val"]
        torch.fx.passes.fake_tensor_prop.FakeTensorProp(graph_module, mode=fake_mode).propagate(*self.example_inputs)
        # propagate meta["tensor_meta"]
        torch.fx.passes.shape_prop.ShapeProp(graph_module, fake_mode=fake_mode).propagate(*self.example_inputs)

        modified = True
        return PassResult(graph_module, modified)

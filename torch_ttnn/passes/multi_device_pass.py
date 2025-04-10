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
        self.gm = gm
        self.g = node.graph
        self.graph = node.graph
        self.node = node
        self.device = device

    def call_function(self, target, args=(), kwargs={}):
        new_node = self.g.call_function(target, args, kwargs)

        return new_node

    def inserting_before(self, node):
        return self.g.inserting_before(node)

    def inserting_after(self, node):
        return self.g.inserting_after(node)

    def _get_val(self, obj):
        if not isinstance(obj, torch.fx.node.Node):
            return obj
        if obj.op == "get_attr":
            val = getattr(self.gm, obj.target)
            fake_mode = detect_fake_mode()
            if isinstance(val, torch.Tensor) and fake_mode is not None:
                val = fake_mode.fake_tensor_converter.from_real_tensor(fake_mode, val)
            return val
        return obj.meta["val"]


class MultiDevicePass(PassBase):
    def __init__(self, device, n_parameters, n_buffers, n_arguments, gm, example_inputs):
        super().__init__()

        self.device = device

        self.n_distributed = n_parameters + n_buffers
        self.n_sharded = n_arguments
        self.gm = gm
        self.example_inputs = example_inputs

        self.mapper = None
        self.replicator = None
        self.composer = None

    def call(self, gm: torch.fx.GraphModule):
        if not isinstance(self.device, ttnn._ttnn.multi_device.MeshDevice):
            modified = False
            return PassResult(gm, modified)

        node_list = list(gm.graph.nodes)
        for node in node_list:
            g = GraphWrapper(gm, node, self.device)
            if node.op == "placeholder":
                try:
                    if (node.meta["primal_tag"] == PrimalTag.PARAMETER) or (
                        node.meta["primal_tag"] == PrimalTag.BUFFER
                    ):
                        self.replicate_to_mesh(g, node)
                    elif node.meta["primal_tag"] == PrimalTag.ARGUMENT:
                        self.shard_to_mesh(g, node)
                except Exception as e:
                    print(f"Warning: Could not shard node {node.name}: {e}")

            elif node.op == "output":
                try:
                    self.concat_to_tensor(g, node)
                except Exception as e:
                    print(f"Warning: Could not concat node {node.name}: {e}")

            elif node.op == "call_function":
                if node.target == torch.ops.aten.view.default:
                    self.rewrite_const_args(gm, node)
                elif node.target == torch.ops.aten._unsafe_view.default:
                    self.rewrite_const_args(gm, node)
                elif node.target == torch.ops.aten.expand.default:
                    self.rewrite_const_args(gm, node)

            else:
                pass

        fake_mode = detect_fake_mode(self.example_inputs)
        # propagate meta["val"]
        torch.fx.passes.fake_tensor_prop.FakeTensorProp(gm, mode=fake_mode).propagate(*self.example_inputs)
        # propagate meta["tensor_meta"]
        torch.fx.passes.shape_prop.ShapeProp(gm, fake_mode=fake_mode).propagate(*self.example_inputs)

        modified = True
        return PassResult(gm, modified)

    def replicate_to_mesh(self, gm: torch.fx.GraphModule, node):
        with gm.inserting_after(node):
            new_node = gm.call_function(target_wrappers.replicate_tensor, (node,))
            node.replace_all_uses_with(new_node, delete_user_cb=lambda node: node != new_node and node.op != "output")

    def shard_to_mesh(self, gm: torch.fx.GraphModule, node):
        batch_dimension = 0
        with gm.inserting_after(node):
            new_node = gm.call_function(
                target_wrappers.shard_tensor, (node, batch_dimension, self.device.get_num_devices())
            )
            node.replace_all_uses_with(new_node, delete_user_cb=lambda node: node != new_node)

        # # mark all transitive users as sharded
        # new_node.meta["is_sharded"] = True
        # seen = set(new_node.users.keys())
        # user_list = list(seen)
        # while len(user_list) > 0:
        #     n = user_list.pop(-1)
        #     n.meta["is_sharded"] = True
        #     users = set(n.users.keys()) - seen
        #     seen |= users
        #     user_list += list(users)

    def concat_to_tensor(self, gm: torch.fx.GraphModule, node):
        new_arg_list = []
        batch_dimension = 0
        with gm.inserting_before(node):
            for arg_node in node.args[0]:
                # only concat sharded nodes
                if arg_node.meta.get("is_sharded", False) is False:
                    new_arg = arg_node
                else:
                    # change the node so we get the right metadata
                    gm.node = arg_node
                    new_arg = gm.call_function(
                        target_wrappers.concat_tensor, (arg_node, batch_dimension, self.device.get_num_devices())
                    )
                new_arg_list.append(new_arg)

            new_node = gm.graph.create_node("output", target="output", args=(new_arg_list,))
            node.replace_all_uses_with(new_node)
        gm.graph.erase_node(node)

    def rewrite_const_args(self, gm: torch.fx.GraphModule, node):
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

# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
from torch._guards import detect_fake_mode
import torch_ttnn.metrics as metrics
from torch._subclasses.fake_tensor import unset_fake_temporarily
from torch.fx.passes.infra.pass_base import PassBase, PassResult
from torch_ttnn.utils import GraphCleanup, TtnnDevice
from torch_ttnn.passes.lowering import target_wrappers
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
        # new_node.meta = dict(self.node.meta)
        # if hasattr(self.node.target, "_schema"):
        #     new_node.meta["original_input_variations"] = metrics.collect_input_variation_from_node(self.node)
        # new_node.meta["val"] = self._get_val(new_node)
        #
        # # fixup val for sharding
        # if target == target_wrappers.shard_tensor:
        #     num_devices = self.device.get_num_devices()
        #     batch_dimension = 0
        #     new_node.meta["val"] = torch.chunk(new_node.meta["val"], num_devices, dim=batch_dimension)[0]
        #     new_node.meta["tensor_meta"] = torch.fx.passes.shape_prop._extract_tensor_metadata(new_node.meta["val"])
        #
        #     # recursively fix users
        #     print("here")
        #
        #     # batch_dimension = 0
        #     # output_tensor = new_node.meta["val"]
        #     # output_shape = list(output_tensor.size())
        #     # num_devices = math.prod(self.device.shape)
        #     # output_shape[batch_dimension] = int((output_shape[batch_dimension]+num_devices-1)//num_devices)
        #     # result_tensor = output_tensor.new_empty(output_shape)
        # new_node.meta["val"] = result_tensor

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
            return PassResult(gm, False)

        # rewrite with wrappers
        placeholder_counter = 0
        for node in gm.graph.nodes:
            g = GraphWrapper(gm, node, self.device)
            if node.op == "placeholder":
                try:
                    if placeholder_counter < self.n_distributed:
                        self.replicate_to_mesh(g, node)
                    else:
                        self.shard_to_mesh(g, node)
                except Exception as e:
                    print(f"Warning: Could not shard node {node.name}: {e}")
                finally:
                    placeholder_counter += 1

            elif node.op == "output":
                try:
                    self.concat_to_tensor(g, node)
                except Exception as e:
                    print(f"Warning: Could not concat node {node.name}: {e}")
            else:
                pass

        fake_mode = detect_fake_mode(self.example_inputs)
        # propagates meta["val"]
        torch.fx.passes.fake_tensor_prop.FakeTensorProp(gm, mode=fake_mode).propagate(*self.example_inputs)
        # propagates meta["tensor_meta"]
        torch.fx.passes.shape_prop.ShapeProp(gm, fake_mode=fake_mode).propagate(*self.example_inputs)

        # # convert wrappers to actual calls
        # def rewrite_wrappers(g, node):
        #     if node.target == target_wrappers.replicate_tensor:
        #         rep = g.call_function(ttnn.ReplicateTensorToMesh, args=(TtnnDevice(),))
        #         return g.call_function(
        #             ttnn.from_torch, args=node.args, kwargs={"mesh_mapper": rep, "device": TtnnDevice()}
        #         )
        #     if node.target == target_wrappers.shard_tensor:
        #         inp_node, shard_dim, _ = node.args
        #         rep = g.call_function(ttnn.ShardTensorToMesh, args=(TtnnDevice(),), kwargs={"dim": shard_dim})
        #         return g.call_function(
        #             ttnn.from_torch, args=(inp_node,), kwargs={"mesh_mapper": rep, "device": TtnnDevice()}
        #         )
        #
        #     if node.target == target_wrappers.concat_tensor:
        #         inp_node, shard_dim, _ = node.args
        #         rep = g.call_function(ttnn.ConcatMeshToTensor, args=(TtnnDevice(),), kwargs={"dim": shard_dim})
        #         return g.call_function(
        #             ttnn.to_torch, args=(inp_node,), kwargs={"mesh_composer": rep, "device": TtnnDevice()}
        #         )
        #
        #     return None
        #
        # node_list = [node for node in gm.graph.nodes]
        #
        # for node in node_list:
        #     g = GraphWrapper(gm, node, self.device)
        #     with g.inserting_before(node):
        #         new_node = rewrite_wrappers(g, node)
        #         if new_node is not None:
        #             node.replace_all_uses_with(new_node, delete_user_cb=lambda node: node != new_node)
        # gm = GraphCleanup(gm)

        return PassResult(gm, True)

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

        # mark all transitive users as sharded
        new_node.meta["is_sharded"] = True
        seen = set(new_node.users.keys())
        user_list = list(seen)
        while len(user_list) > 0:
            n = user_list.pop(-1)
            n.meta["is_sharded"] = True
            users = set(n.users.keys()) - seen
            seen |= users
            user_list += list(users)

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

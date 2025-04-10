# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
from torch._subclasses.fake_tensor import unset_fake_temporarily
from torch.fx.passes.infra.pass_base import PassBase, PassResult
from torch_ttnn.utils import TtnnDevice
from torch_ttnn.passes.analysis.input_analysis_pass import PrimalTag

import ttnn
from enum import Enum

seen = []


def propagate_sharding_to_users(node, shard_dim, concat_size, seen_set):
    global seen
    seen.append(node)

    if node.op == "output" or (seen_set is not None and node in seen_set):
        return

    seen_set.add(node)

    node.meta["is_sharded"] = True

    # permute changes which dimension is sharded
    if node.target == torch.ops.aten.permute.default:
        shard_dim = node.args[1].index(shard_dim)

    node.meta["shard_dim"] = shard_dim

    # if any ops change the size after concatenating all shards, adjust here
    node.meta["concat_size"] = concat_size

    for user in node.users:
        propagate_sharding_to_users(user, shard_dim, concat_size, seen_set)


class MultiDeviceShardAnalysisPass(PassBase):
    def __init__(self, device):
        super().__init__()

        self.device = device

    def call(self, gm: torch.fx.GraphModule):
        if not isinstance(self.device, ttnn._ttnn.multi_device.MeshDevice):
            modified = False
            return PassResult(gm, modified)

        node_list = list(gm.graph.nodes)
        for node in node_list:
            if node.op == "placeholder" and node.meta.get("primal_tag") == PrimalTag.ARGUMENT:
                shard_dim = 0
                concat_size = node.meta["val"].shape[shard_dim]
                propagate_sharding_to_users(node, shard_dim=shard_dim, concat_size=concat_size, seen_set=set())

        modified = False
        return PassResult(gm, modified)

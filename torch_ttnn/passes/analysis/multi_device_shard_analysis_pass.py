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


def propagate_sharding_to_users(node, shard_dim):
    if node.op == "output":
        return

    node.meta["is_sharded"] = True

    # permute changes which dimension is sharded
    if node.target == torch.ops.aten.permute.default:
        shard_dim = node.args[0].index(shard_dim)

    node.meta["shard_dim"] = shard_dim

    for user in node.users:
        propagate_sharding_to_users(user, shard_dim)


class MultiDeviceShardAnalysisPass(PassBase):
    def __init__(self):
        super().__init__()

    def call(self, gm: torch.fx.GraphModule):
        modified = False

        node_list = list(gm.graph.nodes)
        for node in node_list:
            if node.op == "placeholder" and node.meta.get("primal_tag") == PrimalTag.ARGUMENT:
                propagate_sharding_to_users(node, shard_dim=0)

        return PassResult(gm, modified)

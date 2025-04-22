# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import ttnn

from torch.fx.passes.infra.pass_base import PassBase, PassResult


class EnableBinaryNgPass(PassBase):
    def call(self, gm: torch.fx.GraphModule):
        modified = False
        ops_to_rewrite = [
            ttnn.add,
            ttnn.sub,
            ttnn.mul,
            ttnn.div,
            ttnn.rsub,
            ttnn.eq,
            ttnn.ne,
            ttnn.gt,
            ttnn.ge,
            ttnn.lt,
            ttnn.le,
            ttnn.squared_difference,
            ttnn.bias_gelu,
        ]

        for node in gm.graph.nodes:
            # Only process ttnn.permute and ttnn.reshape
            if node.op != "call_function":
                continue
            if node.target not in ops_to_rewrite:
                continue

            print("!!! rewritten")
            new_kwargs = node.kwargs.copy()
            new_kwargs["use_legacy"] = False
            node.kwargs = new_kwargs
            modified = True

        return PassResult(gm, modified)

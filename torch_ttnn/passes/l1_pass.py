# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
from torch.fx.passes.infra.pass_base import PassBase, PassResult
from torch_ttnn.utils import TtnnL1MemoryConfig, TtnnFullCoreGrid
import ttnn


class L1Pass(PassBase):
    def __init__(self):
        super().__init__()

    def call(self, gm: torch.fx.GraphModule):
        """Marks inputs for the compiled function as parameters, buffers, or arguments.

        This relies on how PyTorch behaves under the hood. Namely, PyTorch will lay out function arguments in the order of parameters, then buffers, then arguments. We can rely on this layout order and the number of parameters, buffers, and arguments passed in from AOTAutograd to our backend function.

        :param gm: Graph module for the function being compiled.
        :return: Pass result with the updated graph module and whether the graph was modified.
        :rtype: PassResult[torch.fx.GraphModule, bool]
        """

        def make_l1(node):
            new_kwargs = node.kwargs.copy()
            new_kwargs["memory_config"] = TtnnL1MemoryConfig()
            node.kwargs = new_kwargs

        def make_core_grid_full(node):
            new_kwargs = node.kwargs.copy()
            new_kwargs["core_grid"] = TtnnFullCoreGrid()
            node.kwargs = new_kwargs

        modified = False

        node_list = list(gm.graph.nodes)
        for node in node_list:
            if node.op != "call_function":
                continue

            if node.target in [
                ttnn.from_torch,
                ttnn.linear,
                ttnn.matmul,
                ttnn.transformer.split_query_key_value_and_split_heads,
                ttnn.transformer.concatenate_heads,
                ttnn.add,
                ttnn.global_avg_pool2d,
                ttnn.untilize_with_unpadding,
                ttnn.tilize_with_val_padding,
                ttnn.subtract,
                ttnn.relu,
                ttnn.reshape,
                ttnn.permute,
                ttnn.multiply,
            ]:
                make_l1(node)
                modified = True

            if node.target in [ttnn.linear, ttnn.matmul]:
                make_core_grid_full(node)
                modified = True

        return PassResult(gm, modified)

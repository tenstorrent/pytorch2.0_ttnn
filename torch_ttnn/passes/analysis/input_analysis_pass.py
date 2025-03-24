# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
from torch._subclasses.fake_tensor import unset_fake_temporarily
from torch.fx.passes.infra.pass_base import PassBase, PassResult
from torch_ttnn.utils import TtnnDevice

import ttnn
from enum import Enum


class PrimalTag(Enum):
    PARAMETER = 1
    BUFFER = 2
    ARGUMENT = 3


class InputAnalysisPass(PassBase):
    def __init__(self, n_parameters, n_buffers, n_arguments):
        super().__init__()

        self.n_parameters = n_parameters
        self.n_buffers = n_buffers
        self.n_arguments = n_arguments

    def call(self, gm: torch.fx.GraphModule):
        def annotate_node(node, tag):
            node.meta["primal_tag"] = tag

        modified = False
        placeholder_counter = 0

        node_list = list(gm.graph.nodes)
        for node in node_list:
            if node.op == "placeholder":
                if placeholder_counter < self.n_parameters:
                    annotate_node(node, PrimalTag.PARAMETER)
                elif placeholder_counter < self.n_parameters + self.n_buffers:
                    annotate_node(node, PrimalTag.BUFFER)
                else:
                    annotate_node(node, PrimalTag.ARGUMENT)
                placeholder_counter += 1

        return PassResult(gm, modified)

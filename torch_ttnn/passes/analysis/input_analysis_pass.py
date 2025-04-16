# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
from torch.fx.passes.infra.pass_base import PassBase, PassResult
from enum import Enum


class PrimalTag(Enum):
    """Enumeration of compiled model inputs.

    It is expected that PARAMETER and BUFFER tensors do not change between inference runs, but ARGUMENT tensors may change.

    :param PARAMETER: Tensor tracked by optimizer during training. Represents weights and biases.
    :param BUFFER: Tensor not updated during training but still part of model state. Normally used for non-trainable data like fixed weights or running statistics in batch norm.
    :param ARGUMENT: Tensors not tracked by model and not persistent between calls. Can be input data or configuration options to module's methods.
    """

    PARAMETER = 1
    BUFFER = 2
    ARGUMENT = 3


class InputAnalysisPass(PassBase):
    def __init__(self, num_parameters, num_buffers, num_arguments):
        super().__init__()

        self.num_parameters = num_parameters
        self.num_buffers = num_buffers
        self.num_arguments = num_arguments

    def call(self, gm: torch.fx.GraphModule):
        """Marks inputs for the compiled function as parameters, buffers, or arguments.

        This relies on how PyTorch behaves under the hood. Namely, PyTorch will lay out function arguments in the order of parameters, then buffers, then arguments. We can rely on this layout order and the number of parameters, buffers, and arguments passed in from AOTAutograd to our backend function.

        :param gm: Graph module for the function being compiled.
        :return: Pass result with the updated graph module and whether the graph was modified.
        :rtype: PassResult[torch.fx.GraphModule, bool]
        """

        def annotate_node(node, tag):
            node.meta["primal_tag"] = tag

        modified = False
        placeholder_counter = 0

        node_list = list(gm.graph.nodes)
        for node in node_list:
            if node.op == "placeholder":
                if placeholder_counter < self.num_parameters:
                    annotate_node(node, PrimalTag.PARAMETER)
                elif placeholder_counter < self.num_parameters + self.num_buffers:
                    annotate_node(node, PrimalTag.BUFFER)
                else:
                    annotate_node(node, PrimalTag.ARGUMENT)
                placeholder_counter += 1

        return PassResult(gm, modified)

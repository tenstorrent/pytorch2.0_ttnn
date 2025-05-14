# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
from torch.fx.passes.infra.pass_base import PassBase, PassResult
from enum import Enum


class ModelType(Enum):
    """Enumeration of compiled model inputs.

    It is expected that PARAMETER and BUFFER tensors do not change between inference runs, but ARGUMENT tensors may change.

    :param PARAMETER: Tensor tracked by optimizer during training. Represents weights and biases.
    :param BUFFER: Tensor not updated during training but still part of model state. Normally used for non-trainable data like fixed weights or running statistics in batch norm.
    :param ARGUMENT: Tensors not tracked by model and not persistent between calls. Can be input data or configuration options to module's methods.
    """

    INFERENCE = 1
    TRAIN_FORWARD = 2
    TRAIN_BACKWARD = 3


aten_backward_ops = {
    torch.ops.aten._adaptive_avg_pool2d_backward.default,
    torch.ops.aten.avg_pool2d_backward.default,
    torch.ops.aten.convolution_backward.default,
    torch.ops.aten.embedding_dense_backward.default,
    torch.ops.aten.max_pool2d_with_indices_backward.default,
    torch.ops.aten.native_group_norm_backward.default,
    torch.ops.aten.native_layer_norm_backward.default,
}


def is_train_backward(gm):
    node_list = list(gm.graph.nodes)
    for node in node_list:
        if node.op == "call_function" and node.target in aten_backward_ops:
            return True

    return False


def is_train_forward(gm):
    outputs = [node for node in gm.graph.nodes if node.op == "output"]
    for node in outputs:
        placeholder_args = [arg for arg in node.args[0] if arg.op == "placeholder"]
        if len(placeholder_args) > 0:
            return True

    return False


class GraphModuleAnalysisPass(PassBase):
    def __init__(self):
        super().__init__()

    def call(self, gm: torch.fx.GraphModule):
        """Marks inputs for the compiled function as parameters, buffers, or arguments.

        This relies on how PyTorch behaves under the hood. Namely, PyTorch will lay out function arguments in the order of parameters, then buffers, then arguments. We can rely on this layout order and the number of parameters, buffers, and arguments passed in from AOTAutograd to our backend function.

        :param gm: Graph module for the function being compiled.
        :return: Pass result with the updated graph module and whether the graph was modified.
        :rtype: PassResult[torch.fx.GraphModule, bool]
        """

        modified = False

        # check nodes for backward function call
        if is_train_backward(gm):
            gm.meta["graph_type"] = ModelType.TRAIN_BACKWARD
        elif is_train_forward(gm):
            gm.meta["graph_type"] = ModelType.TRAIN_FORWARD
        else:
            gm.meta["graph_type"] = ModelType.INFERENCE

        return PassResult(gm, modified)

# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
from torch.fx.passes.infra.pass_base import PassBase, PassResult
from enum import Enum


class ModelType(Enum):
    """Enumeration of model types differentiating between inference and training, forward and backward.

    :param INFERENCE: Model with this tag is for the forward pass of inference.
    :param TRAIN_FORWARD: Model wih this tag is for the forward pass of a training run.
    :param TRAIN_BACKWARD: Model with this tag is for the backward pass of a training run.
    """

    INFERENCE = 1
    TRAIN_FORWARD = 2
    TRAIN_BACKWARD = 3


# This list seems small, but is based off all the backward calls from the Core Aten IR:
# https://docs.pytorch.org/docs/stable/torch.compiler_ir.html
# The list is augmented by any ops we track in docs/operations, which helps capture more in practice
aten_backward_ops = {
    torch.ops.aten.convolution_backward.default,
    torch.ops.aten.hardsigmoid_backward.default,
    torch.ops.aten.native_batch_norm_backward.default,
    torch.ops.aten.avg_pool2d_backward.default,
    torch.ops.aten._softmax_backward_data.default,
    torch.ops.aten.elu_backward.default,
    torch.ops.aten.embedding_dense_backward.default,
    torch.ops.aten.threshold_backward.default,
    torch.ops.aten.sigmoid_backward.default,
    torch.ops.aten.native_layer_norm_backward.default,
    torch.ops.aten.select_backward.default,
    torch.ops.aten._log_softmax_backward_data.default,
    torch.ops.aten.hardtanh_backward.default,
    torch.ops.aten.gelu_backward.default,
    torch.ops.aten.native_dropout_backward.default,
    torch.ops.aten.max_pool2d_with_indices_backward.default,
    torch.ops.aten.slice_backward.default,
}


def is_train_backward(gm):
    node_list = list(gm.graph.nodes)
    for node in node_list:
        if node.op == "call_function" and node.target in aten_backward_ops:
            return True

    return False


def is_train_forward(gm):
    # Assume training forward calls are differentiated by directly returning one of the inputs to be used for calculating gradients
    # If this assumption fails in the future, we will need to update this function
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
        """Marks the GraphModule as either training forward, training backward, or inference (forward).

        This relies on commonalities between training forward, backward, and inference graphs. Namely, backward passes call backward versions of the forward functions to calculate gradients. Training forward passes return inputs unchanged. Inference forward functions do neither of these. It would be cleaner if we could just use something like `torch.is_grad_enabled()` or `gm.training` instead, but these appear to be inaccurate by the time the GraphModule is passed to our backend.

        :param gm: Graph module for the function being compiled.
        :return: Pass result with the updated graph module with metadata indicating the type of graph being compiled.
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

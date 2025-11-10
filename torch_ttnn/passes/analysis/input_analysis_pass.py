# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
from torch.fx.passes.infra.pass_base import PassBase, PassResult
from enum import Enum
from torch_ttnn.utils import get_input_nodes


def find_first_source_member(source, member):
    """
    This function attempts to recursively find the first member in a ChainedSource class.
    If it exists, then return True, otherwise return False.
    """

    if hasattr(source, "member") and source.member == member:
        return True
    if hasattr(source, "base"):
        return find_first_source_member(source.base, member)
    else:
        return False


def get_placeholder_types(gm):
    """
    This function will try to find certain member values in the `source` metadata to determine how to assign the
    placeholder types that will be used in other passes.
    View the top comment in torch/_dynamo/source.py code for more information on the various Source class subtypes.

    Example source metadata:

    The following placeholder contains the "_parameters" member, which will be assigned PARAMETER.
    ```
    DictGetItemSource(base=UnspecializedBuiltinNNModuleSource(base=UnspecializedParamBufferSource
    (base=DictGetItemSource(base=UnspecializedNNModuleSource(base=AttrSource(base=LocalSource
    (local_name='self', is_input=True, dynamism=None, is_derefed_cell_contents=False), member='_modules')),
    index='conv1'), member='_parameters')), index='weight')
    ```

    The following placeholder does not contain "_parameters" nor "_buffers". This is will be assigned ARGUMENT.
    ```
    LocalSource(local_name='x', is_input=True, dynamism=None, is_derefed_cell_contents=False)
    ```
    """

    node_list = list(gm.graph.nodes)
    placeholder_types = []
    for node in node_list:
        if node.op == "placeholder":
            source = node.meta["grapharg"].source
            if find_first_source_member(source, "_buffers"):
                placeholder_types.append("BUFFER")
            elif find_first_source_member(source, "_parameters"):
                placeholder_types.append("PARAMETER")
            else:
                placeholder_types.append("ARGUMENT")

    return placeholder_types


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
    def __init__(self, placeholder_types):
        super().__init__()

        self.placeholder_types = placeholder_types

    def call(self, gm: torch.fx.GraphModule):
        """Marks inputs for the compiled function as parameters, buffers, or arguments.

        After upgrading to Pytorch 2.7.1, Pytorch no longer lays out the function arguments in the order of parameters, then buffers, then arguments.
        We can no longer rely on this layout order. Instead, at the AOTAutograd level, Pytorch labels the placeholders as either
        torch.nn.paramtorch.nn.parameter.Parameter or torch.nn.parameter.Buffer. We can save these in the same order and pass them to our backend.
        This does assume the argument order doesn't change.

        :param gm: Graph module for the function being compiled.
        :return: Pass result with the updated graph module and whether the graph was modified.
        :rtype: PassResult[torch.fx.GraphModule, bool]
        """

        def annotate_node(node, tag):
            node.meta["primal_tag"] = tag

        modified = False

        node_list = get_input_nodes(gm.graph)
        if len(node_list) == len(self.placeholder_types):
            for node, placeholder_type in zip(node_list, self.placeholder_types):
                if placeholder_type == "PARAMETER":
                    annotate_node(node, PrimalTag.PARAMETER)
                elif placeholder_type == "BUFFER":
                    annotate_node(node, PrimalTag.BUFFER)
                else:
                    annotate_node(node, PrimalTag.ARGUMENT)

        return PassResult(gm, modified)

# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
from torch._functorch._aot_autograd.schemas import OutputType
from torch_ttnn.utils import get_node_name


def mark_output_as_tangents(graph: torch.fx.Graph) -> torch.fx.Graph:
    """
    Using metadata from pytorch, insert additional metadata into output nodes that are marked as tangents

    Args:
        graph: torch.fx.Graph
    Returns:
        torch.fx.Graph: Modified graph

    """
    output_node = list(graph.nodes)[-1]
    assert output_node.op == "output"
    outputs = output_node.args[0]

    # tangents are nodes before the first primal.
    # If primals do not exist, then nothing will change. We can prepend nodes in advance.
    tangents = []
    have_primals = False
    for out_arg in outputs:
        if get_node_name(out_arg).startswith("primals"):
            have_primals = True
            break
        tangents.append(out_arg)
    if have_primals:
        """
        Following the same process in Pytorch to create a mask for the tangents
        https://github.com/pytorch/pytorch/blob/30587195d314eb5eb02ce63f39a9be4c943629ef/torch/_functorch/_aot_autograd/traced_function_transforms.py#L159-L174
        """
        tracing_context = torch._guards.TracingContext.try_get()
        fw_metadata = tracing_context.fw_metadata

        output_grad_mask = [
            fw_metadata.output_info[i].output_type
            in [
                OutputType.non_alias,
                OutputType.unsafe_view_alias,
                OutputType.custom_function_view,
            ]
            # Also, only tensor outputs should participate in the backward
            # (in particular, Symint outputs in the forward graph shouldn't get tangents)
            and issubclass(fw_metadata.output_info[i].raw_type, torch.Tensor)
            and fw_metadata.output_info[i].requires_grad
            for i in range(len(fw_metadata.output_info))
        ]

        assert len(tangents) == len(output_grad_mask)
        for tan, mask in zip(tangents, output_grad_mask):
            tan.meta["tangents"] = mask

    return graph

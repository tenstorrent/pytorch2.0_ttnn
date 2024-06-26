import math
import torch
from typing import List
from .utils import GraphCleanup


# torch.fx defines a placeholder node as a function input
def get_input_nodes(gm: torch.fx.GraphModule) -> List[torch.fx.Node]:
    input_nodes = [node for node in gm.graph.nodes if (node.op == "placeholder")]
    return input_nodes


pytorch_float_types = [
    torch.float32,
    torch.float64,
    torch.float16,
]


def convert_float_to_bfloat16(gm: torch.fx.GraphModule) -> torch.fx.GraphModule:
    input_nodes = get_input_nodes(gm)
    modified = False

    for node in input_nodes:
        arg_metadata = node.meta["val"]
        if arg_metadata.dtype in pytorch_float_types:
            with gm.graph.inserting_after(input_nodes[-1]):
                to = gm.graph.call_method("to", args=(node, torch.bfloat16))
                node.replace_all_uses_with(
                    to,
                    delete_user_cb=lambda node: node != to,
                )
                modified = True

    if modified:
        gm = GraphCleanup(gm)
    return gm


# Use on aten level
def convert_dtype_to_bfloat16(gm: torch.fx.GraphModule) -> torch.fx.GraphModule:
    modified = False
    for node in gm.graph.nodes:
        # Convert min, max, of float32 to float16
        # TODO(kevinwuTT): Optimize this without needing to process every arg?
        new_args = []
        for arg in node.args:
            if type(arg) == int or type(arg) == float:
                if arg == torch.finfo(torch.float32).min:
                    new_args.append(torch.finfo(torch.bfloat16).min)
                elif arg == torch.finfo(torch.float32).max:
                    new_args.append(torch.finfo(torch.bfloat16).max)
                else:
                    new_args.append(arg)
            else:
                new_args.append(arg)
        node.args = tuple(new_args)

        if node.target == torch.ops.aten._to_copy.default:
            new_kwargs = {"dtype": torch.bfloat16}
            node.kwargs = new_kwargs
        if node.target == torch.ops.aten.full.default:
            new_kwargs = node.kwargs.copy()
            new_kwargs["dtype"] = torch.bfloat16
            node.kwargs = new_kwargs

    gm = GraphCleanup(gm)

    return gm

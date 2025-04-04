# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
from typing import List
from torch_ttnn.utils import GraphCleanup

"""
AOT Autograd has an optimization where if it determines that the storage of the
output is the same as the input, it will return data from the input. The output
is checked if it's an alias of the input. This becomes problematic when we
have data transfer between host and device. The issue has been raised before.
See: https://github.com/pytorch/pytorch/issues/108079

One workaround is to insert a clone op after every input node before the graph
is completely lowered to aten ops. This can be accomplished by pointing the
entry function with a `torch.fx.GraphModule` parameter to the `backend`
positional argument for `torch.compile`. At this point, the graph will have
higher-level torch ops where clone ops can be inserted. Then define another
function that will be passed to the `fw_compiler/bw_compiler` parameter for
`aot_autograd`. This is when the input aliasing metadata will be determined
and the graph will be lowered to aten ops. After this, the clone ops can
be removed with another pass.

The method is inspired by TensorRT:
https://github.com/pytorch/TensorRT/commit/7daa1120dc1bc72d6f92f1e7aa2b357a65b6ea08
"""


# Insert aten.clone nodes after every input to prevent input aliasing
def insert_clones_for_input_aliasing(gm: torch.fx.GraphModule) -> torch.fx.GraphModule:
    # get input tensor nodes only
    input_nodes = [node for node in gm.graph.nodes if (node.op == "placeholder" and node.meta["grapharg"].is_tensor)]

    modified = False
    for node in input_nodes:
        """TODO(kevinwuTT): This does not work if inserting right after the node itself.
        Only works if inserting after all of the input_nodes.
        TypeError: forward() missing `n` required positional arguments
        Somehow the argument list will get truncated.
        """
        with gm.graph.inserting_after(input_nodes[-1]):
            clone_node = gm.graph.call_function(torch.ops.aten.clone.default, args=(node,))
            node.replace_all_uses_with(
                clone_node,
                delete_user_cb=lambda node: node != clone_node,
            )
            modified = True

    if modified:
        """
        Do not call `eliminate_dead_code()` before `aot_autograd` because the function has not
        been functionalized yet. This means some other mutations will be eliminate
        inadvertently.

        Example:
        ```
        1: def f():
        2:    mask = torch.full((1, 1), 1)
        3:    mask_cond = torch.full((1, 1), True)
        4:    masked_fill = mask.masked_fill_(mask_cond, 0)
        5:    mask_1 = mask.to(torch.bfloat16)
        6:    return mask_1
        ```

        In the function above, `eliminate_dead_code()` does not know that `mask.masked_fill_` mutates
        the `mask` tensor in-place. Therefore, it sees that `masked_fill` is not used and will eliminate lines 3 and 4. The result of the function above should be `tensor([[0.]], dtype=torch.bfloat16)`. However, after code elimination, the function will become below and
        the result will be `tensor([[1.]], dtype=torch.bfloat16)` which is incorrect.

        ```
        1: def f():
        2:    mask = torch.full((1, 1), 1)
        3:    mask_1 = mask.to(torch.bfloat16)
        4:    return mask_1
        ```
        """
        gm.graph.lint()
        gm.recompile()

    return gm


def remove_clones_for_input_aliasing(gm: torch.fx.GraphModule) -> torch.fx.GraphModule:
    """Remove the clone ops inserted to handle input aliasing
    opcode         name             target               args
    -------------  ---------------  -------------------  ------------
    placeholder    l_input_         L_input_             ()
    call_function  clone_default    aten.clone.default   (l_input_,)
    call_function  op               <op_func>            (clone_default)
    """
    modified = False
    for node in gm.graph.nodes:
        if (
            node.op == "placeholder"
            and len(node.users) == 1
            and list(node.users)[0].target == torch.ops.aten.clone.default
        ):
            clone_node = list(node.users)[0]
            clone_node.replace_all_uses_with(node)
            gm.graph.erase_node(clone_node)

            modified = True

    if modified:
        gm = GraphCleanup(gm)

    return gm

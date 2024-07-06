# TODO(kevinwuTT): I have a patch for tt-metal that assigns the __name__ attribute of each Operation.
# This file may not be needed anymore.

import torch
import ttnn


# NOTE(yoco) The name `add` must be the same as the name of the function.
# Because in the implementation of fx.wrap use fn.__name__ to get the
# name of the function. If we write
#
#    some_other_name = ttnn.add
#
# The fn.__name__ will be `add` instead of `some_other_name`, because
# it is just a reference to the function `ttnn.add`.
#
# In the implementation of torch, it will use the name of the function
# to find the original function in current frame's globals and patch it.
# If the name of the function is `some_other_name`, it will not find the
# original function and raise an error.
add = ttnn.add
torch.fx.wrap(add)


def add_pat(x, y):
    return torch.ops.aten.add.Tensor(x, y)


def add_rep(x, y):
    return add(x, y)


def add_pat2(x):
    return torch.ops.aten.add.Tensor(x, x)


def add_rep2(x):
    return add(x, x)


pat_rep_list = [
    (add_pat, add_rep),
    (add_pat2, add_rep2),
]

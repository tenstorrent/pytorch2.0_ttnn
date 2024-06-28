# TODO(kevinwuTT): I have a patch for tt-metal that assigns the __name__ attribute of each Operation.
# This file may not be needed anymore.

import torch

try:
    import ttnn
except ImportError:
    print("ttnn is not installed, use mock_ttnn instead")
    from .. import mock_ttnn as ttnn


# NOTE(yoco) The name `matmul` must be the same as the name of the function.
# Because in the implementation of fx.wrap use fn.__name__ to get the
# name of the function. If we write
#
#    some_other_name = ttnn.matmul
#
# The fn.__name__ will be `matmul` instead of `some_other_name`, because
# it is just a reference to the function `ttnn.matmul`.
#
# In the implementation of torch, it will use the name of the function
# to find the original function in current frame's globals and patch it.
# If the name of the function is `some_other_name`, it will not find the
# original function and raise an error.
matmul = ttnn.matmul
torch.fx.wrap(matmul)


def mm_pat(x, y):
    return torch.ops.aten.mm.default(x, y)


def mm_rep(x, y):
    return matmul(x, y)


def mm_pat2(x):
    return torch.ops.aten.mm.default(x, x)


def mm_rep2(x):
    return matmul(x, x)


pat_rep_list = [
    (mm_pat, mm_rep),
    (mm_pat2, mm_rep2),
]

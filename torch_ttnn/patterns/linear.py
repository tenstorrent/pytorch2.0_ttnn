import torch


from .. import wrap_ttnn_ops as wrap


def linear_pat(x, y, z):
    a = torch.ops.aten.t.default(y)
    b = torch.ops.aten.addmm.default(z, x, a)
    return b


def linear_rep(x, y, z):
    return wrap.linear(x, y, z)


pat_rep_list = [
    (linear_pat, linear_rep),
]

import torch


from .. import wrap_ttnn_ops as wrap


def linear_with_bias_pat(x, y, z):
    a = torch.ops.aten.t.default(y)
    b = torch.ops.aten.addmm.default(z, x, a)
    return b


def linear_with_bias_rep(x, y, z):
    return wrap.linear(x, y, bias=z)


def linear_pat(x, y):
    a = torch.ops.aten.t.default(y)
    b = torch.ops.aten.mm.default(x, a)
    return b


def linear_rep(x, y):
    return wrap.linear(x, y)


pat_rep_list = [
    (linear_pat, linear_rep),
    (linear_with_bias_pat, linear_with_bias_rep),
]

import torch


from .. import wrap_ttnn_ops as wrap


def addcdiv_with_value_pat(a0, a1, a2, value):
    div = torch.ops.aten.div.Tensor(a1, a2)
    mul = torch.ops.aten.mul.Tensor(div, value)
    add = torch.ops.aten.add.Tensor(a0, mul)
    return add


def addcdiv_with_value_rep(a0, a1, a2, value):
    return wrap.addcdiv(a0, a1, a2, value)



pat_rep_list = [
    (addcdiv_with_value_pat, addcdiv_with_value_rep),
]


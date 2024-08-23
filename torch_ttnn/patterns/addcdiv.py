import torch


import ttnn

addcdiv = ttnn.addcdiv
# NOTE(yoco) wrap the addcdiv will cause error in current ttnn version
# Try to fix it, or don't use subgraph rewriter, but manipulate the raw graph
# torch.fx.wrap(addcdiv)


def addcdiv_with_value_pattern(a0, a1, a2, value):
    div = torch.ops.aten.div.Tensor(a1, a2)
    mul = torch.ops.aten.mul.Tensor(div, value)
    add = torch.ops.aten.add.Tensor(a0, mul)
    return add


def addcdiv_with_value_replace(a0, a1, a2, value):
    return addcdiv(a0, a1, a2, value)


pattern_replace_list = [
    (addcdiv_with_value_pattern, addcdiv_with_value_replace),
]

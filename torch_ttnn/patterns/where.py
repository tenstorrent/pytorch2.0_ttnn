import torch


import ttnn

where = ttnn.fx.wrap(ttnn.where)


def where_pat(x, y, z):
    b = torch.ops.aten.where.self(x, y, z)
    return b


def where_rep(x, y, z):
    x_bfloat16 = x.to(torch.bfloat16)
    r = where(x_bfloat16, y, z)
    return r


pat_rep_list = [
    (where_pat, where_rep),
]

import torch


from .. import wrap_ttnn_ops as wrap

def group_norm_pat(input, weight, bias, N, C, HxW, group, eps):
    gn = torch.ops.aten.native_group_norm.default(input, weight, bias, N, C, HxW, group, eps)
    result = gn[0]
    return result

def group_norm_rep(input, weight, bias, N, C, HxW, group, eps):
    kwargs = {
        "num_groups": group,
        "epsilon": eps,
    }
    # if weight is not None:
    #     kwargs["weight"] = weight
    # if bias is not None:
    #     kwargs["bias"] = bias
    gn = wrap.group_norm(input, **kwargs)
    return gn

pat_rep_list = [
    (group_norm_pat, group_norm_rep),
]

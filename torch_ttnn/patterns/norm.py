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

def layer_norm_pat(input, normalized_shape, weight, bias, eps):
    ln = torch.ops.aten.native_layer_norm.default(input, normalized_shape, weight, bias, eps)
    result = ln[0]
    return result

def layer_norm_rep(input, normalized_shape, weight, bias, eps):
    ln = wrap.layer_norm(input)#, normalized_shape)
    return ln

pat_rep_list = [
    (group_norm_pat, group_norm_rep),
    # (layer_norm_pat, layer_norm_rep),
]

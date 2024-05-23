import ttnn
import torch


@torch.fx.wrap
def clone(t):
    return ttnn.clone(t, t.memory_config(), t.dtype)


@torch.fx.wrap
def repeat(t, sizes):
    return ttnn.repeat(t, ttnn.Size(sizes))


def group_norm(input, num_groups, epsilon, weight=None, bias=None):
    # TODO: make it work
    #  if weight is not None:
    #      kwargs["weight"] = weight
    #  if bias is not None:
    #      kwargs["bias"] = bias
    #  if weight is None:
    #      weight = ttnn.Tensor()
    return ttnn.group_norm(input, num_groups, epsilon, weight, bias)

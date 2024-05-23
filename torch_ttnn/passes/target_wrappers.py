import ttnn
import torch


@torch.fx.wrap
def clone(t):
    return ttnn.clone(t, t.memory_config(), t.dtype)


@torch.fx.wrap
def repeat(t, sizes):
    return ttnn.repeat(t, ttnn.Size(sizes))

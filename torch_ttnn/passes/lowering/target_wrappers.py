import ttnn
import torch


@torch.fx.wrap
def clone(t):
    return ttnn.clone(t, memory_config=t.memory_config(), dtype=t.dtype)


@torch.fx.wrap
def repeat(t, sizes):
    return ttnn.repeat(t, ttnn.Shape(sizes))


@torch.fx.wrap
def getitem(t, bounds):
    return t[[slice(lower, upper) for lower, upper in bounds]]

import ttnn
import torch


@torch.fx.wrap
def clone(t):
    return ttnn.clone(t, memory_config=t.memory_config(), dtype=t.dtype)


@torch.fx.wrap
def repeat(t, sizes):
    return ttnn.repeat(t, ttnn.Shape(sizes))


# Perform symbolic crop operation `t[0:a, 0:b, ...]`, which results in the shape `(a[x], b[y], ...)`
@torch.fx.wrap
def crop(t, sizes):
    return t[[slice(0, size) for size in sizes]]

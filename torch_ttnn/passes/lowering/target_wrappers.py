import ttnn
import torch


@torch.fx.wrap
def clone(t):
    return ttnn.clone(t, memory_config=t.memory_config(), dtype=t.dtype)


@torch.fx.wrap
def repeat(t, sizes):
    return ttnn.repeat(t, ttnn.Shape(sizes))


# Helper function to pack multiple values into a tuple on the graph
@torch.fx.wrap
def pack_to_tuple(*args):
    return tuple(args)

import ttnn
import torch

@torch.fx.wrap
def clone(t):
    return ttnn.clone(t, t.memory_config(), t.dtype)
import torch
import ttnn


def add_pattern(x, y):
    return torch.ops.aten.add.Tensor(x, y)


def add_replace(x, y):
    return ttnn.add(x, y)


def add_pattern2(x):
    return torch.ops.aten.add.Tensor(x, x)


def add_replace2(x):
    return ttnn.add(x, x)


pattern_replace_list = [
    (add_pattern, add_replace),
    (add_pattern2, add_replace2),
]

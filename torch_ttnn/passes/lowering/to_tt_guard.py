from functools import partial
from .to_tt_guard_autogen import *

# Add for pass CLIP eval
aten_mul_Tensor_blocklist += [
    ["Tensor<[1, 50, 768]> self = ?", "Tensor other = 0.125"],
    ["Tensor<[1, 50, 3072]> self = ?", "Tensor other = 1.702"],
    ["Tensor<[1, 50, 3072]> self = ?", "Tensor<[1, 50, 3072]> other = ?"],
    ["Tensor<[2, 7, 512]> self = ?", "Tensor other = 0.125"],
    ["Tensor<[2, 7, 2048]> self = ?", "Tensor other = 1.702"],
    ["Tensor<[2, 7, 2048]> self = ?", "Tensor<[2, 7, 2048]> other = ?"],
    ["Tensor<[2, 1]> self = ?", "Tensor<[]> other = ?"],
]

aten_view_default_blocklist += [
    ["Tensor<[1, 768, 7, 7]> self = ?", "List[int] size = [1, 768, 49]"],
    ["Tensor<[1, 50, 768]> self = ?", "List[int] size = [50, 768]"],
    ["Tensor<[50, 768]> self = ?", "List[int] size = [1, 50, 768]"],
    ["Tensor<[1, 50, 768]> self = ?", "List[int] size = [1, -1, 12, 64]"],
    ["Tensor<[1, 50, 768]> self = ?", "List[int] size = [1, 50, 12, 64]"],
    ["Tensor<[1, 12, 50, 64]> self = ?", "List[int] size = [12, -1, 64]"],
    ["Tensor<[12, 50, 64]> self = ?", "List[int] size = [1, 12, 50, 64]"],
    ["Tensor<[50, 3072]> self = ?", "List[int] size = [1, 50, 3072]"],
    ["Tensor<[1, 50, 3072]> self = ?", "List[int] size = [50, 3072]"],
    ["Tensor<[2, 7]> self = ?", "List[int] size = [-1, 7]"],
    ["Tensor<[2, 7, 512]> self = ?", "List[int] size = [14, 512]"],
    ["Tensor<[14, 512]> self = ?", "List[int] size = [2, 7, 512]"],
    ["Tensor<[2, 7, 512]> self = ?", "List[int] size = [2, -1, 8, 64]"],
    ["Tensor<[2, 7, 512]> self = ?", "List[int] size = [2, 7, 8, 64]"],
    ["Tensor<[2, 8, 7, 64]> self = ?", "List[int] size = [16, -1, 64]"],
    ["Tensor<[16, 7, 7]> self = ?", "List[int] size = [2, 8, 7, 7]"],
    ["Tensor<[2, 8, 7, 7]> self = ?", "List[int] size = [16, 7, 7]"],
    ["Tensor<[16, 7, 64]> self = ?", "List[int] size = [2, 8, 7, 64]"],
    ["Tensor<[14, 2048]> self = ?", "List[int] size = [2, 7, 2048]"],
    ["Tensor<[2, 7, 2048]> self = ?", "List[int] size = [14, 2048]"],
]

aten__to_copy_default_blocklist = [
    ["Tensor<[1, 3, 224, 224]> self = ?", "Optional[int] dtype = torch.bfloat16"],
    ["Tensor<[7, 7]> self = ?", "Optional[int] dtype = torch.bfloat16"],
    ["Tensor<[2, 1, 7, 7]> self = ?", "Optional[int] dtype = torch.bfloat16"],
    ["Tensor<[2, 1, 7, 7]> self = ?", "Optional[int] dtype = torch.bool"],
    ["Tensor<[2, 7]> self = ?", "Optional[int] dtype = torch.int32", "Optional[Device] device = cpu"],
]

aten_native_layer_norm_default_blocklist += [
    [
        "Tensor<[1, 50, 768]> input = ?",
        "List[int] normalized_shape = [768]",
        "Optional[Tensor]<[768]> weight = ?",
        "Optional[Tensor]<[768]> bias = ?",
        "float eps = 1e-05",
    ],
    [
        "Tensor<[1, 768]> input = ?",
        "List[int] normalized_shape = [768]",
        "Optional[Tensor]<[768]> weight = ?",
        "Optional[Tensor]<[768]> bias = ?",
        "float eps = 1e-05",
    ],
    [
        "Tensor<[2, 7, 512]> input = ?",
        "List[int] normalized_shape = [512]",
        "Optional[Tensor]<[512]> weight = ?",
        "Optional[Tensor]<[512]> bias = ?",
        "float eps = 1e-05",
    ],
]

# Need to remove this from the blocklist so that yolos can pass
aten_view_default_blocklist.remove(["Tensor<[1, 192, 32, 42]> self = ?", "List[int] size = [1, 192, 1344]"])


GUARD[torch.ops.aten._to_copy.default] = partial(guard_aten, aten__to_copy_default_blocklist)


def can_lowering_to_ttnn(node):
    if node.target in GUARD:
        return GUARD[node.target](node)

    return True

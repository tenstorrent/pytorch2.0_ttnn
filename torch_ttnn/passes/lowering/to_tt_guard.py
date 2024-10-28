from functools import partial
from .to_tt_guard_autogen import *

### EXTRA BLOCKLIST OF CLIP START ###
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

### EXTRA BLOCKLIST OF CLIP END ###

### EXTRA BLOCKLIST OF albert/albert-base-v2-classification START ###

# If enable, then ttnn._ttnn.operations.binary.add_t will encounter this inputs and failed:
# (ttnn.Tensor([[[ 0.74219,  0.07324,  ...,  1.32812,  0.25391],
#               [ 0.57031,  0.38086,  ...,  0.37695, -0.16309],
#               ...,
#               [ 0.71875,  0.25000,  ...,  0.36133,  0.04224],
#               [ 0.44727,  0.45312,  ...,  0.42188, -0.65234]]],
#       shape=Shape([1, 12, 768]), dtype=DataType::BFLOAT16, layout=Layout::ROW_MAJOR),
#   ttnn.Tensor(<buffer is not allocated>, shape=Shape([1, 12[32], 768]),
#       dtype=DataType::BFLOAT16, layout=Layout::TILE))
# And I don't know why its inputs[1] become ([1, 12[32], 768])
# Reproduce method: comment this line and run "pytest tests/models/albert/test_albert_token_classification.py"
aten_add_Tensor_blocklist += [["Tensor<[1, 12, 768]> self = ?", "Tensor<[1, 12, 768]> other = ?"]]
### EXTRA BLOCKLIST OF albert/albert-base-v2-classification END ###

### EXTRA BLOCKLIST OF other albert START ###
# other albert models have the same issue as albert/albert-base-v2-classification
# albert/albert-base-v2: inputs[1].shape become ([1, 9[32], 768]) during inference
aten_add_Tensor_blocklist += [["Tensor<[1, 9, 768]> self = ?", "Tensor<[1, 9, 768]> other = ?"]]
# albert/albert-large-v2: inputs[1].shape become ([1, 9[32], 1024]) during inference
aten_add_Tensor_blocklist += [["Tensor<[1, 9, 1024]> self = ?", "Tensor<[1, 9, 1024]> other = ?"]]
# albert/albert-xlarge-v2: inputs[1].shape become ([1, 9[32], 2048]) during inference
aten_add_Tensor_blocklist += [["Tensor<[1, 9, 2048]> self = ?", "Tensor<[1, 9, 2048]> other = ?"]]
# albert/albert-xxlarge-v2: inputs[1].shape become ([1, 9[32], 4096]) during inference
aten_add_Tensor_blocklist += [["Tensor<[1, 9, 4096]> self = ?", "Tensor<[1, 9, 4096]> other = ?"]]
# twmkn9/albert-base-v2-squad2: inputs[1].shape become ([1, 14[32], 768) during inference
aten_add_Tensor_blocklist += [["Tensor<[1, 14, 768]> self = ?", "Tensor<[1, 14, 768]> other = ?"]]
### EXTRA BLOCKLIST OF albert/albert-base-v2 END ###


### EXTRA BLOCKLIST OF microsoft/beit-*-patch16-224 START ###
# This pattern origin is
# view_37 -> aten::index.Tensor
# after is
# ttnn_reshape_39 -> aten::index.Tensor
# And the error msg is "IndexError: tensors used as indices must be long, int, byte or bool tensors"
# It means origin dtype of view_37 is int64
# But after it convert to ttnn.reshape, the dtype of ttnn_reshape_39 is NOT int64
# So there disable view lowering to avoid it become ttnn.reshape

# beit-base-patch16-224
aten_view_default_blocklist += [
    ["Tensor<[1, 768, 14, 14]> self = ?", "List[int] size = [1, 768, 196]"],
    ["Tensor<[1, 197, 768]> self = ?", "List[int] size = [197, 768]"],
    ["Tensor<[197, 768]> self = ?", "List[int] size = [1, 197, 768]"],
    ["Tensor<[1, 197, 768]> self = ?", "List[int] size = [1, 197, 12, 64]"],
    ["Tensor<[1, 12, 197, 64]> self = ?", "List[int] size = [12, 197, 64]"],
    ["Tensor<[1, 12, 64, 197]> self = ?", "List[int] size = [12, 64, 197]"],
    ["Tensor<[12, 197, 197]> self = ?", "List[int] size = [1, 12, 197, 197]"],
    ["Tensor<[197, 197]> self = ?", "List[int] size = [-1]"],
    ["Tensor<[38809, 12]> self = ?", "List[int] size = [197, 197, -1]"],
    ["Tensor<[1, 12, 197, 197]> self = ?", "List[int] size = [12, 197, 197]"],
    ["Tensor<[12, 197, 64]> self = ?", "List[int] size = [1, 12, 197, 64]"],
    ["Tensor<[1, 197, 12, 64]> self = ?", "List[int] size = [1, 197, 768]"],
    ["Tensor<[197, 3072]> self = ?", "List[int] size = [1, 197, 3072]"],
    ["Tensor<[1, 197, 3072]> self = ?", "List[int] size = [197, 3072]"],
]

# beit-large-patch16-224
aten_view_default_blocklist += [
    ["Tensor<[1, 1024, 14, 14]> self = ?", "List[int] size = [1, 1024, 196]"],
    ["Tensor<[1, 197, 1024]> self = ?", "List[int] size = [197, 1024]"],
    ["Tensor<[197, 1024]> self = ?", "List[int] size = [1, 197, 1024]"],
    ["Tensor<[1, 197, 1024]> self = ?", "List[int] size = [1, 197, 16, 64]"],
    ["Tensor<[1, 16, 197, 64]> self = ?", "List[int] size = [16, 197, 64]"],
    ["Tensor<[1, 16, 64, 197]> self = ?", "List[int] size = [16, 64, 197]"],
    ["Tensor<[16, 197, 197]> self = ?", "List[int] size = [1, 16, 197, 197]"],
    ["Tensor<[197, 197]> self = ?", "List[int] size = [-1]"],
    ["Tensor<[38809, 16]> self = ?", "List[int] size = [197, 197, -1]"],
    ["Tensor<[1, 16, 197, 197]> self = ?", "List[int] size = [16, 197, 197]"],
    ["Tensor<[16, 197, 64]> self = ?", "List[int] size = [1, 16, 197, 64]"],
    ["Tensor<[1, 197, 16, 64]> self = ?", "List[int] size = [1, 197, 1024]"],
    ["Tensor<[197, 4096]> self = ?", "List[int] size = [1, 197, 4096]"],
    ["Tensor<[1, 197, 4096]> self = ?", "List[int] size = [197, 4096]"],
]
### EXTRA BLOCKLIST OF microsoft/beit-*-patch16-224 END ###

### EXTRA BLOCKLIST OF XGLM START ###
# Error msg:
# self = <OpOverload(op='aten.index_select', overload='default')>
# args = (tensor([[ 0.0000,  0.0000,  0.0000,  ...,  1.0000,  1.0000,  1.0000],
#         [ 0.0000,  0.0000,  0.0000,  ...,  0.00....,  5.,  6.,  7.,  8.,  9., 10., 11., 12., 13., 14.,
#              15., 16., 17., 18., 19., 20.], dtype=torch.bfloat16))
# kwargs = {}
#     def __call__(self, *args, **kwargs):
# >       return self._op(*args, **(kwargs or {}))
# E       RuntimeError: index_select(): Expected dtype int32 or int64 for index
#
# open "metrics/XGLM/00.origin.dot.svg" and search "index_select", you can see this pattern...
# aten::arange.start -> aten::unsqueeze -> aten::add.Tensor ->
# aten::squeeze.dim -> aten::unsqueeze -> aten::view -> 3rd input of aten::index_select
# 3rd input of aten::index_select should be int32 or int64, but after lowering, it is bf16
#
# I disable above pattern to avoid it become ttnn op

# aten::arange.start: it's not lowering, no need to block
# aten::unsqueeze
aten_unsqueeze_default_blocklist = [["Tensor<[19]> self = ?", "int dim = 0"]]
# aten::add.Tensor
aten_add_Tensor_blocklist += [["Tensor<[1, 19]> self = ?", "Tensor other = 2"]]
# aten::squeeze.dim
aten_squeeze_dim_blocklist = [["Tensor<[1, 19]> self = ?", "int dim = 0"]]
# aten::unsqueeze: same with above, no need to block
# aten::view
aten_view_default_blocklist += [
    ["Tensor<[1, 19]> self = ?", "List[int] size = [-1]"],
]

### EXTRA BLOCKLIST OF XGLM END ###

### EXTRA BLOCKLIST OF FALCON START ###

aten_unsqueeze_default_blocklist += [["Tensor<[7]> self = ?", "int dim = 0"]]

aten_masked_fill_scalar_blocklist += [["Tensor<[7, 7]> self = ?", "Tensor<[7, 7]> mask = ?", "number value = -inf"]]

### EXTRA BLOCKLIST OF FALCON END ###

GUARD[torch.ops.aten._to_copy.default] = partial(guard_aten, aten__to_copy_default_blocklist)
GUARD[torch.ops.aten.unsqueeze.default] = partial(guard_aten, aten_unsqueeze_default_blocklist)
GUARD[torch.ops.aten.squeeze.dim] = partial(guard_aten, aten_squeeze_dim_blocklist)


def can_lowering_to_ttnn(node):
    if node.target in GUARD:
        return GUARD[node.target](node)

    return True

from functools import partial
from .to_tt_guard_autogen import *

############################################################
# EXTRA BLOCKLIST OF microsoft/beit-*-patch16-224
############################################################
# error value let 731 become 732 and cause index error (shape is [732, 12])
# see issue #420

aten_view_default_blocklist = [
    ["Tensor<[197, 197]> self = ?", "List[int] size = [-1]"],
]

############################################################
# EXTRA BLOCKLIST OF retinanet_resnet50_fpn*
############################################################

# retinanet_resnet50_fpn
# RuntimeError: Missing conversion from torch.dtype: torch.int32 to Ttnn dtype.
# => comment ttnn_dtype = torch_dtype_to_ttnn_dtype(arg_metadata.dtype), it is not used now

# RuntimeError: _unsafe_index found unexpected index type BFloat16
# ... => aten::sub.Tensor => aten::div.Tensor => unsqueeze => unsafe_index
# it is too long to block, so just wait the to_tt_pass fix

# TODO: not pass yet

############################################################
# EXTRA BLOCKLIST OF ghostnetv2_100.in1k*
############################################################

# see issue #390
# ghostnetv2_100.in1k
# RuntimeError: _unsafe_index found unexpected index type BFloat16
# arange => add => mul => to_copy => unsqueeze => unsafe_index
aten_add_Tensor_blocklist = []
aten_add_Tensor_blocklist += [
    ["Tensor<[56]> self = ?", "Tensor other = 0.0"],
    ["Tensor<[28]> self = ?", "Tensor other = 0.0"],
    ["Tensor<[14]> self = ?", "Tensor other = 0.0"],
    ["Tensor<[7]> self = ?", "Tensor other = 0.0"],
]

aten_mul_Tensor_blocklist += [
    ["Tensor<[56]> self = ?", "Tensor other = 0.5"],
    ["Tensor<[28]> self = ?", "Tensor other = 0.5"],
    ["Tensor<[14]> self = ?", "Tensor other = 0.5"],
    ["Tensor<[7]> self = ?", "Tensor other = 0.42857142857142855"],
]

# ghostnetv2_100.in1k-train
# TODO:
# RuntimeError: Index put requires the source and destination dtypes match,
# got Float for the destination and BFloat16 for the source.
# gm.code:
# new_zeros_default_1 = torch.ops.aten.new_zeros.default(
#     mul_tensor_2, [1, 960, 3, 3], dtype=torch.float32, layout=torch.strided, device=device(type="cpu")
# )
# _unsafe_index_put_default = torch.ops.aten._unsafe_index_put.default(
#     new_zeros_default_1, [None, None, unsqueeze_13, _to_copy_292], ttnn_to_torch_7, True
# )
# new_zeros_default_1 is float32 type and ttnn_to_torch_7 is bf16 type
# need a pass to equal _unsafe_index_put_default's input type

############################################################
# EXTRA BLOCKLIST OF hrnet_w18.ms_aug_in1k*
############################################################
# see issue #363
# self = <OpOverload(op='aten.convolution', overload='default')>
# args = (TorchTensor([[[[[6.6797e-01, 1.5703e+00, 1.1562e+00,  ..., 5.8203e-01,
#                  3.3936e-02, 1.1953e+00],
#     ...-03,  1.2360e-03, -4.0527e-02]]]], dtype=torch.bfloat16,
#        requires_grad=True), None, [1, 1], [1, 1], [1, 1], ...)
# kwargs = {}
#     def __call__(self, *args, **kwargs):
# >       return self._op(*args, **(kwargs or {}))
# RuntimeError: Expected 4-dimensional input for 4-dimensional weight [18, 18, 3, 3], but got 5-dimensional input of size [1, 18, 18, 56, 56] instead
# gm.code:
# add_tensor = torch.ops.aten.add.Tensor(arange_default, 0.0);  arange_default = None
# mul_tensor = torch.ops.aten.mul.Tensor(add_tensor, 0.5)
# _to_copy_default_1 = torch.ops.aten._to_copy.default(mul_tensor, dtype = torch.int64);  mul_tensor = None
# unsqueeze_default = torch.ops.aten.unsqueeze.default(_to_copy_default_1, -1)
# _unsafe_index_tensor = torch.ops.aten._unsafe_index.Tensor(getitem_33, [None, None, unsqueeze_default, _to_copy_default_1]);  getitem_33 = None
# ttnn_from_torch_33 = ttnn_decorators_ttnn_from_torch(_unsafe_index_tensor, layout = ttnn_TILE_LAYOUT, dtype = ttnn_bfloat16, device = ttnn_Specified_Device);  _unsafe_index_tensor = None
# ttnn_add_12 = ttnn_decorators_ttnn_add(ttnn_relu_23, ttnn_from_torch_33);  ttnn_from_torch_33 = None
# ttnn_relu_32 = ttnn_decorators_ttnn_relu(ttnn_add_12);  ttnn_add_12 = None
# ttnn_to_torch_33 = ttnn_decorators_ttnn_to_torch(ttnn_relu_23);  ttnn_relu_23 = None
# convolution_default_34 = torch.ops.aten.convolution.default(ttnn_to_torch_33, arg102_1, None, [2, 2], [1, 1], [1, 1], False, [0, 0], 1);  ttnn_to_torch_33 = arg102_1 = None
# Don't know why mul cause failed

aten_mul_Tensor_blocklist += [
    ["Tensor<[56]> self = ?", "Tensor other = 0.5"],
    ["Tensor<[56]> self = ?", "Tensor other = 0.25"],
    ["Tensor<[28]> self = ?", "Tensor other = 0.5"],
    ["Tensor<[56]> self = ?", "Tensor other = 0.125"],
    ["Tensor<[28]> self = ?", "Tensor other = 0.25"],
    ["Tensor<[14]> self = ?", "Tensor other = 0.5"],
]

# hrnet_w18.ms_aug_in1k train
#     def __call__(self, *args, **kwargs):
# >       return self._op(*args, **(kwargs or {}))
# RuntimeError: Index put requires the source and destination dtypes match, got Float for the destination and BFloat16 for the source.


############################################################
# EXTRA BLOCKLIST OF ViLT
############################################################
# see issue #390
# RuntimeError: _unsafe_index found unexpected index type BFloat16
# arange => add => mul => to_copy => unsafe_index

aten_add_Tensor_blocklist += [
    ["Tensor<[12]> self = ?", "Tensor other = 0.0"],
    ["Tensor<[16]> self = ?", "Tensor other = 0.0"],
]

aten_mul_Tensor_blocklist += [
    ["Tensor<[12]> self = ?", "Tensor other = 32.0"],
    ["Tensor<[16]> self = ?", "Tensor other = 32.0"],
]

############################################################
# EXTRA BLOCKLIST OF Whisper
############################################################
# embedding
# RuntimeError: Expected tensor for argument #1 'indices'
# to have one of the following scalar types: Long, Int; but got CPUB...
# ones = torch.ops.aten.ones.default([1, 1], dtype = torch.int64, device = device(type='cpu'), pin_memory = False)
# mul = torch.ops.aten.mul.Tensor(ones, 50258);  ones = None
# view_192 = torch.ops.aten.view.default(mul, [-1, 1]);  mul = None
# embedding = torch.ops.aten.embedding.default(arg188_1, view_192, 50257);  arg188_1 = view_192 = None

aten_mul_Tensor_blocklist += [["Tensor<[1, 1]> self = ?", "Tensor other = 50258"]]

# torch._dynamo.exc.BackendCompilerFailed: backend='ttnn_backend' raised:
# RuntimeError: aten::clone() Expected a value of type 'Tensor' for argument 'self' but instead found type 'SymInt'.
# Position: 0
# Value: s1
# Declaration: aten::clone(Tensor self, *, MemoryFormat? memory_format=None) -> Tensor
# Cast error details: Unable to cast s1 to Tensor
# TODO: not pass yet

############################################################
# EXTRA BLOCKLIST OF GPTNeo
############################################################
# RuntimeError: TT_FATAL @ xxx/ttnn/cpp/ttnn/operations/data_movement/slice/slice.cpp:110:
# modified_ends[idx] >= modified_begins[idx]

aten_select_int_blocklist = [["Tensor<[1, 45]> self = ?", "int dim = 1", "int index = -1"]]

# ERROR tests/models/gpt_neo/test_gpt_neo.py::test_gpt_neo[eval], see issue #503
# RuntimeError: probability tensor contains either `inf`, `nan` or element < 0
# TODO: not pass yet

############################################################
# EXTRA BLOCKLIST OF codegen
############################################################
# ttnn.from_torch(torch.tensor(False)) => ttnn.gt
# ttnn.from_torch not support sclar of bool dtype
# RuntimeError: TT_FATAL @ tensor/types.cpp:209: normalized_index >= 0 and normalized_index < rank
# not lowering ttnn.gt to avoid ttnn.from_torch of sclar of bool dtype
aten_gt_Scalar_blocklist = [["Tensor<[]> self = ?", "number other = 0"]]

# torch._dynamo.exc.BackendCompilerFailed: backend='ttnn_backend' raised:
# RuntimeError: aten::clone() Expected a value of type 'Tensor' for argument 'self' but instead found type 'SymInt'.
# Position: 0
# Value: s0
# Declaration: aten::clone(Tensor self, *, MemoryFormat? memory_format=None) -> Tensor
# Cast error details: Unable to cast s0 to Tensor
# TODO: not pass yet

############################################################
# EXTRA BLOCKLIST OF FLAN-T5
############################################################
# This div converted to reciprocal & mul, and reciprocal show this err msg:
# TypeError: __call__(): incompatible function arguments. The following argument types are supported: ...
aten_div_Tensor_blocklist += [["Tensor<[1, 1]> self = ?", "Tensor other = 16"]]

# torch._dynamo.exc.BackendCompilerFailed: backend='ttnn_backend' raised:
# Exception: unhashable type: non-singleton SymInt
# TODO: not pass yet

############################################################
# EXTRA BLOCKLIST OF GLPN-KITTI
############################################################
# index out of bound, see issue #420
# clamp => unsqueeze => unsafe_index
aten_unsqueeze_default_blocklist = [["Tensor<[240]> self = ?", "int dim = 1"]]

# IndexError: shape mismatch: indexing tensors could not be broadcast together with shapes [1, 1, 240], [1, 320]
# guess is issue #390
# TODO: not pass yet

############################################################
# EXTRA BLOCKLIST OF OPT
############################################################

# ttnn.from_torch(torch.tensor(-3.3895e+38)) => ttnn.maximum
# ttnn.from_torch not support scalar
# RuntimeError: TT_FATAL @ tensor/types.cpp:209: normalized_index >= 0 and normalized_index < rank
# not lowering ttnn.maximum to avoid ttnn.from_torch of scalar
aten_maximum_default_blocklist += [["Tensor<[1, 16, 59, 59]> self = ?", "Tensor other = ?"]]

# torch._dynamo.exc.BackendCompilerFailed: backend='ttnn_backend' raised:
# RuntimeError: aten::clone() Expected a value of type 'Tensor' for argument 'self' but instead found type 'SymInt'.
# Position: 0
# Value: s0
# Declaration: aten::clone(Tensor self, *, MemoryFormat? memory_format=None) -> Tensor
# Cast error details: Unable to cast s0 to Tensor
# TODO: not pass yet

############################################################
# EXTRA BLOCKLIST OF t5
############################################################
# torch._dynamo.exc.BackendCompilerFailed: backend='ttnn_backend' raised:
# Exception: unhashable type: non-singleton SymInt
# TODO: not pass yet

############################################################
# EXTRA BLOCKLIST OF DETR
############################################################
# TypeError: __call__(): incompatible function arguments. The following argument types are supported:
#     1. (self: ttnn._ttnn.operations.moreh.moreh_cumsum_t, input: ttnn._ttnn.tensor.Tensor, dim: int, *, output: Optional[ttnn._ttnn.tensor.Tensor] = None, memory_config: Optional[ttnn._ttnn.tensor.MemoryConfig] = None, compute_kernel_config: Optional[Union[ttnn._ttnn.operations.core.GrayskullComputeKernelConfig, ttnn._ttnn.operations.core.WormholeComputeKernelConfig]] = None) -> ttnn._ttnn.tensor.Tensor
#
# Invoked with: <ttnn._ttnn.operations.moreh.moreh_cumsum_t object at 0x7faef0b78b30>, ttnn.Tensor([[[[ 0.00000,  0.00000,  ...,  0.00000,  0.00000],
#               ...,
#                [ 0.00000,  0.00000,  ...,  0.00000,  0.00000]]]], shape=Shape([1, 23, 40[64], 1[32]]), dtype=DataType::BFLOAT16, layout=Layout::TILE), 1; kwargs: dtype=torch.float32
aten_cumsum_default_blocklist = [["Tensor<[1, 23, 40]> self = ?", "int dim = 1", "Optional[int] dtype = torch.float32"]]

# TypeError: __call__(): incompatible function arguments. The following argument types are supported:
#     1. (self: ttnn._ttnn.operations.unary.reciprocal_t, input_tensor: ttnn._ttnn.tensor.Tensor, *, memory_config: Optional[ttnn._ttnn.tensor.MemoryConfig] = None, output_tensor: Optional[ttnn._ttnn.tensor.Tensor] = None, queue_id: int = 0) -> ttnn._ttnn.tensor.Tensor
#     2. (self: ttnn._ttnn.operations.unary.reciprocal_t, input_tensor: ttnn::operations::complex::ComplexTensor, *, memory_config: ttnn._ttnn.tensor.MemoryConfig) -> ttnn::operations::complex::ComplexTensor
#
# Invoked with: <ttnn._ttnn.operations.unary.reciprocal_t object at 0x7f08ea7a0e30>, 128
aten_div_Tensor_blocklist += [["Tensor<[128]> self = ?", "Tensor other = 128"]]

# RuntimeError: TT_FATAL @ binary_device_operation.cpp:68: input_tensor_a.get_layout() == Layout::TILE
# info:
# Input to eltwise binary must be tilized
# zero_like([1, 920]) & subtract([1[32], 920[928]]) => mul
aten_zeros_like_default_blocklist += [
    ["Tensor<[1, 920]> self = ?", "Optional[int] dtype = torch.bfloat16", "Optional[bool] pin_memory = False"],
    ["Tensor<[100, 1, 256]> self = ?", "Optional[bool] pin_memory = False"],
]


############################################################
# EXTRA BLOCKLIST OF ssd300_vgg16
############################################################
# IndexError: index 480 is out of bounds for dimension 0 with size 480, see issue #420
# add => multiply => subtract => unsqueeze
aten_add_Tensor_blocklist += [["Tensor<[300]> self = ?", "Tensor other = 0.5"]]
aten_mul_Tensor_blocklist += [["Tensor<[300]> self = ?", "Tensor other = 1.6"]]
aten_sub_Tensor_blocklist += [["Tensor<[300]> self = ?", "Tensor other = 0.5"]]
aten_unsqueeze_default_blocklist += [["Tensor<[300]> self = ?", "int dim = 1"]]
# RuntimeError: expected scalar type BFloat16 but found Float
# convolution_default_5 weight dtype is float32, this is
# because RuntimeError: "nms_kernel" not implemented for 'BFloat16' so cannot model.to(torch.bfloat16)
# TODO: not pass yet

############################################################
# EXTRA BLOCKLIST OF ssdlite320_mobilenet_v3_large
############################################################
# IndexError: IndexError: index 640 is out of bounds for dimension 1 with size 640, see issue #420
# add => multiply => subtract => unsqueeze
aten_add_Tensor_blocklist += [["Tensor<[320]> self = ?", "Tensor other = 0.5"]]
aten_mul_Tensor_blocklist += [
    ["Tensor<[320]> self = ?", "Tensor other = 1.5"],
    ["Tensor<[320]> self = ?", "Tensor other = 2.0"],
]
aten_sub_Tensor_blocklist += [["Tensor<[320]> self = ?", "Tensor other = 0.5"]]
aten_unsqueeze_default_blocklist += [["Tensor<[320]> self = ?", "int dim = 1"]]
# tt_metal/common/math.hpp:16: b > 0
# Divide by 0 error
aten_convolution_default_blocklist += [
    [
        "Tensor<[1, 128, 5, 5]> input = ?",
        "Tensor<[128, 1, 3, 3]> weight = ?",
        "Optional[Tensor] bias = ?",
        "List[int] stride = [2, 2]",
        "List[int] padding = [1, 1]",
        "List[int] dilation = [1, 1]",
        "bool transposed = False",
        "List[int] output_padding = [0, 0]",
        "int groups = 128",
    ]
]

# RuntimeError: expected scalar type BFloat16 but found Float
# convolution_default_66 weight dtype is float32, this is
# because RuntimeError: "nms_kernel" not implemented for 'BFloat16' so cannot model.to(torch.bfloat16)
# TODO: not pass yet

############################################################
# EXTRA BLOCKLIST OF MobileNetSSD
############################################################
# IndexError: index 320 is out of bounds for dimension 0 with size 320, see issue #420
# add => multiply => subtract => unsqueeze
aten_add_Tensor_blocklist += [["Tensor<[320]> self = ?", "Tensor other = 0.5"]]
aten_mul_Tensor_blocklist += [["Tensor<[320]> self = ?", "Tensor other = 1.0"]]
aten_sub_Tensor_blocklist += [["Tensor<[320]> self = ?", "Tensor other = 0.5"]]
aten_unsqueeze_default_blocklist += [["Tensor<[320]> self = ?", "int dim = 1"]]
# RuntimeError: expected scalar type BFloat16 but found Float
# convolution_default_66 weight dtype is float32, this is
# because RuntimeError: "nms_kernel" not implemented for 'BFloat16' so cannot model.to(torch.bfloat16)
# TODO: not pass yet

############################################################
# EXTRA BLOCKLIST OF retinanet_resnet50_fpn
############################################################
# IndexError: index 480 is out of bounds for dimension 0 with size 480, see issue #420
aten_add_Tensor_blocklist += [["Tensor<[800]> self = ?", "Tensor other = 0.5"]]
aten_mul_Tensor_blocklist += [["Tensor<[800]> self = ?", "Tensor other = 0.6"]]
aten_sub_Tensor_blocklist += [["Tensor<[800]> self = ?", "Tensor other = 0.5"]]
aten_unsqueeze_default_blocklist += [["Tensor<[800]> self = ?", "int dim = 1"]]
# RuntimeError: expected scalar type BFloat16 but found Float
# convolution_default weight dtype is float32, this is
# because RuntimeError: "nms_kernel" not implemented for 'BFloat16' so cannot model.to(torch.bfloat16)
# TODO: not pass yet


############################################################
# EXTRA BLOCKLIST OF retinanet_resnet50_fpn_v2
############################################################
# RuntimeError: expected scalar type BFloat16 but found Float
# convolution_default weight dtype is float32, this is
# because RuntimeError: "nms_kernel" not implemented for 'BFloat16' so cannot model.to(torch.bfloat16)
# TODO: not pass yet

############################################################
# EXTRA BLOCKLIST OF RoBERTa
############################################################
# RuntimeError: TT_FATAL @ xxx/embedding.cpp:32: input_tensor_arg.get_layout() == ttnn::ROW_MAJOR_LAYOUT
# info:
# Indices tensor must be in row major layout.
# ttnn_embedding = ttnn_decorators_ttnn_embedding(ttnn_from_torch_2, ttnn_to_device_3, layout = ttnn_ROW_MAJOR_LAYOUT)
# (Pdb) ttnn_from_torch_2.layout
# <Layout.TILE: 1>
aten_embedding_default_blocklist = [
    ["Tensor<[250002, 768]> weight = ?", "Tensor<[1, 10]> indices = ?", "int padding_idx = 1"]
]

############################################################

GUARD[torch.ops.aten.add.Tensor] = partial(guard_aten, aten_add_Tensor_blocklist)
GUARD[torch.ops.aten.view.default] = partial(guard_aten, aten_view_default_blocklist)
GUARD[torch.ops.aten.select.int] = partial(guard_aten, aten_select_int_blocklist)
GUARD[torch.ops.aten.gt.Scalar] = partial(guard_aten, aten_gt_Scalar_blocklist)
GUARD[torch.ops.aten.unsqueeze.default] = partial(guard_aten, aten_unsqueeze_default_blocklist)
GUARD[torch.ops.aten.cumsum.default] = partial(guard_aten, aten_cumsum_default_blocklist)
GUARD[torch.ops.aten.embedding.default] = partial(guard_aten, aten_embedding_default_blocklist)


def can_lowering_to_ttnn(node):
    if node.target in GUARD:
        return GUARD[node.target](node)

    return True

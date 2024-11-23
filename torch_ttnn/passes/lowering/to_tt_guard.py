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
# EXTRA BLOCKLIST OF XGLM
############################################################
# see issue #361
# For valid non-interleaved buffers page size 38 must equal buffer size 720.
# For interleaved-buffers page size should be divisible by buffer size
aten_masked_fill_scalar_blocklist += [
    ["Tensor<[1, 1, 19, 19]> self = ?", "Tensor<[1, 1, 19, 19]> mask = ?", "number value = -3.3895313892515355e+38"]
]

############################################################
# EXTRA BLOCKLIST OF FALCON
############################################################

aten_masked_fill_scalar_blocklist += [["Tensor<[7, 7]> self = ?", "Tensor<[7, 7]> mask = ?", "number value = -inf"]]

############################################################
# EXTRA BLOCKLIST OF swin_*
############################################################
# swin_b
# This input vars become pass without blocking, and if blocking, the err msg shown:
# RuntimeError: view size is not compatible with input tensor's size and stride
# (at least one dimension spans across two contiguous subspaces). Use .reshape(...) instead.

# TT_FATAL @ .../buffer.cpp:41: page_size % sizeof(uint32_t) == 0

# see issue #361
aten_masked_fill_scalar_blocklist += [
    ["Tensor<[64, 49, 49]> self = ?", "Tensor<[64, 49, 49]> mask = ?", "number value = -100.0"],
    ["Tensor<[64, 49, 49]> self = ?", "Tensor<[64, 49, 49]> mask = ?", "number value = 0.0"],
    ["Tensor<[16, 49, 49]> self = ?", "Tensor<[16, 49, 49]> mask = ?", "number value = -100.0"],
    ["Tensor<[16, 49, 49]> self = ?", "Tensor<[16, 49, 49]> mask = ?", "number value = 0.0"],
    ["Tensor<[4, 49, 49]> self = ?", "Tensor<[4, 49, 49]> mask = ?", "number value = -100.0"],
    ["Tensor<[4, 49, 49]> self = ?", "Tensor<[4, 49, 49]> mask = ?", "number value = 0.0"],
]


############################################################
# EXTRA BLOCKLIST OF vgg*
############################################################
# see issue #362
# vgg11
# aten::_adaptive_avg_pool2d => aten::view
# if aten avgpool lowering to ttnn avgpool,
# then its output shape become torch.Size([1, 1, 1, 7]) and cause aten::view error
# RuntimeError: shape '[1, 25088]' is invalid for input of size 7
# vgg11/vgg11_bn/vgg13/vgg13_bn/vgg16/vgg16_bn/vgg19/vgg19_bn all have this input var
aten__adaptive_avg_pool2d_default_blocklist = [["Tensor<[1, 512, 7, 7]> self = ?", "List[int] output_size = [7, 7]"]]


############################################################
# EXTRA BLOCKLIST OF t5*
############################################################


############################################################
# EXTRA BLOCKLIST OF retinanet_resnet50_fpn*
############################################################

# retinanet_resnet50_fpn
# RuntimeError: Missing conversion from torch.dtype: torch.int32 to Ttnn dtype.
# => comment ttnn_dtype = torch_dtype_to_ttnn_dtype(arg_metadata.dtype), it is not used now

# RuntimeError: _unsafe_index found unexpected index type BFloat16
# ... => aten::sub.Tensor => aten::div.Tensor => unsqueeze => unsafe_index
# it is too long to block, so just wait the to_tt_pass fix

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
# E       RuntimeError: Expected 4-dimensional input for 4-dimensional weight [18, 18, 3, 3], but got 5-dimensional input of size [1, 18, 18, 56, 56] instead
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
# E       RuntimeError: Index put requires the source and destination dtypes match, got Float for the destination and BFloat16 for the source.


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
# EXTRA BLOCKLIST OF speecht5-tts
############################################################
# see issue 361
# self = FastOperation(python_fully_qualified_name='ttnn.ones',
#   function=<ttnn._ttnn.operations.creation.ones_t object at
#   0x7f6...<function default_postprocess_golden_function_outputs at 0x7f6e7f0ddca0>,
#   is_cpp_operation=True, is_experimental=False)
# function_args = ((1, 1, 24, 24),)
# function_kwargs = {'device': <ttnn._ttnn.device.Device object at 0x7f6e6358bcf0>,
#   'dtype': <DataType.BFLOAT16: 0>, 'layout': <Layout.TILE: 1>}

#     def __call__(self, *function_args, **function_kwargs):
# >       return self.function(*function_args, **function_kwargs)
# E       RuntimeError: TT_FATAL @ .../functions.hpp:66: shape[-1] % tt::constants::TILE_WIDTH == 0

# torch.ops.aten.masked_fill.Scalar is converted as ttnn.ones and it is failed at single op test

aten_masked_fill_scalar_blocklist += [
    [
        "Tensor<[1, 1, 24, 24]> self = ?",
        "Tensor<[1, 1, 24, 24]> mask = ?",
        "number value = -3.3895313892515355e+38",
    ],
    ["Tensor<[1, 1, 1, 24]> self = ?", "Tensor<[1, 1, 1, 24]> mask = ?", "number value = -3.3895313892515355e+38"],
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
# TODO: not pass yet

aten_mul_Tensor_blocklist += [["Tensor<[1, 1]> self = ?", "Tensor other = 50258"]]


############################################################
# EXTRA BLOCKLIST OF GPTNeo
############################################################
# RuntimeError: TT_FATAL @ xxx/ttnn/cpp/ttnn/operations/data_movement/slice/slice.cpp:110:
# modified_ends[idx] >= modified_begins[idx]

aten_select_int_blocklist = [["Tensor<[1, 45]> self = ?", "int dim = 1", "int index = -1"]]

# ERROR tests/models/gpt_neo/test_gpt_neo.py::test_gpt_neo[eval] -
# RuntimeError: probability tensor contains either `inf`, `nan` or element < 0

############################################################

GUARD[torch.ops.aten.add.Tensor] = partial(guard_aten, aten_add_Tensor_blocklist)
GUARD[torch.ops.aten._adaptive_avg_pool2d.default] = partial(guard_aten, aten__adaptive_avg_pool2d_default_blocklist)
GUARD[torch.ops.aten.view.default] = partial(guard_aten, aten_view_default_blocklist)
GUARD[torch.ops.aten.select.int] = partial(guard_aten, aten_select_int_blocklist)


def can_lowering_to_ttnn(node):
    if node.target in GUARD:
        return GUARD[node.target](node)

    return True

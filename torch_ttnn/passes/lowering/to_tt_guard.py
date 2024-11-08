from functools import partial
from .to_tt_guard_autogen import *

############################################################
# EXTRA BLOCKLIST OF CLIP
############################################################
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
    ["Tensor<[9, 30000]> self = ?", "List[int] size = [1, 9, 30000]"],
    ["Tensor<[9, 8192]> self = ?", "List[int] size = [1, 9, 8192]"],
    ["Tensor<[1, 9, 8192]> self = ?", "List[int] size = [9, 8192]"],
    ["Tensor<[9, 16384]> self = ?", "List[int] size = [1, 9, 16384]"],
    ["Tensor<[1, 9, 16384]> self = ?", "List[int] size = [9, 16384]"],
    ["Tensor<[7, 18176]> self = ?", "List[int] size = [1, 7, 18176]"],
    ["Tensor<[1, 7, 18176]> self = ?", "List[int] size = [7, 18176]"],
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

############################################################
# EXTRA BLOCKLIST OF microsoft/beit-*-patch16-224
############################################################
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
aten_view_default_blocklist.remove(["Tensor<[64, 49, 128]> self = ?", "List[int] size = [3136, 128]"])
aten_view_default_blocklist.remove(["Tensor<[1, 56, 56, 128]> self = ?", "List[int] size = [3136, 128]"])
aten_view_default_blocklist.remove(["Tensor<[1, 56, 56, 512]> self = ?", "List[int] size = [3136, 512]"])

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

# swin_t
aten_view_default_blocklist.remove(["Tensor<[64, 49, 96]> self = ?", "List[int] size = [3136, 96]"])
aten_view_default_blocklist.remove(["Tensor<[1, 56, 56, 96]> self = ?", "List[int] size = [3136, 96]"])
aten_view_default_blocklist.remove(["Tensor<[1, 56, 56, 384]> self = ?", "List[int] size = [3136, 384]"])

# swin_s
# swin_v2_t
aten__unsafe_view_default_blocklist.remove(["Tensor<[1, 8, 8, 8, 8, 96]> self = ?", "List[int] size = [64, 64, 96]"])
aten__unsafe_view_default_blocklist.remove(["Tensor<[1, 8, 8, 8, 8, 96]> self = ?", "List[int] size = [1, 64, 64, 96]"])
aten__unsafe_view_default_blocklist.remove(["Tensor<[8, 8, 8, 8]> self = ?", "List[int] size = [64, 64]"])
aten__unsafe_view_default_blocklist.remove(["Tensor<[1, 4, 4, 8, 8, 192]> self = ?", "List[int] size = [16, 64, 192]"])
aten__unsafe_view_default_blocklist.remove(
    ["Tensor<[1, 4, 8, 4, 8, 192]> self = ?", "List[int] size = [1, 32, 32, 192]"]
)
aten__unsafe_view_default_blocklist.remove(["Tensor<[1, 2, 2, 8, 8, 384]> self = ?", "List[int] size = [4, 64, 384]"])

aten_view_default_blocklist.remove(["Tensor<[1, 16, 16, 384]> self = ?", "List[int] size = [256, 384]"])
aten_view_default_blocklist.remove(["Tensor<[1, 16, 16, 1536]> self = ?", "List[int] size = [256, 1536]"])
aten_view_default_blocklist.remove(["Tensor<[1, 8, 8, 768]> self = ?", "List[int] size = [64, 768]"])
aten_view_default_blocklist.remove(["Tensor<[1, 8, 8, 3072]> self = ?", "List[int] size = [64, 3072]"])
# swin_v2_s
# swin_v2_b
aten__unsafe_view_default_blocklist.remove(["Tensor<[1, 8, 8, 8, 8, 128]> self = ?", "List[int] size = [64, 64, 128]"])
aten__unsafe_view_default_blocklist.remove(
    ["Tensor<[1, 8, 8, 8, 8, 128]> self = ?", "List[int] size = [1, 64, 64, 128]"]
)
aten__unsafe_view_default_blocklist.remove(["Tensor<[1, 4, 4, 8, 8, 256]> self = ?", "List[int] size = [16, 64, 256]"])
aten__unsafe_view_default_blocklist.remove(
    ["Tensor<[1, 4, 8, 4, 8, 256]> self = ?", "List[int] size = [1, 32, 32, 256]"]
)
aten__unsafe_view_default_blocklist.remove(["Tensor<[1, 2, 2, 8, 8, 512]> self = ?", "List[int] size = [4, 64, 512]"])

aten_view_default_blocklist.remove(["Tensor<[1, 16, 16, 512]> self = ?", "List[int] size = [256, 512]"])
aten_view_default_blocklist.remove(["Tensor<[1, 16, 16, 2048]> self = ?", "List[int] size = [256, 2048]"])
aten_view_default_blocklist.remove(["Tensor<[1, 8, 8, 1024]> self = ?", "List[int] size = [64, 1024]"])
aten_view_default_blocklist.remove(["Tensor<[1, 8, 8, 4096]> self = ?", "List[int] size = [64, 4096]"])

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

# aten::view => aten::embedding
# current aten::view output shape will be bf16 if it convert to ttnn op
# and will caue emb error
# E       RuntimeError: Expected tensor for argument #1 'indices' to have
# one of the following scalar types: Long, Int; but got CPUBFloat16Type instead
# (while checking arguments for embedding)
aten_view_default_blocklist += [["Tensor<[1, 10]> self = ?", "List[int] size = [-1, 10]"]]

# TODO: Another pattern is
# aten::arange => aten::unsqueeze => aten::slice.Tensor => aten::sub.Tensor
# => aten::gt.Scalar => aten::_to_copy => aten::mul.Tensor => aten::add.Tensor
# => aten::add.Tensor => aten::embedding
# it is too long to block, so just wait the to_tt_pass fix

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

aten_view_default_blocklist += [["Tensor<[1, 1]> self = ?", "List[int] size = [-1, 1]"]]


############################################################
# EXTRA BLOCKLIST OF microsoft/beit-*-patch16-224-train
############################################################
# see issue #364
# microsoft/beit-base-patch16-224
# self = FastOperation(python_fully_qualified_name='ttnn.permute', ...)
# function_args = (ttnn.Tensor(<buffer is not allocated>,
# shape=Shape([1, 1[32], 1000[1024]]), dtype=DataType::BFLOAT16, layout=Layout::TILE), (1, 0))
# function_kwargs = {}
# RuntimeError: TT_FATAL @ .../permute.cpp:170: input_rank == dims.size()
# don't know why block aten.mean can avoid this error
aten_mean_dim_blocklist = [["Tensor<[1, 196, 768]> self = ?", "Optional[List[int]] dim = [1]"]]
# microsoft/beit-large-patch16-224: same issue
aten_mean_dim_blocklist += [["Tensor<[1, 196, 1024]> self = ?", "Optional[List[int]] dim = [1]"]]

############################################################

GUARD[torch.ops.aten.add.Tensor] = partial(guard_aten, aten_add_Tensor_blocklist)
GUARD[torch.ops.aten._to_copy.default] = partial(guard_aten, aten__to_copy_default_blocklist)
GUARD[torch.ops.aten._adaptive_avg_pool2d.default] = partial(guard_aten, aten__adaptive_avg_pool2d_default_blocklist)
GUARD[torch.ops.aten.mean.dim] = partial(guard_aten, aten_mean_dim_blocklist)


def can_lowering_to_ttnn(node):
    if node.target in GUARD:
        return GUARD[node.target](node)

    return True

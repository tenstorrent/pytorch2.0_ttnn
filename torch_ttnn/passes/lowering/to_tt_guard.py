from functools import partial
from .to_tt_guard_autogen import *

############################################################
# EXTRA BLOCKLIST OF Whisper
############################################################
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
# torch._dynamo.exc.BackendCompilerFailed: backend='ttnn_backend' raised:
# RuntimeError: aten::clone() Expected a value of type 'Tensor' for argument 'self' but instead found type 'SymInt'.
# Position: 0
# Value: s0
# Declaration: aten::clone(Tensor self, *, MemoryFormat? memory_format=None) -> Tensor
# Cast error details: Unable to cast s0 to Tensor
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
# EXTRA BLOCKLIST OF OPT
############################################################
# ttnn.from_torch(torch.tensor(-3.3895e+38)) => ttnn.maximum
# ttnn.from_torch not support scalar
# RuntimeError: TT_FATAL @ tensor/types.cpp:209: normalized_index >= 0 and normalized_index < rank
# not lowering ttnn.maximum to avoid ttnn.from_torch of scalar
# aten_maximum_default_blocklist += [["Tensor<[1, 16, 59, 59]> self = ?", "Tensor other = ?"]]

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

############################################################
# EXTRA BLOCKLIST OF retinanet_resnet50_fpn
############################################################
# Statically allocated circular buffers on core range [(x=0,y=0) - (x=0,y=0)] grow to 3580704 B which is beyond max L1 size of 1499136 B
aten_aten_stack_default = [
    ["List[Tensor] tensors = [<[13600]>, <[13600]>, <[13600]>, <[13600]>]", "int dim = 1"],
]

############################################################
# EXTRA BLOCKLIST OF falcon-7b-instruct
############################################################
# Statically allocated circular buffers on core range [(x=0,y=0) - (x=0,y=0)] grow to 3580704 B which is beyond max L1 size of 1499136 B
aten_arange_start_step = [
    [
        "number start = 7",
        "number end = 0",
        "number step = -1",
        "Optional[Device] device = cpu",
        "Optional[bool] pin_memory = False",
    ]
]
aten_argmax_default_blocklist += [["Tensor<[1, 7]> self = ?", "Optional[int] dim = 1", "bool keepdim = True"]]

############################################################
# EXTRA BLOCKLIST OF retinanet_resnet50_fpn_v2
############################################################
# Statically allocated circular buffers on core range [(x=0,y=0) - (x=0,y=0)] grow to 3580704 B which is beyond max L1 size of 1499136 B
# TODO: not pass yet

############################################################

GUARD[torch.ops.aten.gt.Scalar] = partial(guard_aten, aten_gt_Scalar_blocklist)
GUARD[torch.ops.aten.cumsum.default] = partial(guard_aten, aten_cumsum_default_blocklist)
GUARD[torch.ops.aten.stack.default] = partial(guard_aten, aten_aten_stack_default)
GUARD[torch.ops.aten.arange.start_step] = partial(guard_aten, aten_arange_start_step)


def can_lowering_to_ttnn(node):
    if node.target in GUARD:
        return GUARD[node.target](node)

    return True

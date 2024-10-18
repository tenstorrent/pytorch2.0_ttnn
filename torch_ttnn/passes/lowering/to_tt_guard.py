import torch
import torch_ttnn.metrics as metrics


def get_inputs(node):
    node_inputs = metrics.collect_input_variation_from_node(node)
    if type(node_inputs) == metrics.InputVariation:
        return node_inputs.inputs
    elif type(node_inputs) == metrics.ConvertedInput:
        return node_inputs.original_input_variation.inputs
    else:
        return None


def aten_exp_default(node):
    inputs = get_inputs(node)
    size_len = len(inputs[0].shape_.size())
    # ttnn seems not accept scalar now
    if size_len == 0:
        return False
    return True


def aten_expand_default(node):
    # TODO: find root cause
    blacklist = [[[768], [1, 1, -1]], [[1, 1, 7, 7], [2, 1, 7, 7]], [[2, 1, 1, 7], [2, 1, 7, 7]]]
    inputs = get_inputs(node)
    self_shape = list(inputs[0].shape_.size())
    size = inputs[1].value_
    if [self_shape, size] in blacklist:
        return False
    return True


def aten_full_default(node):
    # For valid non-interleaved buffers page size 2048 must equal buffer size 96.
    # For interleaved-buffers page size should be divisible by buffer size
    # TODO: find root cause
    blacklist = [[7, 7]]
    inputs = get_inputs(node)
    size = inputs[0].value_
    if size in blacklist:
        return False
    return True


def aten_mul_tensor(node):
    inputs = get_inputs(node)
    # ttnn seems not accept scalar now
    try:
        size0_len = len(inputs[0].shape_.size())
        if size0_len == 0:
            return False
    except:
        pass
    try:
        size1_len = len(inputs[1].shape_.size())
        if size1_len == 0:
            return False
    except:
        pass
    return True


def aten_rsub_scalar(node):
    # TODO: find root cause
    blacklist = [[2, 1, 7, 7]]
    inputs = get_inputs(node)
    shape = list(inputs[0].shape_.size())
    if shape in blacklist:
        return False
    return True


def aten_slice_tensor(node):
    # TODO: find root cause
    blacklist = [[[1, 77], 1], [[1, 50, 768], 1]]
    inputs = get_inputs(node)
    # ttnn seems not accept scalar now
    shape = list(inputs[0].shape_.size())
    dim = inputs[1].value_
    if [shape, dim] in blacklist:
        return False
    return True


def aten_t_default(node):
    # TODO: find root cause
    blacklist = [[2, 1], [512, 1]]
    inputs = get_inputs(node)
    shape = list(inputs[0].shape_.size())
    if shape in blacklist:
        return False
    return True


def aten_transpose_int(node):
    # TODO: find root cause
    blacklist = [[[1, 768, 49], 1, 2], [[1, 49, 768], 1, 2], [[16, 64, 7], 1, 2], [[16, 7, 7], 1, 2]]
    inputs = get_inputs(node)
    # ttnn seems not accept scalar now
    shape = list(inputs[0].shape_.size())
    dim0 = inputs[1].value_
    dim1 = inputs[2].value_
    if [shape, dim0, dim1] in blacklist:
        return False
    return True


def aten__softmax_default(node):
    # TODO: find root cause
    blacklist = [
        ["Tensor<[12, 50, 50]> self = ?", "int dim = -1", "bool half_to_float = False"],
        ["Tensor<[16, 7, 7]> self = ?", "int dim = -1", "bool half_to_float = False"],
    ]
    inputs = get_inputs(node)
    inputs_str = [str(i) for i in inputs]
    if inputs_str in blacklist:
        return False
    return True


def aten__unsafe_view_default(node):
    # TODO: find root cause
    blacklist = [
        ["Tensor<[1, 50, 12, 64]> self = ?", "List[int] size = [1, 50, 768]"],
        ["Tensor<[2, 7, 8, 64]> self = ?", "List[int] size = [2, 7, 512]"],
    ]
    inputs = get_inputs(node)
    inputs_str = [str(i) for i in inputs]
    if inputs_str in blacklist:
        return False
    return True


def aten_view_default(node):
    # TODO: find root cause
    blacklist = [
        ["Tensor<[1, 50, 768]> self = ?", "List[int] size = [1, -1, 12, 64]"],
        ["Tensor<[1, 50, 768]> self = ?", "List[int] size = [1, 50, 12, 64]"],
        ["Tensor<[2, 7, 512]> self = ?", "List[int] size = [2, -1, 8, 64]"],
        ["Tensor<[2, 7, 512]> self = ?", "List[int] size = [2, 7, 8, 64]"],
        ["Tensor<[1, 50, 12, 64]> self = ?", "List[int] size = [1, 50, 768]"],
        ["Tensor<[1, 50, 768]> self = ?", "List[int] size = [1, -1, 12, 64]"],
        ["Tensor<[1, 50, 768]> self = ?", "List[int] size = [1, 50, 12, 64]"],
        ["Tensor<[2, 7, 512]> self = ?", "List[int] size = [2, -1, 8, 64]"],
        ["Tensor<[2, 7, 512]> self = ?", "List[int] size = [2, 7, 8, 64]"],
        ["Tensor<[2, 7, 8, 64]> self = ?", "List[int] size = [2, 7, 512]"],
    ]
    inputs = get_inputs(node)
    inputs_str = [str(i) for i in inputs]
    if inputs_str in blacklist:
        return False
    return True


def aten_embedding_dense_backward_default(node):
    # TODO: find root cause
    blacklist = [
        [
            "Tensor<[1, 7, 512]> grad_output = ?",
            "Tensor<[1, 7]> indices = ?",
            "int num_weights = 77",
            "int padding_idx = -1",
            "bool scale_grad_by_freq = False",
        ],
        [
            "Tensor<[2, 7, 512]> grad_output = ?",
            "Tensor<[2, 7]> indices = ?",
            "int num_weights = 49408",
            "int padding_idx = -1",
            "bool scale_grad_by_freq = False",
        ],
        [
            "Tensor<[1, 50, 768]> grad_output = ?",
            "Tensor<[1, 50]> indices = ?",
            "int num_weights = 50",
            "int padding_idx = -1",
            "bool scale_grad_by_freq = False",
        ],
    ]
    inputs = get_inputs(node)
    inputs_str = [str(i) for i in inputs]
    if inputs_str in blacklist:
        return False
    return True


def blocked_aten_mul_tensor(node):
    # TODO: block all input variations from CLIP eval, find root cause
    blacklist = [
        ["Tensor<[1, 50, 768]> self = ?", "Tensor other = 0.125"],
        ["Tensor<[1, 50, 3072]> self = ?", "Tensor other = 1.702"],
        ["Tensor<[1, 50, 3072]> self = ?", "Tensor<[1, 50, 3072]> other = ?"],
        ["Tensor<[2, 7, 512]> self = ?", "Tensor other = 0.125"],
        ["Tensor<[2, 7, 2048]> self = ?", "Tensor other = 1.702"],
        ["Tensor<[2, 7, 2048]> self = ?", "Tensor<[2, 7, 2048]> other = ?"],
        ["Tensor<[2, 1]> self = ?", "Tensor<[]> other = ?"],
    ]
    inputs = get_inputs(node)
    inputs_str = [str(i) for i in inputs]
    if inputs_str in blacklist:
        return False
    return True


def blocked_aten_view_default(node):
    # TODO: block all input variations from CLIP eval, find root cause
    blacklist = [
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
    inputs = get_inputs(node)
    inputs_str = [str(i) for i in inputs]
    if inputs_str in blacklist:
        return False
    return True


def blocked_aten__to_copy_default(node):
    # TODO: block all input variations from CLIP eval, find root cause
    blacklist = [
        ["Tensor<[1, 3, 224, 224]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[7, 7]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[2, 1, 7, 7]> self = ?", "Optional[int] dtype = torch.bfloat16"],
        ["Tensor<[2, 1, 7, 7]> self = ?", "Optional[int] dtype = torch.bool"],
        ["Tensor<[2, 7]> self = ?", "Optional[int] dtype = torch.int32", "Optional[Device] device = cpu"],
    ]
    inputs = get_inputs(node)
    inputs_str = [str(i) for i in inputs]
    if inputs_str in blacklist:
        return False
    return True


def blocked_aten_native_layer_norm_default(node):
    # TODO: block all input variations from CLIP eval, find root cause
    blacklist = [
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
    inputs = get_inputs(node)
    inputs_str = [str(i) for i in inputs]
    if inputs_str in blacklist:
        return False
    return True


def blocked_aten_masked_fill_Scalar(node):
    # TODO: block all input variations from CLIP eval, find root cause
    blacklist = [
        ["Tensor<[2, 1, 7, 7]> self = ?", "Tensor<[2, 1, 7, 7]> mask = ?", "number value = -3.3895313892515355e+38"],
    ]
    inputs = get_inputs(node)
    inputs_str = [str(i) for i in inputs]
    if inputs_str in blacklist:
        return False
    return True


OPLIST = {
    torch.ops.aten.exp.default: aten_exp_default,
    torch.ops.aten.expand.default: aten_expand_default,
    torch.ops.aten.full.default: aten_full_default,
    torch.ops.aten.rsub.Scalar: aten_rsub_scalar,
    torch.ops.aten.slice.Tensor: aten_slice_tensor,
    torch.ops.aten.t.default: aten_t_default,
    torch.ops.aten.transpose.int: aten_transpose_int,
    torch.ops.aten._softmax.default: aten__softmax_default,
    torch.ops.aten._unsafe_view.default: aten__unsafe_view_default,
    # TODO: With CLIP model of eval mode, these four ops are passed in single op tests
    # but failed in model tests, and because don't know which input variation caused the model
    # failed, so block all input variations of these ops
    torch.ops.aten.mul.Tensor: blocked_aten_mul_tensor,
    torch.ops.aten.view.default: blocked_aten_view_default,
    torch.ops.aten._to_copy.default: blocked_aten__to_copy_default,
    torch.ops.aten.native_layer_norm.default: blocked_aten_native_layer_norm_default,
    torch.ops.aten.masked_fill.Scalar: blocked_aten_masked_fill_Scalar,
}


def can_lowering_to_ttnn(node):
    if node.target in OPLIST:
        return OPLIST[node.target](node)

    return True

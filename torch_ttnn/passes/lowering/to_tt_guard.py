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
    blacklist = [[[1, 77], 1]]
    inputs = get_inputs(node)
    # ttnn seems not accept scalar now
    shape = list(inputs[0].shape_.size())
    dim = inputs[1].value_
    if [shape, dim] in blacklist:
        return False
    return True


def aten_t_default(node):
    # TODO: find root cause
    blacklist = [[2, 1]]
    inputs = get_inputs(node)
    shape = list(inputs[0].shape_.size())
    if shape in blacklist:
        return False
    return True


def aten_transpose_int(node):
    # TODO: find root cause
    blacklist = [[[1, 768, 49], 1, 2]]
    inputs = get_inputs(node)
    # ttnn seems not accept scalar now
    shape = list(inputs[0].shape_.size())
    dim0 = inputs[1].value_
    dim1 = inputs[2].value_
    if [shape, dim0, dim1] in blacklist:
        return False
    return True


OPLIST = {
    torch.ops.aten.exp.default: aten_exp_default,
    torch.ops.aten.expand.default: aten_expand_default,
    torch.ops.aten.full.default: aten_full_default,
    torch.ops.aten.mul.Tensor: aten_mul_tensor,
    torch.ops.aten.rsub.Scalar: aten_rsub_scalar,
    torch.ops.aten.slice.Tensor: aten_slice_tensor,
    torch.ops.aten.t.default: aten_t_default,
    torch.ops.aten.transpose.int: aten_transpose_int,
}


def can_lowering_to_ttnn(node):
    if node.target in OPLIST:
        return OPLIST[node.target](node)

    return True

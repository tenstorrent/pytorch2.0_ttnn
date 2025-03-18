import lzma
import numpy as np
import pickle
import torch
import ttnn
from pathlib import Path
aten = torch.ops.aten
@torch.fx.wrap
def clone(t):
    return ttnn.clone(t, memory_config=t.memory_config(), dtype=t.dtype)

@torch.fx.wrap
def stack(tensors, dim, output_shape):
    # Handle negative dims by wrapping around
    dim = (dim + len(output_shape)) % len(output_shape)

    # Create shape for unsqueezed tensors - same as output but with size 1
    # in the stack dimension
    unsqueezed_shape = output_shape.copy()
    unsqueezed_shape[dim] = 1

    # Reshape each input tensor to add the new dimension
    unsqueezed_tensors = []
    for tensor in tensors:
        unsqueezed_tensors.append(ttnn.reshape(tensor, unsqueezed_shape))

    # Concatenate all reshaped tensors along the stack dimension
    return ttnn.concat(unsqueezed_tensors, dim)


ref = globals()["clone"]
globals()["clone_wrapper"] = ref
del globals()["clone"]


ref = globals()["stack"]
globals()["stack_wrapper"] = ref
del globals()["stack"]

def comp_pcc(golden, calculated, pcc=0.99):
    golden = torch.Tensor(golden)
    calculated = torch.Tensor(calculated)

    if golden.dtype != calculated.dtype:
        calculated = calculated.type(golden.dtype)

    if torch.all(torch.isnan(golden)) and torch.all(torch.isnan(calculated)):
        # logger.warning("Both tensors are 'nan'")
        return True, 1.0

    if torch.all(torch.isnan(golden)) or torch.all(torch.isnan(calculated)):
        # logger.error("One tensor is all nan, the other is not.")
        return False, 0.0

    # Test if either is completely zero
    if torch.any(golden.bool()) != torch.any(calculated.bool()):
        # logger.error("One tensor is all zero")
        return False, 0.0

    # For now, mask all infs and nans so that we check the rest... TODO
    golden = golden.clone()
    golden[
        torch.logical_or(
            torch.isnan(golden),
            torch.logical_or(torch.isinf(golden), torch.isneginf(golden)),
        )
    ] = 0
    calculated = calculated.clone()
    calculated[
        torch.logical_or(
            torch.isnan(calculated),
            torch.logical_or(torch.isinf(calculated), torch.isneginf(calculated)),
        )
    ] = 0

    if torch.equal(golden, calculated):
        return True, 1.0

    if golden.dtype == torch.bfloat16:
        golden = golden.type(torch.float32)
        calculated = calculated.type(torch.float32)
    cal_pcc = np.min(
        np.ma.corrcoef(
            np.ma.masked_invalid(torch.squeeze(golden).detach().numpy()).flatten(),
            np.ma.masked_invalid(torch.squeeze(calculated).detach().numpy()).flatten(),
        )
    )

    if isinstance(cal_pcc, np.ma.core.MaskedConstant):
        return True, 1.0

    return cal_pcc >= pcc, cal_pcc

def construct_pcc_assert_message(message, expected_pytorch_result, actual_pytorch_result):
    messages = []
    messages.append(message)
    # messages.append("Expected")
    # messages.append(str(expected_pytorch_result))
    # messages.append("Actual")
    # messages.append(str(actual_pytorch_result))
    messages = [str(m) for m in messages]
    return "\n".join(messages)

def assert_with_pcc(expected_pytorch_result, actual_pytorch_result, pcc=0.999):
    assert list(expected_pytorch_result.shape) == list(
        actual_pytorch_result.shape
    ), f"list(expected_pytorch_result.shape)={list(expected_pytorch_result.shape)} vs list(actual_pytorch_result.shape)={list(actual_pytorch_result.shape)}"
    pcc_passed, pcc_message = comp_pcc(expected_pytorch_result, actual_pytorch_result, pcc)
    print("Test: "+ str(pcc_message)+"\n")
    assert pcc_passed, construct_pcc_assert_message(pcc_message, expected_pytorch_result, actual_pytorch_result)
    return pcc_passed, pcc_message


def test_accuracy(expected, actual):
    if isinstance(actual, ttnn.Tensor):
        actual = ttnn.to_torch(actual)
    assert_with_pcc(expected, actual, pcc = 0.90)

def forward(arg0_1, arg1_1, arg2_1, arg3_1, arg4_1, arg5_1, arg6_1, arg7_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  slice_1 = aten.slice.Tensor(arg5_1, 0, 0, 9223372036854775807, )
  slice_2 = aten.slice.Tensor(slice_1, 1, 0, 8, )
  embedding = aten.embedding.default(arg0_1, arg6_1, )
  embedding_1 = aten.embedding.default(arg1_1, arg7_1, )
  add = aten.add.Tensor(embedding, embedding_1, )
  embedding_2 = aten.embedding.default(arg2_1, slice_2, )
  add_1 = aten.add.Tensor(add, embedding_2, )
  native_layer_norm = aten.native_layer_norm.default(add_1, [768], arg3_1, arg4_1, 1e-12, )
  getitem = native_layer_norm[0]
  clone_2 = aten.clone.default(getitem, )
  # return (clone_2,)
  ttnn_from_torch = ttnn.from_torch(arg5_1, layout = ttnn.ROW_MAJOR_LAYOUT, dtype = ttnn.uint32)
  ttnn_slice = ttnn.slice(ttnn_from_torch, [0, 0], [1, 8], )
  test_accuracy(slice_2, ttnn_slice)
  ttnn_from_torch_1 = ttnn.from_torch(arg6_1, device = device, layout = ttnn.ROW_MAJOR_LAYOUT, dtype = ttnn.uint32)
  ttnn_from_torch_2 = ttnn.from_torch(arg0_1, device = device, layout = ttnn.ROW_MAJOR_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_embedding = ttnn.embedding(ttnn_from_torch_1, ttnn_from_torch_2, layout = ttnn.ROW_MAJOR_LAYOUT)
  ttnn_to_layout = ttnn.to_layout(ttnn_embedding, ttnn.TILE_LAYOUT, )
  ttnn_from_torch_3 = ttnn.from_torch(arg7_1, device = device, layout = ttnn.ROW_MAJOR_LAYOUT, dtype = ttnn.uint32)
  ttnn_from_torch_4 = ttnn.from_torch(arg1_1, device = device, layout = ttnn.ROW_MAJOR_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_embedding_1 = ttnn.embedding(ttnn_from_torch_3, ttnn_from_torch_4, layout = ttnn.ROW_MAJOR_LAYOUT)
  ttnn_to_layout_1 = ttnn.to_layout(ttnn_embedding_1, ttnn.TILE_LAYOUT, )
  ttnn_add = ttnn.add(ttnn_to_layout, ttnn_to_layout_1, )
  ttnn_from_device = ttnn.from_device(ttnn_slice, )
  ttnn_to_layout_3 = ttnn.to_layout(ttnn_from_device, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_to_device = ttnn.to_device(ttnn_to_layout_3, device = device)
  ttnn_from_torch_5 = ttnn.from_torch(arg2_1, device = device, layout = ttnn.ROW_MAJOR_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_embedding_2 = ttnn.embedding(ttnn_to_device, ttnn_from_torch_5, layout = ttnn.ROW_MAJOR_LAYOUT)
  ttnn_to_layout_2 = ttnn.to_layout(ttnn_embedding_2, ttnn.TILE_LAYOUT, )
  test_accuracy(embedding_2, ttnn_to_layout_2)
  ttnn_add_1 = ttnn.add(ttnn_add, ttnn_to_layout_2, )
  test_accuracy(add_1, ttnn_add_1)
  ttnn_from_torch_6 = ttnn.from_torch(arg3_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_7 = ttnn.from_torch(arg4_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm = ttnn.layer_norm(ttnn_add_1, epsilon = 1e-12, weight = ttnn_from_torch_6, bias = ttnn_from_torch_7)
  ttnn_prefix_clone = clone_wrapper(ttnn_layer_norm, )
  test_accuracy(clone_2, ttnn_prefix_clone)
  ttnn_to_torch = ttnn.to_torch(ttnn_prefix_clone, dtype = torch.bfloat16)
  ttnn.close_device(device)
   # def forward(arg0_1, arg1_1, arg2_1, arg3_1, arg4_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  convolution = aten.convolution.default(arg3_1, arg1_1, arg2_1, [32, 32], [0, 0], [1, 1], False, [0, 0], 1, )
  slice_1 = aten.slice.Tensor(arg4_1, 0, 0, 9223372036854775807, )
  unsqueeze = aten.unsqueeze.default(slice_1, 1, )
  slice_2 = aten.slice.Tensor(unsqueeze, 2, 0, 9223372036854775807, )
  slice_3 = aten.slice.Tensor(slice_2, 3, 0, 9223372036854775807, )
  _to_copy = aten._to_copy.default(slice_3, dtype = torch.float32)
  arange = aten.arange.default(12, dtype = torch.float32, device = "cpu", pin_memory = False)
  add = aten.add.Tensor(arange, 0.0, )
  mul = aten.mul.Tensor(add, 32.0, )
  _to_copy_1 = aten._to_copy.default(mul, dtype = torch.int64)
  unsqueeze_1 = aten.unsqueeze.default(_to_copy_1, -1, )
  arange_1 = aten.arange.default(16, dtype = torch.float32, device = "cpu", pin_memory = False)
  add_1 = aten.add.Tensor(arange_1, 0.0, )
  mul_1 = aten.mul.Tensor(add_1, 32.0, )
  _to_copy_2 = aten._to_copy.default(mul_1, dtype = torch.int64)
  _unsafe_index = aten._unsafe_index.Tensor(_to_copy, [None, None, unsqueeze_1, _to_copy_2], )
  _to_copy_3 = aten._to_copy.default(_unsafe_index, dtype = torch.int64)
  slice_4 = aten.slice.Tensor(_to_copy_3, 0, 0, 9223372036854775807, )
  select = aten.select.int(slice_4, 1, 0, )
  sum_1 = aten.sum.dim_IntList(select, [1], )
  slice_5 = aten.slice.Tensor(sum_1, 0, 0, 9223372036854775807, )
  select_1 = aten.select.int(slice_5, 1, 0, )
  slice_6 = aten.slice.Tensor(_to_copy_3, 0, 0, 9223372036854775807, )
  select_2 = aten.select.int(slice_6, 1, 0, )
  sum_2 = aten.sum.dim_IntList(select_2, [2], )
  slice_7 = aten.slice.Tensor(sum_2, 0, 0, 9223372036854775807, )
  select_3 = aten.select.int(slice_7, 1, 0, )
  slice_8 = aten.slice.Tensor(arg0_1, 0, 0, 9223372036854775807, )
  slice_9 = aten.slice.Tensor(slice_8, 1, 1, 9223372036854775807, )
  slice_10 = aten.slice.Tensor(slice_9, 2, 0, 9223372036854775807, )
  transpose = aten.transpose.int(slice_10, 1, 2, )
  view = aten.view.default(transpose, [1, 768, 12, 12], )
  select_4 = aten.select.int(select_1, 0, 0, )
  select_5 = aten.select.int(select_3, 0, 0, )
  # return (select_4, select_5, convolution, _to_copy_3, select_1, select_3, view)
  convolution_default = aten.convolution.default(arg3_1, arg1_1, arg2_1, [32, 32], [0, 0], [1, 1], False, [0, 0], 1, )
  test_accuracy(convolution, convolution_default)
  ttnn_from_torch = ttnn.from_torch(arg4_1, layout = ttnn.ROW_MAJOR_LAYOUT, dtype = ttnn.uint32)
  ttnn_reshape = ttnn.reshape(ttnn_from_torch, (1, 1, 384, 512), )
  test_accuracy(unsqueeze, ttnn_reshape)
  ttnn_from_device = ttnn.from_device(ttnn_reshape, )
  ttnn_to_layout = ttnn.to_layout(ttnn_from_device, ttnn.TILE_LAYOUT, )
  ttnn_to_device = ttnn.to_device(ttnn_to_layout, device = device)
  ttnn_typecast = ttnn.typecast(ttnn_to_device, ttnn.bfloat16, )
  test_accuracy(_to_copy, ttnn_typecast)
  _folded_unsqueeze_1 = torch.tensor([[  0],
        [ 32],
        [ 64],
        [ 96],
        [128],
        [160],
        [192],
        [224],
        [256],
        [288],
        [320],
        [352]])
  test_accuracy(unsqueeze_1, _folded_unsqueeze_1)
  _folded__to_copy_2 = torch.tensor([  0,  32,  64,  96, 128, 160, 192, 224, 256, 288, 320, 352, 384, 416,
        448, 480])
  test_accuracy(_to_copy_2, _folded__to_copy_2)
  ttnn_to_torch = ttnn.to_torch(ttnn_typecast, dtype = torch.float32)
  _unsafe_index_tensor = aten._unsafe_index.Tensor(ttnn_to_torch, [None, None, _folded_unsqueeze_1, _folded__to_copy_2], )
  test_accuracy(_unsafe_index, _unsafe_index_tensor)
  _to_copy_default_1 = aten._to_copy.default(_unsafe_index_tensor, dtype = torch.int64)
  test_accuracy(_to_copy_3, _to_copy_default_1)
  ttnn_from_torch_1 = ttnn.from_torch(_to_copy_default_1, layout = ttnn.ROW_MAJOR_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_slice = ttnn.slice(ttnn_from_torch_1, [0, 0, 0, 0], [1, 1, 12, 16], )
  ttnn_from_device_1 = ttnn.from_device(ttnn_slice, )
  ttnn_to_layout_1 = ttnn.to_layout(ttnn_from_device_1, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_1 = ttnn.reshape(ttnn_to_layout_1, (1, 12, 16), )
  ttnn_to_torch_1 = ttnn.to_torch(ttnn_reshape_1, dtype = torch.int64)
  sum_dim_int_list = aten.sum.dim_IntList(ttnn_to_torch_1, [1], )
  test_accuracy(sum_1, sum_dim_int_list)
  ttnn_from_torch_2 = ttnn.from_torch(sum_dim_int_list, layout = ttnn.ROW_MAJOR_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_slice_1 = ttnn.slice(ttnn_from_torch_2, [0, 0], [1, 1], )
  ttnn_from_device_2 = ttnn.from_device(ttnn_slice_1, )
  ttnn_to_layout_2 = ttnn.to_layout(ttnn_from_device_2, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_2 = ttnn.reshape(ttnn_to_layout_2, (1,), )
  test_accuracy(select_1, ttnn_reshape_2)
  ttnn_to_layout_3 = ttnn.to_layout(ttnn_from_device_1, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_3 = ttnn.reshape(ttnn_to_layout_3, (1, 12, 16), )
  test_accuracy(select_2, ttnn_reshape_3)
  ttnn_to_torch_2 = ttnn.to_torch(ttnn_reshape_3, dtype = torch.int64)
  sum_dim_int_list_1 = aten.sum.dim_IntList(ttnn_to_torch_2, [2], )
  test_accuracy(sum_2, sum_dim_int_list_1)
  ttnn_from_torch_3 = ttnn.from_torch(sum_dim_int_list_1, layout = ttnn.ROW_MAJOR_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_slice_3 = ttnn.slice(ttnn_from_torch_3, [0, 0], [1, 1], )
  ttnn_from_device_4 = ttnn.from_device(ttnn_slice_3, )
  ttnn_to_layout_4 = ttnn.to_layout(ttnn_from_device_4, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_4 = ttnn.reshape(ttnn_to_layout_4, (1,), )
  test_accuracy(select_3, ttnn_reshape_4)
  ttnn_from_torch_4 = ttnn.from_torch(arg0_1, layout = ttnn.ROW_MAJOR_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_slice_4 = ttnn.slice(ttnn_from_torch_4, [0, 1, 0], [1, 145, 768], )
  test_accuracy(slice_10, ttnn_slice_4)
  ttnn_from_device_5 = ttnn.from_device(ttnn_slice_4, )
  ttnn_to_layout_5 = ttnn.to_layout(ttnn_from_device_5, ttnn.TILE_LAYOUT, )
  ttnn_to_device_1 = ttnn.to_device(ttnn_to_layout_5, device = device)
  ttnn_transpose = ttnn.transpose(ttnn_to_device_1, 1, 2, )
  test_accuracy(transpose, ttnn_transpose)
  ttnn_from_device_6 = ttnn.from_device(ttnn_transpose, )
  ttnn_to_layout_6 = ttnn.to_layout(ttnn_from_device_6, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_5 = ttnn.reshape(ttnn_to_layout_6, (1, 768, 12, 12), )
  test_accuracy(view, ttnn_reshape_5)
  ttnn_to_torch_3 = ttnn.to_torch(ttnn_reshape_2, dtype = torch.int64)
  squeeze_dim = aten.squeeze.dim(ttnn_to_torch_3, 0, )
  ttnn_to_torch_4 = ttnn.to_torch(ttnn_reshape_4, dtype = torch.int64)
  squeeze_dim_1 = aten.squeeze.dim(ttnn_to_torch_4, 0, )
  test_accuracy(select_5, squeeze_dim_1)
  ttnn_to_torch_5 = ttnn.to_torch(ttnn_reshape_5, dtype = torch.bfloat16)
  ttnn.close_device(device)
   # def forward(arg0_1, arg1_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  cat = aten.cat.default([arg0_1], )
  view = aten.view.default(cat, [1, 768, 192], )
  transpose = aten.transpose.int(view, 1, 2, )
  view_1 = aten.view.default(arg1_1, [1, 768, 192], )
  transpose_1 = aten.transpose.int(view_1, 1, 2, )
  # return (transpose_1, transpose)
  ttnn_from_torch = ttnn.from_torch(arg0_1, layout = ttnn.ROW_MAJOR_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_reshape = ttnn.reshape(ttnn_from_torch, (1, 768, 192), )
  ttnn_from_device = ttnn.from_device(ttnn_reshape, )
  ttnn_to_layout = ttnn.to_layout(ttnn_from_device, ttnn.TILE_LAYOUT, )
  ttnn_to_device = ttnn.to_device(ttnn_to_layout, device = device)
  ttnn_transpose = ttnn.transpose(ttnn_to_device, 1, 2, )
  ttnn_from_torch_1 = ttnn.from_torch(arg1_1, layout = ttnn.ROW_MAJOR_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_reshape_1 = ttnn.reshape(ttnn_from_torch_1, (1, 768, 192), )
  test_accuracy(view_1, ttnn_reshape_1)
  ttnn_from_device_1 = ttnn.from_device(ttnn_reshape_1, )
  ttnn_to_layout_1 = ttnn.to_layout(ttnn_from_device_1, ttnn.TILE_LAYOUT, )
  ttnn_to_device_1 = ttnn.to_device(ttnn_to_layout_1, device = device)
  ttnn_transpose_1 = ttnn.transpose(ttnn_to_device_1, 1, 2, )
  test_accuracy(transpose_1, ttnn_transpose_1)
  ttnn_to_torch = ttnn.to_torch(ttnn_transpose_1, dtype = torch.bfloat16)
  ttnn_to_torch_1 = ttnn.to_torch(ttnn_transpose, dtype = torch.bfloat16)
  ttnn.close_device(device)
   # def forward():
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  arange = aten.arange.default(12, device = "cpu", pin_memory = False)
  # return (arange,)
  _folded_arange = torch.tensor([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
  test_accuracy(arange, _folded_arange)
  ttnn.close_device(device)
   # def forward(arg0_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  arange = aten.arange.default(16, device = "cpu", pin_memory = False)
  view = aten.view.default(arg0_1, [-1, 1], )
  expand = aten.expand.default(view, [12, 16], )
  view_1 = aten.view.default(arange, [1, -1], )
  expand_1 = aten.expand.default(view_1, [12, 16], )
  stack = aten.stack.default([expand, expand_1], -1, )
  # return (stack,)
  ttnn_from_torch = ttnn.from_torch(arg0_1, layout = ttnn.ROW_MAJOR_LAYOUT, dtype = ttnn.uint32)
  ttnn_reshape = ttnn.reshape(ttnn_from_torch, (-1, 1), )
  test_accuracy(view, ttnn_reshape)
  ttnn_to_torch = ttnn.to_torch(ttnn_reshape, dtype = torch.int64)
  expand_default = aten.expand.default(ttnn_to_torch, [12, 16], )
  test_accuracy(expand, expand_default)
  _folded_expand_1 = torch.tensor([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15],
        [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15],
        [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15],
        [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15],
        [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15],
        [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15],
        [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15],
        [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15],
        [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15],
        [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15],
        [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15],
        [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15]])
  test_accuracy(expand_1, _folded_expand_1)
  ttnn_from_torch_1 = ttnn.from_torch(expand_default, device = device, layout = ttnn.ROW_MAJOR_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_2 = ttnn.from_torch(_folded_expand_1, device = device, layout = ttnn.ROW_MAJOR_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_prefix_stack = stack_wrapper((ttnn_from_torch_1, ttnn_from_torch_2), -1, [12, 16, 2], )
  test_accuracy(stack, ttnn_prefix_stack)
  ttnn_to_torch_1 = ttnn.to_torch(ttnn_prefix_stack, dtype = torch.int64)
  ttnn.close_device(device)

if __name__ == "__main__":
    filepath = Path(__file__).with_name("ViLT_inputs.pickle")
    file = lzma.open(filepath, "rb")
    inputs = pickle.load(file)
    forward(*inputs)


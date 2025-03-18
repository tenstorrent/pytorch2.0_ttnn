import lzma
import numpy as np
import pickle
import torch
import ttnn
from pathlib import Path
aten = torch.ops.aten
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
    assert pcc_passed, construct_pcc_assert_message(pcc_message, expected_pytorch_result, actual_pytorch_result)
    return pcc_passed, pcc_message


def test_accuracy(expected, actual):
    if isinstance(actual, ttnn.Tensor):
        actual = ttnn.to_torch(actual)
    assert_with_pcc(expected, actual, pcc = 0.90)

def forward():
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  ones = aten.ones.default([1, 1], dtype = torch.int64, device = "cpu", pin_memory = False)
  mul = aten.mul.Tensor(ones, 151643, )
  # return (mul,)
  _folded_mul = torch.tensor([[151643]])
  test_accuracy(mul, _folded_mul)
  ttnn.close_device(device)
   # def forward():
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  _tensor_constant0 = 151643
  lift_fresh_copy = aten.lift_fresh_copy.default(_tensor_constant0, )
  # return (lift_fresh_copy,)
  _folded_lift_fresh_copy = 151643
  test_accuracy(lift_fresh_copy, _folded_lift_fresh_copy)
  ttnn.close_device(device)
   # def forward():
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  _tensor_constant0 = torch.tensor([151645, 151643])
  lift_fresh_copy = aten.lift_fresh_copy.default(_tensor_constant0, )
  # return (lift_fresh_copy,)
  _folded_lift_fresh_copy = torch.tensor([151645, 151643])
  test_accuracy(lift_fresh_copy, _folded_lift_fresh_copy)
  ttnn.close_device(device)
   # def forward(arg0_1, arg1_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  isin = aten.isin.Tensor_Tensor(arg0_1, arg1_1, )
  # return (isin,)
  isin_tensor_tensor = aten.isin.Tensor_Tensor(arg0_1, arg1_1, )
  test_accuracy(isin, isin_tensor_tensor)
  ttnn.close_device(device)
   # def forward(arg0_1, arg1_1, arg2_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  ones = aten.ones.default([1, 1], dtype = torch.int64, device = "cpu", pin_memory = False)
  isin = aten.isin.Tensor_Tensor(arg0_1, arg1_1, )
  any_1 = aten.any.default(isin, )
  isin_1 = aten.isin.Tensor_Tensor(arg2_1, arg1_1, )
  any_2 = aten.any.default(isin_1, )
  bitwise_not = aten.bitwise_not.default(any_2, )
  mul = aten.mul.Tensor(any_1, bitwise_not, )
  ne = aten.ne.Tensor(arg0_1, arg1_1, )
  _to_copy = aten._to_copy.default(ne, dtype = torch.int64)
  mul_1 = aten.mul.Tensor(_to_copy, mul, )
  bitwise_not_1 = aten.bitwise_not.default(mul, )
  mul_2 = aten.mul.Tensor(ones, bitwise_not_1, )
  add = aten.add.Tensor(mul_1, mul_2, )
  # return (add,)
  _folded_ones = torch.tensor([[1]])
  test_accuracy(ones, _folded_ones)
  isin_tensor_tensor = aten.isin.Tensor_Tensor(arg0_1, arg1_1, )
  test_accuracy(isin, isin_tensor_tensor)
  any_default = aten.any.default(isin_tensor_tensor, )
  isin_tensor_tensor_1 = aten.isin.Tensor_Tensor(arg2_1, arg1_1, )
  test_accuracy(isin_1, isin_tensor_tensor_1)
  any_default_1 = aten.any.default(isin_tensor_tensor_1, )
  test_accuracy(any_2, any_default_1)
  ttnn_from_torch = ttnn.from_torch(any_default_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_eq = ttnn.eq(ttnn_from_torch, 0, )
  ttnn_to_torch = ttnn.to_torch(ttnn_eq, dtype = torch.bool)
  mul_tensor = aten.mul.Tensor(any_default, ttnn_to_torch, )
  test_accuracy(mul, mul_tensor)
  ne_tensor = aten.ne.Tensor(arg0_1, arg1_1, )
  test_accuracy(ne, ne_tensor)
  mul_tensor_1 = aten.mul.Tensor(ne_tensor, mul_tensor, )
  ttnn_from_torch_1 = ttnn.from_torch(mul_tensor, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_eq_1 = ttnn.eq(ttnn_from_torch_1, 0, )
  test_accuracy(bitwise_not_1, ttnn_eq_1)
  ttnn_to_torch_1 = ttnn.to_torch(ttnn_eq_1, dtype = torch.bool)
  mul_tensor_2 = aten.mul.Tensor(_folded_ones, ttnn_to_torch_1, )
  test_accuracy(mul_2, mul_tensor_2)
  ttnn_from_torch_2 = ttnn.from_torch(mul_tensor_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_3 = ttnn.from_torch(mul_tensor_2, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add = ttnn.add(ttnn_from_torch_2, ttnn_from_torch_3, )
  test_accuracy(add, ttnn_add)
  ttnn_to_torch_2 = ttnn.to_torch(ttnn_add, dtype = torch.int64)
  ttnn.close_device(device)
   # def forward(arg0_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  select = aten.select.int(arg0_1, 0, 0, )
  eq = aten.eq.Scalar(select, 0, )
  # return (eq,)
  squeeze_dim = aten.squeeze.dim(arg0_1, 0, )
  test_accuracy(select, squeeze_dim)
  ttnn_from_torch = ttnn.from_torch(squeeze_dim, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_eq = ttnn.eq(ttnn_from_torch, 0, )
  test_accuracy(eq, ttnn_eq)
  ttnn_to_torch = ttnn.to_torch(ttnn_eq, dtype = torch.bool)
  ttnn.close_device(device)
   # def forward(arg0_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  select = aten.select.int(arg0_1, 0, 0, )
  ne = aten.ne.Scalar(select, 0, )
  # return (ne,)
  squeeze_dim = aten.squeeze.dim(arg0_1, 0, )
  test_accuracy(select, squeeze_dim)
  ttnn_from_torch = ttnn.from_torch(squeeze_dim, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_ne = ttnn.ne(ttnn_from_torch, 0, )
  test_accuracy(ne, ttnn_ne)
  ttnn_to_torch = ttnn.to_torch(ttnn_ne, dtype = torch.bool)
  ttnn.close_device(device)
   # def forward(arg0_1, arg1_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  embedding = aten.embedding.default(arg0_1, arg1_1, )
  # return (embedding,)
  ttnn_from_torch = ttnn.from_torch(arg1_1, device = device, layout = ttnn.ROW_MAJOR_LAYOUT, dtype = ttnn.uint32)
  ttnn_from_torch_1 = ttnn.from_torch(arg0_1, device = device, layout = ttnn.ROW_MAJOR_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_embedding = ttnn.embedding(ttnn_from_torch, ttnn_from_torch_1, layout = ttnn.ROW_MAJOR_LAYOUT)
  ttnn_to_layout = ttnn.to_layout(ttnn_embedding, ttnn.TILE_LAYOUT, )
  test_accuracy(embedding, ttnn_to_layout)
  ttnn_to_torch = ttnn.to_torch(ttnn_to_layout, dtype = torch.bfloat16)
  ttnn.close_device(device)
   # def forward(arg0_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  unsqueeze = aten.unsqueeze.default(arg0_1, 0, )
  unsqueeze_1 = aten.unsqueeze.default(unsqueeze, 1, )
  slice_1 = aten.slice.Tensor(unsqueeze_1, 2, 0, 9223372036854775807, )
  unsqueeze_2 = aten.unsqueeze.default(slice_1, 3, )
  # return (unsqueeze_2,)
  ttnn_from_torch = ttnn.from_torch(arg0_1, layout = ttnn.ROW_MAJOR_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_reshape = ttnn.reshape(ttnn_from_torch, (1, 64), )
  test_accuracy(unsqueeze, ttnn_reshape)
  ttnn_from_device = ttnn.from_device(ttnn_reshape, )
  ttnn_to_layout = ttnn.to_layout(ttnn_from_device, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_1 = ttnn.reshape(ttnn_to_layout, (1, 1, 64), )
  test_accuracy(unsqueeze_1, ttnn_reshape_1)
  ttnn_from_device_1 = ttnn.from_device(ttnn_reshape_1, )
  ttnn_to_layout_1 = ttnn.to_layout(ttnn_from_device_1, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_2 = ttnn.reshape(ttnn_to_layout_1, (1, 1, 64, 1), )
  test_accuracy(unsqueeze_2, ttnn_reshape_2)
  ttnn_to_torch = ttnn.to_torch(ttnn_reshape_2, dtype = torch.float32)
  ttnn.close_device(device)
   # def forward(arg0_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  slice_1 = aten.slice.Tensor(arg0_1, 0, -1, 9223372036854775807, )
  add = aten.add.Tensor(slice_1, 1, )
  # return (add,)
  ttnn_from_torch = ttnn.from_torch(arg0_1, layout = ttnn.ROW_MAJOR_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_slice = ttnn.slice(ttnn_from_torch, [-1], [1], )
  test_accuracy(slice_1, ttnn_slice)
  ttnn_from_device = ttnn.from_device(ttnn_slice, )
  ttnn_to_layout = ttnn.to_layout(ttnn_from_device, ttnn.TILE_LAYOUT, )
  ttnn_to_device = ttnn.to_device(ttnn_to_layout, device = device)
  ttnn_add = ttnn.add(ttnn_to_device, 1, )
  test_accuracy(add, ttnn_add)
  ttnn_to_torch = ttnn.to_torch(ttnn_add, dtype = torch.int64)
  ttnn.close_device(device)
   # def forward(arg0_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  # return ()
  ttnn.close_device(device)
   # def forward(arg0_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  # return ()
  ttnn.close_device(device)
   # def forward(arg0_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  # return ()
  ttnn.close_device(device)
   # def forward(arg0_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  # return ()
  ttnn.close_device(device)
   # def forward(arg0_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  # return ()
  ttnn.close_device(device)
   # def forward(arg0_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  # return ()
  ttnn.close_device(device)
   # def forward(arg0_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  # return ()
  ttnn.close_device(device)
   # def forward(arg0_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  # return ()
  ttnn.close_device(device)
   # def forward(arg0_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  # return ()
  ttnn.close_device(device)
   # def forward(arg0_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  # return ()
  ttnn.close_device(device)
   # def forward(arg0_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  # return ()
  ttnn.close_device(device)
   # def forward(arg0_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  # return ()
  ttnn.close_device(device)
   # def forward(arg0_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  # return ()
  ttnn.close_device(device)

if __name__ == "__main__":
    filepath = Path(__file__).with_name("Qwen2-VL-2B_inputs.pickle")
    file = lzma.open(filepath, "rb")
    inputs = pickle.load(file)
    forward(*inputs)


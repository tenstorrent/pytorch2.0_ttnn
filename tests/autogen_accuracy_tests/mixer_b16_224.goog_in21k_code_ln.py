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


ref = globals()["clone"]
globals()["clone_wrapper"] = ref
del globals()["clone"]

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
    return assert_with_pcc(expected, actual, pcc = 0.50)

def forward(arg0_1, arg1_1, arg2_1, arg3_1, arg4_1, arg5_1, arg6_1, arg7_1, arg8_1, arg9_1, arg10_1, arg11_1, arg12_1, arg13_1, arg14_1, arg15_1, arg16_1, arg17_1, arg18_1, arg19_1, arg20_1, arg21_1, arg22_1, arg23_1, arg24_1, arg25_1, arg26_1, arg27_1, arg28_1, arg29_1, arg30_1, arg31_1, arg32_1, arg33_1, arg34_1, arg35_1, arg36_1, arg37_1, arg38_1, arg39_1, arg40_1, arg41_1, arg42_1, arg43_1, arg44_1, arg45_1, arg46_1, arg47_1, arg48_1, arg49_1, arg50_1, arg51_1, arg52_1, arg53_1, arg54_1, arg55_1, arg56_1, arg57_1, arg58_1, arg59_1, arg60_1, arg61_1, arg62_1, arg63_1, arg64_1, arg65_1, arg66_1, arg67_1, arg68_1, arg69_1, arg70_1, arg71_1, arg72_1, arg73_1, arg74_1, arg75_1, arg76_1, arg77_1, arg78_1, arg79_1, arg80_1, arg81_1, arg82_1, arg83_1, arg84_1, arg85_1, arg86_1, arg87_1, arg88_1, arg89_1, arg90_1, arg91_1, arg92_1, arg93_1, arg94_1, arg95_1, arg96_1, arg97_1, arg98_1, arg99_1, arg100_1, arg101_1, arg102_1, arg103_1, arg104_1, arg105_1, arg106_1, arg107_1, arg108_1, arg109_1, arg110_1, arg111_1, arg112_1, arg113_1, arg114_1, arg115_1, arg116_1, arg117_1, arg118_1, arg119_1, arg120_1, arg121_1, arg122_1, arg123_1, arg124_1, arg125_1, arg126_1, arg127_1, arg128_1, arg129_1, arg130_1, arg131_1, arg132_1, arg133_1, arg134_1, arg135_1, arg136_1, arg137_1, arg138_1, arg139_1, arg140_1, arg141_1, arg142_1, arg143_1, arg144_1, arg145_1, arg146_1, arg147_1, arg148_1, arg149_1, arg150_1):
  device = ttnn.open_device(device_id=0, l1_small_size=16384)
  convolution = aten.convolution.default(arg150_1, arg0_1, arg1_1, [16, 16], [0, 0], [1, 1], False, [0, 0], 1, )
  view = aten.view.default(convolution, [1, 768, 196], )
  transpose = aten.transpose.int(view, 1, 2, )
  native_layer_norm = aten.native_layer_norm.default(transpose, [768], arg2_1, arg3_1, 1e-06, )
  getitem = native_layer_norm[0]
  transpose_1 = aten.transpose.int(getitem, 1, 2, )
  t = aten.t.default(arg4_1, )
  view_1 = aten.view.default(transpose_1, [768, 196], )
  mm = aten.mm.default(view_1, t, )
  view_2 = aten.view.default(mm, [1, 768, 384], )
  add = aten.add.Tensor(view_2, arg5_1, )
  gelu = aten.gelu.default(add, )
  clone_1 = aten.clone.default(gelu, )
  view_3 = aten.view.default(clone_1, [768, 384], )
  t_1 = aten.t.default(arg6_1, )
  addmm = aten.addmm.default(arg7_1, view_3, t_1, )
  view_4 = aten.view.default(addmm, [1, 768, 196], )
  clone_2 = aten.clone.default(view_4, )
  transpose_2 = aten.transpose.int(clone_2, 1, 2, )
  add_1 = aten.add.Tensor(transpose, transpose_2, )
  native_layer_norm_1 = aten.native_layer_norm.default(add_1, [768], arg8_1, arg9_1, 1e-06, )
  getitem_3 = native_layer_norm_1[0]
  view_5 = aten.view.default(getitem_3, [196, 768], )
  t_2 = aten.t.default(arg10_1, )
  addmm_1 = aten.addmm.default(arg11_1, view_5, t_2, )
  view_6 = aten.view.default(addmm_1, [1, 196, 3072], )
  gelu_1 = aten.gelu.default(view_6, )
  clone_3 = aten.clone.default(gelu_1, )
  view_7 = aten.view.default(clone_3, [196, 3072], )
  t_3 = aten.t.default(arg12_1, )
  addmm_2 = aten.addmm.default(arg13_1, view_7, t_3, )
  view_8 = aten.view.default(addmm_2, [1, 196, 768], )
  clone_4 = aten.clone.default(view_8, )
  add_2 = aten.add.Tensor(add_1, clone_4, )
  native_layer_norm_2 = aten.native_layer_norm.default(add_2, [768], arg14_1, arg15_1, 1e-06, )
  getitem_6 = native_layer_norm_2[0]
  transpose_3 = aten.transpose.int(getitem_6, 1, 2, )
  t_4 = aten.t.default(arg16_1, )
  view_9 = aten.view.default(transpose_3, [768, 196], )
  mm_1 = aten.mm.default(view_9, t_4, )
  view_10 = aten.view.default(mm_1, [1, 768, 384], )
  add_3 = aten.add.Tensor(view_10, arg17_1, )
  gelu_2 = aten.gelu.default(add_3, )
  clone_5 = aten.clone.default(gelu_2, )
  view_11 = aten.view.default(clone_5, [768, 384], )
  t_5 = aten.t.default(arg18_1, )
  addmm_3 = aten.addmm.default(arg19_1, view_11, t_5, )
  view_12 = aten.view.default(addmm_3, [1, 768, 196], )
  clone_6 = aten.clone.default(view_12, )
  transpose_4 = aten.transpose.int(clone_6, 1, 2, )
  add_4 = aten.add.Tensor(add_2, transpose_4, )
  native_layer_norm_3 = aten.native_layer_norm.default(add_4, [768], arg20_1, arg21_1, 1e-06, )
  getitem_9 = native_layer_norm_3[0]
  view_13 = aten.view.default(getitem_9, [196, 768], )
  t_6 = aten.t.default(arg22_1, )
  addmm_4 = aten.addmm.default(arg23_1, view_13, t_6, )
  view_14 = aten.view.default(addmm_4, [1, 196, 3072], )
  gelu_3 = aten.gelu.default(view_14, )
  clone_7 = aten.clone.default(gelu_3, )
  view_15 = aten.view.default(clone_7, [196, 3072], )
  t_7 = aten.t.default(arg24_1, )
  addmm_5 = aten.addmm.default(arg25_1, view_15, t_7, )
  view_16 = aten.view.default(addmm_5, [1, 196, 768], )
  clone_8 = aten.clone.default(view_16, )
  add_5 = aten.add.Tensor(add_4, clone_8, )
  native_layer_norm_4 = aten.native_layer_norm.default(add_5, [768], arg26_1, arg27_1, 1e-06, )
  getitem_12 = native_layer_norm_4[0]
  transpose_5 = aten.transpose.int(getitem_12, 1, 2, )
  t_8 = aten.t.default(arg28_1, )
  view_17 = aten.view.default(transpose_5, [768, 196], )
  mm_2 = aten.mm.default(view_17, t_8, )
  view_18 = aten.view.default(mm_2, [1, 768, 384], )
  add_6 = aten.add.Tensor(view_18, arg29_1, )
  gelu_4 = aten.gelu.default(add_6, )
  clone_9 = aten.clone.default(gelu_4, )
  view_19 = aten.view.default(clone_9, [768, 384], )
  t_9 = aten.t.default(arg30_1, )
  addmm_6 = aten.addmm.default(arg31_1, view_19, t_9, )
  view_20 = aten.view.default(addmm_6, [1, 768, 196], )
  clone_10 = aten.clone.default(view_20, )
  transpose_6 = aten.transpose.int(clone_10, 1, 2, )
  add_7 = aten.add.Tensor(add_5, transpose_6, )
  native_layer_norm_5 = aten.native_layer_norm.default(add_7, [768], arg32_1, arg33_1, 1e-06, )
  getitem_15 = native_layer_norm_5[0]
  view_21 = aten.view.default(getitem_15, [196, 768], )
  t_10 = aten.t.default(arg34_1, )
  addmm_7 = aten.addmm.default(arg35_1, view_21, t_10, )
  view_22 = aten.view.default(addmm_7, [1, 196, 3072], )
  gelu_5 = aten.gelu.default(view_22, )
  clone_11 = aten.clone.default(gelu_5, )
  view_23 = aten.view.default(clone_11, [196, 3072], )
  t_11 = aten.t.default(arg36_1, )
  addmm_8 = aten.addmm.default(arg37_1, view_23, t_11, )
  view_24 = aten.view.default(addmm_8, [1, 196, 768], )
  clone_12 = aten.clone.default(view_24, )
  add_8 = aten.add.Tensor(add_7, clone_12, )
  native_layer_norm_6 = aten.native_layer_norm.default(add_8, [768], arg38_1, arg39_1, 1e-06, )
  getitem_18 = native_layer_norm_6[0]
  transpose_7 = aten.transpose.int(getitem_18, 1, 2, )
  t_12 = aten.t.default(arg40_1, )
  view_25 = aten.view.default(transpose_7, [768, 196], )
  mm_3 = aten.mm.default(view_25, t_12, )
  view_26 = aten.view.default(mm_3, [1, 768, 384], )
  add_9 = aten.add.Tensor(view_26, arg41_1, )
  gelu_6 = aten.gelu.default(add_9, )
  clone_13 = aten.clone.default(gelu_6, )
  view_27 = aten.view.default(clone_13, [768, 384], )
  t_13 = aten.t.default(arg42_1, )
  addmm_9 = aten.addmm.default(arg43_1, view_27, t_13, )
  view_28 = aten.view.default(addmm_9, [1, 768, 196], )
  clone_14 = aten.clone.default(view_28, )
  transpose_8 = aten.transpose.int(clone_14, 1, 2, )
  add_10 = aten.add.Tensor(add_8, transpose_8, )
  native_layer_norm_7 = aten.native_layer_norm.default(add_10, [768], arg44_1, arg45_1, 1e-06, )
  getitem_21 = native_layer_norm_7[0]
  view_29 = aten.view.default(getitem_21, [196, 768], )
  t_14 = aten.t.default(arg46_1, )
  addmm_10 = aten.addmm.default(arg47_1, view_29, t_14, )
  view_30 = aten.view.default(addmm_10, [1, 196, 3072], )
  gelu_7 = aten.gelu.default(view_30, )
  clone_15 = aten.clone.default(gelu_7, )
  view_31 = aten.view.default(clone_15, [196, 3072], )
  t_15 = aten.t.default(arg48_1, )
  addmm_11 = aten.addmm.default(arg49_1, view_31, t_15, )
  view_32 = aten.view.default(addmm_11, [1, 196, 768], )
  clone_16 = aten.clone.default(view_32, )
  add_11 = aten.add.Tensor(add_10, clone_16, )
  native_layer_norm_8 = aten.native_layer_norm.default(add_11, [768], arg50_1, arg51_1, 1e-06, )
  getitem_24 = native_layer_norm_8[0]
  transpose_9 = aten.transpose.int(getitem_24, 1, 2, )
  t_16 = aten.t.default(arg52_1, )
  view_33 = aten.view.default(transpose_9, [768, 196], )
  mm_4 = aten.mm.default(view_33, t_16, )
  view_34 = aten.view.default(mm_4, [1, 768, 384], )
  add_12 = aten.add.Tensor(view_34, arg53_1, )
  gelu_8 = aten.gelu.default(add_12, )
  clone_17 = aten.clone.default(gelu_8, )
  view_35 = aten.view.default(clone_17, [768, 384], )
  t_17 = aten.t.default(arg54_1, )
  addmm_12 = aten.addmm.default(arg55_1, view_35, t_17, )
  view_36 = aten.view.default(addmm_12, [1, 768, 196], )
  clone_18 = aten.clone.default(view_36, )
  transpose_10 = aten.transpose.int(clone_18, 1, 2, )
  add_13 = aten.add.Tensor(add_11, transpose_10, )
  native_layer_norm_9 = aten.native_layer_norm.default(add_13, [768], arg56_1, arg57_1, 1e-06, )
  getitem_27 = native_layer_norm_9[0]
  view_37 = aten.view.default(getitem_27, [196, 768], )
  t_18 = aten.t.default(arg58_1, )
  addmm_13 = aten.addmm.default(arg59_1, view_37, t_18, )
  view_38 = aten.view.default(addmm_13, [1, 196, 3072], )
  gelu_9 = aten.gelu.default(view_38, )
  clone_19 = aten.clone.default(gelu_9, )
  view_39 = aten.view.default(clone_19, [196, 3072], )
  t_19 = aten.t.default(arg60_1, )
  addmm_14 = aten.addmm.default(arg61_1, view_39, t_19, )
  view_40 = aten.view.default(addmm_14, [1, 196, 768], )
  clone_20 = aten.clone.default(view_40, )
  add_14 = aten.add.Tensor(add_13, clone_20, )
  native_layer_norm_10 = aten.native_layer_norm.default(add_14, [768], arg62_1, arg63_1, 1e-06, )
  getitem_30 = native_layer_norm_10[0]
  transpose_11 = aten.transpose.int(getitem_30, 1, 2, )
  t_20 = aten.t.default(arg64_1, )
  view_41 = aten.view.default(transpose_11, [768, 196], )
  mm_5 = aten.mm.default(view_41, t_20, )
  view_42 = aten.view.default(mm_5, [1, 768, 384], )
  add_15 = aten.add.Tensor(view_42, arg65_1, )
  gelu_10 = aten.gelu.default(add_15, )
  clone_21 = aten.clone.default(gelu_10, )
  view_43 = aten.view.default(clone_21, [768, 384], )
  t_21 = aten.t.default(arg66_1, )
  addmm_15 = aten.addmm.default(arg67_1, view_43, t_21, )
  view_44 = aten.view.default(addmm_15, [1, 768, 196], )
  clone_22 = aten.clone.default(view_44, )
  transpose_12 = aten.transpose.int(clone_22, 1, 2, )
  add_16 = aten.add.Tensor(add_14, transpose_12, )
  native_layer_norm_11 = aten.native_layer_norm.default(add_16, [768], arg68_1, arg69_1, 1e-06, )
  getitem_33 = native_layer_norm_11[0]
  view_45 = aten.view.default(getitem_33, [196, 768], )
  t_22 = aten.t.default(arg70_1, )
  addmm_16 = aten.addmm.default(arg71_1, view_45, t_22, )
  view_46 = aten.view.default(addmm_16, [1, 196, 3072], )
  gelu_11 = aten.gelu.default(view_46, )
  clone_23 = aten.clone.default(gelu_11, )
  view_47 = aten.view.default(clone_23, [196, 3072], )
  t_23 = aten.t.default(arg72_1, )
  addmm_17 = aten.addmm.default(arg73_1, view_47, t_23, )
  view_48 = aten.view.default(addmm_17, [1, 196, 768], )
  clone_24 = aten.clone.default(view_48, )
  add_17 = aten.add.Tensor(add_16, clone_24, )
  native_layer_norm_12 = aten.native_layer_norm.default(add_17, [768], arg74_1, arg75_1, 1e-06, )
  getitem_36 = native_layer_norm_12[0]
  transpose_13 = aten.transpose.int(getitem_36, 1, 2, )
  t_24 = aten.t.default(arg76_1, )
  view_49 = aten.view.default(transpose_13, [768, 196], )
  mm_6 = aten.mm.default(view_49, t_24, )
  view_50 = aten.view.default(mm_6, [1, 768, 384], )
  add_18 = aten.add.Tensor(view_50, arg77_1, )
  gelu_12 = aten.gelu.default(add_18, )
  clone_25 = aten.clone.default(gelu_12, )
  view_51 = aten.view.default(clone_25, [768, 384], )
  t_25 = aten.t.default(arg78_1, )
  addmm_18 = aten.addmm.default(arg79_1, view_51, t_25, )
  view_52 = aten.view.default(addmm_18, [1, 768, 196], )
  clone_26 = aten.clone.default(view_52, )
  transpose_14 = aten.transpose.int(clone_26, 1, 2, )
  add_19 = aten.add.Tensor(add_17, transpose_14, )
  native_layer_norm_13 = aten.native_layer_norm.default(add_19, [768], arg80_1, arg81_1, 1e-06, )
  getitem_39 = native_layer_norm_13[0]
  view_53 = aten.view.default(getitem_39, [196, 768], )
  t_26 = aten.t.default(arg82_1, )
  addmm_19 = aten.addmm.default(arg83_1, view_53, t_26, )
  view_54 = aten.view.default(addmm_19, [1, 196, 3072], )
  gelu_13 = aten.gelu.default(view_54, )
  clone_27 = aten.clone.default(gelu_13, )
  view_55 = aten.view.default(clone_27, [196, 3072], )
  t_27 = aten.t.default(arg84_1, )
  addmm_20 = aten.addmm.default(arg85_1, view_55, t_27, )
  view_56 = aten.view.default(addmm_20, [1, 196, 768], )
  clone_28 = aten.clone.default(view_56, )
  add_20 = aten.add.Tensor(add_19, clone_28, )
  native_layer_norm_14 = aten.native_layer_norm.default(add_20, [768], arg86_1, arg87_1, 1e-06, )
  getitem_42 = native_layer_norm_14[0]
  transpose_15 = aten.transpose.int(getitem_42, 1, 2, )
  t_28 = aten.t.default(arg88_1, )
  view_57 = aten.view.default(transpose_15, [768, 196], )
  mm_7 = aten.mm.default(view_57, t_28, )
  view_58 = aten.view.default(mm_7, [1, 768, 384], )
  add_21 = aten.add.Tensor(view_58, arg89_1, )
  gelu_14 = aten.gelu.default(add_21, )
  clone_29 = aten.clone.default(gelu_14, )
  view_59 = aten.view.default(clone_29, [768, 384], )
  t_29 = aten.t.default(arg90_1, )
  addmm_21 = aten.addmm.default(arg91_1, view_59, t_29, )
  view_60 = aten.view.default(addmm_21, [1, 768, 196], )
  clone_30 = aten.clone.default(view_60, )
  transpose_16 = aten.transpose.int(clone_30, 1, 2, )
  add_22 = aten.add.Tensor(add_20, transpose_16, )
  native_layer_norm_15 = aten.native_layer_norm.default(add_22, [768], arg92_1, arg93_1, 1e-06, )
  getitem_45 = native_layer_norm_15[0]
  view_61 = aten.view.default(getitem_45, [196, 768], )
  t_30 = aten.t.default(arg94_1, )
  addmm_22 = aten.addmm.default(arg95_1, view_61, t_30, )
  view_62 = aten.view.default(addmm_22, [1, 196, 3072], )
  gelu_15 = aten.gelu.default(view_62, )
  clone_31 = aten.clone.default(gelu_15, )
  view_63 = aten.view.default(clone_31, [196, 3072], )
  t_31 = aten.t.default(arg96_1, )
  addmm_23 = aten.addmm.default(arg97_1, view_63, t_31, )
  view_64 = aten.view.default(addmm_23, [1, 196, 768], )
  clone_32 = aten.clone.default(view_64, )
  add_23 = aten.add.Tensor(add_22, clone_32, )
  native_layer_norm_16 = aten.native_layer_norm.default(add_23, [768], arg98_1, arg99_1, 1e-06, )
  getitem_48 = native_layer_norm_16[0]
  transpose_17 = aten.transpose.int(getitem_48, 1, 2, )
  t_32 = aten.t.default(arg100_1, )
  view_65 = aten.view.default(transpose_17, [768, 196], )
  mm_8 = aten.mm.default(view_65, t_32, )
  view_66 = aten.view.default(mm_8, [1, 768, 384], )
  add_24 = aten.add.Tensor(view_66, arg101_1, )
  gelu_16 = aten.gelu.default(add_24, )
  clone_33 = aten.clone.default(gelu_16, )
  view_67 = aten.view.default(clone_33, [768, 384], )
  t_33 = aten.t.default(arg102_1, )
  addmm_24 = aten.addmm.default(arg103_1, view_67, t_33, )
  view_68 = aten.view.default(addmm_24, [1, 768, 196], )
  clone_34 = aten.clone.default(view_68, )
  transpose_18 = aten.transpose.int(clone_34, 1, 2, )
  add_25 = aten.add.Tensor(add_23, transpose_18, )
  native_layer_norm_17 = aten.native_layer_norm.default(add_25, [768], arg104_1, arg105_1, 1e-06, )
  getitem_51 = native_layer_norm_17[0]
  view_69 = aten.view.default(getitem_51, [196, 768], )
  t_34 = aten.t.default(arg106_1, )
  addmm_25 = aten.addmm.default(arg107_1, view_69, t_34, )
  view_70 = aten.view.default(addmm_25, [1, 196, 3072], )
  gelu_17 = aten.gelu.default(view_70, )
  clone_35 = aten.clone.default(gelu_17, )
  view_71 = aten.view.default(clone_35, [196, 3072], )
  t_35 = aten.t.default(arg108_1, )
  addmm_26 = aten.addmm.default(arg109_1, view_71, t_35, )
  view_72 = aten.view.default(addmm_26, [1, 196, 768], )
  clone_36 = aten.clone.default(view_72, )
  add_26 = aten.add.Tensor(add_25, clone_36, )
  native_layer_norm_18 = aten.native_layer_norm.default(add_26, [768], arg110_1, arg111_1, 1e-06, )
  getitem_54 = native_layer_norm_18[0]
  transpose_19 = aten.transpose.int(getitem_54, 1, 2, )
  t_36 = aten.t.default(arg112_1, )
  view_73 = aten.view.default(transpose_19, [768, 196], )
  mm_9 = aten.mm.default(view_73, t_36, )
  view_74 = aten.view.default(mm_9, [1, 768, 384], )
  add_27 = aten.add.Tensor(view_74, arg113_1, )
  gelu_18 = aten.gelu.default(add_27, )
  clone_37 = aten.clone.default(gelu_18, )
  view_75 = aten.view.default(clone_37, [768, 384], )
  t_37 = aten.t.default(arg114_1, )
  addmm_27 = aten.addmm.default(arg115_1, view_75, t_37, )
  view_76 = aten.view.default(addmm_27, [1, 768, 196], )
  clone_38 = aten.clone.default(view_76, )
  transpose_20 = aten.transpose.int(clone_38, 1, 2, )
  add_28 = aten.add.Tensor(add_26, transpose_20, )
  native_layer_norm_19 = aten.native_layer_norm.default(add_28, [768], arg116_1, arg117_1, 1e-06, )
  getitem_57 = native_layer_norm_19[0]
  view_77 = aten.view.default(getitem_57, [196, 768], )
  t_38 = aten.t.default(arg118_1, )
  addmm_28 = aten.addmm.default(arg119_1, view_77, t_38, )
  view_78 = aten.view.default(addmm_28, [1, 196, 3072], )
  gelu_19 = aten.gelu.default(view_78, )
  clone_39 = aten.clone.default(gelu_19, )
  view_79 = aten.view.default(clone_39, [196, 3072], )
  t_39 = aten.t.default(arg120_1, )
  addmm_29 = aten.addmm.default(arg121_1, view_79, t_39, )
  view_80 = aten.view.default(addmm_29, [1, 196, 768], )
  clone_40 = aten.clone.default(view_80, )
  add_29 = aten.add.Tensor(add_28, clone_40, )
  native_layer_norm_20 = aten.native_layer_norm.default(add_29, [768], arg122_1, arg123_1, 1e-06, )
  getitem_60 = native_layer_norm_20[0]
  transpose_21 = aten.transpose.int(getitem_60, 1, 2, )
  t_40 = aten.t.default(arg124_1, )
  view_81 = aten.view.default(transpose_21, [768, 196], )
  mm_10 = aten.mm.default(view_81, t_40, )
  view_82 = aten.view.default(mm_10, [1, 768, 384], )
  add_30 = aten.add.Tensor(view_82, arg125_1, )
  gelu_20 = aten.gelu.default(add_30, )
  clone_41 = aten.clone.default(gelu_20, )
  view_83 = aten.view.default(clone_41, [768, 384], )
  t_41 = aten.t.default(arg126_1, )
  addmm_30 = aten.addmm.default(arg127_1, view_83, t_41, )
  view_84 = aten.view.default(addmm_30, [1, 768, 196], )
  clone_42 = aten.clone.default(view_84, )
  transpose_22 = aten.transpose.int(clone_42, 1, 2, )
  add_31 = aten.add.Tensor(add_29, transpose_22, )
  native_layer_norm_21 = aten.native_layer_norm.default(add_31, [768], arg128_1, arg129_1, 1e-06, )
  getitem_63 = native_layer_norm_21[0]
  view_85 = aten.view.default(getitem_63, [196, 768], )
  t_42 = aten.t.default(arg130_1, )
  addmm_31 = aten.addmm.default(arg131_1, view_85, t_42, )
  view_86 = aten.view.default(addmm_31, [1, 196, 3072], )
  gelu_21 = aten.gelu.default(view_86, )
  clone_43 = aten.clone.default(gelu_21, )
  view_87 = aten.view.default(clone_43, [196, 3072], )
  t_43 = aten.t.default(arg132_1, )
  addmm_32 = aten.addmm.default(arg133_1, view_87, t_43, )
  view_88 = aten.view.default(addmm_32, [1, 196, 768], )
  clone_44 = aten.clone.default(view_88, )
  add_32 = aten.add.Tensor(add_31, clone_44, )
  native_layer_norm_22 = aten.native_layer_norm.default(add_32, [768], arg134_1, arg135_1, 1e-06, )
  getitem_66 = native_layer_norm_22[0]
  transpose_23 = aten.transpose.int(getitem_66, 1, 2, )
  t_44 = aten.t.default(arg136_1, )
  view_89 = aten.view.default(transpose_23, [768, 196], )
  mm_11 = aten.mm.default(view_89, t_44, )
  view_90 = aten.view.default(mm_11, [1, 768, 384], )
  add_33 = aten.add.Tensor(view_90, arg137_1, )
  gelu_22 = aten.gelu.default(add_33, )
  clone_45 = aten.clone.default(gelu_22, )
  view_91 = aten.view.default(clone_45, [768, 384], )
  t_45 = aten.t.default(arg138_1, )
  addmm_33 = aten.addmm.default(arg139_1, view_91, t_45, )
  view_92 = aten.view.default(addmm_33, [1, 768, 196], )
  clone_46 = aten.clone.default(view_92, )
  transpose_24 = aten.transpose.int(clone_46, 1, 2, )
  add_34 = aten.add.Tensor(add_32, transpose_24, )
  native_layer_norm_23 = aten.native_layer_norm.default(add_34, [768], arg140_1, arg141_1, 1e-06, )
  getitem_69 = native_layer_norm_23[0]
  view_93 = aten.view.default(getitem_69, [196, 768], )
  t_46 = aten.t.default(arg142_1, )
  addmm_34 = aten.addmm.default(arg143_1, view_93, t_46, )
  view_94 = aten.view.default(addmm_34, [1, 196, 3072], )
  gelu_23 = aten.gelu.default(view_94, )
  clone_47 = aten.clone.default(gelu_23, )
  view_95 = aten.view.default(clone_47, [196, 3072], )
  t_47 = aten.t.default(arg144_1, )
  addmm_35 = aten.addmm.default(arg145_1, view_95, t_47, )
  view_96 = aten.view.default(addmm_35, [1, 196, 768], )
  clone_48 = aten.clone.default(view_96, )
  add_35 = aten.add.Tensor(add_34, clone_48, )
  native_layer_norm_24 = aten.native_layer_norm.default(add_35, [768], arg146_1, arg147_1, 1e-06, )
  getitem_72 = native_layer_norm_24[0]
  mean = aten.mean.dim(getitem_72, [1], )
  clone_49 = aten.clone.default(mean, )
  t_48 = aten.t.default(arg148_1, )
  addmm_36 = aten.addmm.default(arg149_1, clone_49, t_48, )
  # return (addmm_36,)
  convolution_default = aten.convolution.default(arg150_1, arg0_1, arg1_1, [16, 16], [0, 0], [1, 1], False, [0, 0], 1, )
  test_accuracy(convolution_default, convolution_default) # Dodato
  test_accuracy(convolution, convolution_default)
  ttnn_from_torch = ttnn.from_torch(convolution_default, layout = ttnn.ROW_MAJOR_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_reshape_1 = ttnn.reshape(ttnn_from_torch, (1, 768, 196), )
  ttnn_from_device = ttnn.from_device(ttnn_reshape_1, )
  ttnn_to_layout = ttnn.to_layout(ttnn_from_device, ttnn.TILE_LAYOUT, )
  ttnn_to_device = ttnn.to_device(ttnn_to_layout, device = device)
  ttnn_transpose = ttnn.transpose(ttnn_to_device, 1, 2, )
  ttnn_from_torch_1 = ttnn.from_torch(arg2_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_2 = ttnn.from_torch(arg3_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_ = ttnn.layer_norm(ttnn_transpose, epsilon = 1e-06, weight = ttnn_from_torch_1, bias = ttnn_from_torch_2)
  ttnn_layer_norm_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_transpose), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_1), 
                                                                  ttnn.to_torch(ttnn_from_torch_2), 1e-06, )[0]
  ttnn_layer_norm = ttnn.from_torch(ttnn_layer_norm_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_), ttnn_layer_norm))
  ttnn_transpose_1 = ttnn.transpose(ttnn_layer_norm, 1, 2, )
  ttnn_from_torch_3 = ttnn.from_torch(arg4_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_2 = ttnn.transpose(ttnn_from_torch_3, 0, 1, )
  ttnn_from_device_1 = ttnn.from_device(ttnn_transpose_1, )
  ttnn_to_layout_1 = ttnn.to_layout(ttnn_from_device_1, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_2 = ttnn.reshape(ttnn_to_layout_1, (768, 196), )
  ttnn_from_device_2 = ttnn.from_device(ttnn_reshape_2, )
  ttnn_to_layout_2 = ttnn.to_layout(ttnn_from_device_2, ttnn.TILE_LAYOUT, )
  ttnn_to_device_1 = ttnn.to_device(ttnn_to_layout_2, device = device)
  ttnn_matmul = ttnn.matmul(ttnn_to_device_1, ttnn_transpose_2, )
  ttnn_from_device_3 = ttnn.from_device(ttnn_matmul, )
  ttnn_to_layout_3 = ttnn.to_layout(ttnn_from_device_3, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_3 = ttnn.reshape(ttnn_to_layout_3, (1, 768, 384), )
  ttnn_from_device_4 = ttnn.from_device(ttnn_reshape_3, )
  ttnn_to_layout_4 = ttnn.to_layout(ttnn_from_device_4, ttnn.TILE_LAYOUT, )
  ttnn_to_device_2 = ttnn.to_device(ttnn_to_layout_4, device = device)
  ttnn_from_torch_4 = ttnn.from_torch(arg5_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_37 = ttnn.add(ttnn_to_device_2, ttnn_from_torch_4, )
  ttnn_gelu = ttnn.gelu(ttnn_add_37, )
  #ttnn_gelu_intermediate = aten.gelu.default(ttnn.to_torch(ttnn_add_37), )
  #ttnn_gelu = ttnn.from_torch(ttnn_gelu_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  #print("ttnn_gelu: ", test_accuracy(ttnn.to_torch(ttnn_gelu_), ttnn_gelu))
  ttnn_prefix_clone = clone_wrapper(ttnn_gelu, )
  ttnn_from_device_5 = ttnn.from_device(ttnn_prefix_clone, )
  ttnn_to_layout_5 = ttnn.to_layout(ttnn_from_device_5, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_4 = ttnn.reshape(ttnn_to_layout_5, (768, 384), )
  ttnn_from_torch_5 = ttnn.from_torch(arg6_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_3 = ttnn.transpose(ttnn_from_torch_5, 0, 1, )
  ttnn_from_device_6 = ttnn.from_device(ttnn_reshape_4, )
  ttnn_to_layout_6 = ttnn.to_layout(ttnn_from_device_6, ttnn.TILE_LAYOUT, )
  ttnn_to_device_3 = ttnn.to_device(ttnn_to_layout_6, device = device)
  ttnn_matmul_1 = ttnn.matmul(ttnn_to_device_3, ttnn_transpose_3, )
  ttnn_from_torch_6 = ttnn.from_torch(arg7_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add = ttnn.add(ttnn_from_torch_6, ttnn_matmul_1, )
  ttnn_from_device_7 = ttnn.from_device(ttnn_add, )
  ttnn_to_layout_7 = ttnn.to_layout(ttnn_from_device_7, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_5 = ttnn.reshape(ttnn_to_layout_7, (1, 768, 196), )
  ttnn_from_device_8 = ttnn.from_device(ttnn_reshape_5, )
  ttnn_to_layout_8 = ttnn.to_layout(ttnn_from_device_8, ttnn.TILE_LAYOUT, )
  ttnn_to_device_4 = ttnn.to_device(ttnn_to_layout_8, device = device)
  ttnn_prefix_clone_1 = clone_wrapper(ttnn_to_device_4, )
  ttnn_transpose_4 = ttnn.transpose(ttnn_prefix_clone_1, 1, 2, )
  ttnn_add_38 = ttnn.add(ttnn_transpose, ttnn_transpose_4, )
  ttnn_from_torch_7 = ttnn.from_torch(arg8_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_8 = ttnn.from_torch(arg9_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_1_ = ttnn.layer_norm(ttnn_add_38, epsilon = 1e-06, weight = ttnn_from_torch_7, bias = ttnn_from_torch_8)
  ttnn_layer_norm_1_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_add_38), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_7), 
                                                                  ttnn.to_torch(ttnn_from_torch_8), 1e-06, )[0]
  ttnn_layer_norm_1 = ttnn.from_torch(ttnn_layer_norm_1_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_1_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_1_), ttnn_layer_norm_1))
    # Pocetak koda za proveru
  print(f"mixer_ln1_input: {ttnn_add_38}")
  print(f"mixer_ln1_weight: {ttnn_from_torch_7}")
  print(f"mixer_ln1_bias: {ttnn_from_torch_8}")
  def save_tensor_to_csv(tensor, filename):
    import pandas as pd
    tensor = tensor.contiguous()
    if tensor.dtype == torch.bfloat16:
        tensor = tensor.to(torch.float32)
    if tensor.ndim == 0:  # Scalar
        df = pd.DataFrame([tensor.item()])
    elif tensor.ndim == 1:  # 1D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 2:  # 2D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 3:  # 3D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    elif tensor.ndim == 4:  # 4D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    else:
        raise ValueError("Unsupported tensor dimension")
    df.to_csv(filename, index=False)
  def load_tensor_from_csv(filename, shape):
    import pandas as pd
    df = pd.read_csv(filename)
    data = df.values
    tensor = torch.tensor(data)
    # Reshape the tensor to the original shape
    tensor = tensor.view(shape)
    return tensor

  x_1 = ttnn.to_torch(ttnn_add_38)
  x_2 = ttnn.to_torch(ttnn_from_torch_7)
  x_3 = ttnn.to_torch(ttnn_from_torch_8)
  x1_shape = x_1.shape
  x2_shape = x_2.shape
  x3_shape = x_3.shape
  save_tensor_to_csv(x_1, "mixer_ln1_input.csv")
  save_tensor_to_csv(x_2, "mixer_ln1_weight.csv")
  save_tensor_to_csv(x_3, "mixer_ln1_bias.csv")
  load_1 = load_tensor_from_csv("mixer_ln1_input.csv", x1_shape)
  load_2 = load_tensor_from_csv("mixer_ln1_weight.csv", x2_shape)
  load_3 = load_tensor_from_csv("mixer_ln1_bias.csv", x3_shape)
  test_accuracy(x_1, load_1)
  test_accuracy(x_2, load_2)
  test_accuracy(x_3, load_3)
  # Kraj koda za proveru
  test_accuracy(native_layer_norm_1[0], ttnn_layer_norm_1)
  ttnn_from_device_9 = ttnn.from_device(ttnn_layer_norm_1, )
  ttnn_to_layout_9 = ttnn.to_layout(ttnn_from_device_9, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_6 = ttnn.reshape(ttnn_to_layout_9, (196, 768), )
  ttnn_from_torch_9 = ttnn.from_torch(arg10_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_5 = ttnn.transpose(ttnn_from_torch_9, 0, 1, )
  ttnn_from_device_10 = ttnn.from_device(ttnn_reshape_6, )
  ttnn_to_layout_10 = ttnn.to_layout(ttnn_from_device_10, ttnn.TILE_LAYOUT, )
  ttnn_to_device_5 = ttnn.to_device(ttnn_to_layout_10, device = device)
  ttnn_matmul_2 = ttnn.matmul(ttnn_to_device_5, ttnn_transpose_5, )
  ttnn_from_torch_10 = ttnn.from_torch(arg11_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_1 = ttnn.add(ttnn_from_torch_10, ttnn_matmul_2, )
  ttnn_from_device_11 = ttnn.from_device(ttnn_add_1, )
  ttnn_to_layout_11 = ttnn.to_layout(ttnn_from_device_11, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_7 = ttnn.reshape(ttnn_to_layout_11, (1, 196, 3072), )
  ttnn_from_device_12 = ttnn.from_device(ttnn_reshape_7, )
  ttnn_to_layout_12 = ttnn.to_layout(ttnn_from_device_12, ttnn.TILE_LAYOUT, )
  ttnn_to_device_6 = ttnn.to_device(ttnn_to_layout_12, device = device)
  ttnn_gelu_1 = ttnn.gelu(ttnn_to_device_6, )
  ttnn_prefix_clone_2 = clone_wrapper(ttnn_gelu_1, )
  ttnn_from_device_13 = ttnn.from_device(ttnn_prefix_clone_2, )
  ttnn_to_layout_13 = ttnn.to_layout(ttnn_from_device_13, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_8 = ttnn.reshape(ttnn_to_layout_13, (196, 3072), )
  ttnn_from_torch_11 = ttnn.from_torch(arg12_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_6 = ttnn.transpose(ttnn_from_torch_11, 0, 1, )
  ttnn_from_device_14 = ttnn.from_device(ttnn_reshape_8, )
  ttnn_to_layout_14 = ttnn.to_layout(ttnn_from_device_14, ttnn.TILE_LAYOUT, )
  ttnn_to_device_7 = ttnn.to_device(ttnn_to_layout_14, device = device)
  ttnn_matmul_3 = ttnn.matmul(ttnn_to_device_7, ttnn_transpose_6, )
  ttnn_from_torch_12 = ttnn.from_torch(arg13_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_2 = ttnn.add(ttnn_from_torch_12, ttnn_matmul_3, )
  ttnn_from_device_15 = ttnn.from_device(ttnn_add_2, )
  ttnn_to_layout_15 = ttnn.to_layout(ttnn_from_device_15, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_9 = ttnn.reshape(ttnn_to_layout_15, (1, 196, 768), )
  ttnn_from_device_16 = ttnn.from_device(ttnn_reshape_9, )
  ttnn_to_layout_16 = ttnn.to_layout(ttnn_from_device_16, ttnn.TILE_LAYOUT, )
  ttnn_to_device_8 = ttnn.to_device(ttnn_to_layout_16, device = device)
  ttnn_prefix_clone_3 = clone_wrapper(ttnn_to_device_8, )
  ttnn_add_39 = ttnn.add(ttnn_add_38, ttnn_prefix_clone_3, )
  ttnn_from_torch_13 = ttnn.from_torch(arg14_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_14 = ttnn.from_torch(arg15_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_2_ = ttnn.layer_norm(ttnn_add_39, epsilon = 1e-06, weight = ttnn_from_torch_13, bias = ttnn_from_torch_14)
  ttnn_layer_norm_2_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_add_39), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_13), 
                                                                  ttnn.to_torch(ttnn_from_torch_14), 1e-06, )[0]
  ttnn_layer_norm_2 = ttnn.from_torch(ttnn_layer_norm_2_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_2_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_2_), ttnn_layer_norm_2))
  test_accuracy(native_layer_norm_2[0], ttnn_layer_norm_2)
  ttnn_transpose_7 = ttnn.transpose(ttnn_layer_norm_2, 1, 2, )
  ttnn_from_torch_15 = ttnn.from_torch(arg16_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_8 = ttnn.transpose(ttnn_from_torch_15, 0, 1, )
  ttnn_from_device_17 = ttnn.from_device(ttnn_transpose_7, )
  ttnn_to_layout_17 = ttnn.to_layout(ttnn_from_device_17, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_10 = ttnn.reshape(ttnn_to_layout_17, (768, 196), )
  ttnn_from_device_18 = ttnn.from_device(ttnn_reshape_10, )
  ttnn_to_layout_18 = ttnn.to_layout(ttnn_from_device_18, ttnn.TILE_LAYOUT, )
  ttnn_to_device_9 = ttnn.to_device(ttnn_to_layout_18, device = device)
  ttnn_matmul_4 = ttnn.matmul(ttnn_to_device_9, ttnn_transpose_8, )
  ttnn_from_device_19 = ttnn.from_device(ttnn_matmul_4, )
  ttnn_to_layout_19 = ttnn.to_layout(ttnn_from_device_19, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_11 = ttnn.reshape(ttnn_to_layout_19, (1, 768, 384), )
  ttnn_from_device_20 = ttnn.from_device(ttnn_reshape_11, )
  ttnn_to_layout_20 = ttnn.to_layout(ttnn_from_device_20, ttnn.TILE_LAYOUT, )
  ttnn_to_device_10 = ttnn.to_device(ttnn_to_layout_20, device = device)
  ttnn_from_torch_16 = ttnn.from_torch(arg17_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_40 = ttnn.add(ttnn_to_device_10, ttnn_from_torch_16, )
  ttnn_gelu_2 = ttnn.gelu(ttnn_add_40, )
  ttnn_prefix_clone_4 = clone_wrapper(ttnn_gelu_2, )
  ttnn_from_device_21 = ttnn.from_device(ttnn_prefix_clone_4, )
  ttnn_to_layout_21 = ttnn.to_layout(ttnn_from_device_21, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_12 = ttnn.reshape(ttnn_to_layout_21, (768, 384), )
  ttnn_from_torch_17 = ttnn.from_torch(arg18_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_9 = ttnn.transpose(ttnn_from_torch_17, 0, 1, )
  ttnn_from_device_22 = ttnn.from_device(ttnn_reshape_12, )
  ttnn_to_layout_22 = ttnn.to_layout(ttnn_from_device_22, ttnn.TILE_LAYOUT, )
  ttnn_to_device_11 = ttnn.to_device(ttnn_to_layout_22, device = device)
  ttnn_matmul_5 = ttnn.matmul(ttnn_to_device_11, ttnn_transpose_9, )
  ttnn_from_torch_18 = ttnn.from_torch(arg19_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_3 = ttnn.add(ttnn_from_torch_18, ttnn_matmul_5, )
  ttnn_from_device_23 = ttnn.from_device(ttnn_add_3, )
  ttnn_to_layout_23 = ttnn.to_layout(ttnn_from_device_23, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_13 = ttnn.reshape(ttnn_to_layout_23, (1, 768, 196), )
  ttnn_from_device_24 = ttnn.from_device(ttnn_reshape_13, )
  ttnn_to_layout_24 = ttnn.to_layout(ttnn_from_device_24, ttnn.TILE_LAYOUT, )
  ttnn_to_device_12 = ttnn.to_device(ttnn_to_layout_24, device = device)
  ttnn_prefix_clone_5 = clone_wrapper(ttnn_to_device_12, )
  ttnn_transpose_10 = ttnn.transpose(ttnn_prefix_clone_5, 1, 2, )
  ttnn_add_41 = ttnn.add(ttnn_add_39, ttnn_transpose_10, )
  ttnn_from_torch_19 = ttnn.from_torch(arg20_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_20 = ttnn.from_torch(arg21_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_3_ = ttnn.layer_norm(ttnn_add_41, epsilon = 1e-06, weight = ttnn_from_torch_19, bias = ttnn_from_torch_20)
  ttnn_layer_norm_3_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_add_41), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_19), 
                                                                  ttnn.to_torch(ttnn_from_torch_20), 1e-06, )[0]
  ttnn_layer_norm_3 = ttnn.from_torch(ttnn_layer_norm_3_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_3_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_3_), ttnn_layer_norm_3))
    # Pocetak koda za proveru
  print(f"mixer_ln3_input: {ttnn_add_41}")
  print(f"mixer_ln3_weight: {ttnn_from_torch_19}")
  print(f"mixer_ln3_bias: {ttnn_from_torch_20}")
  def save_tensor_to_csv(tensor, filename):
    import pandas as pd
    tensor = tensor.contiguous()
    if tensor.dtype == torch.bfloat16:
        tensor = tensor.to(torch.float32)
    if tensor.ndim == 0:  # Scalar
        df = pd.DataFrame([tensor.item()])
    elif tensor.ndim == 1:  # 1D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 2:  # 2D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 3:  # 3D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    elif tensor.ndim == 4:  # 4D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    else:
        raise ValueError("Unsupported tensor dimension")
    df.to_csv(filename, index=False)
  def load_tensor_from_csv(filename, shape):
    import pandas as pd
    df = pd.read_csv(filename)
    data = df.values
    tensor = torch.tensor(data)
    # Reshape the tensor to the original shape
    tensor = tensor.view(shape)
    return tensor
  x_1 = ttnn.to_torch(ttnn_add_41)
  x_2 = ttnn.to_torch(ttnn_from_torch_19)
  x_3 = ttnn.to_torch(ttnn_from_torch_20)
  x1_shape = x_1.shape
  x2_shape = x_2.shape
  x3_shape = x_3.shape
  save_tensor_to_csv(x_1, "mixer_ln3_input.csv")
  save_tensor_to_csv(x_2, "mixer_ln3_weight.csv")
  save_tensor_to_csv(x_3, "mixer_ln3_bias.csv")
  load_1 = load_tensor_from_csv("mixer_ln3_input.csv", x1_shape)
  load_2 = load_tensor_from_csv("mixer_ln3_weight.csv", x2_shape)
  load_3 = load_tensor_from_csv("mixer_ln3_bias.csv", x3_shape)
  test_accuracy(x_1, load_1)
  test_accuracy(x_2, load_2)
  test_accuracy(x_3, load_3)
  # Kraj koda za proveru
  test_accuracy(native_layer_norm_3[0], ttnn_layer_norm_3)
  ttnn_from_device_25 = ttnn.from_device(ttnn_layer_norm_3, )
  ttnn_to_layout_25 = ttnn.to_layout(ttnn_from_device_25, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_14 = ttnn.reshape(ttnn_to_layout_25, (196, 768), )
  ttnn_from_torch_21 = ttnn.from_torch(arg22_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_11 = ttnn.transpose(ttnn_from_torch_21, 0, 1, )
  ttnn_from_device_26 = ttnn.from_device(ttnn_reshape_14, )
  ttnn_to_layout_26 = ttnn.to_layout(ttnn_from_device_26, ttnn.TILE_LAYOUT, )
  ttnn_to_device_13 = ttnn.to_device(ttnn_to_layout_26, device = device)
  ttnn_matmul_6 = ttnn.matmul(ttnn_to_device_13, ttnn_transpose_11, )
  ttnn_from_torch_22 = ttnn.from_torch(arg23_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_4 = ttnn.add(ttnn_from_torch_22, ttnn_matmul_6, )
  ttnn_from_device_27 = ttnn.from_device(ttnn_add_4, )
  ttnn_to_layout_27 = ttnn.to_layout(ttnn_from_device_27, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_15 = ttnn.reshape(ttnn_to_layout_27, (1, 196, 3072), )
  ttnn_from_device_28 = ttnn.from_device(ttnn_reshape_15, )
  ttnn_to_layout_28 = ttnn.to_layout(ttnn_from_device_28, ttnn.TILE_LAYOUT, )
  ttnn_to_device_14 = ttnn.to_device(ttnn_to_layout_28, device = device)
  ttnn_gelu_3 = ttnn.gelu(ttnn_to_device_14, )
  ttnn_prefix_clone_6 = clone_wrapper(ttnn_gelu_3, )
  ttnn_from_device_29 = ttnn.from_device(ttnn_prefix_clone_6, )
  ttnn_to_layout_29 = ttnn.to_layout(ttnn_from_device_29, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_16 = ttnn.reshape(ttnn_to_layout_29, (196, 3072), )
  ttnn_from_torch_23 = ttnn.from_torch(arg24_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_12 = ttnn.transpose(ttnn_from_torch_23, 0, 1, )
  ttnn_from_device_30 = ttnn.from_device(ttnn_reshape_16, )
  ttnn_to_layout_30 = ttnn.to_layout(ttnn_from_device_30, ttnn.TILE_LAYOUT, )
  ttnn_to_device_15 = ttnn.to_device(ttnn_to_layout_30, device = device)
  ttnn_matmul_7 = ttnn.matmul(ttnn_to_device_15, ttnn_transpose_12, )
  ttnn_from_torch_24 = ttnn.from_torch(arg25_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_5 = ttnn.add(ttnn_from_torch_24, ttnn_matmul_7, )
  ttnn_from_device_31 = ttnn.from_device(ttnn_add_5, )
  ttnn_to_layout_31 = ttnn.to_layout(ttnn_from_device_31, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_17 = ttnn.reshape(ttnn_to_layout_31, (1, 196, 768), )
  ttnn_from_device_32 = ttnn.from_device(ttnn_reshape_17, )
  ttnn_to_layout_32 = ttnn.to_layout(ttnn_from_device_32, ttnn.TILE_LAYOUT, )
  ttnn_to_device_16 = ttnn.to_device(ttnn_to_layout_32, device = device)
  ttnn_prefix_clone_7 = clone_wrapper(ttnn_to_device_16, )
  ttnn_add_42 = ttnn.add(ttnn_add_41, ttnn_prefix_clone_7, )
  ttnn_from_torch_25 = ttnn.from_torch(arg26_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_26 = ttnn.from_torch(arg27_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_4_ = ttnn.layer_norm(ttnn_add_42, epsilon = 1e-06, weight = ttnn_from_torch_25, bias = ttnn_from_torch_26)
  ttnn_layer_norm_4_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_add_42), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_25), 
                                                                  ttnn.to_torch(ttnn_from_torch_26), 1e-06, )[0]
  ttnn_layer_norm_4 = ttnn.from_torch(ttnn_layer_norm_4_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_4_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_4_), ttnn_layer_norm_4))
    # Pocetak koda za proveru
  print(f"mixer_ln4_input: {ttnn_add_42}")
  print(f"mixer_ln4_weight: {ttnn_from_torch_25}")
  print(f"mixer_ln4_bias: {ttnn_from_torch_26}")
  def save_tensor_to_csv(tensor, filename):
    import pandas as pd
    tensor = tensor.contiguous()
    if tensor.dtype == torch.bfloat16:
        tensor = tensor.to(torch.float32)
    if tensor.ndim == 0:  # Scalar
        df = pd.DataFrame([tensor.item()])
    elif tensor.ndim == 1:  # 1D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 2:  # 2D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 3:  # 3D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    elif tensor.ndim == 4:  # 4D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    else:
        raise ValueError("Unsupported tensor dimension")
    df.to_csv(filename, index=False)
  def load_tensor_from_csv(filename, shape):
    import pandas as pd
    df = pd.read_csv(filename)
    data = df.values
    tensor = torch.tensor(data)
    # Reshape the tensor to the original shape
    tensor = tensor.view(shape)
    return tensor
  x_1 = ttnn.to_torch(ttnn_add_42)
  x_2 = ttnn.to_torch(ttnn_from_torch_25)
  x_3 = ttnn.to_torch(ttnn_from_torch_26)
  x1_shape = x_1.shape
  x2_shape = x_2.shape
  x3_shape = x_3.shape
  save_tensor_to_csv(x_1, "mixer_ln4_input.csv")
  save_tensor_to_csv(x_2, "mixer_ln4_weight.csv")
  save_tensor_to_csv(x_3, "mixer_ln4_bias.csv")
  load_1 = load_tensor_from_csv("mixer_ln4_input.csv", x1_shape)
  load_2 = load_tensor_from_csv("mixer_ln4_weight.csv", x2_shape)
  load_3 = load_tensor_from_csv("mixer_ln4_bias.csv", x3_shape)
  test_accuracy(x_1, load_1)
  test_accuracy(x_2, load_2)
  test_accuracy(x_3, load_3)
  # Kraj koda za proveru
  test_accuracy(native_layer_norm_4[0], ttnn_layer_norm_4)
  ttnn_transpose_13 = ttnn.transpose(ttnn_layer_norm_4, 1, 2, )
  ttnn_from_torch_27 = ttnn.from_torch(arg28_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_14 = ttnn.transpose(ttnn_from_torch_27, 0, 1, )
  ttnn_from_device_33 = ttnn.from_device(ttnn_transpose_13, )
  ttnn_to_layout_33 = ttnn.to_layout(ttnn_from_device_33, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_18 = ttnn.reshape(ttnn_to_layout_33, (768, 196), )
  ttnn_from_device_34 = ttnn.from_device(ttnn_reshape_18, )
  ttnn_to_layout_34 = ttnn.to_layout(ttnn_from_device_34, ttnn.TILE_LAYOUT, )
  ttnn_to_device_17 = ttnn.to_device(ttnn_to_layout_34, device = device)
  ttnn_matmul_8 = ttnn.matmul(ttnn_to_device_17, ttnn_transpose_14, )
  ttnn_from_device_35 = ttnn.from_device(ttnn_matmul_8, )
  ttnn_to_layout_35 = ttnn.to_layout(ttnn_from_device_35, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_19 = ttnn.reshape(ttnn_to_layout_35, (1, 768, 384), )
  ttnn_from_device_36 = ttnn.from_device(ttnn_reshape_19, )
  ttnn_to_layout_36 = ttnn.to_layout(ttnn_from_device_36, ttnn.TILE_LAYOUT, )
  ttnn_to_device_18 = ttnn.to_device(ttnn_to_layout_36, device = device)
  ttnn_from_torch_28 = ttnn.from_torch(arg29_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_43 = ttnn.add(ttnn_to_device_18, ttnn_from_torch_28, )
  ttnn_gelu_4 = ttnn.gelu(ttnn_add_43, )
  ttnn_prefix_clone_8 = clone_wrapper(ttnn_gelu_4, )
  ttnn_from_device_37 = ttnn.from_device(ttnn_prefix_clone_8, )
  ttnn_to_layout_37 = ttnn.to_layout(ttnn_from_device_37, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_20 = ttnn.reshape(ttnn_to_layout_37, (768, 384), )
  ttnn_from_torch_29 = ttnn.from_torch(arg30_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_15 = ttnn.transpose(ttnn_from_torch_29, 0, 1, )
  ttnn_from_device_38 = ttnn.from_device(ttnn_reshape_20, )
  ttnn_to_layout_38 = ttnn.to_layout(ttnn_from_device_38, ttnn.TILE_LAYOUT, )
  ttnn_to_device_19 = ttnn.to_device(ttnn_to_layout_38, device = device)
  ttnn_matmul_9 = ttnn.matmul(ttnn_to_device_19, ttnn_transpose_15, )
  ttnn_from_torch_30 = ttnn.from_torch(arg31_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_6 = ttnn.add(ttnn_from_torch_30, ttnn_matmul_9, )
  ttnn_from_device_39 = ttnn.from_device(ttnn_add_6, )
  ttnn_to_layout_39 = ttnn.to_layout(ttnn_from_device_39, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_21 = ttnn.reshape(ttnn_to_layout_39, (1, 768, 196), )
  ttnn_from_device_40 = ttnn.from_device(ttnn_reshape_21, )
  ttnn_to_layout_40 = ttnn.to_layout(ttnn_from_device_40, ttnn.TILE_LAYOUT, )
  ttnn_to_device_20 = ttnn.to_device(ttnn_to_layout_40, device = device)
  ttnn_prefix_clone_9 = clone_wrapper(ttnn_to_device_20, )
  ttnn_transpose_16 = ttnn.transpose(ttnn_prefix_clone_9, 1, 2, )
  ttnn_add_44 = ttnn.add(ttnn_add_42, ttnn_transpose_16, )
  ttnn_from_torch_31 = ttnn.from_torch(arg32_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_32 = ttnn.from_torch(arg33_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_5_ = ttnn.layer_norm(ttnn_add_44, epsilon = 1e-06, weight = ttnn_from_torch_31, bias = ttnn_from_torch_32)
  ttnn_layer_norm_5_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_add_44), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_31), 
                                                                  ttnn.to_torch(ttnn_from_torch_32), 1e-06, )[0]
  ttnn_layer_norm_5 = ttnn.from_torch(ttnn_layer_norm_5_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_5_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_5_), ttnn_layer_norm_5))
    # Pocetak koda za proveru
  print(f"mixer_ln5_input: {ttnn_add_44}")
  print(f"mixer_ln5_weight: {ttnn_from_torch_31}")
  print(f"mixer_ln5_bias: {ttnn_from_torch_32}")
  def save_tensor_to_csv(tensor, filename):
    import pandas as pd
    tensor = tensor.contiguous()
    if tensor.dtype == torch.bfloat16:
        tensor = tensor.to(torch.float32)
    if tensor.ndim == 0:  # Scalar
        df = pd.DataFrame([tensor.item()])
    elif tensor.ndim == 1:  # 1D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 2:  # 2D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 3:  # 3D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    elif tensor.ndim == 4:  # 4D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    else:
        raise ValueError("Unsupported tensor dimension")
    df.to_csv(filename, index=False)
  def load_tensor_from_csv(filename, shape):
    import pandas as pd
    df = pd.read_csv(filename)
    data = df.values
    tensor = torch.tensor(data)
    # Reshape the tensor to the original shape
    tensor = tensor.view(shape)
    return tensor
  x_1 = ttnn.to_torch(ttnn_add_44)
  x_2 = ttnn.to_torch(ttnn_from_torch_31)
  x_3 = ttnn.to_torch(ttnn_from_torch_32)
  x1_shape = x_1.shape
  x2_shape = x_2.shape
  x3_shape = x_3.shape
  save_tensor_to_csv(x_1, "mixer_ln5_input.csv")
  save_tensor_to_csv(x_2, "mixer_ln5_weight.csv")
  save_tensor_to_csv(x_3, "mixer_ln5_bias.csv")
  load_1 = load_tensor_from_csv("mixer_ln5_input.csv", x1_shape)
  load_2 = load_tensor_from_csv("mixer_ln5_weight.csv", x2_shape)
  load_3 = load_tensor_from_csv("mixer_ln5_bias.csv", x3_shape)
  test_accuracy(x_1, load_1)
  test_accuracy(x_2, load_2)
  test_accuracy(x_3, load_3)
  # Kraj koda za proveru
  test_accuracy(native_layer_norm_5[0], ttnn_layer_norm_5)
  ttnn_from_device_41 = ttnn.from_device(ttnn_layer_norm_5, )
  ttnn_to_layout_41 = ttnn.to_layout(ttnn_from_device_41, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_22 = ttnn.reshape(ttnn_to_layout_41, (196, 768), )
  ttnn_from_torch_33 = ttnn.from_torch(arg34_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_17 = ttnn.transpose(ttnn_from_torch_33, 0, 1, )
  ttnn_from_device_42 = ttnn.from_device(ttnn_reshape_22, )
  ttnn_to_layout_42 = ttnn.to_layout(ttnn_from_device_42, ttnn.TILE_LAYOUT, )
  ttnn_to_device_21 = ttnn.to_device(ttnn_to_layout_42, device = device)
  ttnn_matmul_10 = ttnn.matmul(ttnn_to_device_21, ttnn_transpose_17, )
  ttnn_from_torch_34 = ttnn.from_torch(arg35_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_7 = ttnn.add(ttnn_from_torch_34, ttnn_matmul_10, )
  ttnn_from_device_43 = ttnn.from_device(ttnn_add_7, )
  ttnn_to_layout_43 = ttnn.to_layout(ttnn_from_device_43, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_23 = ttnn.reshape(ttnn_to_layout_43, (1, 196, 3072), )
  ttnn_from_device_44 = ttnn.from_device(ttnn_reshape_23, )
  ttnn_to_layout_44 = ttnn.to_layout(ttnn_from_device_44, ttnn.TILE_LAYOUT, )
  ttnn_to_device_22 = ttnn.to_device(ttnn_to_layout_44, device = device)
  ttnn_gelu_5 = ttnn.gelu(ttnn_to_device_22, )
  ttnn_prefix_clone_10 = clone_wrapper(ttnn_gelu_5, )
  ttnn_from_device_45 = ttnn.from_device(ttnn_prefix_clone_10, )
  ttnn_to_layout_45 = ttnn.to_layout(ttnn_from_device_45, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_24 = ttnn.reshape(ttnn_to_layout_45, (196, 3072), )
  ttnn_from_torch_35 = ttnn.from_torch(arg36_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_18 = ttnn.transpose(ttnn_from_torch_35, 0, 1, )
  ttnn_from_device_46 = ttnn.from_device(ttnn_reshape_24, )
  ttnn_to_layout_46 = ttnn.to_layout(ttnn_from_device_46, ttnn.TILE_LAYOUT, )
  ttnn_to_device_23 = ttnn.to_device(ttnn_to_layout_46, device = device)
  ttnn_matmul_11 = ttnn.matmul(ttnn_to_device_23, ttnn_transpose_18, )
  ttnn_from_torch_36 = ttnn.from_torch(arg37_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_8 = ttnn.add(ttnn_from_torch_36, ttnn_matmul_11, )
  ttnn_from_device_47 = ttnn.from_device(ttnn_add_8, )
  ttnn_to_layout_47 = ttnn.to_layout(ttnn_from_device_47, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_25 = ttnn.reshape(ttnn_to_layout_47, (1, 196, 768), )
  ttnn_from_device_48 = ttnn.from_device(ttnn_reshape_25, )
  ttnn_to_layout_48 = ttnn.to_layout(ttnn_from_device_48, ttnn.TILE_LAYOUT, )
  ttnn_to_device_24 = ttnn.to_device(ttnn_to_layout_48, device = device)
  ttnn_prefix_clone_11 = clone_wrapper(ttnn_to_device_24, )
  ttnn_add_45 = ttnn.add(ttnn_add_44, ttnn_prefix_clone_11, )
  ttnn_from_torch_37 = ttnn.from_torch(arg38_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_38 = ttnn.from_torch(arg39_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_6_ = ttnn.layer_norm(ttnn_add_45, epsilon = 1e-06, weight = ttnn_from_torch_37, bias = ttnn_from_torch_38)
  ttnn_layer_norm_6_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_add_45), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_37), 
                                                                  ttnn.to_torch(ttnn_from_torch_38), 1e-06, )[0]
  ttnn_layer_norm_6 = ttnn.from_torch(ttnn_layer_norm_6_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_6_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_6_), ttnn_layer_norm_6))
    # Pocetak koda za proveru
  print(f"mixer_ln6_input: {ttnn_add_45}")
  print(f"mixer_ln6_weight: {ttnn_from_torch_37}")
  print(f"mixer_ln6_bias: {ttnn_from_torch_38}")
  def save_tensor_to_csv(tensor, filename):
    import pandas as pd
    tensor = tensor.contiguous()
    if tensor.dtype == torch.bfloat16:
        tensor = tensor.to(torch.float32)
    if tensor.ndim == 0:  # Scalar
        df = pd.DataFrame([tensor.item()])
    elif tensor.ndim == 1:  # 1D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 2:  # 2D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 3:  # 3D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    elif tensor.ndim == 4:  # 4D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    else:
        raise ValueError("Unsupported tensor dimension")
    df.to_csv(filename, index=False)
  def load_tensor_from_csv(filename, shape):
    import pandas as pd
    df = pd.read_csv(filename)
    data = df.values
    tensor = torch.tensor(data)
    # Reshape the tensor to the original shape
    tensor = tensor.view(shape)
    return tensor
  x_1 = ttnn.to_torch(ttnn_add_45)
  x_2 = ttnn.to_torch(ttnn_from_torch_37)
  x_3 = ttnn.to_torch(ttnn_from_torch_38)
  x1_shape = x_1.shape
  x2_shape = x_2.shape
  x3_shape = x_3.shape
  save_tensor_to_csv(x_1, "mixer_ln6_input.csv")
  save_tensor_to_csv(x_2, "mixer_ln6_weight.csv")
  save_tensor_to_csv(x_3, "mixer_ln6_bias.csv")
  load_1 = load_tensor_from_csv("mixer_ln6_input.csv", x1_shape)
  load_2 = load_tensor_from_csv("mixer_ln6_weight.csv", x2_shape)
  load_3 = load_tensor_from_csv("mixer_ln6_bias.csv", x3_shape)
  test_accuracy(x_1, load_1)
  test_accuracy(x_2, load_2)
  test_accuracy(x_3, load_3)
  # Kraj koda za proveru
  test_accuracy(native_layer_norm_6[0], ttnn_layer_norm_6)
  ttnn_transpose_19 = ttnn.transpose(ttnn_layer_norm_6, 1, 2, )
  ttnn_from_torch_39 = ttnn.from_torch(arg40_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_20 = ttnn.transpose(ttnn_from_torch_39, 0, 1, )
  ttnn_from_device_49 = ttnn.from_device(ttnn_transpose_19, )
  ttnn_to_layout_49 = ttnn.to_layout(ttnn_from_device_49, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_26 = ttnn.reshape(ttnn_to_layout_49, (768, 196), )
  ttnn_from_device_50 = ttnn.from_device(ttnn_reshape_26, )
  ttnn_to_layout_50 = ttnn.to_layout(ttnn_from_device_50, ttnn.TILE_LAYOUT, )
  ttnn_to_device_25 = ttnn.to_device(ttnn_to_layout_50, device = device)
  ttnn_matmul_12 = ttnn.matmul(ttnn_to_device_25, ttnn_transpose_20, )
  ttnn_from_device_51 = ttnn.from_device(ttnn_matmul_12, )
  ttnn_to_layout_51 = ttnn.to_layout(ttnn_from_device_51, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_27 = ttnn.reshape(ttnn_to_layout_51, (1, 768, 384), )
  ttnn_from_device_52 = ttnn.from_device(ttnn_reshape_27, )
  ttnn_to_layout_52 = ttnn.to_layout(ttnn_from_device_52, ttnn.TILE_LAYOUT, )
  ttnn_to_device_26 = ttnn.to_device(ttnn_to_layout_52, device = device)
  ttnn_from_torch_40 = ttnn.from_torch(arg41_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_46 = ttnn.add(ttnn_to_device_26, ttnn_from_torch_40, )
  ttnn_gelu_6 = ttnn.gelu(ttnn_add_46, )
  ttnn_prefix_clone_12 = clone_wrapper(ttnn_gelu_6, )
  ttnn_from_device_53 = ttnn.from_device(ttnn_prefix_clone_12, )
  ttnn_to_layout_53 = ttnn.to_layout(ttnn_from_device_53, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_28 = ttnn.reshape(ttnn_to_layout_53, (768, 384), )
  ttnn_from_torch_41 = ttnn.from_torch(arg42_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_21 = ttnn.transpose(ttnn_from_torch_41, 0, 1, )
  ttnn_from_device_54 = ttnn.from_device(ttnn_reshape_28, )
  ttnn_to_layout_54 = ttnn.to_layout(ttnn_from_device_54, ttnn.TILE_LAYOUT, )
  ttnn_to_device_27 = ttnn.to_device(ttnn_to_layout_54, device = device)
  ttnn_matmul_13 = ttnn.matmul(ttnn_to_device_27, ttnn_transpose_21, )
  ttnn_from_torch_42 = ttnn.from_torch(arg43_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_9 = ttnn.add(ttnn_from_torch_42, ttnn_matmul_13, )
  ttnn_from_device_55 = ttnn.from_device(ttnn_add_9, )
  ttnn_to_layout_55 = ttnn.to_layout(ttnn_from_device_55, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_29 = ttnn.reshape(ttnn_to_layout_55, (1, 768, 196), )
  ttnn_from_device_56 = ttnn.from_device(ttnn_reshape_29, )
  ttnn_to_layout_56 = ttnn.to_layout(ttnn_from_device_56, ttnn.TILE_LAYOUT, )
  ttnn_to_device_28 = ttnn.to_device(ttnn_to_layout_56, device = device)
  ttnn_prefix_clone_13 = clone_wrapper(ttnn_to_device_28, )
  ttnn_transpose_22 = ttnn.transpose(ttnn_prefix_clone_13, 1, 2, )
  ttnn_add_47 = ttnn.add(ttnn_add_45, ttnn_transpose_22, )
  ttnn_from_torch_43 = ttnn.from_torch(arg44_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_44 = ttnn.from_torch(arg45_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_7_ = ttnn.layer_norm(ttnn_add_47, epsilon = 1e-06, weight = ttnn_from_torch_43, bias = ttnn_from_torch_44)
  ttnn_layer_norm_7_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_add_47), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_43), 
                                                                  ttnn.to_torch(ttnn_from_torch_44), 1e-06, )[0]
  ttnn_layer_norm_7 = ttnn.from_torch(ttnn_layer_norm_7_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_7_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_7_), ttnn_layer_norm_7))
    # Pocetak koda za proveru
  print(f"mixer_ln7_input: {ttnn_add_47}")
  print(f"mixer_ln7_weight: {ttnn_from_torch_43}")
  print(f"mixer_ln7_bias: {ttnn_from_torch_44}")
  def save_tensor_to_csv(tensor, filename):
    import pandas as pd
    tensor = tensor.contiguous()
    if tensor.dtype == torch.bfloat16:
        tensor = tensor.to(torch.float32)
    if tensor.ndim == 0:  # Scalar
        df = pd.DataFrame([tensor.item()])
    elif tensor.ndim == 1:  # 1D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 2:  # 2D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 3:  # 3D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    elif tensor.ndim == 4:  # 4D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    else:
        raise ValueError("Unsupported tensor dimension")
    df.to_csv(filename, index=False)
  def load_tensor_from_csv(filename, shape):
    import pandas as pd
    df = pd.read_csv(filename)
    data = df.values
    tensor = torch.tensor(data)
    # Reshape the tensor to the original shape
    tensor = tensor.view(shape)
    return tensor
  x_1 = ttnn.to_torch(ttnn_add_47)
  x_2 = ttnn.to_torch(ttnn_from_torch_43)
  x_3 = ttnn.to_torch(ttnn_from_torch_44)
  x1_shape = x_1.shape
  x2_shape = x_2.shape
  x3_shape = x_3.shape
  save_tensor_to_csv(x_1, "mixer_ln7_input.csv")
  save_tensor_to_csv(x_2, "mixer_ln7_weight.csv")
  save_tensor_to_csv(x_3, "mixer_ln7_bias.csv")
  load_1 = load_tensor_from_csv("mixer_ln7_input.csv", x1_shape)
  load_2 = load_tensor_from_csv("mixer_ln7_weight.csv", x2_shape)
  load_3 = load_tensor_from_csv("mixer_ln7_bias.csv", x3_shape)
  test_accuracy(x_1, load_1)
  test_accuracy(x_2, load_2)
  test_accuracy(x_3, load_3)
  # Kraj koda za proveru
  test_accuracy(native_layer_norm_7[0], ttnn_layer_norm_7)
  ttnn_from_device_57 = ttnn.from_device(ttnn_layer_norm_7, )
  ttnn_to_layout_57 = ttnn.to_layout(ttnn_from_device_57, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_30 = ttnn.reshape(ttnn_to_layout_57, (196, 768), )
  ttnn_from_torch_45 = ttnn.from_torch(arg46_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_23 = ttnn.transpose(ttnn_from_torch_45, 0, 1, )
  ttnn_from_device_58 = ttnn.from_device(ttnn_reshape_30, )
  ttnn_to_layout_58 = ttnn.to_layout(ttnn_from_device_58, ttnn.TILE_LAYOUT, )
  ttnn_to_device_29 = ttnn.to_device(ttnn_to_layout_58, device = device)
  ttnn_matmul_14 = ttnn.matmul(ttnn_to_device_29, ttnn_transpose_23, )
  ttnn_from_torch_46 = ttnn.from_torch(arg47_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_10 = ttnn.add(ttnn_from_torch_46, ttnn_matmul_14, )
  ttnn_from_device_59 = ttnn.from_device(ttnn_add_10, )
  ttnn_to_layout_59 = ttnn.to_layout(ttnn_from_device_59, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_31 = ttnn.reshape(ttnn_to_layout_59, (1, 196, 3072), )
  ttnn_from_device_60 = ttnn.from_device(ttnn_reshape_31, )
  ttnn_to_layout_60 = ttnn.to_layout(ttnn_from_device_60, ttnn.TILE_LAYOUT, )
  ttnn_to_device_30 = ttnn.to_device(ttnn_to_layout_60, device = device)
  ttnn_gelu_7 = ttnn.gelu(ttnn_to_device_30, )
  ttnn_prefix_clone_14 = clone_wrapper(ttnn_gelu_7, )
  ttnn_from_device_61 = ttnn.from_device(ttnn_prefix_clone_14, )
  ttnn_to_layout_61 = ttnn.to_layout(ttnn_from_device_61, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_32 = ttnn.reshape(ttnn_to_layout_61, (196, 3072), )
  ttnn_from_torch_47 = ttnn.from_torch(arg48_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_24 = ttnn.transpose(ttnn_from_torch_47, 0, 1, )
  ttnn_from_device_62 = ttnn.from_device(ttnn_reshape_32, )
  ttnn_to_layout_62 = ttnn.to_layout(ttnn_from_device_62, ttnn.TILE_LAYOUT, )
  ttnn_to_device_31 = ttnn.to_device(ttnn_to_layout_62, device = device)
  ttnn_matmul_15 = ttnn.matmul(ttnn_to_device_31, ttnn_transpose_24, )
  ttnn_from_torch_48 = ttnn.from_torch(arg49_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_11 = ttnn.add(ttnn_from_torch_48, ttnn_matmul_15, )
  ttnn_from_device_63 = ttnn.from_device(ttnn_add_11, )
  ttnn_to_layout_63 = ttnn.to_layout(ttnn_from_device_63, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_33 = ttnn.reshape(ttnn_to_layout_63, (1, 196, 768), )
  ttnn_from_device_64 = ttnn.from_device(ttnn_reshape_33, )
  ttnn_to_layout_64 = ttnn.to_layout(ttnn_from_device_64, ttnn.TILE_LAYOUT, )
  ttnn_to_device_32 = ttnn.to_device(ttnn_to_layout_64, device = device)
  ttnn_prefix_clone_15 = clone_wrapper(ttnn_to_device_32, )
  ttnn_add_48 = ttnn.add(ttnn_add_47, ttnn_prefix_clone_15, )
  ttnn_from_torch_49 = ttnn.from_torch(arg50_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_50 = ttnn.from_torch(arg51_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_8_ = ttnn.layer_norm(ttnn_add_48, epsilon = 1e-06, weight = ttnn_from_torch_49, bias = ttnn_from_torch_50)
  ttnn_layer_norm_8_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_add_48), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_49), 
                                                                  ttnn.to_torch(ttnn_from_torch_50), 1e-06, )[0]
  ttnn_layer_norm_8 = ttnn.from_torch(ttnn_layer_norm_8_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_8_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_8_), ttnn_layer_norm_8))
    # Pocetak koda za proveru
  print(f"mixer_ln8_input: {ttnn_add_48}")
  print(f"mixer_ln8_weight: {ttnn_from_torch_49}")
  print(f"mixer_ln8_bias: {ttnn_from_torch_50}")
  def save_tensor_to_csv(tensor, filename):
    import pandas as pd
    tensor = tensor.contiguous()
    if tensor.dtype == torch.bfloat16:
        tensor = tensor.to(torch.float32)
    if tensor.ndim == 0:  # Scalar
        df = pd.DataFrame([tensor.item()])
    elif tensor.ndim == 1:  # 1D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 2:  # 2D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 3:  # 3D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    elif tensor.ndim == 4:  # 4D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    else:
        raise ValueError("Unsupported tensor dimension")
    df.to_csv(filename, index=False)
  def load_tensor_from_csv(filename, shape):
    import pandas as pd
    df = pd.read_csv(filename)
    data = df.values
    tensor = torch.tensor(data)
    # Reshape the tensor to the original shape
    tensor = tensor.view(shape)
    return tensor
  x_1 = ttnn.to_torch(ttnn_add_48)
  x_2 = ttnn.to_torch(ttnn_from_torch_49)
  x_3 = ttnn.to_torch(ttnn_from_torch_50)
  x1_shape = x_1.shape
  x2_shape = x_2.shape
  x3_shape = x_3.shape
  save_tensor_to_csv(x_1, "mixer_ln8_input.csv")
  save_tensor_to_csv(x_2, "mixer_ln8_weight.csv")
  save_tensor_to_csv(x_3, "mixer_ln8_bias.csv")
  load_1 = load_tensor_from_csv("mixer_ln8_input.csv", x1_shape)
  load_2 = load_tensor_from_csv("mixer_ln8_weight.csv", x2_shape)
  load_3 = load_tensor_from_csv("mixer_ln8_bias.csv", x3_shape)
  test_accuracy(x_1, load_1)
  test_accuracy(x_2, load_2)
  test_accuracy(x_3, load_3)
  # Kraj koda za proveru
  test_accuracy(native_layer_norm_8[0], ttnn_layer_norm_8)
  ttnn_transpose_25 = ttnn.transpose(ttnn_layer_norm_8, 1, 2, )
  ttnn_from_torch_51 = ttnn.from_torch(arg52_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_26 = ttnn.transpose(ttnn_from_torch_51, 0, 1, )
  ttnn_from_device_65 = ttnn.from_device(ttnn_transpose_25, )
  ttnn_to_layout_65 = ttnn.to_layout(ttnn_from_device_65, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_34 = ttnn.reshape(ttnn_to_layout_65, (768, 196), )
  ttnn_from_device_66 = ttnn.from_device(ttnn_reshape_34, )
  ttnn_to_layout_66 = ttnn.to_layout(ttnn_from_device_66, ttnn.TILE_LAYOUT, )
  ttnn_to_device_33 = ttnn.to_device(ttnn_to_layout_66, device = device)
  ttnn_matmul_16 = ttnn.matmul(ttnn_to_device_33, ttnn_transpose_26, )
  ttnn_from_device_67 = ttnn.from_device(ttnn_matmul_16, )
  ttnn_to_layout_67 = ttnn.to_layout(ttnn_from_device_67, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_35 = ttnn.reshape(ttnn_to_layout_67, (1, 768, 384), )
  ttnn_from_device_68 = ttnn.from_device(ttnn_reshape_35, )
  ttnn_to_layout_68 = ttnn.to_layout(ttnn_from_device_68, ttnn.TILE_LAYOUT, )
  ttnn_to_device_34 = ttnn.to_device(ttnn_to_layout_68, device = device)
  ttnn_from_torch_52 = ttnn.from_torch(arg53_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_49 = ttnn.add(ttnn_to_device_34, ttnn_from_torch_52, )
  ttnn_gelu_8 = ttnn.gelu(ttnn_add_49, )
  ttnn_prefix_clone_16 = clone_wrapper(ttnn_gelu_8, )
  ttnn_from_device_69 = ttnn.from_device(ttnn_prefix_clone_16, )
  ttnn_to_layout_69 = ttnn.to_layout(ttnn_from_device_69, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_36 = ttnn.reshape(ttnn_to_layout_69, (768, 384), )
  ttnn_from_torch_53 = ttnn.from_torch(arg54_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_27 = ttnn.transpose(ttnn_from_torch_53, 0, 1, )
  ttnn_from_device_70 = ttnn.from_device(ttnn_reshape_36, )
  ttnn_to_layout_70 = ttnn.to_layout(ttnn_from_device_70, ttnn.TILE_LAYOUT, )
  ttnn_to_device_35 = ttnn.to_device(ttnn_to_layout_70, device = device)
  ttnn_matmul_17 = ttnn.matmul(ttnn_to_device_35, ttnn_transpose_27, )
  ttnn_from_torch_54 = ttnn.from_torch(arg55_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_12 = ttnn.add(ttnn_from_torch_54, ttnn_matmul_17, )
  ttnn_from_device_71 = ttnn.from_device(ttnn_add_12, )
  ttnn_to_layout_71 = ttnn.to_layout(ttnn_from_device_71, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_37 = ttnn.reshape(ttnn_to_layout_71, (1, 768, 196), )
  ttnn_from_device_72 = ttnn.from_device(ttnn_reshape_37, )
  ttnn_to_layout_72 = ttnn.to_layout(ttnn_from_device_72, ttnn.TILE_LAYOUT, )
  ttnn_to_device_36 = ttnn.to_device(ttnn_to_layout_72, device = device)
  ttnn_prefix_clone_17 = clone_wrapper(ttnn_to_device_36, )
  ttnn_transpose_28 = ttnn.transpose(ttnn_prefix_clone_17, 1, 2, )
  ttnn_add_50 = ttnn.add(ttnn_add_48, ttnn_transpose_28, )
  ttnn_from_torch_55 = ttnn.from_torch(arg56_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_56 = ttnn.from_torch(arg57_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_9_ = ttnn.layer_norm(ttnn_add_50, epsilon = 1e-06, weight = ttnn_from_torch_55, bias = ttnn_from_torch_56)
  ttnn_layer_norm_9_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_add_50), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_55), 
                                                                  ttnn.to_torch(ttnn_from_torch_56), 1e-06, )[0]
  ttnn_layer_norm_9 = ttnn.from_torch(ttnn_layer_norm_9_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_9_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_9_), ttnn_layer_norm_9))
    # Pocetak koda za proveru
  print(f"mixer_ln9_input: {ttnn_add_50}")
  print(f"mixer_ln9_weight: {ttnn_from_torch_55}")
  print(f"mixer_ln9_bias: {ttnn_from_torch_56}")
  def save_tensor_to_csv(tensor, filename):
    import pandas as pd
    tensor = tensor.contiguous()
    if tensor.dtype == torch.bfloat16:
        tensor = tensor.to(torch.float32)
    if tensor.ndim == 0:  # Scalar
        df = pd.DataFrame([tensor.item()])
    elif tensor.ndim == 1:  # 1D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 2:  # 2D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 3:  # 3D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    elif tensor.ndim == 4:  # 4D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    else:
        raise ValueError("Unsupported tensor dimension")
    df.to_csv(filename, index=False)
  def load_tensor_from_csv(filename, shape):
    import pandas as pd
    df = pd.read_csv(filename)
    data = df.values
    tensor = torch.tensor(data)
    # Reshape the tensor to the original shape
    tensor = tensor.view(shape)
    return tensor
  x_1 = ttnn.to_torch(ttnn_add_50)
  x_2 = ttnn.to_torch(ttnn_from_torch_55)
  x_3 = ttnn.to_torch(ttnn_from_torch_56)
  x1_shape = x_1.shape
  x2_shape = x_2.shape
  x3_shape = x_3.shape
  save_tensor_to_csv(x_1, "mixer_ln9_input.csv")
  save_tensor_to_csv(x_2, "mixer_ln9_weight.csv")
  save_tensor_to_csv(x_3, "mixer_ln9_bias.csv")
  load_1 = load_tensor_from_csv("mixer_ln9_input.csv", x1_shape)
  load_2 = load_tensor_from_csv("mixer_ln9_weight.csv", x2_shape)
  load_3 = load_tensor_from_csv("mixer_ln9_bias.csv", x3_shape)
  test_accuracy(x_1, load_1)
  test_accuracy(x_2, load_2)
  test_accuracy(x_3, load_3)
  # Kraj koda za proveru
  test_accuracy(native_layer_norm_9[0], ttnn_layer_norm_9)
  ttnn_from_device_73 = ttnn.from_device(ttnn_layer_norm_9, )
  ttnn_to_layout_73 = ttnn.to_layout(ttnn_from_device_73, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_38 = ttnn.reshape(ttnn_to_layout_73, (196, 768), )
  ttnn_from_torch_57 = ttnn.from_torch(arg58_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_29 = ttnn.transpose(ttnn_from_torch_57, 0, 1, )
  ttnn_from_device_74 = ttnn.from_device(ttnn_reshape_38, )
  ttnn_to_layout_74 = ttnn.to_layout(ttnn_from_device_74, ttnn.TILE_LAYOUT, )
  ttnn_to_device_37 = ttnn.to_device(ttnn_to_layout_74, device = device)
  ttnn_matmul_18 = ttnn.matmul(ttnn_to_device_37, ttnn_transpose_29, )
  ttnn_from_torch_58 = ttnn.from_torch(arg59_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_13 = ttnn.add(ttnn_from_torch_58, ttnn_matmul_18, )
  ttnn_from_device_75 = ttnn.from_device(ttnn_add_13, )
  ttnn_to_layout_75 = ttnn.to_layout(ttnn_from_device_75, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_39 = ttnn.reshape(ttnn_to_layout_75, (1, 196, 3072), )
  ttnn_from_device_76 = ttnn.from_device(ttnn_reshape_39, )
  ttnn_to_layout_76 = ttnn.to_layout(ttnn_from_device_76, ttnn.TILE_LAYOUT, )
  ttnn_to_device_38 = ttnn.to_device(ttnn_to_layout_76, device = device)
  ttnn_gelu_9 = ttnn.gelu(ttnn_to_device_38, )
  ttnn_prefix_clone_18 = clone_wrapper(ttnn_gelu_9, )
  ttnn_from_device_77 = ttnn.from_device(ttnn_prefix_clone_18, )
  ttnn_to_layout_77 = ttnn.to_layout(ttnn_from_device_77, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_40 = ttnn.reshape(ttnn_to_layout_77, (196, 3072), )
  ttnn_from_torch_59 = ttnn.from_torch(arg60_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_30 = ttnn.transpose(ttnn_from_torch_59, 0, 1, )
  ttnn_from_device_78 = ttnn.from_device(ttnn_reshape_40, )
  ttnn_to_layout_78 = ttnn.to_layout(ttnn_from_device_78, ttnn.TILE_LAYOUT, )
  ttnn_to_device_39 = ttnn.to_device(ttnn_to_layout_78, device = device)
  ttnn_matmul_19 = ttnn.matmul(ttnn_to_device_39, ttnn_transpose_30, )
  ttnn_from_torch_60 = ttnn.from_torch(arg61_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_14 = ttnn.add(ttnn_from_torch_60, ttnn_matmul_19, )
  ttnn_from_device_79 = ttnn.from_device(ttnn_add_14, )
  ttnn_to_layout_79 = ttnn.to_layout(ttnn_from_device_79, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_41 = ttnn.reshape(ttnn_to_layout_79, (1, 196, 768), )
  ttnn_from_device_80 = ttnn.from_device(ttnn_reshape_41, )
  ttnn_to_layout_80 = ttnn.to_layout(ttnn_from_device_80, ttnn.TILE_LAYOUT, )
  ttnn_to_device_40 = ttnn.to_device(ttnn_to_layout_80, device = device)
  ttnn_prefix_clone_19 = clone_wrapper(ttnn_to_device_40, )
  ttnn_add_51 = ttnn.add(ttnn_add_50, ttnn_prefix_clone_19, )
  ttnn_from_torch_61 = ttnn.from_torch(arg62_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_62 = ttnn.from_torch(arg63_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_10_ = ttnn.layer_norm(ttnn_add_51, epsilon = 1e-06, weight = ttnn_from_torch_61, bias = ttnn_from_torch_62)
  ttnn_layer_norm_10_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_add_51), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_61), 
                                                                  ttnn.to_torch(ttnn_from_torch_62), 1e-06, )[0]
  ttnn_layer_norm_10 = ttnn.from_torch(ttnn_layer_norm_10_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_10_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_10_), ttnn_layer_norm_10))
    # Pocetak koda za proveru
  print(f"mixer_ln10_input: {ttnn_add_51}")
  print(f"mixer_ln10_weight: {ttnn_from_torch_61}")
  print(f"mixer_ln10_bias: {ttnn_from_torch_62}")
  def save_tensor_to_csv(tensor, filename):
    import pandas as pd
    tensor = tensor.contiguous()
    if tensor.dtype == torch.bfloat16:
        tensor = tensor.to(torch.float32)
    if tensor.ndim == 0:  # Scalar
        df = pd.DataFrame([tensor.item()])
    elif tensor.ndim == 1:  # 1D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 2:  # 2D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 3:  # 3D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    elif tensor.ndim == 4:  # 4D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    else:
        raise ValueError("Unsupported tensor dimension")
    df.to_csv(filename, index=False)
  def load_tensor_from_csv(filename, shape):
    import pandas as pd
    df = pd.read_csv(filename)
    data = df.values
    tensor = torch.tensor(data)
    # Reshape the tensor to the original shape
    tensor = tensor.view(shape)
    return tensor
  x_1 = ttnn.to_torch(ttnn_add_51)
  x_2 = ttnn.to_torch(ttnn_from_torch_61)
  x_3 = ttnn.to_torch(ttnn_from_torch_62)
  x1_shape = x_1.shape
  x2_shape = x_2.shape
  x3_shape = x_3.shape
  save_tensor_to_csv(x_1, "mixer_ln10_input.csv")
  save_tensor_to_csv(x_2, "mixer_ln10_weight.csv")
  save_tensor_to_csv(x_3, "mixer_ln10_bias.csv")
  load_1 = load_tensor_from_csv("mixer_ln10_input.csv", x1_shape)
  load_2 = load_tensor_from_csv("mixer_ln10_weight.csv", x2_shape)
  load_3 = load_tensor_from_csv("mixer_ln10_bias.csv", x3_shape)
  test_accuracy(x_1, load_1)
  test_accuracy(x_2, load_2)
  test_accuracy(x_3, load_3)
  # Kraj koda za proveru
  test_accuracy(native_layer_norm_10[0], ttnn_layer_norm_10)
  ttnn_transpose_31 = ttnn.transpose(ttnn_layer_norm_10, 1, 2, )
  ttnn_from_torch_63 = ttnn.from_torch(arg64_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_32 = ttnn.transpose(ttnn_from_torch_63, 0, 1, )
  ttnn_from_device_81 = ttnn.from_device(ttnn_transpose_31, )
  ttnn_to_layout_81 = ttnn.to_layout(ttnn_from_device_81, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_42 = ttnn.reshape(ttnn_to_layout_81, (768, 196), )
  ttnn_from_device_82 = ttnn.from_device(ttnn_reshape_42, )
  ttnn_to_layout_82 = ttnn.to_layout(ttnn_from_device_82, ttnn.TILE_LAYOUT, )
  ttnn_to_device_41 = ttnn.to_device(ttnn_to_layout_82, device = device)
  ttnn_matmul_20 = ttnn.matmul(ttnn_to_device_41, ttnn_transpose_32, )
  ttnn_from_device_83 = ttnn.from_device(ttnn_matmul_20, )
  ttnn_to_layout_83 = ttnn.to_layout(ttnn_from_device_83, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_43 = ttnn.reshape(ttnn_to_layout_83, (1, 768, 384), )
  ttnn_from_device_84 = ttnn.from_device(ttnn_reshape_43, )
  ttnn_to_layout_84 = ttnn.to_layout(ttnn_from_device_84, ttnn.TILE_LAYOUT, )
  ttnn_to_device_42 = ttnn.to_device(ttnn_to_layout_84, device = device)
  ttnn_from_torch_64 = ttnn.from_torch(arg65_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_52 = ttnn.add(ttnn_to_device_42, ttnn_from_torch_64, )
  ttnn_gelu_10 = ttnn.gelu(ttnn_add_52, )
  ttnn_prefix_clone_20 = clone_wrapper(ttnn_gelu_10, )
  ttnn_from_device_85 = ttnn.from_device(ttnn_prefix_clone_20, )
  ttnn_to_layout_85 = ttnn.to_layout(ttnn_from_device_85, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_44 = ttnn.reshape(ttnn_to_layout_85, (768, 384), )
  ttnn_from_torch_65 = ttnn.from_torch(arg66_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_33 = ttnn.transpose(ttnn_from_torch_65, 0, 1, )
  ttnn_from_device_86 = ttnn.from_device(ttnn_reshape_44, )
  ttnn_to_layout_86 = ttnn.to_layout(ttnn_from_device_86, ttnn.TILE_LAYOUT, )
  ttnn_to_device_43 = ttnn.to_device(ttnn_to_layout_86, device = device)
  ttnn_matmul_21 = ttnn.matmul(ttnn_to_device_43, ttnn_transpose_33, )
  ttnn_from_torch_66 = ttnn.from_torch(arg67_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_15 = ttnn.add(ttnn_from_torch_66, ttnn_matmul_21, )
  ttnn_from_device_87 = ttnn.from_device(ttnn_add_15, )
  ttnn_to_layout_87 = ttnn.to_layout(ttnn_from_device_87, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_45 = ttnn.reshape(ttnn_to_layout_87, (1, 768, 196), )
  ttnn_from_device_88 = ttnn.from_device(ttnn_reshape_45, )
  ttnn_to_layout_88 = ttnn.to_layout(ttnn_from_device_88, ttnn.TILE_LAYOUT, )
  ttnn_to_device_44 = ttnn.to_device(ttnn_to_layout_88, device = device)
  ttnn_prefix_clone_21 = clone_wrapper(ttnn_to_device_44, )
  ttnn_transpose_34 = ttnn.transpose(ttnn_prefix_clone_21, 1, 2, )
  ttnn_add_53 = ttnn.add(ttnn_add_51, ttnn_transpose_34, )
  ttnn_from_torch_67 = ttnn.from_torch(arg68_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_68 = ttnn.from_torch(arg69_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_11_ = ttnn.layer_norm(ttnn_add_53, epsilon = 1e-06, weight = ttnn_from_torch_67, bias = ttnn_from_torch_68)
  ttnn_layer_norm_11_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_add_53), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_67), 
                                                                  ttnn.to_torch(ttnn_from_torch_68), 1e-06, )[0]
  ttnn_layer_norm_11 = ttnn.from_torch(ttnn_layer_norm_11_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_11_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_11_), ttnn_layer_norm_11))
    # Pocetak koda za proveru
  print(f"mixer_ln11_input: {ttnn_add_53}")
  print(f"mixer_ln11_weight: {ttnn_from_torch_67}")
  print(f"mixer_ln11_bias: {ttnn_from_torch_68}")
  def save_tensor_to_csv(tensor, filename):
    import pandas as pd
    tensor = tensor.contiguous()
    if tensor.dtype == torch.bfloat16:
        tensor = tensor.to(torch.float32)
    if tensor.ndim == 0:  # Scalar
        df = pd.DataFrame([tensor.item()])
    elif tensor.ndim == 1:  # 1D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 2:  # 2D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 3:  # 3D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    elif tensor.ndim == 4:  # 4D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    else:
        raise ValueError("Unsupported tensor dimension")
    df.to_csv(filename, index=False)
  def load_tensor_from_csv(filename, shape):
    import pandas as pd
    df = pd.read_csv(filename)
    data = df.values
    tensor = torch.tensor(data)
    # Reshape the tensor to the original shape
    tensor = tensor.view(shape)
    return tensor
  x_1 = ttnn.to_torch(ttnn_add_53)
  x_2 = ttnn.to_torch(ttnn_from_torch_67)
  x_3 = ttnn.to_torch(ttnn_from_torch_68)
  x1_shape = x_1.shape
  x2_shape = x_2.shape
  x3_shape = x_3.shape
  save_tensor_to_csv(x_1, "mixer_ln11_input.csv")
  save_tensor_to_csv(x_2, "mixer_ln11_weight.csv")
  save_tensor_to_csv(x_3, "mixer_ln11_bias.csv")
  load_1 = load_tensor_from_csv("mixer_ln11_input.csv", x1_shape)
  load_2 = load_tensor_from_csv("mixer_ln11_weight.csv", x2_shape)
  load_3 = load_tensor_from_csv("mixer_ln11_bias.csv", x3_shape)
  test_accuracy(x_1, load_1)
  test_accuracy(x_2, load_2)
  test_accuracy(x_3, load_3)
  # Kraj koda za proveru
  test_accuracy(native_layer_norm_11[0], ttnn_layer_norm_11)
  ttnn_from_device_89 = ttnn.from_device(ttnn_layer_norm_11, )
  ttnn_to_layout_89 = ttnn.to_layout(ttnn_from_device_89, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_46 = ttnn.reshape(ttnn_to_layout_89, (196, 768), )
  ttnn_from_torch_69 = ttnn.from_torch(arg70_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_35 = ttnn.transpose(ttnn_from_torch_69, 0, 1, )
  ttnn_from_device_90 = ttnn.from_device(ttnn_reshape_46, )
  ttnn_to_layout_90 = ttnn.to_layout(ttnn_from_device_90, ttnn.TILE_LAYOUT, )
  ttnn_to_device_45 = ttnn.to_device(ttnn_to_layout_90, device = device)
  ttnn_matmul_22 = ttnn.matmul(ttnn_to_device_45, ttnn_transpose_35, )
  ttnn_from_torch_70 = ttnn.from_torch(arg71_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_16 = ttnn.add(ttnn_from_torch_70, ttnn_matmul_22, )
  ttnn_from_device_91 = ttnn.from_device(ttnn_add_16, )
  ttnn_to_layout_91 = ttnn.to_layout(ttnn_from_device_91, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_47 = ttnn.reshape(ttnn_to_layout_91, (1, 196, 3072), )
  ttnn_from_device_92 = ttnn.from_device(ttnn_reshape_47, )
  ttnn_to_layout_92 = ttnn.to_layout(ttnn_from_device_92, ttnn.TILE_LAYOUT, )
  ttnn_to_device_46 = ttnn.to_device(ttnn_to_layout_92, device = device)
  ttnn_gelu_11 = ttnn.gelu(ttnn_to_device_46, )
  ttnn_prefix_clone_22 = clone_wrapper(ttnn_gelu_11, )
  ttnn_from_device_93 = ttnn.from_device(ttnn_prefix_clone_22, )
  ttnn_to_layout_93 = ttnn.to_layout(ttnn_from_device_93, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_48 = ttnn.reshape(ttnn_to_layout_93, (196, 3072), )
  ttnn_from_torch_71 = ttnn.from_torch(arg72_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_36 = ttnn.transpose(ttnn_from_torch_71, 0, 1, )
  ttnn_from_device_94 = ttnn.from_device(ttnn_reshape_48, )
  ttnn_to_layout_94 = ttnn.to_layout(ttnn_from_device_94, ttnn.TILE_LAYOUT, )
  ttnn_to_device_47 = ttnn.to_device(ttnn_to_layout_94, device = device)
  ttnn_matmul_23 = ttnn.matmul(ttnn_to_device_47, ttnn_transpose_36, )
  ttnn_from_torch_72 = ttnn.from_torch(arg73_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_17 = ttnn.add(ttnn_from_torch_72, ttnn_matmul_23, )
  ttnn_from_device_95 = ttnn.from_device(ttnn_add_17, )
  ttnn_to_layout_95 = ttnn.to_layout(ttnn_from_device_95, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_49 = ttnn.reshape(ttnn_to_layout_95, (1, 196, 768), )
  ttnn_from_device_96 = ttnn.from_device(ttnn_reshape_49, )
  ttnn_to_layout_96 = ttnn.to_layout(ttnn_from_device_96, ttnn.TILE_LAYOUT, )
  ttnn_to_device_48 = ttnn.to_device(ttnn_to_layout_96, device = device)
  ttnn_prefix_clone_23 = clone_wrapper(ttnn_to_device_48, )
  ttnn_add_54 = ttnn.add(ttnn_add_53, ttnn_prefix_clone_23, )
  ttnn_from_torch_73 = ttnn.from_torch(arg74_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_74 = ttnn.from_torch(arg75_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_12_ = ttnn.layer_norm(ttnn_add_54, epsilon = 1e-06, weight = ttnn_from_torch_73, bias = ttnn_from_torch_74)
  ttnn_layer_norm_12_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_add_54), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_73), 
                                                                  ttnn.to_torch(ttnn_from_torch_74), 1e-06, )[0]
  ttnn_layer_norm_12 = ttnn.from_torch(ttnn_layer_norm_12_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_12_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_12_), ttnn_layer_norm_12))
    # Pocetak koda za proveru
  print(f"mixer_ln12_input: {ttnn_add_54}")
  print(f"mixer_ln12_weight: {ttnn_from_torch_73}")
  print(f"mixer_ln12_bias: {ttnn_from_torch_74}")
  def save_tensor_to_csv(tensor, filename):
    import pandas as pd
    tensor = tensor.contiguous()
    if tensor.dtype == torch.bfloat16:
        tensor = tensor.to(torch.float32)
    if tensor.ndim == 0:  # Scalar
        df = pd.DataFrame([tensor.item()])
    elif tensor.ndim == 1:  # 1D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 2:  # 2D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 3:  # 3D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    elif tensor.ndim == 4:  # 4D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    else:
        raise ValueError("Unsupported tensor dimension")
    df.to_csv(filename, index=False)
  def load_tensor_from_csv(filename, shape):
    import pandas as pd
    df = pd.read_csv(filename)
    data = df.values
    tensor = torch.tensor(data)
    # Reshape the tensor to the original shape
    tensor = tensor.view(shape)
    return tensor
  x_1 = ttnn.to_torch(ttnn_add_54)
  x_2 = ttnn.to_torch(ttnn_from_torch_73)
  x_3 = ttnn.to_torch(ttnn_from_torch_74)
  x1_shape = x_1.shape
  x2_shape = x_2.shape
  x3_shape = x_3.shape
  save_tensor_to_csv(x_1, "mixer_ln12_input.csv")
  save_tensor_to_csv(x_2, "mixer_ln12_weight.csv")
  save_tensor_to_csv(x_3, "mixer_ln12_bias.csv")
  load_1 = load_tensor_from_csv("mixer_ln12_input.csv", x1_shape)
  load_2 = load_tensor_from_csv("mixer_ln12_weight.csv", x2_shape)
  load_3 = load_tensor_from_csv("mixer_ln12_bias.csv", x3_shape)
  test_accuracy(x_1, load_1)
  test_accuracy(x_2, load_2)
  test_accuracy(x_3, load_3)
  # Kraj koda za proveru
  test_accuracy(native_layer_norm_12[0], ttnn_layer_norm_12)
  ttnn_transpose_37 = ttnn.transpose(ttnn_layer_norm_12, 1, 2, )
  ttnn_from_torch_75 = ttnn.from_torch(arg76_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_38 = ttnn.transpose(ttnn_from_torch_75, 0, 1, )
  ttnn_from_device_97 = ttnn.from_device(ttnn_transpose_37, )
  ttnn_to_layout_97 = ttnn.to_layout(ttnn_from_device_97, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_50 = ttnn.reshape(ttnn_to_layout_97, (768, 196), )
  ttnn_from_device_98 = ttnn.from_device(ttnn_reshape_50, )
  ttnn_to_layout_98 = ttnn.to_layout(ttnn_from_device_98, ttnn.TILE_LAYOUT, )
  ttnn_to_device_49 = ttnn.to_device(ttnn_to_layout_98, device = device)
  ttnn_matmul_24 = ttnn.matmul(ttnn_to_device_49, ttnn_transpose_38, )
  ttnn_from_device_99 = ttnn.from_device(ttnn_matmul_24, )
  ttnn_to_layout_99 = ttnn.to_layout(ttnn_from_device_99, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_51 = ttnn.reshape(ttnn_to_layout_99, (1, 768, 384), )
  ttnn_from_device_100 = ttnn.from_device(ttnn_reshape_51, )
  ttnn_to_layout_100 = ttnn.to_layout(ttnn_from_device_100, ttnn.TILE_LAYOUT, )
  ttnn_to_device_50 = ttnn.to_device(ttnn_to_layout_100, device = device)
  ttnn_from_torch_76 = ttnn.from_torch(arg77_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_55 = ttnn.add(ttnn_to_device_50, ttnn_from_torch_76, )
  ttnn_gelu_12 = ttnn.gelu(ttnn_add_55, )
  ttnn_prefix_clone_24 = clone_wrapper(ttnn_gelu_12, )
  ttnn_from_device_101 = ttnn.from_device(ttnn_prefix_clone_24, )
  ttnn_to_layout_101 = ttnn.to_layout(ttnn_from_device_101, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_52 = ttnn.reshape(ttnn_to_layout_101, (768, 384), )
  ttnn_from_torch_77 = ttnn.from_torch(arg78_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_39 = ttnn.transpose(ttnn_from_torch_77, 0, 1, )
  ttnn_from_device_102 = ttnn.from_device(ttnn_reshape_52, )
  ttnn_to_layout_102 = ttnn.to_layout(ttnn_from_device_102, ttnn.TILE_LAYOUT, )
  ttnn_to_device_51 = ttnn.to_device(ttnn_to_layout_102, device = device)
  ttnn_matmul_25 = ttnn.matmul(ttnn_to_device_51, ttnn_transpose_39, )
  ttnn_from_torch_78 = ttnn.from_torch(arg79_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_18 = ttnn.add(ttnn_from_torch_78, ttnn_matmul_25, )
  ttnn_from_device_103 = ttnn.from_device(ttnn_add_18, )
  ttnn_to_layout_103 = ttnn.to_layout(ttnn_from_device_103, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_53 = ttnn.reshape(ttnn_to_layout_103, (1, 768, 196), )
  ttnn_from_device_104 = ttnn.from_device(ttnn_reshape_53, )
  ttnn_to_layout_104 = ttnn.to_layout(ttnn_from_device_104, ttnn.TILE_LAYOUT, )
  ttnn_to_device_52 = ttnn.to_device(ttnn_to_layout_104, device = device)
  ttnn_prefix_clone_25 = clone_wrapper(ttnn_to_device_52, )
  ttnn_transpose_40 = ttnn.transpose(ttnn_prefix_clone_25, 1, 2, )
  ttnn_add_56 = ttnn.add(ttnn_add_54, ttnn_transpose_40, )
  ttnn_from_torch_79 = ttnn.from_torch(arg80_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_80 = ttnn.from_torch(arg81_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_13_ = ttnn.layer_norm(ttnn_add_56, epsilon = 1e-06, weight = ttnn_from_torch_79, bias = ttnn_from_torch_80)
  ttnn_layer_norm_13_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_add_56), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_79), 
                                                                  ttnn.to_torch(ttnn_from_torch_80), 1e-06, )[0]
  ttnn_layer_norm_13 = ttnn.from_torch(ttnn_layer_norm_13_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_13_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_13_), ttnn_layer_norm_13))
    # Pocetak koda za proveru
  print(f"mixer_ln13_input: {ttnn_add_56}")
  print(f"mixer_ln13_weight: {ttnn_from_torch_79}")
  print(f"mixer_ln13_bias: {ttnn_from_torch_80}")
  def save_tensor_to_csv(tensor, filename):
    import pandas as pd
    tensor = tensor.contiguous()
    if tensor.dtype == torch.bfloat16:
        tensor = tensor.to(torch.float32)
    if tensor.ndim == 0:  # Scalar
        df = pd.DataFrame([tensor.item()])
    elif tensor.ndim == 1:  # 1D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 2:  # 2D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 3:  # 3D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    elif tensor.ndim == 4:  # 4D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    else:
        raise ValueError("Unsupported tensor dimension")
    df.to_csv(filename, index=False)
  def load_tensor_from_csv(filename, shape):
    import pandas as pd
    df = pd.read_csv(filename)
    data = df.values
    tensor = torch.tensor(data)
    # Reshape the tensor to the original shape
    tensor = tensor.view(shape)
    return tensor
  x_1 = ttnn.to_torch(ttnn_add_56)
  x_2 = ttnn.to_torch(ttnn_from_torch_79)
  x_3 = ttnn.to_torch(ttnn_from_torch_80)
  x1_shape = x_1.shape
  x2_shape = x_2.shape
  x3_shape = x_3.shape
  save_tensor_to_csv(x_1, "mixer_ln13_input.csv")
  save_tensor_to_csv(x_2, "mixer_ln13_weight.csv")
  save_tensor_to_csv(x_3, "mixer_ln13_bias.csv")
  load_1 = load_tensor_from_csv("mixer_ln13_input.csv", x1_shape)
  load_2 = load_tensor_from_csv("mixer_ln13_weight.csv", x2_shape)
  load_3 = load_tensor_from_csv("mixer_ln13_bias.csv", x3_shape)
  test_accuracy(x_1, load_1)
  test_accuracy(x_2, load_2)
  test_accuracy(x_3, load_3)
  # Kraj koda za proveru
  test_accuracy(native_layer_norm_13[0], ttnn_layer_norm_13)
  ttnn_from_device_105 = ttnn.from_device(ttnn_layer_norm_13, )
  ttnn_to_layout_105 = ttnn.to_layout(ttnn_from_device_105, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_54 = ttnn.reshape(ttnn_to_layout_105, (196, 768), )
  ttnn_from_torch_81 = ttnn.from_torch(arg82_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_41 = ttnn.transpose(ttnn_from_torch_81, 0, 1, )
  ttnn_from_device_106 = ttnn.from_device(ttnn_reshape_54, )
  ttnn_to_layout_106 = ttnn.to_layout(ttnn_from_device_106, ttnn.TILE_LAYOUT, )
  ttnn_to_device_53 = ttnn.to_device(ttnn_to_layout_106, device = device)
  ttnn_matmul_26 = ttnn.matmul(ttnn_to_device_53, ttnn_transpose_41, )
  ttnn_from_torch_82 = ttnn.from_torch(arg83_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_19 = ttnn.add(ttnn_from_torch_82, ttnn_matmul_26, )
  ttnn_from_device_107 = ttnn.from_device(ttnn_add_19, )
  ttnn_to_layout_107 = ttnn.to_layout(ttnn_from_device_107, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_55 = ttnn.reshape(ttnn_to_layout_107, (1, 196, 3072), )
  ttnn_from_device_108 = ttnn.from_device(ttnn_reshape_55, )
  ttnn_to_layout_108 = ttnn.to_layout(ttnn_from_device_108, ttnn.TILE_LAYOUT, )
  ttnn_to_device_54 = ttnn.to_device(ttnn_to_layout_108, device = device)
  ttnn_gelu_13 = ttnn.gelu(ttnn_to_device_54, )
  ttnn_prefix_clone_26 = clone_wrapper(ttnn_gelu_13, )
  ttnn_from_device_109 = ttnn.from_device(ttnn_prefix_clone_26, )
  ttnn_to_layout_109 = ttnn.to_layout(ttnn_from_device_109, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_56 = ttnn.reshape(ttnn_to_layout_109, (196, 3072), )
  ttnn_from_torch_83 = ttnn.from_torch(arg84_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_42 = ttnn.transpose(ttnn_from_torch_83, 0, 1, )
  ttnn_from_device_110 = ttnn.from_device(ttnn_reshape_56, )
  ttnn_to_layout_110 = ttnn.to_layout(ttnn_from_device_110, ttnn.TILE_LAYOUT, )
  ttnn_to_device_55 = ttnn.to_device(ttnn_to_layout_110, device = device)
  ttnn_matmul_27 = ttnn.matmul(ttnn_to_device_55, ttnn_transpose_42, )
  ttnn_from_torch_84 = ttnn.from_torch(arg85_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_20 = ttnn.add(ttnn_from_torch_84, ttnn_matmul_27, )
  ttnn_from_device_111 = ttnn.from_device(ttnn_add_20, )
  ttnn_to_layout_111 = ttnn.to_layout(ttnn_from_device_111, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_57 = ttnn.reshape(ttnn_to_layout_111, (1, 196, 768), )
  ttnn_from_device_112 = ttnn.from_device(ttnn_reshape_57, )
  ttnn_to_layout_112 = ttnn.to_layout(ttnn_from_device_112, ttnn.TILE_LAYOUT, )
  ttnn_to_device_56 = ttnn.to_device(ttnn_to_layout_112, device = device)
  ttnn_prefix_clone_27 = clone_wrapper(ttnn_to_device_56, )
  ttnn_add_57 = ttnn.add(ttnn_add_56, ttnn_prefix_clone_27, )
  ttnn_from_torch_85 = ttnn.from_torch(arg86_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_86 = ttnn.from_torch(arg87_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_14_ = ttnn.layer_norm(ttnn_add_57, epsilon = 1e-06, weight = ttnn_from_torch_85, bias = ttnn_from_torch_86)
  ttnn_layer_norm_14_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_add_57), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_85), 
                                                                  ttnn.to_torch(ttnn_from_torch_86), 1e-06, )[0]
  ttnn_layer_norm_14 = ttnn.from_torch(ttnn_layer_norm_14_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_14_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_14_), ttnn_layer_norm_14))
    # Pocetak koda za proveru
  print(f"mixer_ln14_input: {ttnn_add_57}")
  print(f"mixer_ln14_weight: {ttnn_from_torch_85}")
  print(f"mixer_ln14_bias: {ttnn_from_torch_86}")
  def save_tensor_to_csv(tensor, filename):
    import pandas as pd
    tensor = tensor.contiguous()
    if tensor.dtype == torch.bfloat16:
        tensor = tensor.to(torch.float32)
    if tensor.ndim == 0:  # Scalar
        df = pd.DataFrame([tensor.item()])
    elif tensor.ndim == 1:  # 1D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 2:  # 2D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 3:  # 3D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    elif tensor.ndim == 4:  # 4D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    else:
        raise ValueError("Unsupported tensor dimension")
    df.to_csv(filename, index=False)
  def load_tensor_from_csv(filename, shape):
    import pandas as pd
    df = pd.read_csv(filename)
    data = df.values
    tensor = torch.tensor(data)
    # Reshape the tensor to the original shape
    tensor = tensor.view(shape)
    return tensor
  x_1 = ttnn.to_torch(ttnn_add_57)
  x_2 = ttnn.to_torch(ttnn_from_torch_85)
  x_3 = ttnn.to_torch(ttnn_from_torch_86)
  x1_shape = x_1.shape
  x2_shape = x_2.shape
  x3_shape = x_3.shape
  save_tensor_to_csv(x_1, "mixer_ln14_input.csv")
  save_tensor_to_csv(x_2, "mixer_ln14_weight.csv")
  save_tensor_to_csv(x_3, "mixer_ln14_bias.csv")
  load_1 = load_tensor_from_csv("mixer_ln14_input.csv", x1_shape)
  load_2 = load_tensor_from_csv("mixer_ln14_weight.csv", x2_shape)
  load_3 = load_tensor_from_csv("mixer_ln14_bias.csv", x3_shape)
  test_accuracy(x_1, load_1)
  test_accuracy(x_2, load_2)
  test_accuracy(x_3, load_3)
  test_accuracy(native_layer_norm_14[0], ttnn_layer_norm_14)
  ttnn_transpose_43 = ttnn.transpose(ttnn_layer_norm_14, 1, 2, )
  ttnn_from_torch_87 = ttnn.from_torch(arg88_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_44 = ttnn.transpose(ttnn_from_torch_87, 0, 1, )
  ttnn_from_device_113 = ttnn.from_device(ttnn_transpose_43, )
  ttnn_to_layout_113 = ttnn.to_layout(ttnn_from_device_113, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_58 = ttnn.reshape(ttnn_to_layout_113, (768, 196), )
  ttnn_from_device_114 = ttnn.from_device(ttnn_reshape_58, )
  ttnn_to_layout_114 = ttnn.to_layout(ttnn_from_device_114, ttnn.TILE_LAYOUT, )
  ttnn_to_device_57 = ttnn.to_device(ttnn_to_layout_114, device = device)
  ttnn_matmul_28 = ttnn.matmul(ttnn_to_device_57, ttnn_transpose_44, )
  ttnn_from_device_115 = ttnn.from_device(ttnn_matmul_28, )
  ttnn_to_layout_115 = ttnn.to_layout(ttnn_from_device_115, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_59 = ttnn.reshape(ttnn_to_layout_115, (1, 768, 384), )
  ttnn_from_device_116 = ttnn.from_device(ttnn_reshape_59, )
  ttnn_to_layout_116 = ttnn.to_layout(ttnn_from_device_116, ttnn.TILE_LAYOUT, )
  ttnn_to_device_58 = ttnn.to_device(ttnn_to_layout_116, device = device)
  ttnn_from_torch_88 = ttnn.from_torch(arg89_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_58 = ttnn.add(ttnn_to_device_58, ttnn_from_torch_88, )
  ttnn_gelu_14 = ttnn.gelu(ttnn_add_58, )
  ttnn_prefix_clone_28 = clone_wrapper(ttnn_gelu_14, )
  ttnn_from_device_117 = ttnn.from_device(ttnn_prefix_clone_28, )
  ttnn_to_layout_117 = ttnn.to_layout(ttnn_from_device_117, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_60 = ttnn.reshape(ttnn_to_layout_117, (768, 384), )
  ttnn_from_torch_89 = ttnn.from_torch(arg90_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_45 = ttnn.transpose(ttnn_from_torch_89, 0, 1, )
  ttnn_from_device_118 = ttnn.from_device(ttnn_reshape_60, )
  ttnn_to_layout_118 = ttnn.to_layout(ttnn_from_device_118, ttnn.TILE_LAYOUT, )
  ttnn_to_device_59 = ttnn.to_device(ttnn_to_layout_118, device = device)
  ttnn_matmul_29 = ttnn.matmul(ttnn_to_device_59, ttnn_transpose_45, )
  ttnn_from_torch_90 = ttnn.from_torch(arg91_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_21 = ttnn.add(ttnn_from_torch_90, ttnn_matmul_29, )
  ttnn_from_device_119 = ttnn.from_device(ttnn_add_21, )
  ttnn_to_layout_119 = ttnn.to_layout(ttnn_from_device_119, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_61 = ttnn.reshape(ttnn_to_layout_119, (1, 768, 196), )
  ttnn_from_device_120 = ttnn.from_device(ttnn_reshape_61, )
  ttnn_to_layout_120 = ttnn.to_layout(ttnn_from_device_120, ttnn.TILE_LAYOUT, )
  ttnn_to_device_60 = ttnn.to_device(ttnn_to_layout_120, device = device)
  ttnn_prefix_clone_29 = clone_wrapper(ttnn_to_device_60, )
  ttnn_transpose_46 = ttnn.transpose(ttnn_prefix_clone_29, 1, 2, )
  ttnn_add_59 = ttnn.add(ttnn_add_57, ttnn_transpose_46, )
  ttnn_from_torch_91 = ttnn.from_torch(arg92_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_92 = ttnn.from_torch(arg93_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_15_ = ttnn.layer_norm(ttnn_add_59, epsilon = 1e-06, weight = ttnn_from_torch_91, bias = ttnn_from_torch_92)
  ttnn_layer_norm_15_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_add_59), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_91), 
                                                                  ttnn.to_torch(ttnn_from_torch_92), 1e-06, )[0]
  ttnn_layer_norm_15 = ttnn.from_torch(ttnn_layer_norm_15_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_15_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_15_), ttnn_layer_norm_15))
    # Pocetak koda za proveru
  print(f"mixer_ln15_input: {ttnn_add_59}")
  print(f"mixer_ln15_weight: {ttnn_from_torch_91}")
  print(f"mixer_ln15_bias: {ttnn_from_torch_92}")
  def save_tensor_to_csv(tensor, filename):
    import pandas as pd
    tensor = tensor.contiguous()
    if tensor.dtype == torch.bfloat16:
        tensor = tensor.to(torch.float32)
    if tensor.ndim == 0:  # Scalar
        df = pd.DataFrame([tensor.item()])
    elif tensor.ndim == 1:  # 1D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 2:  # 2D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 3:  # 3D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    elif tensor.ndim == 4:  # 4D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    else:
        raise ValueError("Unsupported tensor dimension")
    df.to_csv(filename, index=False)
  def load_tensor_from_csv(filename, shape):
    import pandas as pd
    df = pd.read_csv(filename)
    data = df.values
    tensor = torch.tensor(data)
    # Reshape the tensor to the original shape
    tensor = tensor.view(shape)
    return tensor
  x_1 = ttnn.to_torch(ttnn_add_59)
  x_2 = ttnn.to_torch(ttnn_from_torch_91)
  x_3 = ttnn.to_torch(ttnn_from_torch_92)
  x1_shape = x_1.shape
  x2_shape = x_2.shape
  x3_shape = x_3.shape
  save_tensor_to_csv(x_1, "mixer_ln15_input.csv")
  save_tensor_to_csv(x_2, "mixer_ln15_weight.csv")
  save_tensor_to_csv(x_3, "mixer_ln15_bias.csv")
  load_1 = load_tensor_from_csv("mixer_ln15_input.csv", x1_shape)
  load_2 = load_tensor_from_csv("mixer_ln15_weight.csv", x2_shape)
  load_3 = load_tensor_from_csv("mixer_ln15_bias.csv", x3_shape)
  test_accuracy(x_1, load_1)
  test_accuracy(x_2, load_2)
  test_accuracy(x_3, load_3)
  test_accuracy(native_layer_norm_15[0], ttnn_layer_norm_15)
  ttnn_from_device_121 = ttnn.from_device(ttnn_layer_norm_15, )
  ttnn_to_layout_121 = ttnn.to_layout(ttnn_from_device_121, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_62 = ttnn.reshape(ttnn_to_layout_121, (196, 768), )
  ttnn_from_torch_93 = ttnn.from_torch(arg94_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_47 = ttnn.transpose(ttnn_from_torch_93, 0, 1, )
  ttnn_from_device_122 = ttnn.from_device(ttnn_reshape_62, )
  ttnn_to_layout_122 = ttnn.to_layout(ttnn_from_device_122, ttnn.TILE_LAYOUT, )
  ttnn_to_device_61 = ttnn.to_device(ttnn_to_layout_122, device = device)
  ttnn_matmul_30 = ttnn.matmul(ttnn_to_device_61, ttnn_transpose_47, )
  ttnn_from_torch_94 = ttnn.from_torch(arg95_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_22 = ttnn.add(ttnn_from_torch_94, ttnn_matmul_30, )
  ttnn_from_device_123 = ttnn.from_device(ttnn_add_22, )
  ttnn_to_layout_123 = ttnn.to_layout(ttnn_from_device_123, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_63 = ttnn.reshape(ttnn_to_layout_123, (1, 196, 3072), )
  ttnn_from_device_124 = ttnn.from_device(ttnn_reshape_63, )
  ttnn_to_layout_124 = ttnn.to_layout(ttnn_from_device_124, ttnn.TILE_LAYOUT, )
  ttnn_to_device_62 = ttnn.to_device(ttnn_to_layout_124, device = device)
  ttnn_gelu_15 = ttnn.gelu(ttnn_to_device_62, )
  ttnn_prefix_clone_30 = clone_wrapper(ttnn_gelu_15, )
  ttnn_from_device_125 = ttnn.from_device(ttnn_prefix_clone_30, )
  ttnn_to_layout_125 = ttnn.to_layout(ttnn_from_device_125, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_64 = ttnn.reshape(ttnn_to_layout_125, (196, 3072), )
  ttnn_from_torch_95 = ttnn.from_torch(arg96_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_48 = ttnn.transpose(ttnn_from_torch_95, 0, 1, )
  ttnn_from_device_126 = ttnn.from_device(ttnn_reshape_64, )
  ttnn_to_layout_126 = ttnn.to_layout(ttnn_from_device_126, ttnn.TILE_LAYOUT, )
  ttnn_to_device_63 = ttnn.to_device(ttnn_to_layout_126, device = device)
  ttnn_matmul_31 = ttnn.matmul(ttnn_to_device_63, ttnn_transpose_48, )
  ttnn_from_torch_96 = ttnn.from_torch(arg97_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_23 = ttnn.add(ttnn_from_torch_96, ttnn_matmul_31, )
  ttnn_from_device_127 = ttnn.from_device(ttnn_add_23, )
  ttnn_to_layout_127 = ttnn.to_layout(ttnn_from_device_127, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_65 = ttnn.reshape(ttnn_to_layout_127, (1, 196, 768), )
  ttnn_from_device_128 = ttnn.from_device(ttnn_reshape_65, )
  ttnn_to_layout_128 = ttnn.to_layout(ttnn_from_device_128, ttnn.TILE_LAYOUT, )
  ttnn_to_device_64 = ttnn.to_device(ttnn_to_layout_128, device = device)
  ttnn_prefix_clone_31 = clone_wrapper(ttnn_to_device_64, )
  ttnn_add_60 = ttnn.add(ttnn_add_59, ttnn_prefix_clone_31, )
  ttnn_from_torch_97 = ttnn.from_torch(arg98_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_98 = ttnn.from_torch(arg99_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_16_ = ttnn.layer_norm(ttnn_add_60, epsilon = 1e-06, weight = ttnn_from_torch_97, bias = ttnn_from_torch_98)
  ttnn_layer_norm_16_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_add_60), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_97), 
                                                                  ttnn.to_torch(ttnn_from_torch_98), 1e-06, )[0]
  ttnn_layer_norm_16 = ttnn.from_torch(ttnn_layer_norm_16_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_16_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_16_), ttnn_layer_norm_16))
    # Pocetak koda za proveru
  print(f"mixer_ln16_input: {ttnn_add_60}")
  print(f"mixer_ln16_weight: {ttnn_from_torch_97}")
  print(f"mixer_ln16_bias: {ttnn_from_torch_98}")
  def save_tensor_to_csv(tensor, filename):
    import pandas as pd
    tensor = tensor.contiguous()
    if tensor.dtype == torch.bfloat16:
        tensor = tensor.to(torch.float32)
    if tensor.ndim == 0:  # Scalar
        df = pd.DataFrame([tensor.item()])
    elif tensor.ndim == 1:  # 1D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 2:  # 2D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 3:  # 3D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    elif tensor.ndim == 4:  # 4D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    else:
        raise ValueError("Unsupported tensor dimension")
    df.to_csv(filename, index=False)
  def load_tensor_from_csv(filename, shape):
    import pandas as pd
    df = pd.read_csv(filename)
    data = df.values
    tensor = torch.tensor(data)
    # Reshape the tensor to the original shape
    tensor = tensor.view(shape)
    return tensor

  x_1 = ttnn.to_torch(ttnn_add_60)
  x_2 = ttnn.to_torch(ttnn_from_torch_97)
  x_3 = ttnn.to_torch(ttnn_from_torch_98)
  x1_shape = x_1.shape
  x2_shape = x_2.shape
  x3_shape = x_3.shape
  save_tensor_to_csv(x_1, "mixer_ln16_input.csv")
  save_tensor_to_csv(x_2, "mixer_ln16_weight.csv")
  save_tensor_to_csv(x_3, "mixer_ln16_bias.csv")
  load_1 = load_tensor_from_csv("mixer_ln16_input.csv", x1_shape)
  load_2 = load_tensor_from_csv("mixer_ln16_weight.csv", x2_shape)
  load_3 = load_tensor_from_csv("mixer_ln16_bias.csv", x3_shape)
  test_accuracy(x_1, load_1)
  test_accuracy(x_2, load_2)
  test_accuracy(x_3, load_3)
  # Kraj koda za proveru
  test_accuracy(native_layer_norm_16[0], ttnn_layer_norm_16)
  ttnn_transpose_49 = ttnn.transpose(ttnn_layer_norm_16, 1, 2, )
  ttnn_from_torch_99 = ttnn.from_torch(arg100_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_50 = ttnn.transpose(ttnn_from_torch_99, 0, 1, )
  ttnn_from_device_129 = ttnn.from_device(ttnn_transpose_49, )
  ttnn_to_layout_129 = ttnn.to_layout(ttnn_from_device_129, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_66 = ttnn.reshape(ttnn_to_layout_129, (768, 196), )
  ttnn_from_device_130 = ttnn.from_device(ttnn_reshape_66, )
  ttnn_to_layout_130 = ttnn.to_layout(ttnn_from_device_130, ttnn.TILE_LAYOUT, )
  ttnn_to_device_65 = ttnn.to_device(ttnn_to_layout_130, device = device)
  ttnn_matmul_32 = ttnn.matmul(ttnn_to_device_65, ttnn_transpose_50, )
  ttnn_from_device_131 = ttnn.from_device(ttnn_matmul_32, )
  ttnn_to_layout_131 = ttnn.to_layout(ttnn_from_device_131, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_67 = ttnn.reshape(ttnn_to_layout_131, (1, 768, 384), )
  ttnn_from_device_132 = ttnn.from_device(ttnn_reshape_67, )
  ttnn_to_layout_132 = ttnn.to_layout(ttnn_from_device_132, ttnn.TILE_LAYOUT, )
  ttnn_to_device_66 = ttnn.to_device(ttnn_to_layout_132, device = device)
  ttnn_from_torch_100 = ttnn.from_torch(arg101_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_61 = ttnn.add(ttnn_to_device_66, ttnn_from_torch_100, )
  ttnn_gelu_16 = ttnn.gelu(ttnn_add_61, )
  ttnn_prefix_clone_32 = clone_wrapper(ttnn_gelu_16, )
  ttnn_from_device_133 = ttnn.from_device(ttnn_prefix_clone_32, )
  ttnn_to_layout_133 = ttnn.to_layout(ttnn_from_device_133, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_68 = ttnn.reshape(ttnn_to_layout_133, (768, 384), )
  ttnn_from_torch_101 = ttnn.from_torch(arg102_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_51 = ttnn.transpose(ttnn_from_torch_101, 0, 1, )
  ttnn_from_device_134 = ttnn.from_device(ttnn_reshape_68, )
  ttnn_to_layout_134 = ttnn.to_layout(ttnn_from_device_134, ttnn.TILE_LAYOUT, )
  ttnn_to_device_67 = ttnn.to_device(ttnn_to_layout_134, device = device)
  ttnn_matmul_33 = ttnn.matmul(ttnn_to_device_67, ttnn_transpose_51, )
  ttnn_from_torch_102 = ttnn.from_torch(arg103_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_24 = ttnn.add(ttnn_from_torch_102, ttnn_matmul_33, )
  ttnn_from_device_135 = ttnn.from_device(ttnn_add_24, )
  ttnn_to_layout_135 = ttnn.to_layout(ttnn_from_device_135, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_69 = ttnn.reshape(ttnn_to_layout_135, (1, 768, 196), )
  ttnn_from_device_136 = ttnn.from_device(ttnn_reshape_69, )
  ttnn_to_layout_136 = ttnn.to_layout(ttnn_from_device_136, ttnn.TILE_LAYOUT, )
  ttnn_to_device_68 = ttnn.to_device(ttnn_to_layout_136, device = device)
  ttnn_prefix_clone_33 = clone_wrapper(ttnn_to_device_68, )
  ttnn_transpose_52 = ttnn.transpose(ttnn_prefix_clone_33, 1, 2, )
  ttnn_add_62 = ttnn.add(ttnn_add_60, ttnn_transpose_52, )
  ttnn_from_torch_103 = ttnn.from_torch(arg104_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_104 = ttnn.from_torch(arg105_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_17_ = ttnn.layer_norm(ttnn_add_62, epsilon = 1e-06, weight = ttnn_from_torch_103, bias = ttnn_from_torch_104)
  ttnn_layer_norm_17_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_add_62), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_103), 
                                                                  ttnn.to_torch(ttnn_from_torch_104), 1e-06, )[0]
  ttnn_layer_norm_17 = ttnn.from_torch(ttnn_layer_norm_17_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_17_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_17_), ttnn_layer_norm_17))
    # Pocetak koda za proveru
  print(f"mixer_ln17_input: {ttnn_add_62}")
  print(f"mixer_ln17_weight: {ttnn_from_torch_103}")
  print(f"mixer_ln17_bias: {ttnn_from_torch_104}")
  def save_tensor_to_csv(tensor, filename):
    import pandas as pd
    tensor = tensor.contiguous()
    if tensor.dtype == torch.bfloat16:
        tensor = tensor.to(torch.float32)
    if tensor.ndim == 0:  # Scalar
        df = pd.DataFrame([tensor.item()])
    elif tensor.ndim == 1:  # 1D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 2:  # 2D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 3:  # 3D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    elif tensor.ndim == 4:  # 4D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    else:
        raise ValueError("Unsupported tensor dimension")
    df.to_csv(filename, index=False)
  def load_tensor_from_csv(filename, shape):
    import pandas as pd
    df = pd.read_csv(filename)
    data = df.values
    tensor = torch.tensor(data)
    # Reshape the tensor to the original shape
    tensor = tensor.view(shape)
    return tensor

  x_1 = ttnn.to_torch(ttnn_add_62)
  x_2 = ttnn.to_torch(ttnn_from_torch_103)
  x_3 = ttnn.to_torch(ttnn_from_torch_104)
  x1_shape = x_1.shape
  x2_shape = x_2.shape
  x3_shape = x_3.shape
  save_tensor_to_csv(x_1, "mixer_ln17_input.csv")
  save_tensor_to_csv(x_2, "mixer_ln17_weight.csv")
  save_tensor_to_csv(x_3, "mixer_ln17_bias.csv")
  load_1 = load_tensor_from_csv("mixer_ln17_input.csv", x1_shape)
  load_2 = load_tensor_from_csv("mixer_ln17_weight.csv", x2_shape)
  load_3 = load_tensor_from_csv("mixer_ln17_bias.csv", x3_shape)
  test_accuracy(x_1, load_1)
  test_accuracy(x_2, load_2)
  test_accuracy(x_3, load_3)
  # Kraj koda za proveru
  test_accuracy(native_layer_norm_17[0], ttnn_layer_norm_17)
  ttnn_from_device_137 = ttnn.from_device(ttnn_layer_norm_17, )
  ttnn_to_layout_137 = ttnn.to_layout(ttnn_from_device_137, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_70 = ttnn.reshape(ttnn_to_layout_137, (196, 768), )
  ttnn_from_torch_105 = ttnn.from_torch(arg106_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_53 = ttnn.transpose(ttnn_from_torch_105, 0, 1, )
  ttnn_from_device_138 = ttnn.from_device(ttnn_reshape_70, )
  ttnn_to_layout_138 = ttnn.to_layout(ttnn_from_device_138, ttnn.TILE_LAYOUT, )
  ttnn_to_device_69 = ttnn.to_device(ttnn_to_layout_138, device = device)
  ttnn_matmul_34 = ttnn.matmul(ttnn_to_device_69, ttnn_transpose_53, )
  ttnn_from_torch_106 = ttnn.from_torch(arg107_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_25 = ttnn.add(ttnn_from_torch_106, ttnn_matmul_34, )
  ttnn_from_device_139 = ttnn.from_device(ttnn_add_25, )
  ttnn_to_layout_139 = ttnn.to_layout(ttnn_from_device_139, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_71 = ttnn.reshape(ttnn_to_layout_139, (1, 196, 3072), )
  ttnn_from_device_140 = ttnn.from_device(ttnn_reshape_71, )
  ttnn_to_layout_140 = ttnn.to_layout(ttnn_from_device_140, ttnn.TILE_LAYOUT, )
  ttnn_to_device_70 = ttnn.to_device(ttnn_to_layout_140, device = device)
  ttnn_gelu_17 = ttnn.gelu(ttnn_to_device_70, )
  ttnn_prefix_clone_34 = clone_wrapper(ttnn_gelu_17, )
  ttnn_from_device_141 = ttnn.from_device(ttnn_prefix_clone_34, )
  ttnn_to_layout_141 = ttnn.to_layout(ttnn_from_device_141, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_72 = ttnn.reshape(ttnn_to_layout_141, (196, 3072), )
  ttnn_from_torch_107 = ttnn.from_torch(arg108_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_54 = ttnn.transpose(ttnn_from_torch_107, 0, 1, )
  ttnn_from_device_142 = ttnn.from_device(ttnn_reshape_72, )
  ttnn_to_layout_142 = ttnn.to_layout(ttnn_from_device_142, ttnn.TILE_LAYOUT, )
  ttnn_to_device_71 = ttnn.to_device(ttnn_to_layout_142, device = device)
  ttnn_matmul_35 = ttnn.matmul(ttnn_to_device_71, ttnn_transpose_54, )
  ttnn_from_torch_108 = ttnn.from_torch(arg109_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_26 = ttnn.add(ttnn_from_torch_108, ttnn_matmul_35, )
  ttnn_from_device_143 = ttnn.from_device(ttnn_add_26, )
  ttnn_to_layout_143 = ttnn.to_layout(ttnn_from_device_143, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_73 = ttnn.reshape(ttnn_to_layout_143, (1, 196, 768), )
  ttnn_from_device_144 = ttnn.from_device(ttnn_reshape_73, )
  ttnn_to_layout_144 = ttnn.to_layout(ttnn_from_device_144, ttnn.TILE_LAYOUT, )
  ttnn_to_device_72 = ttnn.to_device(ttnn_to_layout_144, device = device)
  ttnn_prefix_clone_35 = clone_wrapper(ttnn_to_device_72, )
  ttnn_add_63 = ttnn.add(ttnn_add_62, ttnn_prefix_clone_35, )
  ttnn_from_torch_109 = ttnn.from_torch(arg110_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_110 = ttnn.from_torch(arg111_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_18_ = ttnn.layer_norm(ttnn_add_63, epsilon = 1e-06, weight = ttnn_from_torch_109, bias = ttnn_from_torch_110)
  ttnn_layer_norm_18_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_add_63), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_109), 
                                                                  ttnn.to_torch(ttnn_from_torch_110), 1e-06, )[0]
  ttnn_layer_norm_18 = ttnn.from_torch(ttnn_layer_norm_18_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_18_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_18_), ttnn_layer_norm_18))
    # Pocetak koda za proveru
  print(f"mixer_ln18_input: {ttnn_add_63}")
  print(f"mixer_ln18_weight: {ttnn_from_torch_109}")
  print(f"mixer_ln18_bias: {ttnn_from_torch_110}")
  def save_tensor_to_csv(tensor, filename):
    import pandas as pd
    tensor = tensor.contiguous()
    if tensor.dtype == torch.bfloat16:
        tensor = tensor.to(torch.float32)
    if tensor.ndim == 0:  # Scalar
        df = pd.DataFrame([tensor.item()])
    elif tensor.ndim == 1:  # 1D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 2:  # 2D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 3:  # 3D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    elif tensor.ndim == 4:  # 4D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    else:
        raise ValueError("Unsupported tensor dimension")
    df.to_csv(filename, index=False)
  def load_tensor_from_csv(filename, shape):
    import pandas as pd
    df = pd.read_csv(filename)
    data = df.values
    tensor = torch.tensor(data)
    # Reshape the tensor to the original shape
    tensor = tensor.view(shape)
    return tensor

  x_1 = ttnn.to_torch(ttnn_add_63)
  x_2 = ttnn.to_torch(ttnn_from_torch_109)
  x_3 = ttnn.to_torch(ttnn_from_torch_110)
  x1_shape = x_1.shape
  x2_shape = x_2.shape
  x3_shape = x_3.shape
  save_tensor_to_csv(x_1, "mixer_ln18_input.csv")
  save_tensor_to_csv(x_2, "mixer_ln18_weight.csv")
  save_tensor_to_csv(x_3, "mixer_ln18_bias.csv")
  load_1 = load_tensor_from_csv("mixer_ln18_input.csv", x1_shape)
  load_2 = load_tensor_from_csv("mixer_ln18_weight.csv", x2_shape)
  load_3 = load_tensor_from_csv("mixer_ln18_bias.csv", x3_shape)
  test_accuracy(x_1, load_1)
  test_accuracy(x_2, load_2)
  test_accuracy(x_3, load_3)
  # Kraj koda za proveru
  test_accuracy(native_layer_norm_18[0], ttnn_layer_norm_18)
  ttnn_transpose_55 = ttnn.transpose(ttnn_layer_norm_18, 1, 2, )
  ttnn_from_torch_111 = ttnn.from_torch(arg112_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_56 = ttnn.transpose(ttnn_from_torch_111, 0, 1, )
  ttnn_from_device_145 = ttnn.from_device(ttnn_transpose_55, )
  ttnn_to_layout_145 = ttnn.to_layout(ttnn_from_device_145, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_74 = ttnn.reshape(ttnn_to_layout_145, (768, 196), )
  ttnn_from_device_146 = ttnn.from_device(ttnn_reshape_74, )
  ttnn_to_layout_146 = ttnn.to_layout(ttnn_from_device_146, ttnn.TILE_LAYOUT, )
  ttnn_to_device_73 = ttnn.to_device(ttnn_to_layout_146, device = device)
  ttnn_matmul_36 = ttnn.matmul(ttnn_to_device_73, ttnn_transpose_56, )
  ttnn_from_device_147 = ttnn.from_device(ttnn_matmul_36, )
  ttnn_to_layout_147 = ttnn.to_layout(ttnn_from_device_147, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_75 = ttnn.reshape(ttnn_to_layout_147, (1, 768, 384), )
  ttnn_from_device_148 = ttnn.from_device(ttnn_reshape_75, )
  ttnn_to_layout_148 = ttnn.to_layout(ttnn_from_device_148, ttnn.TILE_LAYOUT, )
  ttnn_to_device_74 = ttnn.to_device(ttnn_to_layout_148, device = device)
  ttnn_from_torch_112 = ttnn.from_torch(arg113_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_64 = ttnn.add(ttnn_to_device_74, ttnn_from_torch_112, )
  ttnn_gelu_18 = ttnn.gelu(ttnn_add_64, )
  ttnn_prefix_clone_36 = clone_wrapper(ttnn_gelu_18, )
  ttnn_from_device_149 = ttnn.from_device(ttnn_prefix_clone_36, )
  ttnn_to_layout_149 = ttnn.to_layout(ttnn_from_device_149, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_76 = ttnn.reshape(ttnn_to_layout_149, (768, 384), )
  ttnn_from_torch_113 = ttnn.from_torch(arg114_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_57 = ttnn.transpose(ttnn_from_torch_113, 0, 1, )
  ttnn_from_device_150 = ttnn.from_device(ttnn_reshape_76, )
  ttnn_to_layout_150 = ttnn.to_layout(ttnn_from_device_150, ttnn.TILE_LAYOUT, )
  ttnn_to_device_75 = ttnn.to_device(ttnn_to_layout_150, device = device)
  ttnn_matmul_37 = ttnn.matmul(ttnn_to_device_75, ttnn_transpose_57, )
  ttnn_from_torch_114 = ttnn.from_torch(arg115_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_27 = ttnn.add(ttnn_from_torch_114, ttnn_matmul_37, )
  ttnn_from_device_151 = ttnn.from_device(ttnn_add_27, )
  ttnn_to_layout_151 = ttnn.to_layout(ttnn_from_device_151, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_77 = ttnn.reshape(ttnn_to_layout_151, (1, 768, 196), )
  ttnn_from_device_152 = ttnn.from_device(ttnn_reshape_77, )
  ttnn_to_layout_152 = ttnn.to_layout(ttnn_from_device_152, ttnn.TILE_LAYOUT, )
  ttnn_to_device_76 = ttnn.to_device(ttnn_to_layout_152, device = device)
  ttnn_prefix_clone_37 = clone_wrapper(ttnn_to_device_76, )
  ttnn_transpose_58 = ttnn.transpose(ttnn_prefix_clone_37, 1, 2, )
  ttnn_add_65 = ttnn.add(ttnn_add_63, ttnn_transpose_58, )
  ttnn_from_torch_115 = ttnn.from_torch(arg116_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_116 = ttnn.from_torch(arg117_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_19_ = ttnn.layer_norm(ttnn_add_65, epsilon = 1e-06, weight = ttnn_from_torch_115, bias = ttnn_from_torch_116)
  ttnn_layer_norm_19_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_add_65), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_115), 
                                                                  ttnn.to_torch(ttnn_from_torch_116), 1e-06, )[0]
  ttnn_layer_norm_19 = ttnn.from_torch(ttnn_layer_norm_19_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_19_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_19_), ttnn_layer_norm_19))
    # Pocetak koda za proveru
  print(f"mixer_ln19_input: {ttnn_add_65}")
  print(f"mixer_ln19_weight: {ttnn_from_torch_115}")
  print(f"mixer_ln19_bias: {ttnn_from_torch_116}")
  def save_tensor_to_csv(tensor, filename):
    import pandas as pd
    tensor = tensor.contiguous()
    if tensor.dtype == torch.bfloat16:
        tensor = tensor.to(torch.float32)
    if tensor.ndim == 0:  # Scalar
        df = pd.DataFrame([tensor.item()])
    elif tensor.ndim == 1:  # 1D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 2:  # 2D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 3:  # 3D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    elif tensor.ndim == 4:  # 4D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    else:
        raise ValueError("Unsupported tensor dimension")
    df.to_csv(filename, index=False)
  def load_tensor_from_csv(filename, shape):
    import pandas as pd
    df = pd.read_csv(filename)
    data = df.values
    tensor = torch.tensor(data)
    # Reshape the tensor to the original shape
    tensor = tensor.view(shape)
    return tensor

  x_1 = ttnn.to_torch(ttnn_add_65)
  x_2 = ttnn.to_torch(ttnn_from_torch_115)
  x_3 = ttnn.to_torch(ttnn_from_torch_116)
  x1_shape = x_1.shape
  x2_shape = x_2.shape
  x3_shape = x_3.shape
  save_tensor_to_csv(x_1, "mixer_ln19_input.csv")
  save_tensor_to_csv(x_2, "mixer_ln19_weight.csv")
  save_tensor_to_csv(x_3, "mixer_ln19_bias.csv")
  load_1 = load_tensor_from_csv("mixer_ln19_input.csv", x1_shape)
  load_2 = load_tensor_from_csv("mixer_ln19_weight.csv", x2_shape)
  load_3 = load_tensor_from_csv("mixer_ln19_bias.csv", x3_shape)
  test_accuracy(x_1, load_1)
  test_accuracy(x_2, load_2)
  test_accuracy(x_3, load_3)
  # Kraj koda za proveru
  test_accuracy(native_layer_norm_19[0], ttnn_layer_norm_19)
  ttnn_from_device_153 = ttnn.from_device(ttnn_layer_norm_19, )
  ttnn_to_layout_153 = ttnn.to_layout(ttnn_from_device_153, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_78 = ttnn.reshape(ttnn_to_layout_153, (196, 768), )
  ttnn_from_torch_117 = ttnn.from_torch(arg118_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_59 = ttnn.transpose(ttnn_from_torch_117, 0, 1, )
  ttnn_from_device_154 = ttnn.from_device(ttnn_reshape_78, )
  ttnn_to_layout_154 = ttnn.to_layout(ttnn_from_device_154, ttnn.TILE_LAYOUT, )
  ttnn_to_device_77 = ttnn.to_device(ttnn_to_layout_154, device = device)
  ttnn_matmul_38 = ttnn.matmul(ttnn_to_device_77, ttnn_transpose_59, )
  ttnn_from_torch_118 = ttnn.from_torch(arg119_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_28 = ttnn.add(ttnn_from_torch_118, ttnn_matmul_38, )
  ttnn_from_device_155 = ttnn.from_device(ttnn_add_28, )
  ttnn_to_layout_155 = ttnn.to_layout(ttnn_from_device_155, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_79 = ttnn.reshape(ttnn_to_layout_155, (1, 196, 3072), )
  ttnn_from_device_156 = ttnn.from_device(ttnn_reshape_79, )
  ttnn_to_layout_156 = ttnn.to_layout(ttnn_from_device_156, ttnn.TILE_LAYOUT, )
  ttnn_to_device_78 = ttnn.to_device(ttnn_to_layout_156, device = device)
  ttnn_gelu_19 = ttnn.gelu(ttnn_to_device_78, )
  ttnn_prefix_clone_38 = clone_wrapper(ttnn_gelu_19, )
  ttnn_from_device_157 = ttnn.from_device(ttnn_prefix_clone_38, )
  ttnn_to_layout_157 = ttnn.to_layout(ttnn_from_device_157, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_80 = ttnn.reshape(ttnn_to_layout_157, (196, 3072), )
  ttnn_from_torch_119 = ttnn.from_torch(arg120_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_60 = ttnn.transpose(ttnn_from_torch_119, 0, 1, )
  ttnn_from_device_158 = ttnn.from_device(ttnn_reshape_80, )
  ttnn_to_layout_158 = ttnn.to_layout(ttnn_from_device_158, ttnn.TILE_LAYOUT, )
  ttnn_to_device_79 = ttnn.to_device(ttnn_to_layout_158, device = device)
  ttnn_matmul_39 = ttnn.matmul(ttnn_to_device_79, ttnn_transpose_60, )
  ttnn_from_torch_120 = ttnn.from_torch(arg121_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_29 = ttnn.add(ttnn_from_torch_120, ttnn_matmul_39, )
  ttnn_from_device_159 = ttnn.from_device(ttnn_add_29, )
  ttnn_to_layout_159 = ttnn.to_layout(ttnn_from_device_159, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_81 = ttnn.reshape(ttnn_to_layout_159, (1, 196, 768), )
  ttnn_from_device_160 = ttnn.from_device(ttnn_reshape_81, )
  ttnn_to_layout_160 = ttnn.to_layout(ttnn_from_device_160, ttnn.TILE_LAYOUT, )
  ttnn_to_device_80 = ttnn.to_device(ttnn_to_layout_160, device = device)
  ttnn_prefix_clone_39 = clone_wrapper(ttnn_to_device_80, )
  ttnn_add_66 = ttnn.add(ttnn_add_65, ttnn_prefix_clone_39, )
  ttnn_from_torch_121 = ttnn.from_torch(arg122_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_122 = ttnn.from_torch(arg123_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_20_ = ttnn.layer_norm(ttnn_add_66, epsilon = 1e-06, weight = ttnn_from_torch_121, bias = ttnn_from_torch_122)
  ttnn_layer_norm_20_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_add_66), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_121), 
                                                                  ttnn.to_torch(ttnn_from_torch_122), 1e-06, )[0]
  ttnn_layer_norm_20 = ttnn.from_torch(ttnn_layer_norm_20_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_20_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_20_), ttnn_layer_norm_20))
    # Pocetak koda za proveru
  print(f"mixer_ln20_input: {ttnn_add_66}")
  print(f"mixer_ln20_weight: {ttnn_from_torch_121}")
  print(f"mixer_ln20_bias: {ttnn_from_torch_122}")
  def save_tensor_to_csv(tensor, filename):
    import pandas as pd
    tensor = tensor.contiguous()
    if tensor.dtype == torch.bfloat16:
        tensor = tensor.to(torch.float32)
    if tensor.ndim == 0:  # Scalar
        df = pd.DataFrame([tensor.item()])
    elif tensor.ndim == 1:  # 1D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 2:  # 2D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 3:  # 3D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    elif tensor.ndim == 4:  # 4D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    else:
        raise ValueError("Unsupported tensor dimension")
    df.to_csv(filename, index=False)
  def load_tensor_from_csv(filename, shape):
    import pandas as pd
    df = pd.read_csv(filename)
    data = df.values
    tensor = torch.tensor(data)
    # Reshape the tensor to the original shape
    tensor = tensor.view(shape)
    return tensor

  x_1 = ttnn.to_torch(ttnn_add_66)
  x_2 = ttnn.to_torch(ttnn_from_torch_121)
  x_3 = ttnn.to_torch(ttnn_from_torch_122)
  x1_shape = x_1.shape
  x2_shape = x_2.shape
  x3_shape = x_3.shape
  save_tensor_to_csv(x_1, "mixer_ln20_input.csv")
  save_tensor_to_csv(x_2, "mixer_ln20_weight.csv")
  save_tensor_to_csv(x_3, "mixer_ln20_bias.csv")
  load_1 = load_tensor_from_csv("mixer_ln20_input.csv", x1_shape)
  load_2 = load_tensor_from_csv("mixer_ln20_weight.csv", x2_shape)
  load_3 = load_tensor_from_csv("mixer_ln20_bias.csv", x3_shape)
  test_accuracy(x_1, load_1)
  test_accuracy(x_2, load_2)
  test_accuracy(x_3, load_3)
  # Kraj koda za proveru
  test_accuracy(native_layer_norm_20[0], ttnn_layer_norm_20)
  ttnn_transpose_61 = ttnn.transpose(ttnn_layer_norm_20, 1, 2, )
  ttnn_from_torch_123 = ttnn.from_torch(arg124_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_62 = ttnn.transpose(ttnn_from_torch_123, 0, 1, )
  ttnn_from_device_161 = ttnn.from_device(ttnn_transpose_61, )
  ttnn_to_layout_161 = ttnn.to_layout(ttnn_from_device_161, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_82 = ttnn.reshape(ttnn_to_layout_161, (768, 196), )
  ttnn_from_device_162 = ttnn.from_device(ttnn_reshape_82, )
  ttnn_to_layout_162 = ttnn.to_layout(ttnn_from_device_162, ttnn.TILE_LAYOUT, )
  ttnn_to_device_81 = ttnn.to_device(ttnn_to_layout_162, device = device)
  ttnn_matmul_40 = ttnn.matmul(ttnn_to_device_81, ttnn_transpose_62, )
  ttnn_from_device_163 = ttnn.from_device(ttnn_matmul_40, )
  ttnn_to_layout_163 = ttnn.to_layout(ttnn_from_device_163, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_83 = ttnn.reshape(ttnn_to_layout_163, (1, 768, 384), )
  ttnn_from_device_164 = ttnn.from_device(ttnn_reshape_83, )
  ttnn_to_layout_164 = ttnn.to_layout(ttnn_from_device_164, ttnn.TILE_LAYOUT, )
  ttnn_to_device_82 = ttnn.to_device(ttnn_to_layout_164, device = device)
  ttnn_from_torch_124 = ttnn.from_torch(arg125_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_67 = ttnn.add(ttnn_to_device_82, ttnn_from_torch_124, )
  ttnn_gelu_20 = ttnn.gelu(ttnn_add_67, )
  ttnn_prefix_clone_40 = clone_wrapper(ttnn_gelu_20, )
  ttnn_from_device_165 = ttnn.from_device(ttnn_prefix_clone_40, )
  ttnn_to_layout_165 = ttnn.to_layout(ttnn_from_device_165, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_84 = ttnn.reshape(ttnn_to_layout_165, (768, 384), )
  ttnn_from_torch_125 = ttnn.from_torch(arg126_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_63 = ttnn.transpose(ttnn_from_torch_125, 0, 1, )
  ttnn_from_device_166 = ttnn.from_device(ttnn_reshape_84, )
  ttnn_to_layout_166 = ttnn.to_layout(ttnn_from_device_166, ttnn.TILE_LAYOUT, )
  ttnn_to_device_83 = ttnn.to_device(ttnn_to_layout_166, device = device)
  ttnn_matmul_41 = ttnn.matmul(ttnn_to_device_83, ttnn_transpose_63, )
  ttnn_from_torch_126 = ttnn.from_torch(arg127_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_30 = ttnn.add(ttnn_from_torch_126, ttnn_matmul_41, )
  ttnn_from_device_167 = ttnn.from_device(ttnn_add_30, )
  ttnn_to_layout_167 = ttnn.to_layout(ttnn_from_device_167, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_85 = ttnn.reshape(ttnn_to_layout_167, (1, 768, 196), )
  ttnn_from_device_168 = ttnn.from_device(ttnn_reshape_85, )
  ttnn_to_layout_168 = ttnn.to_layout(ttnn_from_device_168, ttnn.TILE_LAYOUT, )
  ttnn_to_device_84 = ttnn.to_device(ttnn_to_layout_168, device = device)
  ttnn_prefix_clone_41 = clone_wrapper(ttnn_to_device_84, )
  ttnn_transpose_64 = ttnn.transpose(ttnn_prefix_clone_41, 1, 2, )
  ttnn_add_68 = ttnn.add(ttnn_add_66, ttnn_transpose_64, )
  ttnn_from_torch_127 = ttnn.from_torch(arg128_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_128 = ttnn.from_torch(arg129_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_21_ = ttnn.layer_norm(ttnn_add_68, epsilon = 1e-06, weight = ttnn_from_torch_127, bias = ttnn_from_torch_128)
  ttnn_layer_norm_21_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_add_68), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_127), 
                                                                  ttnn.to_torch(ttnn_from_torch_128), 1e-06, )[0]
  ttnn_layer_norm_21 = ttnn.from_torch(ttnn_layer_norm_21_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_21_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_21_), ttnn_layer_norm_21))
    # Pocetak koda za proveru
  print(f"mixer_ln21_input: {ttnn_add_68}")
  print(f"mixer_ln21_weight: {ttnn_from_torch_127}")
  print(f"mixer_ln21_bias: {ttnn_from_torch_128}")
  def save_tensor_to_csv(tensor, filename):
    import pandas as pd
    tensor = tensor.contiguous()
    if tensor.dtype == torch.bfloat16:
        tensor = tensor.to(torch.float32)
    if tensor.ndim == 0:  # Scalar
        df = pd.DataFrame([tensor.item()])
    elif tensor.ndim == 1:  # 1D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 2:  # 2D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 3:  # 3D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    elif tensor.ndim == 4:  # 4D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    else:
        raise ValueError("Unsupported tensor dimension")
    df.to_csv(filename, index=False)
  def load_tensor_from_csv(filename, shape):
    import pandas as pd
    df = pd.read_csv(filename)
    data = df.values
    tensor = torch.tensor(data)
    # Reshape the tensor to the original shape
    tensor = tensor.view(shape)
    return tensor

  x_1 = ttnn.to_torch(ttnn_add_68)
  x_2 = ttnn.to_torch(ttnn_from_torch_127)
  x_3 = ttnn.to_torch(ttnn_from_torch_128)
  x1_shape = x_1.shape
  x2_shape = x_2.shape
  x3_shape = x_3.shape
  save_tensor_to_csv(x_1, "mixer_ln21_input.csv")
  save_tensor_to_csv(x_2, "mixer_ln21_weight.csv")
  save_tensor_to_csv(x_3, "mixer_ln21_bias.csv")
  load_1 = load_tensor_from_csv("mixer_ln21_input.csv", x1_shape)
  load_2 = load_tensor_from_csv("mixer_ln21_weight.csv", x2_shape)
  load_3 = load_tensor_from_csv("mixer_ln21_bias.csv", x3_shape)
  test_accuracy(x_1, load_1)
  test_accuracy(x_2, load_2)
  test_accuracy(x_3, load_3)
  # Kraj koda za proveru
  test_accuracy(native_layer_norm_21[0], ttnn_layer_norm_21)
  ttnn_from_device_169 = ttnn.from_device(ttnn_layer_norm_21, )
  ttnn_to_layout_169 = ttnn.to_layout(ttnn_from_device_169, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_86 = ttnn.reshape(ttnn_to_layout_169, (196, 768), )
  ttnn_from_torch_129 = ttnn.from_torch(arg130_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_65 = ttnn.transpose(ttnn_from_torch_129, 0, 1, )
  ttnn_from_device_170 = ttnn.from_device(ttnn_reshape_86, )
  ttnn_to_layout_170 = ttnn.to_layout(ttnn_from_device_170, ttnn.TILE_LAYOUT, )
  ttnn_to_device_85 = ttnn.to_device(ttnn_to_layout_170, device = device)
  ttnn_matmul_42 = ttnn.matmul(ttnn_to_device_85, ttnn_transpose_65, )
  ttnn_from_torch_130 = ttnn.from_torch(arg131_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_31 = ttnn.add(ttnn_from_torch_130, ttnn_matmul_42, )
  ttnn_from_device_171 = ttnn.from_device(ttnn_add_31, )
  ttnn_to_layout_171 = ttnn.to_layout(ttnn_from_device_171, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_87 = ttnn.reshape(ttnn_to_layout_171, (1, 196, 3072), )
  ttnn_from_device_172 = ttnn.from_device(ttnn_reshape_87, )
  ttnn_to_layout_172 = ttnn.to_layout(ttnn_from_device_172, ttnn.TILE_LAYOUT, )
  ttnn_to_device_86 = ttnn.to_device(ttnn_to_layout_172, device = device)
  ttnn_gelu_21 = ttnn.gelu(ttnn_to_device_86, )
  ttnn_prefix_clone_42 = clone_wrapper(ttnn_gelu_21, )
  ttnn_from_device_173 = ttnn.from_device(ttnn_prefix_clone_42, )
  ttnn_to_layout_173 = ttnn.to_layout(ttnn_from_device_173, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_88 = ttnn.reshape(ttnn_to_layout_173, (196, 3072), )
  ttnn_from_torch_131 = ttnn.from_torch(arg132_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_66 = ttnn.transpose(ttnn_from_torch_131, 0, 1, )
  ttnn_from_device_174 = ttnn.from_device(ttnn_reshape_88, )
  ttnn_to_layout_174 = ttnn.to_layout(ttnn_from_device_174, ttnn.TILE_LAYOUT, )
  ttnn_to_device_87 = ttnn.to_device(ttnn_to_layout_174, device = device)
  ttnn_matmul_43 = ttnn.matmul(ttnn_to_device_87, ttnn_transpose_66, )
  ttnn_from_torch_132 = ttnn.from_torch(arg133_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_32 = ttnn.add(ttnn_from_torch_132, ttnn_matmul_43, )
  ttnn_from_device_175 = ttnn.from_device(ttnn_add_32, )
  ttnn_to_layout_175 = ttnn.to_layout(ttnn_from_device_175, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_89 = ttnn.reshape(ttnn_to_layout_175, (1, 196, 768), )
  ttnn_from_device_176 = ttnn.from_device(ttnn_reshape_89, )
  ttnn_to_layout_176 = ttnn.to_layout(ttnn_from_device_176, ttnn.TILE_LAYOUT, )
  ttnn_to_device_88 = ttnn.to_device(ttnn_to_layout_176, device = device)
  ttnn_prefix_clone_43 = clone_wrapper(ttnn_to_device_88, )
  ttnn_add_69 = ttnn.add(ttnn_add_68, ttnn_prefix_clone_43, )
  ttnn_from_torch_133 = ttnn.from_torch(arg134_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_134 = ttnn.from_torch(arg135_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_22_ = ttnn.layer_norm(ttnn_add_69, epsilon = 1e-06, weight = ttnn_from_torch_133, bias = ttnn_from_torch_134)
  ttnn_layer_norm_22_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_add_69), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_133), 
                                                                  ttnn.to_torch(ttnn_from_torch_134), 1e-06, )[0]
  ttnn_layer_norm_22 = ttnn.from_torch(ttnn_layer_norm_22_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_22_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_22_), ttnn_layer_norm_22))
    # Pocetak koda za proveru
  print(f"mixer_ln22_input: {ttnn_add_69}")
  print(f"mixer_ln22_weight: {ttnn_from_torch_133}")
  print(f"mixer_ln22_bias: {ttnn_from_torch_134}")
  def save_tensor_to_csv(tensor, filename):
    import pandas as pd
    tensor = tensor.contiguous()
    if tensor.dtype == torch.bfloat16:
        tensor = tensor.to(torch.float32)
    if tensor.ndim == 0:  # Scalar
        df = pd.DataFrame([tensor.item()])
    elif tensor.ndim == 1:  # 1D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 2:  # 2D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 3:  # 3D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    elif tensor.ndim == 4:  # 4D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    else:
        raise ValueError("Unsupported tensor dimension")
    df.to_csv(filename, index=False)
  def load_tensor_from_csv(filename, shape):
    import pandas as pd
    df = pd.read_csv(filename)
    data = df.values
    tensor = torch.tensor(data)
    # Reshape the tensor to the original shape
    tensor = tensor.view(shape)
    return tensor

  x_1 = ttnn.to_torch(ttnn_add_69)
  x_2 = ttnn.to_torch(ttnn_from_torch_133)
  x_3 = ttnn.to_torch(ttnn_from_torch_134)
  x1_shape = x_1.shape
  x2_shape = x_2.shape
  x3_shape = x_3.shape
  save_tensor_to_csv(x_1, "mixer_ln22_input.csv")
  save_tensor_to_csv(x_2, "mixer_ln22_weight.csv")
  save_tensor_to_csv(x_3, "mixer_ln22_bias.csv")
  load_1 = load_tensor_from_csv("mixer_ln22_input.csv", x1_shape)
  load_2 = load_tensor_from_csv("mixer_ln22_weight.csv", x2_shape)
  load_3 = load_tensor_from_csv("mixer_ln22_bias.csv", x3_shape)
  test_accuracy(x_1, load_1)
  test_accuracy(x_2, load_2)
  test_accuracy(x_3, load_3)
  # Kraj koda za proveru
  test_accuracy(native_layer_norm_22[0], ttnn_layer_norm_22)
  ttnn_transpose_67 = ttnn.transpose(ttnn_layer_norm_22, 1, 2, )
  test_accuracy(transpose_23, ttnn_transpose_67)
  ttnn_from_torch_135 = ttnn.from_torch(arg136_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_68 = ttnn.transpose(ttnn_from_torch_135, 0, 1, )
  test_accuracy(t_44, ttnn_transpose_68)
  ttnn_from_device_177 = ttnn.from_device(ttnn_transpose_67, )
  ttnn_to_layout_177 = ttnn.to_layout(ttnn_from_device_177, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_90 = ttnn.reshape(ttnn_to_layout_177, (768, 196), )
  test_accuracy(view_89, ttnn_reshape_90)
  ttnn_from_device_178 = ttnn.from_device(ttnn_reshape_90, )
  ttnn_to_layout_178 = ttnn.to_layout(ttnn_from_device_178, ttnn.TILE_LAYOUT, )
  ttnn_to_device_89 = ttnn.to_device(ttnn_to_layout_178, device = device)
  ttnn_matmul_44 = ttnn.matmul(ttnn_to_device_89, ttnn_transpose_68, )
  test_accuracy(mm_11, ttnn_matmul_44)
  ttnn_from_device_179 = ttnn.from_device(ttnn_matmul_44, )
  ttnn_to_layout_179 = ttnn.to_layout(ttnn_from_device_179, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_91 = ttnn.reshape(ttnn_to_layout_179, (1, 768, 384), )
  test_accuracy(view_90, ttnn_reshape_91)
  ttnn_from_device_180 = ttnn.from_device(ttnn_reshape_91, )
  ttnn_to_layout_180 = ttnn.to_layout(ttnn_from_device_180, ttnn.TILE_LAYOUT, )
  ttnn_to_device_90 = ttnn.to_device(ttnn_to_layout_180, device = device)
  ttnn_from_torch_136 = ttnn.from_torch(arg137_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_70 = ttnn.add(ttnn_to_device_90, ttnn_from_torch_136, )
  test_accuracy(add_33, ttnn_add_70)
  ttnn_gelu_22 = ttnn.gelu(ttnn_add_70, )
  test_accuracy(gelu_22, ttnn_gelu_22)
  ttnn_prefix_clone_44 = clone_wrapper(ttnn_gelu_22, )
  test_accuracy(clone_45, ttnn_prefix_clone_44)
  ttnn_from_device_181 = ttnn.from_device(ttnn_prefix_clone_44, )
  ttnn_to_layout_181 = ttnn.to_layout(ttnn_from_device_181, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_92 = ttnn.reshape(ttnn_to_layout_181, (768, 384), )
  test_accuracy(view_91, ttnn_reshape_92)
  ttnn_from_torch_137 = ttnn.from_torch(arg138_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_69 = ttnn.transpose(ttnn_from_torch_137, 0, 1, )
  test_accuracy(t_45, ttnn_transpose_69)
  ttnn_from_device_182 = ttnn.from_device(ttnn_reshape_92, )
  ttnn_to_layout_182 = ttnn.to_layout(ttnn_from_device_182, ttnn.TILE_LAYOUT, )
  ttnn_to_device_91 = ttnn.to_device(ttnn_to_layout_182, device = device)
  ttnn_matmul_45 = ttnn.matmul(ttnn_to_device_91, ttnn_transpose_69, )
  ttnn_from_torch_138 = ttnn.from_torch(arg139_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_33 = ttnn.add(ttnn_from_torch_138, ttnn_matmul_45, )
  test_accuracy(addmm_33, ttnn_add_33)
  ttnn_from_device_183 = ttnn.from_device(ttnn_add_33, )
  ttnn_to_layout_183 = ttnn.to_layout(ttnn_from_device_183, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_93 = ttnn.reshape(ttnn_to_layout_183, (1, 768, 196), )
  test_accuracy(view_92, ttnn_reshape_93)
  ttnn_from_device_184 = ttnn.from_device(ttnn_reshape_93, )
  ttnn_to_layout_184 = ttnn.to_layout(ttnn_from_device_184, ttnn.TILE_LAYOUT, )
  ttnn_to_device_92 = ttnn.to_device(ttnn_to_layout_184, device = device)
  ttnn_prefix_clone_45 = clone_wrapper(ttnn_to_device_92, )
  test_accuracy(clone_46, ttnn_prefix_clone_45)
  ttnn_transpose_70 = ttnn.transpose(ttnn_prefix_clone_45, 1, 2, )
  test_accuracy(transpose_24, ttnn_transpose_70)
  ttnn_add_71 = ttnn.add(ttnn_add_69, ttnn_transpose_70, )
  ttnn_from_torch_139 = ttnn.from_torch(arg140_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_140 = ttnn.from_torch(arg141_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_23_ = ttnn.layer_norm(ttnn_add_71, epsilon = 1e-06, weight = ttnn_from_torch_139, bias = ttnn_from_torch_140)
  ttnn_layer_norm_23_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_add_71), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_139), 
                                                                  ttnn.to_torch(ttnn_from_torch_140), 1e-06, )[0]
  ttnn_layer_norm_23 = ttnn.from_torch(ttnn_layer_norm_23_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_23_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_23_), ttnn_layer_norm_23))
    # Pocetak koda za proveru
  print(f"mixer_ln23_input: {ttnn_add_71}")
  print(f"mixer_ln23_weight: {ttnn_from_torch_139}")
  print(f"mixer_ln23_bias: {ttnn_from_torch_140}")
  def save_tensor_to_csv(tensor, filename):
    import pandas as pd
    tensor = tensor.contiguous()
    if tensor.dtype == torch.bfloat16:
        tensor = tensor.to(torch.float32)
    if tensor.ndim == 0:  # Scalar
        df = pd.DataFrame([tensor.item()])
    elif tensor.ndim == 1:  # 1D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 2:  # 2D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 3:  # 3D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    elif tensor.ndim == 4:  # 4D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    else:
        raise ValueError("Unsupported tensor dimension")
    df.to_csv(filename, index=False)
  def load_tensor_from_csv(filename, shape):
    import pandas as pd
    df = pd.read_csv(filename)
    data = df.values
    tensor = torch.tensor(data)
    # Reshape the tensor to the original shape
    tensor = tensor.view(shape)
    return tensor

  x_1 = ttnn.to_torch(ttnn_add_71)
  x_2 = ttnn.to_torch(ttnn_from_torch_139)
  x_3 = ttnn.to_torch(ttnn_from_torch_140)
  x1_shape = x_1.shape
  x2_shape = x_2.shape
  x3_shape = x_3.shape
  save_tensor_to_csv(x_1, "mixer_ln23_input.csv")
  save_tensor_to_csv(x_2, "mixer_ln23_weight.csv")
  save_tensor_to_csv(x_3, "mixer_ln23_bias.csv")
  load_1 = load_tensor_from_csv("mixer_ln23_input.csv", x1_shape)
  load_2 = load_tensor_from_csv("mixer_ln23_weight.csv", x2_shape)
  load_3 = load_tensor_from_csv("mixer_ln23_bias.csv", x3_shape)
  test_accuracy(x_1, load_1)
  test_accuracy(x_2, load_2)
  test_accuracy(x_3, load_3)
  # Kraj koda za proveru
  test_accuracy(native_layer_norm_23[0], ttnn_layer_norm_23)
  ttnn_from_device_185 = ttnn.from_device(ttnn_layer_norm_23, )
  ttnn_to_layout_185 = ttnn.to_layout(ttnn_from_device_185, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_94 = ttnn.reshape(ttnn_to_layout_185, (196, 768), )
  test_accuracy(view_93, ttnn_reshape_94)
  ttnn_from_torch_141 = ttnn.from_torch(arg142_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_71 = ttnn.transpose(ttnn_from_torch_141, 0, 1, )
  test_accuracy(t_46, ttnn_transpose_71)
  ttnn_from_device_186 = ttnn.from_device(ttnn_reshape_94, )
  ttnn_to_layout_186 = ttnn.to_layout(ttnn_from_device_186, ttnn.TILE_LAYOUT, )
  ttnn_to_device_93 = ttnn.to_device(ttnn_to_layout_186, device = device)
  ttnn_matmul_46 = ttnn.matmul(ttnn_to_device_93, ttnn_transpose_71, )
  ttnn_from_torch_142 = ttnn.from_torch(arg143_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_34 = ttnn.add(ttnn_from_torch_142, ttnn_matmul_46, )
  test_accuracy(addmm_34, ttnn_add_34)
  ttnn_from_device_187 = ttnn.from_device(ttnn_add_34, )
  ttnn_to_layout_187 = ttnn.to_layout(ttnn_from_device_187, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_95 = ttnn.reshape(ttnn_to_layout_187, (1, 196, 3072), )
  test_accuracy(view_94, ttnn_reshape_95)
  ttnn_from_device_188 = ttnn.from_device(ttnn_reshape_95, )
  ttnn_to_layout_188 = ttnn.to_layout(ttnn_from_device_188, ttnn.TILE_LAYOUT, )
  ttnn_to_device_94 = ttnn.to_device(ttnn_to_layout_188, device = device)
  ttnn_gelu_23 = ttnn.gelu(ttnn_to_device_94, )
  test_accuracy(gelu_23, ttnn_gelu_23)
  ttnn_prefix_clone_46 = clone_wrapper(ttnn_gelu_23, )
  test_accuracy(clone_47, ttnn_prefix_clone_46)
  ttnn_from_device_189 = ttnn.from_device(ttnn_prefix_clone_46, )
  ttnn_to_layout_189 = ttnn.to_layout(ttnn_from_device_189, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_96 = ttnn.reshape(ttnn_to_layout_189, (196, 3072), )
  test_accuracy(view_95, ttnn_reshape_96)
  ttnn_from_torch_143 = ttnn.from_torch(arg144_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_72 = ttnn.transpose(ttnn_from_torch_143, 0, 1, )
  test_accuracy(t_47, ttnn_transpose_72)
  ttnn_from_device_190 = ttnn.from_device(ttnn_reshape_96, )
  ttnn_to_layout_190 = ttnn.to_layout(ttnn_from_device_190, ttnn.TILE_LAYOUT, )
  ttnn_to_device_95 = ttnn.to_device(ttnn_to_layout_190, device = device)
  ttnn_matmul_47 = ttnn.matmul(ttnn_to_device_95, ttnn_transpose_72, )
  ttnn_from_torch_144 = ttnn.from_torch(arg145_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_35 = ttnn.add(ttnn_from_torch_144, ttnn_matmul_47, )
  test_accuracy(addmm_35, ttnn_add_35)
  ttnn_from_device_191 = ttnn.from_device(ttnn_add_35, )
  ttnn_to_layout_191 = ttnn.to_layout(ttnn_from_device_191, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape_97 = ttnn.reshape(ttnn_to_layout_191, (1, 196, 768), )
  test_accuracy(view_96, ttnn_reshape_97)
  ttnn_from_device_192 = ttnn.from_device(ttnn_reshape_97, )
  ttnn_to_layout_192 = ttnn.to_layout(ttnn_from_device_192, ttnn.TILE_LAYOUT, )
  ttnn_to_device_96 = ttnn.to_device(ttnn_to_layout_192, device = device)
  ttnn_prefix_clone_47 = clone_wrapper(ttnn_to_device_96, )
  test_accuracy(clone_48, ttnn_prefix_clone_47)
  ttnn_add_72 = ttnn.add(ttnn_add_71, ttnn_prefix_clone_47, )
  test_accuracy(add_35, ttnn_add_72)
  ttnn_from_torch_145 = ttnn.from_torch(arg146_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_from_torch_146 = ttnn.from_torch(arg147_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_layer_norm_24_ = ttnn.layer_norm(ttnn_add_72, epsilon = 1e-06, weight = ttnn_from_torch_145, bias = ttnn_from_torch_146)
  ttnn_layer_norm_24_intermediate = aten.native_layer_norm.default(ttnn.to_torch(ttnn_add_72), 
                                                                  [768], 
                                                                  ttnn.to_torch(ttnn_from_torch_145), 
                                                                  ttnn.to_torch(ttnn_from_torch_146), 1e-06, )[0]
  ttnn_layer_norm_24 = ttnn.from_torch(ttnn_layer_norm_24_intermediate, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16, )
  print("ttnn_layer_norm_24_: ", test_accuracy(ttnn.to_torch(ttnn_layer_norm_24_), ttnn_layer_norm_24))
    # Pocetak koda za proveru
  print(f"mixer_ln24_input: {ttnn_add_72}")
  print(f"mixer_ln24_weight: {ttnn_from_torch_145}")
  print(f"mixer_ln24_bias: {ttnn_from_torch_146}")
  def save_tensor_to_csv(tensor, filename):
    import pandas as pd
    tensor = tensor.contiguous()
    if tensor.dtype == torch.bfloat16:
        tensor = tensor.to(torch.float32)
    if tensor.ndim == 0:  # Scalar
        df = pd.DataFrame([tensor.item()])
    elif tensor.ndim == 1:  # 1D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 2:  # 2D
        df = pd.DataFrame(tensor.numpy())
    elif tensor.ndim == 3:  # 3D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    elif tensor.ndim == 4:  # 4D
        df = pd.DataFrame(tensor.view(-1, tensor.size(-1)).numpy())
    else:
        raise ValueError("Unsupported tensor dimension")
    df.to_csv(filename, index=False)
  def load_tensor_from_csv(filename, shape):
    import pandas as pd
    df = pd.read_csv(filename)
    data = df.values
    tensor = torch.tensor(data)
    # Reshape the tensor to the original shape
    tensor = tensor.view(shape)
    return tensor

  x_1 = ttnn.to_torch(ttnn_add_72)
  x_2 = ttnn.to_torch(ttnn_from_torch_145)
  x_3 = ttnn.to_torch(ttnn_from_torch_146)
  x1_shape = x_1.shape
  x2_shape = x_2.shape
  x3_shape = x_3.shape
  save_tensor_to_csv(x_1, "mixer_ln24_input.csv")
  save_tensor_to_csv(x_2, "mixer_ln24_weight.csv")
  save_tensor_to_csv(x_3, "mixer_ln24_bias.csv")
  load_1 = load_tensor_from_csv("mixer_ln24_input.csv", x1_shape)
  load_2 = load_tensor_from_csv("mixer_ln24_weight.csv", x2_shape)
  load_3 = load_tensor_from_csv("mixer_ln24_bias.csv", x3_shape)
  test_accuracy(x_1, load_1)
  test_accuracy(x_2, load_2)
  test_accuracy(x_3, load_3)
  # Kraj koda za proveru
  test_accuracy(native_layer_norm_24[0], ttnn_layer_norm_24)
  ttnn_mean = ttnn.mean(ttnn_layer_norm_24, 1, )
  ttnn_from_device_193 = ttnn.from_device(ttnn_mean, )
  ttnn_to_layout_193 = ttnn.to_layout(ttnn_from_device_193, ttnn.ROW_MAJOR_LAYOUT, )
  ttnn_reshape = ttnn.reshape(ttnn_to_layout_193, (1, 768), )
  test_accuracy(mean, ttnn_reshape)
  ttnn_from_device_194 = ttnn.from_device(ttnn_reshape, )
  ttnn_to_layout_194 = ttnn.to_layout(ttnn_from_device_194, ttnn.TILE_LAYOUT, )
  ttnn_to_device_97 = ttnn.to_device(ttnn_to_layout_194, device = device)
  ttnn_prefix_clone_48 = clone_wrapper(ttnn_to_device_97, )
  test_accuracy(clone_49, ttnn_prefix_clone_48)
  ttnn_from_torch_147 = ttnn.from_torch(arg148_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_transpose_73 = ttnn.transpose(ttnn_from_torch_147, 0, 1, )
  test_accuracy(t_48, ttnn_transpose_73)
  ttnn_matmul_48 = ttnn.matmul(ttnn_prefix_clone_48, ttnn_transpose_73, )
  ttnn_from_torch_148 = ttnn.from_torch(arg149_1, device = device, layout = ttnn.TILE_LAYOUT, dtype = ttnn.bfloat16)
  ttnn_add_36 = ttnn.add(ttnn_from_torch_148, ttnn_matmul_48, )
  print(test_accuracy(addmm_36, ttnn_add_36))
  ttnn_to_torch = ttnn.to_torch(ttnn_add_36, dtype = torch.bfloat16)
  ttnn.close_device(device)

if __name__ == "__main__":
    filepath = Path(__file__).with_name("mixer_b16_224.goog_in21k_inputs.pickle")
    file = lzma.open(filepath, "rb")
    inputs = pickle.load(file)
    forward(*inputs)


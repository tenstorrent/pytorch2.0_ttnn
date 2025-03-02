# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest
import ttnn


class PatternModule(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self._tensor_constant0 = torch.tensor([0.4850, 0.4560, 0.4060])
        self._tensor_constant1 = torch.tensor([0.2290, 0.2240, 0.2250])

    # arg306_1.shape: torch.Size([1, 3, 480, 640])
    def forward(self, arg306_1):
        clone = torch.ops.aten.clone.default(arg306_1)
        select = torch.ops.aten.select.int(clone, 0, 0)
        _tensor_constant0 = self._tensor_constant0  # tensor([0.4850, 0.4560, 0.4060])
        lift_fresh_copy = torch.ops.aten.lift_fresh_copy.default(_tensor_constant0)
        _tensor_constant1 = self._tensor_constant1  # tensor([0.2290, 0.2240, 0.2250])
        lift_fresh_copy_1 = torch.ops.aten.lift_fresh_copy.default(_tensor_constant1)
        slice_1 = torch.ops.aten.slice.Tensor(lift_fresh_copy, 0, 0, 9223372036854775807)
        unsqueeze = torch.ops.aten.unsqueeze.default(slice_1, 1)
        unsqueeze_1 = torch.ops.aten.unsqueeze.default(unsqueeze, 2)
        sub = torch.ops.aten.sub.Tensor(select, unsqueeze_1)
        slice_2 = torch.ops.aten.slice.Tensor(lift_fresh_copy_1, 0, 0, 9223372036854775807)
        unsqueeze_2 = torch.ops.aten.unsqueeze.default(slice_2, 1)
        unsqueeze_3 = torch.ops.aten.unsqueeze.default(unsqueeze_2, 2)
        div = torch.ops.aten.div.Tensor(sub, unsqueeze_3)
        unsqueeze_4 = torch.ops.aten.unsqueeze.default(div, 0)
        arange = torch.ops.aten.arange.default(
            800, dtype=torch.float32, device=torch.device(type="cpu"), pin_memory=False
        )
        arange_1 = torch.ops.aten.arange.default(
            1066, dtype=torch.float32, device=torch.device(type="cpu"), pin_memory=False
        )
        add = torch.ops.aten.add.Tensor(arange, 0.5)
        mul = torch.ops.aten.mul.Tensor(add, 0.6)
        sub_1 = torch.ops.aten.sub.Tensor(mul, 0.5)
        clamp = torch.ops.aten.clamp.default(sub_1, 0.0)
        add_1 = torch.ops.aten.add.Tensor(arange_1, 0.5)
        mul_1 = torch.ops.aten.mul.Tensor(add_1, 0.600375234521576)
        sub_2 = torch.ops.aten.sub.Tensor(mul_1, 0.5)
        clamp_1 = torch.ops.aten.clamp.default(sub_2, 0.0)
        _to_copy = torch.ops.aten._to_copy.default(clamp, dtype=torch.int64)
        _to_copy_2 = torch.ops.aten._to_copy.default(clamp_1, dtype=torch.int64)
        unsqueeze_6 = torch.ops.aten.unsqueeze.default(_to_copy, 1)
        # result_before:
        # unsqueeze_4.shape: torch.Size([1, 3, 480, 640])
        # unsqueeze_6.shape: torch.Size([800, 1]) (0~479)
        # _to_copy_2.shape: torch.Size([1066]) (0~639)
        # result_after:
        # unsqueeze_4.shape: torch.Size([1, 3, 480, 640])
        # unsqueeze_6.shape: torch.Size([1, 1, 800]) (0~480)
        # _to_copy_2.shape: torch.Size([1, 1066]) (0~640)
        # this open can trigger graph break and let breakpoint on currect line
        # with open("aa.txt", "w") as f:
        #     pass
        # breakpoint()
        _unsafe_index = torch.ops.aten._unsafe_index.Tensor(unsqueeze_4, [None, None, unsqueeze_6, _to_copy_2])
        return _unsafe_index


class PatternUnsqueezeModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self):
        arange = torch.ops.aten.arange.default(
            800, dtype=torch.float32, device=torch.device(type="cpu"), pin_memory=False
        )
        add = torch.ops.aten.add.Tensor(arange, 0.5)
        mul = torch.ops.aten.mul.Tensor(add, 0.6)
        sub_1 = torch.ops.aten.sub.Tensor(mul, 0.5)
        clamp = torch.ops.aten.clamp.default(sub_1, 0.0)
        _to_copy = torch.ops.aten._to_copy.default(clamp, dtype=torch.int64)
        unsqueeze_6 = torch.ops.aten.unsqueeze.default(_to_copy, 1)
        return unsqueeze_6


def test_retinanet_pattern(device):
    m = PatternModule()
    input = torch.rand([1, 3, 480, 640])
    result_before = m.forward(input)
    option = torch_ttnn.TorchTtnnOption(device=device)
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input)
    assert torch.allclose(result_before, result_after, rtol=0.1, atol=0.1)


def test_retinanet_pattern_unsqueeze(device):
    m = PatternUnsqueezeModule()
    result_before = m.forward()
    option = torch_ttnn.TorchTtnnOption(device=device)
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward()
    # result_before.shape: torch.Size([800, 1]) (0~479)
    # result_after.shape: torch.Size([1, 1, 800]) (0~480)
    assert result_before.shape == result_after.shape
    assert torch.allclose(result_before, result_after, rtol=0.1, atol=0.1)

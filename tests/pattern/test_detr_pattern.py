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

    def forward(self, arg56_1, addend):
        split = torch.ops.aten.split.Tensor(arg56_1, 256)
        getitem_2 = split[0]
        return torch.ops.aten.add.Tensor(getitem_2, addend)


def test_detr_pattern(device):
    m = PatternModule()
    arg56_1 = torch.randn([768, 256]).to(torch.bfloat16)
    addend = torch.randn([256, 256]).to(torch.bfloat16)
    result_before = m.forward(arg56_1, addend)
    option = torch_ttnn.TorchTtnnOption(device=device)
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(arg56_1, addend)
    assert torch.allclose(result_before, result_after, rtol=0.1, atol=0.1)

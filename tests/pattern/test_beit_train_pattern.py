# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest
import ttnn


# Found this bug on beit is aten.mean result shape is [1, 1000] but ttnn.mean result become [1, 1, 1000]
# Fixed it on the lowering of aten.mean
class PatternModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, dim):
        return torch.ops.aten.mean.dim(x, dim)


def test_beit_train_pattern(device):
    m = PatternModule()
    x = torch.randn([1, 2, 3]).to(torch.bfloat16)
    dim = [1]
    result_before = m.forward(x, dim)
    option = torch_ttnn.TorchTtnnOption(device=device)
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(x, dim)
    assert result_before.shape == result_after.shape
    assert torch.allclose(result_before, result_after, rtol=0.1, atol=0.1)

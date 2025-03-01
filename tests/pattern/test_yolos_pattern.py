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

    def forward(self, add1, add2):
        add = torch.ops.aten.add.Tensor(add1.reshape([7, 7]), add2)
        return add


def test_beit_pattern(device):
    m = PatternModule()
    add1 = torch.randint(0, 10, [49])
    add2 = torch.randn([7, 7]).to(torch.bfloat16)
    result_before = m.forward(add1, add2)
    option = torch_ttnn.TorchTtnnOption(device=device)
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(add1, add2)
    assert torch.allclose(result_before, result_after, rtol=0.1, atol=0.1)
    assert not any(node.target == torch.ops.aten.add.Tensor for node in option._out_fx_graphs[0].nodes)

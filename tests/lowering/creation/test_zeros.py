# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest


class ZerosModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, size, dtype):
        return torch.zeros(size, dtype=dtype)


@pytest.mark.parametrize(
    "size, dtype",
    [
        ((32, 32), torch.bfloat16),
        ((1, 256, 16, 16), torch.float32),
        ((1, 6, 18, 15), torch.bfloat16),
        ((1, 8, 3, 10), torch.bfloat16),
    ],
)
def test_zeros(device, size, dtype):
    m = ZerosModule()
    result_before = m.forward(size, dtype)
    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(size, dtype)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    # Check the graph has be rewritten and aten ops are replaced
    assert not any(node.target == torch.ops.aten.zeros.default for node in nodes)
    # Check inference result
    assert result_before.dtype == result_after.dtype
    assert torch.allclose(result_before, result_after)

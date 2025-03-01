# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest


class ZerosLikeModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input):
        return torch.zeros_like(input)


@pytest.mark.parametrize(
    "input_shape",
    [
        (4, 4),
        (7, 7),
        (1, 1),
        (17, 17),
        (1, 920),
        (100, 1, 256),
        pytest.param(
            (13685,), marks=pytest.mark.xfail(reason="Doesn't support 1D output tensor in tile layout (#280)")
        ),
    ],
)
def test_zeros_like(device, input_shape):
    m = ZerosLikeModule()
    torch_input = torch.rand(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(torch_input)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(torch_input)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    # Check the graph has be rewritten and aten ops are replaced
    assert not any(node.target == torch.ops.aten.zeros_like.default for node in nodes)
    # Check inference result
    assert torch.allclose(result_before, result_after)
    assert result_before.shape == result_after.shape

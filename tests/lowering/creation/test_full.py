# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest


class FullModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, size, fill_value):
        return torch.full(size, fill_value)


@pytest.mark.parametrize(
    "input_shape",
    [
        [64, 128],
        [19, 19],
        [59, 59],
        [33,],
        [],   # scalar
    ],
)
def test_full(device, input_shape):
    m = FullModule()
    fill_value = 1.23
    result_before = m.forward(input_shape, fill_value).to(torch.bfloat16)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input_shape, fill_value).to(torch.bfloat16)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    # Check the graph has be rewritten and aten ops are replaced
    assert not any(node.target == torch.ops.aten.full.default for node in nodes)
    # Check inference result
    assert torch.allclose(result_before, result_after)

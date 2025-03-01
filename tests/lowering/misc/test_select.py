# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class SelectModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, dim, index):
        return torch.select(input, dim, index)


@pytest.mark.parametrize(
    "input_shapes, dim, index",
    [
        ((3, 32, 16, 3, 96), 3, 0),
        ((3, 32, 16, 3, 96), 3, 1),
        ((3, 32, 16, 3, 96), 3, 2),
        ((3, 32, 16, 3, 96), 2, 0),
        ((3, 32, 16, 3, 96), 2, 1),
        ((3, 32, 16, 3, 96), 2, 2),
        ((3, 32, 16, 3, 96), 1, 0),
        ((3, 32, 16, 3, 96), 1, 1),
        ((3, 32, 16, 3, 96), 1, 2),
        ((3, 32, 16, 3, 96), 0, 0),
        ((3, 32, 16, 3, 96), 0, 1),
        ((3, 32, 16, 3, 96), 0, 2),
        ((3, 32, 16, 96), 1, 0),
        ((3, 32, 16, 96), 0, 0),
        ((3, 32, 16), 2, 0),
        ((3, 32, 16), 1, 0),
        ((3, 32, 16), 0, 0),
        ((3, 32), 0, 0),
        pytest.param((3, 32, 16, 3, 96), 4, 0, marks=pytest.mark.xfail()),
        pytest.param((3, 32, 16, 96), 3, 0, marks=pytest.mark.xfail()),
        pytest.param((3, 32, 16, 96), 2, 0, marks=pytest.mark.xfail()),
        pytest.param((3, 32), 1, 0, marks=pytest.mark.xfail()),
    ],
)
def test_select(device, input_shapes, dim, index):
    m = SelectModule()
    inputs = torch.rand(input_shapes, dtype=torch.bfloat16)
    result_before = m.forward(inputs, dim, index)

    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True

    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)

    result_after = m.forward(inputs, dim, index)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = [node.target for node in option._out_fx_graphs[0].nodes]
    assert torch.ops.aten.select.int not in nodes

    # Check inference result
    assert_with_pcc(result_before, result_after, pcc=0.99)

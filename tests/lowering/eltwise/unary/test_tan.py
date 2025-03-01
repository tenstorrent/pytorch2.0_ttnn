# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class TanModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.tan(x)


@pytest.mark.parametrize(
    "input_shape, range",
    (
        ((4, 4), 1),
        ((1, 1066), 1),
        ((1, 1066), 1.5),
        pytest.param((1, 1066), 1.6, marks=pytest.mark.xfail(reason="tt-metal#14414: inaccurate reciprocal")),
    ),
)
def test_tan(device, input_shape, range):
    m = TanModule()
    input = (torch.rand(input_shape, dtype=torch.bfloat16) * 2 - 1) * range
    result_before = m.forward(input)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.tan) == 1

    # Check inference result
    assert_with_pcc(result_before, result_after)

# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest

from tests.utils import assert_with_pcc


class ExpandModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input_tensor, shape):
        return torch.ops.aten.expand.default(input_tensor, shape)


@pytest.mark.parametrize(
    "input_shape, output_shape",
    [
        ((1, 2), (32, -1)),
        ((1, 4), (32, -1)),
        ((1, 6), (32, -1)),
        pytest.param((1, 3), (32, -1), marks=pytest.mark.xfail()),
        pytest.param((12, 1), (-1, 32), marks=pytest.mark.xfail()),
    ],
)
def test_expand(device, input_shape, output_shape):
    m = ExpandModule()
    input_tensor = torch.rand(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input_tensor, output_shape)

    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = False

    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)

    result_after = m.forward(input_tensor, output_shape)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = [node.target for node in option._out_fx_graphs[0].nodes]
    assert nodes.count(torch.ops.aten.expand.default) == 0

    assert_with_pcc(result_before, result_after, pcc=0.99)

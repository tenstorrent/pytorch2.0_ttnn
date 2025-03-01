# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest

from tests.utils import assert_with_pcc


class EluModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input_tensor, alpha):
        return torch.nn.functional.elu(input_tensor, alpha)


@pytest.mark.parametrize(
    "input_shape, alpha",
    [
        ((1, 128, 28, 28), 1.0),
        ((1, 128, 28, 28), 2.0),
        ((16, 32, 128, 28, 28), 1.0),
        ((1, 28), 1.0),
        pytest.param((28,), 1.0, marks=pytest.mark.xfail(reason="lost 1D shape with tile layout (tt-metal#12671)")),
    ],
)
def test_elu(device, input_shape, alpha):
    m = EluModule()
    input_tensor = torch.rand(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input_tensor, alpha)
    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input_tensor, alpha)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and not contain aten ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert not any(node.target == torch.ops.aten.elu.default for node in nodes)
    # Check inference result
    assert_with_pcc(result_before, result_after)

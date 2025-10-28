# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_ulp, assert_allclose


class PowTensorScalarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, exponent):
        square = torch.ops.aten.pow.Scalar(input, exponent)
        return square


@pytest.mark.parametrize(
    "input, exponent_shape",
    [[3, [2, 2]], [0, [1, 1]], [2.2, (2, 2)]],
)
def test_pow_tensor_scalar_square(device, input, exponent_shape):
    m = PowTensorScalarModule()
    exponent = torch.rand(exponent_shape, dtype=torch.bfloat16)
    result_before = m.forward(input, exponent)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, exponent)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.pow) == 1
    assert result_before.shape == result_after.shape
    # Check inference result
    if input == 0:
        assert_allclose(result_before, result_after, rtol=0.02, atol=1e-5)
    else:
        assert_with_ulp(result_before, result_after, 5)

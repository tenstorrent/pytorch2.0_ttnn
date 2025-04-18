# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest

from tests.utils import assert_with_pcc


class SumModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, tensor):
        return torch.ops.aten.sum.default(tensor)


@pytest.mark.xfail(reason="Knwon precision issue (#499)")
@pytest.mark.parametrize(
    "input_shapes",
    [
        (1, 20, 30),
        (1, 20),
        (1, 1),
        (1,),
    ],
)
@pytest.mark.skip(reason="Temporarily disabled due to issue#499")
def test_sum(device, input_shapes):
    m = SumModule()
    inputs = torch.rand(input_shapes, dtype=torch.bfloat16)
    result_before = m.forward(inputs)

    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=False)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)

    result_after = m.forward(inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = [node.target for node in option._out_fx_graphs[0].nodes]
    assert nodes.count(torch.ops.aten.sum.default) == 0

    assert_with_pcc(result_before, result_after, pcc=0.99)


class EqSumModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, tensor):
        eq_zero = torch.eq(tensor, 0)
        return torch.ops.aten.sum.default(eq_zero)


@pytest.mark.parametrize(
    "input_shape",
    [
        (1, 32, 32),
        pytest.param(
            (1, 7),
            marks=pytest.mark.xfail(reason="Knwon precision issue#499"),
        ),
    ],
)
def test_eq_sum(device, input_shape):
    m = EqSumModule()
    input_tensor = torch.randint(1, 10, input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input_tensor)

    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=False)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)

    result_after = m.forward(input_tensor)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = [node.target for node in option._out_fx_graphs[0].nodes]
    assert nodes.count(torch.ops.aten.sum.default) == 0

    print("result:", result_after)
    assert_with_pcc(result_before, result_after, pcc=0.99)

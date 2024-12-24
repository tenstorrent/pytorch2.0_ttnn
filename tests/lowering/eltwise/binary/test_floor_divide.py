import torch
import torch_ttnn
import pytest
import ttnn
from tests.utils import assert_with_pcc


class FloorDivideModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, numerator, denominator):
        return torch.floor_divide(numerator, denominator)


@pytest.mark.xfail(reason="ttnn.floor_div does not support tensor-tensor op yet")
@pytest.mark.parametrize(
    "input_shapes",
    (
        ((32, 32), (32, 32)),
        ((64,), (32, 64)),
        ((64, 32), (64, 1)),
        ((64, 1), (1, 64)),
        ((1, 23, 40, 1), (128,)),
        ((), ()),
        ((1, 12, 9, 9), ()),
    ),
)
def test_floor_divide(device, input_shapes):
    m = FloorDivideModule()
    inputs = [torch.randint(1, 15, shape).to(torch.bfloat16) for shape in input_shapes]
    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = [node.target for node in option._out_fx_graphs[0].nodes]
    assert torch.ops.aten.floor_divide.default not in nodes
    assert nodes.count(ttnn.floor_div) == 1

    # Check inference result
    assert_with_pcc(result_before, result_after)


@pytest.mark.parametrize(
    "input_shape, divisor",
    (
        ((15, 15), 2),
        ((17, 17), 2),
        ((32, 32), 2),
        ((15, 15), 4),
        ((15, 15), 8),
        ((15, 15), 16),
        pytest.param((15, 15), 5, marks=pytest.mark.xfail(reason="ttnn.floor_div is only accurate for 2^n divisor")),
        pytest.param((17, 17), 5, marks=pytest.mark.xfail(reason="ttnn.floor_div is only accurate for 2^n divisor")),
        pytest.param((32, 32), 5, marks=pytest.mark.xfail(reason="ttnn.floor_div is only accurate for 2^n divisor")),
    ),
)
def test_floor_divide_scalar_denom(device, input_shape, divisor):
    m = FloorDivideModule()
    input = torch.randint(1, 15, input_shape).to(torch.bfloat16)
    result_before = m.forward(input, divisor)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, divisor)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = [node.target for node in option._out_fx_graphs[0].nodes]
    assert torch.ops.aten.floor_divide.default not in nodes
    assert nodes.count(ttnn.floor_div) == 1

    # Check inference result
    assert_with_pcc(result_before, result_after)

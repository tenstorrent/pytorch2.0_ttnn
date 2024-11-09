import torch
import torch_ttnn
import pytest
import ttnn
from tests.utils import assert_with_pcc


class DivModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, numerator, denominator):
        return torch.div(numerator, denominator)


# ttnn.div does not support broadcasting some combination of shapes. Fallback to reciprocal and multiply.
@pytest.mark.parametrize(
    "input_shapes, use_ttnn_div",
    (
        (((32, 32), (32, 32)), True),
        (((64,), (32, 64)), False),
        (((64, 32), (64, 1)), False),
        pytest.param(
            ((64, 1), (1, 64)),
            False,
            marks=pytest.mark.xfail(reason="broadcasting issues (#64)"),
        ),
    ),
)
def test_div(device, input_shapes, use_ttnn_div):
    m = DivModule()
    inputs = [torch.randint(1, 15, shape).to(torch.bfloat16) for shape in input_shapes]
    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    target = [node.target for node in nodes]
    if use_ttnn_div:
        assert target.count(ttnn.div) == 1
    else:
        assert target.count(ttnn.reciprocal) == 1
        assert target.count(ttnn.mul) == 1
        assert target.index(ttnn.reciprocal) < target.index(ttnn.mul)
        assert nodes[target.index(ttnn.mul)].args[1].target == ttnn.reciprocal

    # Check inference result
    assert_with_pcc(result_before, result_after)


@pytest.mark.parametrize(
    "input_shapes",
    [[(4, 4)], [(32, 32)], [(1, 197, 1024)]],
)
def test_div_scalar_denom(device, input_shapes):
    m = DivModule()
    inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
    result_before = m.forward(*inputs, 5.0)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs, 5.0)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    target = [node.target for node in nodes]
    assert target.count(ttnn.div) == 1
    assert_with_pcc(result_before, result_after)

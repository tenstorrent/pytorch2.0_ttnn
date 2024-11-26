import torch
import torch_ttnn
import pytest
import ttnn
from tests.utils import assert_with_pcc


class GeModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, y):
        return torch.ge(x, y)


@pytest.mark.xfail(reason="broadcasting issues (#64)")
@pytest.mark.parametrize(
    "input_shapes",
    (((32, 32), (32, 32)), ((64,), (32, 64)), ((64, 32), (64, 1)), ((64, 1), (1, 64))),
)
def test_ge(device, input_shapes):
    m = GeModule()
    inputs = [torch.randint(1, 5, shape).type(torch.bfloat16) for shape in input_shapes]
    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.ge) == 1

    # Check inference result
    assert torch.allclose(result_before, result_after.to(torch.bool))


@pytest.mark.parametrize("input_shape", ((64, 128), (1, 1, 256), (2, 377, 355)))
def test_ge_scalar(device, input_shape):
    m = GeModule()
    input = torch.randint(0, 10, input_shape, dtype=torch.bfloat16)
    scalar = torch.randint(0, 10, ()).item()
    result_before = m.forward(input, scalar)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, scalar)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.ge) == 1

    # Check inference result
    assert torch.allclose(result_before, result_after.to(torch.bool))

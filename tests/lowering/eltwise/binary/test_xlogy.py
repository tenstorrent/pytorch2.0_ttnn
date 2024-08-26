import torch
import torch_ttnn
import pytest
import ttnn
from tests.utils import assert_with_pcc


class XlogyModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, y):
        return torch.xlogy(x, y)


@pytest.mark.parametrize(
    "input_shapes",
    (
        ((4, 4), (4, 4)),
        pytest.param(
            ((8, 1), (8, 8)),
            marks=pytest.mark.xfail(reason="broadcasting issues (#64)"),
        ),
        pytest.param(
            ((1, 8), (8, 1)),
            marks=pytest.mark.xfail(reason="broadcasting issues (#64)"),
        ),
    ),
)
def test_xlogy(device, input_shapes):
    m = XlogyModule()
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
    assert [node.target for node in nodes].count(ttnn.xlogy) == 1

    # Check inference result
    assert_with_pcc(result_before, result_after)

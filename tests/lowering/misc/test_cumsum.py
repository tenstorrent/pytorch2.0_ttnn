import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class CumsumModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, dim):
        return torch.ops.aten.cumsum.default(input, dim=dim)


@pytest.mark.parametrize(
    "input_shapes, dim",
    [
        ((1, 32), 1),
    ],
)
def test_cumsum(device, input_shapes, dim):
    m = CumsumModule()
    inputs = torch.rand(input_shapes, dtype=torch.bfloat16)
    result_before = m.forward(inputs, dim)

    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = False

    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)

    result_after = m.forward(inputs, dim)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = [node.target for node in option._out_fx_graphs[0].nodes]
    assert nodes.count(ttnn.moreh_cumsum) == 1

    # Check inference result
    assert_with_pcc(result_before, result_after, pcc=0.99)

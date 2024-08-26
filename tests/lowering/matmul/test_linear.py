import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class LinearModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, weight):
        return torch.nn.functional.linear(input, weight)


@pytest.mark.xfail(reason="cannot lower to ttnn.linear (#66)")
@pytest.mark.parametrize(
    "input_shapes",
    [[(4, 8), (6, 8)]],
)
def test_linear(device, input_shapes):
    m = LinearModule()
    inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
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
    assert target.count(ttnn.linear) == 1

    # Check inference result
    assert_with_pcc(result_before, result_after)

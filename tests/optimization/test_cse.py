import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class CseModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return x + x


@pytest.mark.parametrize(
    "input_shape",
    [(4, 4)],
)
def test_cse(device, input_shape):
    m = CseModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    target = [node.target for node in nodes]
    assert target.count(ttnn.from_torch) == 1
    assert target.count(ttnn.add) == 1
    assert target.index(ttnn.from_torch) < target.index(ttnn.add)

    # Check inference result
    assert_with_pcc(result_before, result_after)

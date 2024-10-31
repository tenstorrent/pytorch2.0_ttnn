import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class SelectModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input):
        return torch.select(input, 3, 0)


@pytest.mark.parametrize(
    "input_shapes",
    [(1, 32, 16, 3, 96)],
)
def test_adaptive_avg_pool_2d(device, input_shapes):
    m = SelectModule()
    inputs = torch.rand(input_shapes, dtype=torch.bfloat16)
    result_before = m.forward(inputs)

    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True

    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)

    result_after = m.forward(inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.slice) == 1

    # Check inference result
    assert_with_pcc(result_before, result_after, pcc=0.99)

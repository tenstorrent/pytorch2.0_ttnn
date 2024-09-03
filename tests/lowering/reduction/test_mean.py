import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class MeanModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        return torch.mean(*args, **kwargs)


@pytest.mark.parametrize(
    "input_shape, dim",
    [((1, 32, 32), -1)],
)
def test_mean_dim(device, input_shape, dim):
    m = MeanModule()
    input = torch.zeros(input_shape, dtype=torch.bfloat16).uniform_(-1, 1)
    result_before = m.forward(input, dim, keepdim=True)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, dim, keepdim=True)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.mean) == 1
    # Check inference result
    assert_with_pcc(result_before, result_after)

import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class ArgmaxDimModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, dim, keepdim=False):
        return torch.argmax(input, dim, keepdim=keepdim)


@pytest.mark.parametrize(
    "input_shape, dim",
    [((1, 32, 32), -1)],
)
def test_argmax_dim(device, input_shape, dim):
    m = ArgmaxDimModule()
    input = torch.zeros(input_shape, dtype=torch.bfloat16).uniform_(-1, 1)
    keepdim = True
    result_before = m.forward(input, dim, keepdim)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, dim, keepdim)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has been rewritten and contains ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.argmax) == 1
    # Check inference result
    assert_with_pcc(result_before, result_after)

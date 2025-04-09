import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class SumDimModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, dim, keepdim=False):
        return torch.sum(input, dim, keepdim=keepdim)


@pytest.mark.parametrize(
    "input_shape, dim",
    (
        ((1, 32, 32), (-1, -2)),
        ((1, 1, 768), (0, 1)),
        ((1, 1000), (0,)),
        ((1, 1024, 256), (0, 1)),
        ((1, 1024, 7, 7), (2, 3)),
        ((1, 12, 16), (1,)),
        ((1, 12, 16), (2,)),
        ((1, 512), (1,)),
        ((1, 64), (0,)),
        ((1024, 160), (0,)),
        ((1024, 640), (0,)),
        ((14, 2048), (0,)),
        ((14, 512), (0,)),
        ((16384, 128), (0,)),
        ((16384, 32), (0,)),
        ((197, 1024), (0,)),
        ((197, 3072), (0,)),
        ((197, 4096), (0,)),
        ((197, 768), (0,)),
        ((2, 512), (1,)),
        ((2, 7, 512), (0,)),
        ((50, 768), (0,)),
        ((768, 196), (0,)),
    ),
)
def test_sum_dim(device, input_shape, dim):
    m = SumDimModule()
    input = torch.empty(input_shape, dtype=torch.bfloat16).uniform_(-1, 1)
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
    trivial = all(input_shape[n] == 1 for n in dim)
    assert [node.target for node in nodes].count(ttnn.sum) >= (not trivial)
    # Check inference result
    assert_with_pcc(result_before, result_after)

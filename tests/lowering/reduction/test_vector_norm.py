import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class VectorNormModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, ord, dim, keepdim=False):
        return torch.linalg.vector_norm(input, ord, dim, keepdim)


@pytest.mark.parametrize(
    "input_shape, ord, dim",
    (
        ((1, 24, 64, 32), 2, -1),
        pytest.param((1, 32, 64, 32), 2, 2, marks=pytest.mark.xfail(reason="Known PCC failure, tt-metal#16335")),
        pytest.param((1, 512, 38, 38), 2, 1, marks=pytest.mark.xfail(reason="Known PCC failure, tt-metal#16335")),
        ((1, 512), 2, -1),
        ((16, 6, 64, 32), 2, -1),
        ((16, 8, 64, 32), 2, -1),
        ((2, 512), 2, -1),
        ((4, 12, 64, 32), 2, -1),
        ((4, 16, 64, 32), 2, -1),
        ((64, 3, 64, 32), 2, -1),
        ((64, 4, 64, 32), 2, -1),
    ),
)
def test_vector_norm(device, input_shape, ord, dim):
    m = VectorNormModule()
    input = torch.zeros(input_shape, dtype=torch.bfloat16).uniform_(-1, 1)
    keepdim = True
    result_before = m.forward(input, ord, dim, keepdim)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, ord, dim, keepdim)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = [node.target for node in option._out_fx_graphs[0].nodes]
    assert torch.ops.aten.linalg_vector_norm.default not in nodes
    assert nodes.count(ttnn.moreh_norm) == 1
    # Check inference result
    assert_with_pcc(result_before, result_after)

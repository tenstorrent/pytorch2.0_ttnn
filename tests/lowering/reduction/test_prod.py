import torch
import torch_ttnn
import pytest
import ttnn


class ProdDimIntModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, dim, keep_dim):
        return torch.prod(input, dim, keep_dim)


@pytest.mark.parametrize(
    "input_shape, dim, keep_dim",
    [
        ((1, 2, 32, 32), 3, True),
        ((1, 1, 32, 32), 2, True),
        ((1, 2, 32, 32), 1, True),
        ((2, 1, 32, 32), 0, True),
        ((2, 1, 32, 32), 0, True),
        pytest.param(
            (1, 1, 2, 32, 32), -1, True, marks=pytest.mark.xfail(reason="Unexpected output shape [1, 1, 2, 1] (#244)")
        ),
        pytest.param((1, 2, 32, 32), 3, False, marks=pytest.mark.xfail(reason="Not support keep_dim = False (#244)")),
        pytest.param(
            (1, 1, 1, 32, 32),
            4,
            True,
            marks=pytest.mark.xfail(
                reason='dim >= -4 && dim <= 3 && "Dimension out of range (expected to be in range of [-4, 3]" (#244)'
            ),
        ),
        pytest.param(
            (1, 1, 32, 16), -1, True, marks=pytest.mark.xfail(reason="Need to pad with 1.0 instead of 0 (#244)")
        ),
        pytest.param((32, 32), 1, True, marks=pytest.mark.xfail(reason="Input rank can't < 4")),
    ],
)
def test_prod_dim_int(device, input_shape, dim, keep_dim):
    m = ProdDimIntModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16) + 0.5
    result_before = m.forward(input, dim, keep_dim)

    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, dim, keep_dim)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.prod) == 1
    # Check inference result
    assert result_before.shape == result_after.shape
    # Give higher tolerance for product as it's not associative with float
    assert torch.allclose(result_before, result_after, rtol=0.1)

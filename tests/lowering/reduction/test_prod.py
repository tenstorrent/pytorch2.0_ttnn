import torch
import torch_ttnn
import pytest
import ttnn


class ProdDimModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, dim, keep_dim):
        return torch.prod(input, dim, keep_dim)


@pytest.mark.parametrize(
    "input_shape, dim, keep_dim",
    [
        ((1, 2, 32, 32), -1, True),
        # ((1, 2, 32, 32), -1, False), # Not support keep_dim = False
        ((1, 1, 32, 32), 2, True),
        ((1, 2, 32, 32), 1, True),
        ((2, 1, 32, 32), 0, True),
        # ((2, 1, 1, 32, 32), -1, True), # Output size cannot fit input with offset
        # ((1, 1, 32, 16), -1, True), # Need 1.0 padding
        # ((1, 1, 16, 32), -1, True), # Need to crop
        # ((32, 32), -1, True), # Need 4d shape
    ],
)
def test_prod_dim(device, input_shape, dim, keep_dim):
    m = ProdDimModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16) + 0.5
    result_before = m.forward(input, dim, keep_dim)

    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, dim, keep_dim)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten
    nodes = list(option._out_fx_graphs[0].nodes)
    # There should be no op
    assert [node.target for node in nodes].count(ttnn.prod) == 1
    # Check inference result
    assert result_before.shape == result_after.shape
    # Give higher tolerance for product as it's not associative with float
    assert torch.allclose(result_before, result_after, rtol=0.1)

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
    "input_shape, dim, keep_dim, converted",
    [
        ((1, 2, 32, 32), 3, True, True),
        ((1, 1, 32, 32), 2, True, True),
        ((1, 2, 32, 32), 1, True, True),
        ((2, 1, 32, 32), 0, True, True),
        ((2, 1, 32, 32), 0, True, True),
        # TODO(TODO): Cannot get the device from a tensor with host storage
        ((1, 1, 1, 32, 32), 3, True, False),
        # TODO(TODO): Not support keep_dim = False
        ((1, 2, 32, 32), 3, False, False),
        # TODO(TODO): dim >= -4 && dim <= 3 && "Dimension out of range (expected to be in range of [-4, 3]
        ((1, 1, 1, 32, 32), 4, True, False),
        # TODO(TODO): Need to pad with 1.0 instead of 0
        ((1, 1, 32, 16), -1, True, False),
        # TODO(TODO): Need 4d shape
        ((32, 32), 1, True, False),
    ],
)
def test_prod_dim(device, input_shape, dim, keep_dim, converted):
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
    assert [node.target for node in nodes].count(ttnn.prod) == (1 if converted else 0)
    # Check inference result
    assert result_before.shape == result_after.shape
    # Give higher tolerance for product as it's not associative with float
    assert torch.allclose(result_before, result_after, rtol=0.1)

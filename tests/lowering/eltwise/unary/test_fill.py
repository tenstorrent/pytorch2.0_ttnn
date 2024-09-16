import pytest
import torch
import torch_ttnn
import ttnn


class FillScalarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, value):
        return torch.fill(input, value)


@pytest.mark.parametrize(
    "input_shape, value, converted",
    [
        ((32, 32), 0.5, True),
        ((32, 1), 114, True),
        ((1, 32), 120, True),
        ((4, 4), 32, True),
        ((1, 2, 100, 100), 16, True),
        ((1, 1, 1, 1), 61, True),
        ((2, 1, 1, 1), 64, True),
        ((1, 1, 2, 1), 8, True),
        ((1, 1, 1, 2, 2), 1.0, True),
        ((64,), 1.0, True),
        # Unsupported: scalar
        ((), 1.0, False),
    ],
)
def test_fill_scalar(device, input_shape, value, converted):
    m = FillScalarModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input, value)

    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, value)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contains ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.full) == (1 if converted else 0)
    # Check inference result
    assert torch.allclose(result_before, result_after)

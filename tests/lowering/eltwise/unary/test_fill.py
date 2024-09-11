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
    "input_shape",
    [
        (64,),
        (32, 32),
        (1, 64, 32),
        (2, 32, 64),
        (32, 1),
        (1, 32),
    ],
)
def test_fill_scalar(device, input_shape):
    m = FillScalarModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    value = 0.125
    result_before = m.forward(input, value)

    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, value)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contains ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    # Currently only tensor sizes divisible by 32x32 are converted.
    if len(input_shape) > 1 and input_shape[-1] % ttnn.TILE_SIZE == 0 and input_shape[-2] % ttnn.TILE_SIZE == 0:
        assert [node.target for node in nodes].count(ttnn.full) == 1
    else:
        assert [node.target for node in nodes].count(ttnn.full) == 0
    # Check inference result
    assert torch.allclose(result_before, result_after)

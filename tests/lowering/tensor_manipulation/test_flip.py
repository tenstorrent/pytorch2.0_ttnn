import torch
import torch_ttnn
import pytest
import ttnn


class FlipModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, dims):
        return torch.flip(input, dims)


@pytest.mark.parametrize(
    "input_shape, dims",
    (
        ((1, 32, 16), (0,)),
        ((1, 32, 16), (1,)),
        ((1, 32, 16), (2,)),
        ((1, 32, 16), (0, 1)),
        ((1, 32, 16), (0, 2)),
        ((1, 32, 16), (1, 2)),
    ),
)
def test_flip(device, input_shape, dims):
    m = FlipModule()
    input_tensor = torch.randn(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input_tensor, dims)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input_tensor, dims)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has been rewritten and contains ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.slice) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after)
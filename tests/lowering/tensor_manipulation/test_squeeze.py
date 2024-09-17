import torch
import torch_ttnn
import pytest
import ttnn


class SqueezeDimModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, dim):
        return torch.squeeze(input, dim)


@pytest.mark.parametrize(
    "input_shapes, dim",
    (
        ((1, 32, 16), 0),
        ((1, 256, 1), 2),
    ),
)
def test_squeeze_dim(device, input_shapes, dim):
    m = SqueezeDimModule()
    inputs = [torch.zeros(input_shapes, dtype=torch.bfloat16)]
    result_before = m.forward(inputs[0], dim)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(inputs[0], dim)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    if dim == 0:
        assert [node.target for node in nodes].count(ttnn.squeeze) == 1
    else:
        assert [node.target for node in nodes].count(ttnn.reshape) == 1
    # Check inference result
    print(f"torch result shape: {result_before.shape}\nttnn result shape: {result_after.shape}")
    assert torch.allclose(result_before, result_after)

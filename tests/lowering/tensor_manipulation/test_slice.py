import torch
import torch_ttnn
import pytest
import ttnn


class SliceModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, start, end):
        return input[:, :, start:end]


@pytest.mark.parametrize(
    "input_shape, start, end",
    (
        ((1, 4, 16, 32), 0, 8),
        ((1, 4, 16, 32), 4, 12),
        ((1, 4, 16, 32), 8, 16),
    ),
)
def test_slice(device, input_shape, start, end):
    m = SliceModule()
    input_tensor = torch.randn(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input_tensor, start, end)
    option = torch_ttnn.TorchTtnnOption(device=device)
    # option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input_tensor, start, end)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has been rewritten and contains ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.slice) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after)

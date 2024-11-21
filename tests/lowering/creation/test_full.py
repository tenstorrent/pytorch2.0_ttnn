import torch
import torch_ttnn
import pytest
import ttnn


class FullModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, size, fill_value):
        return torch.full(size, fill_value)


@pytest.mark.parametrize(
    "input_shapes",
    [[(64, 128)]],
)
def test_full(device, input_shapes):
    m = FullModule()
    fill_value = 1.23
    result_before = m.forward(input_shapes[0], fill_value).to(torch.bfloat16)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input_shapes[0], fill_value).to(torch.bfloat16)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.full) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after)

import torch
import torch_ttnn
import pytest
import ttnn


class AddModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return x + x


@pytest.mark.parametrize(
    "input_shapes",
    [
        [(4, 4)],
    ],
)
def test_add(device, input_shapes):
    m = AddModule()
    inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs)
    assert 1 == len(option._out_fx_graphs)
    option._out_fx_graphs[0].print_tabular()
    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.add) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after)

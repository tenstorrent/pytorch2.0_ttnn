import torch
import torch_ttnn
import pytest
import ttnn


class OnesModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, shape):
        return torch.ones(shape)


@pytest.mark.parametrize(
    "input_shapes",
    [(32, 32)],
)
def test_ones(device, input_shapes):
    m = OnesModule()
    result_before = m.forward(input_shapes)
    result_before = result_before.to(torch.bfloat16)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input_shapes)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.ones) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after)

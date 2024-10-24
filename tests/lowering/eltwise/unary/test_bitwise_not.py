import torch
import torch_ttnn
import pytest
import ttnn


class BitwiseNotModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input):
        return torch.bitwise_not(input)


@pytest.mark.parametrize(
    "input_shape",
    [(4, 4)],
)
def test_bitwise_not(device, input_shape):
    m = BitwiseNotModule()
    input = torch.randint(-256, 256, input_shape, dtype=torch.int32)
    result_before = m.forward(input)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has been rewritten and contains ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.bitwise_not) == 1
    # Check inference result
    assert torch.equal(result_before, result_after)

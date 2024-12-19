import torch
import torch_ttnn
import pytest
import ttnn


class LogSoftmaxModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, dim):
        return torch.ops.aten._log_softmax.default(x, dim, 0)


@pytest.mark.parametrize(
    ("input_shape", "dim"),
    [((4, 4), 0), ((15, 15), 1), ((1, 1), 0), ((2, 2), 1), ((17, 17), 0), ((10, 10), 1)],
)
def test_aten_log_softmax(device, input_shape, dim):
    m = LogSoftmaxModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input, dim)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, dim)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.log) == 1
    assert [node.target for node in nodes].count(ttnn.softmax) == 1

    # Check inference result
    assert torch.allclose(result_before, result_after, rtol=0.1, atol=0.1)

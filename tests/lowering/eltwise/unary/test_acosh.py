import torch
import torch_ttnn
import pytest
import ttnn


class AcoshModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.acosh(x)


@pytest.mark.parametrize(
    ("input_shape", "init_offset"),
    [((4, 4), 1)],
)
def test_acosh(device, input_shape, init_offset):
    m = AcoshModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16) + init_offset
    result_before = m.forward(input)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.acosh) == 1

    # Check inference result
    assert torch.allclose(result_before, result_after, rtol=0.2)

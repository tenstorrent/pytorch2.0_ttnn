import pytest
import torch
import torch_ttnn
import ttnn


class ClampTensorModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, min_tensor, max_tensor):
        return torch.clamp(input, min_tensor, max_tensor)


@pytest.mark.parametrize(
    "input_shape",
    [pytest.param((16, 32), marks=pytest.mark.xfail(reason="ttnn.clip doesn't support min/max tensor (#172)"))],
)
def test_clamp_tensor(device, input_shape):
    m = ClampTensorModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    min_tensor = torch.rand(input_shape, dtype=torch.bfloat16)
    max_tensor = torch.rand(input_shape, dtype=torch.bfloat16)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    result_before = m.forward(input, min_tensor, max_tensor)

    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True)
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, min_tensor, max_tensor)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contains ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.clip) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after)

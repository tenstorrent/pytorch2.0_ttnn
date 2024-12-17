import torch
import torch_ttnn
import pytest


class FullLikeModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, tensor, fill_value):
        return torch.full_like(tensor, fill_value)


@pytest.mark.parametrize(
    "input_shape",
    [
        (64, 128),
        (15, 15),
        (1, 1),
        (2, 2),
        (17, 17),
    ],
)
def test_full_like(device, input_shape):
    m = FullLikeModule()
    fill_value = 1.23
    tensor = torch.zeros(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(tensor, fill_value)
    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(tensor, fill_value)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    # Check the graph has be rewritten and aten ops are replaced
    assert not any(node.target == torch.ops.aten.full_like.default for node in nodes)
    # Check inference result
    assert torch.allclose(result_before, result_after)

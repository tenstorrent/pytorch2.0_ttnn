import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class AllModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input):
        return torch.all(input)


@pytest.mark.parametrize(
    "input_shape",
    [
        (1, 32, 32),
        (1, 32),
        (1, 7),
        (1,),
    ],
)
def test_mean_dim(device, input_shape):
    m = AllModule()
    input = torch.randint(-10, 10, input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input)
    option = torch_ttnn.TorchTtnnOption(device=device)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert nodes.count(torch.ops.aten.all.default) == 0

    # Check inference result
    assert_with_pcc(result_before, result_after)

import torch
import torch_ttnn
import pytest
import ttnn
from tests.utils import assert_with_pcc


class CeilModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.ceil(x)


@pytest.mark.skip_platform("grayskull")
@pytest.mark.parametrize(
    "input_shape",
    (
        (1066,),
        (120,),
        (128,),
        (160,),
        (1, 1066),
        (4, 4),
        (4, 32),
    ),
)
def test_ceil(device, input_shape):
    m = CeilModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16) * 20 - 10
    result_before = m.forward(input)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has been rewritten and contains ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.ceil) == 1

    # Check inference result
    assert_with_pcc(result_before, result_after)

import torch
import torch_ttnn
import pytest
import ttnn


class SqrtModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.sqrt(x)


@pytest.mark.parametrize(
    "input_shape",
    ((4, 4), (1066,)),
)
def test_sqrt(device, input_shape):
    m = SqrtModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.sqrt) == 1

    # Check inference result
    from tests.utils import assert_with_pcc

    assert_with_pcc(result_before, result_after)

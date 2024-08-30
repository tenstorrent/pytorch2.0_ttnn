import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class Conv2dModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        return torch.nn.functional.conv2d(*args, **kwargs)


@pytest.mark.parametrize(
    "input_shapes",
    [((1, 2, 5, 5), (4, 2, 3, 3))],
)
def test_conv_2d(device, input_shapes):
    m = Conv2dModule()
    inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    # ttnn operates on channels-last tensors
    result_after = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.conv2d) == 1
    # Check inference result
    assert_with_pcc(result_before, result_after, pcc=0.95)

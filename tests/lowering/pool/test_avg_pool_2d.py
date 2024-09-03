import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class AvgPool2dModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        return torch.nn.functional.avg_pool2d(*args, **kwargs)


@pytest.mark.parametrize(
    "input_shape, kernel_size",
    [((1, 4, 7, 7), (3, 3))],
)
def test_avg_pool_2d(device, input_shape, kernel_size):
    m = AvgPool2dModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input, kernel_size)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    # ttnn operates on channels-last tensors
    input_tensor = torch.permute(input, (0, 2, 3, 1))
    result_after = m.forward(input_tensor, kernel_size)
    result_after = torch.permute(result_after, (0, 3, 1, 2))
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.avg_pool2d) == 1
    # Check inference result
    assert_with_pcc(result_before, result_after, pcc=0.99)

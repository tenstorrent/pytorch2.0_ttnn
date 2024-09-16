import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class MaxPool2dModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        return torch.nn.functional.max_pool2d(*args, **kwargs, stride=2)


@pytest.mark.parametrize(
    "input_shapes, kernel_size",
    [((1, 16, 64, 64), (3, 3))],
)
def test_max_pool_2d_plain(device, input_shapes, kernel_size):
    m = MaxPool2dModule()
    input_tensor = torch.rand(input_shapes, dtype=torch.bfloat16)
    result_before = m.forward(input_tensor, kernel_size)
    option = torch_ttnn.TorchTtnnOption(device=device)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    # ttnn operates on channels-last tensors
    result_after = m.forward(input_tensor, kernel_size)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.max_pool2d) == 1
    # Check inference result
    assert_with_pcc(result_before, result_after, pcc=0.99)


@pytest.mark.xfail(reason="We don't support returning indices from max_pool2d yet")
@pytest.mark.parametrize(
    "input_shapes, kernel_size",
    [((1, 3, 64, 64), (3, 3))],
)
def test_max_pool_2d_with_indices(device, input_shapes, kernel_size):
    m = MaxPool2dModule()
    input_tensor = torch.rand(input_shapes, dtype=torch.bfloat16)
    (pool_before, argmax_before) = m.forward(input_tensor, kernel_size, return_indices=True)
    option = torch_ttnn.TorchTtnnOption(device=device)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    # ttnn operates on channels-last tensors
    (pool_after, argmax_after) = m.forward(input_tensor, kernel_size, return_indices=True)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.max_pool2d) == 1
    # Check inference result
    assert_with_pcc(pool_before, pool_after, pcc=0.99)
    assert_with_pcc(argmax_before, argmax_after)

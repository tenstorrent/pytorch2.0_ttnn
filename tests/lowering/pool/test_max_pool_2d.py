import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class MaxPool2dModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        return torch.nn.functional.max_pool2d(*args, **kwargs)


@pytest.mark.xfail(reason="We don't support returning indices from max_pool2d yet")
@pytest.mark.parametrize(
    "input_shapes, kernel_size, stride, padding, dilation",
    (
        ((1, 1024, 17, 17), (3, 3), 2, 0, 1),
        ((1, 128, 112, 112), (2, 2), 2, 0, 1),
        ((1, 192, 28, 28), (3, 3), 1, 1, 1),  # ceil_mode=True?
        ((1, 512, 19, 19), (3, 3), 1, 1, 1),
    ),
)
def test_max_pool_2d_plain(device, input_shapes, kernel_size, stride, padding, dilation):
    m = MaxPool2dModule()
    input_tensor = torch.rand(input_shapes, dtype=torch.bfloat16)
    result_before = m.forward(input_tensor, kernel_size, stride, padding, dilation)
    option = torch_ttnn.TorchTtnnOption(device=device)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    # ttnn operates on channels-last tensors
    result_after = m.forward(input_tensor, kernel_size, stride, padding, dilation)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.max_pool2d) == 1
    # Check inference result
    assert_with_pcc(result_before, result_after, pcc=0.99)


@pytest.mark.parametrize(
    "input_shapes, kernel_size",
    [((1, 3, 64, 64), (3, 3))],
)
def test_max_pool_2d_with_indices(device, input_shapes, kernel_size):
    m = MaxPool2dModule()
    inputs = torch.rand(input_shapes, dtype=torch.bfloat16)
    (pool_before, argmax_before) = m.forward(inputs, kernel_size, return_indices=True)
    option = torch_ttnn.TorchTtnnOption(device=device)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    # ttnn operates on channels-last tensors
    input_tensor = torch.permute(inputs, (0, 2, 3, 1))
    (pool_after, argmax_after) = m.forward(input_tensor, kernel_size, return_indices=True)
    pool_after = torch.permute(pool_after, (0, 3, 1, 2))
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.max_pool2d) == 1
    # Check inference result
    assert_with_pcc(pool_before, pool_after, pcc=0.99)
    assert_with_pcc(argmax_before, argmax_after)

import torch
import torch_ttnn
import pytest

from tests.utils import assert_with_pcc


class MaxPool2dModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        return torch.nn.functional.max_pool2d(*args, **kwargs)


@pytest.mark.parametrize(
    "input_shapes, kernel_size, stride, padding, dilation, ceil_mode",
    (
        ((1, 1024, 17, 17), (3, 3), 2, 0, 1, False),
        ((1, 128, 112, 112), (2, 2), 2, 0, 1, False),
        ((1, 512, 19, 19), (3, 3), 1, 1, 1, False),
        ((1, 192, 28, 28), (3, 3), 1, 1, 1, False),
        pytest.param(
            (1, 320, 28, 28),
            (3, 3),
            1,
            1,
            1,
            False,
            marks=pytest.mark.xfail(reason="wide channel not divisible by TILE_SIZE * 8 (tt-metal#13901)"),
        ),
        pytest.param(
            (1, 256, 28, 28),
            (3, 3),
            1,
            1,
            1,
            True,
            marks=pytest.mark.xfail(reason="ceil_mode=True is not supported yet (tt-metal#14976)"),
        ),
        pytest.param(
            (1, 64, 360, 640),
            (3, 3),
            2,
            1,
            1,
            False,
            marks=pytest.mark.xfail(reason="OOM (#385)"),
        ),
        pytest.param(
            (1, 4, 14, 14),
            (2, 2),
            2,
            1,
            1,
            False,
            marks=pytest.mark.xfail(reason="channel size is not aligned to L1 page size (#419)"),
        ),
        pytest.param(
            (1, 8, 14, 14),
            (2, 2),
            2,
            1,
            1,
            False,
            marks=pytest.mark.xfail(reason="unknown error (#419)"),
        ),
    ),
)
def test_max_pool_2d_plain(device, input_shapes, kernel_size, stride, padding, dilation, ceil_mode):
    m = MaxPool2dModule()
    input_tensor = torch.rand(input_shapes, dtype=torch.bfloat16)
    result_before = m.forward(input_tensor, kernel_size, stride, padding, dilation, ceil_mode)
    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input_tensor, kernel_size, stride, padding, dilation, ceil_mode)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    # Check the graph has be rewritten and aten ops are replaced
    assert not any(node.target == torch.ops.aten.max_pool2d_with_indices.default for node in nodes)
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
    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    (pool_after, argmax_after) = m.forward(input_tensor, kernel_size, return_indices=True)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    # Check the graph has be rewritten and aten ops are replaced
    assert not any(node.target == torch.ops.aten.max_pool2d_with_indices.default for node in nodes)
    # Check inference result
    assert_with_pcc(pool_before, pool_after, pcc=0.99)
    assert_with_pcc(argmax_before, argmax_after)

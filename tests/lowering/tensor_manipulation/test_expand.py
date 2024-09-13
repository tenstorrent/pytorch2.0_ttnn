import torch
import torch_ttnn
import pytest
import ttnn
from torch_ttnn.utils import TtnnRowMajorLayout, TtnnTileLayout
from torch_ttnn import target_wrappers


class ExpandModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, new_shape):
        return x.expand(new_shape)


ALIGNMENT = pytest.mark.xfail(
    reason="Current repeat implementation requires aligned last dim when repeating on last dim"
)


PAGE_SIZE = pytest.mark.xfail(reason="For interleaved-buffers page size should be divisible by buffer size")


@pytest.mark.parametrize(
    "input_shape, new_shape",
    (
        pytest.param((1, 1, 1, 16, 1), (1, 1, 1, 16, 2), marks=ALIGNMENT),
        ((1, 1, 1, 16), (1, 12, 16, 16)),
        pytest.param((1, 1, 1, 19), (1, 1, 19, 19), marks=PAGE_SIZE),
        ((1, 1, 1, 24), (1, 1, 1, 24)),
        ((1, 1, 1, 24), (1, 1, 24, 24)),
        ((1, 1, 1, 32), (1, 1, 32, 32)),
        pytest.param((1, 1, 1, 45), (1, 1, 45, 45), marks=PAGE_SIZE),
        ((1, 1, 1, 46), (1, 1, 1, 46)),
        ((1, 1, 1024), (1, -1, -1)),
        ((1, 1, 12, 16, 2), (1, 1, -1, -1, -1)),
        pytest.param((1, 1, 7, 7), (2, 1, 7, 7), marks=PAGE_SIZE),
    ),
)
def test_expand(device, input_shape, new_shape):
    m = ExpandModule()
    tensor = torch.rand(input_shape, dtype=torch.bfloat16)
    inputs = [tensor, new_shape]
    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    target = [node.target for node in nodes]
    non_trivial = input_shape != result_before.shape
    assert target.count(target_wrappers.repeat) == non_trivial
    # Check inference result
    assert torch.allclose(result_before, result_after, rtol=0.2)

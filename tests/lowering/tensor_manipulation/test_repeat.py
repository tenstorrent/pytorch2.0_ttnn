import numpy as np
import pytest
import torch
import ttnn
import torch_ttnn


class RepeatModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, sizes):
        return x.repeat(sizes)


@pytest.mark.parametrize(
    "input_shape, sizes",
    (
        ((1, 1, 1), (1, 1, 1)),
        ((1, 1, 2048, 2048), (1, 1, 1, 1)),
        ((1, 1, 256), (1, 1, 1)),
        ((1, 50, 256), (1, 1, 1)),
        ((100, 1, 256), (1, 1, 1)),
        ((4, 2), (1, 1)),
        ((4, 2), (1444, 1)),
        ((4, 2), (9, 1)),
        ((6, 2), (1, 1)),
        ((6, 2), (100, 1)),
        ((6, 2), (25, 1)),
        ((6, 2), (361, 1)),
        ((6, 2), (4, 1)),
        ((6, 2), (400, 1)),
        ((6, 2), (9, 1)),
        pytest.param(
            (4, 4),
            (3, 2),
            marks=pytest.mark.xfail(
                reason="Current repeat implementation requires aligned last dim when repeating on last dim"
            ),
        ),
        ((5, 16), (2, 3)),
    ),
)
def test_repeat(device, input_shape, sizes):
    m = RepeatModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input, sizes)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, sizes)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    non_trivial = np.prod(sizes) != 1
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(torch_ttnn.target_wrappers.repeat) == non_trivial

    # Check inference result
    assert torch.allclose(result_before, result_after)

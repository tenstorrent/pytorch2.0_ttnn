import torch
import torch_ttnn
import pytest
import ttnn
from tests.utils import assert_with_pcc


class MulModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, y):
        return torch.mul(x, y)


@pytest.mark.parametrize(
    "input_shapes",
    (
        ((32, 32), (32, 32)),
        ((64,), (32, 64)),
        ((64, 32), (64, 1)),
        pytest.param(
            ((64, 1), (1, 64)),
            marks=pytest.mark.xfail(reason="broadcasting issues (tt-metal#12852)"),
        ),
        pytest.param(
            ((16, 1), (1, 1, 32)),
            marks=pytest.mark.xfail(reason="broadcasting issues (tt-metal#12852, tt-metal#15808)"),
        ),
        ((1, 64, 30, 40), (1, 1, 30, 40)),
        ((1, 64, 60, 80), (1, 1, 60, 80)),
        ((1, 64, 120, 160), (1, 1, 120, 160)),
        ((0, 1), (0, 1)),
        pytest.param(
            ((1, 71, 7, 64), (1, 1, 7, 64)),
            marks=pytest.mark.xfail(reason="broadcasting issues (tt-metal#15808)"),
        ),
        pytest.param(
            ((64, 3, 64, 64), (3, 1, 1)),
            marks=pytest.mark.xfail(reason="broadcasting issues (tt-metal#15808)"),
        ),
        pytest.param(
            ((16, 6, 64, 64), (6, 1, 1)),
            marks=pytest.mark.xfail(reason="broadcasting issues (tt-metal#15808)"),
        ),
        pytest.param(
            ((4, 12, 64, 64), (12, 1, 1)),
            marks=pytest.mark.xfail(reason="broadcasting issues (tt-metal#15808)"),
        ),
        pytest.param(
            ((64, 4, 64, 64), (4, 1, 1)),
            marks=pytest.mark.xfail(reason="broadcasting issues (tt-metal#15808)"),
        ),
        pytest.param(
            ((16, 8, 64, 64), (8, 1, 1)),
            marks=pytest.mark.xfail(reason="broadcasting issues (tt-metal#15808)"),
        ),
        pytest.param(
            ((4, 16, 64, 64), (16, 1, 1)),
            marks=pytest.mark.xfail(reason="broadcasting issues (tt-metal#15808)"),
        ),
    ),
)
def test_mul(device, input_shapes):
    m = MulModule()
    inputs = [torch.randint(1, 5, shape).type(torch.bfloat16) for shape in input_shapes]
    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    targets = [node.target for node in option._out_fx_graphs[0].nodes]
    assert targets.count(ttnn.mul) == 1

    # Check inference result
    assert_with_pcc(result_before, result_after)

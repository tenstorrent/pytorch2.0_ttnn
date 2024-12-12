import torch
import torch_ttnn
import pytest
import ttnn
from tests.utils import assert_with_pcc


class DivModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, numerator, denominator):
        return torch.div(numerator, denominator)


# ttnn.div does not support broadcasting some combination of shapes. Fallback to reciprocal and multiply.
@pytest.mark.parametrize(
    "input_shapes",
    (
        ((32, 32), (32, 32)),
        ((64,), (32, 64)),
        ((64, 32), (64, 1)),
        pytest.param(
            ((64, 1), (1, 64)),
            marks=pytest.mark.xfail(reason="Bidirectional broadcasting issue (#64)"),
        ),
        pytest.param(
            ((1, 23, 40, 1), (128,)),
            marks=pytest.mark.xfail(reason="Bidirectional broadcasting issue (#64)"),
        ),
        pytest.param(
            ((), ()),
            marks=pytest.mark.xfail(reason="ttnn.div does not handle 0-D tensors (tt-metal#15630)"),
        ),
        pytest.param(
            ((1, 12, 9, 9), ()),
            marks=pytest.mark.xfail(reason="ttnn.div does not handle 0-D tensors (tt-metal#15630)"),
        ),
        pytest.param(
            ((1, 64, 9, 9), ()),
            marks=pytest.mark.xfail(reason="ttnn.div does not handle 0-D tensors (tt-metal#15630)"),
        ),
        pytest.param(
            ((1, 12, 25, 25), ()),
            marks=pytest.mark.xfail(reason="ttnn.div does not handle 0-D tensors (tt-metal#15630)"),
        ),
        pytest.param(
            ((1, 16, 9, 9), ()),
            marks=pytest.mark.xfail(reason="ttnn.div does not handle 0-D tensors (tt-metal#15630)"),
        ),
        pytest.param(
            ((1, 12, 7, 7), ()),
            marks=pytest.mark.xfail(reason="ttnn.div does not handle 0-D tensors (tt-metal#15630)"),
        ),
        pytest.param(
            ((1, 1280, 8, 8), ()),
            marks=pytest.mark.xfail(reason="ttnn.div does not handle 0-D tensors (tt-metal#15630)"),
        ),
        pytest.param(
            ((10, 10), ()),
            marks=pytest.mark.xfail(reason="ttnn.div does not handle 0-D tensors (tt-metal#15630)"),
        ),
        pytest.param(
            ((2, 2), ()),
            marks=pytest.mark.xfail(reason="ttnn.div does not handle 0-D tensors (tt-metal#15630)"),
        ),
        pytest.param(
            ((1, 16, 5, 5), ()),
            marks=pytest.mark.xfail(reason="ttnn.div does not handle 0-D tensors (tt-metal#15630)"),
        ),
        pytest.param(
            ((1, 16, 1, 6), ()),
            marks=pytest.mark.xfail(reason="ttnn.div does not handle 0-D tensors (tt-metal#15630)"),
        ),
        pytest.param(
            ((1, 128, 1568), ()),
            marks=pytest.mark.xfail(reason="ttnn.div does not handle 0-D tensors (tt-metal#15630)"),
        ),
        pytest.param(
            ((1, 64, 6272), ()),
            marks=pytest.mark.xfail(reason="ttnn.div does not handle 0-D tensors (tt-metal#15630)"),
        ),
        pytest.param(
            ((1, 32, 25088), ()),
            marks=pytest.mark.xfail(reason="ttnn.div does not handle 0-D tensors (tt-metal#15630)"),
        ),
        pytest.param(
            ((15, 15), ()),
            marks=pytest.mark.xfail(reason="ttnn.div does not handle 0-D tensors (tt-metal#15630)"),
        ),
        pytest.param(
            ((17, 17), ()),
            marks=pytest.mark.xfail(reason="ttnn.div does not handle 0-D tensors (tt-metal#15630)"),
        ),
    ),
)
def test_div(device, input_shapes):
    m = DivModule()
    inputs = [torch.randint(1, 15, shape).to(torch.bfloat16) for shape in input_shapes]
    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    targets = (*(node.target for node in option._out_fx_graphs[0].nodes),)
    assert torch.ops.aten.div.Tensor not in targets
    assert targets.count(ttnn.mul) + targets.count(ttnn.div) == 1

    # Check inference result
    assert_with_pcc(result_before, result_after)


@pytest.mark.parametrize(
    "input_shape",
    (
        (4, 4),
        (32, 32),
        (1, 197, 1024),
        (1, 1),
        (1, 12, 9, 9),
        (1, 64, 9, 9),
        (1, 12, 25, 25),
        (1, 16, 9, 9),
        (1, 12, 7, 7),
        (1, 1280, 8, 8),
        (10, 10),
        (2, 2),
        (1, 128, 1568),
        (1, 64, 6272),
        (1, 32, 25088),
        (15, 15),
        (17, 17),
    ),
)
def test_div_scalar_denom(device, input_shape):
    m = DivModule()
    input = torch.randint(1, 15, input_shape).to(torch.bfloat16)
    result_before = m.forward(input, 5.0)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, 5.0)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    targets = (*(node.target for node in option._out_fx_graphs[0].nodes),)
    assert torch.ops.aten.div.Scalar not in targets
    assert torch.ops.aten.div.Tensor not in targets
    assert targets.count(ttnn.mul) == 1

    # Check inference result
    assert_with_pcc(result_before, result_after)

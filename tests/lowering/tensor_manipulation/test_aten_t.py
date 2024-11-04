import torch
import torch_ttnn
import pytest

from tests.utils import assert_with_pcc


class AtenTModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.t(x)


def _t(device, input_shapes):
    m = AtenTModule()
    inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check inference result
    assert_with_pcc(result_before, result_after)

    # Return nodes
    return list(option._out_fx_graphs[0].nodes)


@pytest.mark.parametrize(
    "input_shapes",
    [
        [(1, 32)],
        [(1, 3)],
        [(12, 3)],
        [(1, 21843)],
        [(768, 21843)],
        pytest.param((2, 1), marks=pytest.mark.xfail(reason="inner-most dim can't be 1 (#377)")),
        pytest.param((512, 1), marks=pytest.mark.xfail(reason="inner-most dim can't be 1 (#377)")),
    ],
)
def test_aten_t(device, input_shapes):
    nodes = _t(device, input_shapes)
    # Check the graph has be rewritten and aten ops are replaced
    assert not any(node.target == torch.ops.aten.t.default for node in nodes)


@pytest.mark.parametrize(
    "input_shapes",
    [
        [5],
        [(5)],
    ],
)
def test_aten_t_less_2d(device, input_shapes):
    nodes = _t(device, input_shapes)
    # Check the graph has be rewritten and aten ops are replaced
    assert not any(node.target == torch.ops.aten.t.default for node in nodes)

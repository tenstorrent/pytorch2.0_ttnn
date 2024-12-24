import torch
import torch_ttnn
import pytest

from tests.utils import assert_with_pcc


class TransposeModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, dim0, dim1):
        return torch.transpose(x, dim0, dim1)


@pytest.mark.parametrize(
    "input_shape, dim0, dim1",
    [
        ((32,), 0, 0),
        ((5, 3, 2), 0, 2),
        ((5, 3, 1), 0, 2),
        ((5, 3, 1), 1, 2),
        ((5, 3, 1), 0, 1),
        ((1, 3), 0, 1),
        ((3, 1), 1, 0),
        ((1, 197, 1, 3, 1024), 0, -2),
        pytest.param(
            (1, 197, 1, 3, 1024),
            1,
            -2,
            marks=pytest.mark.xfail(reason="transpose rank > 4 issues (#585)"),
        ),
    ],
)
def test_transpose(device, input_shape, dim0, dim1):
    m = TransposeModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    torch_result = m.forward(input, dim0, dim1)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    ttnn_result = m.forward(input, dim0, dim1)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and aten ops are replaced
    nodes = list(option._out_fx_graphs[0].nodes)
    assert not any(node.target == torch.ops.aten.transpose.int for node in nodes)
    # Check inference result
    assert_with_pcc(torch_result, ttnn_result)

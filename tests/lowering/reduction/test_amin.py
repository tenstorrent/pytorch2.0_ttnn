import torch
import torch_ttnn
import pytest
import ttnn


class AminModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, dim, keepdim):
        return torch.amin(input, dim=dim, keepdim=keepdim)


@pytest.mark.parametrize("sign", [1, -1])
@pytest.mark.parametrize(
    "input_shape, dim, keepdim, converted",
    [
        ((32, 32), [], True, True),
        ((16, 32, 32), [], True, True),
        ((16, 32, 32), 1, True, True),
        ((16, 32, 32), [1], True, True),
        ((16, 32, 32), [2], True, True),
        ((16, 32, 32), [1, 2], True, True),
        # TODO(TODO): keepdim = false is not supported
        ((32, 32), [1], False, False),
        # TODO(TODO): Unsupport reduction on < rank - 2 dims
        ((16, 32, 32), [0], True, False),
        ((32, 32, 32), [0, 1, 2], True, False),
        # TODO(TODO): Unexpected output shape (1, 1) instead of (1)
        ((32,), [], True, False),
        # TODO(TODO): Need -inf padding value
        ((1, 32), [], True, False),
        ((32, 1), [], True, False),
        # TODO(TODO): Output reshape inside generic reduction can't handle non-tile-aligned size
        ((1, 32), [1], True, False),
    ],
)
def test_amin(device, sign, input_shape, dim, keepdim, converted):
    m = AminModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16) * sign
    result_before = m.forward(input, dim, keepdim)

    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, dim, keepdim)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten
    nodes = list(option._out_fx_graphs[0].nodes)
    # There should be no op
    assert [node.target for node in nodes].count(ttnn.min) == (1 if converted else 0)
    # Check inference result
    assert result_before.shape == result_after.shape
    assert torch.allclose(result_before, result_after)

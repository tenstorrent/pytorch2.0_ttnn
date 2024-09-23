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
    "input_shape, dim, keepdim",
    [
        ((32, 32), [], True),
        ((16, 32, 32), [], True),
        ((16, 32, 32), 1, True),
        ((16, 32, 32), [1], True),
        ((16, 32, 32), [2], True),
        ((16, 32, 32), [1, 2], True),
        # TODO(#240): keepdim = false is not supported
        pytest.param((32, 32), [1], False, marks=pytest.mark.xfail(reason="keepdim = false is not supported (#240)")),
        # TODO(#240): Not support reduction on < rank - 2 dims
        pytest.param(
            (16, 32, 32), [0], True, marks=pytest.mark.xfail(reason="Not support reduction on < rank - 2 dims (#240)")
        ),
        pytest.param(
            (32, 32, 32),
            [0, 1, 2],
            True,
            marks=pytest.mark.xfail(reason="Not support reduction on < rank - 2 dims (#240)"),
        ),
        # TODO(#240): Unexpected output shape (1, 1) instead of (1)
        pytest.param(
            (32,), [], True, marks=pytest.mark.xfail(reason="Unexpected output shape (1, 1) instead of (1) (#240)")
        ),
        # TODO(#240): Need inf padding value
        pytest.param((1, 32), [], True, marks=pytest.mark.xfail(reason="Need inf padding value (#240)")),
        pytest.param((32, 1), [], True, marks=pytest.mark.xfail(reason="Need inf padding value (#240)")),
        # TODO(#240): Output reshape inside generic reduction can't handle non-tile-aligned size
        pytest.param(
            (1, 32),
            [1],
            True,
            marks=pytest.mark.xfail(
                reason="Output reshape inside generic reduction can't handle non-tile-aligned size (#240)"
            ),
        ),
    ],
)
def test_amin(device, sign, input_shape, dim, keepdim):
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
    assert [node.target for node in nodes].count(ttnn.min) == 1
    # Check inference result
    assert result_before.shape == result_after.shape
    assert torch.allclose(result_before, result_after)

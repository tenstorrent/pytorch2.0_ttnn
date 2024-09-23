import torch
import torch_ttnn
import pytest
import ttnn


class VarModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, dim, keepdim, correction):
        return torch.var(input, dim=dim, keepdim=keepdim, correction=correction)


@pytest.mark.parametrize(
    "input_shape, dim, keepdim, correction",
    [
        ((32, 32), [1], True, 0),
        ((16, 32, 32), [1], True, 0),
        ((16, 32, 32), 1, True, 0),
        ((16, 32, 32), [2], True, 0),
        ((16, 32, 32), [1, 2], True, 0),
        # TODO(#242): Not support correction != 0
        pytest.param((32, 32), [1], True, 1, marks=pytest.mark.xfail(reason="Not support correction != 0 (#240)")),
        # TODO(#242): Unsupported reduction operation
        pytest.param((32, 32), [], True, 0, marks=pytest.mark.xfail(reason="Unsupported reduction operation (#240)")),
        # TODO(#240): keepdim = false is not supported
        pytest.param(
            (32, 32), [1], False, 0, marks=pytest.mark.xfail(reason="keepdim = false is not supported (#240)")
        ),
        # TODO(#240): Not ssupport reduction on < rank - 2 dims
        pytest.param(
            (16, 32, 32),
            [0],
            True,
            0,
            marks=pytest.mark.xfail(reason="Not ssupport reduction on < rank - 2 dims (#240)"),
        ),
        pytest.param(
            (32, 32, 32),
            [0, 1, 2],
            True,
            0,
            marks=pytest.mark.xfail(reason="Not ssupport reduction on < rank - 2 dims (#240)"),
        ),
        # TODO(#240): Unexpected output shape (1, 1) instead of (1)
        pytest.param(
            (32,), [], True, 0, marks=pytest.mark.xfail(reason="Unexpected output shape (1, 1) instead of (1) (#240)")
        ),
        # TODO(#240): Need -inf padding value
        pytest.param((1, 32), [], True, 0, marks=pytest.mark.xfail(reason="Need -inf padding value (#240)")),
        pytest.param((32, 1), [], True, 0, marks=pytest.mark.xfail(reason="Need -inf padding value (#240)")),
        # TODO(#240): Output reshape inside generic reduction can't handle non-tile-aligned size
        pytest.param(
            (1, 32),
            [1],
            True,
            0,
            marks=pytest.mark.xfail(
                reason="Output reshape inside generic reduction can't handle non-tile-aligned size (#240)"
            ),
        ),
    ],
)
def test_var(device, input_shape, dim, keepdim, correction):
    m = VarModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input, dim, keepdim, correction)

    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, dim, keepdim, correction)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.var) == 1
    # Check inference result
    assert result_before.shape == result_after.shape
    # Multiple float multiplications needs higher tolerance
    assert torch.allclose(result_before, result_after, rtol=0.2)

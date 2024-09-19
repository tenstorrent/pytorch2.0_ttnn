import torch
import torch_ttnn
import pytest
import ttnn


class AmaxModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, dim, keepdim):
        return torch.amax(input, dim=dim, keepdim=keepdim)


@pytest.mark.parametrize(
    "input_shape, dim, keepdim",
    [
        # pytest.param((32, 32), [], False, marks=pytest.mark.xfail(reason="keepdim = false not supported (#TODO)")),
        # ((32, 32), [], True),
        # ((16, 32, 32), [0], True),  Output size cannot fit input with offset
        ((16, 32, 32), [1], True),
        ((16, 32, 32), [2], True),
        ((16, 32, 32), [1, 2], True),
        # ((16, 32, 32), [0, 1, 2], True),  Unsupported dim
        ((1, 32), [], True),
        ((32, 1), [], True),
        # ((16,), [], True), assert torch.Size([1]) == torch.Size([1, 1])
        # ((4, 16, 32), [2], True), Unable to reshape a tensor in TILE_LAYOUT to non-tile height and width! Please convert the tensor to ROW_MAJOR_LAYOUT first.
    ],
)
def test_amax(device, input_shape, dim, keepdim):
    m = AmaxModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input, dim, keepdim)

    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, dim, keepdim)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten
    nodes = list(option._out_fx_graphs[0].nodes)
    # There should be no op
    assert [node.target for node in nodes].count(ttnn.max) == 1
    # Check inference result
    assert result_before.shape == result_after.shape
    assert torch.allclose(result_before, result_after)

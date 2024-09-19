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
        # pytest.param((32, 32), [], False, marks=pytest.mark.xfail(reason="keepdim = false not supported (#TODO)")),
        # ((32, 32), [], True, True), # dim = [], Unsupported reduction operation
        ((32, 32), [1], True, 0),
        # ((32, 32), [1], True, 1), # Not support correction
        # ((16, 32, 32), [0], True),  #Output size cannot fit input with offset
        ((16, 32, 32), [1], True, 0),
        ((16, 32, 32), [2], True, 0),
        ((16, 32, 32), [1, 2], True, 0),
        # ((16, 32, 32), [0, 1, 2], True),  Unsupported dim
        # ((1, 32), [], True), 0.0 padding issue
        # ((32, 1), [], True), 0.0 padding issue
        # ((16,), [], True), #assert torch.Size([1]) == torch.Size([1, 1])
        # ((4, 16, 32), [2], True), #Unable to reshape a tensor in TILE_LAYOUT to non-tile height and width! Please convert the tensor to ROW_MAJOR_LAYOUT first.
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
    # There should be no op
    assert [node.target for node in nodes].count(ttnn.var) == 1
    # Check inference result
    assert result_before.shape == result_after.shape
    assert torch.allclose(result_before, result_after, rtol=0.2)

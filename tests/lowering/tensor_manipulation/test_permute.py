import pytest
import torch
import ttnn
import torch_ttnn


class PermuteModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, order):
        return torch.permute(x, order)


@pytest.mark.parametrize(
    "input_shapes",
    [
        [(4, 4)],
    ],
)
def test_permute(device, input_shapes):
    m = PermuteModule()
    inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
    order = (1, 0)
    result_before = m.forward(*inputs, order)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs, order)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.permute) == 1
    # Check shape or result
    assert result_before.size() == result_after.size()
    # Check inference result
    assert torch.allclose(result_before, result_after)


# This tests tests the workaround for issue https://github.com/tenstorrent/tt-metal/issues/11191
@pytest.mark.parametrize(
    "input_shapes",
    [
        [(5, 1, 2)],
    ],
)
def test_permute_missing_dim(device, input_shapes):
    m = PermuteModule()
    inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
    order = (1, 0, 2)
    result_before = m.forward(*inputs, order)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs, order)
    option._out_fx_graphs[0].print_tabular()
    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.permute) == 1
    # Check shape or result
    assert result_before.size() == result_after.size()
    # Check inference result
    assert torch.allclose(result_before, result_after)

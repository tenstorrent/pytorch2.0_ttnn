import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class IndexSelectModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, dim, index):
        return torch.ops.aten.index_select.default(input, dim, index)


@pytest.mark.parametrize(
    "input_shapes, dim, index, converted",
    [
        ((3, 4), 0, [0, 1, 1, 0], "embedding"),  # => index => embedding
        ((3, 4), 1, [0, 1], "index"),
        ((3, 4, 5), 0, [1, 0], "index"),
        ((3, 4, 5), 1, [2, 3], "index"),
    ],
)
def test_index_select(device, input_shapes, dim, index, converted):
    m = IndexSelectModule()
    inputs = torch.rand(input_shapes, dtype=torch.bfloat16)
    index = torch.tensor(index)
    result_before = m.forward(inputs, dim, index)

    option = torch_ttnn.TorchTtnnOption(device=device)
    # option.gen_graphviz = True

    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)

    result_after = m.forward(inputs, dim, index)
    # option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    if converted == "embedding":
        nodes = [node.target for node in option._out_fx_graphs[0].nodes]
        assert torch.ops.aten.index_select.default not in nodes
        assert ttnn.embedding in nodes
    if converted == "index":
        nodes = [node.target for node in option._out_fx_graphs[0].nodes]
        assert torch.ops.aten.index_select.default not in nodes
        assert torch.ops.aten.index.Tensor in nodes

    # Check inference result
    assert_with_pcc(result_before, result_after, pcc=0.99)

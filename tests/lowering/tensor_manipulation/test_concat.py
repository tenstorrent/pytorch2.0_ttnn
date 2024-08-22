import pytest
import torch
import ttnn
import torch_ttnn


class ConcatModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, dim):
        return torch.cat((x1, x2), dim)


@pytest.mark.xfail(reason="lowering issue (#67)")
@pytest.mark.parametrize(
    "input_shapes, dim",
    [
        (((4, 2), (4, 2)), 1),
    ],
)
def test_concat(device, input_shapes, dim):
    m = ConcatModule()
    inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
    result_before = m.forward(*inputs, dim)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs, dim)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.concat) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after)

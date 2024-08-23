import pytest
import torch
import ttnn
import torch_ttnn


class ReshapeModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, new_shape):
        return torch.reshape(x, new_shape)


@pytest.mark.xfail(reason="lowering issue (#67)")
@pytest.mark.parametrize(
    "input_shape, new_shape",
    [((3 * 5, 7), (7 * 3, 5))],
)
def test_reshape(device, input_shape, new_shape):
    m = ReshapeModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input, new_shape)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, new_shape)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.reshape) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after)

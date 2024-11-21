import torch
import torch_ttnn
import pytest
import ttnn


class IfModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        if torch.sum(x) > 0:
            return x + x
        else:
            return torch.matmul(x, x)


@pytest.mark.parametrize(
    "input_shape",
    [(4, 4)],
)
def test_if(device, input_shape):
    m = IfModule()
    inputs_then = [torch.tensor(range(1, 17)).reshape(input_shape).to(torch.bfloat16)]
    inputs_else = [-inputs_then[0]]
    result_before_then = m.forward(*inputs_then)
    result_before_else = m.forward(*inputs_else)
    option = torch_ttnn.TorchTtnnOption(device=device)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after_then = m.forward(*inputs_then)
    result_after_else = m.forward(*inputs_else)

    # After the forward & compilation, there should be total 3 graphs
    assert 3 == len(option._out_fx_graphs)
    option._out_fx_graphs[0].print_tabular()
    # Check the graph has be rewritten and contain ttnn ops
    nodes_0 = list(option._out_fx_graphs[0].nodes)
    target_0 = [node.target for node in nodes_0]
    assert target_0.count(ttnn.sum) == 1
    # This `gt` is not converted yet because its shape does not fit tiled layout
    assert target_0.count(torch.ops.aten.gt.Scalar) == 1
    nodes_1 = list(option._out_fx_graphs[1].nodes)
    target_1 = [node.target for node in nodes_1]
    assert target_1.count(ttnn.add) == 1
    nodes_2 = list(option._out_fx_graphs[2].nodes)
    target_2 = [node.target for node in nodes_2]
    assert target_2.count(ttnn.matmul) == 1

    # Check inference result
    assert torch.allclose(result_before_then, result_after_then)
    assert torch.allclose(result_before_else, result_after_else)

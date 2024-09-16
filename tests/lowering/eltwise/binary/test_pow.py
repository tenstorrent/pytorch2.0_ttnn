import pytest
import torch
import torch_ttnn
import ttnn


class PowModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, exp):
        return input.pow(exp)


@pytest.mark.xfail(reason="missing ttnn.pow support of exponent tensor (#211)")
@pytest.mark.parametrize(
    "input_shape, converted",
    [
        ((32, 32), True),
        ((1, 32), True),
        ((16, 16), True),
        ((16,), True),
        ((1, 2, 3, 6, 4), True),
    ],
)
def test_pow(device, input_shape, converted):
    m = PowModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    exp = torch.rand(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input, exp)

    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, exp)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contains ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.pow) == (1 if converted else 0)
    # Check inference result
    assert torch.allclose(result_before, result_after)

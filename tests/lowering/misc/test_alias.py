import torch
import torch_ttnn
import pytest


class AliasModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.ops.aten.alias.default(x)


@pytest.mark.parametrize(
    "input_shape",
    [(4, 4)],
)
def test_alias(device, input_shape):
    m = AliasModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input)

    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten
    nodes = list(option._out_fx_graphs[0].nodes)
    # There should be no op
    assert [node.op for node in nodes].count("call_function") == 0
    # Check inference result
    assert torch.allclose(result_before, result_after)

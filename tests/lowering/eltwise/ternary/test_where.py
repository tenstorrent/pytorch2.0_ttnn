import torch
import torch_ttnn
import pytest
import ttnn


class WhereModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, cond, then, other):
        return then.where(cond, other)


@pytest.mark.parametrize(
    "input_shapes",
    (
        ((8, 8), (8, 8), (8, 8)),
        ((8, 8), (8, 1), (8, 8)),
        ((8, 8), (8, 1), (1, 8)),
        ((8, 8), (1, 1), (1, 8)),
        pytest.param(
            ((8, 1), (1, 1), (1, 8)),
            marks=pytest.mark.xfail(reason="broadcasting issues (#64)"),
        ),
    ),
)
def test_add(device, input_shapes):
    m = WhereModule()
    inputs = [torch.randint(0, 2, shape).type(torch.bfloat16) for shape in input_shapes]
    inputs[0] = inputs[0].to(torch.bool)
    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.where) == 1

    # Check inference result
    assert torch.allclose(result_before, result_after)

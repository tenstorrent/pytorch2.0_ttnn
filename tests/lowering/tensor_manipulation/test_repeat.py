import pytest
import torch
import ttnn
import torch_ttnn


class RepeatModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, sizes):
        return x.repeat(sizes)


@pytest.mark.xfail(reason="lowering issue (#67)")
@pytest.mark.parametrize(
    "input_shape, sizes",
    [((4, 4), (3, 2))],
)
def test_repeat(device, input_shape, sizes):
    m = RepeatModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input, sizes)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, sizes)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(torch_ttnn.target_wrappers.repeat) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after)

import pytest
import torch
import torch_ttnn
import ttnn


class RemainderModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, mod):
        return input % mod


@pytest.mark.parametrize(
    "input_shape, mod",
    (
        ((32, 32), 7),
        ((1, 32), 3),
        ((16, 16), 5),
        ((4,), 1),
        ((1, 2, 3, 6, 4), 1),
    ),
)
def test_remainder(device, input_shape, mod):
    m = RemainderModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16) * (mod * 3)
    result_before = m.forward(input, mod)
    # print(torch.export.export(m, args=(input, mod)))

    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, mod)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contains ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.remainder) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after)
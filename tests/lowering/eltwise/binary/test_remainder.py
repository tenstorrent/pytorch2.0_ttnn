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
    "input_shapes",
    (
        ((32, 32), (32, 32)),
        ((1, 32), (1, 32)),
        ((16, 16), (16, 16)),
        ((4,), (4,)),
        ((1, 2, 3, 6, 4), (1, 2, 3, 6, 4)),
    ),
)
def test_remainder_tensor(device, input_shapes):
    m = RemainderModule()
    numerator = torch.rand(input_shapes[0], dtype=torch.bfloat16) * 5
    denominator = torch.rand(input_shapes[1], dtype=torch.bfloat16) - 2
    result_before = m.forward(numerator, denominator)
    # print(torch.export.export(m, args=(input, mod)))

    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(numerator, denominator)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contains ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.remainder) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after, 0.99)

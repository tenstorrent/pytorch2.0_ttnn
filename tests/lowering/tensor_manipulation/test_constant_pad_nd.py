import pytest
import torch
import torch_ttnn
import ttnn


class ConstantPadNdModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, pad, value):
        return torch.constant_pad_nd(input, pad, value)


@pytest.mark.parametrize(
    "input_shape, pad, convert",
    [
        ((1, 1, 32, 32), [0, 64, 0, 32, 0, 4], True),
        ((64, 32), [0, 32, 0, 64], True),
        ((1, 1, 32, 32), [0, 32], True),
        ((1, 1, 32, 32), [0, 0, 0, 0], True),
        ((1, 32), [0, 32, 0, 0], True),
        ((16, 16), [0, 16, 0, 0], True),
        ((4,), [0, 16], True),
        [(1, 14, 14, 384), [0, 0, 0, 0, 0, 0], True],
        # Not supported: more than 4 dims
        ((1, 1, 1, 32, 32), [0, 32], False),
        # Not supported: front padding
        ((32, 32), [32, 0, 32, 0], False),
    ],
)
def test_constant_pad_nd(device, input_shape, pad, convert):
    m = ConstantPadNdModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    value = 0.5
    result_before = m.forward(input, pad, value)

    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, pad, value)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contains ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.pad) == (1 if convert else 0)
    # Check inference result
    assert torch.allclose(result_before, result_after)

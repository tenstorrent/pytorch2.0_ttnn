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
    "input_shape, pad",
    [
        ((1, 32, 32), [0, 64, 0, 32]),
        ((64, 32), [0, 32, 0, 64]),
        pytest.param((1, 32), [0, 32, 0, 0], marks=pytest.mark.xfail(reason="output shape incorrect (#176)")),
        pytest.param((16, 16), [0, 16, 0, 0], marks=pytest.mark.xfail(reason="not support layout (#176)")),
        pytest.param((32, 32), [32, 0, 32, 0], marks=pytest.mark.xfail(reason="not support front padding (#176)")),
    ],
)
def test_constant_pad_nd(device, input_shape, pad):
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
    assert [node.target for node in nodes].count(ttnn.pad) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after)

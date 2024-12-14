import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class ArgmaxModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, dim):
        return torch.argmax(input, dim=dim)


@pytest.mark.xfail(reason="argmax issues (#605)")
@pytest.mark.parametrize(
    "input_shapes, dim",
    [
        ((1, 32), None),
    ],
)
def test_select(device, input_shapes, dim):
    m = ArgmaxModule()
    inputs = torch.rand(input_shapes, dtype=torch.bfloat16)
    result_before = m.forward(inputs, dim)

    option = torch_ttnn.TorchTtnnOption(device=device)

    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)

    result_after = m.forward(inputs, dim)
    print(option._out_fx_graphs[0])

    # Check the graph has be rewritten and contain ttnn ops

    # Check inference result
    assert_with_pcc(result_before, result_after, pcc=0.99)

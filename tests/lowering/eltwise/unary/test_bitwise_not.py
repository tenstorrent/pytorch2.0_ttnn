import torch
import torch_ttnn
import pytest
import ttnn


class BitwiseNotModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.bitwise_not(x)


@pytest.mark.parametrize(
    "input_shape, is_bool",
    [
        ((4, 4), True),
        ((4, 4), False),
        ((1, 64, 4), True),
        ((1, 64, 4), False),
    ],
)
def test_relu(device, input_shape, is_bool):
    m = BitwiseNotModule()
    if is_bool:
        input = torch.randint(0, 2, input_shape, dtype=torch.bool)
    else:
        input = torch.randint(-10, 10, input_shape, dtype=torch.int32)

    result_before = m.forward(input)
    option = torch_ttnn.TorchTtnnOption(device=device)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input)
    print(option._out_fx_graphs[0])

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert nodes.count(torch.ops.aten.bitwise_not.default) == 0

    # Check inference result
    assert torch.allclose(result_before, result_after)

import pytest
import torch
import ttnn
import torch_ttnn


class RollModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, tensor, shifts, dims):
        return torch.roll(tensor, shifts, dims)


@pytest.mark.parametrize(
    "input_shape, shifts, dims",
    [
        ((1, 56, 56, 128), [3, 3], [1, 2]),
        ((1, 28, 28, 256), [-3, -3], [1, 2]),
    ],
)
def test_roll(device, input_shape, shifts, dims):
    m = RollModule()
    input_tensor = torch.rand(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input_tensor, shifts, dims)
    option = torch_ttnn.TorchTtnnOption(device=device)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input_tensor, shifts, dims)
    print(option._out_fx_graphs[0])

    # Check the graph has be rewritten and contain ttnn ops
    nodes = [node.target for node in option._out_fx_graphs[0].nodes]
    assert nodes.count(torch.ops.aten.roll.default) == 0

    # Check inference result
    assert torch.allclose(result_before, result_after)

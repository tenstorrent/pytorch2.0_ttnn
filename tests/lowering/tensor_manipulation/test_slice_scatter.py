import pytest
import torch
import ttnn
import torch_ttnn


class SliceScatterModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input_tensor, src_tensor, dim, start, end):
        out_relu = torch.relu(src_tensor)
        return torch.slice_scatter(input_tensor, out_relu, dim, start, end)


@pytest.mark.parametrize(
    "input_shape, dim, start, end",
    [
        ((1, 128, 28, 28), 1, 3, 20),
    ],
)
def test_slice_scatter(device, input_shape, dim, start, end):
    m = SliceScatterModule()
    input_tensor = torch.rand(input_shape, dtype=torch.bfloat16)
    src_tensor_shape = list(input_shape)
    src_tensor_shape[dim] = end - start
    src_tensor = torch.rand(src_tensor_shape, dtype=torch.bfloat16)

    result_before = m.forward(input_tensor, src_tensor, dim, start, end)
    option = torch_ttnn.TorchTtnnOption(device=device)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input_tensor, src_tensor, dim, start, end)
    print(option._out_fx_graphs[0])

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(torch.ops.aten.slice_scatter.default) == 0
    # Check inference result
    assert torch.allclose(result_before, result_after)

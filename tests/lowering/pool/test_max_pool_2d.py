import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class MaxPool2dModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        return torch.nn.functional.max_pool2d(*args, **kwargs)


@pytest.mark.parametrize(
    "input_shapes, kernel_size, return_indices",
    (
        ((1, 3, 64, 64), (3, 3), False),
        ((1, 3, 64, 64), (3, 3), True),
    ),
)
def test_max_pool_2d(device, input_shapes, kernel_size, return_indices):
    m = MaxPool2dModule()
    inputs = torch.rand(input_shapes, dtype=torch.bfloat16)
    args = (kernel_size,)
    kwargs = {"return_indices": return_indices}
    result_before = m.forward(inputs, *args, **kwargs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    # ttnn operates on channels-last tensors
    input_tensor = torch.permute(inputs, (0, 2, 3, 1))
    result_after = m.forward(input_tensor, *args, **kwargs)
    result_after = torch.permute(result_after, (0, 3, 1, 2))
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.max_pool2d) == 1
    # Check inference result
    assert_with_pcc(result_before, result_after, pcc=0.99)

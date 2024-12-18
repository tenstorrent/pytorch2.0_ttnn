import torch
import torch_ttnn
import pytest
import ttnn


class PatternModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):
        return torch.ops.aten.add.Tensor(input1, input2)


# nms_kernel needs float
def test_nms_pattern(device):
    m = PatternModule()
    input1 = torch.randn([3, 4])
    input2 = torch.randn([3, 4])
    result_before = m.forward(input1, input2)
    option = torch_ttnn.TorchTtnnOption(device=device)
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input1, input2)
    assert result_before.dtype == result_after.dtype
    assert torch.allclose(result_before, result_after, rtol=0.1, atol=0.1)

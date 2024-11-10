import torch
import torch_ttnn
import pytest
import ttnn


class PatternModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        add = torch.ops.aten.add.Tensor(x, 0.0)
        return add


def test_add_vilt(device):
    m = PatternModule()
    input = torch.ones([5])
    result_before = m.forward(input)
    option = torch_ttnn.TorchTtnnOption(device=device)
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input)
    assert result_before.shape == result_after.shape
    assert torch.allclose(result_before, result_after, rtol=0.1, atol=0.1)

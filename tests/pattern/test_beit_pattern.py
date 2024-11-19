import torch
import torch_ttnn
import pytest
import ttnn


class PatternModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, arg1_1, arg223_1):
        view_13 = torch.ops.aten.view.default(arg223_1, [-1])
        index = torch.ops.aten.index.Tensor(arg1_1, [view_13])
        return index


def test_beit_pattern(device):
    m = PatternModule()
    arg1_1 = torch.randn([732, 12]).to(torch.bfloat16)
    arg223_1 = torch.ones([197, 197]).to(torch.int64) * 731
    result_before = m.forward(arg1_1, arg223_1)
    option = torch_ttnn.TorchTtnnOption(device=device)
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(arg1_1, arg223_1)
    assert torch.allclose(result_before, result_after, rtol=0.1, atol=0.1)

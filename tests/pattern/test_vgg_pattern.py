import torch
import torch_ttnn
import pytest
import ttnn


class PatternModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, output_size):
        return torch.ops.aten._adaptive_avg_pool2d.default(input, output_size)


def test_vgg_adaptive_avg_pool2d(device):
    m = PatternModule()
    input = torch.randn([1, 512, 7, 7]).to(torch.bfloat16)
    output_size = [7, 7]
    result_before = m.forward(input, output_size)
    option = torch_ttnn.TorchTtnnOption(device=device)
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, output_size)
    assert result_before.shape == result_after.shape
    assert torch.allclose(result_before, result_after, rtol=0.1, atol=0.1)
    assert not any(
        node.target == torch.ops.aten._adaptive_avg_pool2d.default for node in option._out_fx_graphs[0].nodes
    )

import torch
import torch_ttnn
import ttnn


class PatternModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input):
        add1 = torch.ops.aten.add.Tensor(input, 1.0)
        mul1 = torch.ops.aten.mul.Tensor(input, 1.0)
        add2 = torch.ops.aten.add.Tensor(add1, mul1)
        return add2


def test_data_move_reuse(device):
    m = PatternModule()
    input = torch.randn([4, 4]).to(torch.bfloat16)
    result_before = m.forward(input)
    option = torch_ttnn.TorchTtnnOption(device=device)
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input)
    assert torch.allclose(result_before, result_after, rtol=0.1, atol=0.1)
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.from_torch) == 1

import torch
import torch_ttnn
import pytest
import ttnn


# From XGLM
class PatternModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        # arange = tensor([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
        # arange.dtype = torch.int64
        arange = torch.ops.aten.arange.start(
            0, 19, dtype=torch.int64, device=torch.device(type="cpu"), pin_memory=False
        )
        # unsqueeze.shape = torch.Size([1, 19])
        # unsqueeze.dtype = torch.int64
        unsqueeze = torch.ops.aten.unsqueeze.default(arange, 0)
        # add.shape = torch.Size([1, 19])
        # add.dtype = torch.int64
        add = torch.ops.aten.add.Tensor(unsqueeze, 2)
        # squeeze.shape = torch.Size([19])
        # squeeze.dtype = torch.int64
        squeeze = torch.ops.aten.squeeze.dim(add, 0)
        # unsqueeze_6.shape = torch.Size([1, 19])
        # unsqueeze_6.dtype = torch.int64
        unsqueeze_6 = torch.ops.aten.unsqueeze.default(squeeze, 0)
        # view_2.shape = torch.Size([19])
        # view_2.dtype = torch.int64
        view_2 = torch.ops.aten.view.default(unsqueeze_6, [-1])
        # index_select.shape = torch.Size([19, 1024])
        # index_select.dtype = torch.float32
        index_select = torch.ops.aten.index_select.default(x, 0, view_2)
        return index_select


class AddModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, y):
        return torch.ops.aten.add.Tensor(x, y)


def test_index(device):
    m = PatternModule()
    input = torch.rand([2050, 1024])
    result_before = m.forward(input)
    option = torch_ttnn.TorchTtnnOption(device=device)
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input)
    assert torch.allclose(result_before, result_after, rtol=0.1, atol=0.1)


@pytest.mark.skip()
def test_index_add(device):
    m = AddModule()
    # root cause, output type become bfloat16, but origin is int64
    input1 = torch.randint(0, 5, [2, 3]).to(torch.int64)
    input2 = torch.randint(0, 5, [2, 3]).to(torch.int64)
    result_before = m.forward(input1, input2)
    option = torch_ttnn.TorchTtnnOption(device=device)
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input1, input2)
    assert result_before.dtype == torch.int64
    assert result_after.dtype == torch.int64

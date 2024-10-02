import torch
import torch_ttnn
import pytest
import ttnn


##### Error that both test throw:
# E       RuntimeError: TT_FATAL @ ../tt_metal/impl/buffers/buffer.cpp:38: valid_page_size
# E       info:
# E       For valid non-interleaved buffers page size 90 must equal buffer size 88. For interleaved-buffers page size should be divisible by buffer size


# Smallest module that causes the error, using bfloat16
class UnsqueezeCloneModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        a1 = torch.unsqueeze(x, 1)
        a2 = torch.clone(a1)
        return a2


@pytest.mark.xfail
def test_unsqueeze_clone(device):
    m = UnsqueezeCloneModule()
    input = torch.rand((1, 45), dtype=torch.bfloat16)
    result_before = m.forward(input)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input)
    option._out_fx_graphs[0].print_tabular()
    # Check inference result
    assert torch.allclose(result_before, result_after)


# Full module that causes error in GPT Neo, using torch.int64 as is in the model
# Note that compiler currently does not support int64 data type for clone OP.
# (Add mapping torch.int64->TtnnUint32() to torch_dtype_to_ttnn_dtype in torch_ttnn/passes/lowering/to_tt_pass.py to enable support.)
class GptNeoUnsqueezeCloneModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        a1 = torch.unsqueeze(x, 1)
        a2 = a1.expand(1, 1, 45)
        a3 = torch.clone(a2)
        a4 = a3.view(1, 45)
        return a4


@pytest.mark.xfail
def test_gptneo_unsqueeze_clone(device):
    m = GptNeoUnsqueezeCloneModule()
    input = torch.randint(-100, 100, (1, 45))
    result_before = m.forward(input)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input)
    option._out_fx_graphs[0].print_tabular()
    # Check inference result
    assert torch.allclose(result_before, result_after)

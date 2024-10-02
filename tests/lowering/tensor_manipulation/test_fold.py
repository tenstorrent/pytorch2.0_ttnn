import torch
import torch_ttnn
import pytest
import ttnn


class FoldModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        return torch.nn.functional.fold(*args, **kwargs)


@pytest.mark.parametrize(
    "input_size, output_size, kernel_size, dilation, padding, stride", (((36, 36), (8, 8), (3, 3), 1, 0, 1),)
)
def test_fold(device, input_size, output_size, kernel_size, dilation, padding, stride):
    m = FoldModule()
    tensor = torch.randn(input_size, dtype=torch.bfloat16)
    inputs = tensor, output_size, kernel_size, dilation, padding, stride
    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.fold) == 1

    # Check inference result
    assert torch.allclose(result_before, result_after)

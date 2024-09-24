import torch
import torch_ttnn
import pytest
import ttnn


class SliceModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, start, end):
        return input[:, :, start:end]


class SliceModule2(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, dim, start, end):
        # NOTE: aten.slice treats 9223372036854775807 (64-bit max int) as the last index
        if end == -1:
            end = 9223372036854775807
        return torch.ops.aten.slice.Tensor(input, dim, start, end)


@pytest.mark.parametrize(
    "input_shape, start, end",
    (
        ((1, 4, 16, 32), 0, 8),
        ((1, 4, 16, 32), 4, 12),
        ((1, 4, 16, 32), 8, 16),
    ),
)
def test_slice(device, input_shape, start, end):
    m = SliceModule()
    input_tensor = torch.randn(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input_tensor, start, end)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input_tensor, start, end)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has been rewritten and contains ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.slice) == 1
    # Check inference result
    assert torch.equal(result_before, result_after)


@pytest.mark.parametrize(
    "input_shape, dim, start, end",
    (
        ((1, 1, 1, 256), 3, 0, -1),
        ((1, 256), 0, 0, -1),
        ((1, 512), 0, 0, -1),
        ((1, 512), 1, 0, 256),
    ),
)
def test_slice2(device, input_shape, dim, start, end):
    m = SliceModule2()
    input_tensor = torch.randn(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input_tensor, dim, start, end)
    option = torch_ttnn.TorchTtnnOption(device=device)

    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input_tensor, dim, start, end)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has been rewritten and contains ttnn ops
    if not (start == 0 and (end == -1 or end == input_shape[dim])):
        nodes = list(option._out_fx_graphs[0].nodes)
        assert [node.target for node in nodes].count(ttnn.slice) == 1
    # Check inference result
    print(f"torch_result_shape:{result_before.shape}\nttnn_result_shape:{result_after.shape}")
    assert torch.equal(result_before, result_after)

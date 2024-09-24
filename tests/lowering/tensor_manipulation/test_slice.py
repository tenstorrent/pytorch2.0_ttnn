import torch
import torch_ttnn
import pytest
import ttnn


# Maps special integers to compatible values for aten.slice
# aten.slice treats 9223372036854775807 (64-bit max int) as the last index
def convert_int(val):
    special_int_map = {-1: 9223372036854775807}
    if (ret := special_int_map.get(val)) is not None:
        return ret
    else:
        return val


class SliceModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, start, end):
        return input[:, :, start:end]


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


class AtenSliceModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, dim, start, end):
        return torch.ops.aten.slice.Tensor(input, dim, start, end)


class AtenSliceAfterOpModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, dim, start, end):
        abs = torch.abs(input)
        return torch.ops.aten.slice.Tensor(abs, dim, start, end)


class AtenSliceBeforeOpModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, dim, start, end):
        slice = torch.ops.aten.slice.Tensor(input, dim, start, end)
        return torch.abs(slice)


class AtenSliceBetweenOpModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, dim, start, end):
        abs = torch.abs(input)
        slice = torch.ops.aten.slice.Tensor(abs, dim, start, end)
        return torch.abs(slice)


@pytest.mark.parametrize(
    "module",
    [
        AtenSliceModule(),
        AtenSliceAfterOpModule(),
        AtenSliceBeforeOpModule(),
        AtenSliceBetweenOpModule(),
    ],
)
@pytest.mark.parametrize(
    "input_shape, dim, start, end",
    (
        ((1, 1, 1, 256), 3, 0, -1),
        ((1, 256), 0, 0, -1),
        ((1, 512), 0, 0, -1),
        ((1, 512), 1, 0, 256),
    ),
)
def test_aten_slice(device, input_shape, dim, start, end, module):
    m = module
    input_tensor = torch.randn(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input_tensor, dim, start, convert_int(end))
    option = torch_ttnn.TorchTtnnOption(device=device)

    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input_tensor, dim, start, end)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has been rewritten and contains ttnn ops
    # Ignore if no-op
    if not (start == 0 and (end == -1 or end == input_shape[dim])):
        nodes = list(option._out_fx_graphs[0].nodes)
        assert [node.target for node in nodes].count(ttnn.slice) == 1
    # Check inference result
    print(f"torch_result_shape:{result_before.shape}\nttnn_result_shape:{result_after.shape}")
    assert torch.equal(result_before, result_after)


class SliceEmbeddingModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, dim, start, end, weights):
        slice = torch.ops.aten.slice.Tensor(input, dim, start, end)
        embedding = torch.ops.aten.embedding(weights, slice)
        return torch.abs(embedding)


@pytest.mark.parametrize(
    "weights_shape",
    [
        (512, 1024),
    ],
)
@pytest.mark.parametrize(
    "input_shape, dim, start, end",
    (
        ((1, 256), 0, 0, -1),
        ((1, 512), 0, 0, -1),
        ((1, 512), 1, 0, 256),
    ),
)
def test_reshape_slice_embedding(device, input_shape, dim, start, end, weights_shape):
    m = SliceEmbeddingModule()
    print(convert_int(end))
    input = torch.randint(0, 16, input_shape)
    weights = torch.rand(weights_shape, dtype=torch.bfloat16)
    result_before = m.forward(input, dim, start, convert_int(end), weights)
    option = torch_ttnn.TorchTtnnOption(device=device)

    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, dim, start, end, weights)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has been rewritten and contains ttnn ops
    # Ignore if no-op
    if not (start == 0 and (end == -1 or end == input_shape[dim])):
        nodes = list(option._out_fx_graphs[0].nodes)
        assert [node.target for node in nodes].count(ttnn.slice) == 1
    # Check inference result
    assert torch.equal(result_before, result_after)

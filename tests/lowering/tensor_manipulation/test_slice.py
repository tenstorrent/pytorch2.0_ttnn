import torch
import torch_ttnn
import pytest
import ttnn

END_MAX = 9223372036854775807


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
        # BERT
        ((1, 1, 1, 256), 3, 0, END_MAX),
        ((1, 256), 0, 0, END_MAX),
        ((1, 512), 0, 0, END_MAX),
        ((1, 512), 1, 0, 256),
        # YOLOS
        ((1, 100, 192), 2, 0, END_MAX),
        ((1, 1445, 192), 0, 0, END_MAX),
        ((1, 1445, 192), 1, -100, END_MAX),
        ((1, 192), 0, 0, END_MAX),
        ((1, 192), 1, 0, END_MAX),
        ((1, 4150, 192), 2, 0, END_MAX),
        ((1, 4251, 192), 0, 0, END_MAX),
        ((1, 4251, 192), 1, -100, END_MAX),
        ((1, 4251, 192), 1, 1, -100),
        # Hardnet (train)
        ((1, 782, 7, 7), 1, 0, 160),
    ),
)
def test_aten_slice(device, input_shape, dim, start, end, module):
    m = module
    input_tensor = torch.randn(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input_tensor, dim, start, end)
    option = torch_ttnn.TorchTtnnOption(device=device)

    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input_tensor, dim, start, end)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has been rewritten and contains ttnn ops
    # Ignore if no-op
    if not (start == 0 and (end == END_MAX or end == input_shape[dim])):
        nodes = list(option._out_fx_graphs[0].nodes)
        assert [node.target for node in nodes].count(ttnn.slice) == 1
    # Check inference result
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
        ((1, 256), 0, 0, END_MAX),
        ((1, 512), 0, 0, END_MAX),
        ((1, 512), 1, 0, 256),
    ),
)
def test_reshape_slice_embedding(device, input_shape, dim, start, end, weights_shape):
    m = SliceEmbeddingModule()
    input = torch.randint(0, 16, input_shape)
    weights = torch.rand(weights_shape, dtype=torch.bfloat16)
    result_before = m.forward(input, dim, start, end, weights)
    option = torch_ttnn.TorchTtnnOption(device=device)

    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, dim, start, end, weights)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has been rewritten and contains ttnn ops
    # Ignore if no-op
    if not (start == 0 and (end == END_MAX or end == input_shape[dim])):
        nodes = list(option._out_fx_graphs[0].nodes)
        assert [node.target for node in nodes].count(ttnn.slice) == 1
    # Check inference result
    assert torch.equal(result_before, result_after)

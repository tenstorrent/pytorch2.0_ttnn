import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class ToCopyModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return x.to(torch.bfloat16)


@pytest.mark.parametrize(
    "input_shapes",
    [[(4, 4)]],
)
def test_to_copy(device, input_shapes):
    m = ToCopyModule()
    inputs = [torch.rand(shape) for shape in input_shapes]
    torch_result = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    ttnn_result = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(torch_ttnn.target_wrappers.clone_to) == 1
    # Check inference result
    assert torch.allclose(torch_result, ttnn_result, rtol=0.2)


class ToCopyWithOpAfterModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        to = x.to(torch.bfloat16)
        return torch.add(to, to)


@pytest.mark.parametrize(
    "input_shapes",
    [[(4, 4)]],
)
def test_to_copy_with_op_after(device, input_shapes):
    m = ToCopyWithOpAfterModule()
    inputs = [torch.rand(shape) for shape in input_shapes]
    torch_result = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    ttnn_result = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    target = [node.target for node in nodes]
    assert target.count(torch.ops.aten._to_copy.default) == 0
    assert target.count(ttnn.add) == 1
    # Check inference result
    assert torch.allclose(torch_result, ttnn_result, rtol=0.2)


class ToCopyViewModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, y, target_shape, target_dtype):
        view = torch.ops.aten.view.default(x, target_shape)
        _to_copy = torch.ops.aten._to_copy.default(view, dtype=target_dtype)
        abs = torch.abs(y)
        return torch.add(_to_copy, abs)

    def input_shapes(self):
        return ((16, 1, 32), (16, 32, 32), (16, 1, 32))


class ToCopyExpand(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, y, target_shape, target_dtype):
        expand = torch.ops.aten.expand.default(x, target_shape)
        _to_copy = torch.ops.aten._to_copy.default(expand, dtype=target_dtype)
        abs = torch.abs(y)
        return torch.add(_to_copy, abs)

    def input_shapes(self):
        return ((16, 1, 32), (16, 32, 32), (16, 32, 32))


@pytest.mark.parametrize(
    "module, ttnn_op, target_dtype",
    [
        (ToCopyViewModule(), ttnn.reshape, torch.float32),
        (ToCopyViewModule(), ttnn.reshape, torch.bfloat16),
        (ToCopyExpand(), torch_ttnn.target_wrappers.repeat, torch.float32),
        (ToCopyExpand(), torch_ttnn.target_wrappers.repeat, torch.bfloat16),
    ],
)
def test_reshape_test1(device, module, ttnn_op, target_dtype):
    m = module
    input_shape1, input_shape2, target_shape = m.input_shapes()
    x = torch.rand(input_shape1, dtype=torch.bfloat16)
    y = torch.rand(input_shape2, dtype=torch.bfloat16)
    torch_result = m.forward(x, y, target_shape, target_dtype)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    ttnn_result = m.forward(x, y, target_shape, target_dtype)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    target = [node.target for node in nodes]
    assert target.count(torch.ops.aten._to_copy.default) == 0
    assert [node.target for node in nodes].count(ttnn_op) == 1
    # Check inference result
    assert_with_pcc(torch_result, ttnn_result, 0.99)

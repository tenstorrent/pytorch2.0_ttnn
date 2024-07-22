import torch
import torch_ttnn
import pytest
import ttnn
from torch_ttnn.utils import (
    TtnnRowMajorLayout,
    TtnnTileLayout,
)


class ExpandModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, new_shape):
        return x.expand(new_shape)


class ExpandAfterOpModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, new_shape):
        a = torch.clone(x)
        return a.expand(new_shape)


class ExpandBetweenOpsModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, new_shape):
        a = torch.clone(x)
        ex = a.expand(new_shape)
        return torch.add(ex, ex)


@pytest.mark.parametrize(
    "input_shape, new_shape",
    [
        ((1, 4), (4, 4)),
    ],
)
def test_expand(device, input_shape, new_shape):
    m = ExpandModule()
    tensor = torch.rand(input_shape, dtype=torch.bfloat16)
    inputs = [tensor, new_shape]
    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    target = [node.target for node in nodes]
    assert target.count(ttnn.repeat) == 1
    assert nodes[target.index(ttnn.repeat)].args[1].target == ttnn.Shape
    # Check inference result
    assert torch.allclose(result_before, result_after, rtol=0.2)


@pytest.mark.parametrize(
    "input_shape, new_shape",
    [
        ((1, 4), (4, 4)),
    ],
)
def test_expand_after_op(device, input_shape, new_shape):
    m = ExpandAfterOpModule()
    tensor = torch.rand(input_shape, dtype=torch.bfloat16)
    inputs = [tensor, new_shape]
    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    target = [node.target for node in nodes]
    assert target.count(ttnn.repeat) == 1
    repeat_node = nodes[target.index(ttnn.repeat)]
    assert repeat_node.args[0].target == ttnn.to_layout
    assert repeat_node.args[0].args[0].target == ttnn.clone
    assert type(repeat_node.args[0].args[1]) is type(TtnnRowMajorLayout())
    assert repeat_node.args[1].target == ttnn.Shape
    # Check inference result
    assert torch.allclose(result_before, result_after, rtol=0.2)


@pytest.mark.parametrize(
    "input_shape, new_shape",
    [
        ((1, 4), (4, 4)),
    ],
)
def test_expand_before_op(device, input_shape, new_shape):
    class ExpandBeforeOpModule(torch.nn.Module):
        def __init__(self):
            super().__init__()

        def forward(self, x, new_shape):
            ex = x.expand(new_shape)
            return torch.add(ex, ex)

    m = ExpandBeforeOpModule()
    tensor = torch.rand(input_shape, dtype=torch.bfloat16)
    inputs = [tensor, new_shape]
    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    target = [node.target for node in nodes]
    assert target.count(ttnn.repeat) == 1
    assert nodes[target.index(ttnn.repeat)].args[1].target == ttnn.Shape
    # to_layout that follows ttnn.repeat
    to_layout_idx = target.index(ttnn.to_layout, target.index(ttnn.repeat))
    to_layout_node = nodes[to_layout_idx]
    assert to_layout_node.args[0].target == ttnn.repeat
    assert type(to_layout_node.args[1]) is type(TtnnTileLayout())
    assert target.count(ttnn.add) == 1
    assert to_layout_idx < target.index(ttnn.add)

    # Check inference result
    assert torch.allclose(result_before, result_after, rtol=0.2)


@pytest.mark.parametrize(
    "input_shape, new_shape",
    [
        ((1, 4), (4, 4)),
    ],
)
def test_expand_between_ops(device, input_shape, new_shape):
    m = ExpandBetweenOpsModule()
    tensor = torch.rand(input_shape, dtype=torch.bfloat16)
    inputs = [tensor, new_shape]
    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    target = [node.target for node in nodes]
    assert target.count(ttnn.repeat) == 1
    repeat_node = nodes[target.index(ttnn.repeat)]
    assert repeat_node.args[0].target == ttnn.to_layout
    assert repeat_node.args[0].args[0].target == ttnn.clone
    assert type(repeat_node.args[0].args[1]) is type(TtnnRowMajorLayout())
    assert repeat_node.args[1].target == ttnn.Shape
    # to_layout that follows ttnn.repeat
    to_layout_idx = target.index(ttnn.to_layout, target.index(ttnn.repeat))
    to_layout_node = nodes[to_layout_idx]
    assert to_layout_node.args[0].target == ttnn.repeat
    assert type(to_layout_node.args[1]) is type(TtnnTileLayout())
    assert target.count(ttnn.add) == 1
    assert to_layout_idx < target.index(ttnn.add)
    # Check inference result
    assert torch.allclose(result_before, result_after, rtol=0.2)

# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
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


class ToCopyWithOpAfterModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        to = x.to(torch.bfloat16)
        return torch.add(to, to)


# aten._to_copy is used to convert a dtype to another.
# If there is no ttnn.from_torch that follows aten._to_copy, then leave alone.
# TODO: Will need to re-evaluate the conversion.
@pytest.mark.parametrize(
    "input_shapes",
    [[(4, 4)]],
)
def test_to_copy(device, input_shapes):
    m = ToCopyModule()
    inputs = [torch.rand(shape) for shape in input_shapes]
    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(torch.ops.aten._to_copy.default) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after, rtol=0.2)


# aten._to_copy is used to convert a dtype to another.
# If there is a ttnn.from_torch that follows aten._to_copy and is casting to bfloat, then convert.
@pytest.mark.parametrize(
    "input_shapes",
    [[(4, 4)]],
)
def test_to_copy_with_op_after(device, input_shapes):
    m = ToCopyWithOpAfterModule()
    inputs = [torch.rand(shape) for shape in input_shapes]
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
    assert target.count(torch.ops.aten._to_copy.default) == 0
    assert target.count(ttnn.add) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after, rtol=0.2)


class ToCopyViewModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, y, target_shape):
        view = torch.ops.aten.view.default(x, target_shape)
        _to_copy = torch.ops.aten._to_copy.default(view, dtype=torch.bfloat16)
        abs = torch.abs(y)
        return torch.add(_to_copy, abs)

    def input_shapes(self):
        return ((16, 1, 32), (16, 32, 32), (16, 1, 32))


class ToCopyExpand(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, y, target_shape):
        expand = torch.ops.aten.expand.default(x, target_shape)
        _to_copy = torch.ops.aten._to_copy.default(expand, dtype=torch.bfloat16)
        abs = torch.abs(y)
        return torch.add(_to_copy, abs)

    def input_shapes(self):
        return ((16, 1, 32), (16, 32, 32), (16, 32, 32))


@pytest.mark.parametrize(
    "module, ttnn_op",
    [
        (ToCopyViewModule(), ttnn.experimental.view),
        (ToCopyExpand(), torch_ttnn.target_wrappers.repeat),
    ],
)
def test_reshape_test1(device, module, ttnn_op):
    m = module
    input_shape1, input_shape2, target_shape = m.input_shapes()
    x = torch.rand(input_shape1, dtype=torch.bfloat16)
    y = torch.rand(input_shape2, dtype=torch.bfloat16)
    result_before = m.forward(x, y, target_shape)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(x, y, target_shape)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    target = [node.target for node in nodes]
    assert target.count(torch.ops.aten._to_copy.default) == 0
    assert [node.target for node in nodes].count(ttnn_op) == 1
    # Check inference result
    assert_with_pcc(result_before, result_after, 0.99)

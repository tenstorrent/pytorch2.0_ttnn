import torch
import torch_ttnn
import pytest
import ttnn


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


# aten.to_copy is used to convert a dtype to another.
# TODO: Will need to re-evaluate the conversion.
@pytest.mark.xfail
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
    assert [node.target for node in nodes].count(ttnn.as_tensor) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after, rtol=0.2)


@pytest.mark.xfail
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
    assert target.count(ttnn.as_tensor) == 1
    assert target.count(ttnn.add) == 1
    add_node = nodes[target.index(ttnn.add)]
    assert add_node.args[0].target == ttnn.as_tensor
    assert add_node.args[1].target == ttnn.as_tensor
    # Check inference result
    assert torch.allclose(result_before, result_after, rtol=0.2)

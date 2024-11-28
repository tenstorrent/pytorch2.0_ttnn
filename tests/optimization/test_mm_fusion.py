import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class MatmulModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, other, activation):
        return activation(torch.matmul(input, other))
        
@pytest.mark.parametrize(
    ("input_shapes", "activation"),
    [
     ([(64, 64), (64, 64)], torch.nn.functional.relu),
     ([(64, 64), (64, 64)], torch.nn.functional.gelu),
     ([(64, 64), (64, 64)], torch.nn.functional.silu),
     
     # Inside ttnn/cpp/ttnn/operations/matmul/matmul.cpp, function bound_matmul only supports the thre activations above
     pytest.param([(64, 64), (64, 64)], torch.nn.functional.sigmoid, marks=pytest.mark.xfail()),
     pytest.param([(64, 64), (64, 64)], torch.sqrt, marks=pytest.mark.xfail()),
     pytest.param([(64, 64), (64, 64)], torch.exp, marks=pytest.mark.xfail()),
     pytest.param([(64, 64), (64, 64)], torch.reciprocal, marks=pytest.mark.xfail()),
     pytest.param([(64, 64), (64, 64)], torch.log, marks=pytest.mark.xfail()),
     pytest.param([(64, 64), (64, 64)], torch.nn.functional.tanh, marks=pytest.mark.xfail()),
     pytest.param([(64, 64), (64, 64)], torch.log2, marks=pytest.mark.xfail()),
     pytest.param([(64, 64), (64, 64)], torch.log10, marks=pytest.mark.xfail()),
     pytest.param([(64, 64), (64, 64)], torch.sin, marks=pytest.mark.xfail()),
     pytest.param([(64, 64), (64, 64)], torch.cos, marks=pytest.mark.xfail()),
     pytest.param([(64, 64), (64, 64)], torch.abs, marks=pytest.mark.xfail()),
     pytest.param([(64, 64), (64, 64)], torch.sign, marks=pytest.mark.xfail()),
     pytest.param([(64, 64), (64, 64)], torch.square, marks=pytest.mark.xfail()),
     pytest.param([(64, 64), (64, 64)], torch.nn.functional.softplus, marks=pytest.mark.xfail()),
    ]
)
def test_matmul(device, input_shapes, activation):
    m = MatmulModule()
    inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
    torch_result = m.forward(*inputs, activation)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    ttnn_result = m.forward(*inputs, activation)
    option._out_fx_graphs[0].print_tabular()
    
    # Check the graph has be rewritten and contains ttnn mat mul and total of 7 ops
    # (2 input args, 2 from_torch, 1 mat mul, 1 to_torch, 1 output arg)
    nodes = list(option._out_fx_graphs[0].nodes)
    target = [node.target for node in nodes]
    assert target.count(ttnn.matmul) == 1 and len(target) == 7
    
    # Check inference result
    assert_with_pcc(torch_result, ttnn_result, 0.98)


class BmmModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, other, activation):
        return activation(torch.bmm(input, other))

@pytest.mark.parametrize(
    ("input_shapes", "activation"),
    [
     ([(3, 64, 64), (3, 64, 64)], torch.nn.functional.relu),
     ([(3, 64, 64), (3, 64, 64)], torch.nn.functional.gelu),
     ([(3, 64, 64), (3, 64, 64)], torch.nn.functional.silu),

     # Inside ttnn/cpp/ttnn/operations/matmul/matmul.cpp, function bound_matmul only supports the thre activations above
     pytest.param([(3, 64, 64), (3, 64, 64)], torch.nn.functional.sigmoid, marks=pytest.mark.xfail()),
     pytest.param([(3, 64, 64), (3, 64, 64)], torch.sqrt, marks=pytest.mark.xfail()),
     pytest.param([(3, 64, 64), (3, 64, 64)], torch.exp, marks=pytest.mark.xfail()),
     pytest.param([(3, 64, 64), (3, 64, 64)], torch.reciprocal, marks=pytest.mark.xfail()),
     pytest.param([(3, 64, 64), (3, 64, 64)], torch.log, marks=pytest.mark.xfail()),
     pytest.param([(3, 64, 64), (3, 64, 64)], torch.nn.functional.tanh, marks=pytest.mark.xfail()),
     pytest.param([(3, 64, 64), (3, 64, 64)], torch.log2, marks=pytest.mark.xfail()),
     pytest.param([(3, 64, 64), (3, 64, 64)], torch.log10, marks=pytest.mark.xfail()),
     pytest.param([(3, 64, 64), (3, 64, 64)], torch.sin, marks=pytest.mark.xfail()),
     pytest.param([(3, 64, 64), (3, 64, 64)], torch.cos, marks=pytest.mark.xfail()),
     pytest.param([(3, 64, 64), (3, 64, 64)], torch.abs, marks=pytest.mark.xfail()),
     pytest.param([(3, 64, 64), (3, 64, 64)], torch.sign, marks=pytest.mark.xfail()),
     pytest.param([(3, 64, 64), (3, 64, 64)], torch.square, marks=pytest.mark.xfail()),
     pytest.param([(3, 64, 64), (3, 64, 64)], torch.nn.functional.softplus, marks=pytest.mark.xfail()),
    ]
)
def test_bmm(device, input_shapes, activation):
    m = BmmModule()
    inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
    torch_result = m.forward(*inputs, activation)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    ttnn_result = m.forward(*inputs, activation)
    option._out_fx_graphs[0].print_tabular()
    
    # Check the graph has be rewritten and contains ttnn mat mul and total of 7 ops
    # (2 input args, 2 from_torch, 1 mat mul, 1 to_torch, 1 output arg)
    nodes = list(option._out_fx_graphs[0].nodes)
    target = [node.target for node in nodes]
    assert target.count(ttnn.matmul) == 1 and len(target) == 7
    
    # Check inference result
    assert_with_pcc(torch_result, ttnn_result, 0.98)

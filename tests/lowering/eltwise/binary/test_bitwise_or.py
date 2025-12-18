import torch
import torch_ttnn
import pytest
import ttnn


class BitwiseOrModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, y):
        return torch.bitwise_or(x, y)


@pytest.mark.xfail(
    reason="tt-metal/ttnn/cpp/ttnn/operations/eltwise/unary/device/unary_device_operation.cpp:42: input_datatype == DataType::INT32"
)
@pytest.mark.parametrize("input_shape", ((4, 4), (1, 32)))
def test_bitwise_or_scalar(device, input_shape):
    m = BitwiseOrModule()
    input = torch.randint(-256, 256, input_shape, dtype=torch.int32)
    value = torch.randint(-256, 256, ()).item()
    result_before = m.forward(input, value)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, value)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has been rewritten and contains ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.bitwise_or) == 1

    # Check inference result
    assert torch.equal(result_before, result_after)


@pytest.mark.xfail(reason="Tensor-tensor bitwise operation not supported yet (tenstorrent/tt-metal#12907)")
@pytest.mark.parametrize(
    "input_shapes",
    (((32, 32), (32, 32)), ((64,), (32, 64)), ((64, 32), (64, 1)), ((64, 1), (1, 64))),
)
def test_bitwise_or_tensor(device, input_shapes):
    m = BitwiseOrModule()
    inputs = [torch.randint(0, 256, shape, dtype=torch.int32) for shape in input_shapes]
    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has been rewritten and contains ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.bitwise_or) == 1

    # Check inference result
    assert torch.equal(result_before, result_after)

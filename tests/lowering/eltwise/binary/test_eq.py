import torch
import torch_ttnn
import pytest
import ttnn


class EqModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):
        return torch.eq(input1, input2)


@pytest.mark.xfail(reason="broadcasting issues (#64)")
@pytest.mark.parametrize(
    "input_shapes",
    (((32, 32), (32, 32)), ((64,), (32, 64)), ((64, 32), (64, 1)), ((64, 1), (1, 64))),
)
def test_eq_tensor(device, input_shapes):
    m = EqModule()
    inputs = [torch.randint(0, 2, shape, dtype=torch.bfloat16) for shape in input_shapes]
    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.eq) == 1
    # Intermediate node meta check if preserved
    for node in nodes:
        if node.target == ttnn.full:
            assert node.meta["val"].size() == input_shapes[0]
    # Check inference result
    assert torch.allclose(result_before, result_after.to(torch.bool))


@pytest.mark.parametrize("input_shape", ((64, 128),))
def test_eq_scalar(device, input_shape):
    m = EqModule()
    input = torch.randint(0, 2, input_shape, dtype=torch.bfloat16)
    scalar = torch.randint(0, 2, (1,)).item()
    result_before = m.forward(input, scalar)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, scalar)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    target = [node.target for node in nodes]
    assert target.count(ttnn.full) == 1
    assert target.count(ttnn.eq) == 1
    assert target.index(ttnn.full) < target.index(ttnn.eq)
    # Intermediate node meta check if preserved
    for node in nodes:
        if node.target == ttnn.full:
            assert node.meta["val"].size() == input_shape
    # Check inference result
    assert torch.allclose(result_before, result_after.to(torch.bool))

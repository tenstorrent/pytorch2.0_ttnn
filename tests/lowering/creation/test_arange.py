import torch
import torch_ttnn
import pytest
import ttnn


class ArangeModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, end):
        # start = 0, step = 1
        return torch.arange(end, dtype=torch.bfloat16)


class ArangeStartModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, start, end):
        # step = 1
        return torch.arange(start, end, dtype=torch.bfloat16)


class ArangeStartStepModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, start, end, step):
        return torch.arange(start, end, step, dtype=torch.bfloat16)


# NOTE(kevinwuTT) This test fails because ttnn.arange does not support start value of 0.
@pytest.mark.xfail(reason="ttnn.arange does not support start value of 0")
@pytest.mark.parametrize(
    "input_shapes",
    [[100]],
)
def test_arange(device, input_shapes):
    m = ArangeModule()
    result_before = m.forward(*input_shapes)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*input_shapes)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.arange) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after)


@pytest.mark.parametrize(
    "input_shapes",
    [[2, 100]],
)
def test_arange_start(device, input_shapes):
    m = ArangeStartModule()
    result_before = m.forward(*input_shapes)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*input_shapes)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.arange) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after)


@pytest.mark.parametrize(
    "input_shapes",
    [[4, 100, 3]],
)
def test_arange_start_step(device, input_shapes):
    m = ArangeStartStepModule()
    result_before = m.forward(*input_shapes)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*input_shapes)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.arange) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after)

import torch
import torch_ttnn
import pytest
import ttnn


# RuntimeError: TT_THROW @ ../ttnn/cpp/ttnn/operations/core.hpp:81: tt::exception
# info: Unable to reshape a tensor in TILE_LAYOUT to non-tile height and width!
# Please convert the input tensor to ROW_MAJOR_LAYOUT first.
class UnsqueezeModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, y):
        return torch.unsqueeze(x, y)


@pytest.mark.parametrize(
    "input_shape, dim",
    [((5, 2, 4, 3), 1)],
)
def test_unsqueeze1(device, input_shape, dim):
    mod = UnsqueezeModule()
    tensor = torch.rand(input_shape, dtype=torch.bfloat16)
    inputs = [tensor, dim]
    result_before = mod.forward(*inputs)

    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    ttnn_mod = torch.compile(mod, backend=torch_ttnn.backend, options=option)
    # Throwing error in to_tt_pass.py not sure exactly where
    result_after = ttnn_mod.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()
    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.reshape) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after)


@pytest.mark.parametrize(
    "input_shape, dim",
    [((5, 2, 4), 1)],
)
# 4D reshapes are done on device
def test_unsqueeze2(device, input_shape, dim):
    mod = UnsqueezeModule()
    tensor = torch.rand(input_shape, dtype=torch.bfloat16)
    inputs = [tensor, dim]
    result_before = mod.forward(*inputs)

    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    ttnn_mod = torch.compile(mod, backend=torch_ttnn.backend, options=option)
    # Throwing error in to_tt_pass.py not sure exactly where
    result_after = ttnn_mod.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()
    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.reshape) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after)


@pytest.mark.parametrize(
    "input_shape, dim",
    [((5, 2, 4, 3), -2)],
)
def test_unsqueeze3(device, input_shape, dim):
    mod = UnsqueezeModule()
    tensor = torch.rand(input_shape, dtype=torch.bfloat16)
    inputs = [tensor, dim]
    result_before = mod.forward(*inputs)

    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    ttnn_mod = torch.compile(mod, backend=torch_ttnn.backend, options=option)
    # Throwing error in to_tt_pass.py not sure exactly where
    result_after = ttnn_mod.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()
    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.reshape) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after)

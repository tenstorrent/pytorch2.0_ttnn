import pytest
import torch
import ttnn
import torch_ttnn


class PermuteModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, order):
        return torch.permute(x, order)


@pytest.mark.parametrize(
    "input_shape, permute_order",
    [
        ((4, 4), (1, 0)),
        pytest.param(
            (1, 3, 16, 16, 16, 16),
            (0, 2, 4, 3, 5, 1),
            marks=pytest.mark.xfail(reason="not support > 4D shape (tt-metal#15165)"),
        ),
    ],
)
def test_permute(device, input_shape, permute_order):
    m = PermuteModule()
    input_tensor = torch.rand(input_shape, dtype=torch.bfloat16)
    torch_result = m.forward(input_tensor, permute_order)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    ttnn_result = m.forward(input_tensor, permute_order)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and not contain aten ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert not any(node.target == torch.ops.aten.permute.default for node in nodes)
    # Check shape or result
    assert torch_result.size() == ttnn_result.size()
    # Check inference result
    assert torch.allclose(torch_result, ttnn_result)


# This tests tests the workaround for issue https://github.com/tenstorrent/tt-metal/issues/11191
@pytest.mark.parametrize(
    "input_shape, permute_order",
    [
        (
            (5, 1, 2),
            (1, 0, 2),
        ),
        (
            (1, 1024, 160),
            (0, 2, 1),
        ),
        (
            (1, 1024, 196),
            (0, 2, 1),
        ),
        (
            (1, 1024, 256),
            (0, 2, 1),
        ),
        pytest.param(
            (1, 1024, 49),
            (0, 2, 1),
            marks=pytest.mark.xfail(
                reason="Page size must be divisible by sizeof(uint32_t) because buffers hold uint32_t values"
            ),
        ),
        (
            (1, 1200, 320),
            (0, 2, 1),
        ),
        (
            (1, 128, 300),
            (0, 2, 1),
        ),
        pytest.param(
            (1, 1280, 1369),
            (0, 2, 1),
            marks=pytest.mark.xfail(
                reason="Page size must be divisible by sizeof(uint32_t) because buffers hold uint32_t values"
            ),
        ),
        (
            (1, 160, 256),
            (0, 2, 1),
        ),
        (
            (1, 16384, 256),
            (0, 2, 1),
        ),
        (
            (1, 16384, 32),
            (0, 2, 1),
        ),
        (
            (1, 19200, 64),
            (0, 2, 1),
        ),
        (
            (1, 256, 256),
            (0, 2, 1),
        ),
        (
            (1, 256, 512),
            (0, 2, 1),
        ),
        (
            (1, 32, 256),
            (0, 2, 1),
        ),
        (
            (1, 320, 300),
            (0, 2, 1),
        ),
        (
            (1, 4096, 256),
            (0, 2, 1),
        ),
        (
            (1, 4096, 64),
            (0, 2, 1),
        ),
        (
            (1, 4800, 128),
            (0, 2, 1),
        ),
        (
            (1, 64, 256),
            (0, 2, 1),
        ),
        (
            (1, 64, 300),
            (0, 2, 1),
        ),
        (
            (1, 768, 1500),
            (0, 2, 1),
        ),
        (
            (1, 768, 196),
            (0, 2, 1),
        ),
        pytest.param(
            (1, 768, 49),
            (0, 2, 1),
            marks=pytest.mark.xfail(
                reason="Page size must be divisible by sizeof(uint32_t) because buffers hold uint32_t values"
            ),
        ),
    ],
)
def test_permute_missing_dim(device, input_shape, permute_order):
    m = PermuteModule()
    inputs = torch.rand(input_shape, dtype=torch.bfloat16)
    torch_result = m.forward(inputs, permute_order)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    ttnn_result = m.forward(inputs, permute_order)
    option._out_fx_graphs[0].print_tabular()
    # Check the graph has be rewritten and not contain aten ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert not any(node.target == torch.ops.aten.permute.default for node in nodes)
    # Check shape or result
    assert torch_result.size() == ttnn_result.size()
    # Check inference result
    assert torch.allclose(torch_result, ttnn_result)

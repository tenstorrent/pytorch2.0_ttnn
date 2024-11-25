import pytest
import torch
import ttnn
import torch_ttnn


class ViewModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, new_shape):
        return torch.reshape(x, new_shape)


class ViewAfterOpModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, new_shape):
        abs = torch.abs(x)
        return torch.reshape(abs, new_shape)


class ViewBeforeOpModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, new_shape):
        reshape = torch.reshape(x, new_shape)
        return torch.abs(reshape)


class ViewBetweenOpModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, new_shape):
        abs = torch.abs(x)
        reshape = torch.reshape(abs, new_shape)
        return torch.abs(reshape)


# Most ttnn computation ops use tile layout, but reshape sometimes doesn't.
# This tests the interactions between them.
class ViewShareOpModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, new_shape):
        abs = torch.abs(x)
        reshape = torch.reshape(x, new_shape)
        reshape2 = torch.reshape(abs, new_shape)
        return reshape + reshape2


@pytest.mark.parametrize(
    "module",
    [
        ViewModule(),
        ViewAfterOpModule(),
        ViewBeforeOpModule(),
        ViewBetweenOpModule(),
        ViewShareOpModule(),
    ],
)
@pytest.mark.parametrize(
    "input_shape, new_shape",
    [
        ((1, 16, 256, 256), (16, 256, 256)),
        ((1, 16, 256, 64), (16, 256, 64)),
        ((1, 16, 64, 256), (16, 64, 256)),
        ((1, 256, 1024), (1, 256, 16, 64)),
        ((1, 256, 1024), (256, 1024)),
        ((1, 256, 16, 64), (1, 256, 1024)),
        ((1, 256, 4096), (256, 4096)),
        ((16, 256, 256), (1, 16, 256, 256)),
        ((16, 256, 64), (1, 16, 256, 64)),
        ((256, 1024), (1, 256, 1024)),
        ((256, 2), (1, 256, 2)),
        ((256, 4096), (1, 256, 4096)),
        ((1, 32, 16, 96), (1, 32, 1536)),
        ((1, 192, 4150), (1, 192, 50, 83)),
        ((1, 100, 192), (100, 192)),
        ((1, 1445, 192), (1, 1445, 3, 64)),
        ((1, 1445, 192), (1445, 192)),
        ((1, 1445, 3, 64), (1, 1445, 192)),
        ((1, 1445, 768), (1445, 768)),
        ((1, 192, 32, 42), (1, 192, 1344)),
        ((1, 192, 4150), (1, 192, 50, 83)),
        ((1, 3, 1445, 1445), (3, 1445, 1445)),
        ((1, 3, 1445, 64), (3, 1445, 64)),
        ((1, 3, 64, 1445), (3, 64, 1445)),
        ((100, 192), (1, 100, 192)),
        ((100, 4), (1, 100, 4)),
        ((100, 92), (1, 100, 92)),
        ((1445, 192), (1, 1445, 192)),
        ((1445, 768), (1, 1445, 768)),
        ((192), (1, 192, 1, 1)),
        ((1), (1, 1, 1, 1)),
        ((3, 1445, 1445), (1, 3, 1445, 1445)),
        ((3, 1445, 64), (1, 3, 1445, 64)),
        ((32), (1, 1, 32, 1)),
        ((42), (1, 1, 1, 42)),
        pytest.param(
            (1, 10),
            (10,),
            marks=pytest.mark.xfail(reason="Does not support TILE_LAYOUT."),
        ),
    ],
)
def test_reshape(device, input_shape, new_shape, module):
    m = module
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input, new_shape)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, new_shape)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.reshape) >= 1
    # Check inference result
    assert torch.allclose(result_before, result_after)

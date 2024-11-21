import torch
import torch_ttnn
import pytest
import ttnn


def _test_masked_fill_common(device, module, input_shape, mask_shape, fill_value):
    m = module
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    mask = torch.rand(mask_shape) > 0.5
    result_before = m.forward(input, mask, fill_value)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, mask, fill_value)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    target = [node.target for node in nodes]
    assert target.count(torch.ops.aten.masked_fill.Scalar) == 0
    assert target.count(torch_ttnn.target_wrappers.repeat) == 1
    assert target.count(ttnn.ones) == 1
    assert target.count(ttnn.subtract) == 1
    assert target.count(ttnn.multiply) == 2
    assert target.count(ttnn.full) == 1
    assert target.count(ttnn.add) == 1

    multiply_idx = [i for i, n in enumerate(target) if n == ttnn.multiply]
    assert target.index(ttnn.ones) < target.index(ttnn.subtract)
    assert target.index(ttnn.ones) < multiply_idx[0]
    assert target.index(torch_ttnn.target_wrappers.repeat) < target.index(ttnn.subtract)
    assert target.index(torch_ttnn.target_wrappers.repeat) < multiply_idx[0]

    assert target.index(ttnn.full) < multiply_idx[1]

    assert multiply_idx[0] < multiply_idx[1]
    assert multiply_idx[1] < target.index(ttnn.add)

    # Check inference result
    assert torch.allclose(result_before, result_after)

    # Return list of nodes of converted graph
    return target


class MaskedFillModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, mask, fill_value):
        return input.masked_fill(mask, fill_value)


@pytest.mark.parametrize(
    "input_shape, mask_shape, fill_value",
    [
        ((1, 1, 32, 32), (1, 1, 32, 32), -3.3895313892515355e38),
        ((1, 16, 32, 32), (1, 1, 32, 32), -3.3895313892515355e38),
        ((64, 64, 64), (64, 64, 64), -100.0),
        ((64, 64, 64), (64, 64, 64), 0.0),
        ((16, 64, 64), (16, 64, 64), -100.0),
        ((16, 64, 64), (16, 64, 64), 0.0),
        ((4, 64, 64), (4, 64, 64), -100.0),
        ((4, 64, 64), (4, 64, 64), 0.0),
        # The following have unsupported shapes:
        pytest.param((2, 1, 7, 7), (2, 1, 7, 7), -3.3895313892515355e38, marks=pytest.mark.xfail()),
        pytest.param((1, 920), (1, 920), float("-inf"), marks=pytest.mark.xfail()),
        pytest.param((7, 7), (7, 7), float("-inf"), marks=pytest.mark.xfail()),
        pytest.param((1, 1, 45, 45), (1, 1, 45, 45), -3.4028234663852886e38, marks=pytest.mark.xfail()),
        pytest.param((1, 50257), (1, 50257), float("-inf"), marks=pytest.mark.xfail()),
        pytest.param((1, 1, 1, 46), (1, 1, 1, 46), -3.4028234663852886e38, marks=pytest.mark.xfail()),
        pytest.param((1, 1, 59, 59), (1, 1, 59, 59), -3.4028234663852886e38, marks=pytest.mark.xfail()),
        pytest.param((1, 1, 1, 60), (1, 1, 1, 60), -3.4028234663852886e38, marks=pytest.mark.xfail()),
        pytest.param((1, 1, 19, 19), (1, 1, 19, 19), -3.4028234663852886e38, marks=pytest.mark.xfail()),
        pytest.param((1, 1, 24, 24), (1, 1, 24, 24), -3.4028234663852886e38, marks=pytest.mark.xfail()),
        pytest.param((1, 1, 1, 24), (1, 1, 1, 24), -3.4028234663852886e38, marks=pytest.mark.xfail()),
        pytest.param((64, 49, 49), (64, 49, 49), -100.0, marks=pytest.mark.xfail()),
        pytest.param((64, 49, 49), (64, 49, 49), 0.0, marks=pytest.mark.xfail()),
        pytest.param((16, 49, 49), (16, 49, 49), -100.0, marks=pytest.mark.xfail()),
        pytest.param((16, 49, 49), (16, 49, 49), 0.0, marks=pytest.mark.xfail()),
        pytest.param((4, 49, 49), (4, 49, 49), -100.0, marks=pytest.mark.xfail()),
        pytest.param((4, 49, 49), (4, 49, 49), 0.0, marks=pytest.mark.xfail()),
        # pytest.param((1, 1, 1, s10 + 1), (1, 1, 1, s10 + 1), -3.4028234663852886e+38, marks=pytest.mark.xfail(reason="Input variation shape")),
    ],
)
@pytest.mark.skip(reason="Temporarily disabled due to #458")
def test_masked_fill(device, input_shape, mask_shape, fill_value):
    _test_masked_fill_common(device, MaskedFillModule(), input_shape, mask_shape, fill_value)

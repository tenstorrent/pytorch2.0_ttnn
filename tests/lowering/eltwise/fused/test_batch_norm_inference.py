import torch
import torch_ttnn
import pytest
import ttnn


class BatchNormModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        return torch.nn.functional.batch_norm(*args, **kwargs)


def expand_param_tuple(*shape, **kwargs):
    shape = (*shape,)
    return (
        pytest.param(shape, True, True, **kwargs),
        pytest.param(shape, False, True, **kwargs),
        pytest.param(shape, True, False, **kwargs),
        pytest.param(shape, False, False, **kwargs),
    )


@pytest.mark.parametrize(
    "input_shape, weight, bias",
    (
        *expand_param_tuple(1, 100, 14, 14),
        *expand_param_tuple(1, 224, 112, 112),
        *expand_param_tuple(1, 640, 14, 14),
        *expand_param_tuple(1, 640, 7, 7),
        *expand_param_tuple(1, 672, 15, 15),
        *expand_param_tuple(1, 64, 30, 40),
        *expand_param_tuple(2, 64, 30, 40, marks=pytest.mark.xfail(reason="Some eltwise op fails for batch size > 1")),
        *expand_param_tuple(3, 64, 30, 40, marks=pytest.mark.xfail(reason="Some eltwise op fails for batch size > 1")),
        # The following test cases are from MobileNetV2
        *expand_param_tuple(1, 32, 112, 112),
        *expand_param_tuple(1, 16, 112, 112),
        *expand_param_tuple(1, 96, 112, 112),
        *expand_param_tuple(1, 96, 56, 56),
        *expand_param_tuple(1, 24, 56, 56),
        *expand_param_tuple(1, 144, 56, 56),
        *expand_param_tuple(1, 144, 28, 28),
        *expand_param_tuple(1, 32, 28, 28),
        *expand_param_tuple(1, 192, 28, 28),
        *expand_param_tuple(1, 192, 14, 14),
        *expand_param_tuple(1, 64, 14, 14),
        *expand_param_tuple(1, 384, 14, 14),
        *expand_param_tuple(1, 96, 14, 14),
        *expand_param_tuple(1, 576, 14, 14),
        *expand_param_tuple(1, 576, 7, 7),
        *expand_param_tuple(1, 160, 7, 7),
        *expand_param_tuple(1, 960, 7, 7),
        *expand_param_tuple(1, 320, 7, 7),
        *expand_param_tuple(1, 1280, 7, 7),
    ),
)
def test_batch_norm_inference(device, input_shape, weight, bias):
    m = BatchNormModule()
    channels = input_shape[1]
    input = torch.randn(input_shape, dtype=torch.bfloat16)
    mean = torch.randn(channels, dtype=torch.bfloat16)
    var = torch.randn(channels, dtype=torch.bfloat16)
    weight = torch.randn(channels, dtype=torch.bfloat16) if weight else None
    bias = torch.randn(channels, dtype=torch.bfloat16) if bias else None
    args = input, mean, var, weight, bias

    result_before = m.forward(*args)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*args)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    targets = (*(node.target for node in option._out_fx_graphs[0].nodes),)
    assert targets.count(ttnn.rsqrt) == 1
    assert targets.count(ttnn.sub) == 1

    # Check inference result
    assert torch.allclose(result_before, result_after)

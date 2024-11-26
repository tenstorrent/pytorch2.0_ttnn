import torch
import torch_ttnn
import pytest

from tests.utils import assert_with_pcc


class BatchNormModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        return torch.nn.functional.batch_norm(*args, **kwargs)


@pytest.mark.parametrize(
    "input_shape",
    (
        (1, 100, 14, 14),
        (1, 224, 112, 112),
        (1, 640, 14, 14),
        (1, 640, 7, 7),
        (1, 672, 15, 15),
        (1, 64, 30, 40),
        (2, 64, 30, 40),
        (3, 64, 30, 40),
        # The following test cases are from MobileNetV2
        (1, 32, 112, 112),
        (1, 16, 112, 112),
        (1, 96, 112, 112),
        (1, 96, 56, 56),
        (1, 24, 56, 56),
        (1, 144, 56, 56),
        (1, 144, 28, 28),
        (1, 32, 28, 28),
        (1, 192, 28, 28),
        (1, 192, 14, 14),
        (1, 64, 14, 14),
        (1, 384, 14, 14),
        (1, 96, 14, 14),
        (1, 576, 14, 14),
        (1, 576, 7, 7),
        (1, 160, 7, 7),
        (1, 960, 7, 7),
        (1, 320, 7, 7),
        (1, 1280, 7, 7),
    ),
)
@pytest.mark.parametrize("weight", (True, False))
@pytest.mark.parametrize("bias", (True, False))
def test_batch_norm_inference(device, input_shape, weight, bias):
    m = BatchNormModule()
    channels = input_shape[1]
    input_tensor = torch.randn(input_shape, dtype=torch.bfloat16)
    mean = torch.randn(channels, dtype=torch.bfloat16)
    var = torch.randn(channels, dtype=torch.bfloat16) ** 2
    weight = torch.randn(channels, dtype=torch.bfloat16) if weight else None
    bias = torch.randn(channels, dtype=torch.bfloat16) if bias else None
    args = input_tensor, mean, var, weight, bias

    result_before = m.forward(*args)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*args)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and aten ops are replaced
    nodes = option._out_fx_graphs[0].nodes
    assert not any(node.target == torch.ops.aten._native_batch_norm_legit_no_training.default for node in nodes)

    # Check inference result
    assert_with_pcc(result_before, result_after, pcc=0.99)

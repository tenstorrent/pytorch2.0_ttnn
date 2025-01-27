import torch
import torch_ttnn
import pytest

from tests.utils import assert_with_pcc


class ConvolutionModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(
        self,
        input_tensor,
        weight_tensor,
        bias_tensor,
        stride,
        padding,
        dilation,
        transposed,
        groups,
    ):
        return torch.ops.aten.convolution.default(
            input=input_tensor,
            weight=weight_tensor,
            bias=bias_tensor,
            stride=stride,
            padding=padding,
            dilation=dilation,
            transposed=transposed,
            groups=groups,
            output_padding=[0] * len(padding),
        )


@pytest.mark.parametrize(
    "input_shape, weight_shape, stride, padding, dilation, groups, transposed",
    [
        ((1, 1, 28, 28), (16, 1, 3, 3), (1, 1), (1, 1), (1, 1), 1, False),
        ((1, 1, 28, 28), (16, 1, 3, 3), (1, 1), (1, 1), (1, 1), 1, False),
        ((1, 4, 7, 7), (4, 16, 2, 2), (2, 2), (0, 0), (1, 1), 1, True),
        ((1, 16, 14, 14), (16, 1, 2, 2), (2, 2), (0, 0), (1, 1), 1, True),
        ((1, 64, 56, 56), (128, 64, 1, 1), (1, 1), (0, 0), (1, 1), 1, False),
        pytest.param(
            (1, 1024, 45, 80),
            (2048, 1024, 1, 1),
            (2, 2),
            (0, 0),
            (1, 1),
            1,
            False,
            marks=pytest.mark.xfail(reason="Low PCC (tt-metal#16262)"),
        ),
        ((1, 16, 28, 28), (16, 4, 3, 3), (1, 1), (1, 1), (1, 1), 4, False),
        ((1, 32, 7, 7), (32, 32, 2, 2), (2, 2), (0, 0), (1, 1), 1, False),
        ((1, 256, 512), (1024, 256, 1), (1,), (0,), (1,), 1, False),
        ((8, 128, 56, 56), (128, 128, 3, 3), (2, 2), (1, 1), (1, 1), 1, False),
    ],
)
@pytest.mark.parametrize("has_bias", [False, True])
def test_conv(
    device,
    input_shape,
    weight_shape,
    stride,
    padding,
    dilation,
    groups,
    transposed,
    has_bias,
):
    m = ConvolutionModule()
    input_tensor = torch.rand(input_shape, dtype=torch.bfloat16)
    weight_tensor = torch.rand(weight_shape, dtype=torch.bfloat16)
    bias_tensor = torch.rand((weight_shape[1 if transposed else 0],), dtype=torch.bfloat16) if has_bias else None
    result_before = m.forward(
        input_tensor,
        weight_tensor,
        bias_tensor,
        stride,
        padding,
        dilation,
        transposed,
        groups,
    )
    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(
        input_tensor,
        weight_tensor,
        bias_tensor,
        stride,
        padding,
        dilation,
        transposed,
        groups,
    )
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    # Check the graph has be rewritten and aten ops are replaced
    assert not any(node.target == torch.ops.aten.convolution.default for node in nodes)
    # Check inference result
    assert_with_pcc(result_before, result_after, pcc=0.99)

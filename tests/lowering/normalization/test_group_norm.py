import torch
import torch_ttnn
from torch_ttnn.passes.lowering import target_wrappers
import pytest
import ttnn

from tests.utils import assert_with_pcc


class GroupNormModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, num_groups, weight=None, bias=None, eps=1e-05):
        return torch.nn.functional.group_norm(input, num_groups, weight, bias, eps)


@pytest.mark.parametrize(
    "input_shape, num_groups",
    [
        [(1, 320, 32, 32), 32],
        [(1, 1280, 16, 16), 32],
        [(2, 320, 64, 64), 32],
        [(1, 1280, 1, 512), 32],
        # These two cases appeared in stable diffusion v2 and accuracy failed
        pytest.param((1, 1280, 8, 8), 32, marks=pytest.mark.xfail(reason="see #555")),
        pytest.param((1, 2560, 8, 8), 32, marks=pytest.mark.xfail(reason="see #555")),
        # These four cases appeared in retinanet_resnet50_fpn_v2 and RuntimeError
        pytest.param((1, 256, 50, 68), 32, marks=pytest.mark.xfail(reason="see #555")),
        pytest.param((1, 256, 25, 34), 32, marks=pytest.mark.xfail(reason="see #555")),
        pytest.param((1, 256, 13, 17), 32, marks=pytest.mark.xfail(reason="see #555")),
        pytest.param((1, 256, 7, 9), 32, marks=pytest.mark.xfail(reason="see #555")),
    ],
)
def test_group_norm(device, input_shape, num_groups):
    m = GroupNormModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    weight = torch.ones(input_shape[1], dtype=torch.bfloat16)
    bias = torch.rand(input_shape[1], dtype=torch.bfloat16)
    result_before = m.forward(input, num_groups, weight, bias)
    option = torch_ttnn.TorchTtnnOption(device=device)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, num_groups, weight, bias)
    # option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(target_wrappers.group_norm) == 1
    # Check inference result
    assert_with_pcc(result_before, result_after, 0.9997)

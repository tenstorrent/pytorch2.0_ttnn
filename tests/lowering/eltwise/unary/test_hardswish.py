# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class HardSwishModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.nn.functional.hardswish(x)


@pytest.mark.parametrize(
    "input_shape",
    (
        (1, 16, 160, 160),
        (1, 240, 40, 40),
        (1, 240, 20, 20),
        (1, 200, 20, 20),
        (1, 184, 20, 20),
        (1, 480, 20, 20),
        (1, 672, 20, 20),
        (1, 672, 10, 10),
        (1, 480, 10, 10),
        (1, 16, 112, 112),
        (1, 240, 28, 28),
        (1, 240, 14, 14),
        (1, 200, 14, 14),
        (1, 184, 14, 14),
        (1, 480, 14, 14),
        (1, 672, 14, 14),
        (1, 672, 7, 7),
        (1, 960, 7, 7),
        (1, 1280),
        (1, 96, 28, 28),
        (1, 96, 14, 14),
        (1, 120, 14, 14),
        (1, 144, 14, 14),
        (1, 288, 14, 14),
        (1, 288, 7, 7),
        (1, 576, 7, 7),
        (1, 1024),
        (2, 3, 4, 5),
        (7, 7, 7),
        (420, 69),
        (1337,),
    ),
)
def test_hardswish(device, input_shape):
    m = HardSwishModule()
    input_tensor = torch.rand(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input_tensor)
    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True)

    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input_tensor)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and not contain aten ops
    targets = (*(node.target for node in option._out_fx_graphs[0].nodes),)
    assert torch.ops.aten.hardswish.default not in targets
    assert targets.count(ttnn.hardswish) == 1

    # Check inference result
    assert_with_pcc(result_before, result_after)

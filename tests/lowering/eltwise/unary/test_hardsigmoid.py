# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class HardSigmoidModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.nn.functional.hardsigmoid(x)


@pytest.mark.parametrize(
    "input_shape",
    (
        (1, 72, 1, 1),
        (1, 120, 1, 1),
        (1, 480, 1, 1),
        (1, 672, 1, 1),
        (1, 256, 1, 1),
        (1, 512, 1, 1),
        (1, 768, 1, 1),
        (1, 1024, 1, 1),
        (1, 960, 1, 1),
        (1, 16, 1, 1),
        (1, 96, 1, 1),
        (1, 240, 1, 1),
        (1, 144, 1, 1),
        (1, 288, 1, 1),
        (1, 576, 1, 1),
        (2, 3, 4, 5),
        (7, 7, 7),
        (420, 69),
        (1337,),
    ),
)
def test_hardsigmoid(device, input_shape):
    m = HardSigmoidModule()
    input_tensor = torch.rand(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input_tensor)
    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True)

    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input_tensor)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and not contain aten ops
    targets = (*(node.target for node in option._out_fx_graphs[0].nodes),)
    assert torch.ops.aten.hardsigmoid.default not in targets
    assert targets.count(ttnn.hardsigmoid) == 1

    # Check inference result
    assert_with_pcc(result_before, result_after)

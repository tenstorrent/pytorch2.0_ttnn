# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import pytest
import torch
import ttnn
import torch_ttnn


class AsStridedModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, size, stride):
        return torch.as_strided(x, size, stride)


@pytest.mark.parametrize(
    "input_shape, size, stride",
    (
        ((1, 1024, 1, 1), (1, 1024, 1, 1), (1024, 1, 1024, 1024)),
        ((1, 112, 14, 14), (1, 112, 14, 14), (21952, 196, 14, 1)),
        ((1, 16, 112, 112), (1, 16, 112, 112), (200704, 12544, 112, 1)),
        ((1, 160, 7, 7), (1, 160, 7, 7), (7840, 49, 7, 1)),
        ((1, 24, 56, 56), (1, 24, 56, 56), (75264, 3136, 56, 1)),
        ((1, 40, 28, 28), (1, 40, 28, 28), (31360, 784, 28, 1)),
        ((1, 768, 1, 1), (1, 768, 1, 1), (768, 1, 768, 768)),
        ((1, 80, 14, 14), (1, 80, 14, 14), (15680, 196, 14, 1)),
        ((15680,), (1, 80, 14, 14), (15680, 196, 14, 1)),
        ((15680,), (80, 14, 14), (196, 14, 1)),
        ((200704,), (1, 16, 112, 112), (200704, 12544, 112, 1)),
        ((200704,), (16, 112, 112), (12544, 112, 1)),
        ((21952,), (1, 112, 14, 14), (21952, 196, 14, 1)),
        ((21952,), (112, 14, 14), (196, 14, 1)),
        ((31360,), (1, 40, 28, 28), (31360, 784, 28, 1)),
        ((31360,), (40, 28, 28), (784, 28, 1)),
        ((75264,), (1, 24, 56, 56), (75264, 3136, 56, 1)),
        ((75264,), (24, 56, 56), (3136, 56, 1)),
        ((7840,), (1, 160, 7, 7), (7840, 49, 7, 1)),
        ((7840,), (160, 7, 7), (49, 7, 1)),
    ),
)
def test_as_strided(device, input_shape, size, stride):
    m = AsStridedModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input, size, stride)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, size, stride)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = [node.target for node in option._out_fx_graphs[0].nodes]
    assert torch.ops.aten.as_strided.default not in nodes
    assert nodes.count(ttnn.reshape) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after)

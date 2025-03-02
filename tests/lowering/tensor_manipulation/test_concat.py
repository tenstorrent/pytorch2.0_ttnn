# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import pytest
import torch
import ttnn
import torch_ttnn


class ConcatModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, dim):
        out_relu = torch.ops.aten.relu.default(x2)
        return torch.cat((x1, out_relu), dim)


@pytest.mark.parametrize(
    "input_shapes, dim",
    [
        (((1, 128, 28, 28), (1, 19, 28, 28)), 1),
    ],
)
def test_concat(device, input_shapes, dim):
    m = ConcatModule()
    inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
    result_before = m.forward(*inputs, dim)
    option = torch_ttnn.TorchTtnnOption(device=device)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs, dim)
    print(option._out_fx_graphs[0])

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.concat) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after)

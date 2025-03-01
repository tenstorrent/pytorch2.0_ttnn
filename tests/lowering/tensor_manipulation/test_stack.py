# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import pytest
import torch
import ttnn
import torch_ttnn


class StackModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, tensors, dim):
        return torch.stack(tensors, dim)


@pytest.mark.parametrize(
    "input_shape, dim",
    [
        ((12, 16), -1),
        ((12, 16), 1),
        ((12, 16), 0),
        ((3, 16, 12), 0),
        ((3, 16, 12), -1),
        ((3, 16, 12), 1),
        ((3, 16, 12), 2),
    ],
)
def test_stack(device, input_shape, dim):
    m = StackModule()
    inputs = [torch.rand(input_shape, dtype=torch.bfloat16) for _ in range(2)]
    result_before = m.forward(inputs, dim)
    option = torch_ttnn.TorchTtnnOption(device=device)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(inputs, dim)
    print(option._out_fx_graphs[0])

    # Check the graph has be rewritten and contain ttnn ops
    nodes = [node.target for node in option._out_fx_graphs[0].nodes]
    assert nodes.count(torch.ops.aten.stack.default) == 0

    # Check inference result
    assert torch.allclose(result_before, result_after)

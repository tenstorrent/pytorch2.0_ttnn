# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest
import ttnn


class BitwiseAndModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, y):
        return torch.bitwise_and(x, y)


@pytest.mark.parametrize(
    "input_shapes, dtype",
    [
        (((32, 32), (32, 32)), torch.bool),
        (((32, 1), (32, 32)), torch.bool),
        (((32, 32), (1, 1, 32)), torch.bool),
        (((32, 32), (32, 1, 32)), torch.bool),
        (((32, 32), (32, 32)), torch.int32),
    ],
)
def test_bitwise_and(device, input_shapes, dtype):
    m = BitwiseAndModule()

    if dtype == torch.bool:
        inputs = [torch.randint(0, 2, shape, dtype=dtype) for shape in input_shapes]
    else:
        inputs = [torch.randint(-100, 100, shape, dtype=dtype) for shape in input_shapes]

    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has been rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    node_targets = [node.target for node in nodes]

    # Should have either ttnn.logical_and (for bool) or ttnn.bitwise_and (for int)
    assert node_targets.count(ttnn.logical_and) + node_targets.count(ttnn.bitwise_and) >= 1

    # Check inference result
    assert torch.allclose(result_before.to(dtype), result_after.to(dtype))

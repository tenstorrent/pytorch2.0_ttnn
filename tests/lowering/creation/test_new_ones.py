# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest
import ttnn


class NewOnesModule(torch.nn.Module):
    def __init__(self, size, dtype=None):
        super().__init__()
        self.size = size
        self.dtype = dtype

    def forward(self, x):
        if self.dtype:
            return x.new_ones(self.size, dtype=self.dtype)
        else:
            return x.new_ones(self.size)


@pytest.mark.parametrize(
    "input_shape, new_size, dtype",
    [
        ((4, 4), (32,), torch.bool),
        ((4, 4), (32,), None),
        ((1, 45), (1, 1), None),
        ((1, 32), (32,), torch.float32),
    ],
)
def test_new_ones(device, input_shape, new_size, dtype):
    m = NewOnesModule(new_size, dtype)
    input_tensor = torch.randn(input_shape)

    result_before = m.forward(input_tensor)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input_tensor)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has been rewritten and doesn't contain aten.new_ones
    nodes = list(option._out_fx_graphs[0].nodes)
    node_targets = [node.target for node in nodes]

    # Should not have aten.new_ones, should have been decomposed
    assert torch.ops.aten.new_ones.default not in node_targets

    # Check inference result
    assert torch.allclose(result_before.to(torch.float32), result_after.to(torch.float32))

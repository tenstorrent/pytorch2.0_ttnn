# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import pytest
import random
import torch
import torch_ttnn


class NewFullModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, tensor, size, value, dtype):
        return torch.ops.aten.new_full.default(tensor, size, value, dtype=dtype)


@pytest.mark.parametrize(
    "input_shape, input_dtype, size, dtype",
    [
        ((64, 128), torch.bfloat16, (32, 32), torch.bfloat16),
        ((1, 256, 128, 128), torch.float32, (1, 256, 16, 16), torch.bfloat16),
        ((1, 960, 7, 7), torch.bfloat16, (1, 256, 3, 3), None),
        ((3, 800, 1066), torch.bfloat16, (1, 3, 800, 1088), None),
    ],
)
def test_new_full(device, input_shape, input_dtype, size, dtype):
    m = NewFullModule()
    tensor = torch.rand(input_shape, dtype=input_dtype)
    value = 0.5
    result_before = m.forward(tensor, size, value, dtype)
    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(tensor, size, value, dtype)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    # Check the graph has be rewritten and aten ops are replaced
    assert not any(node.target == torch.ops.aten.new_full.default for node in nodes)
    # Check inference result
    assert result_before.dtype == result_after.dtype
    assert torch.allclose(result_before, result_after)

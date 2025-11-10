# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class FreshLiftCopyModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        tensor = torch.tensor(1.0, dtype=torch.bfloat16)
        return tensor - x


@pytest.mark.parametrize(
    "batch_size",
    [2],
)
@pytest.mark.parametrize(
    "shape",
    [(1, 9, 9)],
)
def test_torch_scalar_sub_fresh(device, batch_size, shape):
    m = FreshLiftCopyModule()
    input_shape = (batch_size,) + shape
    tensor = torch.rand(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(tensor)
    option = torch_ttnn.TorchTtnnOption(device=device)
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(tensor)

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.sub) == 1
    # Check inference result
    assert_with_pcc(result_before, result_after, 0.99)

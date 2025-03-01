# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class IndexModule(torch.nn.Module):
    def __init__(self, op):
        super().__init__()
        self.op = op

    def forward(self, input, indices):
        return self.op(input, indices)


@pytest.mark.parametrize(
    "input_shapes, indices, converted",
    [
        ((3, 4), [[[0, 1], [1, 2]]], "embedding"),
        ((3, 4, 5), [[0, 1], [2, 1], [2, 4]], False),
        ((3, 4, 5), [[0, 1], [2, 1]], False),
        ((3, 4, 5), [[[0, 1]], [[2, 1]]], False),
        ((3, 4, 5), [[[0, 1, 1]], [[2, 1, 2]]], False),
        ((3, 4, 5), [[[0, 1, 1], [1, 1, 0]], [[2, 1, 2]]], False),  # broadcast
    ],
)
@pytest.mark.parametrize("op", [torch.ops.aten.index.Tensor, torch.ops.aten._unsafe_index.Tensor])
def test_index(device, op, input_shapes, indices, converted):
    m = IndexModule(op)
    inputs = torch.rand(input_shapes, dtype=torch.bfloat16)
    indices = [torch.tensor(index) for index in indices]
    result_before = m.forward(inputs, indices)

    option = torch_ttnn.TorchTtnnOption(device=device)
    # option.gen_graphviz = True

    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)

    result_after = m.forward(inputs, indices)
    # option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    if converted == "embedding":
        nodes = [node.target for node in option._out_fx_graphs[0].nodes]
        assert op not in nodes
        assert ttnn.embedding in nodes

    # Check inference result
    assert_with_pcc(result_before, result_after, pcc=0.99)

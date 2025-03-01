# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest
import ttnn


class LogSoftmaxModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, axis):
        return torch.log_softmax(x, axis)


@pytest.mark.parametrize(
    "input_shapes",
    [[(1, 1, 64, 32)]],
)
def test_log_softmax(device, input_shapes):
    m = LogSoftmaxModule()
    inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
    axis = -1
    result_before = m.forward(*inputs, axis)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs, axis)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    targets = [node.target for node in nodes]
    assert targets.count(ttnn.softmax) == 1
    assert targets.count(ttnn.log) == 1
    assert targets.index(ttnn.softmax) < targets.index(ttnn.log)
    # Check inference result
    assert torch.allclose(result_before, result_after, rtol=0.2)

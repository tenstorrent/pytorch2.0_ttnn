# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest
import ttnn


class SqueezeDimModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, dim):
        return torch.squeeze(input, dim)


@pytest.mark.parametrize(
    "input_shape, dim",
    [
        ((1, 32, 16), 0),
        ((1, 256, 1), -1),
        ((33, 44, 1, 32, 16), 1),
        ((33, 44, 1, 32, 16), 2),
        ((1, 12), 0),
        ((1), 0),
        ((), 0),
    ],
)
def test_squeeze_dim(device, input_shape, dim):
    m = SqueezeDimModule()
    inputs = torch.zeros(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(inputs, dim)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(inputs, dim)
    option._out_fx_graphs[0].print_tabular()
    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    if option.use_less_ttnn_op_types:
        # squeeze is lowered to reshape
        assert [node.target for node in nodes].count(ttnn.reshape) == 1
    else:
        assert [node.target for node in nodes].count(ttnn.squeeze) == 1
    # TODO: use following line when we update tt-metal
    # assert [node.target for node in nodes].count(ttnn.squeeze) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after)


class SqueezeNoneDimModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input):
        return torch.squeeze(input)


@pytest.mark.parametrize(
    "input_shape",
    [
        ((64, 1, 32, 16, 1, 32, 32)),
        ((1, 1, 55, 23, 44, 32, 32)),
        ((22, 1, 55, 23, 44, 32, 1)),
        ((1, 1, 55, 1, 1, 1, 1)),
        ((1, 12)),
        ((1, 1)),
        ((1)),
        (()),
    ],
)
def test_squeeze_none_dim(device, input_shape):
    m = SqueezeNoneDimModule()
    inputs = torch.zeros(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(inputs)
    option._out_fx_graphs[0].print_tabular()
    # Check the graph has be rewritten and contain ttnn ops (squeeze without provided dim is lowered to reshape)
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.reshape) == 1
    # TODO: use following line when we update tt-metal
    # assert [node.target for node in nodes].count(ttnn.squeeze) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after)

# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest
import ttnn
from tests.utils import assert_with_pcc


class RoundModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        return torch.round(*args, **kwargs)


@pytest.mark.skip_platform("grayskull")
@pytest.mark.parametrize(
    "input_shape",
    (
        (1, 1, 1, 42),
        (1, 1, 32, 1),
        (4, 4),
        (4, 32),
        (1066,),
    ),
)
def test_round_default(device, input_shape):
    m = RoundModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16) * 20 - 10
    result_before = m.forward(input)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input)
    option._out_fx_graphs[0].print_tabular()
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.round) == 1
    assert_with_pcc(result_before, result_after, 0.99)


@pytest.mark.skip_platform("grayskull")
@pytest.mark.parametrize(
    "input_shape, decimals",
    (
        ((1, 1, 1, 42), 1),
        ((1, 1, 32, 1), 2),
        ((4, 4), 3),
        ((4, 32), 0),
        ((1066,), 2),
        ((1066,), 1),
        ((1066,), 0),
        pytest.param(
            (1066,),
            -1,
            # NOTE(jdh8): skip instead of xfail because it takes a long time
            marks=pytest.mark.skip(reason="decimals < 0 not supported (until tt-metal#13851?)"),
        ),
    ),
)
def test_round_decimals(device, input_shape, decimals):
    m = RoundModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16) * 20 - 10
    result_before = m.forward(input, decimals=decimals)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, decimals=decimals)
    option._out_fx_graphs[0].print_tabular()
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.round) == 1
    assert_with_pcc(result_before, result_after, 0.99)

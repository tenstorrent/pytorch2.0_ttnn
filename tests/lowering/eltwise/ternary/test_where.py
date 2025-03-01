# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest
import ttnn


class WhereModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, cond, then, other):
        return then.where(cond, other)


@pytest.mark.parametrize(
    "input_shapes",
    (
        ((8, 8), (8, 8), (8, 8)),
        ((8, 8), (8, 1), (8, 8)),
        ((8, 8), (8, 1), (1, 8)),
        ((8, 8), (1, 1), (1, 8)),
        pytest.param(
            ((8, 1), (1, 1), (1, 8)),
            marks=pytest.mark.xfail(reason="broadcasting issues (#64)"),
        ),
        pytest.param(
            ((1, 1, 7, 7), (1, 12, 7, 7), ()),
            marks=pytest.mark.xfail(reason="ttnn.where cannot handle 0-D tensors (tt-metal#16254)"),
        ),
        pytest.param(
            ((1, 1, 45, 45), (1, 12, 45, 45), ()),
            marks=pytest.mark.xfail(reason="ttnn.where cannot handle 0-D tensors (tt-metal#16254)"),
        ),
        pytest.param(
            ((1, 1, 1, 46), (1, 12, 1, 46), ()),
            marks=pytest.mark.xfail(reason="ttnn.where cannot handle 0-D tensors (tt-metal#16254)"),
        ),
        pytest.param(
            ((1, 1, 5, 5), (1, 16, 5, 5), ()),
            marks=pytest.mark.xfail(reason="ttnn.where cannot handle 0-D tensors (tt-metal#16254)"),
        ),
        pytest.param(
            ((1, 1, 1, 6), (1, 16, 1, 6), ()),
            marks=pytest.mark.xfail(reason="ttnn.where cannot handle 0-D tensors (tt-metal#16254)"),
        ),
        pytest.param(
            ((1, 1, 256), (1, 1, 256), ()),
            marks=pytest.mark.xfail(reason="ttnn.where cannot handle 0-D tensors (tt-metal#16254)"),
        ),
        ((1, 1, 7, 7), (1, 12, 7, 7), (1,)),
        ((1, 1, 45, 45), (1, 12, 45, 45), (1,)),
        ((1, 1, 1, 46), (1, 12, 1, 46), (1,)),
        ((1, 1, 5, 5), (1, 16, 5, 5), (1,)),
        ((1, 1, 1, 6), (1, 16, 1, 6), (1,)),
        ((1, 1, 256), (1, 1, 256), (1,)),
        ((1, 1),) * 3,
        ((10, 10),) * 3,
        ((15, 15),) * 3,
        ((17, 17),) * 3,
        ((2, 2),) * 3,
    ),
)
def test_where(device, input_shapes):
    m = WhereModule()
    inputs = [torch.randint(0, 2, shape).type(torch.bfloat16) for shape in input_shapes]
    inputs[0] = inputs[0].to(torch.bool)
    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.where) == 1

    # Check inference result
    assert torch.allclose(result_before, result_after)

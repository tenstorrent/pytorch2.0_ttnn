# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn


class MutationModel(torch.nn.Module):
    def forward(self, dummy_input):
        mask = torch.full((32, 32), 1)
        mask_cond = torch.full((32, 32), True)
        masked_fill = mask.masked_fill_(mask_cond, 0)
        mask_1 = mask.to(torch.bfloat16)
        result = dummy_input + mask_1
        return result


def test_mutation(device):
    m = MutationModel()
    option = torch_ttnn.TorchTtnnOption(device=device)
    # Dummy input to force `insert_clones_for_input_aliasing` to modify graph
    dummy_input = torch.rand((32, 32), dtype=torch.bfloat16)
    result_before = m(dummy_input)
    # The compilation is lazy, so we need to run forward once to trigger the compilation

    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m(dummy_input)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)

    # Check inference result
    assert torch.allclose(result_before, result_after)

# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest


class CopyModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, self_tensor, src_tensor):
        self_tensor.copy_(src_tensor)
        add = self_tensor + self_tensor
        return add


@pytest.mark.parametrize(
    "input_shapes",
    [((1, 19), (1, 19))],
)
def test_clone_from_arg(device, input_shapes):
    m = CopyModule()
    inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
    # clone these inputs to use for compiled model because tensor.copy_ is in-place
    inputs_cloned = [torch.clone(tensor) for tensor in inputs]

    result_before = m.forward(*inputs)
    assert torch.allclose(inputs[0], inputs[1])

    option = torch_ttnn.TorchTtnnOption(device=device)

    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs_cloned)
    assert torch.allclose(inputs_cloned[0], inputs_cloned[1])

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(torch.ops.aten.copy.default) == 0
    # Check inference result
    assert torch.allclose(result_before, result_after)

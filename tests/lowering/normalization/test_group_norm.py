import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class GroupNormModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, embedding, num_groups, weight, bias):
        return torch.nn.functional.group_norm(
            embedding, num_groups=num_groups, weight=weight, bias=bias
        )


@pytest.mark.parametrize(
    "num_groups, batch, sentence_length, embedding_dim",
    [(3, 20, 6, 10)],
)
def test_group_norm(device, num_groups, batch, sentence_length, embedding_dim):
    m = GroupNormModule()
    input_shapes = [
        (batch, sentence_length, embedding_dim),
        (sentence_length),
        (sentence_length),
    ]
    inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
    inputs.insert(1, num_groups)
    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.group_norm) == 1
    # Check inference result
    assert_with_pcc(result_before, result_after, 0.9998)

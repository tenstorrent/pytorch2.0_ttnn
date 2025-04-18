import torch
import torch_ttnn
import pytest
import ttnn


class EmbeddingBagModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, weight, offsets=None, mode="mean"):
        return torch.nn.functional.embedding_bag(input, weight, offsets, mode=mode)


@pytest.mark.parametrize(
    "input_shape, weight_shape, offsets, mode",
    (
        ((8,), (10, 3), (0, 4), "mean"),
        ((8, 4), (10, 3), None, "mean"),
    ),
)
def test_embedding_bag(device, input_shape, weight_shape, offsets, mode):
    input_tensor = torch.randint(1, 5, input_shape).type(torch.long)
    weight_tensor = torch.randn(weight_shape).type(torch.bfloat16)
    offsets_tensor = torch.tensor(offsets).type(torch.long) if offsets else None
    inputs = input_tensor, weight_tensor, offsets_tensor, mode

    model = EmbeddingBagModule()
    result_before = model.forward(*inputs)

    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    model = torch.compile(model, backend=torch_ttnn.backend, options=option)
    result_after = model.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.embedding) == 1

    # Check inference result
    assert torch.allclose(result_before, result_after)

import torch
import torch_ttnn
import pytest
import ttnn


class EmbeddingModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, weight):
        embedding = torch.nn.Embedding.from_pretrained(weight)
        return embedding(input)


class EmbeddingTileLayoutModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, weights):
        return torch.nn.functional.embedding(input, weights)


# NOTE(kevinwuTT) Re-enable after conversion to ttnn.embedding with both ROW_MAJOR_LAYOUT and TILE_LAYOUT
@pytest.mark.xfail
@pytest.mark.parametrize(
    "input_shapes",
    [[((1, 2, 4, 5), (4, 3, 2, 9)), (10, 4)]],
)
def test_embedding(device, input_shapes):
    m = EmbeddingModule()
    input_shapes = m.input_shapes()
    input = torch.tensor(input_shapes[0])
    weight = torch.rand(input_shapes[1], dtype=torch.bfloat16)
    result_before = m.forward(input, weight)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, weight)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.embedding) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after)


@pytest.mark.parametrize(
    "batch_size, sentence_size, vocabulary_size, hidden_embedding_dim",
    [
        (8, 384, 250880, 1024),
    ],
)
def test_embedding_tile_layout(device, batch_size, sentence_size, vocabulary_size, hidden_embedding_dim):
    m = EmbeddingTileLayoutModule()
    input = torch.randint(batch_size, vocabulary_size - 1, (batch_size, sentence_size))
    weights = torch.zeros((vocabulary_size, hidden_embedding_dim), dtype=torch.bfloat16).uniform_(-0.1, 0.1)
    result_before = m.forward(input, weights)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, weights)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.embedding) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after)


@pytest.mark.parametrize(
    "batch, sentence_size, vocabulary_size, hidden_embedding_dim, converted",
    [
        (1, 384, 160, 1024, True),
        (8, 384, 256, 512, True),
        # TODO(#248): Not support vocabulary size > 256
        (8, 384, 512, 1024, False),
    ],
)
def test_embedding_backward_tile_layout(device, batch, sentence_size, vocabulary_size, hidden_embedding_dim, converted):
    m = EmbeddingTileLayoutModule()
    input = torch.randint(0, vocabulary_size, (batch, sentence_size), dtype=torch.int64)
    weights = torch.rand((vocabulary_size, hidden_embedding_dim), dtype=torch.bfloat16)
    grad_data = torch.rand((batch, sentence_size, hidden_embedding_dim))

    weights_before = weights.clone().detach().requires_grad_(True)
    m.forward(input, weights_before).backward(gradient=grad_data)

    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    weights_after = weights.clone().detach().requires_grad_(True)
    m.forward(input, weights_after).backward(gradient=grad_data)

    # Check the graph has be rewritten
    nodes = list(option._out_fx_graphs[-1].nodes)
    assert [node.target for node in nodes].count(ttnn.embedding_bw) == (1 if converted else 0)
    # Check inference result
    assert weights_before.grad.shape == weights_after.grad.shape
    # Multiple float multiplications needs a higher tolerance
    assert torch.allclose(weights_before.grad, weights_after.grad, rtol=0.1)

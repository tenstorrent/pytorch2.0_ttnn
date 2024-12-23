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


@pytest.mark.parametrize(
    "input_shapes",
    [[((1, 2, 4, 5), (4, 3, 2, 9)), (10, 4)]],
)
def test_embedding(device, input_shapes):
    m = EmbeddingModule()
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
        (8, 384, 2048, 768),
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
    "batch_size, sentence_size, vocabulary_size, hidden_embedding_dim",
    [
        (1, 8, 30528, 768),
        (1, 8, 2048, 768),
    ],
)
def test_embedding_squeezebert(device, batch_size, sentence_size, vocabulary_size, hidden_embedding_dim):
    input = torch.randint(0, vocabulary_size - 1, (batch_size, sentence_size))
    weights = torch.zeros((vocabulary_size, hidden_embedding_dim), dtype=torch.bfloat16).uniform_(-0.1, 0.1)

    m = EmbeddingModule()
    result_before = m.forward(input, weights)

    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, weights)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(
        ttnn.embedding
    ) == 1, "Compiled graph does not contain ttnn.embedding; likely torch fallback OP was used instead."

    # Check inference result
    assert torch.allclose(result_before, result_after)

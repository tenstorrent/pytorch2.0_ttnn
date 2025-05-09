# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class LayerNormModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, embedding, weight, bias):
        return torch.nn.functional.layer_norm(
            embedding, normalized_shape=[embedding.shape[-1]], weight=weight, bias=bias
        )


class LayerNormWithOtherOpModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, embedding, weight, bias):
        layer_norm = torch.nn.functional.layer_norm(
            embedding, normalized_shape=[embedding.shape[-1]], weight=weight, bias=bias
        )
        return layer_norm + layer_norm


@pytest.mark.parametrize(
    "batch, sentence_length, embedding_dim",
    [(2, 32, 64)],
)
def test_layer_norm(device, batch, sentence_length, embedding_dim):
    m = LayerNormModule()
    input_shapes = [
        (batch, sentence_length, embedding_dim),
        (embedding_dim),
        (embedding_dim),
    ]
    inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert not any(node.target == torch.ops.aten.native_layer_norm.default for node in nodes)
    # Check inference result
    assert_with_pcc(result_before, result_after, 0.9998)


@pytest.mark.parametrize(
    "batch, sentence_length, embedding_dim",
    [(2, 32, 64)],
)
def test_layer_norm_with_other_op(device, batch, sentence_length, embedding_dim):
    m = LayerNormWithOtherOpModule()
    input_shapes = [
        (batch, sentence_length, embedding_dim),
        (embedding_dim),
        (embedding_dim),
    ]
    inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert not any(node.target == torch.ops.aten.native_layer_norm.default for node in nodes)
    # Check inference result
    assert_with_pcc(result_before, result_after, 0.9998)


@pytest.mark.parametrize(
    "batch, sentence_length, embedding_dim",
    [(2, 32, 64)],
)
def test_layer_norm_train(device, batch, sentence_length, embedding_dim):
    m = LayerNormModule()
    input_shapes = [
        (batch, sentence_length, embedding_dim),
        (embedding_dim),
        (embedding_dim),
    ]
    dldy = torch.rand((batch, sentence_length, embedding_dim), dtype=torch.bfloat16)
    inputs = [torch.rand(shape, dtype=torch.bfloat16, requires_grad=True) for shape in input_shapes]
    inputs_ttnn = [i.clone() for i in inputs]
    result_before = m.forward(*inputs)
    result_before.backward(dldy)

    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs_ttnn)
    result_after.backward(dldy)

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert not any(node.target == torch.ops.aten.native_layer_norm.default for node in nodes)
    # Check inference result
    assert_with_pcc(result_before, result_after, 0.9998)
    assert_with_pcc(inputs[0], inputs_ttnn[0], 0.9998)
    assert_with_pcc(inputs[1], inputs_ttnn[1], 0.9998)
    assert_with_pcc(inputs[2], inputs_ttnn[2], 0.9998)


class AtenNativeLayerNormModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input_tensor, normalized_shape, weight, bias, epsilon):
        return torch.ops.aten.native_layer_norm.default(input_tensor, normalized_shape, weight, bias, epsilon)


@pytest.mark.parametrize(
    "batch, sentence_length, embedding_dim, normalized_dims, eps",
    [(2, 32, 64, 1, 1e-5)],
)
def test_aten_native_layer_norm(device, batch, sentence_length, embedding_dim, normalized_dims, eps):
    m = AtenNativeLayerNormModule()

    input_shapes = [
        (batch, sentence_length, embedding_dim),
        (embedding_dim),
        (embedding_dim),
    ]

    input_tensor, weight, bias = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
    normalized_shape = input_tensor.shape[-normalized_dims:]

    outputs_before = m.forward(input_tensor, normalized_shape, weight, bias, eps)

    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    outputs_after = m.forward(input_tensor, normalized_shape, weight, bias, eps)

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert not any(node.target == torch.ops.aten.native_layer_norm.default for node in nodes)
    # Check inference result
    assert len(outputs_before) == len(outputs_after)
    # output
    assert_with_pcc(outputs_before[0], outputs_after[0], 0.9998)
    # mean, can pcc be improved to 0.9998?
    assert_with_pcc(outputs_before[1], outputs_after[1], 0.998)
    # rstd, can pcc be improved to 0.9998?
    assert_with_pcc(outputs_before[2], outputs_after[2], 0.998)

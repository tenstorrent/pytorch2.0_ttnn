import pytest
import torch
import torch_ttnn
import ttnn

from tests.utils import assert_with_pcc


class ScaledDotProductAttentionModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        return torch.nn.functional.scaled_dot_product_attention(*args, **kwargs)


def rand_in_range(shape, a, b, dtype=torch.bfloat16):
    rand_tensor = torch.rand(*shape, dtype=dtype)
    return a + rand_tensor * (b - a)

@pytest.mark.parametrize(
    "input_shape, is_causal",
    (
        ((1, 16, 197, 64), False),
        ((1, 12, 197, 64), False),
        ((1, 16, 50, 64), False),
        ((1, 8, 4096, 40), False),
        ((1, 8, 1024, 80), False),
        ((1, 8, 256, 160), False),
        ((1, 8, 64, 160), False),
        ((1, 12, 50, 64), False),
        ((1, 16, 1370, 80), False),
        ((1, 12, 1, 64), False),
        ((1, 12, 4, 64), True),
    ),
)
def test_sdpa(device, input_shape, is_causal):
    module = ScaledDotProductAttentionModule()
    # Values must be centered around 0 to avoid accuracy issues
    query = rand_in_range(input_shape, -10.0, 10.0, dtype=torch.bfloat16)
    key = rand_in_range(input_shape, -10.0, 10.0, dtype=torch.bfloat16)
    value = rand_in_range(input_shape, -10.0, 10.0, dtype=torch.bfloat16)
    result_before = module.forward(query, key, value, is_causal=is_causal)

    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=False)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    module = torch.compile(module, backend=torch_ttnn.backend, options=option)
    result_after = module.forward(query, key, value, is_causal=is_causal)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = [node.target for node in option._out_fx_graphs[0].nodes]
    assert torch.ops.aten._scaled_dot_product_flash_attention.default not in nodes
    assert nodes.count(ttnn.transformer.scaled_dot_product_attention) == 1
    assert_with_pcc(result_before, result_after, 0.99)

import torch
import torch_ttnn
import pytest
import ttnn


class SplitModule(torch.nn.Module):
    def __init__(self, split_size_or_sections, dim):
        super().__init__()
        self.split_size_or_sections = split_size_or_sections
        self.dim = dim

    def forward(self, input):
        return torch.split(input, self.split_size_or_sections, self.dim)


@pytest.mark.parametrize(
    "input_shape, split_size_or_sections, dim",
    (
        ((1, 4, 16, 32), 8, 3),
        ((1, 4, 16, 32), 4, 2),
        ((1, 4, 16, 32), (8, 8), 2),
    ),
)
def test_split(device, input_shape, split_size_or_sections, dim):
    m = SplitModule(split_size_or_sections, dim)
    input_tensor = torch.randn(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input_tensor)
    option = torch_ttnn.TorchTtnnOption(device=device)
    # option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input_tensor)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has been rewritten and contains ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.split) == 1

    # Check inference result
    for res_before, res_after in zip(result_before, result_after):
        assert torch.allclose(res_before, res_after)

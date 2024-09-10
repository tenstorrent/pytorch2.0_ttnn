import torch
import torch_ttnn
import pytest
import ttnn


class SelectModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, dim, index):
        return torch.select(input, dim, index)


@pytest.mark.parametrize(
    "input_shape, dim, index",
    (
        pytest.param((4, 32, 16, 2), 0, 2, marks=pytest.mark.xfail(reason="Buffer size and page size should be larger than 0 bytes!")),
        pytest.param((4, 32, 16), 0, 2, marks=pytest.mark.xfail(reason="ttnn.slice only supports 4D tensors")),
        pytest.param((4, 32, 16, 2), 1, 15, marks=pytest.mark.xfail(reason="ttnn.squeeze only supports dim=0")),
        pytest.param((4, 32, 16, 2), 2, 10, marks=pytest.mark.xfail(reason="ttnn.squeeze only supports dim=0")),
    ),
)
def test_select(device, input_shape, dim, index):
    m = SelectModule()
    input_tensor = torch.zeros(input_shape, dtype=torch.bfloat16)
    result_before = m.forward(input_tensor, dim, index)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input_tensor, dim, index)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has been rewritten and contains ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    # assert [node.target for node in nodes].count(ttnn.slice) == 1
    # Check inference result
    assert torch.allclose(result_before, result_after)

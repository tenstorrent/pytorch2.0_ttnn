import pytest
import torch
import torch_ttnn
import ttnn


class TopKModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, k, dim, largest, sorted):
        return input.topk(k, dim, largest, sorted)


@pytest.mark.parametrize(
    "input_shape, k, dim, largest, sorted",
    [
        ((1, 1, 4, 32), 32, -1, True, True),
        ((1, 16), 8, -1, True, True),
        ((256,), 24, -1, True, True),
        # TODO(#216): Incorrect indices
        pytest.param((24, 64), 32, -1, True, True, marks=pytest.mark.xfail(reason="Incorrect indices (#216)")),
        # TODO(#215): Not support k > 32
        pytest.param((128,), 50, -1, True, True, marks=pytest.mark.xfail(reason="Not support k > 32 (#215)")),
        # TODO(#215): Not support largest = false
        pytest.param((128,), 32, -1, False, True, marks=pytest.mark.xfail(reason="Not support largest = false (#215)")),
        # TODO(#215): Not support sorted = false
        pytest.param((128,), 32, -1, True, False, marks=pytest.mark.xfail(reason="Not support sorted = false (#215)")),
    ],
)
def test_topk(device, input_shape, k, dim, largest, sorted):
    m = TopKModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    exp = torch.rand(input_shape, dtype=torch.bfloat16)
    values_before, _ = m.forward(input, k, dim, largest, sorted)
    # print(torch.export.export(m, args=(input, k, dim, largest, sorted)))

    option = torch_ttnn.TorchTtnnOption(device=device, gen_graphviz=True)
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    values_after, indices_after = m.forward(input, k, dim, largest, sorted)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contains ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    assert [node.target for node in nodes].count(ttnn.topk) == 1
    # Check inference result
    assert torch.allclose(values_before, values_after)
    # Only check if the indices work as expected because precision error can result in big differences
    assert torch.allclose(torch.gather(input, dim, indices_after), values_after)

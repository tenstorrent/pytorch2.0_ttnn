import torch
import torch_ttnn
import pytest
import ttnn


class FloorModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.floor(x)


@pytest.mark.parametrize(
    "input_shape",
    [(4, 4)],
)
def test_floor(device, input_shape):
    m = FloorModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16) * 20 - 10
    result_before = m.forward(input)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input)
    option._out_fx_graphs[0].print_tabular()

    # This test will fallback to torch.ops.aten.floor.default
    nodes = list(option._out_fx_graphs[0].nodes)
    target = [node.target for node in nodes]
    if ttnn.device.is_grayskull:
        assert target.count(ttnn.floor) == 0
        assert target.count(torch.ops.aten.floor.default) == 1
    else:
        assert target.count(ttnn.floor) == 1
        assert target.count(torch.ops.aten.floor.default) == 0

    # Check inference result
    from tests.utils import assert_with_pcc

    assert_with_pcc(result_before, result_after)

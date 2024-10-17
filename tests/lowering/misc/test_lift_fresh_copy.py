import torch
import torch_ttnn
import pytest
import ttnn
from tests.utils import assert_with_pcc


class LiftFreshModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        lifted = torch.ops.aten.lift_fresh_copy.default(x)
        return lifted * x


@pytest.mark.parametrize(
    "input_shape",
    [(4, 4)],
)
def test_lift_fresh(device, input_shape):
    m = LiftFreshModule()
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    torch_result = m.forward(input)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    ttnn_result = m.forward(input)
    option._out_fx_graphs[0].print_tabular()

    nodes = list(option._out_fx_graphs[0].nodes)
    target = [node.target for node in nodes]
    # lift_fresh_copy is lowered to clone
    assert target.count(torch.ops.aten.lift_fresh_copy.default) == 0
    assert target.count(torch_ttnn.target_wrappers.clone) == 1
    assert_with_pcc(torch_result, ttnn_result, 0.99)

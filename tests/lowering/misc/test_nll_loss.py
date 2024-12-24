import torch
import torch_ttnn
import pytest
import ttnn

from tests.utils import assert_with_pcc


class NllLossModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        return torch.nn.functional.nll_loss(*args, **kwargs)


@pytest.mark.parametrize(
    "input_shape, has_weight, reduction, ignore_index",
    (
        ((19, 256008), True, "mean", -100),
        ((19, 256008), False, "mean", -100),
    ),
)
def test_nll_loss(device, input_shape, has_weight, reduction, ignore_index):
    module = NllLossModule()
    batch, channels = input_shape
    input = torch.rand((batch, channels), dtype=torch.bfloat16)
    input = torch.nn.functional.log_softmax(input, dim=1)

    target = torch.randint(0, channels, (batch,), dtype=torch.long)
    weight = torch.rand((channels,), dtype=torch.bfloat16) if has_weight else None
    result_before = module.forward(input, target, weight, reduction=reduction, ignore_index=ignore_index)

    option = torch_ttnn.TorchTtnnOption(device=device)

    # The compilation is lazy, so we need to run forward once to trigger the compilation
    module = torch.compile(module, backend=torch_ttnn.backend, options=option)

    result_after = module.forward(input, target, weight, reduction=reduction, ignore_index=ignore_index)
    print(option._out_fx_graphs[0])

    # Check the graph has be rewritten and contain ttnn ops
    nodes = [node.target for node in option._out_fx_graphs[0].nodes]
    assert torch.ops.aten.nll_loss_forward.default not in nodes
    assert nodes.count(ttnn.operations.moreh.nll_loss) == 1

    # Check inference result
    assert_with_pcc(result_before, result_after, pcc=0.99)

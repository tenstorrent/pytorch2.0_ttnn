import torch.linalg
import torch
from typing import List
import torch._dynamo

torch._dynamo.config.suppress_errors = False
torch._dynamo.config.verbose = True

try:
    import ttnn
except ImportError:
    print("ttnn is not installed, use mock_ttnn instead")
    import mock_ttnn as ttnn


# The backend for torch.compile that converts a graph to use ttnn.
# The "option" parameter is a dict that contains one key "torch_ttnn_option".
# The value of "torch_ttnn_option" is a TorchTtnnOption object.
# See document for detail.
def aten_backend(
    gm: torch.fx.GraphModule, example_inputs: List[torch.Tensor], options: dict
) -> torch.fx.GraphModule:
    """
    The backend for torch.compile that converts a graph to use ttnn.
    The graph is wrapped in torch._dynamo.backends.common.aot_autograd, which
    trace into low level ATen ops not only high level torch ops.
    """

    option: TorchTtnnOption = options["torch_ttnn_option"]
    torch.fx.graph._register_custom_builtin("device", "", option.device)

    # Rewrite with ttnn ops, will insert redundant data movement
    from torch.fx.passes.infra.pass_manager import PassManager
    from passes.to_tt_pass import ToTtPass
    from passes.add_data_move_pass import AddDataMovePass
    from passes.graphviz_pass import GraphvizPass
    from passes.eliminate_data_move_pass import EliminateDataMovePass
    from torch.fx.passes.dialect.common.cse_pass import CSEPass

    pm = PassManager(
        passes=[
            GraphvizPass("00-before"),
            ToTtPass(),
            GraphvizPass("01-rewrite"),
            AddDataMovePass(),
            GraphvizPass("02-add_data_move"),
            EliminateDataMovePass(),
            GraphvizPass("03-elimate_data_move"),
            CSEPass(),
            GraphvizPass("04-cse"),
        ]
    )
    gm, modified = pm(gm)

    gm.recompile()
    gm.graph.print_tabular()
    print(gm.code)
    option.out_fx_graph = gm.graph
    return gm


from torch._dynamo.backends.common import aot_autograd
from functools import partial


# The option for torch_ttnn.backend
class TorchTtnnOption:
    def __init__(self, device: ttnn.Device):
        self.device = device
        self.out_fx_graph = None


# The wrapper of aot_autograd that takes a TorchTtnnOption as options.
def backend(torch_ttnn_option: TorchTtnnOption):
    options = {"torch_ttnn_option": torch_ttnn_option}
    return aot_autograd(fw_compiler=partial(aten_backend, options=options))

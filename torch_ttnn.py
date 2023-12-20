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
    from passes.graphviz_pass import GraphvizPass
    from passes.eliminate_data_move_pass import EliminateDataMovePass
    from torch.fx.passes.dialect.common.cse_pass import CSEPass

    passes=[
        GraphvizPass("00-before"),
        ToTtPass(),
        GraphvizPass("01-rewrite"),
        EliminateDataMovePass(),
        GraphvizPass("02-eliminate"),
        CSEPass(),
        GraphvizPass("03-cse"),
    ]
    if option.enable_stat:
        assert option.model_name != "" and "should give the model_name"
        from passes.stat_pass import StatPass
        passes.append(StatPass(option.model_name))

    pm = PassManager(
        passes=passes
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
    def __init__(self, device: ttnn.Device, enable_stat = False, model_name: str = ""):
        self.device = device
        self.enable_stat = enable_stat
        self.model_name = model_name
        self.out_fx_graph = None


# The wrapper of aot_autograd that takes a TorchTtnnOption as options.
def backend(torch_ttnn_option: TorchTtnnOption):
    options = {"torch_ttnn_option": torch_ttnn_option}
    return aot_autograd(fw_compiler=partial(aten_backend, options=options))

import torch.linalg
import torch
from typing import List
import torch._dynamo
import os
from collections import Counter

torch._dynamo.config.suppress_errors = False
torch._dynamo.config.verbose = True

# The backend for torch.compile that statistics the graph information.
# The "option" parameter is a dict that contains one key "torch_stat_option".
# The value of "torch_stat_option" is a TorchStatOption object.
# See document for detail.
def aten_backend(
    gm: torch.fx.GraphModule, example_inputs: List[torch.Tensor], options: dict
) -> torch.fx.GraphModule:
    """
    The backend for torch.compile that statistics the graph information.
    The graph is wrapped in torch._dynamo.backends.common.aot_autograd, which
    trace into low level ATen ops not only high level torch ops.
    """

    option: TorchStatOption = options["torch_stat_option"]
    assert option.model_name != "" and "should give the model_name"


    # Rewrite with ttnn ops, will insert redundant data movement
    from torch.fx.passes.infra.pass_manager import PassManager
    from passes.stat_pass import StatPass

    passes = [StatPass(option.model_name, example_inputs, option.counter, option.out)]

    pm = PassManager(passes=passes)
    gm, modified = pm(gm)

    gm.recompile()
    option.out_fx_graph = gm.graph
    return gm


from torch._dynamo.backends.common import aot_autograd
from functools import partial


# The option for torch_stat.backend
class TorchStatOption:
    def __init__(self, model_name: str = "", out = os.path.join(os.getcwd(), "stat")):
        self.model_name = model_name
        self.out = out
        self.out_fx_graph = None
        self.counter = Counter()

# The wrapper of aot_autograd that takes a TorchStatOption as options.
def backend(torch_stat_option: TorchStatOption):
    options = {"torch_stat_option": torch_stat_option}
    return aot_autograd(fw_compiler=partial(aten_backend, options=options))

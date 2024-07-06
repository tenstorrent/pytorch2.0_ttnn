import torch
from torch_ttnn import fx_graphviz

try:
    import ttnn
except ImportError:
    print("ttnn is not installed, use mock_ttnn instead")
    from torch_ttnn import mock_ttnn as ttnn

from torch.fx.passes.infra.pass_base import PassBase, PassResult


class GraphvizPass(PassBase):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def call(self, gm: torch.fx.GraphModule):
        fx_graphviz.to_svg(gm.graph, self.filename)
        return PassResult(gm, False)

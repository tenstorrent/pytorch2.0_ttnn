import torch

try:
    import ttnn
except ImportError:
    print("ttnn is not installed, use mock_ttnn instead")
    import mock_ttnn as ttnn

from torch.fx.passes.infra.pass_base import PassBase, PassResult


class ToTtPass(PassBase):
    def call(self, gm: torch.fx.GraphModule):
        modified = False
        for node in gm.graph.nodes:
            if node.op != "call_function":
                continue
            if node.target == torch.ops.aten.add.Tensor:
                node.target = ttnn.add
                modified = True
            elif node.target == torch.ops.aten.mm.default:
                node.target = ttnn.matmul
                modified = True

        return PassResult(gm, modified)

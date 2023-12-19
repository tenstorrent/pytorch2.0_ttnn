import torch

try:
    import ttnn
except ImportError:
    print("ttnn is not installed, use mock_ttnn instead")
    import mock_ttnn as ttnn

from torch.fx.passes.infra.pass_base import PassBase, PassResult


class DummyDevice:
    def __repr__(self):
        return f"device"


def replace_with_ttnn(node, func, device):
    """
    Replace a node with a new node that calls the given function with the same arguments.
    It will insert data movement and data conversion before and after the call.
    Replace:
        node
    With:
        from_torch => to_device => op-func => from_device => to_torch
    """
    graph: torch.fx.Graph = node.graph
    with graph.inserting_before(node):
        from_torch = tuple(
            graph.call_function(ttnn.from_torch, (i,)) for i in node.args
        )
        to_device = tuple(
            graph.call_function(ttnn.to_device, (i, device)) for i in from_torch
        )
        ttnn_op = graph.call_function(func, to_device)
        from_device = graph.call_function(ttnn.from_device, (ttnn_op,))
        to_torch = graph.call_function(ttnn.to_torch, (from_device,))
        node.replace_all_uses_with(to_torch)
        graph.erase_node(node)


class ToTtPass(PassBase):
    def call(self, gm: torch.fx.GraphModule):
        device = DummyDevice()
        modified = False
        for node in gm.graph.nodes:
            if node.op == "call_function" and node.target == torch.ops.aten.add.Tensor:
                replace_with_ttnn(node, ttnn.add, device)
                modified = True
            elif (
                node.op == "call_function" and node.target == torch.ops.aten.mm.default
            ):
                replace_with_ttnn(node, ttnn.matmul, device)
                modified = True

        return PassResult(gm, modified)

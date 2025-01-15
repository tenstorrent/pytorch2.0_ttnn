import torch
import ttnn
from torch._subclasses.fake_tensor import unset_fake_temporarily
from torch.fx.passes.infra.pass_base import PassBase, PassResult


class MMFusionPass(PassBase):
    def __init__(self):
        super().__init__()
        self.mm_ops = {
            torch.ops.aten.mm.default,
            torch.ops.aten.bmm.default,
        }

        self.activation_ops_map = {
            torch.ops.aten.relu.default: "relu",
            torch.ops.aten.gelu.default: "gelu",
            torch.ops.aten.silu.default: "silu",
            # (Issue #15745) Inside ttnn/cpp/ttnn/operations/matmul/matmul.cpp, function bound_matmul only supports the three activations above
            # torch.ops.aten.sigmoid.default : 'sigmoid',
            # torch.ops.aten.sqrt.default : 'sqrt',
            # torch.ops.aten.exp.default : 'exp',
            # torch.ops.aten.reciprocal.default : 'recip',
            # torch.ops.aten.log.default : 'log',
            # torch.ops.aten.tanh.default : 'tanh',
            # torch.ops.aten.log2.default : 'log2',
            # torch.ops.aten.log10.default : 'log10',
            # torch.ops.aten.sin.default : 'sin',
            # torch.ops.aten.cos.default : 'cos',
            # torch.ops.aten.abs.default : 'abs',
            # torch.ops.aten.sign.default : 'sign',
            # torch.ops.aten.pow.Tensor_Scalar : 'square',
            # torch.ops.aten.softplus.default : 'softplus',
        }

    def call(self, gm: torch.fx.GraphModule):
        g = gm.graph
        for node in gm.graph.nodes:
            # Find nodes that are mat mul and don't already have an activation fuinction fused to them
            if node.op == "call_function" and node.target in self.mm_ops and "activation" not in node.kwargs:
                users = [user for user in node.users.keys()]
                # If only user of mat mul is an activation, we can fuse activation into mat mul
                if len(users) == 1 and users[0].op == "call_function" and users[0].target in self.activation_ops_map:
                    activation = users[0].target
                    if activation == torch.ops.aten.pow.Tensor_Scalar and users[0].args[1] != 2:
                        # pow in general is not supported for fusion, but if exponent is 2 we can fuse as square op
                        continue
                    with g.inserting_after(node):
                        # create ttnn mat mul with fused activation function
                        new_kwargs = node.kwargs.copy()
                        new_kwargs["activation"] = self.activation_ops_map[users[0].target]
                        new_node = g.call_function(ttnn.matmul, node.args, new_kwargs)
                    # delete torch mat mul and activation nodes that were replaced by ttnn mat mul with fused activation
                    users[0].replace_all_uses_with(new_node)
                    g.erase_node(users[0])
                    g.erase_node(node)

        return PassResult(gm, True)

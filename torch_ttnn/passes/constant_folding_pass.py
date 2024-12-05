import torch
from torch._subclasses.fake_tensor import unset_fake_temporarily
from torch.fx.passes.infra.pass_base import PassBase, PassResult


class ConstantFoldingPass(PassBase):
    def __init__(self):
        super().__init__()
        self.foldable_ops = {
            torch.ops.aten.lift_fresh_copy.default,
            torch.ops.aten.pow.Tensor_Tensor,
            torch.ops.aten.arange.start,
            torch.ops.aten.unsqueeze.default,
            torch.ops.aten.arange.default,
            torch.ops.aten.view.default,
        }

    def call(self, gm: torch.fx.GraphModule):
        with unset_fake_temporarily():
            for node in gm.graph.nodes:
                if node.op == "call_function" and node.target in self.foldable_ops and self._can_fold(gm, node):
                    try:
                        folded_value = self._evaluate_node(gm, node)
                        self._replace_with_constant(gm, node, folded_value)
                    except Exception as e:
                        print(f"Warning: Could not fold node {node.name}: {e}")

        return PassResult(gm, True)

    def _can_fold(self, gm: torch.fx.GraphModule, node):
        for arg in node.args:
            if not isinstance(arg, (int, float,)) and isinstance(arg, torch.fx.Node):
                if arg.op not in ("get_attr", "constant"):
                    return False
        return True

    def _evaluate_node(self, gm: torch.fx.GraphModule, node):
        args = []
        for arg in node.args:
            if isinstance(arg, torch.fx.Node):
                if arg.op == "get_attr":
                    value = getattr(gm, arg.target)
                    args.append(value)
                elif arg.op == "constant":
                    args.append(arg.args[0])
            else:
                args.append(arg)

        if node.target == torch.ops.aten.lift_fresh_copy.default:
            return args[0]
        elif node.target == torch.ops.aten.pow.Tensor_Tensor:
            return torch.pow(*args)
        elif node.target == torch.ops.aten.arange.start:
            return torch.arange(*args, **node.kwargs)
        elif node.target == torch.ops.aten.unsqueeze.default:
            return torch.unsqueeze(*args)
        elif node.target == torch.ops.aten.arange.default:
            return torch.arange(*args, **node.kwargs)
        elif node.target == torch.ops.aten.view.default:
            return torch.ops.aten.view.default(*args)

        # Add handlers for other operations...

        raise ValueError(f"Unsupported operation: {node.target}")

    def _replace_with_constant(self, gm: torch.fx.GraphModule, node, value):
        with gm.graph.inserting_before(node):
            new_node = gm.graph.create_node("get_attr", target=f"_folded_{node.name}", args=(), kwargs=None)

        gm.register_parameter(f"_folded_{node.name}", torch.nn.Parameter(value, requires_grad=False))

        node.replace_all_uses_with(new_node)
        gm.graph.erase_node(node)

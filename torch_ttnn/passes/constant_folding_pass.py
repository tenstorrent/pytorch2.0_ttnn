import torch
from torch._subclasses.fake_tensor import unset_fake_temporarily
from torch.fx.passes.infra.pass_base import PassBase, PassResult
from .lowering.to_tt_guard import can_lowering_to_ttnn


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
            torch.ops.aten.add.Tensor,
            torch.ops.aten.mul.Tensor,
            torch.ops.aten._to_copy.default,
            torch.ops.aten.expand.default,
            torch.ops.aten.sub.Tensor,
            torch.ops.aten.ceil.default,
            torch.ops.aten.clamp.default,
            torch.ops.aten.ones.default,
            torch.ops.aten.cumsum.default,
            torch.ops.aten._unsafe_index.Tensor,
            torch.ops.aten.ne.Scalar,
            torch.ops.aten.select.int,
            torch.ops.aten.bitwise_not.default,
            torch.ops.aten.floor_divide.default,
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
        if not can_lowering_to_ttnn(node):
            return False

        def can_arg_fold(arg):
            if (
                isinstance(
                    arg,
                    (
                        int,
                        float,
                    ),
                )
                or arg is None
            ):
                return True

            if isinstance(arg, torch.fx.Node) and arg.op in ("get_attr", "constant"):
                return True
            return False

        for arg in node.args:
            if isinstance(
                arg,
                (
                    list,
                    tuple,
                    torch.fx.immutable_collections.immutable_list,
                ),
            ):
                for arg_element in arg:
                    if not can_arg_fold(arg_element):
                        return False
            elif not can_arg_fold(arg):
                return False

        return True

    def _evaluate_node(self, gm: torch.fx.GraphModule, node):
        def eval_arg(arg):
            if isinstance(arg, torch.fx.Node):
                if arg.op == "get_attr":
                    return getattr(gm, arg.target)
                elif arg.op == "constant":
                    return arg.args[0]
            return arg

        args = []
        for arg in node.args:
            if isinstance(
                arg,
                (
                    list,
                    tuple,
                    torch.fx.immutable_collections.immutable_list,
                ),
            ):
                list_arg = []
                for arg_element in arg:
                    list_arg.append(eval_arg(arg_element))
                args.append(list_arg)
            else:
                args.append(eval_arg(arg))

        if node.target == torch.ops.aten.lift_fresh_copy.default:
            return args[0]

        if node.target in self.foldable_ops:
            result = node.target(*args, **node.kwargs)
            return result

        # Add handlers for other operations...

        raise ValueError(f"Unsupported operation: {node.target}")

    def _replace_with_constant(self, gm: torch.fx.GraphModule, node, value):
        with gm.graph.inserting_before(node):
            new_node = gm.graph.create_node("get_attr", target=f"_folded_{node.name}", args=(), kwargs=None)
            # Copying all of the meta causes some ops to be missing
            new_node.meta["seq_nr"] = node.meta["seq_nr"]
            new_node.meta["original_aten"] = node.meta["original_aten"]
            new_node.meta["tensor_meta"] = node.meta["tensor_meta"]

        gm.register_parameter(f"_folded_{node.name}", torch.nn.Parameter(value, requires_grad=False))

        node.replace_all_uses_with(new_node)
        gm.graph.erase_node(node)

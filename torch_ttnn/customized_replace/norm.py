import torch
import ttnn


def is_getitem(n: torch.fx.node.Node):
    if n.op == "call_function" and n.target.__name__ == "getitem":
        return True
    return False


def group_norm_rep(gm: torch.fx.GraphModule):
    changed = False
    for n in gm.graph.nodes:
        if not (
            isinstance(n, torch.fx.node.Node)
            and n.op == "call_function"
            and n.target == torch.ops.aten.native_group_norm.default
            and len(n.users) == 1
        ):
            continue

        next_n = next(iter(n.users))
        if not (
            isinstance(next_n, torch.fx.node.Node)
            and next_n.op == "call_function"
            and is_getitem(next_n)
        ):
            continue

        n_kwargs = {
            "input": n.args[0],
            "weight": n.args[1],
            "bias": n.args[2],
            "N": n.args[3],
            "C": n.args[4],
            "HxW": n.args[5],
            "group": n.args[6],
            "eps": n.args[7],
        }
        ttnn_kwargs = {
            "num_groups": n_kwargs["group"],
            "epsilon": n_kwargs["eps"],
        }
        if n_kwargs["weight"] is not None:
            ttnn_kwargs["weight"] = n_kwargs["weight"]
        if n_kwargs["bias"] is not None:
            ttnn_kwargs["bias"] = n_kwargs["bias"]

        g = gm.graph
        with g.inserting_after(next_n):
            ttnn_node = g.call_function(
                ttnn.group_norm, (n_kwargs["input"],), ttnn_kwargs
            )
            next_n.replace_all_uses_with(ttnn_node)
        changed = True

    if changed:
        gm.graph.eliminate_dead_code()
    return gm


def layer_norm_rep(gm: torch.fx.GraphModule):
    changed = False
    for n in gm.graph.nodes:
        if not (
            isinstance(n, torch.fx.node.Node)
            and n.op == "call_function"
            and n.target == torch.ops.aten.native_layer_norm.default
            and len(n.users) == 1
        ):
            continue

        next_n = next(iter(n.users))
        if not (
            isinstance(next_n, torch.fx.node.Node)
            and next_n.op == "call_function"
            and is_getitem(next_n)
        ):
            continue

        n_kwargs = {
            "input": n.args[0],
            "normalized_shape": n.args[1],
            "weight": n.args[2],
            "bias": n.args[3],
            "eps": n.args[4],
        }
        ttnn_kwargs = {"normalized_shape": n_kwargs["normalized_shape"]}
        if n_kwargs["weight"] is not None:
            ttnn_kwargs["weight"] = n_kwargs["weight"]
        if n_kwargs["bias"] is not None:
            ttnn_kwargs["bias"] = n_kwargs["bias"]

        g = gm.graph
        with g.inserting_after(next_n):
            ttnn_node = g.call_function(
                ttnn.layer_norm, (n_kwargs["input"],), ttnn_kwargs
            )
            next_n.replace_all_uses_with(ttnn_node)
        changed = True

    if changed:
        gm.graph.eliminate_dead_code()
    return gm


customized_rep_list = [
    group_norm_rep,
    # layer_norm_rep
]

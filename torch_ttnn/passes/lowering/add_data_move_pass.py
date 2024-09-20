import torch
import ttnn
from torch_ttnn.utils import (
    TtnnRowMajorLayout,
    TtnnTileLayout,
    TtnnDevice,
    TtnnBfloat16,
)


from torch.fx.passes.infra.pass_base import PassBase, PassResult
from . import target_wrappers


class _Kwarg:
    def __init__(self, key, value):
        self.key = key
        self.value = value


def is_function_call(node) -> bool:
    if not isinstance(node, torch.fx.node.Node):
        return False
    return node.op == "call_function"


TTNN_POINTWISE_UNARY_OPS = [
    ttnn.abs,
    ttnn.acos,
    ttnn.acosh,
    ttnn.asin,
    ttnn.asinh,
    ttnn.atan,
    ttnn.atan2,  # binary
    ttnn.atanh,
    #  ttnn.clone,  in target_wrappers
    ttnn.cos,
    ttnn.cosh,
    ttnn.erf,
    ttnn.exp,
    ttnn.expm1,
    ttnn.floor,
    ttnn.gelu,
    ttnn.hardtanh,
    ttnn.isinf,
    ttnn.isnan,
    ttnn.leaky_relu,
    ttnn.log,
    ttnn.log10,
    ttnn.log1p,
    ttnn.log2,
    ttnn.logical_not,
    ttnn.min,
    ttnn.neg,
    ttnn.reciprocal,
    ttnn.relu,
    ttnn.remainder,
    ttnn.rsqrt,
    ttnn.sigmoid,
    ttnn.softmax,
    ttnn.sign,
    ttnn.sin,
    ttnn.sinh,
    ttnn.silu,
    ttnn.sqrt,
    ttnn.tan,
    ttnn.tanh,
]


TTNN_POINTWISE_BINARY_OPS = [
    ttnn.add,
    ttnn.eqz,
    ttnn.gez,
    ttnn.ge,
    ttnn.gtz,
    ttnn.isclose,
    ttnn.ldexp,
    ttnn.lez,
    ttnn.logaddexp,
    ttnn.logaddexp2,
    ttnn.le,
    ttnn.ltz,
    ttnn.nextafter,
    ttnn.nez,
    ttnn.polyval,
    ttnn.squared_difference,
    ttnn.eq,
    ttnn.gt,
    ttnn.logical_and,
    ttnn.logical_or,
    ttnn.logical_xor,
    ttnn.lt,
    ttnn.maximum,
    ttnn.minimum,
    ttnn.mul,
    ttnn.ne,
    ttnn.pow,
    ttnn.sub,
    ttnn.xlogy,
    # ttnn.add_and_apply_activation,  # ttnn has no add_and_apply_activation, remote the comment in the future when it has
    # ttnn.add_and_apply_activation_,  # ttnn has no add_and_apply_activation, remote the comment in the future when it has
]

TTNN_POINTWISE_TRINARY_OPS = [
    ttnn.addcdiv,
    ttnn.addcmul,
    ttnn.mac,
    ttnn.where,
]

TTNN_REDUCTION_OPS = [
    ttnn.mean,
    ttnn.var,
]

TTNN_MATRIX_MULPIPLICATION_OPS = [
    ttnn.matmul,
    ttnn.linear,
]

TTNN_DATAMOVE_OPS = [
    ttnn.reshape,
    ttnn.pad,
    ttnn.permute,
    ttnn.concat,
    ttnn.split,
    ttnn.slice,
    ttnn.to_layout,
]

TTNN_TARGET_WRAPPERS = [target_wrappers.clone, target_wrappers.repeat]

TTNN_NORM_OPS = [
    ttnn.group_norm,
    ttnn.layer_norm,
]


# For operations limitations
# See https://github.com/tenstorrent-metal/tt-metal/blob/main/ttnn/README.md?plain=1#L19
def is_tt_compute(node) -> bool:
    if not is_function_call(node):
        return False

    # if node is the built-in function "getitme", the result of split
    # we have to check the input of split
    if node.op == "call_function" and node.target.__name__ == "getitem":
        return is_tt_compute(node.args[0])

    return node.target in set(
        TTNN_POINTWISE_UNARY_OPS
        + TTNN_POINTWISE_BINARY_OPS
        + TTNN_POINTWISE_TRINARY_OPS
        + TTNN_REDUCTION_OPS
        + TTNN_MATRIX_MULPIPLICATION_OPS
        + TTNN_TARGET_WRAPPERS
        + TTNN_DATAMOVE_OPS
        + TTNN_NORM_OPS
        + [
            ttnn.embedding,
            ttnn.ones,
            ttnn.tril,
            ttnn.arange,
            ttnn.zeros_like,
            ttnn.global_avg_pool2d,
            ttnn.clip,
            ttnn.squeeze,
            ttnn.full,
            ttnn.as_tensor,
        ]
    )


def is_tt_data_move(node) -> bool:
    if not is_function_call(node):
        return False
    return node.target in [
        ttnn.from_device,
        ttnn.to_device,
        ttnn.from_torch,
        ttnn.to_torch,
        ttnn.to_layout,
        ttnn.MemoryConfig,
        ttnn.Shape,
    ]


def is_tt(node):
    return is_tt_compute(node) or is_tt_data_move(node)


def is_reshape_rank_4(node):
    if node.target == ttnn.reshape:
        return len(node.args[1]) == 4
    else:
        return False


def call_to_torch_with_meta(g, src_node):
    call_func = g.call_function(ttnn.to_torch, (src_node,))
    if src_node.meta is not None:
        call_func.meta = src_node.meta
    return call_func


def should_add_data_move_in(src_node, dst_node) -> bool:
    if isinstance(src_node, (int, float, list, tuple)) or not isinstance(src_node, torch.fx.node.Node):
        return False
    return is_tt_compute(dst_node) and not is_tt(src_node) and not (dst_node.target == ttnn.as_tensor)


def should_add_data_move_out(src_node, dst_node) -> bool:
    return is_tt_compute(src_node) and not is_tt(dst_node)


def insert_node_between(src_node, dst_idx, dst_node, new_nodes):
    """
    Insert new_node between src_node and dest_node's dst_idx-th arg

    If dst_node is output, the args is stored in dst_node.args[0], and it is a tuple,
    so we need to check if dst_node is output and handle it separately.
    """
    new_nodes[0].update_arg(0, src_node)
    if dst_node.op != "output":
        dst_node.update_arg(dst_idx, new_nodes[-1])
    else:
        old_arg = dst_node.args[0]
        new_arg = list(old_arg)
        new_arg[dst_idx] = new_nodes[-1]
        dst_node.update_arg(0, tuple(new_arg))


def insert_node_between_kwarg(src_node, key, dst_node, new_nodes):
    """
    Insert new_node between src_node and dest_node's keyword arg.

    Output does not have keyword args.
    """
    assert dst_node.op != "output"
    new_nodes[0].update_arg(0, src_node)
    dst_node.update_kwarg(key, new_nodes[-1])


def try_add_data_move_in_kwargs(src_node_kwarg, dst_node, device) -> torch.fx.node.Node:
    if not isinstance(src_node_kwarg, _Kwarg):
        return None
    key = src_node_kwarg.key
    src_node = src_node_kwarg.value
    if not should_add_data_move_in(src_node, dst_node):
        return None

    g = dst_node.graph
    new_nodes = list()
    with g.inserting_before(dst_node):
        kwargs = {"layout": TtnnTileLayout(), "device": device}
        new_nodes.append(g.call_function(ttnn.from_torch, (src_node,), kwargs))

    insert_node_between_kwarg(src_node, key, dst_node, new_nodes)
    return new_nodes[-1]


def try_add_data_move_in(src_node, dst_idx, dst_node, device) -> torch.fx.node.Node:
    if not should_add_data_move_in(src_node, dst_node):
        return None

    g = dst_node.graph
    new_nodes = list()
    with g.inserting_before(dst_node):
        kwargs = {}
        if (
            dst_node.target == ttnn.reshape
            or dst_node.target == ttnn.embedding
            or dst_node.target == ttnn.zeros_like
            or dst_node.target == target_wrappers.repeat
        ):
            kwargs["layout"] = TtnnRowMajorLayout()
        else:
            kwargs["layout"] = TtnnTileLayout()

        if dst_node.target != ttnn.embedding:
            kwargs["dtype"] = TtnnBfloat16()

        # For reshape only put tensor on device if rank is 4
        if (is_tt_compute(dst_node) and dst_node.target != ttnn.reshape) or (
            dst_node.target == ttnn.reshape and len(dst_node.args[1]) == 4
        ):
            kwargs["device"] = device

        new_nodes.append(g.call_function(ttnn.from_torch, (src_node,), kwargs))

    insert_node_between(src_node, dst_idx, dst_node, new_nodes)
    return new_nodes[-1]


layout_change_ops = set(
    [
        target_wrappers.repeat,
        ttnn.reshape,
    ]
)


def try_add_layout_change_before_node(src_node, dst_idx, dst_node) -> torch.fx.node.Node:
    # Consider dst_node is ttnn.repeat, and src_node are any tt nodes that ttnn.repeat uses
    if isinstance(src_node, (int, float, list, tuple)) or not isinstance(src_node, torch.fx.node.Node):
        return None
    if not is_function_call(dst_node):
        return None
    if dst_node.target not in layout_change_ops or dst_idx != 0 or not is_tt(src_node):
        return None

    g = dst_node.graph
    with g.inserting_before(dst_node):
        to_layout = g.call_function(ttnn.to_layout, (src_node, TtnnRowMajorLayout()))

    insert_node_between(src_node, dst_idx, dst_node, [to_layout])

    return to_layout


def try_add_layout_change_after_node(src_node, dst_idx, dst_node) -> torch.fx.node.Node:
    # Consider src_node is ttnn.repeat, and dst_node should be any tt_compute node that uses ttnn.repeat
    if not is_function_call(src_node):
        return None
    if src_node.target not in layout_change_ops or not is_tt_compute(dst_node) or dst_node.target == ttnn.embedding:
        return None

    g = dst_node.graph
    with g.inserting_before(dst_node):
        to_layout = g.call_function(ttnn.to_layout, (dst_node, TtnnTileLayout()))

    insert_node_between(src_node, dst_idx, dst_node, [to_layout])

    return to_layout


def try_add_data_move_out_for_list_args(src_nodes, dst_idx, dst_node):
    # Handle list type arguments from ops like cat
    if not isinstance(src_nodes, list):
        return None

    new_nodes = list()
    for src_node in src_nodes:
        if should_add_data_move_out(src_node, dst_node):
            g = dst_node.graph
            with g.inserting_before(dst_node):
                new_nodes.append(call_to_torch_with_meta(g, src_node))
        else:
            new_nodes.append(src_node)

    if new_nodes:
        dst_node.update_arg(dst_idx, new_nodes)
        return new_nodes
    else:
        return None


def try_add_data_move_out(src_node, dst_idx, dst_node) -> torch.fx.node.Node:
    if not should_add_data_move_out(src_node, dst_node):
        return None

    g = dst_node.graph
    new_nodes = list()
    with g.inserting_before(dst_node):
        new_nodes.append(call_to_torch_with_meta(g, new_nodes[-1] if new_nodes else src_node))

    insert_node_between(src_node, dst_idx, dst_node, new_nodes)
    return new_nodes[-1]


def try_add_data_move_out_for_layer_norm(src_node, dst_idx, dst_node) -> torch.fx.node.Node:
    if not should_add_data_move_out(src_node, dst_node):
        return None

    g = dst_node.graph
    new_nodes = list()
    with g.inserting_before(dst_node):
        if is_tt_compute(src_node) and src_node.target == ttnn.layer_norm:
            new_nodes.append(call_to_torch_with_meta(g, src_node))

    # Workaround to output the same layer_norm output
    # Before: layer_norm = aten.layer_norm
    #          getitem = getitem(layer_norm, 0)
    #          return ((getitem,),)
    # After: layer_norm = ttnn.layer_norm
    #        return (layer_norm,)
    # Need to match the tuple in the original return statement
    if new_nodes:
        old_args = dst_node.args[0]
        if isinstance(old_args, tuple):
            new_args = list(old_args)
            for idx, old_arg in enumerate(old_args):
                if old_arg == src_node:
                    new_args[idx] = new_nodes[-1]
            dst_node.update_arg(0, tuple(new_args))
        else:
            dst_node.update_arg(dst_idx, new_nodes[-1])
        return new_nodes[-1]
    else:
        return None


class AddDataMovePass(PassBase):
    def call(self, gm: torch.fx.GraphModule):
        modified = False
        device = TtnnDevice()
        i = 0
        nodes = list(gm.graph.nodes)
        # Track argument reuse
        data_move_in_hash = {}
        # This might not be needed if workaround is not needed
        data_move_out_hash = {}
        for node in nodes:
            args = node.args[0] if node.op == "output" else node.args
            kwargs = tuple(_Kwarg(k, v) for k, v in node.kwargs.items() if isinstance(v, torch.fx.node.Node))
            if isinstance(args, tuple):
                args += kwargs

            for idx, arg in enumerate(args):
                if isinstance(arg, _Kwarg):
                    try_add_data_move_in_kwargs(arg, node, device)
                elif (
                    arg in data_move_in_hash
                    and not isinstance(node.target, torch._ops.OpOverload)
                    and node.op != "output"
                ):
                    node.update_arg(idx, data_move_in_hash[arg])
                elif to_device := try_add_data_move_in(arg, idx, node, device):
                    data_move_in_hash[arg] = to_device
                    i += 1
                elif to_layout := try_add_layout_change_before_node(arg, idx, node):
                    data_move_in_hash[arg] = to_layout
                    i += 1
                elif to_layout := try_add_layout_change_after_node(arg, idx, node):
                    data_move_in_hash[arg] = to_layout
                    i += 1

                if arg in data_move_out_hash and node.op == "output":
                    old_arg = node.args[0]
                    new_arg = list(old_arg)
                    new_arg[idx] = data_move_out_hash[arg]
                    node.update_arg(0, tuple(new_arg))
                    i += 1
                elif (node.target != ttnn.layer_norm) and (to_torch := try_add_data_move_out(arg, idx, node)):
                    data_move_out_hash[arg] = to_torch
                    i += 1
                elif to_torch := try_add_data_move_out_for_layer_norm(arg, idx, node):
                    data_move_out_hash[arg] = to_torch
                    i += 1
                elif to_torch := try_add_data_move_out_for_list_args(arg, idx, node):
                    data_move_out_hash[arg] = to_torch
                    i += 1

        modified = i > 0
        return PassResult(gm, modified)

    def ensures(self, gm: torch.fx.GraphModule) -> None:
        # Because of the mixing of ttnn and aten ops, some types need to be fixed
        for node in gm.graph.nodes:
            if node.target == ttnn.to_torch:
                # Reconvert int64 types back to torch
                if node.meta["val"].dtype == torch.int64:
                    g = node.graph
                    with g.inserting_after(node):
                        # TODO: Is _to_copy the right op?
                        new_node = g.call_function(
                            torch.ops.aten._to_copy.default,
                            (node,),
                            {"dtype": torch.int64},
                        )
                        new_node.meta = node.meta
                        node.replace_all_uses_with(new_node, delete_user_cb=lambda node: node != new_node)

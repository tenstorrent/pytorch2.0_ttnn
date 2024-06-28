import torch
from ..utils import (
    DummyTtnnUint32,
    DummyTtnnRowMajorLayout,
    DummyTtnnTileLayout,
    DummyDevice,
)

try:
    import ttnn
except ImportError:
    print("ttnn is not installed, use mock_ttnn instead")
    from .. import mock_ttnn as ttnn

from torch.fx.passes.infra.pass_base import PassBase, PassResult


class _Kwarg:
    def __init__(self, key, value):
        self.key = key
        self.value = value


def is_function_call(node) -> bool:
    if not isinstance(node, torch.fx.node.Node):
        return False
    return node.op == "call_function"


# For operations limitations
# See https://github.com/tenstorrent-metal/tt-metal/blob/main/ttnn/README.md?plain=1#L19
def is_tt_compute(node) -> bool:
    if not is_function_call(node):
        return False
    return node.target in set(
        [
            ttnn.add,
            ttnn.matmul,
            ttnn.sub,
            ttnn.mul,
            ttnn.softmax,
            ttnn.tanh,
            ttnn.reshape,
            ttnn.permute,
            ttnn.relu,
            ttnn.reciprocal,
            ttnn.gelu,
            ttnn.embedding,
            ttnn.clone,
            ttnn.layer_norm,
            ttnn.neg,
            ttnn.ones,
            ttnn.tril,
            ttnn.arange,
            ttnn.eq,
            ttnn.logical_not,
            ttnn.zeros_like,
            ttnn.mean,
            ttnn.pow,
            ttnn.rsqrt,
            ttnn.silu,
            ttnn.global_avg_pool2d,
            ttnn.clip,
            ttnn.squeeze,
            ttnn.full,
            ttnn.lt,
            ttnn.cos,
            ttnn.sigmoid,
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
        ttnn.MemoryConfig,
    ]


def is_tt(node):
    return is_tt_compute(node) or is_tt_data_move(node)


def is_reshape_rank_4(node):
    if node.target == ttnn.reshape:
        return len(node.args[1]) == 4
    else:
        return False


def should_add_data_move_in(src_node, dst_node) -> bool:
    if isinstance(src_node, (int, float, list, tuple)) or not isinstance(
        src_node, torch.fx.node.Node
    ):
        return False
    return is_tt_compute(dst_node) and not is_tt(src_node)


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
        new_nodes.append(g.call_function(ttnn.from_torch, (src_node,)))
        new_nodes.append(
            g.call_function(ttnn.to_layout, (new_nodes[-1], DummyTtnnTileLayout()))
        )
        if is_tt_compute(dst_node):
            new_nodes.append(g.call_function(ttnn.to_device, (new_nodes[-1], device)))

    insert_node_between_kwarg(src_node, key, dst_node, new_nodes)
    return new_nodes[-1]


def try_add_data_move_in(src_node, dst_idx, dst_node, device) -> torch.fx.node.Node:
    if not should_add_data_move_in(src_node, dst_node):
        return None

    g = dst_node.graph
    new_nodes = list()
    with g.inserting_before(dst_node):
        new_nodes.append(g.call_function(ttnn.from_torch, (src_node,)))
        if (
            dst_node.target != ttnn.reshape
            and dst_node.target != ttnn.embedding
            and dst_node.target != ttnn.zeros_like
        ):
            new_nodes.append(
                g.call_function(ttnn.to_layout, (new_nodes[-1], DummyTtnnTileLayout()))
            )
        # For reshape only put tensor on device if rank is 4
        if (is_tt_compute(dst_node) and dst_node.target != ttnn.reshape) or (
            dst_node.target == ttnn.reshape and len(dst_node.args[1]) == 4
        ):
            new_nodes.append(g.call_function(ttnn.to_device, (new_nodes[-1], device)))

    insert_node_between(src_node, dst_idx, dst_node, new_nodes)
    return new_nodes[-1]


def try_add_data_move_out(src_node, dst_idx, dst_node) -> torch.fx.node.Node:
    if not should_add_data_move_out(src_node, dst_node):
        return None

    g = dst_node.graph
    new_nodes = list()
    with g.inserting_before(dst_node):
        if (is_tt_compute(src_node) and src_node.target != ttnn.reshape) or (
            src_node.target == ttnn.reshape and len(src_node.args[1]) == 4
        ):
            new_nodes.append(g.call_function(ttnn.from_device, (src_node,)))
            if src_node.target != ttnn.embedding and src_node.target != ttnn.zeros_like:
                new_nodes.append(
                    g.call_function(
                        ttnn.to_layout, (new_nodes[-1], DummyTtnnRowMajorLayout())
                    )
                )
        new_nodes.append(
            g.call_function(ttnn.to_torch, (new_nodes[-1] if new_nodes else src_node,))
        )

    insert_node_between(src_node, dst_idx, dst_node, new_nodes)
    return new_nodes[-1]


def try_add_data_move_out_for_layer_norm(
    src_node, dst_idx, dst_node
) -> torch.fx.node.Node:
    if not should_add_data_move_out(src_node, dst_node):
        return None

    g = dst_node.graph
    new_nodes = list()
    with g.inserting_before(dst_node):
        if is_tt_compute(src_node) and src_node.target == ttnn.layer_norm:
            new_nodes.append(
                g.call_function(ttnn.to_layout, (src_node, DummyTtnnRowMajorLayout()))
            )
            new_nodes.append(g.call_function(ttnn.from_device, (new_nodes[-1],)))
            new_nodes.append(g.call_function(ttnn.to_torch, (new_nodes[-1],)))

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
        device = DummyDevice()
        i = 0
        nodes = list(gm.graph.nodes)
        # Track argument reuse
        data_move_in_hash = {}
        # This might not be needed if workaround is not needed
        data_move_out_hash = {}
        for node in nodes:
            args = node.args[0] if node.op == "output" else node.args
            kwargs = tuple(
                _Kwarg(k, v)
                for k, v in node.kwargs.items()
                if isinstance(v, torch.fx.node.Node)
            )
            if isinstance(args, tuple):
                args += kwargs

            for idx, arg in enumerate(args):
                if isinstance(arg, _Kwarg):
                    try_add_data_move_in_kwargs(arg, node, device)
                elif arg in data_move_in_hash and node.op != "output":
                    node.update_arg(idx, data_move_in_hash[arg])
                elif to_device := try_add_data_move_in(arg, idx, node, device):
                    data_move_in_hash[arg] = to_device
                    i += 1

                if arg in data_move_out_hash and node.op == "output":
                    old_arg = node.args[0]
                    new_arg = list(old_arg)
                    new_arg[idx] = data_move_out_hash[arg]
                    node.update_arg(0, tuple(new_arg))
                    i += 1
                elif (node.target != ttnn.layer_norm) and (
                    to_torch := try_add_data_move_out(arg, idx, node)
                ):
                    data_move_out_hash[arg] = to_torch
                    i += 1
                elif to_torch := try_add_data_move_out_for_layer_norm(arg, idx, node):
                    data_move_out_hash[arg] = to_torch
                    i += 1

        modified = i > 0
        return PassResult(gm, modified)

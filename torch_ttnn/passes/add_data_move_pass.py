import torch
import ttnn
from torch.fx.passes.infra.pass_base import PassBase, PassResult


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
    ttnn.clone,
    ttnn.cos,
    ttnn.cosh,
    ttnn.erf,
    ttnn.exp,
    ttnn.expm1,
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
    ttnn.neg,
    ttnn.reciprocal,
    ttnn.relu,
    ttnn.rsqrt,
    ttnn.sigmoid,
    ttnn.sign,
    ttnn.sin,
    ttnn.sinh,
    ttnn.sqrt,
    ttnn.tan,
    ttnn.tanh,
]


TTNN_POINTWISE_BINARY_OPS = [
    ttnn.add,
    ttnn.eqz,
    ttnn.gez,
    ttnn.gte,
    ttnn.gtz,
    ttnn.isclose,
    ttnn.ldexp,
    ttnn.lez,
    ttnn.logaddexp,
    ttnn.logaddexp2,
    ttnn.lte,
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
    ttnn.add_and_apply_activation,
    ttnn.add_and_apply_activation_,
]

TTNN_POINTWISE_TRINARY_OPS = [
    ttnn.addcdiv,
    ttnn.addcmul,
    ttnn.mac,
    ttnn.where,
]

TTNN_MATRIX_MULPIPLICATION_OPS = [
    ttnn.matmul,
    ttnn.linear,
]


# For operations limitations
# See https://github.com/tenstorrent-metal/tt-metal/blob/main/ttnn/README.md?plain=1#L19
def is_tt_compute(node) -> bool:
    if not is_function_call(node):
        return False
    return node.target in set(
        [
            ttnn.softmax,
            ttnn.reshape,
            ttnn.permute,
        ]
        + TTNN_POINTWISE_UNARY_OPS
        + TTNN_POINTWISE_BINARY_OPS
        + TTNN_POINTWISE_TRINARY_OPS
        + TTNN_MATRIX_MULPIPLICATION_OPS
    )


def is_tt_data_move(node) -> bool:
    if not is_function_call(node):
        return False
    return node.target in [
        ttnn.from_device,
        ttnn.to_device,
        ttnn.from_torch,
        ttnn.to_torch,
    ]


def is_tt(node):
    return is_tt_compute(node) or is_tt_data_move(node)


def should_add_data_move_in(src_node, dst_node) -> bool:
    if isinstance(src_node, (int, float, list, tuple)):
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


def try_add_data_move_in(src_node, dst_idx, dst_node, device) -> bool:
    if not should_add_data_move_in(src_node, dst_node):
        return False

    g = dst_node.graph
    with g.inserting_before(dst_node):
        from_torch = g.call_function(ttnn.from_torch, (src_node,))
        to_device = g.call_function(ttnn.to_device, (from_torch, device))

    insert_node_between(src_node, dst_idx, dst_node, [from_torch, to_device])
    return True


def try_add_data_move_out(src_node, dst_idx, dst_node) -> bool:
    if not should_add_data_move_out(src_node, dst_node):
        return False

    g = dst_node.graph
    with g.inserting_before(dst_node):
        from_device = g.call_function(ttnn.from_device, (src_node,))
        row_major_layout = g.call_function(
            ttnn.to_layout, (from_device, DummyTtnnRowMajorLayout())
        )
        to_torch = g.call_function(ttnn.to_torch, (row_major_layout,))

    insert_node_between(src_node, dst_idx, dst_node, [from_device, to_torch])
    return True


# See https://docs.google.com/document/d/1r2D4AagoeTRjEmXFnWzzafaWQkf-8hlIbX2ze-JAUFo/edit#heading=h.zad9rwqjv6cr
class DummyDevice:
    def __repr__(self):
        return f"ttnn_Specified_Device"


class DummyTtnnRowMajorLayout:
    def __repr__(self):
        return f"ttnn_ROW_MAJOR_LAYOUT"


class AddDataMovePass(PassBase):
    def call(self, gm: torch.fx.GraphModule):
        modified = False
        device = DummyDevice()
        i = 0
        nodes = list(gm.graph.nodes)
        for node in nodes:
            args = node.args[0] if node.op == "output" else node.args
            for idx, arg in enumerate(args):
                if try_add_data_move_in(arg, idx, node, device):
                    i += 1
                if try_add_data_move_out(arg, idx, node):
                    i += 1

        modified = i > 0
        return PassResult(gm, modified)

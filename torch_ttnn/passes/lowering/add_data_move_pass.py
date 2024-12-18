import torch
import ttnn
from torch_ttnn.utils import (
    TtnnRowMajorLayout,
    TtnnTileLayout,
    TtnnDevice,
    TtnnBfloat16,
    TtnnUint32,
    HasValidPageSize,
    get_dtype,
)
from dataclasses import dataclass
from enum import Enum
from typing import Union, Type, Literal

from torch.fx.passes.infra.pass_base import PassBase, PassResult
from . import target_wrappers


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
    ttnn.elu,
    ttnn.erf,
    ttnn.exp,
    ttnn.expm1,
    ttnn.floor,
    ttnn.gelu,
    ttnn.hardsigmoid,
    ttnn.hardswish,
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
    ttnn.div,
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
    ttnn.rsub,
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

TTNN_MATRIX_MULPIPLICATION_OPS = [
    ttnn.matmul,
    ttnn.linear,
]

TTNN_DATAMOVE_OPS = [
    ttnn.concat,
    ttnn.pad,
    ttnn.permute,
    ttnn.reshape,
    ttnn.sharded_to_interleaved,
    ttnn.slice,
    ttnn.split,
    ttnn.to_layout,
    ttnn.transpose,
]

TTNN_TARGET_WRAPPERS = [
    target_wrappers.clone,
    target_wrappers.repeat,
    target_wrappers.pack_to_tuple,
    target_wrappers.move_to_host,
    target_wrappers.conv2d,
]

TTNN_NORM_OPS = [
    ttnn.group_norm,
    ttnn.layer_norm,
]

TTNN_POOL_OPS = [
    ttnn.max_pool2d,
]

TTNN_LAYOUT_CHANGE_OPS = set(
    [
        ttnn.reshape,
        ttnn.slice,
        ttnn.argmax,
    ]
)


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
        + TTNN_MATRIX_MULPIPLICATION_OPS
        + TTNN_TARGET_WRAPPERS
        + TTNN_DATAMOVE_OPS
        + TTNN_NORM_OPS
        + TTNN_POOL_OPS
        + [
            ttnn.embedding,
            ttnn.ones,
            ttnn.tril,
            ttnn.arange,
            ttnn.zeros,
            ttnn.zeros_like,
            ttnn.mean,
            ttnn.moreh_cumsum,
            ttnn.clip,
            ttnn.squeeze,
            ttnn.full,
            ttnn.as_tensor,
            ttnn.expand,
            ttnn.moreh_cumsum,
            ttnn.sum,
            ttnn.typecast,
            ttnn.argmax,
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


def call_to_torch_with_meta(g, src_node, dtype=None):
    if dtype == "by_node_meta":
        dtype = get_dtype(src_node)
    call_func = g.call_function(ttnn.to_torch, (src_node,), {"dtype": dtype})
    if src_node.meta is not None:
        call_func.meta = src_node.meta.copy()
    if "original_input_variations" in call_func.meta:
        call_func.meta["original_input_variations"] = None
    return call_func


def is_torch_to_ttnn(src_node, dst_node) -> bool:
    if isinstance(src_node, (int, float, list, tuple)) or not isinstance(src_node, torch.fx.node.Node):
        return False
    return is_tt_compute(dst_node) and not is_tt(src_node) and not (dst_node.target == ttnn.as_tensor)


def is_ttnn_to_torch(src_node, dst_node) -> bool:
    return is_tt_compute(src_node) and not is_tt(dst_node)


def is_ttnn_to_ttnn(src_node, dst_node):
    if not is_tt(src_node) or not is_tt(dst_node):
        return False
    return True


def is_target_a_user_of_curr_node(curr_node, target):
    """
    Trace the users of the current node to check if a target is found.

    Returns true is so or returns false if the end of the graph is reached.
    """
    if curr_node.target == target:
        return True

    # Only trace certain nodes that support different layouts
    if curr_node.target not in TTNN_LAYOUT_CHANGE_OPS:
        return False

    for user in list(curr_node.users.keys()):
        if is_target_a_user_of_curr_node(user, target):
            return True

    # Target is not found
    return False


class NodeInputAligner:
    def __init__(self, graph):
        self.graph = graph
        self.aligned_node_dict = {}

    class InputSiteType(Enum):
        ARGS = 1
        KWARGS = 2
        ARGS_TUPLE = 3
        KWARGS_TUPLE = 4

    @dataclass(unsafe_hash=True)
    class AlignSpecFromTorch:
        input_node: torch.fx.node.Node
        device: Union[None, Type[TtnnDevice], Literal["host"]]
        layout: Union[None, Type[TtnnTileLayout], Type[TtnnRowMajorLayout]]
        dtype: Union[None, Type[TtnnBfloat16], Type[TtnnUint32]]

    @dataclass(unsafe_hash=True)
    class AlignSpecToTorch:
        input_node: torch.fx.node.Node
        dtype: Union[None, Type[TtnnBfloat16], Type[TtnnUint32], Literal["by_node_meta"]]

    @dataclass(unsafe_hash=True)
    class AlignSpecInTtnn:
        input_node: torch.fx.node.Node
        device: Union[None, Type[TtnnDevice], Literal["host"]]
        layout: Union[None, Type[TtnnTileLayout], Type[TtnnRowMajorLayout]]
        dtype: Union[None, Type[TtnnBfloat16], Type[TtnnUint32]]

    def _align_for_special_layout(self, node, spec, input_site, input_site_type: InputSiteType):
        if is_target_a_user_of_curr_node(node, ttnn.embedding) and (
            input_site_type == self.InputSiteType.ARGS and input_site == 0
        ):
            spec.dtype = TtnnUint32
        # TODO(#372): #322 will enable tile layout for more layout change ops
        if node.target in TTNN_LAYOUT_CHANGE_OPS and (input_site_type == self.InputSiteType.ARGS and input_site == 0):
            spec.layout = TtnnRowMajorLayout
            spec.device = "host"
        if node.target in [ttnn.embedding, ttnn.zeros_like, target_wrappers.repeat]:
            # TODO: Only uint32 needs to to_layout on host
            spec.layout = TtnnRowMajorLayout
            spec.device = TtnnDevice
        return spec

    def _reset_to_default_layout(self, input_node, spec):
        # legalize to the default layout and device
        if input_node.target in TTNN_LAYOUT_CHANGE_OPS.union(
            set(
                [
                    target_wrappers.repeat,
                    ttnn.concat,
                ]
            )
        ):
            spec.layout = TtnnTileLayout
            spec.device = TtnnDevice
        return spec

    def _get_align_spec(self, node, input_node, input_site, input_site_type: InputSiteType):
        if is_torch_to_ttnn(input_node, node):
            # default set these layout for torch to ttnn
            spec = self.AlignSpecFromTorch(input_node, TtnnDevice, TtnnTileLayout, TtnnBfloat16)
            spec = self._align_for_special_layout(node, spec, input_site, input_site_type)
            return spec
        elif is_ttnn_to_torch(input_node, node):
            spec = self.AlignSpecToTorch(input_node, "by_node_meta")
            return spec
        elif is_ttnn_to_ttnn(input_node, node):
            # default do nothing between ttnn to ttnn
            spec = self.AlignSpecInTtnn(input_node, None, None, None)
            spec = self._reset_to_default_layout(input_node, spec)
            spec = self._align_for_special_layout(node, spec, input_site, input_site_type)
            if spec.device is None and spec.layout is None and spec.dtype is None:
                return None
            return spec
        return None

    def _change_layout(self, spec, aligning_nodes):
        g = self.graph
        need_from_device = False
        need_to_layout = False
        need_to_device = False
        if spec.device == "host":
            need_from_device = True
        elif spec.device is not None:
            need_from_device = True
            need_to_device = True
        if spec.layout is not None:
            need_to_layout = True

        if need_from_device:
            aligning_nodes.append(
                g.call_function(ttnn.from_device, (aligning_nodes[-1] if aligning_nodes else spec.input_node,))
            )
        if need_to_layout:
            aligning_nodes.append(
                g.call_function(
                    ttnn.to_layout, (aligning_nodes[-1] if aligning_nodes else spec.input_node, spec.layout())
                )
            )
        if need_to_device:
            aligning_nodes.append(
                g.call_function(
                    ttnn.to_device,
                    (aligning_nodes[-1] if aligning_nodes else spec.input_node,),
                    {"device": spec.device()},
                )
            )

    def _create_aligned_node(self, spec):
        aligning_nodes = []
        g = self.graph
        if isinstance(spec, self.AlignSpecFromTorch):
            kwargs = {"layout": TtnnTileLayout(), "device": TtnnDevice()}
            if spec.dtype is not None:
                kwargs["dtype"] = spec.dtype()
            aligning_nodes.append(g.call_function(ttnn.from_torch, (spec.input_node,), kwargs))
            if spec.layout != TtnnTileLayout:
                self._change_layout(spec, aligning_nodes)
            # cannot implement by this, or perceiver_io will get this error
            # allocator.cpp:145: Out of Memory: Not enough space to allocate 6442450944 B DRAM buffer across 12 banks, where each bank needs to store 536870912 B
            # see issue #552
            # kwargs = {}
            # if spec.device is not None and spec.device != "host":
            #     kwargs["device"] = spec.device()
            # if spec.layout is not None:
            #     kwargs["layout"] = spec.layout()
            # if spec.dtype is not None:
            #     kwargs["dtype"] = spec.dtype()
            # aligning_nodes.append(g.call_function(ttnn.from_torch, (spec.input_node,), kwargs))
        elif isinstance(spec, self.AlignSpecToTorch):
            target_users_ops = [user.target for user in spec.input_node.users.keys()]
            aligning_nodes.append(call_to_torch_with_meta(g, spec.input_node, spec.dtype))
        elif isinstance(spec, self.AlignSpecInTtnn):
            self._change_layout(spec, aligning_nodes)
        return aligning_nodes[-1]

    def _connect_aligned_node(self, node, aligned_node, input_site, input_site_type: InputSiteType):
        if input_site_type == self.InputSiteType.ARGS:
            input_idx = input_site
            node.update_arg(input_idx, aligned_node)
        elif input_site_type == self.InputSiteType.KWARGS:
            key = input_site
            node.update_kwarg(key, aligned_node)
        elif input_site_type == self.InputSiteType.ARGS_TUPLE:
            input_idx = input_site[0]
            tuple_idx = input_site[1]
            old_arg = node.args[input_idx]
            new_arg = list(old_arg)
            new_arg[tuple_idx] = aligned_node
            node.update_arg(input_idx, tuple(new_arg))
        elif input_site_type == self.InputSiteType.KWARGS_TUPLE:
            key = input_site[0]
            tuple_idx = input_site[1]
            old_arg = node.kwargs[key]
            new_arg = list(old_arg)
            new_arg[tuple_idx] = aligned_node
            node.update_kwarg(key, tuple(new_arg))

    def _connect_aligned_node_layer_norm(
        self, node, input_node, aligned_node, input_site, input_site_type: InputSiteType
    ):
        # Workaround to output the same layer_norm output
        # Before: layer_norm = aten.layer_norm
        #          getitem = getitem(layer_norm, 0)
        #          return ((getitem,),)
        # After: layer_norm = ttnn.layer_norm
        #        return (layer_norm,)
        # Need to match the tuple in the original return statement
        old_args = node.args[0]
        if isinstance(old_args, tuple):
            new_args = list(old_args)
            for idx, old_arg in enumerate(old_args):
                if old_arg == input_node:
                    new_args[idx] = aligned_node
            node.update_arg(0, tuple(new_args))
        else:
            self._connect_aligned_node(node, aligned_node, input_site, input_site_type)

    def align(self, node, input_node, input_site, input_site_type: InputSiteType):
        # assert input_site_type in ["args", "kwargs", "args_tuple", "kwargs_tuple"]
        align_spec = self._get_align_spec(node, input_node, input_site, input_site_type)
        if align_spec is None:
            # No need to align input_node
            return 0
        if align_spec in self.aligned_node_dict:
            aligned_node = self.aligned_node_dict[align_spec]
        else:
            with self.graph.inserting_before(node):
                aligned_node = self._create_aligned_node(align_spec)
            self.aligned_node_dict[align_spec] = aligned_node
        if node.target != ttnn.layer_norm:
            self._connect_aligned_node(node, aligned_node, input_site, input_site_type)
        else:
            self._connect_aligned_node_layer_norm(node, input_node, aligned_node, input_site, input_site_type)
        return 1


class AddDataMovePass(PassBase):
    def call(self, gm: torch.fx.GraphModule):
        modified = False
        i = 0
        node_input_aligner = NodeInputAligner(gm.graph)
        nodes = list(gm.graph.nodes)
        SiteType = NodeInputAligner.InputSiteType
        for node in nodes:
            args = node.args
            kwargs = node.kwargs
            for idx, arg in enumerate(args):
                if not isinstance(arg, (tuple, list, torch.fx.immutable_collections.immutable_list)):
                    i += node_input_aligner.align(node, arg, idx, SiteType.ARGS)
                else:
                    for tuple_idx, tuple_arg in enumerate(arg):
                        i += node_input_aligner.align(node, tuple_arg, [idx, tuple_idx], SiteType.ARGS_TUPLE)
            for key, arg in kwargs.items():
                if not isinstance(arg, (tuple, list, torch.fx.immutable_collections.immutable_list)):
                    i += node_input_aligner.align(node, arg, key, SiteType.KWARGS)
                else:
                    for tuple_idx, tuple_arg in enumerate(arg):
                        i += node_input_aligner.align(node, tuple_arg, [key, tuple_idx], SiteType.KWARGS_TUPLE)

        modified = i > 0
        return PassResult(gm, modified)

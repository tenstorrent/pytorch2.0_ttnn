import torch
import ttnn
from torch_ttnn.utils import (
    TtnnRowMajorLayout,
    TtnnTileLayout,
    TtnnDevice,
    TtnnBfloat16,
    TtnnUint32,
    HasValidPageSize,
)


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


def call_to_torch_with_meta(g, src_node):
    call_func = g.call_function(ttnn.to_torch, (src_node,))
    if src_node.meta is not None:
        call_func.meta = src_node.meta.copy()
    if "original_input_variations" in call_func.meta:
        call_func.meta["original_input_variations"] = None
    return call_func


def try_call_aten__to_copy_with_meta(g, to_torch_node, target_users_ops):
    # try_add_data_move_in will change dtype to bfloat16
    # so the to_torch's output dtype will be bfloat16, which is incorrect
    # luckly, the meta remain the origin correct dtype
    # so add aten._to_copy(dtype) to correct the dtype
    # TODO: If to_torch can specify dtype, then can merge to_copy on it

    if hasattr(to_torch_node, "meta") and "val" in to_torch_node.meta and hasattr(to_torch_node.meta["val"], "dtype"):
        dtype = to_torch_node.meta["val"].dtype
        if dtype in [torch.float32, torch.float64, torch.bfloat16]:
            # segformer: Index put requires the source and destination dtypes match, got Float for the destination and BFloat16 for the source.
            # _unsafe_index_put_default = torch.ops.aten._unsafe_index_put.default(new_zeros_default, [None, None, unsqueeze_11, _to_copy_22], ttnn_to_torch, True)
            # (Pdb) new_zeros_default.dtype
            # torch.float32
            # (Pdb) ttnn_to_torch.dtype
            # torch.bfloat16 => should have to_copy to be torch.float32
            if torch.ops.aten._unsafe_index_put.default not in target_users_ops:
                return None
        call_func = g.call_function(
            torch.ops.aten._to_copy.default,
            (to_torch_node,),
            {"dtype": dtype},
        )
        call_func.meta = to_torch_node.meta.copy()
        if "original_input_variations" in call_func.meta:
            call_func.meta["original_input_variations"] = None
        return call_func
    else:
        return None


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

    class AlignSpecFromTorch:
        def __init__(self, input_node, device, layout, dtype):
            self.input_node = input_node
            self.device = device
            self.layout = layout
            self.dtype = dtype

        def __eq__(self, other):
            if not isinstance(other, self.__class__):
                return False
            return (
                self.input_node == other.input_node
                and self.device == other.device
                and self.layout == other.layout
                and self.dtype == other.dtype
            )

        def __hash__(self):
            return hash((self.input_node, self.device, self.layout, self.dtype))

    class AlignSpecToTorch:
        def __init__(self, input_node, dtype):
            self.input_node = input_node
            self.dtype = dtype

        def __eq__(self, other):
            if not isinstance(other, self.__class__):
                return False
            return self.input_node == other.input_node and self.dtype == other.dtype

        def __hash__(self):
            return hash((self.input_node, self.dtype))

    class AlignSpecInTtnn:
        def __init__(self, input_node, device, layout, dtype):
            self.input_node = input_node
            self.device = device
            self.layout = layout
            self.dtype = dtype

        def __eq__(self, other):
            if not isinstance(other, self.__class__):
                return False
            return (
                self.input_node == other.input_node
                and self.device == other.device
                and self.layout == other.layout
                and self.dtype == other.dtype
            )

        def __hash__(self):
            return hash((self.input_node, self.device, self.layout, self.dtype))

    def _align_for_special_layout(self, node, spec, input_site, input_site_type):
        if is_target_a_user_of_curr_node(node, ttnn.embedding) and (input_site_type == "args" and input_site == 0):
            spec.dtype = TtnnUint32()
        # TODO(#372): #322 will enable tile layout for more layout change ops
        if node.target in TTNN_LAYOUT_CHANGE_OPS and (input_site_type == "args" and input_site == 0):
            spec.layout = TtnnRowMajorLayout()
            spec.device = "host"
        if node.target in [ttnn.embedding, ttnn.zeros_like, target_wrappers.repeat]:
            # TODO: Only uint32 needs to to_layout on host
            spec.layout = TtnnRowMajorLayout()
            spec.device = TtnnDevice()
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
            spec.layout = TtnnTileLayout()
            spec.device = TtnnDevice()
        return spec

    def _get_align_spec(self, node, input_node, input_site, input_site_type):
        if is_torch_to_ttnn(input_node, node):
            # default set these layout for torch to ttnn
            spec = self.AlignSpecFromTorch(input_node, TtnnDevice(), TtnnTileLayout(), TtnnBfloat16())
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

    def _create_aligned_node(self, spec):
        aligner_nodes = []
        g = self.graph
        if isinstance(spec, self.AlignSpecFromTorch):
            kwargs = {}
            if spec.device is not None and spec.device != "host":
                kwargs["device"] = spec.device
            if spec.layout is not None:
                kwargs["layout"] = spec.layout
            if spec.dtype is not None:
                kwargs["dtype"] = spec.dtype
            aligner_nodes.append(g.call_function(ttnn.from_torch, (spec.input_node,), kwargs))
        elif isinstance(spec, self.AlignSpecToTorch):
            target_users_ops = [user.target for user in spec.input_node.users.keys()]
            aligner_nodes.append(call_to_torch_with_meta(g, spec.input_node))
            if spec.dtype == "by_node_meta":
                copy_node = try_call_aten__to_copy_with_meta(g, aligner_nodes[-1], target_users_ops)
                if copy_node:
                    aligner_nodes.append(copy_node)
        elif isinstance(spec, self.AlignSpecInTtnn):
            if spec.device == "host":
                aligner_nodes.append(g.call_function(ttnn.from_device, (spec.input_node,)))
            else:
                aligner_nodes.append(
                    g.call_function(
                        ttnn.to_device,
                        (aligner_nodes[-1] if aligner_nodes else spec.input_node,),
                        {"device": spec.device},
                    )
                )
            if spec.layout is not None:
                aligner_nodes.append(
                    g.call_function(
                        ttnn.to_layout, (aligner_nodes[-1] if aligner_nodes else spec.input_node, spec.layout)
                    )
                )
        return aligner_nodes[-1]

    def _connect_aligned_node(self, node, aligned_node, input_site, input_site_type):
        if input_site_type == "args":
            input_idx = input_site
            node.update_arg(input_idx, aligned_node)
        elif input_site_type == "kwargs":
            key = input_site
            node.update_kwarg(key, aligned_node)
        elif input_site_type == "args_tuple":
            input_idx = input_site[0]
            tuple_idx = input_site[1]
            old_arg = node.args[input_idx]
            new_arg = list(old_arg)
            new_arg[tuple_idx] = aligned_node
            node.update_arg(input_idx, tuple(new_arg))
        elif input_site_type == "kwargs_tuple":
            key = input_site[0]
            tuple_idx = input_site[1]
            old_arg = node.kwargs[key]
            new_arg = list(old_arg)
            new_arg[tuple_idx] = aligned_node
            node.update_kwarg(key, tuple(new_arg))

    def _connect_aligned_node_layer_norm(self, node, input_node, aligned_node, input_site, input_site_type):
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

    def align(self, node, input_node, input_site, input_site_type):
        assert input_site_type in ["args", "kwargs", "args_tuple", "kwargs_tuple"]
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

        for node in nodes:
            args = node.args
            kwargs = node.kwargs
            for idx, arg in enumerate(args):
                if type(arg) not in [tuple, list, torch.fx.immutable_collections.immutable_list]:
                    i += node_input_aligner.align(node, arg, idx, "args")
                else:
                    for tuple_idx, tuple_arg in enumerate(arg):
                        i += node_input_aligner.align(node, tuple_arg, [idx, tuple_idx], "args_tuple")
            for key, arg in kwargs.items():
                if type(arg) not in [tuple, list, torch.fx.immutable_collections.immutable_list]:
                    i += node_input_aligner.align(node, arg, key, "kwargs")
                else:
                    for tuple_idx, tuple_arg in enumerate(arg):
                        i += node_input_aligner.align(node, tuple_arg, [key, tuple_idx], "kwargs_tuple")

        modified = i > 0
        return PassResult(gm, modified)

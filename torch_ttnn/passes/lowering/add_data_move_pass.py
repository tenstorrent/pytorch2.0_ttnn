# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import logging
import torch
import ttnn
from torch_ttnn.passes.analysis.graph_module_analysis_pass import ModelType
from torch_ttnn.passes.analysis.input_analysis_pass import PrimalTag
from torch_ttnn.utils import (
    GraphCleanup,
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
from operator import getitem

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
    ttnn.atanh,
    ttnn.ceil,
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
    ttnn.round,
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
    ttnn.trunc,
    ttnn.bitwise_not,
]


TTNN_POINTWISE_BINARY_OPS = [
    ttnn.add,
    ttnn.atan2,
    ttnn.div,
    ttnn.eqz,
    ttnn.floor_div,
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

TTNN_MATRIX_MULTIPLICATION_OPS = [
    ttnn.matmul,
    ttnn.linear,
]

TTNN_DATAMOVE_OPS = [
    ttnn.concat,
    ttnn.pad,
    ttnn.permute,
    ttnn.reshape,
    ttnn.experimental.view,
    ttnn.sharded_to_interleaved,
    ttnn.slice,
    ttnn.split,
    ttnn.squeeze,
    ttnn.to_layout,
    ttnn.transpose,
    ttnn.unsqueeze,
]

TTNN_TARGET_WRAPPERS = [
    target_wrappers.clone,
    target_wrappers.repeat,
    target_wrappers.pack_to_tuple,
    target_wrappers.move_to_host,
    target_wrappers.conv,
    target_wrappers.roll,
    target_wrappers.stack,
    target_wrappers.all,
    target_wrappers.concat_tensor,
    target_wrappers.native_layer_norm,
]

TTNN_NORM_OPS = [
    ttnn.group_norm,
]

TTNN_POOL_OPS = [
    ttnn.max_pool2d,
    ttnn.avg_pool2d,
]

TTNN_ROW_LAYOUT_OPS = set(
    [
        ttnn.slice,
        target_wrappers.roll,
        ttnn.argmax,
    ]
)

# Operations that might output row major layouts based on ToTtPass implementation
TTNN_MAYBE_ROW_OPS = set(
    [
        ttnn.pad,
        ttnn.concat,
    ]
)

TTNN_HOST_ONLY_OPS = set()


# For operations limitations
# See https://github.com/tenstorrent-metal/tt-metal/blob/main/ttnn/README.md?plain=1#L19
def is_tt_compute(node) -> bool:
    if not is_function_call(node):
        return False

    # if node is the built-in function "getitem", the result of split
    # we have to check the input of split
    if node.op == "call_function" and node.target.__name__ == "getitem":
        return is_tt_compute(node.args[0])

    return node.target in set(
        TTNN_POINTWISE_UNARY_OPS
        + TTNN_POINTWISE_BINARY_OPS
        + TTNN_POINTWISE_TRINARY_OPS
        + TTNN_MATRIX_MULTIPLICATION_OPS
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
            ttnn.fill,
            ttnn.empty,
            ttnn.transformer.scaled_dot_product_attention,
            ttnn.transformer.attention_softmax_,
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


class NodeInputAligner:
    def __init__(self, graph, device):
        self.graph = graph
        self.device = device
        # aligned_node_dict maps DataMoveSpec to aligned version of the node to prevent calling the same data movement twice
        self.aligned_node_dict = {}
        # marshaled_node_dict maps DataMoveSpec to index in the load_weights function that runs once. This is consumed once when adding data movement, and the DataMoveSpec will
        # then be populated in the aligned_node_dict for further usage
        self.marshaled_node_dict = {}
        self.input_idx = 0

        # fields for data parallel
        self.shard_to_mesh = dict()
        self.replicate_to_mesh = None
        self.concat_to_mesh = dict()

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

    def _reset_to_default_layout(self, input_node, spec):
        # split(list of tensor with row major layout) => getitem(row major layout)
        # convert back to tile layout
        if input_node.target == getitem and input_node.args[0].target == ttnn.split:
            spec.layout = TtnnTileLayout

        # re-tilize max_pool2d after sharded_to_interleaved call - may be able to remove after #418
        if input_node.target == ttnn.sharded_to_interleaved and input_node.args[0].target in [
            ttnn.max_pool2d,
            ttnn.avg_pool2d,
        ]:
            spec.layout = TtnnTileLayout

        # be overly cautious and convert to tile layout. These could already be tilized
        # TODO: only insert layout if needed
        if input_node.target in [ttnn.ones, ttnn.ones_like, ttnn.zeros, ttnn.zeros_like]:
            spec.layout = TtnnTileLayout

        # legalize to the default layout and device
        if input_node.target in TTNN_ROW_LAYOUT_OPS:
            spec.layout = TtnnTileLayout
        if input_node.target in TTNN_MAYBE_ROW_OPS:
            # for now, convert to tile (might be nop)
            # TODO: only insert to_layout call if needed
            spec.layout = TtnnTileLayout
        if input_node.target in TTNN_HOST_ONLY_OPS:
            spec.device = TtnnDevice

        return spec

    def _align_special_cases(self, node, spec, input_site, input_site_type: InputSiteType):
        if node.target == ttnn.embedding:
            # Embedding is not as accurate with TileLayout (allclose with torch.embedding fails)
            if input_site == 0:
                # First input must be uint32
                spec.dtype = TtnnUint32
                spec.layout = TtnnRowMajorLayout
        if node.target in [ttnn.slice, target_wrappers.roll] and (
            input_site_type == self.InputSiteType.ARGS and input_site == 0
        ):
            # Slice can only unpad tilized tensors with full tiles. Make input row major to be safe for now
            # Roll is included because it calls slice under the hood
            spec.layout = TtnnRowMajorLayout
        if node.target == ttnn.split and input_site == 0:
            # Runtime error for tilized inputs to split
            spec.layout = TtnnRowMajorLayout
        if node.target == ttnn.argmax and (input_site_type == self.InputSiteType.ARGS and input_site == 0):
            # According to documentation, argmax input must be BFLOAT16 and ROW_MAJOR
            spec.dtype = TtnnBfloat16
            spec.layout = TtnnRowMajorLayout
        if (
            node.target == target_wrappers.stack
            and isinstance(spec, self.AlignSpecFromTorch)
            and get_dtype(node) in [torch.int32, torch.int64]
        ):
            # This allows ViLT to work by coercing stack inputs to be uint32
            # TODO: remove this and handle stack inputs more generally
            spec.dtype = TtnnUint32
        if node.target == target_wrappers.conv and input_site == 1:
            # TODO(#417, tt-metal#15893): weight currently needs to be on host and can't be moved to device first
            spec.layout = TtnnRowMajorLayout
            spec.device = "host"
        if (
            node.target == ttnn.subtract
            and isinstance(spec, self.AlignSpecFromTorch)
            and get_dtype(node) in [torch.int32, torch.int64]
        ):
            # Needed to have GPT2 pass: from_torch -> subtract -> remainder -> indexing but subtract may go below 0
            # TODO: remove when we have signed int support for required ops
            spec.dtype = TtnnBfloat16

        return spec

    def _get_align_spec(self, node, input_node, input_site, input_site_type: InputSiteType):
        if is_torch_to_ttnn(input_node, node):
            # default set these layout for torch to ttnn
            spec_dtype = TtnnBfloat16
            if get_dtype(input_node) in [torch.int32, torch.int64]:
                spec_dtype = TtnnUint32
            spec = self.AlignSpecFromTorch(input_node, TtnnDevice, TtnnTileLayout, spec_dtype)
            spec = self._align_special_cases(node, spec, input_site, input_site_type)
            return spec
        elif is_ttnn_to_torch(input_node, node):
            spec = self.AlignSpecToTorch(input_node, get_dtype(input_node))
            return spec
        elif is_ttnn_to_ttnn(input_node, node):
            # default do nothing between ttnn to ttnn
            spec = self.AlignSpecInTtnn(input_node, None, None, None)
            spec = self._reset_to_default_layout(input_node, spec)
            spec = self._align_special_cases(node, spec, input_site, input_site_type)

            if spec.device is None and spec.layout is None and spec.dtype is None:
                return None
            return spec
        else:
            return None

    def _change_layout(self, spec):
        need_from_device = spec.device == "host"
        need_to_layout = spec.layout is not None
        need_to_device = spec.device == TtnnDevice

        input_node = spec.input_node

        # mesh device tensors need layout on device
        if need_to_device:
            input_node = self.graph.call_function(ttnn.to_device, (input_node,), {"device": TtnnDevice()})

        if need_to_layout:
            input_node = self.graph.call_function(ttnn.to_layout, (input_node, spec.layout()))

        if need_from_device:
            input_node = self.graph.call_function(ttnn.from_device, (input_node,))

        return input_node

    def _extract_args_kwargs_from_spec(self, spec):
        if isinstance(spec, self.AlignSpecFromTorch):
            kwargs = {}
            args = (spec.input_node,)
            if spec.device is not None and spec.device != "host":
                kwargs["device"] = spec.device()
            if spec.layout is not None:
                kwargs["layout"] = spec.layout()
            if spec.dtype is not None:
                kwargs["dtype"] = spec.dtype()

            # A bit tricky: here we actually end up replacing the input_node with its equivalent from_torch call by accessing its arguments. Sharding and replicating are determined by the wrapper name
            if self.device.get_num_devices() > 1:
                if spec.input_node.target == target_wrappers.shard_tensor:
                    actual_inp_node, shard_dim, _ = spec.input_node.args

                    if self.shard_to_mesh.get(shard_dim) is None:
                        self.shard_to_mesh[shard_dim] = self.graph.call_function(
                            ttnn.ShardTensorToMesh, args=(TtnnDevice(),), kwargs={"dim": shard_dim}
                        )

                    mesh_mapper = self.shard_to_mesh[shard_dim]
                    args = (actual_inp_node,)
                else:
                    if self.replicate_to_mesh is None:
                        self.replicate_to_mesh = self.graph.call_function(
                            ttnn.ReplicateTensorToMesh, args=(TtnnDevice(),)
                        )

                    mesh_mapper = self.replicate_to_mesh
                    args = spec.input_node.args
                kwargs["mesh_mapper"] = mesh_mapper

            return args, kwargs

        elif isinstance(spec, self.AlignSpecToTorch):
            kwargs = {"dtype": spec.dtype}
            args = (spec.input_node,)

            # A bit tricky: here we actually end up replacing the input_node with its equivalent to_torch call by accessing its arguments
            if self.device.get_num_devices() > 1:
                if spec.input_node.target == target_wrappers.concat_tensor:
                    actual_inp_node, shard_dim, _ = spec.input_node.args

                    if self.concat_to_mesh.get(shard_dim) is None:
                        self.concat_to_mesh[shard_dim] = self.graph.call_function(
                            ttnn.ConcatMeshToTensor, args=(TtnnDevice(),), kwargs={"dim": shard_dim}
                        )

                    composer = self.concat_to_mesh[shard_dim]
                    kwargs["mesh_composer"] = composer
                    args = (actual_inp_node,)

            return args, kwargs

        elif isinstance(spec, self.AlignSpecInTtnn):
            return (), {}

        else:
            raise RuntimeError(f"Cannot create aligned node for unknown spec ({spec})")

    def _create_aligned_node(self, spec):
        args, kwargs = self._extract_args_kwargs_from_spec(spec)

        if isinstance(spec, self.AlignSpecFromTorch):
            return self.graph.call_function(ttnn.from_torch, args, kwargs)

        elif isinstance(spec, self.AlignSpecToTorch):
            return self.graph.call_function(ttnn.to_torch, args, kwargs)

        elif isinstance(spec, self.AlignSpecInTtnn):
            return self._change_layout(spec)

        else:
            raise RuntimeError(f"Cannot create aligned node for unknown spec ({spec})")

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

    def marshal_params(self, node, input_node, input_site, input_site_type, first_node):
        if not isinstance(input_node, torch.fx.node.Node):
            return 0

        # examine first arg for multi device case
        check_constant = input_node
        if input_node.op == "call_function" and input_node.target in [
            target_wrappers.shard_tensor,
            target_wrappers.replicate_tensor,
        ]:
            check_constant = input_node.args[0]
        is_constant_for_inference = (check_constant.op == "placeholder") and (
            check_constant.meta.get("primal_tag") in [PrimalTag.PARAMETER, PrimalTag.BUFFER]
        )
        if not is_constant_for_inference:
            return 0

        data_move_spec = self._get_align_spec(node, input_node, input_site, input_site_type)
        if not isinstance(data_move_spec, self.AlignSpecFromTorch):
            # No need to align input_node
            return 0

        if data_move_spec in self.marshaled_node_dict:
            # already handled
            return 0

        self.marshaled_node_dict[data_move_spec] = self.input_idx
        self.input_idx += 1

        return 1

    def align(self, node, input_node, input_site, input_site_type: InputSiteType, first_node, ttnn_inputs):
        # assert input_site_type in ["args", "kwargs", "args_tuple", "kwargs_tuple"]
        data_move_spec = self._get_align_spec(node, input_node, input_site, input_site_type)
        if data_move_spec is None:
            # No need to align input_node
            return 0

        if data_move_spec in self.aligned_node_dict:
            aligned_node = self.aligned_node_dict[data_move_spec]
        elif ttnn_inputs is not None and (input_idx := self.marshaled_node_dict.get(data_move_spec)) is not None:
            with self.graph.inserting_before(node):
                aligned_node = self.graph.call_function(getitem, (ttnn_inputs, input_idx))
                # mark node cached so it isn't deallocated by DeallocationPass
                aligned_node.meta["is_cached"] = True
            # update aligned_node_dict
            self.aligned_node_dict[data_move_spec] = aligned_node
        else:
            # push from_torch calls to top of forward function if they are due to a placeholder
            maybe_forward_input = input_node
            # We have to test the first arg of shard_tensor and replicate_tensor calls instead
            if input_node.op == "call_function" and input_node.target in [
                target_wrappers.shard_tensor,
                target_wrappers.replicate_tensor,
            ]:
                maybe_forward_input = input_node.args[0]
            if (
                isinstance(data_move_spec, self.AlignSpecFromTorch)
                and maybe_forward_input.op == "placeholder"
                and maybe_forward_input.meta.get("primal_tag") != PrimalTag.ARGUMENT
            ):
                # This will push all from_torch calls to the top of the forward function. This shouldn't impact performance, but it may impact memory usage since variables will be
                # live longer than they would if from_torch calls occurred right before usage. If we start running out of DRAM or need to be more careful about memory usage, this
                # is a good place to check
                with self.graph.inserting_before(first_node):
                    aligned_node = self._create_aligned_node(data_move_spec)
            else:
                with self.graph.inserting_before(node):
                    aligned_node = self._create_aligned_node(data_move_spec)
            self.aligned_node_dict[data_move_spec] = aligned_node

        self._connect_aligned_node(node, aligned_node, input_site, input_site_type)

        return 1


def insert_load_params_once(gm, first_node, nodes, node_input_aligner):
    SiteType = NodeInputAligner.InputSiteType
    modifications_count = 0

    for node in nodes:
        args = node.args
        for idx, arg in enumerate(args):
            if isinstance(arg, (tuple, list, torch.fx.immutable_collections.immutable_list)):
                for tuple_idx, tuple_arg in enumerate(arg):
                    modifications_count += node_input_aligner.marshal_params(
                        node, tuple_arg, [idx, tuple_idx], SiteType.ARGS_TUPLE, first_node
                    )
            else:
                modifications_count += node_input_aligner.marshal_params(node, arg, idx, SiteType.ARGS, first_node)

        kwargs = node.kwargs
        for key, arg in kwargs.items():
            if isinstance(arg, (tuple, list, torch.fx.immutable_collections.immutable_list)):
                for tuple_idx, tuple_arg in enumerate(arg):
                    modifications_count += node_input_aligner.marshal_params(
                        node, tuple_arg, [key, tuple_idx], SiteType.KWARGS_TUPLE, first_node
                    )
            else:
                modifications_count += node_input_aligner.marshal_params(node, arg, key, SiteType.KWARGS, first_node)

    # reset run_once_count so recompilation triggers loading weights
    with gm.graph.inserting_before(first_node):
        ttnn_inputs = gm.graph.call_function(
            target_wrappers.run_once,
            tuple(
                [
                    node_input_aligner._extract_args_kwargs_from_spec(spec)
                    for spec in node_input_aligner.marshaled_node_dict.keys()
                ]
            ),
        )

    return modifications_count, ttnn_inputs


class AddDataMovePass(PassBase):
    """Pass that adds instructions to move data between host and device and align tensor dtype and layout.

    This pass is multi-device aware, since it must marshal tensors differently in the multi-device case. This pass attempts to introduce the minimum amount of operations while maintaining correctness and performance.

    :param device: The device on which a workload will run (either a MeshDevice or Device).
    """

    def __init__(self, device):
        self.device = device

    def call(self, gm: torch.fx.GraphModule):
        SiteType = NodeInputAligner.InputSiteType

        modifications_count = 0
        node_input_aligner = NodeInputAligner(gm.graph, self.device)
        nodes = list(gm.graph.nodes)

        first_node = [node for node in nodes if node.op != "placeholder"][0]

        # first load weights
        ttnn_inputs = None
        if gm.meta.get("graph_type") == ModelType.INFERENCE:
            global run_once_count
            target_wrappers.run_once_count = 0
            modifications_count, ttnn_inputs = insert_load_params_once(gm, first_node, nodes, node_input_aligner)

        # then handle rest of the args and kwargs
        for node in nodes:
            args = node.args
            for idx, arg in enumerate(args):
                if isinstance(arg, (tuple, list, torch.fx.immutable_collections.immutable_list)):
                    for tuple_idx, tuple_arg in enumerate(arg):
                        modifications_count += node_input_aligner.align(
                            node, tuple_arg, [idx, tuple_idx], SiteType.ARGS_TUPLE, first_node, ttnn_inputs
                        )
                else:
                    modifications_count += node_input_aligner.align(
                        node, arg, idx, SiteType.ARGS, first_node, ttnn_inputs
                    )

            kwargs = node.kwargs
            for key, arg in kwargs.items():
                if isinstance(arg, (tuple, list, torch.fx.immutable_collections.immutable_list)):
                    for tuple_idx, tuple_arg in enumerate(arg):
                        modifications_count += node_input_aligner.align(
                            node, tuple_arg, [key, tuple_idx], SiteType.KWARGS_TUPLE, first_node, ttnn_inputs
                        )
                else:
                    modifications_count += node_input_aligner.align(
                        node, arg, key, SiteType.KWARGS, first_node, ttnn_inputs
                    )

        modified = modifications_count > 0
        GraphCleanup(gm)
        return PassResult(gm, modified)

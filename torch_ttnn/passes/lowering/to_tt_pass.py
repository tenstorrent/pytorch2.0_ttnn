# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import ttnn
import math
from torch._guards import detect_fake_mode
from torch._subclasses.fake_tensor import unset_fake_temporarily

from torch_ttnn.utils import (
    GraphCleanup,
    TtnnBfloat16,
    TtnnUint32,
    TtnnInt32,
    TtnnUint32,
    TtnnDevice,
    TtnnL1MemoryConfig,
    TtnnRowMajorLayout,
    TtnnTileLayout,
    get_emplace_custom_object_in_graph,
    get_shape,
    get_dtype,
    get_arg,
)
import numpy as np
import torch_ttnn.metrics as metrics

from torch.fx.passes.infra.pass_base import PassBase, PassResult
import torch.fx.traceback as fx_traceback
from . import target_wrappers
from .to_tt_guard import can_lowering_to_ttnn
import operator

relational_scalar_ops = {
    torch.ops.aten.eq.Scalar: ttnn.eq,
    torch.ops.aten.lt.Scalar: ttnn.lt,
    torch.ops.aten.le.Scalar: ttnn.le,
    torch.ops.aten.gt.Scalar: ttnn.gt,
    torch.ops.aten.ge.Scalar: ttnn.ge,
    torch.ops.aten.ne.Scalar: ttnn.ne,
}

# Workaround: If an arg of the model output is argmax then skip conversion
# TODO(kevinwuTT): Handle this case with ttnn ops
int_output_ops = [
    torch.ops.aten.argmax.default,
    torch.ops.aten.argmin.default,
]


ops_incompatible_with_grayskull = {
    torch.ops.aten.ceil.default,
    torch.ops.aten.floor.default,
    torch.ops.aten.round.default,
    torch.ops.aten.round.decimals,
    torch.ops.aten.trunc.default,
}


def is_target_incompatible_with_grayskull(target, device):
    return ttnn.device.is_grayskull(device) and target in ops_incompatible_with_grayskull


def are_args_from_int_output_ops(args):
    for arg in args:
        if isinstance(arg, torch.fx.proxy.Proxy):
            if arg.node.target in int_output_ops:
                return True


def create_call_function(transformer, target, args, kwargs):
    transformer.call_function(target, args, kwargs)


def map_args_to_kwargs(args, kw_map, default_none=False):
    """
    Args:
        args (List): the input arguments
        kw_map (List[str]): the list of ("index in args" : int, "keyword name" : str)
        default_none (bool): put none if the value is missing in args; otherwise don't add the key
    Returns:
        Dict[str, Any]: the extracted values
    """
    kwargs = {}
    for idx, kw in kw_map:
        if idx >= len(args) and not default_none:
            break
        kwargs[kw] = args[idx] if idx < len(args) else None
    return kwargs


def is_getitem_0_only_user(node):
    return all(
        user.op == "call_function" and user.target.__name__ == "getitem" and user.args[1] == 0
        for user in node.users.keys()
    )


# Convert (n, c, x, ...) to (n, x, ..., c)
def insert_ncx_to_nxc(g, input_tensor):
    input_shape = input_tensor.meta["val"].size()
    target_permute = [0] + list(range(2, len(input_shape))) + [1]
    return g.call_function(ttnn.permute, (input_tensor, target_permute))


# Convert sharded (1, 1, nx..., c) to interleaved (n, c, x, ...)
def insert_sharded_nxc_to_ncx(g, output_tensor, output_shape):
    output_tensor = g.call_function(ttnn.sharded_to_interleaved, (output_tensor, TtnnL1MemoryConfig()))
    target_shape = (output_shape[0], *output_shape[2:], output_shape[1])
    output_tensor = g.call_function(ttnn.reshape, (output_tensor, target_shape))
    target_permute = [0, len(output_shape) - 1] + list(range(1, len(output_shape) - 1))
    return g.call_function(ttnn.permute, (output_tensor, target_permute))


TTNN_POINTWISE_UNARY_OPS = {
    torch.ops.aten.abs.default: ttnn.abs,
    torch.ops.aten.acos.default: ttnn.acos,
    torch.ops.aten.acosh.default: ttnn.acosh,
    torch.ops.aten.asin.default: ttnn.asin,
    torch.ops.aten.asinh.default: ttnn.asinh,
    torch.ops.aten.atan.default: ttnn.atan,
    torch.ops.aten.atanh.default: ttnn.atanh,
    torch.ops.aten.ceil.default: ttnn.ceil,
    torch.ops.aten.clamp.default: ttnn.clip,
    torch.ops.aten.cos.default: ttnn.cos,
    torch.ops.aten.cosh.default: ttnn.cosh,
    torch.ops.aten.elu.default: ttnn.elu,
    torch.ops.aten.erf.default: ttnn.erf,
    torch.ops.aten.exp.default: ttnn.exp,
    torch.ops.aten.expm1.default: ttnn.expm1,
    torch.ops.aten.floor.default: ttnn.floor,
    torch.ops.aten.gelu.default: ttnn.gelu,
    torch.ops.aten.hardsigmoid.default: ttnn.hardsigmoid,
    torch.ops.aten.hardswish.default: ttnn.hardswish,
    torch.ops.aten.isinf.default: ttnn.isinf,
    torch.ops.aten.isnan.default: ttnn.isnan,
    torch.ops.aten.log.default: ttnn.log,
    torch.ops.aten.log10.default: ttnn.log10,
    torch.ops.aten.log1p.default: ttnn.log1p,
    torch.ops.aten.log2.default: ttnn.log2,
    torch.ops.aten.logical_not.default: ttnn.logical_not,
    torch.ops.aten.neg.default: ttnn.neg,
    torch.ops.aten.reciprocal.default: ttnn.reciprocal,
    torch.ops.aten.remainder.Scalar: ttnn.remainder,
    torch.ops.aten.relu.default: ttnn.relu,
    torch.ops.aten.round.decimals: ttnn.round,
    torch.ops.aten.rsqrt.default: ttnn.rsqrt,
    torch.ops.aten.sigmoid.default: ttnn.sigmoid,
    torch.ops.aten.sign.default: ttnn.sign,
    torch.ops.aten.sin.default: ttnn.sin,
    torch.ops.aten.sinh.default: ttnn.sinh,
    torch.ops.aten.silu.default: ttnn.silu,
    torch.ops.aten.sqrt.default: ttnn.sqrt,
    torch.ops.aten.tan.default: ttnn.tan,
    torch.ops.aten.tanh.default: ttnn.tanh,
    torch.ops.aten.tril.default: ttnn.tril,
    torch.ops.aten.trunc.default: ttnn.trunc,
}


class ReplaceMoreTt(torch.fx.Transformer):
    def __init__(self, module, device, use_less_ttnn_op_types):
        super().__init__(module)
        get_meta_for_op = lambda op: {node.name: node.meta for node in self.module.graph.nodes if node.op == op}
        self._input_node_meta = get_meta_for_op("placeholder")
        self._get_attr_meta = get_meta_for_op("get_attr")
        self.device = device
        self.use_less_ttnn_op_types = use_less_ttnn_op_types

    def transform(self):
        old_meta = self.module.meta
        result = super().transform()
        result.meta = old_meta
        return result

    def get_attr(self, target, args, kwargs):
        # Restore original metadata for get_attr nodes
        proxy = super().get_attr(target, args, kwargs)
        if proxy.node.name in self._get_attr_meta:
            proxy.node.meta = self._get_attr_meta[proxy.node.name]
        return proxy

    def placeholder(self, target, args, kwargs):
        # Restore original metadata for placeholder nodes
        proxy = super().placeholder(target, args, kwargs)
        if proxy.node.name in self._input_node_meta:
            proxy.node.meta = self._input_node_meta[proxy.node.name]
        return proxy

    def call_function_prop_meta(self, target, args=(), kwargs={}):
        call_func = super().call_function(target, args, kwargs)
        meta = fx_traceback.get_current_meta()
        if meta is not None:
            call_func.node.meta = meta
            if hasattr(self.old_target, "_schema"):
                call_func.node.meta["original_input_variations"] = metrics.collect_input_variation(
                    self.old_target, self.old_args, self.old_kwargs
                )

        return call_func

    def call_function(self, target, args, kwargs):
        # FIXME: `call_function_prop_meta` should be moved to an inner function here instead of using member variables
        self.old_target = target
        self.old_args = args
        self.old_kwargs = kwargs

        class PseudoNode:
            def __init__(self, target, args, kwargs):
                self.target = target
                self.args = args
                self.kwargs = kwargs

        pseudo_node = PseudoNode(target, args, kwargs)
        if not can_lowering_to_ttnn(pseudo_node):
            return self.call_function_prop_meta(target, args, kwargs)

        if are_args_from_int_output_ops(args) or is_target_incompatible_with_grayskull(target, self.device):
            return self.call_function_prop_meta(target, args, kwargs)

        ############################################################
        # Matrix multiplication
        ############################################################
        if target == torch.ops.aten.addmm.default:
            # TODO(kevinwuMCW): include beta, alpha, and optional args
            mm = self.call_function_prop_meta(ttnn.matmul, (args[1], args[2]), kwargs)
            return self.call_function_prop_meta(ttnn.add, (args[0], mm), kwargs)

        if target == torch.ops.aten.bmm.default:
            return self.call_function_prop_meta(ttnn.matmul, args, kwargs)

        if target == torch.ops.aten.linear.default:
            return self.call_function_prop_meta(ttnn.linear, args, kwargs)

        if target == torch.ops.aten.mm.default:
            return self.call_function_prop_meta(ttnn.matmul, args, kwargs)

        ############################################################
        # Pointwise unary
        ############################################################
        if target == torch.ops.aten.hardtanh.default:
            # aten.hardtanh args are positional but ttnn.clip uses kw args
            new_kwargs = map_args_to_kwargs(args, ((1, "min_val"), (2, "max_val")), default_none=True)
            new_args = (args[0],)
            return self.call_function_prop_meta(ttnn.hardtanh, new_args, new_kwargs)

        if target == torch.ops.aten._softmax.default:
            kwargs = {
                "numeric_stable": True,
                **kwargs,
            }
            return self.call_function_prop_meta(ttnn.softmax, args[:2], kwargs)

        ############################################################
        # Pointwise binary
        ############################################################
        if target in relational_scalar_ops:
            return self.call_function_prop_meta(relational_scalar_ops[target], args, kwargs)

        if target == torch.ops.aten.atan2.default:
            return self.call_function_prop_meta(ttnn.atan2, args, kwargs)

        if target == torch.ops.aten.leaky_relu.default:
            if len(args) < 2:
                args = (args[0], 0.01)
            return self.call_function_prop_meta(ttnn.leaky_relu, args, kwargs)

        if target == torch.ops.aten.maximum.default:
            if get_shape(None, args[0]) != get_shape(None, args[1]):
                # see tt-metal#12852
                return self.call_function_prop_meta(target, args, kwargs)
            return self.call_function_prop_meta(ttnn.maximum, args, kwargs)

        if target == torch.ops.aten.minimum.default:
            if get_shape(None, args[0]) != get_shape(None, args[1]):
                # see tt-metal#12852
                return self.call_function_prop_meta(target, args, kwargs)
            return self.call_function_prop_meta(ttnn.minimum, args, kwargs)

        if target in [torch.ops.aten.pow.Scalar, torch.ops.aten.pow.Tensor_Scalar, torch.ops.aten.pow.Tensor_Tensor]:
            if target == torch.ops.aten.pow.Tensor_Tensor:
                shape0 = get_shape(None, args[0])
                shape1 = get_shape(None, args[1])
                if (shape0 != shape1) or shape0 is None or shape1 is None:
                    # not support broadcasting
                    return self.call_function_prop_meta(target, args, kwargs)
            return self.call_function_prop_meta(ttnn.pow, args, kwargs)

        if target == torch.ops.aten.rsub.Scalar:
            return self.call_function_prop_meta(ttnn.rsub, args, kwargs)

        if target == torch.ops.aten.rsub.Tensor:
            # TODO(kevinwuMCW): handle alpha parameter if exists
            return self.call_function_prop_meta(ttnn.sub, (args[1], args[0]), kwargs)

        if target == torch.ops.aten.xlogy.Tensor:
            return self.call_function_prop_meta(ttnn.xlogy, args, kwargs)

        ############################################################
        # Pointwise ternary
        ############################################################
        if target == torch.ops.aten.addcdiv.default:
            value = kwargs.pop("value", 1.0)
            return self.call_function_prop_meta(ttnn.addcdiv, args + (value,), kwargs)

        if target == torch.ops.aten.addcmul.default:
            value = kwargs.pop("value", 1.0)
            return self.call_function_prop_meta(ttnn.addcmul, args + (value,), kwargs)

        if target == torch.ops.aten.where.self:
            return self.call_function_prop_meta(ttnn.where, args, kwargs)

        ############################################################
        # Reduction
        ############################################################
        if target == torch.ops.aten.mean.dim:
            return self.call_function_prop_meta(ttnn.mean, args, kwargs)

        if target == torch.ops.aten.min.default:
            return self.call_function_prop_meta(ttnn.min, args, kwargs)

        ############################################################
        # Other ops
        ############################################################
        if target == torch.ops.aten._adaptive_avg_pool2d.default:
            arg0_size = None
            if hasattr(args[0], "node") and hasattr(args[0].node, "meta"):
                arg0_size = list(args[0].node.meta["val"].size())
            output_size = None
            if len(args) > 1:
                output_size = args[1]
            elif "output_size" in kwargs:
                output_size = kwargs["output_size"]
            if arg0_size is not None and output_size is not None and arg0_size[-2:] == output_size:
                return args[0]
            # TODO: no ttnn op can convert _adaptive_avg_pool2d
            return self.call_function_prop_meta(target, args, kwargs)

        if target == torch.ops.aten.detach.default:
            return args[0]

        if target == torch.ops.aten.as_strided.default:
            unpack = lambda tensor, size, stride, offset=0: (tensor, size, stride, offset)
            tensor, size, stride, offset = unpack(*args)
            ndims = len(size)

            if offset != 0 or len(stride) != ndims:
                return self.call_function_prop_meta(target, args, kwargs)

            dummy = torch.empty(0, *size, dtype=torch.bool)

            for i in range(ndims):
                if stride[i] != dummy.stride(i + 1) and size[i] != 1:
                    return self.call_function_prop_meta(target, args, kwargs)

            return self.call_function_prop_meta(ttnn.reshape, (tensor, size))

        if target == torch.ops.aten.permute.default:
            return self.call_function_prop_meta(ttnn.permute, args, kwargs)

        return self.call_function_prop_meta(target, args, kwargs)


def torch_dtype_to_ttnn_dtype(dtype: torch.dtype):
    # Add newly supported dtypes here:
    dtype_map = {
        torch.float32: TtnnBfloat16(),  # Should this be changed to TtnnFloat32?
        torch.bfloat16: TtnnBfloat16(),
    }
    if dtype in dtype_map:
        return dtype_map.get(dtype)
    else:
        raise RuntimeError(f"Missing conversion from torch.dtype: {dtype} to Ttnn dtype.")


# override some functions from torch.fx.graph.Graph
class GraphWrapper:
    def __init__(self, gm, node):
        self.gm = gm
        self.g = node.graph
        self.node = node

    def call_function(self, target, args=(), kwargs={}):
        new_node = self.g.call_function(target, args, kwargs)
        new_node.meta = dict(self.node.meta)
        if hasattr(self.node.target, "_schema"):
            new_node.meta["original_input_variations"] = metrics.collect_input_variation_from_node(self.node)
        new_node.meta["val"] = self._get_output_val(new_node)
        return new_node

    def inserting_before(self, node):
        return self.g.inserting_before(node)

    def _get_output_val(self, node):
        args = node.args
        # Compute on fake tensor to derive the output fake tensor
        if node.target == ttnn.add:
            return torch.add(self._get_val(args[0]), self._get_val(args[1]))
        if node.target == ttnn.mul:
            return torch.mul(self._get_val(args[0]), self._get_val(args[1]))
        if node.target == ttnn.sub:
            return torch.sub(self._get_val(args[0]), self._get_val(args[1]))
        if node.target in [ttnn.rsqrt, ttnn.sharded_to_interleaved]:
            return self._get_val(args[0])
        # When accessing to self.node.meta, we assume the GraphWrapper is created on a pytorch op mapped to that ttnn op,
        # so we can use the output shape from it
        if node.target in [ttnn.max_pool2d, ttnn.avg_pool2d, target_wrappers.conv]:
            output_val = self._get_val(self.node)
            output_tensor = output_val[0] if isinstance(output_val, tuple) else output_val
            output_shape = list(output_tensor.size())
            return output_tensor.new_empty((1, 1, output_shape[0] * math.prod(output_shape[2:]), output_shape[1]))
        if node.target == ttnn.reshape:
            return torch.reshape(self._get_val(args[0]), args[1])
        if node.target == ttnn.permute:
            return torch.permute(self._get_val(args[0]), args[1])
        return self._get_val(node)

    def _get_val(self, obj):
        if not isinstance(obj, torch.fx.node.Node):
            return obj
        if obj.op == "get_attr":
            val = getattr(self.gm, obj.target)
            fake_mode = detect_fake_mode()
            if isinstance(val, torch.Tensor) and fake_mode is not None:
                val = fake_mode.fake_tensor_converter.from_real_tensor(fake_mode, val)
            return val
        return obj.meta["val"]


def ReplaceMoreTtManually(gm: torch.fx.GraphModule, device, use_less_ttnn_op_types: bool) -> torch.fx.GraphModule:
    nodes = list(gm.graph.nodes)
    for node in nodes:
        if not can_lowering_to_ttnn(node):
            continue
        g = GraphWrapper(gm, node)

        def rewrite_node(node):
            args = node.args
            kwargs = node.kwargs

            def batch_norm_post_process(output, shape, weight, bias):
                if weight is not None:
                    weight = g.call_function(ttnn.reshape, (weight, shape))
                    output = g.call_function(ttnn.mul, (output, weight))
                if bias is not None:
                    bias = g.call_function(ttnn.reshape, (bias, shape))
                    output = g.call_function(ttnn.add, (output, bias))
                return output

            # Non-training batch normalization
            def batch_norm_inference(input, weight, bias, mean, var, momentum, eps):
                assert is_getitem_0_only_user(node), "non-training batch_norm should only have first return value used"
                shape = input.meta["val"].size()
                shape = (1, shape[1]) + (1,) * (len(shape) - 2)
                invstd = g.call_function(ttnn.rsqrt, (g.call_function(ttnn.add, (var, eps)),))
                invstd = g.call_function(ttnn.reshape, (invstd, shape))
                mean = g.call_function(ttnn.reshape, (mean, shape))
                output = g.call_function(ttnn.sub, (input, mean))
                output = g.call_function(ttnn.mul, (output, invstd))
                output = batch_norm_post_process(output, shape, weight, bias)
                return g.call_function(target_wrappers.pack_to_tuple, (output,))

            def lower_binary_eltwise(fn, args):
                shapes = get_shape(gm, args[0]), get_shape(gm, args[1])

                if any(s is None for s in shapes):
                    return None

                if max(map(len, shapes)) > 4 and shapes[0][-3:-2] != shapes[1][-3:-2]:
                    return None

                def cast_bf16(target, other):
                    if get_dtype(target) in [torch.int32, torch.int64] and get_dtype(other) in [
                        torch.bfloat16,
                        torch.float32,
                    ]:
                        return g.call_function(ttnn.typecast, args=(target, TtnnBfloat16()))
                    else:
                        return target

                new_args = (cast_bf16(args[0], args[1]), cast_bf16(args[1], args[0]))

                return g.call_function(fn, new_args)

            if node.target == torch.ops.aten.add.Tensor:
                return lower_binary_eltwise(ttnn.add, args)

            if node.target == torch.ops.aten.mul.Tensor:
                return lower_binary_eltwise(ttnn.mul, args)

            if node.target == torch.ops.aten.sub.Tensor:
                return lower_binary_eltwise(ttnn.sub, args)

            if node.target == torch.ops.aten.tanh.default:
                # TODO: Remove once tanh accuracy implementation is realized as a device operation in tt-metal
                new_kwargs = kwargs.copy()
                new_kwargs["accuracy"] = True
                kwargs = new_kwargs

            if node.target in TTNN_POINTWISE_UNARY_OPS:
                return g.call_function(TTNN_POINTWISE_UNARY_OPS[node.target], args, kwargs)

            if node.target == torch.ops.aten.round.default:
                return g.call_function(ttnn.round, (args[0],), {"decimals": 0})

            if node.target == torch.ops.aten.clone.default:
                # Only convert if the input is from graph arguments and node is also returned as an output
                # Otherwise, optimize node out and return input
                node_users = list(node.users.keys())
                if not (args[0].op == "placeholder" and len(node_users) == 1 and node_users[0].op == "output"):
                    return args[0]

                arg_metadata = node.meta["val"]
                try:
                    ttnn_dtype = torch_dtype_to_ttnn_dtype(arg_metadata.dtype)
                except:
                    return None
                # Add additional logic to choose the appropriate memory_config type: DRAM or L1
                return g.call_function(target_wrappers.clone, args=(args[0],))

            if node.target == torch.ops.aten.native_layer_norm.default:
                input_tensor, normalized_shape, weight, bias, epsilon = args

                in_tensor_shape = input_tensor.meta["val"].size()
                mean_rstd_shape = node.meta["val"][1].size()
                torch_dtype = input_tensor.meta["val"].dtype
                ttnn_dtype = torch_dtype_to_ttnn_dtype(torch_dtype)
                norm_dims = len(normalized_shape)

                # aten.native_layer_norm keeps the normalized dimension for mean and rstd,
                # but ttnn.moreh.layer_norm does not.
                ttnn_mean_rstd_shape = in_tensor_shape[:-norm_dims]

                # At the time of implementation, ttnn.layer_norm is marginally faster
                # than moreh.layer_norm if only layer_norm output is needed.
                # Check if mean and/or rstd is used. The output from the wrapper
                # can be a tuple of 1, 2, or 3 items. The 1st item will always be layer_norm.
                # The 2nd can be mean or rstd. The 3rd will always be rstd if it exists.
                # Since `getitem` always follows layer_norm, the number of direct users of this
                # node should always be 1, 2, or 3.
                node_users = list(node.users.keys())
                use_mean = False
                use_rstd = False
                # check the 2nd item if it's mean or rstd
                if len(node_users) > 1:
                    getitem = node_users[1]
                    if getitem.args[1] == 1:
                        use_mean = True
                    if getitem.args[1] == 2:
                        use_rstd = True
                # if the 3rd item exists, it will always be rstd
                if len(node_users) > 2:
                    use_rstd = True

                new_node = g.call_function(
                    target_wrappers.native_layer_norm,
                    (
                        input_tensor,
                        in_tensor_shape,
                        mean_rstd_shape,
                        ttnn_mean_rstd_shape,
                        ttnn_dtype,
                        norm_dims,
                        weight,
                        bias,
                        epsilon,
                        use_mean,
                        use_rstd,
                        TtnnDevice(),
                    ),
                )

                # update metadata since original op does not have dtype for mean and rstd outputs
                for node_user in node_users:
                    node_user.meta["val"] = node_user.meta["val"].to(torch_dtype)

                return new_node

            if node.target == torch.ops.aten.zeros.default:
                return g.call_function(ttnn.zeros, args=args, kwargs={"device": TtnnDevice()})

            if node.target == torch.ops.aten.zeros_like.default:
                # TODO(#280): Doesn't support 1D output tensor in tile layout (#280)
                if len(node.meta["val"].shape) < 2:
                    return None
                return g.call_function(ttnn.zeros_like, args, kwargs={"device": TtnnDevice()})

            if node.target == torch.ops.aten.ones.default:
                return g.call_function(ttnn.ones, args=args, kwargs={"device": TtnnDevice()})

            """
            # NOTE(kevinwuTT): aten.arange.default starts with 0 which is unsupported by ttnn.arange at the moment
            if node.target == torch.ops.aten.arange.default:
                # start = 0, step = 1
                new_args = (0, args[0], 1)
                return g.call_function(ttnn.arange, args=new_args)
            """
            if node.target == torch.ops.aten.arange.start:
                # NOTE(kevinwuTT): ttnn.arange does not support starting values smaller than 2 currently
                if args[0] >= 2:
                    # step = 1
                    new_args = (args[0], args[1], 1)
                    return g.call_function(ttnn.arange, args=new_args)
                return None

            if node.target == torch.ops.aten.arange.start_step:
                # NOTE(kevinwuTT): ttnn.arange does not support starting values smaller than 2 currently
                if args[0] >= 2:
                    new_args = (args[0], args[1], args[2])
                    return g.call_function(ttnn.arange, args=new_args)
                return None

            if node.target == torch.ops.aten.eq.Tensor:
                # Combine this with relational_scalar_ops
                if np.prod(args[1].meta["val"].size()) != 1:
                    return g.call_function(
                        ttnn.eq,
                        args=args,
                        kwargs={},
                    )
                return None

            if node.target == torch.ops.aten.full.default:
                new_kwargs = {
                    "fill_value": args[1],
                    "device": TtnnDevice(),
                    "layout": TtnnTileLayout(),
                }
                return g.call_function(ttnn.full, args=(args[0],), kwargs=new_kwargs)

            if node.target == torch.ops.aten.baddbmm.default:
                # out = beta * input + alpha * (batch1 @ batch2)
                # if beta is 0, input is ignored, and nan and inf in it will not be propogated
                new_node = g.call_function(ttnn.matmul, args=(args[1], args[2]))
                alpha = kwargs.get("alpha", 1)
                beta = kwargs.get("beta", 1)

                if alpha != 1:
                    new_node = g.call_function(ttnn.multiply, args=(new_node, alpha))

                if beta == 0:
                    return new_node

                if beta == 1:
                    return g.call_function(ttnn.add, args=(args[0], new_node))

                beta_node = g.call_function(ttnn.multiply, args=(args[0], beta))
                return g.call_function(ttnn.add, args=(beta_node, new_node))

            if node.target == torch.ops.aten.embedding.default:
                tiled = args[1].meta.get("val")
                tiled = False if tiled is None else tiled.size()[-1] % ttnn.TILE_SIZE == 0
                layout = TtnnTileLayout() if tiled else TtnnRowMajorLayout()
                tensor = g.call_function(ttnn.embedding, (args[1], args[0]), {"layout": layout})
                return tensor if tiled else g.call_function(ttnn.to_layout, (tensor, TtnnTileLayout()))

            if node.target == torch.ops.aten.div.Tensor:
                if isinstance(args[1], (float, int)):
                    return g.call_function(ttnn.mul, (args[0], 1.0 / args[1]), {})

                if get_shape(gm, args[0]) == get_shape(gm, args[1]):
                    return g.call_function(ttnn.div, args, {})

                recip = g.call_function(ttnn.reciprocal, (args[1],), {})
                return g.call_function(ttnn.mul, (args[0], recip), {})

            if node.target == torch.ops.aten.floor_divide.default:
                return g.call_function(ttnn.floor_div, args, {})

            if node.target == torch.ops.aten.expand.default:
                if not (hasattr(args[0], "meta") and "val" in args[0].meta and hasattr(args[0].meta["val"], "size")):
                    return None
                if not (hasattr(node, "meta") and "val" in node.meta and hasattr(node.meta["val"], "size")):
                    return None
                input_tensor_shape = args[0].meta["val"].size()
                output_shape = node.meta["val"].size()
                if input_tensor_shape.numel() == output_shape.numel():
                    if input_tensor_shape != output_shape:
                        return g.call_function(ttnn.reshape, args=(args[0], list(output_shape)))
                    else:
                        return args[0]

                input_shape = np.ones(len(output_shape), dtype=int)
                input_shape[-len(input_tensor_shape) :] = input_tensor_shape
                multiplier = np.array(output_shape) // np.array(input_shape)

                np_output_shape = np.array(list(output_shape))
                expand_multiplier = np_output_shape[np_output_shape > 1] // input_shape[np_output_shape > 1]
                expand_index = np.where(expand_multiplier > 1)[0]

                if input_tensor_shape[-1] % 2 == 0 and np.all(expand_index == np.arange(len(expand_index))):
                    return g.call_function(ttnn.expand, args=(args[0], list(output_shape)))

                # aten.expand and ttnn.repeat has different meaning for their `shape` argument
                # aten.expand: the desired output shape, where respective singleton dims are broadcasted
                # ttnn.repeat: the number of times to repeat a respective singleton dim
                if len(input_tensor_shape) == len(output_shape):
                    return g.call_function(target_wrappers.repeat, args=(args[0], multiplier.tolist()))

                return None

            if node.target == torch.ops.aten.slice.Tensor:
                tensor, dim, start, end, *step = args
                if tensor.op == "get_attr":
                    value = getattr(gm, tensor.target)
                    input_size = list(value.size())
                else:
                    input_size = list(tensor.meta["val"].size())

                [step] = step or [1]
                rank = len(input_size)

                if dim >= rank:
                    return None

                # Check if no-op, just return the input tensor
                if start == 0 and end >= input_size[dim]:
                    return tensor

                slice_start = np.zeros(rank, dtype=int)
                slice_end = input_size

                # For negative end values
                if end < 0:
                    end = input_size[dim] + end
                else:
                    end = np.clip(end, a_min=None, a_max=input_size[dim])

                slice_start[dim] = start
                slice_end[dim] = end

                return g.call_function(ttnn.slice, (tensor, [*slice_start], [*slice_end]))

            if node.target == torch.ops.aten.repeat.default:
                tensor, sizes = args
                shape = get_shape(gm, tensor)
                if shape is None:
                    return None

                if np.prod(sizes) == 1:
                    return tensor

                # Current repeat implementation requires aligned last dim when repeating on last dim
                if sizes[-1] == 1 or shape[-1] % 16 == 0:
                    return g.call_function(target_wrappers.repeat, args)

                return None

            if node.target == torch.ops.aten.squeeze.dim or node.target == torch.ops.aten.squeeze.default:
                return g.call_function(ttnn.squeeze, args=args, kwargs=kwargs)

            if node.target == torch.ops.aten.unsqueeze.default:
                output_shape_num_element = node.meta["val"].numel()
                if output_shape_num_element == 0:
                    return args[0]
                output_size = list(node.meta["val"].size())
                return g.call_function(ttnn.reshape, args=(args[0], output_size))

            if node.target in [torch.ops.aten.transpose.int, torch.ops.aten.t.default]:
                rank = len(node.meta["val"].size())
                if rank < 2:
                    # Less 2D transpose is no-op
                    return args[0]
                if node.target == torch.ops.aten.t.default:
                    assert rank == 2, "Input tensor should only be 2D here"
                    dim0 = 0
                    dim1 = 1
                else:
                    dim0 = args[1]
                    dim1 = args[2]

                dim0 = (dim0 + rank) % rank
                dim1 = (dim1 + rank) % rank

                # directly transpose only support rank <= 4
                if rank <= 4:
                    return g.call_function(ttnn.transpose, args=(args[0], dim0, dim1))

                # Try to reshape. Find the new shape here
                #   eg. the original shape [A, B, C, D, E] shape[dim0] = A, shape[dim1] = D
                #   reshape to [A, (B*C), D, E]
                original_shape = list(args[0].meta["val"].size())
                dim0, dim1 = (dim0, dim1) if dim0 < dim1 else (dim1, dim0)

                new_dim0, new_dim1 = 0, 1
                new_shape = []
                if len(original_shape[:dim0]) > 0:
                    new_shape.append(np.prod(original_shape[:dim0]))
                    new_dim0 += 1
                    new_dim1 += 1

                new_shape.append(original_shape[dim0])

                if len(original_shape[dim0 + 1 : dim1]) > 0:
                    new_shape.append(np.prod(original_shape[dim0 + 1 : dim1]))
                    new_dim1 += 1

                new_shape.append(original_shape[dim1])

                if dim1 + 1 < rank:
                    new_shape.append(np.prod(original_shape[dim1 + 1 :]))

                # if the rank of reshaped result still <= 4, then do
                #    reshape->transpose->reshape
                if len(new_shape) <= 4:
                    reshaped = g.call_function(ttnn.reshape, args=(args[0], list(new_shape)))
                    transposed = g.call_function(ttnn.transpose, args=(reshaped, new_dim0, new_dim1))
                    output_shape = list(node.meta["val"].size())
                    return g.call_function(ttnn.reshape, args=(transposed, list(output_shape)))

                return None

            if node.target == torch.ops.aten.constant_pad_nd.default:
                input, pad = args[0], args[1]
                if len(args) > 2:
                    value = args[2]
                else:
                    value = 0
                # TODO(#516)
                if any(p < 0 for p in pad):
                    return None
                input_shape = input.meta["val"].size()
                output_shape = node.meta["val"].size()
                rank = len(input_shape)
                full_pad = [(0, 0)] * (rank - len(pad))
                # The order of pad from pytorch is reversed
                full_pad += [(pad[i], pad[i + 1]) for i in range(0, len(pad), 2)][::-1]

                # TODO(#514)
                if rank > 4:
                    return None

                # Change layout to row-major for non-tile-size-aligned tensor or front padding
                if (
                    rank < 2
                    or input_shape[-1] % ttnn.TILE_SIZE != 0
                    or input_shape[-2] % ttnn.TILE_SIZE != 0
                    or full_pad[-1][1] % ttnn.TILE_SIZE != 0
                    or full_pad[-2][1] % ttnn.TILE_SIZE != 0
                ) or not all(f == 0 for f, _ in full_pad):
                    input = g.call_function(ttnn.to_layout, args=(input, TtnnRowMajorLayout()))

                return g.call_function(ttnn.pad, args=(input, full_pad, value))

            if node.target in [torch.ops.aten.view.default, torch.ops.aten._unsafe_view.default]:
                input_tensor_num_element = args[0].meta["val"].numel()
                output_shape_num_element = node.meta["val"].numel()
                if input_tensor_num_element == 0 or output_shape_num_element == 0:
                    return None

                input_shape = args[0].meta["val"].shape
                output_shape = args[1]

                # To lower as ttnn.experimental.view:
                # * the last dimension must not change
                # * In Layout::TILE the second last two dimensions must not change OR there is no padding on the second last dimension
                # Be cautious and assume Layout::TILE for now

                last_dimension_constant = input_shape[-1] == output_shape[-1]
                second_last_dimension_constant = (
                    len(input_shape) > 1 and len(output_shape) > 1 and input_shape[-2] == output_shape[-2]
                )
                second_last_dimension_unpadded = (
                    len(input_shape) > 1
                    and len(output_shape) > 1
                    and input_shape[-2] % ttnn.TILE_SIZE == 0
                    and output_shape[-2] % ttnn.TILE_SIZE == 0
                )

                if last_dimension_constant and (second_last_dimension_constant or second_last_dimension_unpadded):
                    return g.call_function(ttnn.experimental.view, (args[0], args[1]), {})
                else:
                    return g.call_function(ttnn.reshape, (args[0], args[1]), {})

            if node.target == torch.ops.aten.split.Tensor:
                if len(args[0].meta["val"].size()) == 1:
                    # For example, the input shape original is [768]
                    # But due to issue #390 it become [1, 768] and cause failed
                    # remove this part once #390 is solved
                    return None

                # convert relative split dim to absolute
                dim = args[2] if len(args) > 2 else 0
                if dim >= 0:
                    split_dim = dim
                else:
                    split_dim = len(args[0].meta["val"].size()) + dim

                # convert from PyTorch size of chunk to ttnn number of chunks
                if isinstance(args[1], int):
                    chunk_size = args[1]
                else:
                    # ttnn.split only supports chunks of same size.
                    return None

                new_args = (args[0], chunk_size, split_dim)
                return g.call_function(ttnn.split, args=new_args)

            if node.target == torch.ops.aten._to_copy.default:
                # Keep it if the graph output uses this op
                target_users_ops = [user.target for user in node.users.keys()]
                if "output" in target_users_ops:
                    return None

                src_dtype, dst_dtype = node.args[0].meta["val"].dtype, kwargs["dtype"]

                # casting to bool type is equivalent to checking if the value is not 0
                if dst_dtype == torch.bool:
                    return g.call_function(ttnn.ne, args=(args[0], 0))

                try:
                    ttnn_dtype = torch_dtype_to_ttnn_dtype(dst_dtype)
                    return g.call_function(ttnn.typecast, args=(node.args[0], ttnn_dtype))
                except:
                    pass

                # Keep it if the cast is not supported
                if src_dtype in [torch.bool, torch.int32, torch.int64] and dst_dtype not in [
                    torch.int32,
                    torch.int64,
                    torch.bfloat16,
                ]:
                    return None

                # Update the dtype of the input node's metadata value to match the destination dtype
                if hasattr(node.args[0], "meta") and "val" in node.args[0].meta:
                    node.args[0].meta["val"] = node.args[0].meta["val"].to(dst_dtype)

                # Essentially remove this op
                return node.args[0]

            if node.target == torch.ops.aten.fill.Scalar:
                return g.call_function(ttnn.fill, args=args)

            if node.target in [torch.ops.aten.masked_fill.Scalar, torch.ops.aten.masked_fill.Tensor]:
                # aten.masked_fill is equivalent to the following:
                # masked_fill = (tensor * (ones - mask)) + (mask * full)

                tensor, mask, fill_value = args
                tensor_shape = get_shape(gm, tensor)
                mask_shape = get_shape(gm, mask)

                # check if divisible, otherwise skip
                np_tensor_shp = np.array(tensor_shape)
                np_mask_shp = np.array(mask_shape)
                if np.sum(np_tensor_shp % np_mask_shp) == 0:
                    # check if the fill_value is a constant
                    if isinstance(fill_value, torch.fx.node.Node) and fill_value.op == "get_attr":
                        with unset_fake_temporarily():
                            fill_value_attr = getattr(gm, fill_value.target)
                            if fill_value_attr.numel() == 1:
                                # extract single fill value
                                fill_value = fill_value_attr.item()
                            else:
                                # extract torch.tensor constant
                                fill_value = fill_value_attr.data

                    if isinstance(fill_value, (float,)):
                        full_kwargs = {"fill_value": fill_value, "device": TtnnDevice(), "layout": TtnnTileLayout()}
                        full = g.call_function(ttnn.full, (list(tensor_shape),), full_kwargs)
                    else:
                        # No cases for non-scalar fill value.
                        return None

                    mask_bcst = mask
                    if not np.all(np_tensor_shp == np_mask_shp):
                        multiplier = np_tensor_shp // np_mask_shp
                        mask_bcst = g.call_function(target_wrappers.repeat, args=(mask, multiplier.tolist()))

                    kwargs = {"dtype": TtnnBfloat16(), "layout": TtnnTileLayout(), "device": TtnnDevice()}
                    ones = g.call_function(ttnn.ones, (tensor_shape,), kwargs)
                    mask_flip = g.call_function(ttnn.subtract, (ones, mask_bcst))
                    tensor_masked = g.call_function(ttnn.multiply, (tensor, mask_flip))

                    full_masked = g.call_function(ttnn.multiply, (mask_bcst, full))
                    masked_fill = g.call_function(ttnn.add, (tensor_masked, full_masked))

                    return masked_fill
                else:
                    return None

            if node.target == torch.ops.aten.select.int:
                tensor, dim, start = args

                input_shape = get_shape(gm, args[0])
                output_shape = get_shape(gm, node)

                slice_start, slice_end = [0] * len(input_shape), list(input_shape)
                slice_start[dim] = (start + input_shape[dim]) % input_shape[dim]
                slice_end[dim] = slice_start[dim] + 1

                slice_tensor = g.call_function(ttnn.slice, (tensor, [*slice_start], [*slice_end]))

                return g.call_function(ttnn.reshape, args=(slice_tensor, list(output_shape)))

            if node.target == torch.ops.aten.cumsum.default:
                tensor, dim = args
                input_shape = get_shape(gm, tensor)
                rank = len(input_shape)
                if rank > 4:
                    return None
                dim = (dim + rank) % rank
                # Unsqueeze input tensor to 4D for cumsum
                # TODO(#367): Special case if dim is inner-most 2 dim. Unsqueeze (x, y) to (x, y, 1, 1) as cumsum currently only support N and C
                if (dim - rank) >= -2:
                    if rank <= 2:
                        input_4d_shape = (1,) * (2 - rank) + (*input_shape, 1, 1)
                    elif rank == 3 and dim == 1:
                        input_4d_shape = (*input_shape, 1)
                    else:
                        return None
                else:
                    input_4d_shape = (1,) * (4 - rank) + input_shape
                    dim += 4 - rank
                input_4d = g.call_function(ttnn.reshape, (tensor, input_4d_shape))
                output_4d = g.call_function(ttnn.moreh_cumsum, (input_4d, dim), kwargs)
                return g.call_function(ttnn.reshape, (output_4d, input_shape))

            if node.target == torch.ops.aten.cat.default:
                tensors = args[0]
                if len(tensors) == 1:
                    return tensors[0]
                dim = 0
                if len(args) > 1:
                    dim = args[1]
                rank = len(node.meta["val"].size())
                dim = (dim + rank) % rank
                layout = TtnnTileLayout() if rank == 4 else TtnnRowMajorLayout()

                tensor_list = []
                for tensor in tensors:
                    tensor_list.append(g.call_function(ttnn.to_layout, (tensor,), {"layout": layout}))

                return g.call_function(ttnn.concat, (tensor_list, dim))

            if node.target == torch.ops.aten.sum.default:
                sum_tensor = g.call_function(ttnn.sum, (args[0],))
                return g.call_function(torch.ops.aten.squeeze.default, args=(sum_tensor,))

            if node.target == torch.ops.aten.max_pool2d_with_indices.default:
                params = map_args_to_kwargs(
                    args,
                    (
                        (0, "input_tensor"),
                        (1, "kernel_size"),
                        (2, "stride"),
                        (3, "padding"),
                        (4, "dilation"),
                        (5, "ceil_mode"),
                    ),
                )
                input_tensor = params["input_tensor"]
                input_shape = input_tensor.meta["val"].size()
                batch_size, in_c, in_h, in_w = input_shape
                kernel_size = params["kernel_size"]
                stride = params.get("stride", kernel_size)
                padding = params.get("padding", (0, 0))
                dilation = params.get("dilation", (1, 1))
                ceil_mode = params.get("ceil_mode", False)
                if (
                    # # TODO: in_c must be 16 or a multiple of 32
                    (in_c != 16 and in_c % 32 != 0)
                    # TODO(#419): Currently fails with in_c < 16
                    or in_c < 16
                    # TODO(tt-metal#12099): Currently it doesn't return indices. Convert if only the value is used
                    or not is_getitem_0_only_user(node)
                ):
                    return None

                input_tensor = insert_ncx_to_nxc(g, input_tensor)
                # TODO(#423): reshape can be removed if (N, H, W, C) is supported
                input_tensor = g.call_function(ttnn.reshape, (input_tensor, (1, 1, batch_size * in_h * in_w, in_c)))
                # TODO(#418): max_pool2d fails with input tensors in tile layout for some shapes
                input_tensor = g.call_function(ttnn.to_layout, (input_tensor, TtnnRowMajorLayout()))
                output_tensor = g.call_function(
                    ttnn.max_pool2d,
                    (
                        input_tensor,
                        batch_size,
                        in_h,
                        in_w,
                        in_c,
                        kernel_size,
                        stride,
                        padding,
                        dilation,
                    ),
                    {"ceil_mode": ceil_mode},
                )
                output_tensor = insert_sharded_nxc_to_ncx(g, output_tensor, node.meta["val"][0].size())
                # TODO(tt-metal#12099): Currently it doesn't return indices. Pack into tuple to maintain the type
                return g.call_function(target_wrappers.pack_to_tuple, (output_tensor,))

            if node.target == torch.ops.aten.avg_pool2d.default:
                params = map_args_to_kwargs(
                    args,
                    (
                        (0, "input_tensor"),
                        (1, "kernel_size"),
                        (2, "stride"),
                        (3, "padding"),
                        (4, "ceil_mode"),
                        (5, "count_include_pad"),
                        (6, "divisor_override"),
                    ),
                )
                input_tensor = params["input_tensor"]
                input_shape = input_tensor.meta["val"].size()
                batch_size, in_c, in_h, in_w = input_shape
                kernel_size = params["kernel_size"]
                stride = params.get("stride", kernel_size)
                padding = params.get("padding", (0, 0))
                ceil_mode = params.get("ceil_mode", False)
                count_include_pad = params.get("count_include_pad", True)
                divisor_override = params.get("divisor_override", None)

                dilation = [1, 1]

                if (
                    # # TODO: in_c must be 16 or a multiple of 32
                    (in_c != 16 and in_c % 32 != 0)
                    # TODO(#419): Currently fails with in_c < 16
                    or in_c < 16
                ):
                    return None
                if ceil_mode or not count_include_pad or divisor_override is not None:
                    return None
                input_tensor = insert_ncx_to_nxc(g, input_tensor)
                input_tensor = g.call_function(ttnn.reshape, (input_tensor, (1, 1, batch_size * in_h * in_w, in_c)))
                input_tensor = g.call_function(ttnn.to_layout, (input_tensor, TtnnRowMajorLayout()))
                output_tensor = g.call_function(
                    ttnn.avg_pool2d,
                    (
                        input_tensor,
                        batch_size,
                        in_h,
                        in_w,
                        in_c,
                        kernel_size,
                        stride,
                        padding,
                        dilation,
                    ),
                    (
                        {
                            "ceil_mode": ceil_mode,
                        }
                    ),
                )
                return insert_sharded_nxc_to_ncx(g, output_tensor, node.meta["val"].size())

            if node.target == torch.ops.aten._native_batch_norm_legit_no_training.default:
                return batch_norm_inference(*args)

            if node.target == torch.ops.aten.convolution.default:
                params = map_args_to_kwargs(
                    args,
                    (
                        (0, "input_tensor"),
                        (1, "weight_tensor"),
                        (2, "bias_tensor"),
                        (3, "stride"),
                        (4, "padding"),
                        (5, "dilation"),
                        (6, "transposed"),
                        (7, "output_padding"),
                        (8, "groups"),
                    ),
                )
                input_node = params["input_tensor"]
                input_shape = list(input_node.meta["val"].size())
                in_spatial_shape = input_shape[2:]
                in_spatial_size = len(in_spatial_shape)
                weight_tensor = params["weight_tensor"]
                weight_shape = list(weight_tensor.meta["val"].size())
                kernel_spatial_shape = weight_shape[2:]

                transposed = params.get("transposed", False)
                groups = params.get("groups", 1)
                stride = params.get("stride", [1] * in_spatial_size)
                padding = params.get("padding", [0] * in_spatial_size)
                dilation = params.get("dilation", [1] * in_spatial_size)
                output_padding = params.get("output_padding", [0] * in_spatial_size)

                # TODO(tt-metal#16258): conv1d API doesn't support transposed yet
                if in_spatial_size == 1 and transposed:
                    return None

                batch_size, in_c = input_shape[:2]
                in_nhw = math.prod([batch_size] + in_spatial_shape)
                out_c = weight_shape[1] if transposed else weight_shape[0]

                input_tensor = insert_ncx_to_nxc(g, input_node)
                # TODO(tt-metal#15148): ttnn.conv2d internal reshape fails with padding
                input_tensor = g.call_function(ttnn.reshape, (input_tensor, (1, 1, in_nhw, in_c)))
                bias_tensor = params.get("bias_tensor", None)
                if bias_tensor is not None:
                    bias_shape = bias_tensor.meta["val"].size()
                    bias_tensor = g.call_function(
                        ttnn.reshape,
                        (bias_tensor, (1,) * (4 - len(bias_shape)) + bias_shape),
                    )
                    bias_tensor = g.call_function(target_wrappers.move_to_host, (bias_tensor, TtnnRowMajorLayout()))
                output_tensor = g.call_function(
                    target_wrappers.conv,
                    (
                        input_tensor,
                        weight_tensor,
                        bias_tensor,
                        batch_size,
                        in_c,
                        out_c,
                        in_spatial_shape,
                        kernel_spatial_shape,
                        stride,
                        padding,
                        dilation,
                        groups,
                        TtnnDevice(),
                        transposed,
                        output_padding if transposed else None,
                    ),
                )
                return insert_sharded_nxc_to_ncx(g, output_tensor, node.meta["val"].size())

            if node.target == torch.ops.aten.slice_scatter.default:
                tensor, src_tensor, dim, start, end, *step = args

                tensor_shape = tensor.meta["val"].size()
                src_tensor_shape = src_tensor.meta["val"].size()

                # nothing to slice, result tensors == src_tensor
                if tensor_shape == src_tensor_shape:
                    return src_tensor

                # Convert both inputs to bfloat16 because ttnn.concat does not work with certain
                # shapes if they are of uint32 dtype.
                # https://github.com/tenstorrent/tt-metal/issues/20376
                if tensor.meta["val"].dtype not in [torch.bfloat16, torch.float]:
                    tensor = g.call_function(ttnn.typecast, (tensor, TtnnBfloat16()))

                if src_tensor.meta["val"].dtype not in [torch.bfloat16, torch.float]:
                    src_tensor = g.call_function(ttnn.typecast, (src_tensor, TtnnBfloat16()))

                # slice_scatter could be concat([pre_slice_tensor, src_tensor, post_slice_tensor])
                rank = len(tensor_shape)
                [step] = step or [1]

                assert dim < rank, f"The slice dim {dim} should be less than rank {rank}"

                dim = (dim + rank) % rank
                start = start if start is not None else 0
                start = start if start >= 0 else (start + tensor_shape[dim])
                end = end if end is not None else tensor_shape[dim]
                end = end if end >= 0 else (end + tensor_shape[dim])
                end = 0 if end < 0 else min(tensor_shape[dim], end)

                tensors_list = []
                # pre_slice_tensor
                if start > 0:
                    slice_start = [0] * rank
                    slice_end = list(tensor_shape)
                    slice_end[dim] = start
                    tensors_list.append(g.call_function(ttnn.slice, (tensor, slice_start, slice_end)))

                # src_tensor
                tensors_list.append(src_tensor)

                # post_slice_tensor
                if end < tensor_shape[dim]:
                    slice_start = [0] * rank
                    slice_start[dim] = end
                    slice_end = list(tensor_shape)
                    tensors_list.append(g.call_function(ttnn.slice, (tensor, slice_start, slice_end)))

                # concat all together
                tensors_to_concat = []
                for tensor in tensors_list:
                    tensors_to_concat.append(g.call_function(ttnn.to_layout, (tensor,), {"layout": TtnnTileLayout()}))

                # Bug: https://github.com/tenstorrent/tt-metal/issues/20205
                # If rank is 1D, unsqueeze to 2D, then squeeze back to 1D
                # Delete this block once the bug is fixed.
                if rank == 1:
                    for idx, ten in enumerate(tensors_to_concat):
                        tensors_to_concat[idx] = g.call_function(ttnn.unsqueeze, (ten, 0))

                    concat = g.call_function(ttnn.concat, (tensors_to_concat, dim + 1))
                    return g.call_function(ttnn.squeeze, (concat, 0))

                return g.call_function(ttnn.concat, (tensors_to_concat, dim))

            if node.target == torch.ops.aten.argmax.default:
                tensor, *dim = args
                rank = len(tensor.meta["val"].size())
                tt_kwargs = {}
                if dim:
                    dim = (dim[0] + rank) % rank
                    tt_kwargs["dim"] = dim

                return g.call_function(ttnn.argmax, args=(tensor,), kwargs=tt_kwargs)

            if node.target == torch.ops.aten.stack.default:
                tensors, *dim = args
                dim = dim[0] if dim else 0
                output_shape = list(node.meta["val"].size())
                return g.call_function(target_wrappers.stack, (tensors, dim, output_shape))

            if node.target == torch.ops.aten.roll.default:
                tensor, shifts, dims = args
                input_shape = list(tensor.meta["val"].size())
                return g.call_function(target_wrappers.roll, (tensor, input_shape, shifts, dims))

            if node.target == torch.ops.aten.bitwise_not.default:
                input_type = get_dtype(args[0])
                if input_type == torch.bool:
                    return g.call_function(ttnn.eq, args=(args[0], 0))

                # ttnn.bitwise_not only supports int32
                cast_to_int32 = g.call_function(ttnn.typecast, args=(args[0], TtnnInt32()))
                return g.call_function(ttnn.bitwise_not, args=(cast_to_int32,))

            if node.target == torch.ops.aten.all.default:
                input_shape = get_shape(gm, args[0])
                ttnn_all = g.call_function(target_wrappers.all, args=(args[0], input_shape.numel()))
                return g.call_function(torch.ops.aten.squeeze.default, args=(ttnn_all,))

            if node.target == torch.ops.aten.copy.default:
                # Equivalent to in-place torch.copy_.
                return args[1]

            if node.target == torch.ops.aten.empty.memory_format:
                # raise RuntimeError(f"{str(kwargs)}, {str(args)}, {str(type(args[0]))}")
                dtype_mapping = {
                    torch.float32: TtnnBfloat16(),
                    torch.float16: TtnnBfloat16(),
                    torch.int32: TtnnInt32(),
                }
                dtype = dtype_mapping.get(kwargs["dtype"], TtnnUint32())
                new_kwargs = {
                    "dtype": dtype,
                    "layout": TtnnTileLayout(),
                    "device": TtnnDevice(),
                }
                return g.call_function(ttnn.empty, args=(args[0],), kwargs=new_kwargs)
            if node.target == torch.ops.aten._scaled_dot_product_flash_attention.default:

                def pad_qkv_ttnn(q, k, v, scale=None, align_by=ttnn.TILE_SIZE):
                    """
                    Pads the last dimension of Q, K, V tensors to `tile_size`
                    and rescales Q so that the scaled-dot-product attention
                    is numerically identical to the unpadded case.
                    """
                    # Extract shape from metadata
                    q_shape = list(q.meta["val"].shape)
                    d = q_shape[-1]
                    pad = (-d) % align_by  # 0 – 31

                    padded_shape = q_shape.copy()
                    padded_shape[-1] = d + pad

                    if pad:
                        ttnn_pad = [(0, pad)]

                        # metadata is broken because torch fx expects sdpa to return a tuple
                        torch_pad = tuple(x for pair in ttnn_pad for x in pair)
                        meta_val = torch.nn.functional.pad(g._get_val(q), torch_pad, value=0)

                        # 1) zero‑pad along head_dim
                        q = g.call_function(ttnn.pad, args=(q, ttnn_pad, 0))
                        k = g.call_function(ttnn.pad, args=(k, ttnn_pad, 0))
                        v = g.call_function(ttnn.pad, args=(v, ttnn_pad, 0))

                        q.meta["val"] = meta_val
                        k.meta["val"] = meta_val
                        v.meta["val"] = meta_val

                        # 2) rescale Q so that Q*K^T / sqrt(d') == Q_p*K_p^T / sqrt(d)
                        if scale is None:
                            calc_scale = math.sqrt((d + pad) / d)
                            q = g.call_function(ttnn.multiply, args=(q, calc_scale))

                    return q, k, v, d

                def select(dropout_p=0.0, is_causal=False):
                    # TODO(jdh8): Add support for training mode
                    if dropout_p > 0.0 or not is_getitem_0_only_user(node):
                        return None

                    # Pad last dimension of Q, K, V to tile size
                    q, k, v = args[:3]
                    q_padded, k_padded, v_padded, d = pad_qkv_ttnn(q, k, v, scale=kwargs.get("scale", None))

                    # TODO: Those configs can be further optimized based on input shape to get
                    # best performance/accuracy tradeoff
                    default_q_chunk_size = 32  # <- The bigger the better accuracy but slower
                    default_k_chunk_size = 32

                    compute_config_params = {
                        "math_fidelity": ttnn.MathFidelity.HiFi2,
                        "math_approx_mode": True,
                        "fp32_dest_acc_en": False,
                        "packer_l1_acc": False,
                    }
                    if ttnn.device.is_wormhole_b0(device):
                        compute_kernel_config = get_emplace_custom_object_in_graph(
                            ttnn.WormholeComputeKernelConfig, **compute_config_params
                        )
                    elif ttnn.device.is_blackhole(device):
                        compute_kernel_config = get_emplace_custom_object_in_graph(
                            ttnn.BlackholeComputeKernelConfig, **compute_config_params
                        )
                    else:
                        raise RuntimeError(f"Unsupported device for {device.arch()} compute kernel config")
                    program_config = get_emplace_custom_object_in_graph(
                        ttnn.SDPAProgramConfig,
                        compute_with_storage_grid_size=device.compute_with_storage_grid_size(),
                        q_chunk_size=default_q_chunk_size,
                        k_chunk_size=default_k_chunk_size,
                        exp_approx_mode=False,
                    )
                    res_node = g.call_function(
                        ttnn.transformer.scaled_dot_product_attention,
                        args=(q_padded, k_padded, v_padded),
                        kwargs={
                            "is_causal": is_causal,
                            "scale": kwargs.get("scale", None),
                            "compute_kernel_config": compute_kernel_config,
                            "program_config": program_config,
                        },
                    )

                    # If padding was applied, slice the result back to original dimension
                    pad = (-d) % 32
                    if pad:
                        output_shape = list(res_node.meta["val"][0].shape)
                        slice_start = [0] * len(output_shape)
                        slice_end = output_shape.copy()
                        slice_end[-1] = d  # Set last dimension back to original size
                        res_node = g.call_function(ttnn.slice, (res_node, slice_start, slice_end))

                    # torch.ops.aten._scaled_dot_product_flash_attention.default return a tuple of values and inserts a
                    # getitem(ret, 0) after it. ttnn.transformer.scaled_dot_product_attention only returns one value.
                    if (val := res_node.meta.get("val", None)) is not None:
                        res_node.meta["val"] = val[0]

                    return res_node

                return select(*args[3:])

            # Removes getitem after ttnn.transformer.scaled_dot_product_attention
            # Related to https://github.com/tenstorrent/tt-metal/issues/16021
            if node.target == operator.getitem and isinstance(args[1], int) and args[1] == 0:
                if args[0].target == ttnn.transformer.scaled_dot_product_attention or (
                    args[0].target == ttnn.slice
                    and args[0].args[0].target == ttnn.transformer.scaled_dot_product_attention
                ):
                    return args[0]

            # PEP 8 suggests this explicit statement
            return None

        modified = False
        with g.inserting_before(node):
            new_node = rewrite_node(node)
            if new_node is not None:
                modified = True
                node.replace_all_uses_with(
                    new_node,
                    delete_user_cb=lambda node: node != new_node,
                )

    gm = GraphCleanup(gm)
    return gm, modified


def decompose_aten_to_aten_ops(gm: torch.fx.GraphModule, g: GraphWrapper, node):
    args = node.args
    kwargs = node.kwargs
    if node.target == torch.ops.aten.full_like.default:
        target_shape = args[0].meta["val"].size()
        return g.call_function(torch.ops.aten.full.default, args=(target_shape, *args[1:]), kwargs=kwargs)

    if node.target == torch.ops.aten.new_full.default:
        target_shape = args[1]
        new_kwargs = dict(kwargs)
        # Use the inferred output dtype so we don't need to figure out the dtype by ourselves
        new_kwargs["dtype"] = node.meta["val"].dtype
        return g.call_function(torch.ops.aten.full.default, args=(target_shape, *args[2:]), kwargs=new_kwargs)

    if node.target == torch.ops.aten.new_zeros.default:
        target_shape = args[1]
        new_kwargs = dict(kwargs)
        # Use the inferred output dtype so we don't need to figure out the dtype by ourselves
        new_kwargs["dtype"] = node.meta["val"].dtype
        return g.call_function(torch.ops.aten.zeros.default, args=(target_shape, *args[2:]), kwargs=new_kwargs)

    if node.target == torch.ops.aten._log_softmax.default:
        dim, half_to_float = get_arg(node, 1, "dim"), get_arg(node, 2, "half_to_float")
        softmax = g.call_function(torch.ops.aten._softmax.default, args=(args[0], dim, half_to_float))
        log = g.call_function(torch.ops.aten.log.default, args=(softmax,))
        return log

    if node.target == torch.ops.aten.clamp_min.default:
        return g.call_function(torch.ops.aten.clamp.default, args=(args[0], args[1], None))

    if node.target == torch.ops.aten.select.int:
        input_shape = get_shape(gm, args[0])
        output_shape = get_shape(gm, node)
        if input_shape.numel() == output_shape.numel() and len(output_shape) == 0:
            return g.call_function(torch.ops.aten.squeeze.dim, args=(args[0], 0))
        return None

    if node.target == torch.ops.aten.sum.default:
        input_shape = get_shape(gm, args[0])
        output_shape = get_shape(gm, node)
        if input_shape.numel() == 1:
            return g.call_function(torch.ops.aten.squeeze.default, args=(args[0],))
        return None

    if node.target in [torch.ops.aten.index.Tensor, torch.ops.aten._unsafe_index.Tensor]:
        input_shape = get_shape(gm, args[0])
        indices = get_arg(node, 1, "indices")
        if len(input_shape) == 2 and len(indices) == 1 and indices[0] is not None:
            index_shape = get_shape(gm, indices[0])
            # magic number, 38000 can pass, 39000 can pass, but 38809 will hang
            # and if device is just ttnn.open_device(device=0), then it can pass
            # see issue #685
            if index_shape == torch.Size([38809]):
                return None
            return g.call_function(torch.ops.aten.embedding.default, args=(args[0], indices[0]))
        return None

    if node.target == torch.ops.aten.index_select.default:
        dim = get_arg(node, 1, "dim")
        indices = get_arg(node, 2, "indices")
        new_indices = [None] * dim + [indices]
        return g.call_function(torch.ops.aten.index.Tensor, args=(args[0], new_indices))
    return None


# TODO(jerrysky3): Refactor ReplaceMoreTtManually with rewrite_graph
def rewrite_graph(gm: torch.fx.GraphModule, rewrite_node_fn) -> torch.fx.GraphModule:
    nodes = list(gm.graph.nodes)
    modified = False
    for node in nodes:
        if not can_lowering_to_ttnn(node):
            continue
        g = GraphWrapper(gm, node)
        with g.inserting_before(node):
            new_node = rewrite_node_fn(gm, g, node)
            if new_node is not None:
                modified = True
                node.replace_all_uses_with(
                    new_node,
                    delete_user_cb=lambda node: node != new_node,
                )

    gm = GraphCleanup(gm)
    return gm, modified


class ToTtPass(PassBase):
    """Pass to convert aten ops to ttnn ops.

    This pass is currently multi-device aware since it rewrites the shard / replicate / concat operations inserted by the MultiDevicePass. Some aten to ttnn conversions are performed with the torch.fx.Transformer, while others are manually rewritten.

    :param device: The device on which the workflow will execute. Can be a MeshDevice or Device.
    :param use_less_ttnn_op_types: Whether to use less ttnn op types (maybe unused).
    """

    def __init__(self, device, use_less_ttnn_op_types):
        self.device = device
        self.use_less_ttnn_op_types = use_less_ttnn_op_types

    def call(self, gm: torch.fx.GraphModule):
        # Decompose some aten ops to simpler aten ops
        max_try = 10
        cnt = 0
        while True:
            cnt += 1
            gm, modified = rewrite_graph(gm, decompose_aten_to_aten_ops)
            if not modified:
                break
            if cnt == max_try:
                raise RuntimeError("Failed to decompose aten ops to simpler aten ops")

        # Replace more patterns with torch.fx.Transformer
        gm = ReplaceMoreTt(gm, self.device, self.use_less_ttnn_op_types).transform()

        # Replace patterns manually
        max_try = 10
        cnt = 0
        while True:
            cnt += 1
            gm, modified = ReplaceMoreTtManually(gm, self.device, self.use_less_ttnn_op_types)
            if not modified:
                break
            if cnt == max_try:
                raise RuntimeError("Failed to decompose aten ops to simpler aten ops")

        return PassResult(gm, True)

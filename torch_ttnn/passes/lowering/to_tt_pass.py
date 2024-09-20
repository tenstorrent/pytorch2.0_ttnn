import torch
import ttnn
from torch_ttnn.utils import (
    GraphCleanup,
    TtnnBfloat16,
    TtnnDevice,
    TtnnTileLayout,
    TtnnDramMemoryConfig,
    TtnnRowMajorLayout,
    HasValidPageSize,
)
import numpy as np
from typing import Tuple
import torch_ttnn.metrics as metrics

from torch.fx.passes.infra.pass_base import PassBase, PassResult
import torch.fx.traceback as fx_traceback
from . import target_wrappers

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
    torch.ops.aten.floor.default,
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


class ReplaceMoreTt(torch.fx.Transformer):
    def __init__(self, module, device):
        super().__init__(module)
        self._input_node_meta = {node.name: node.meta for node in self.module.graph.nodes if node.op == "placeholder"}
        self.device = device

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

        if are_args_from_int_output_ops(args) or is_target_incompatible_with_grayskull(target, self.device):
            return self.call_function_prop_meta(target, args, kwargs)

        ############################################################
        # Tensor creation
        ############################################################
        if target == torch.ops.aten.zeros_like.default:
            return self.call_function_prop_meta(ttnn.zeros_like, args, {})

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
        if target == torch.ops.aten.abs.default:
            return self.call_function_prop_meta(ttnn.abs, args, kwargs)

        if target == torch.ops.aten.acos.default:
            return self.call_function_prop_meta(ttnn.acos, args, kwargs)

        if target == torch.ops.aten.acosh.default:
            return self.call_function_prop_meta(ttnn.acosh, args, kwargs)

        if target == torch.ops.aten.asin.default:
            return self.call_function_prop_meta(ttnn.asin, args, kwargs)

        if target == torch.ops.aten.asinh.default:
            return self.call_function_prop_meta(ttnn.asinh, args, kwargs)

        if target == torch.ops.aten.atan.default:
            return self.call_function_prop_meta(ttnn.atan, args, kwargs)

        if target == torch.ops.aten.atanh.default:
            return self.call_function_prop_meta(ttnn.atanh, args, kwargs)

        if target == torch.ops.aten.clamp.default:
            return self.call_function_prop_meta(ttnn.clip, args, kwargs)

        if target == torch.ops.aten.cos.default:
            return self.call_function_prop_meta(ttnn.cos, args, kwargs)

        if target == torch.ops.aten.cosh.default:
            return self.call_function_prop_meta(ttnn.cosh, args, kwargs)

        if target == torch.ops.aten.erf.default:
            return self.call_function_prop_meta(ttnn.erf, args, kwargs)

        if target == torch.ops.aten.exp.default:
            return self.call_function_prop_meta(ttnn.exp, args, kwargs)

        if target == torch.ops.aten.expm1.default:
            return self.call_function_prop_meta(ttnn.expm1, args, kwargs)

        if target == torch.ops.aten.floor.default:
            return self.call_function_prop_meta(ttnn.floor, args, kwargs)

        if target == torch.ops.aten.gelu.default:
            return self.call_function_prop_meta(ttnn.gelu, args, kwargs)

        if target == torch.ops.aten.hardtanh.default and args[1] == -1.0 and args[2] == 1.0:
            return self.call_function_prop_meta(ttnn.clip, args, kwargs)

        if target == torch.ops.aten.isinf.default:
            return self.call_function_prop_meta(ttnn.isinf, args, kwargs)

        if target == torch.ops.aten.isnan.default:
            return self.call_function_prop_meta(ttnn.isnan, args, kwargs)

        if target == torch.ops.aten.log.default:
            return self.call_function_prop_meta(ttnn.log, args, kwargs)

        if target == torch.ops.aten.log10.default:
            return self.call_function_prop_meta(ttnn.log10, args, kwargs)

        if target == torch.ops.aten.log1p.default:
            return self.call_function_prop_meta(ttnn.log1p, args, kwargs)

        if target == torch.ops.aten.log2.default:
            return self.call_function_prop_meta(ttnn.log2, args, kwargs)

        if target == torch.ops.aten.logical_not.default:
            return self.call_function_prop_meta(ttnn.logical_not, args, kwargs)

        if target == torch.ops.aten.neg.default:
            return self.call_function_prop_meta(ttnn.neg, args, kwargs)

        if target == torch.ops.aten.reciprocal.default:
            return self.call_function_prop_meta(ttnn.reciprocal, args, kwargs)

        if target == torch.ops.aten.relu.default:
            return self.call_function_prop_meta(ttnn.relu, args, kwargs)

        if target == torch.ops.aten.remainder.Scalar:
            return self.call_function_prop_meta(ttnn.remainder, args, kwargs)

        if target == torch.ops.aten.rsqrt.default:
            return self.call_function_prop_meta(ttnn.rsqrt, args, kwargs)

        if target == torch.ops.aten.sigmoid.default:
            return self.call_function_prop_meta(ttnn.sigmoid, args, kwargs)

        if target == torch.ops.aten.sign.default:
            return self.call_function_prop_meta(ttnn.sign, args, kwargs)

        if target == torch.ops.aten.sin.default:
            return self.call_function_prop_meta(ttnn.sin, args, kwargs)

        if target == torch.ops.aten.sinh.default:
            return self.call_function_prop_meta(ttnn.sinh, args, kwargs)

        if target == torch.ops.aten.silu.default:
            return self.call_function_prop_meta(ttnn.silu, args, kwargs)

        if target == torch.ops.aten._softmax.default:
            return self.call_function_prop_meta(ttnn.softmax, args[:2], kwargs)

        if target == torch.ops.aten.sqrt.default:
            return self.call_function_prop_meta(ttnn.sqrt, args, kwargs)

        if target == torch.ops.aten.tan.default:
            return self.call_function_prop_meta(ttnn.tan, args, kwargs)

        if target == torch.ops.aten.tanh.default:
            return self.call_function_prop_meta(ttnn.tanh, args, kwargs)

        if target == torch.ops.aten.tril.default:
            return self.call_function_prop_meta(ttnn.tril, args, kwargs)

        ############################################################
        # Pointwise binary
        ############################################################
        if target == torch.ops.aten.add.Tensor:
            return self.call_function_prop_meta(ttnn.add, args, kwargs)

        if target == torch.ops.aten.atan2.default:
            return self.call_function_prop_meta(ttnn.atan2, args, kwargs)

        if target == torch.ops.aten.leaky_relu.default:
            if len(args) < 2:
                args = (args[0], 0.01)
            return self.call_function_prop_meta(ttnn.leaky_relu, args, kwargs)

        if target == torch.ops.aten.maximum.default:
            return self.call_function_prop_meta(ttnn.maximum, args, kwargs)

        if target == torch.ops.aten.minimum.default:
            return self.call_function_prop_meta(ttnn.minimum, args, kwargs)

        if target == torch.ops.aten.mul.Tensor:
            return self.call_function_prop_meta(ttnn.mul, args, kwargs)

        if target == torch.ops.aten.pow.Tensor_Scalar:
            return self.call_function_prop_meta(ttnn.pow, args, kwargs)

        if target == torch.ops.aten.rsub.Tensor:
            # TODO(kevinwuMCW): handle alpha parameter if exists
            return self.call_function_prop_meta(ttnn.sub, (args[1], args[0]), kwargs)

        if target == torch.ops.aten.sub.Tensor:
            return self.call_function_prop_meta(ttnn.sub, args, kwargs)

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
            # change dim parameter to tuple
            new_args = list(args)
            new_args[1] = tuple(args[1]) if len(args[1]) > 1 else args[1][0]
            return self.call_function_prop_meta(ttnn.mean, tuple(new_args), kwargs)

        if target == torch.ops.aten.min.default:
            return self.call_function_prop_meta(ttnn.min, args, kwargs)

        ############################################################
        # Data movement
        ############################################################
        if target == torch.ops.aten.permute.default:
            return self.call_function_prop_meta(ttnn.permute, args, kwargs)

        ############################################################
        # Other ops
        ############################################################
        if target == torch.ops.aten._adaptive_avg_pool2d.default:
            # assumes output size is (1, 1)
            return self.call_function_prop_meta(ttnn.global_avg_pool2d, (args[0],), kwargs)

        if target == torch.ops.aten.squeeze.dim:
            # NOTE(kevinwuTT): ttnn.squeeze only supports dim 0 currently
            if args[1] == 0:
                return self.call_function_prop_meta(ttnn.squeeze, args, kwargs)
            return self.call_function_prop_meta(target, args, kwargs)

        return self.call_function_prop_meta(target, args, kwargs)


def torch_dtype_to_ttnn_dtype(dtype: torch.dtype):
    # Add newly supported dtypes here:
    dtype_map = {
        torch.float32: TtnnBfloat16(),
        torch.bfloat16: TtnnBfloat16(),
    }
    if dtype in dtype_map:
        return dtype_map.get(dtype)
    else:
        raise RuntimeError(f"Missing conversion from torch.dtype: {dtype} to Ttnn dtype.")


# override some functions from torch.fx.graph.Graph
class GraphWrapper:
    def __init__(self, node):
        self.g = node.graph
        self.node = node

    def call_function(self, target, args=(), kwargs={}):
        new_node = self.g.call_function(target, args, kwargs)
        new_node.meta = self.node.meta
        if hasattr(self.node.target, "_schema"):
            new_node.meta["original_input_variations"] = metrics.collect_input_variation_from_node(self.node)
        if target == ttnn.layer_norm:
            new_node.meta["val"] = new_node.meta["val"][0]
        return new_node

    def inserting_before(self, node):
        return self.g.inserting_before(node)


def ReplaceMoreTtManually(gm: torch.fx.GraphModule) -> torch.fx.GraphModule:
    nodes = list(gm.graph.nodes)
    for node in nodes:
        g = GraphWrapper(node)

        def rewrite_node(node):
            args = node.args
            kwargs = node.kwargs

            if node.target == torch.ops.aten.clone.default:
                arg_metadata = node.meta["val"]
                ttnn_dtype = torch_dtype_to_ttnn_dtype(arg_metadata.dtype)
                # Add additional logic to choose the appropriate memory_config type: DRAM or L1
                return g.call_function(target_wrappers.clone, args=(args[0],))

            if node.target == torch.ops.aten.native_layer_norm.default:
                new_node = g.call_function(
                    ttnn.layer_norm,
                    args=(args[0],),
                    kwargs={"epsilon": args[4], "weight": args[2], "bias": args[3]},
                )
                node.replace_all_uses_with(new_node, delete_user_cb=lambda node: node != new_node)
                node_users = list(new_node.users.keys())
                for node_user in node_users:
                    node_user.replace_all_uses_with(new_node)
                return None

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

            if node.target in relational_scalar_ops:
                # NOTE(kevinwuTT): ttnn.eq shows error if passing a literal scalar as an argument.
                # Instead, fill a tensor with the same size as args[0] with the scalar value using ttnn.full
                # NOTE(jdh8): after broadcasting support is complete, we should fill a (1,) tensor
                arg_metadata = node.meta["val"]
                if HasValidPageSize(arg_metadata.size(), strict=True):
                    new_kwargs = {
                        "fill_value": args[1],
                        "device": TtnnDevice(),
                        "layout": TtnnTileLayout(),
                    }
                    full_node = g.call_function(ttnn.full, args=(arg_metadata.size(),), kwargs=new_kwargs)
                    return g.call_function(
                        relational_scalar_ops[node.target],
                        args=(args[0], full_node),
                        kwargs={},
                    )
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
                # args[0] can be empty for aten.full which simply creates a scalar. Ignore conversion in this case.
                if args[0]:
                    new_kwargs = {
                        "fill_value": args[1],
                        "device": TtnnDevice(),
                        "layout": TtnnTileLayout(),
                    }
                    return g.call_function(ttnn.full, args=(tuple(args[0]),), kwargs=new_kwargs)
                # Replace op with scalar for eltwise ops
                # TODO: Generalize this to support all eltwise ops
                node_users = list(node.users.keys())
                for node_user in node_users:
                    if node_user.target == torch.ops.aten.div.Tensor:
                        node_user.update_arg(1, args[1])
                return None

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
                # TODO(kevinwuTT): Add support for ROW_MAJOR_LAYOUT
                new_kwargs = {"layout": TtnnTileLayout()}
                return g.call_function(ttnn.embedding, args=(args[1], args[0]), kwargs=new_kwargs)

            if node.target == torch.ops.aten._log_softmax.default:
                softmax_node = g.call_function(ttnn.softmax, args[:2], kwargs)
                return g.call_function(ttnn.log, (softmax_node,), kwargs)

            if node.target == torch.ops.aten.rsub.Scalar:
                # NOTE(kevinwuTT): ttnn.sub shows error if passing a literal scalar as the first argument.
                # Instead, fill a tensor with the same size as args[0] with the scalar value using ttnn.full
                node_metadata = node.meta["val"]
                shape = node_metadata.size()
                # If last dim == 1, then the follow error will appear:
                # Page size must be divisible by sizeof(uint32_t) because buffers hold uint32_t values
                if shape[-1] != 1 and HasValidPageSize(shape):
                    # NOTE(kevinwuTT): Only bfloat16 seems to work for now
                    # TODO(kevinwuTT): Use ttnn.full instead of aten
                    new_kwargs = {
                        "fill_value": args[1],
                        "device": TtnnDevice(),
                    }
                    full = g.call_function(
                        ttnn.full,
                        args=(tuple(shape),),
                        kwargs=new_kwargs,
                    )
                    to_layout = g.call_function(ttnn.to_layout, (full,), {"layout": TtnnTileLayout()})
                    return g.call_function(ttnn.sub, args=(to_layout, args[0]), kwargs={})
                return None

            if node.target == torch.ops.aten.div.Tensor:
                # ttnn.recip does not support scalars. Call an ttnn.full and pass that to ttnn.recip
                # TODO(kevinwuTT): Use a ttnn equivalent
                node_metadata = node.meta["val"]
                shape = node_metadata.size()
                # If last dim == 1, then the follow error will appear:
                # Page size must be divisible by sizeof(uint32_t) because buffers hold uint32_t values
                if shape[-1] != 1 and HasValidPageSize(shape):
                    if isinstance(args[1], float):
                        new_kwargs = {
                            "fill_value": args[1],
                            "device": TtnnDevice(),
                        }
                        full = g.call_function(
                            ttnn.full,
                            args=(tuple(shape),),
                            kwargs=new_kwargs,
                        )
                        to_layout = g.call_function(ttnn.to_layout, (full,), {"layout": TtnnTileLayout()})
                        recip = g.call_function(ttnn.reciprocal, (to_layout,), {})
                    else:
                        recip = g.call_function(ttnn.reciprocal, (args[1],), {})
                    return g.call_function(ttnn.mul, (args[0], recip), {})
                return None

            if node.target == torch.ops.aten.expand.default:
                # aten.expand and ttnn.repeat has different meaning for their `shape` argument
                # aten.expand: the desired output shape, where respective singleton dims are broadcasted
                # ttnn.repeat: the number of times to repeat a respective singleton dim
                input_tensor_shape = args[0].meta["val"].size()
                # Repeat fails if last dimension of input is 1
                if input_tensor_shape[-1] != 1:
                    output_shape = torch.Size(args[1])

                    multiplier = np.array(output_shape) // np.array(input_tensor_shape)
                    # -1 // positive non-zero number will always be -1
                    # Convert -1 to 1
                    multiplier = np.array([1 if i == -1 else i for i in multiplier])

                    if np.prod(multiplier) != 1:
                        return g.call_function(target_wrappers.repeat, args=(args[0], multiplier.tolist()))
                    return args[0]
                return None

            if node.target == torch.ops.aten.repeat.default:
                tensor, sizes = args
                shape = tensor.meta["val"].size()

                if np.prod(sizes) == 1:
                    return tensor

                # Current repeat implementation requires aligned last dim when repeating on last dim
                if sizes[-1] == 1 or shape[-1] % 16 == 0:
                    return g.call_function(target_wrappers.repeat, args)

                return None

            if node.target == torch.ops.aten.unsqueeze.default:
                output_size = node.meta["val"].size()
                output_size = list(output_size)
                if output_size[-1] == args[0].meta["val"].size()[-1]:
                    return g.call_function(ttnn.reshape, args=(args[0], output_size))
                return None

            if node.target == torch.ops.aten.transpose.int:
                dim0 = args[1]
                dim1 = args[2]
                output_size = node.meta["val"].size()
                rank = len(output_size)
                permutation = list(range(rank))
                permutation[dim0], permutation[dim1] = (
                    permutation[dim1],
                    permutation[dim0],
                )
                new_nodes = list()
                new_nodes.append(g.call_function(ttnn.permute, args=(args[0], permutation)))
                new_nodes[-1].meta["val"] = node.meta["val"]
                # strange workaround when dim 0 is 1 for rank 3
                if rank == 3 and output_size[0] == 1:
                    if output_size[1] % 32 or output_size[2] % 32:
                        new_nodes.append(
                            g.call_function(
                                ttnn.to_layout,
                                (new_nodes[-1],),
                                {"layout": TtnnRowMajorLayout()},
                            )
                        )
                    new_nodes.append(g.call_function(ttnn.reshape, args=(new_nodes[-1], output_size)))
                return new_nodes[-1]

            if node.target == torch.ops.aten.t.default:
                permutation = list()
                rank = len(node.meta["val"].size())
                assert rank >= 0 and rank <= 2, "Input tensor can only be 0D, 1D or 2D"
                if rank == 2:
                    permutation = [1, 0]
                    return g.call_function(ttnn.permute, args=(args[0], permutation))
                return None
            if node.target == torch.ops.aten.constant_pad_nd.default:
                input, pad, value = args
                input_shape = input.meta["val"].size()
                rank = len(input_shape)
                full_pad = [(0, 0)] * (rank - len(pad))
                # The order of pad from pytorch is reversed
                full_pad += [(pad[i], pad[i + 1]) for i in range(0, len(pad), 2)][::-1]
                # TODO(#192): Front padding isn't well supported so skip for now
                if rank > 4 or (not all(f == 0 for f, _ in full_pad)):
                    return None
                # Change layout to row-major for non-tile-size-aligned tensor
                if (
                    rank < 2
                    or input_shape[-1] % ttnn.TILE_SIZE != 0
                    or input_shape[-2] % ttnn.TILE_SIZE != 0
                    or full_pad[-1][1] % ttnn.TILE_SIZE != 0
                    or full_pad[-2][1] % ttnn.TILE_SIZE != 0
                ):
                    input = g.call_function(ttnn.to_layout, args=(input, TtnnRowMajorLayout()))
                return g.call_function(ttnn.pad, args=(input, full_pad, value))

            if node.target == torch.ops.aten.view.default:
                source_shape = args[0].meta["val"].size()
                out_shape = args[1]
                source_rank = len(source_shape)
                out_rank = len(out_shape)

                # Allow lowering by default
                can_reshape = True

                # Unsupported:
                # (1) -> (1, 1) or (1, 1, 1), etc
                if (source_rank == 1) and (np.prod(source_shape) == 1):
                    can_reshape = False
                elif not HasValidPageSize(source_shape):
                    can_reshape = False
                # Same as ttnn.squeeze with dim = 0
                # Supported:
                # (1, 16, 256, 256) -> (16, 256, 256)
                # (1, 256, 256) - > (256, 256)
                elif (source_rank != 1) and (out_rank == (source_rank - 1)) and (source_shape[0] == 1):
                    for i in range(0, out_rank):
                        if source_shape[i + 1] != out_shape[i]:
                            can_reshape = False
                            break

                # Same as ttnn.unsqueeze_to_4D
                # Supported:
                # (16, 256, 256) -> (1, 16, 256, 256)
                # (256, 256) -> (1, 1, 256, 256)
                elif (out_rank > 1) and (out_rank <= 4) and (source_rank > 0) and (source_rank <= 4):
                    for i in range(0, out_rank):
                        si = i + (source_rank - out_rank)
                        if si < 0:
                            if out_shape[i] != 1:
                                can_reshape = False
                                break
                        else:
                            if out_shape[i] != source_shape[si]:
                                can_reshape = False
                                break
                else:
                    can_reshape = False

                # Transform to ttnn.reshape if possible
                if can_reshape:
                    return g.call_function(ttnn.reshape, (args[0], args[1]), {})
                else:
                    # Fallback: aten.reshape is more stable if the input nodes have changed
                    return g.call_function(torch.ops.aten.reshape.default, args, kwargs)

        with g.inserting_before(node):
            new_node = rewrite_node(node)
            if new_node is not None:
                node.replace_all_uses_with(
                    new_node,
                    delete_user_cb=lambda node: node != new_node,
                )

    gm = GraphCleanup(gm)
    return gm


class ToTtPass(PassBase):
    def __init__(self, device):
        self.device = device

    def call(self, gm: torch.fx.GraphModule):
        # Replace more patterns with torch.fx.Transformer
        gm = ReplaceMoreTt(gm, self.device).transform()

        # Replace patterns manually
        gm = ReplaceMoreTtManually(gm)

        return PassResult(gm, True)

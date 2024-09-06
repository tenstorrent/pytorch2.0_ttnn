import torch
import ttnn
from torch_ttnn.utils import (
    GraphCleanup,
    TtnnBfloat16,
    TtnnDevice,
    TtnnTileLayout,
    TtnnDramMemoryConfig,
    TtnnRowMajorLayout,
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
}

# Workaround: If an arg of the model output is argmax then skip conversion
# TODO(kevinwuTT): Handle this case with ttnn ops
int_output_ops = [
    torch.ops.aten.argmax.default,
    torch.ops.aten.argmin.default,
]


def are_args_from_int_output_ops(args):
    for arg in args:
        if isinstance(arg, torch.fx.proxy.Proxy):
            if arg.node.target in int_output_ops:
                return True


def create_call_function(transformer, target, args, kwargs):
    transformer.call_function(target, args, kwargs)


class ReplaceMoreTt(torch.fx.Transformer):
    def __init__(self, module):
        super().__init__(module)
        self._input_node_meta = {node.name: node.meta for node in self.module.graph.nodes if node.op == "placeholder"}

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

        if are_args_from_int_output_ops(args):
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

        if target == torch.ops.aten.view.default:
            # aten.reshape is more stable if the input nodes have changed
            return self.call_function_prop_meta(torch.ops.aten.reshape.default, args, kwargs)

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


# Certain ops don't support certain shapes and will emit a valid_page_size error
# RuntimeError: TT_FATAL @ ../tt_metal/impl/buffers/buffer.cpp:38: valid_page_size
# For valid non-interleaved buffers page size 2048 must equal buffer size X. For interleaved-buffers page size should be divisible by buffer size
def has_valid_page_size(shape):
    assert len(shape) > 0, f"has_valid_page_size requires rank of {shape} > 0"
    return len(shape) >= 2 and ((shape[-1] > 1 and shape[-1] < 31) or (shape[-1] >= 32 and (shape[-1] % 32 == 0)))


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
        args = node.args

        new_nodes = []
        with g.inserting_before(node):
            # TODO (kevinwuTT): consolidate and simplify these statements?
            if node.target == torch.ops.aten.clone.default:
                arg_metadata = node.meta["val"]
                ttnn_dtype = torch_dtype_to_ttnn_dtype(arg_metadata.dtype)
                # Add additional logic to choose the appropriate memory_config type: DRAM or L1
                new_node = g.call_function(target_wrappers.clone, args=(args[0],))
                new_nodes.append(new_node)
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
            if node.target == torch.ops.aten.ones.default:
                new_node = g.call_function(ttnn.ones, args=args, kwargs={"device": TtnnDevice()})
                new_nodes.append(new_node)
            """
            # NOTE(kevinwuTT): aten.arange.default starts with 0 which is unsupported by ttnn.arange at the moment
            if node.target == torch.ops.aten.arange.default:
                # start = 0, step = 1
                new_args = (0,)
                new_kwargs = {"end": args[0], "step": 1, "device": TtnnDevice()}
                new_node = g.call_function(ttnn.arange, args=new_args, kwargs=new_kwargs)
                new_nodes.append(new_node)
            """
            if node.target == torch.ops.aten.arange.start:
                # NOTE(kevinwuTT): ttnn.arange does not support starting values smaller than 2 currently
                if args[0] >= 2:
                    # step = 1
                    new_args = (args[0],)
                    new_kwargs = {"end": args[1], "step": 1, "device": TtnnDevice()}
                    new_node = g.call_function(ttnn.arange, args=new_args, kwargs=new_kwargs)
                    new_nodes.append(new_node)
            if node.target == torch.ops.aten.arange.start_step:
                # NOTE(kevinwuTT): ttnn.arange does not support starting values smaller than 2 currently
                if args[0] >= 2:
                    new_args = (args[0],)
                    new_kwargs = {
                        "end": args[1],
                        "step": args[2],
                        "device": TtnnDevice(),
                    }
                    new_node = g.call_function(ttnn.arange, args=new_args, kwargs=new_kwargs)
                    new_nodes.append(new_node)
            if node.target in relational_scalar_ops:
                # NOTE(kevinwuTT): ttnn.eq shows error if passing a literal scalar as an argument.
                # Instead, fill a tensor with the same size as args[0] with the scalar value using ttnn.full
                arg_metadata = node.meta["val"]
                if has_valid_page_size(arg_metadata.size()):
                    new_kwargs = {
                        "fill_value": args[1],
                        "device": TtnnDevice(),
                        "layout": TtnnTileLayout(),
                    }
                    full_node = g.call_function(ttnn.full, args=(arg_metadata.size(),), kwargs=new_kwargs)
                    new_node = g.call_function(
                        relational_scalar_ops[node.target],
                        args=(args[0], full_node),
                        kwargs={},
                    )
                    new_nodes.append(new_node)
            if node.target == torch.ops.aten.eq.Tensor:
                # Combine this with relational_scalar_ops
                if np.prod(args[1].meta["val"].size()) != 1:
                    new_node = g.call_function(
                        ttnn.eq,
                        args=args,
                        kwargs={},
                    )
                    new_nodes.append(new_node)
            if node.target == torch.ops.aten.full.default:
                # args[0] can be empty for aten.full which simply creates a scalar. Ignore conversion in this case.
                if args[0]:
                    new_kwargs = {
                        "fill_value": args[1],
                        "device": TtnnDevice(),
                        "layout": TtnnTileLayout(),
                    }
                    new_node = g.call_function(ttnn.full, args=(tuple(args[0]),), kwargs=new_kwargs)
                    new_nodes.append(new_node)
                else:
                    # Replace op with scalar for eltwise ops
                    # TODO: Generalize this to support all eltwise ops
                    node_users = list(node.users.keys())
                    for node_user in node_users:
                        if node_user.target == torch.ops.aten.div.Tensor:
                            node_user.update_arg(1, args[1])
            if node.target == torch.ops.aten.baddbmm.default:
                kwargs = node.kwargs
                # out = beta * input + alpha * (batch1 @ batch2)
                # if beta is 0, input is ignored, and nan and inf in it will not be propogated
                new_node = g.call_function(ttnn.matmul, args=(args[1], args[2]))
                if "alpha" in kwargs:
                    new_node = g.call_function(ttnn.multiply, args=(new_node, kwargs["alpha"]))
                if "beta" in kwargs:
                    if kwargs["beta"] != 0:
                        beta_node = g.call_function(ttnn.multiply, args=(args[0], kwargs["beta"]))
                        new_node = g.call_function(ttnn.add, args=(beta_node, new_node))
                else:
                    new_node = g.call_function(ttnn.add, args=(args[0], new_node))
                new_nodes.append(new_node)
            if node.target == torch.ops.aten.embedding.default:
                # TODO(kevinwuTT): Add support for ROW_MAJOR_LAYOUT
                new_kwargs = {"layout": TtnnTileLayout()}
                new_node = g.call_function(ttnn.embedding, args=(args[1], args[0]), kwargs=new_kwargs)
                new_nodes.append(new_node)
            if node.target == torch.ops.aten._log_softmax.default:
                softmax_node = g.call_function(ttnn.softmax, args[:2], node.kwargs)
                new_node = g.call_function(ttnn.log, (softmax_node,), node.kwargs)
                new_nodes.append(new_node)
            if node.target == torch.ops.aten.rsub.Scalar:
                # NOTE(kevinwuTT): ttnn.sub shows error if passing a literal scalar as the first argument.
                # Instead, fill a tensor with the same size as args[0] with the scalar value using ttnn.full
                node_metadata = node.meta["val"]
                shape = node_metadata.size()
                # If last dim == 1, then the follow error will appear:
                # Page size must be divisible by sizeof(uint32_t) because buffers hold uint32_t values
                if shape[-1] != 1 and has_valid_page_size(shape):
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
                    new_node = g.call_function(ttnn.sub, args=(to_layout, args[0]), kwargs={})
                    new_nodes.append(new_node)
            if node.target == torch.ops.aten.div.Tensor:
                # ttnn.recip does not support scalars. Call an ttnn.full and pass that to ttnn.recip
                # TODO(kevinwuTT): Use a ttnn equivalent
                node_metadata = node.meta["val"]
                shape = node_metadata.size()
                # If last dim == 1, then the follow error will appear:
                # Page size must be divisible by sizeof(uint32_t) because buffers hold uint32_t values
                if shape[-1] != 1 and has_valid_page_size(shape):
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
                    new_node = g.call_function(ttnn.mul, (args[0], recip), {})
                    new_nodes.append(new_node)
            if node.target == torch.ops.aten._to_copy.default:
                kwargs = node.kwargs
                if kwargs["dtype"] == torch.float32:
                    new_kwargs = {"dtype": torch.bfloat16}
                    new_node = g.call_function(torch.ops.aten._to_copy.default, args, new_kwargs)
                    new_nodes.append(new_node)
                """
                # NOTE(kevinwuTT): aten._to_copy is used to cast dtypes. Should combine this with other ops.
                ttnn_dtype = torch_dtype_to_ttnn_dtype(kwargs["dtype"])
                # Add additional logic to choose the appropriate memory_config type: DRAM or L1
                new_kwargs = {
                    "dtype": ttnn_dtype,
                    "layout": TtnnTileLayout(),
                    "device": TtnnDevice(),
                    "memory_config": TtnnDramMemoryConfig(),
                }
                new_node = g.call_function(ttnn.as_tensor, args, new_kwargs)
                new_nodes.append(new_node)
                """
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
                        new_node = g.call_function(target_wrappers.repeat, args=(args[0], multiplier.tolist()))
                        new_nodes.append(new_node)
                    else:
                        node.replace_all_uses_with(
                            args[0],
                            delete_user_cb=lambda node: node != args[0],
                        )
            if node.target == torch.ops.aten.unsqueeze.default:
                output_size = node.meta["val"].size()
                output_size = list(output_size)
                if output_size[-1] == args[0].meta["val"].size()[-1]:
                    new_node = g.call_function(ttnn.reshape, args=(args[0], output_size))
                    new_nodes.append(new_node)
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

                node.replace_all_uses_with(
                    new_nodes[-1],
                    delete_user_cb=lambda node: node != new_nodes[-1],
                )
            if node.target == torch.ops.aten.t.default:
                permutation = list()
                rank = len(node.meta["val"].size())
                assert rank >= 0 and rank <= 2, "Input tensor can only be 0D, 1D or 2D"
                if rank == 2:
                    permutation = [1, 0]
                    new_node = g.call_function(ttnn.permute, args=(args[0], permutation))
                    new_nodes.append(new_node)
            elif node.target == torch.ops.aten.select.int:
                tensor, dim, index = args
                starts = np.array((0,) * len(tensor.meta["val"].size()))
                starts[dim] = index
                starts = [*starts]
                new_node = g.call_function(ttnn.slice, args=(tensor, starts, starts))
                new_node = g.call_function(ttnn.squeeze, args=(new_node, 0))
                new_nodes.append(new_node)

            if new_nodes:
                node.replace_all_uses_with(
                    new_nodes[-1],
                    delete_user_cb=lambda node: node != new_nodes[-1],
                )

    gm = GraphCleanup(gm)
    return gm


class ToTtPass(PassBase):
    def call(self, gm: torch.fx.GraphModule):
        # Replace more patterns with torch.fx.Transformer
        gm = ReplaceMoreTt(gm).transform()

        # Replace patterns manually
        gm = ReplaceMoreTtManually(gm)

        return PassResult(gm, True)

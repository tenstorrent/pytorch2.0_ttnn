import torch
import ttnn
import math
from torch._subclasses.fake_tensor import unset_fake_temporarily
from torch_ttnn.utils import (
    GraphCleanup,
    HasValidPageSize,
    TtnnBfloat16,
    TtnnDevice,
    TtnnL1MemoryConfig,
    TtnnRowMajorLayout,
    TtnnTileLayout,
    get_shape,
)
import numpy as np
import torch_ttnn.metrics as metrics

from torch.fx.passes.infra.pass_base import PassBase, PassResult
import torch.fx.traceback as fx_traceback
from . import target_wrappers
from .to_tt_guard import can_lowering_to_ttnn

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


# Workaround for issue https://github.com/tenstorrent/tt-metal/issues/11191
def workaround_permute_3d_first_out_dim_is_one(g, new_nodes, rank, output_size):
    if rank == 3 and output_size[0] == 1:
        new_nodes.append(g.call_function(ttnn.reshape, args=(new_nodes[-1], output_size)))
    return new_nodes


def is_getitem_0_only_user(node):
    return all(
        user.op == "call_function" and user.target.__name__ == "getitem" and user.args[1] == 0
        for user in node.users.keys()
    )


def insert_nchw_to_nhwc(g, input_tensor):
    return g.call_function(ttnn.permute, (input_tensor, (0, 2, 3, 1)))


def insert_sharded_nhwc_to_nchw(g, output_tensor, output_shape):
    batch_size, out_c, out_h, out_w = output_shape
    output_tensor = g.call_function(ttnn.sharded_to_interleaved, (output_tensor, TtnnL1MemoryConfig()))
    output_tensor = g.call_function(ttnn.reshape, (output_tensor, (batch_size, out_h, out_w, out_c)))
    return g.call_function(ttnn.permute, (output_tensor, (0, 3, 1, 2)))


class ReplaceMoreTt(torch.fx.Transformer):
    def __init__(self, module, device, use_less_ttnn_op_types):
        super().__init__(module)
        self._input_node_meta = {node.name: node.meta for node in self.module.graph.nodes if node.op == "placeholder"}
        self.device = device
        self.use_less_ttnn_op_types = use_less_ttnn_op_types

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
            # aten.clamp args are positional but ttnn.clip uses kw args
            new_kwargs = map_args_to_kwargs(args, ((1, "min"), (2, "max")), default_none=True)
            new_args = (args[0],)
            return self.call_function_prop_meta(ttnn.clip, new_args, new_kwargs)

        if target == torch.ops.aten.cos.default:
            return self.call_function_prop_meta(ttnn.cos, args, kwargs)

        if target == torch.ops.aten.cosh.default:
            return self.call_function_prop_meta(ttnn.cosh, args, kwargs)

        if target == torch.ops.aten.elu.default:
            return self.call_function_prop_meta(ttnn.elu, args, kwargs)

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

        if target == torch.ops.aten.hardsigmoid.default:
            return self.call_function_prop_meta(ttnn.hardsigmoid, args, kwargs)

        if target == torch.ops.aten.hardswish.default:
            return self.call_function_prop_meta(ttnn.hardswish, args, kwargs)

        if target == torch.ops.aten.hardtanh.default:
            new_kwargs = map_args_to_kwargs(args, ((1, "min_val"), (2, "max_val")), default_none=True)
            new_args = (args[0],)
            return self.call_function_prop_meta(ttnn.hardtanh, new_args, new_kwargs)

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
            kwargs = {
                "numeric_stable": True,
                **kwargs,
            }
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
        if target in relational_scalar_ops:
            return self.call_function_prop_meta(relational_scalar_ops[target], args, kwargs)

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

        if target == torch.ops.aten.pow.Tensor_Scalar:
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
            new_args = []
            new_args.append(args[0])
            # change dim parameter to tuple
            new_args.append(tuple(args[1]) if len(args[1]) > 1 else args[1][0])
            keep_dim = False
            if len(args) > 2:
                keep_dim = args[2]
            elif "keepdim" in kwargs:
                keep_dim = kwargs["keepdim"]
            if keep_dim:
                return self.call_function_prop_meta(ttnn.mean, tuple(new_args), {})
            # ttnn.mean does not support keep_dim==False, need reshape to remove dim
            mean_shape = list(fx_traceback.get_current_meta()["val"].shape)
            mean = self.call_function_prop_meta(ttnn.mean, tuple(new_args), {})
            return self.call_function_prop_meta(ttnn.reshape, (mean, mean_shape))

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


def ReplaceMoreTtManually(gm: torch.fx.GraphModule, use_less_ttnn_op_types: bool) -> torch.fx.GraphModule:
    nodes = list(gm.graph.nodes)
    for node in nodes:
        if not can_lowering_to_ttnn(node):
            continue
        g = GraphWrapper(node)

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
                shapes = get_shape(args[0]), get_shape(args[1])

                if any(not s for s in shapes):
                    return None

                if max(map(len, shapes)) > 4 and shapes[0][-3:-2] != shapes[1][-3:-2]:
                    return None

                return g.call_function(fn, args)

            if node.target == torch.ops.aten.add.Tensor:
                return lower_binary_eltwise(ttnn.add, args)

            if node.target == torch.ops.aten.mul.Tensor:
                return lower_binary_eltwise(ttnn.mul, args)

            if node.target == torch.ops.aten.sub.Tensor:
                return lower_binary_eltwise(ttnn.sub, args)

            if node.target == torch.ops.aten.clone.default:
                arg_metadata = node.meta["val"]
                try:
                    ttnn_dtype = torch_dtype_to_ttnn_dtype(arg_metadata.dtype)
                except:
                    return None
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
                tiled = args[1].meta.get("val")
                tiled = False if tiled is None else tiled.size()[-1] % ttnn.TILE_SIZE == 0
                layout = TtnnTileLayout() if tiled else TtnnRowMajorLayout()
                tensor = g.call_function(ttnn.embedding, (args[1], args[0]), {"layout": layout})
                return tensor if tiled else g.call_function(ttnn.to_layout, (tensor, TtnnTileLayout()))

            if node.target == torch.ops.aten._log_softmax.default:
                softmax_node = g.call_function(
                    ttnn.softmax,
                    args[:2],
                    {
                        "numeric_stable": True,
                        **kwargs,
                    },
                )
                return g.call_function(ttnn.log, (softmax_node,), kwargs)

            if node.target == torch.ops.aten.div.Tensor:
                if isinstance(args[1], (float, int)):
                    return g.call_function(ttnn.mul, (args[0], 1.0 / args[1]), {})

                if get_shape(args[0]) == get_shape(args[1]):
                    return g.call_function(ttnn.div, args, {})

                recip = g.call_function(ttnn.reciprocal, (args[1],), {})
                return g.call_function(ttnn.mul, (args[0], recip), {})

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
                # Repeat fails if last dimension of input is 1
                if input_tensor_shape[-1] != 1 and len(input_tensor_shape) == len(output_shape):
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

                if step != 1 or dim >= rank:
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
                shape = tensor.meta["val"].size()

                if np.prod(sizes) == 1:
                    return tensor

                # Current repeat implementation requires aligned last dim when repeating on last dim
                if sizes[-1] == 1 or shape[-1] % 16 == 0:
                    return g.call_function(target_wrappers.repeat, args)

                return None

            if node.target == torch.ops.aten.squeeze.dim or node.target == torch.ops.aten.squeeze.default:
                if use_less_ttnn_op_types or node.target == torch.ops.aten.squeeze.default:
                    # ttnn.squeeze does not support calling the OP without provided dim (torch.ops.aten.squeeze.default)
                    # squeezing is the same as reshaping to shape of output tensor of squeeze
                    output_size = list(node.meta["val"].size())
                    return g.call_function(ttnn.reshape, args=(args[0], output_size))
                else:
                    return g.call_function(ttnn.squeeze, args=(args[0], args[1]))

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

            if node.target == torch.ops.aten.permute.default:
                new_nodes = list()
                new_nodes.append(g.call_function(ttnn.permute, args=(args[0], args[1])))
                new_nodes[-1].meta["val"] = node.meta["val"]

                # strange workaround when dim 0 is 1 for rank 3
                # TODO(bdrazic): remove workaround when permute issue is fixed https://github.com/tenstorrent/tt-metal/issues/11191
                # and this can then go to ReplaceMoreTt class.
                output_size = node.meta["val"].size()
                rank = len(output_size)
                # TODO(tt-metal#15165): ttnn.permute > 4D shape is not supported yet
                if rank > 4:
                    return None
                new_nodes = workaround_permute_3d_first_out_dim_is_one(g, new_nodes, rank, output_size)
                return new_nodes[-1]

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
                # TODO(#192): Front padding isn't well supported so skip for now
                if not all(f == 0 for f, _ in full_pad):
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
                # TODO(#515)
                if output_shape[-1] % 2 != 0:
                    return None
                return g.call_function(ttnn.pad, args=(input, full_pad, value))

            if node.target in [torch.ops.aten.view.default, torch.ops.aten._unsafe_view.default]:
                input_tensor_num_element = args[0].meta["val"].numel()
                output_shape_num_element = node.meta["val"].numel()
                if input_tensor_num_element == 0 or output_shape_num_element == 0:
                    return None
                return g.call_function(ttnn.reshape, (args[0], args[1]), {})

            if node.target == torch.ops.aten.split.Tensor:
                # convert input tensopr to ROW MAJOR layout for split
                to_layout = g.call_function(ttnn.to_layout, (args[0],), {"layout": TtnnRowMajorLayout()})

                # convert relative split dim to absolute
                if args[2] >= 0:
                    split_dim = args[0]
                else:
                    split_dim = len(args[0].meta["val"].size()) + args[2]

                # convert from PyTorch size of chunk to ttnn number of chunks
                if isinstance(args[1], int):
                    num_chunks = math.floor(args[0].meta["val"].size()[split_dim] / args[1])
                else:
                    raise RuntimeError(f"ttnn.split only supports chunks of same size.")

                new_args = (to_layout, num_chunks, split_dim)
                return g.call_function(ttnn.split, args=new_args)

            if node.target == torch.ops.aten._to_copy.default:
                # Keep it if casting to bool type(bool may be problematic)
                if kwargs["dtype"] in [torch.bool]:
                    return None
                # Keep it if the graph output uses this op
                target_users_ops = [user.target for user in node.users.keys()]
                if "output" in target_users_ops:
                    return None
                src_dtype = node.args[0].meta["val"].dtype
                dst_dtype = kwargs["dtype"]
                # Some aten op need it to cast specific dtype (ex, index_select)
                # Keep it if casting from int to float or reverse

                try:
                    ttnn_dtype = torch_dtype_to_ttnn_dtype(dst_dtype)
                    return g.call_function(ttnn.typecast, args=(node.args[0], ttnn_dtype))
                except:
                    pass

                if dst_dtype in [torch.int32, torch.int64] and src_dtype not in [torch.int32, torch.int64]:
                    return None
                if src_dtype in [torch.int32, torch.int64] and dst_dtype not in [torch.int32, torch.int64]:
                    return None
                # Essentially remove this op
                return node.args[0]

            if node.target in [torch.ops.aten.masked_fill.Scalar, torch.ops.aten.masked_fill.Tensor]:
                # aten.masked_fill is equivalent to the following:
                # masked_fill = (tensor * (ones - mask)) + (mask * full)

                tensor, mask, fill_value = args
                tensor_shape = tensor.meta["val"].size()
                mask_shape = mask.meta["val"].size()

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

                input_size = tensor.meta["val"].size()
                output_size = node.meta["val"].size()

                if input_size.numel() != output_size.numel():
                    slice_start, slice_end = [0] * len(input_size), list(input_size)
                    slice_start[dim] = (start + input_size[dim]) % input_size[dim]
                    slice_end[dim] = slice_start[dim] + 1

                    slice_tensor = g.call_function(ttnn.slice, (tensor, [*slice_start], [*slice_end]))
                else:
                    slice_tensor = tensor
                    if len(output_size) == 0:
                        return g.call_function(torch.ops.aten.squeeze.dim, args=(tensor, 0))

                return g.call_function(ttnn.reshape, args=(slice_tensor, list(output_size)))

            if node.target == torch.ops.aten.cumsum.default:
                tensor, dim = args
                input_shape = tensor.meta["val"].size()
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
                input_size = args[0].meta["val"].size()
                output_size = node.meta["val"].size()

                sum_tensor = args[0]
                if input_size.numel() != output_size.numel():
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
                kernel_size = params["kernel_size"]
                batch_size, in_c, in_h, in_w = input_tensor.meta["val"].size()
                stride = params.get("stride", kernel_size)
                padding = params.get("padding", (0, 0))
                dilation = params.get("dilation", (1, 1))
                ceil_mode = params.get("ceil_mode", False)
                # Assume the element size is bfloat16
                volume = (batch_size * in_c * in_h * in_w) * 2
                if (
                    # TODO(tt-metal#14976): ceil mode isn't supported yet
                    ceil_mode
                    # TODO(#385): OOM
                    or volume > 16 * 1024 * 1024
                    # TODO(tt-metal#13901): Wide input channels can only be multiple of 8 tiles
                    or (in_c > (ttnn.TILE_SIZE * 8) and in_c % (ttnn.TILE_SIZE * 8) != 0)
                    # TODO(#419): Currently fails with in_c < 16
                    or in_c < 16
                    # TODO(tt-metal#12099): Currently it doesn't return indices. Convert if only the value is used
                    or not is_getitem_0_only_user(node)
                ):
                    return None

                input_tensor = insert_nchw_to_nhwc(g, input_tensor)
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
                )
                output_tensor = insert_sharded_nhwc_to_nchw(g, output_tensor, node.meta["val"][0].size())
                # TODO(tt-metal#12099): Currently it doesn't return indices. Pack into tuple to maintain the type
                return g.call_function(target_wrappers.pack_to_tuple, (output_tensor,))

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
                weight_node = params["weight_tensor"]
                transposed = params.get("transposed", False)
                groups = params.get("groups", 1)
                stride = params.get("stride", [1, 1])
                padding = params.get("padding", [0, 0])
                dilation = params.get("dilation", [1, 1])
                output_padding = params.get("output_padding", [0, 0])

                input_shape = input_node.meta["val"].size()
                if len(input_shape) < 4:
                    return None

                batch_size, in_c, in_h, in_w = input_shape
                out_a, out_b, kernel_h, kernel_w = weight_node.meta["val"].size()
                out_c = out_b if transposed else out_a

                input_tensor = insert_nchw_to_nhwc(g, input_node)
                # TODO(tt-metal#15148): ttnn.conv2d internal reshape fails with padding
                input_tensor = g.call_function(ttnn.reshape, (input_tensor, (1, 1, batch_size * in_h * in_w, in_c)))
                # TODO(#417): weight currently needs to be on host
                weight_tensor = g.call_function(
                    target_wrappers.move_to_host,
                    (weight_node, TtnnRowMajorLayout()),
                )
                bias_node = params.get("bias_tensor", None)
                if bias_node is None:
                    bias_tensor = None
                else:
                    bias_shape = bias_node.meta["val"].size()
                    bias_tensor = g.call_function(
                        ttnn.reshape,
                        (bias_node, (1,) * (4 - len(bias_shape)) + bias_shape),
                    )
                output_tensor = g.call_function(
                    target_wrappers.conv2d,
                    (
                        input_tensor,
                        weight_tensor,
                        bias_tensor,
                        batch_size,
                        in_c,
                        out_c,
                        in_h,
                        in_w,
                        (kernel_h, kernel_w),
                        stride,
                        padding,
                        dilation,
                        groups,
                        TtnnDevice(),
                        transposed,
                        output_padding if transposed else None,
                    ),
                )
                output_shape = node.meta["val"].size()
                return insert_sharded_nhwc_to_nchw(g, output_tensor, output_shape)

            if node.target == torch.ops.aten.slice_scatter.default:
                tensor, src_tensor, dim, start, end, *step = args

                tensor_shape = tensor.meta["val"].size()
                src_tensor_shape = src_tensor.meta["val"].size()

                # nothing to slice, result tensors == src_tensor
                if tensor_shape == src_tensor_shape:
                    return src_tensor

                # slice_scatter could be concat([pre_slice_tensor, src_tensor, post_slice_tensor])
                rank = len(tensor_shape)
                [step] = step or [1]
                if step != 1:
                    return None

                assert dim < rank, f"The slice dim {dim} should be less than rank {rank}"

                dim = (dim + rank) % rank
                start = start if start is not None else 0
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

                return g.call_function(ttnn.concat, (tensors_to_concat, dim))

            # PEP 8 suggests this explicit statement
            return None

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
    def __init__(self, device, use_less_ttnn_op_types):
        self.device = device
        self.use_less_ttnn_op_types = use_less_ttnn_op_types

    def call(self, gm: torch.fx.GraphModule):
        # Replace more patterns with torch.fx.Transformer
        gm = ReplaceMoreTt(gm, self.device, self.use_less_ttnn_op_types).transform()

        # Replace patterns manually
        gm = ReplaceMoreTtManually(gm, self.use_less_ttnn_op_types)

        return PassResult(gm, True)

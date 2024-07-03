import torch
from ..utils import (
    GraphCleanup,
    DummyTtlTensorTensorMemoryLayoutInterleaved,
    DummyTtlTensorBufferTypeDram,
    DummyTtnnBfloat16,
    DummyDevice,
    DummyTtnnTileLayout,
)

try:
    import ttnn
except ImportError:
    print("ttnn is not installed, use mock_ttnn instead")
    from .. import mock_ttnn as ttnn

from torch.fx.passes.infra.pass_base import PassBase, PassResult
import torch.fx.traceback as fx_traceback

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


class ReplaceMoreTt(torch.fx.Transformer):
    def call_function(self, target, args, kwargs):
        if are_args_from_int_output_ops(args):
            call_func = super().call_function(target, args, kwargs)
        elif target == torch.ops.aten.sub.Tensor:
            call_func = super().call_function(ttnn.sub, args, kwargs)
        elif target == torch.ops.aten.rsub.Tensor:
            # TODO(kevinwuMCW): handle alpha parameter if exists
            call_func = super().call_function(ttnn.sub, (args[1], args[0]), kwargs)
        elif target == torch.ops.aten.mul.Tensor:
            call_func = super().call_function(ttnn.mul, args, kwargs)
        elif target == torch.ops.aten._softmax.default:
            call_func = super().call_function(ttnn.softmax, args[:2], kwargs)
        elif target == torch.ops.aten.tanh.default:
            call_func = super().call_function(ttnn.tanh, args, kwargs)
        elif target == torch.ops.aten.view.default:
            # TODO(kevinwuTT): Handle restrictions from ttnn.reshape
            call_func = super().call_function(target, args, kwargs)
        elif target == torch.ops.aten.permute.default:
            call_func = super().call_function(ttnn.permute, args, kwargs)
        elif target == torch.ops.aten.relu.default:
            call_func = super().call_function(ttnn.relu, args, kwargs)
        elif target == torch.ops.aten.addmm.default:
            # TODO(kevinwuMCW): include beta, alpha, and optional args
            mm = super().call_function(ttnn.matmul, (args[1], args[2]), kwargs)
            call_func = super().call_function(ttnn.add, (args[0], mm), kwargs)
        elif target == torch.ops.aten.bmm.default:
            call_func = super().call_function(ttnn.matmul, args, kwargs)
        elif target == torch.ops.aten.gelu.default:
            call_func = super().call_function(ttnn.gelu, args, kwargs)
        elif target == torch.ops.aten.neg.default:
            call_func = super().call_function(ttnn.neg, args, kwargs)
        elif target == torch.ops.aten.tril.default:
            call_func = super().call_function(ttnn.tril, args, kwargs)
        elif target == torch.ops.aten.eq.Tensor:
            call_func = super().call_function(ttnn.eq, args, kwargs)
        elif target == torch.ops.aten.logical_not.default:
            call_func = super().call_function(ttnn.logical_not, args, kwargs)
        elif target == torch.ops.aten.zeros_like.default:
            call_func = super().call_function(ttnn.zeros_like, args, {})
        elif target == torch.ops.aten.mean.dim:
            # change dim parameter to tuple
            new_args = list(args)
            new_args[1] = tuple(args[1]) if len(args[1]) > 1 else args[1][0]
            call_func = super().call_function(ttnn.mean, tuple(new_args), kwargs)
        elif target == torch.ops.aten.add.Tensor:
            call_func = super().call_function(ttnn.add, args, kwargs)
        elif target == torch.ops.aten.mm.default:
            call_func = super().call_function(ttnn.matmul, args, kwargs)
        elif target == torch.ops.aten.pow.Tensor_Scalar:
            call_func = super().call_function(ttnn.pow, args, kwargs)
        elif target == torch.ops.aten.rsqrt.default:
            call_func = super().call_function(ttnn.rsqrt, args, kwargs)
        elif target == torch.ops.aten.silu.default:
            call_func = super().call_function(ttnn.silu, args, kwargs)
        elif target == torch.ops.aten._adaptive_avg_pool2d.default:
            # assumes output size is (1, 1)
            call_func = super().call_function(
                ttnn.global_avg_pool2d, (args[0],), kwargs
            )
        elif target == torch.ops.aten.clamp.default:
            call_func = super().call_function(ttnn.clip, args, kwargs)
        elif target == torch.ops.aten.squeeze.dim:
            # NOTE(kevinwuTT): ttnn.squeeze only supports dim 0 currently
            if args[1] != 0:
                call_func = super().call_function(target, args, kwargs)
            else:
                call_func = super().call_function(ttnn.squeeze, args, kwargs)
        elif target == torch.ops.aten.lt.Tensor:
            call_func = super().call_function(ttnn.lt, args, kwargs)
        elif target == torch.ops.aten.cos.default:
            call_func = super().call_function(ttnn.cos, args, kwargs)
        elif target == torch.ops.aten.sigmoid.default:
            call_func = super().call_function(ttnn.sigmoid, args, kwargs)
        else:
            call_func = super().call_function(target, args, kwargs)

        # Copy metadata of old node to replacement
        meta = fx_traceback.get_current_meta()
        if meta is not None and "val" in meta:
            call_func.node.meta["val"] = meta["val"]
        return call_func


def torch_dtype_to_dummy_ttnn_dtype(dtype: torch.dtype):
    # Add newly supported dtypes here:
    dtype_map = {
        torch.float32: DummyTtnnBfloat16(),
        torch.bfloat16: DummyTtnnBfloat16(),
    }
    if dtype in dtype_map:
        return dtype_map.get(dtype)
    else:
        raise RuntimeError(
            f"Missing conversion from torch.dtype: {dtype} to DummyTtnn dtype."
        )


# Certain ops don't support certain shapes and will emit a valid_page_size error
# RuntimeError: TT_FATAL @ ../tt_metal/impl/buffers/buffer.cpp:38: valid_page_size
# For valid non-interleaved buffers page size 2048 must equal buffer size X. For interleaved-buffers page size should be divisible by buffer size
def has_valid_page_size(shape):
    for dim in shape:
        if dim < 32:
            return False
    return True


def ReplaceMoreTtManually(gm: torch.fx.GraphModule) -> torch.fx.GraphModule:
    nodes = list(gm.graph.nodes)
    for node in nodes:
        g = node.graph
        args = node.args

        with g.inserting_before(node):
            # TODO (kevinwuTT): consolidate and simplify these statements?
            if node.target == torch.ops.aten.clone.default:
                arg_metadata = node.meta["val"]
                dummy_dtype = torch_dtype_to_dummy_ttnn_dtype(arg_metadata.dtype)
                # Add additional logic to choose the appropriate memory_config type: DRAM or L1
                memory_config = g.call_function(
                    ttnn.MemoryConfig,
                    (
                        DummyTtlTensorTensorMemoryLayoutInterleaved(),
                        DummyTtlTensorBufferTypeDram(),
                    ),
                )
                new_node = g.call_function(
                    ttnn.clone, args=(args[0], memory_config, dummy_dtype)
                )
                node.replace_all_uses_with(
                    new_node,
                    delete_user_cb=lambda node: node != new_node,
                )
            if node.target == torch.ops.aten.native_layer_norm.default:
                new_node = g.call_function(
                    ttnn.layer_norm,
                    args=(args[0],),
                    kwargs={"epsilon": args[4], "weight": args[2], "bias": args[3]},
                )
                node.replace_all_uses_with(
                    new_node,
                    delete_user_cb=lambda node: node != new_node,
                )
                node_users = list(new_node.users.keys())
                for node_user in node_users:
                    node_user.replace_all_uses_with(new_node)
            if node.target == torch.ops.aten.ones.default:
                new_node = g.call_function(
                    ttnn.ones, args=args, kwargs={"device": DummyDevice()}
                )
                node.replace_all_uses_with(
                    new_node,
                    delete_user_cb=lambda node: node != new_node,
                )
            """
            # NOTE(kevinwuTT): aten.arange.default starts with 0 which is unsupported by ttnn.arange at the moment
            if node.target == torch.ops.aten.arange.default:
                # start = 0, step = 1
                new_args = (0,)
                new_kwargs = {"end": args[0], "step": 1, "device": DummyDevice()}
                new_node = g.call_function(ttnn.arange, args=new_args, kwargs=new_kwargs)
                node.replace_all_uses_with(new_node, delete_user_cb=lambda node: node != new_node,)
            """
            if node.target == torch.ops.aten.arange.start:
                # NOTE(kevinwuTT): ttnn.arange does not support starting values smaller than 2 currently
                if args[0] >= 2:
                    # step = 1
                    new_args = (args[0],)
                    new_kwargs = {"end": args[1], "step": 1, "device": DummyDevice()}
                    new_node = g.call_function(
                        ttnn.arange, args=new_args, kwargs=new_kwargs
                    )
                    node.replace_all_uses_with(
                        new_node,
                        delete_user_cb=lambda node: node != new_node,
                    )
            if node.target == torch.ops.aten.arange.start_step:
                # NOTE(kevinwuTT): ttnn.arange does not support starting values smaller than 2 currently
                if args[0] >= 2:
                    new_args = (args[0],)
                    new_kwargs = {
                        "end": args[1],
                        "step": args[2],
                        "device": DummyDevice(),
                    }
                    new_node = g.call_function(
                        ttnn.arange, args=new_args, kwargs=new_kwargs
                    )
                    node.replace_all_uses_with(
                        new_node,
                        delete_user_cb=lambda node: node != new_node,
                    )
            if node.target in relational_scalar_ops:
                # NOTE(kevinwuTT): ttnn.eq shows error if passing a literal scalar as an argument.
                # Instead, fill a tensor with the same size as args[0] with the scalar value using ttnn.full
                arg_metadata = node.meta["val"]
                if has_valid_page_size(arg_metadata.size()):
                    new_kwargs = {
                        "fill_value": args[1],
                        "device": DummyDevice(),
                        "layout": DummyTtnnTileLayout(),
                    }
                    full_node = g.call_function(
                        ttnn.full, args=(arg_metadata.size(),), kwargs=new_kwargs
                    )
                    new_node = g.call_function(
                        relational_scalar_ops[node.target],
                        args=(args[0], full_node),
                        kwargs={},
                    )
                    node.replace_all_uses_with(
                        new_node,
                        delete_user_cb=lambda node: node != new_node,
                    )
            if node.target == torch.ops.aten.full.default:
                # args[0] can be empty for aten.full which simply creates a scalar. Ignore conversion in this case.
                if args[0]:
                    new_kwargs = {
                        "fill_value": args[1],
                        "device": DummyDevice(),
                        "layout": DummyTtnnTileLayout(),
                    }
                    new_node = g.call_function(
                        ttnn.full, args=(tuple(args[0]),), kwargs=new_kwargs
                    )
                    node.replace_all_uses_with(
                        new_node,
                        delete_user_cb=lambda node: node != new_node,
                    )
            if node.target == torch.ops.aten.baddbmm.default:
                kwargs = node.kwargs
                # out = beta * input + alpha * (batch1 @ batch2)
                # if beta is 0, input is ignored, and nan and inf in it will not be propogated
                new_node = g.call_function(ttnn.matmul, args=(args[1], args[2]))
                if "alpha" in kwargs:
                    new_node = g.call_function(
                        ttnn.multiply, args=(new_node, kwargs["alpha"])
                    )
                if "beta" in kwargs:
                    if kwargs["beta"] != 0:
                        beta_node = g.call_function(
                            ttnn.multiply, args=(args[0], kwargs["beta"])
                        )
                        new_node = g.call_function(ttnn.add, args=(beta_node, new_node))
                else:
                    new_node = g.call_function(ttnn.add, args=(args[0], new_node))
                node.replace_all_uses_with(
                    new_node,
                    delete_user_cb=lambda node: node != new_node,
                )
            if node.target == torch.ops.aten.embedding.default:
                # TODO(kevinwuTT): Add support for ROW_MAJOR_LAYOUT
                new_kwargs = {"layout": DummyTtnnTileLayout()}
                new_node = g.call_function(
                    ttnn.embedding, args=(args[1], args[0]), kwargs=new_kwargs
                )
                node.replace_all_uses_with(
                    new_node,
                    delete_user_cb=lambda node: node != new_node,
                )
            if node.target == torch.ops.aten.rsub.Scalar:
                # NOTE(kevinwuTT): ttnn.sub shows error if passing a literal scalar as the first argument.
                # Instead, fill a tensor with the same size as args[0] with the scalar value using ttnn.full
                node_metadata = node.meta["val"]
                # NOTE(kevinwuTT): Only bfloat16 seems to work for now
                # TODO(kevinwuTT): Use ttnn.full instead of aten
                new_kwargs = {
                    "fill_value": args[1],
                    "device": DummyDevice(),
                }
                full = g.call_function(
                    ttnn.full, args=(tuple(node_metadata.size()),), kwargs=new_kwargs
                )
                to_layout = g.call_function(
                    ttnn.to_layout, (full,), {"layout": DummyTtnnTileLayout()}
                )
                new_node = g.call_function(
                    ttnn.sub, args=(to_layout, args[0]), kwargs={}
                )
                node.replace_all_uses_with(
                    new_node,
                    delete_user_cb=lambda node: node != new_node,
                )
            if node.target == torch.ops.aten.div.Tensor:
                # ttnn.recip does not support scalars. Call an ttnn.full and pass that to ttnn.recip
                # TODO(kevinwuTT): Use a ttnn equivalent
                node_metadata = node.meta["val"]
                if isinstance(args[1], float):
                    new_kwargs = {
                        "fill_value": args[1],
                        "device": DummyDevice(),
                    }
                    full = g.call_function(
                        ttnn.full,
                        args=(tuple(node_metadata.size()),),
                        kwargs=new_kwargs,
                    )
                    to_layout = g.call_function(
                        ttnn.to_layout, (full,), {"layout": DummyTtnnTileLayout()}
                    )
                    recip = g.call_function(ttnn.reciprocal, (to_layout,), {})
                else:
                    recip = g.call_function(ttnn.reciprocal, (args[1],), {})
                new_node = g.call_function(ttnn.mul, (args[0], recip), {})
                node.replace_all_uses_with(
                    new_node,
                    delete_user_cb=lambda node: node != new_node,
                )
            if node.target == torch.ops.aten._to_copy.default:
                kwargs = node.kwargs
                dummy_dtype = torch_dtype_to_dummy_ttnn_dtype(kwargs["dtype"])
                # Add additional logic to choose the appropriate memory_config type: DRAM or L1
                memory_config = g.call_function(
                    ttnn.MemoryConfig,
                    (
                        DummyTtlTensorTensorMemoryLayoutInterleaved(),
                        DummyTtlTensorBufferTypeDram(),
                    ),
                )
                new_kwargs = {
                    "dtype": dummy_dtype,
                    "layout": DummyTtnnTileLayout(),
                    "device": DummyDevice(),
                    "memory_config": memory_config,
                }
                new_node = g.call_function(ttnn.as_tensor, args, new_kwargs)
                node.replace_all_uses_with(
                    new_node,
                    delete_user_cb=lambda node: node != new_node,
                )
            if node.target == torch.ops.aten.t.default:
                permutation = list()
                rank = len(node.meta["val"].size())
                assert rank >= 0 and rank <= 2, "Input tensor can only be 0D, 1D or 2D"
                if rank == 2:
                    permutation = [1, 0]
                    new_node = g.call_function(
                        ttnn.permute, args=(args[0], permutation)
                    )
                    node.replace_all_uses_with(
                        new_node,
                        delete_user_cb=lambda node: node != new_node,
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

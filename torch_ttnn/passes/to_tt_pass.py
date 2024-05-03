import torch
from ..utils import (
    GraphCleanup,
    DummyTtlTensorTensorMemoryLayoutInterleaved,
    DummyTtlTensorBufferTypeDram,
    DummyTtnnBfloat16,
    DummyDevice,
)

try:
    import ttnn
except ImportError:
    print("ttnn is not installed, use mock_ttnn instead")
    from .. import mock_ttnn as ttnn

from torch.fx.passes.infra.pass_base import PassBase, PassResult
import torch.fx.traceback as fx_traceback

class ReplaceMoreTt(torch.fx.Transformer):
    def call_function(self, target, args, kwargs):
        if target == torch.ops.aten.sub.Tensor:
            call_func = super().call_function(ttnn.sub, args, kwargs)
        elif target == torch.ops.aten.rsub.Tensor:
            # TODO(kevinwuMCW): handle alpha parameter if exists
            call_func =  super().call_function(ttnn.sub, (args[1], args[0]), kwargs)
        elif target == torch.ops.aten.mul.Tensor:
            call_func =  super().call_function(ttnn.mul, args, kwargs)
        elif target == torch.ops.aten._softmax.default:
            call_func =  super().call_function(ttnn.softmax, args[:2], kwargs)
        elif target == torch.ops.aten.tanh.default:
            call_func =  super().call_function(ttnn.tanh, args, kwargs)
        elif target == torch.ops.aten.view.default:
            call_func =  super().call_function(ttnn.reshape, args, kwargs)
        elif target == torch.ops.aten.permute.default:
            call_func =  super().call_function(ttnn.permute, args, kwargs)
        elif target == torch.ops.aten.relu.default:
            call_func =  super().call_function(ttnn.relu, args, kwargs)
        elif target == torch.ops.aten.addmm.default:
            # TODO(kevinwuMCW): include beta, alpha, and optional args
            mm = super().call_function(ttnn.matmul, (args[1], args[2]), kwargs)
            call_func =  super().call_function(ttnn.add, (args[0], mm), kwargs)
        elif target == torch.ops.aten.div.Tensor:
            recip = super().call_function(ttnn.reciprocal, (args[1],), kwargs)
            call_func =  super().call_function(ttnn.mul, (args[0], recip), kwargs)
        elif target == torch.ops.aten.bmm.default:
            call_func =  super().call_function(ttnn.matmul, args, kwargs)
        elif target == torch.ops.aten.gelu.default:
            call_func =  super().call_function(ttnn.gelu, args, kwargs)
        elif target == torch.ops.aten.embedding.default:
            call_func =  super().call_function(ttnn.embedding, (args[1], args[0]), kwargs)
        elif target == torch.ops.aten.split.Tensor:
            call_func =  super().call_function(ttnn.split, args, kwargs)
        elif target == torch.ops.aten.neg.default:
            call_func =  super().call_function(ttnn.neg, args, kwargs)
        elif target == torch.ops.aten.tril.default:
            call_func =  super().call_function(ttnn.tril, args, kwargs)
        elif target == torch.ops.aten.eq.Tensor:
            call_func =  super().call_function(ttnn.eq, args, kwargs)
        elif target == torch.ops.aten.eq.Scalar:
            call_func =  super().call_function(ttnn.eq, args, kwargs)
        elif target == torch.ops.aten.logical_not.default:
            call_func =  super().call_function(ttnn.logical_not, args, kwargs)
        elif target == torch.ops.aten.zeros_like.default:
            call_func =  super().call_function(ttnn.zeros_like, args, {})
        elif target == torch.ops.aten.mean.dim:
            # change dim parameter to tuple
            new_args = list(args)
            new_args[1] = tuple(args[1]) if len(args[1]) > 1 else args[1][0]
            call_func = super().call_function(ttnn.mean, tuple(new_args), kwargs)
        else:
            call_func = super().call_function(target, args, kwargs)

        # Copy metadata of old node to replacement
        meta = fx_traceback.get_current_meta()
        if meta is not None and "val" in meta:
            call_func.node.meta['val'] = meta["val"]
        return call_func

def torch_dtype_to_dummy_ttnn_dtype(dtype: torch.dtype):
    # Add newly supported dtypes here:
    dtype_map = {
        torch.bfloat16 : DummyTtnnBfloat16()
    }
    if dtype in dtype_map:
        return dtype_map.get(dtype)
    else:
        raise RuntimeError(f"Missing conversion from torch.dtype: {dtype} to DummyTtnn dtype.")

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
                memory_config = g.call_function(ttnn.MemoryConfig, (DummyTtlTensorTensorMemoryLayoutInterleaved(), DummyTtlTensorBufferTypeDram()))
                new_node = g.call_function(ttnn.clone, args=(args[0], memory_config, dummy_dtype))
                node.replace_all_uses_with(new_node, delete_user_cb=lambda node: node != new_node,)
            if node.target == torch.ops.aten.native_layer_norm.default:
                new_node = g.call_function(ttnn.layer_norm, args=(args[0],), kwargs={"epsilon": args[4], "weight": args[2], "bias": args[3]})
                node.replace_all_uses_with(new_node, delete_user_cb=lambda node: node != new_node,)
                node_users = list(new_node.users.keys())
                for node_user in node_users:
                    node_user.replace_all_uses_with(new_node)
            if node.target == torch.ops.aten.ones.default:
                new_node = g.call_function(ttnn.ones, args=args, kwargs={"device": DummyDevice()})
                node.replace_all_uses_with(new_node, delete_user_cb=lambda node: node != new_node,)
            if node.target == torch.ops.aten.arange.default:
                # start = 0, step = 1
                new_args = (0,)
                new_kwargs = {"end": args[0], "step": 1, "device": DummyDevice()}
                new_node = g.call_function(ttnn.arange, args=new_args, kwargs=new_kwargs)
                node.replace_all_uses_with(new_node, delete_user_cb=lambda node: node != new_node,)
            if node.target == torch.ops.aten.arange.start:
                # step = 1
                new_args = (args[0],)
                new_kwargs = {"end": args[1], "step": 1, "device": DummyDevice()}
                new_node = g.call_function(ttnn.arange, args=new_args, kwargs=new_kwargs)
                node.replace_all_uses_with(new_node, delete_user_cb=lambda node: node != new_node,)
            if node.target == torch.ops.aten.arange.start_step:
                new_args = (args[0],)
                new_kwargs = {"end": args[1], "step": args[2], "device": DummyDevice()}
                new_node = g.call_function(ttnn.arange, args=new_args, kwargs=new_kwargs)
                node.replace_all_uses_with(new_node, delete_user_cb=lambda node: node != new_node,)

    gm = GraphCleanup(gm)
    return gm


class ToTtPass(PassBase):
    def call(self, gm: torch.fx.GraphModule):
        # NOTE(yoco): In our case, subgraph_rewriter actually
        # is not a best choice. We should use torch.fx.Transformer.
        # However, we use subgraph_rewriter for demonstration
        # and as a code stub. Because Transformer only support
        # 1-to-N replacement. For N-to-M replacement, we need
        # to use subgraph_rewriter.
        from ..patterns import add
        from ..patterns import mm

        # Patterns and replacements
        pat_rep_list = list()
        pat_rep_list += add.pat_rep_list
        pat_rep_list += mm.pat_rep_list

        # Replace patterns
        modified = False
        for pat, rep in pat_rep_list:
            replaced_pats = torch.fx.subgraph_rewriter.replace_pattern(gm, pat, rep)
            modified = modified or len(replaced_pats) > 0

        # Replace more patterns with torch.fx.Transformer
        gm = ReplaceMoreTt(gm).transform()

        # Replace patterns manually
        gm = ReplaceMoreTtManually(gm)

        return PassResult(gm, True)

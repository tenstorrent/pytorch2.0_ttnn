import torch
import ttnn

from torch.fx.passes.infra.pass_base import PassBase, PassResult


class ReplacePointwiseUnary(torch.fx.Transformer):
    opmap = {
        torch.ops.aten.abs.default: ttnn.abs,
        torch.ops.aten.acos.default: ttnn.acos,
        torch.ops.aten.acosh.default: ttnn.acosh,
        torch.ops.aten.asin.default: ttnn.asin,
        torch.ops.aten.asinh.default: ttnn.asinh,
        torch.ops.aten.atan.default: ttnn.atan,
        torch.ops.aten.atan2.default: ttnn.atan2,
        torch.ops.aten.atanh.default: ttnn.atanh,
        torch.ops.aten.clone.default: ttnn.clone,
        torch.ops.aten.cos.default: ttnn.cos,
        torch.ops.aten.cosh.default: ttnn.cosh,
        torch.ops.aten.erf.default: ttnn.erf,
        torch.ops.aten.exp.default: ttnn.exp,
        torch.ops.aten.expm1.default: ttnn.expm1,
        torch.ops.aten.gelu.default: ttnn.gelu,
        torch.ops.aten.hardtanh.default: ttnn.hardtanh,
        torch.ops.aten.isinf.default: ttnn.isinf,
        torch.ops.aten.isnan.default: ttnn.isnan,
        torch.ops.aten.leaky_relu.default: ttnn.leaky_relu,
        torch.ops.aten.log.default: ttnn.log,
        torch.ops.aten.log10.default: ttnn.log10,
        torch.ops.aten.log1p.default: ttnn.log1p,
        torch.ops.aten.log2.default: ttnn.log2,
        torch.ops.aten.logical_not.default: ttnn.logical_not,
        torch.ops.aten.neg.default: ttnn.neg,
        torch.ops.aten.reciprocal.default: ttnn.reciprocal,
        torch.ops.aten.relu.default: ttnn.relu,
        torch.ops.aten.rsqrt.default: ttnn.rsqrt,
        torch.ops.aten.sigmoid.default: ttnn.sigmoid,
        torch.ops.aten.sign.default: ttnn.sign,
        torch.ops.aten.sin.default: ttnn.sin,
        torch.ops.aten.sinh.default: ttnn.sinh,
        torch.ops.aten.sqrt.default: ttnn.sqrt,
        torch.ops.aten.tan.default: ttnn.tan,
        torch.ops.aten.tanh.default: ttnn.tanh,
    }

    def call_function(self, target, args, kwargs):
        if target in self.opmap:
            return super().call_function(self.opmap[target], args, kwargs)
        return super().call_function(target, args, kwargs)


class ReplacePointwiseBinary(torch.fx.Transformer):
    opmap = {
        torch.ops.aten.add.Tensor: ttnn.add,
        torch.ops.aten.eq.Tensor: ttnn.eq,
        torch.ops.aten.gt.Tensor: ttnn.gt,
        torch.ops.aten.logical_and.default: ttnn.logical_and,
        torch.ops.aten.logical_or.default: ttnn.logical_or,
        torch.ops.aten.logical_xor.default: ttnn.logical_xor,
        torch.ops.aten.lt.Tensor: ttnn.lt,
        torch.ops.aten.maximum.default: ttnn.maximum,
        torch.ops.aten.minimum.default: ttnn.minimum,
        torch.ops.aten.mul.Tensor: ttnn.mul,
        torch.ops.aten.ne.Tensor: ttnn.ne,
        torch.ops.aten.pow.Tensor_Tensor: ttnn.pow,
        torch.ops.aten.sub.Tensor: ttnn.sub,
        torch.ops.aten.xlogy.Tensor: ttnn.xlogy,
    }

    def call_function(self, target, args, kwargs):
        if target in self.opmap:
            return super().call_function(self.opmap[target], args, kwargs)
        return super().call_function(target, args, kwargs)


class ReplacePointwiseTrinary(torch.fx.Transformer):
    opmap = {
        torch.ops.aten.addcdiv.default: ttnn.addcdiv,
        torch.ops.aten.addcmul.default: ttnn.addcmul,
        # torch.ops.aten.mac.Tensor: ttnn.mac,        # NOTE(yoco): I don't what ttnn.mac is
        torch.ops.aten.where.self: ttnn.where,
    }

    def call_function(self, target, args, kwargs):
        if target in self.opmap:
            return super().call_function(self.opmap[target], args, kwargs)
        return super().call_function(target, args, kwargs)


class ReplaceMatrixMultiplication(torch.fx.Transformer):
    opmap = {
        torch.ops.aten.mm.default: ttnn.matmul,
        torch.ops.aten.linear.default: ttnn.linear,
    }

    def call_function(self, target, args, kwargs):
        if target in self.opmap:
            return super().call_function(self.opmap[target], args, kwargs)
        return super().call_function(target, args, kwargs)


class ReplaceMoreTt(torch.fx.Transformer):
    def call_function(self, target, args, kwargs):
        if target == torch.ops.aten.mm.default:
            return super().call_function(ttnn.matmul, args, kwargs)
        elif target == torch.ops.aten._softmax.default:
            return super().call_function(ttnn.softmax, args[:2], kwargs)
        elif target == torch.ops.aten.view.default:
            return super().call_function(ttnn.reshape, args, kwargs)
        elif target == torch.ops.aten.permute.default:
            return super().call_function(ttnn.permute, args, kwargs)
        return super().call_function(target, args, kwargs)


class ToTtPass(PassBase):
    def call(self, gm: torch.fx.GraphModule):
        # NOTE(yoco): In our case, subgraph_rewriter actually
        # is not a best choice. We should use torch.fx.Transformer.
        # However, we use subgraph_rewriter for demonstration
        # and as a code stub. Because Transformer only support
        # 1-to-N replacement. For N-to-M replacement, we need
        # to use subgraph_rewriter.
        # import patterns.add

        pat_rep_list = list()
        # Patterns and replacements
        from ..patterns import linear

        pat_rep_list += linear.pat_rep_list

        # Replace patterns
        modified = False
        for pat, rep in pat_rep_list:
            replaced_pats = torch.fx.subgraph_rewriter.replace_pattern(gm, pat, rep)
            modified = modified or len(replaced_pats) > 0

        # Replace more patterns with torch.fx.Transformer
        gm = ReplaceMoreTt(gm).transform()
        gm = ReplacePointwiseUnary(gm).transform()
        gm = ReplacePointwiseBinary(gm).transform()
        gm = ReplacePointwiseTrinary(gm).transform()
        gm = ReplaceMatrixMultiplication(gm).transform()

        return PassResult(gm, True)

import torch

from torch.fx.passes.infra.pass_base import PassBase, PassResult
from torch.fx import subgraph_rewriter
from torch_ttnn.passes.lowering import target_wrappers


class PatternReplacementPass(PassBase):
    def __init__(self):
        super().__init__()

        def matmul_relu_pattern(x, y):
            mm = target_wrappers.matmul(x, y)
            rl = target_wrappers.relu(mm)
            return rl

        def matmul_relu_replacement(x, y):
            return target_wrappers.matmul(x, y, activation="relu")

        def matmul_gelu_pattern(x, y):
            mm = target_wrappers.matmul(x, y)
            rl = target_wrappers.gelu(mm)
            return rl

        def matmul_gelu_replacement(x, y):
            return target_wrappers.matmul(x, y, activation="gelu")

        def matmul_silu_pattern(x, y):
            mm = target_wrappers.matmul(x, y)
            rl = target_wrappers.silu(mm)
            return rl

        def matmul_silu_replacement(x, y):
            return target_wrappers.matmul(x, y, activation="silu")

        self.patterns = [matmul_relu_pattern, matmul_gelu_pattern, matmul_silu_pattern]
        self.replacements = [
            matmul_relu_replacement,
            matmul_gelu_replacement,
            matmul_silu_replacement,
        ]

    def call(self, gm: torch.fx.GraphModule):
        modified = False
        for idx, pattern in enumerate(self.patterns):
            replaced_patterns = subgraph_rewriter.replace_pattern_with_filters(gm, pattern, self.replacements[idx])
            modified = modified or len(replaced_patterns) > 0
        return PassResult(gm, modified)

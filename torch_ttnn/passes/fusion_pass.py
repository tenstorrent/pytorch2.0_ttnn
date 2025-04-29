# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0

import torch
from torch.fx.passes.infra.pass_base import PassBase, PassResult
from torch_ttnn.passes.patterns.linear_pattern import LinearPatterns
from torch_ttnn.passes.patterns.soft_max_pattern import SoftMaxPatterns
from pathlib import Path
class FusionPass(PassBase):
    def __init__(self):
        super().__init__()

    def call(self, gm: torch.fx.GraphModule):
        modified = False
        
        # Try linear pattern fusion first
        linear_patterns = LinearPatterns(gm)
        linear_replaced = linear_patterns.replace_linear()
        modified |= len(linear_replaced) > 0
        
        # Then try softmax pattern fusion
        softmax_patterns = SoftMaxPatterns(gm)
        softmax_replaced = softmax_patterns.replace_softmax()
        modified |= len(softmax_replaced) > 0

        output_file = Path.home() / "compiled_code.py"
        with open(output_file, "w") as f:
            f.write(gm.code)

        return PassResult(gm, modified)
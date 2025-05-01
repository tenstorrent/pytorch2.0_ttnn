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
        linear_matches = linear_patterns.match_pattern()
        linear_patterns.replace_pattern(linear_matches)
        modified |= len(linear_matches) > 0
        
        # Then try softmax pattern fusion
        softmax_patterns = SoftMaxPatterns(gm)
        softmax_matches = softmax_patterns.match_pattern()
        softmax_patterns.replace_pattern(softmax_matches)
        modified |= len(softmax_matches) > 0
        

        return PassResult(gm, modified)
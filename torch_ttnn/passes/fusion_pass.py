# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0

import torch
from torch.fx.passes.infra.pass_base import PassBase, PassResult
from torch_ttnn.passes.patterns.linear_pattern import LinearPatterns
from torch_ttnn.passes.patterns.soft_max_pattern import SoftMaxPatterns
from torch_ttnn.passes.patterns.attention_pattern import AttentionPatterns
from pathlib import Path


class FusionPass(PassBase):
    def __init__(self):
        super().__init__()

    def call(self, gm: torch.fx.GraphModule):
        modified = False

        # List of pattern classes to apply
        pattern_classes = [LinearPatterns, SoftMaxPatterns]
        # AttentionPatterns must be applied last
        pattern_classes.append(AttentionPatterns)

        for pattern_cls in pattern_classes:
            pattern = pattern_cls(gm)
            matches = pattern.match_pattern()
            pattern.replace_pattern(matches)
            modified |= len(matches) > 0

        return PassResult(gm, modified)

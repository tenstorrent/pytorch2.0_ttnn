# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0

import torch
import ttnn
from torch.fx import Node
from torch_ttnn.passes.patterns.pattern_matcher_base import PatternMatcherBase
from typing import List, Tuple


class SoftMaxPatterns(PatternMatcherBase):
    """Pattern matcher for attention softmax operations."""

    def match_pattern(self) -> List[Tuple[torch.fx.Node, ...]]:
        """
        Match the attention softmax pattern:
        multiply(x) -> add(attention_mask) -> softmax(numeric_stable=True)

        This pattern represents:
        1. Division by sqrt(head_size)
        2. Addition of attention mask
        3. Numerically stable softmax computation

        The expected output will be:
        ttnn.transformer.attention_softmax(input_tensor, head_size, attention_mask)

        Please note that we are doing this in place
        """
        matches = []

        # Find all multiply nodes with something similar to a scale
        # (int, float bigger than 0)
        multiply_nodes = self._find_nodes_of_type(ttnn.multiply)
        for multiply in multiply_nodes:
            # Check for the scale factor (1/sqrt(head_size))
            # this number should be always be positive
            if not (
                len(multiply.args) > 1
                and isinstance(multiply.args[1], (float))
                and multiply.args[1] > 0
                and multiply.args[1] < 1
            ):  # since is 1/sqrt(head_size), it should be less than 1
                continue

            # Find add operation that combines with attention mask
            add = self._find_exclusive_user_of_type(multiply, ttnn.add)
            if not add:
                continue

            # Verify add has both multiply output and attention mask
            if not (multiply in add.args and add.args[0] == multiply):
                continue

            # Find softmax operation with numeric stability
            softmax = self._find_exclusive_user_of_type(add, ttnn.softmax)
            if not softmax:
                continue

            matches.append((multiply, add, softmax))

        return matches

    def replace_pattern(self, matches: List[Tuple[torch.fx.Node, ...]]) -> None:
        for match in matches:
            multiply, add, softmax = match

            with self.gm.graph.inserting_after(softmax):
                # Get the input tensor and attention mask
                input_tensor = multiply.args[0]
                scale = multiply.args[1]
                head_size = None if scale is None else (int(1 / (scale * scale)) if scale < 1 else int(scale))
                attention_mask = add.args[1]
                fused_node = self.gm.graph.call_function(
                    ttnn.transformer.attention_softmax,
                    args=(input_tensor,),
                    kwargs={"head_size": head_size, "attention_mask": attention_mask},
                )

                # Connect output to the next node
                softmax.replace_all_uses_with(fused_node)

            # Remove old nodes in reverse order
            nodes_to_remove = [softmax, add, multiply]
            self.safe_remove_nodes(nodes_to_remove)

        self.gm.graph.lint()
        self.gm.recompile()
        return matches

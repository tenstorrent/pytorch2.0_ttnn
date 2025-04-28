import torch
import ttnn
from torch.fx import Node
from torch_ttnn.passes.patterns.pattern_matcher_base import PatternMatcherBase
from typing import List, Tuple

class SoftMaxPatterns(PatternMatcherBase[Tuple[torch.fx.Node, ...]]):
    """Pattern matcher for attention softmax operations."""

    def match_softmax_pattern(self) -> List[Tuple[torch.fx.Node, ...]]:
        """
        Match the attention softmax pattern:
        multiply(x) -> add(attention_mask) -> softmax(numeric_stable=True)
        
        This pattern represents:
        1. Division by sqrt(head_size)
        2. Addition of attention mask
        3. Numerically stable softmax computation
        """
        matches = []
        
        # Find all multiply nodes with scale 0.125 (1/sqrt(64))
        multiply_nodes = self._find_nodes_of_type(ttnn.multiply)
        for multiply in multiply_nodes:
            # Check for the scale factor (1/sqrt(head_size))
            # this number should be always be positive
            if not (len(multiply.args) > 1 and multiply.args[1] > 0):
                continue

            # Find add operation that combines with attention mask
            add = self._find_single_user_of_type(multiply, ttnn.add)
            if not add:
                continue

            # Verify add has both multiply output and attention mask
            if not (multiply in add.args):
                continue

            # Find softmax operation with numeric stability
            softmax = self._find_single_user_of_type(add, ttnn.softmax)
            if not softmax:
                continue

            matches.append((multiply, add, softmax))

        return matches

    def replace_softmax(self):
        matches = self.match_softmax_pattern()

        for match in matches:
            multiply, add, softmax = match
            
            with self.gm.graph.inserting_after(softmax):
                # Get the input tensor and attention mask
                input_tensor = multiply.args[0]
                scale = multiply.args[1]
                head_size = int(1 / (scale * scale))
                attention_mask = add.args[1]

                fused_node = self.gm.graph.call_function(
                    ttnn.transformer.attention_softmax_,
                    args=(input_tensor,),
                    kwargs={
                        'head_size': head_size,
                        'attention_mask': attention_mask
                    }
                )

                # Connect output to the next node
                softmax.replace_all_uses_with(fused_node)

            # Remove old nodes in reverse order
            for node in [softmax, add, multiply]:
                self.gm.graph.erase_node(node)

        self.gm.graph.lint()
        self.gm.recompile()
        return matches

    def match_pattern(self) -> List[Tuple[torch.fx.Node, ...]]:
        """Implementation of abstract method from base class."""
        return self.match_softmax_pattern()

    def replace_pattern(self, matches: List[Tuple[torch.fx.Node, ...]]) -> None:
        """Implementation of abstract method from base class."""
        self.replace_softmax()


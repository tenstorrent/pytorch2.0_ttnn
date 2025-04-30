# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0

import torch
import ttnn
from torch.fx import Node
from torch_ttnn.passes.patterns.pattern_matcher_base import PatternMatcherBase
from typing import List, Tuple

class LinearPatterns(PatternMatcherBase[Tuple[torch.fx.Node, ...]]):
    """Pattern matcher for linear operations with optional activation and views."""

    def match_linear_pattern(self) -> List[Tuple[torch.fx.Node, ...]]:
        """
        Match the linear pattern: from_torch -> transpose -> matmul -> add(from_torch_2) -> view -> [activation] -> [view2]
        where activation can be gelu, relu, or silu (optional), followed by an optional second view.
        Returns a list of tuples containing the matched nodes.
        """
        matches = []
        
        # Find all from_torch nodes
        from_torch_nodes = self._find_nodes_of_type(ttnn.from_torch)

        for from_torch in from_torch_nodes:
            # Find transpose operation using from_torch
            transpose = self._find_single_user_of_type(from_torch, ttnn.transpose)
            if not transpose:
                continue

            if (self._find_single_user_of_type(transpose, ttnn.to_torch)):
                continue
            
            # Find matmul operation using transpose
            matmul = self._find_single_user_of_type(transpose, ttnn.matmul)
            if not matmul or not self._is_node_in_args(transpose, matmul):
                continue

            # Find other from_torch nodes that could be the bias
            for from_torch_2 in from_torch_nodes:
                if from_torch_2 == from_torch:
                    continue

                # Find add operation using matmul and from_torch_2
                add_users = [
                    node for node in from_torch_2.users 
                    if self._is_ttnn_op(node, ttnn.add) and 
                    matmul in node.args and 
                    from_torch_2 in node.args
                ]
                
                # we only care about one user of this, it must be a view with gelu, relu, or silu
                if len(add_users) != 1:
                    continue
                
                # For each valid add operation, look for view and optional activation
                for add in add_users:
                    potential_replaceable_view = self._find_exclusive_user_of_type(add, ttnn.experimental.view)
                    if potential_replaceable_view != None:
                        gelu = self._find_single_user_of_type(potential_replaceable_view, ttnn.gelu)
                        relu = self._find_single_user_of_type(potential_replaceable_view, ttnn.relu)
                        silu = self._find_single_user_of_type(potential_replaceable_view, ttnn.silu)
                        activation = (None, None)
                        
                        if gelu:
                            activation = ('gelu', gelu)
                        elif relu:
                            activation = ('relu', relu)
                        elif silu:
                            activation = ('silu', silu)
                        
                        if activation[0] is None:
                            potential_replaceable_view = None
                        matches.append((from_torch, transpose, matmul, from_torch_2, add, potential_replaceable_view, activation))

        return matches

    def replace_linear(self):
        matches = self.match_linear_pattern()

        for match in matches:
            from_torch, transpose, matmul, from_torch_2, add, view, activation = match
            
            # please notice that if this has no transformation, I want to keep the last view node
            with self.gm.graph.inserting_after(activation[1] if activation[0] else add):
                fused_node = self.gm.graph.call_function(
                    ttnn.linear,
                    args=(matmul.args[0], from_torch),
                    kwargs={
                        'transpose_b': True,
                        'bias': from_torch_2,
                        'activation': activation[0] if activation[0] else None
                    }
                )

                # Connect output to the next node
                (activation[1] if activation[0] else add).replace_all_uses_with(fused_node)

            # Remove old nodes in reverse order to handle dependencies
            nodes_to_remove = [
                activation[1] if activation[0] else None,
                view if activation[0] else None,
                add,
                matmul,
                transpose
            ]
            self.safe_remove_nodes(nodes_to_remove)

        self.gm.graph.lint()
        self.gm.recompile()
        return matches

    def match_pattern(self) -> List[Tuple[torch.fx.Node, ...]]:
        """Implementation of abstract method from base class."""
        return self.match_linear_pattern()

    def replace_pattern(self, matches: List[Tuple[torch.fx.Node, ...]]) -> None:
        """Implementation of abstract method from base class."""
        self.replace_linear()


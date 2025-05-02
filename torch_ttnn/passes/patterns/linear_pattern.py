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
        Match the linear pattern: arg -> transpose -> matmul -> add(arg_2) -> view -> [activation] -> [view2]
        where activation can be gelu, relu, or silu (optional), followed by an optional second view.
        Returns a list of tuples containing the matched nodes.
        """
        matches = []

        # Find all transpose nodes
        transpose_nodes = self._find_nodes_of_type(ttnn.transpose)

        for transpose in transpose_nodes:
            # The input to transpose can be any node (arg)
            arg = transpose.args[0] if len(transpose.args) > 0 else None
            if arg is None:
                continue

            # Find matmul operation using transpose
            matmul = self._find_single_user_of_type(transpose, ttnn.matmul)
            if not matmul or not self._is_node_in_args(transpose, matmul):
                continue

            # Look for add operation that uses matmul and any other node as bias (arg_2)
            add = None
            arg_2 = None
            for user in matmul.users:
                if self._is_ttnn_op(user, ttnn.add):
                    # Find the other argument to add (not matmul)
                    for possible_arg_2 in user.args:
                        if possible_arg_2 is not matmul:
                            add = user
                            arg_2 = possible_arg_2
                            break
                if add is not None:
                    break

            if add is None or arg_2 is None:
                continue

            # in ttnn.linear, B can't be batched and have bias
            # in this case, B is the one that is going to be transposed
            shape = arg.meta["tensor_meta"].shape
            batched = False
            if len(shape) > 2:
                dims_to_check = shape[: 1 if len(shape) == 3 else 2]
                for dim in dims_to_check:
                    batched |= dim != 1

            if batched:
                continue

            # For each valid add operation, look for view and optional activation
            potential_replaceable_view = self._find_exclusive_user_of_type(add, ttnn.experimental.view)
            if potential_replaceable_view is not None:
                gelu = self._find_single_user_of_type(potential_replaceable_view, ttnn.gelu)
                relu = self._find_single_user_of_type(potential_replaceable_view, ttnn.relu)
                silu = self._find_single_user_of_type(potential_replaceable_view, ttnn.silu)
                activation = (None, None)

                if gelu:
                    activation = ("gelu", gelu)
                elif relu:
                    activation = ("relu", relu)
                elif silu:
                    activation = ("silu", silu)

                if activation[0] is None:
                    potential_replaceable_view = None
                matches.append((transpose, matmul, add, potential_replaceable_view, activation))

        return matches

    def replace_linear(self, matches: List[Tuple[torch.fx.Node, ...]]):
        for match in matches:
            transpose, matmul, add, view, activation = match

            bias_arg = add.args[1] if add.args[0] is matmul else add.args[0]
            # If there is no activation, keep the last view node
            with self.gm.graph.inserting_after(activation[1] if activation[0] else add):
                fused_node = self.gm.graph.call_function(
                    ttnn.linear,
                    args=(matmul.args[0], transpose.args[0]),
                    kwargs={
                        "transpose_b": True,
                        "bias": bias_arg,
                        "activation": activation[0] if activation[0] else None,
                    },
                )

                # Connect output to the next node
                (activation[1] if activation[0] else add).replace_all_uses_with(fused_node)

            # Remove old nodes in reverse order to handle dependencies
            nodes_to_remove = [
                activation[1] if activation[0] else None,
                view if activation[0] else None,
                add,
                matmul,
                transpose,
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
        self.replace_linear(matches)

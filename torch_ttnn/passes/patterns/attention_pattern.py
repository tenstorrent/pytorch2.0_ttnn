# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0

import torch
import ttnn
import operator
from torch.fx import Node
from torch_ttnn.passes.patterns.pattern_matcher_base import PatternMatcherBase
from typing import List, Tuple


class AttentionPatterns(PatternMatcherBase):
    """Pattern matcher for attention operations."""

    def match_pattern(self) -> List[Tuple[torch.fx.Node, ...]]:
        """
        Match the attention pattern:
        linear -> view -> reshape -> permute -> view -> matmul(q, k) -> view -> softmax -> view -> matmul(softmax, v)

        Returns a list of tuples: (q_linear, q_view1, q_reshape, q_permute, q_view2,
                                 k_linear, k_view1, k_reshape, k_permute, k_transpose, k_view2,
                                 v_linear, v_view1, v_reshape, v_permute, v_view2,
                                 matmul_qk, view1, softmax, view2, matmul_sv, attn_mask, scale)
        """
        matches = []

        # Find all potential QKV candidates
        query_candidates = self._find_query_candidates()
        key_candidates = self._find_key_candidates()
        value_candidates = self._find_value_candidates()

        # For each query candidate, try to find matching key and value candidates
        for q_candidate in query_candidates:
            q_linear, q_view1, q_reshape, q_permute, q_view2, q_matmul = q_candidate

            # Find matching key candidate where the matmul connects q and k
            for k_candidate in key_candidates:
                k_linear, k_view1, k_reshape, k_permute, k_transpose, k_view2, k_matmul = k_candidate

                # Check if this is the QK matmul
                if k_matmul is not q_matmul:
                    continue

                # Check if QK matmul output goes to a view
                view1 = self._find_exclusive_user_of_type(q_matmul, ttnn.experimental.view)
                if not view1:
                    continue

                # Check if view output goes to softmax and get the mask if it exists
                softmax = self._find_exclusive_user_of_type(view1, ttnn.transformer.attention_softmax_)
                if not softmax:
                    continue

                # Get attention mask if it exists (it would be an additional argument to softmax)
                attn_mask = softmax.kwargs.get("attention_mask")
                # Get scale if it exists in kwargs
                head_size = softmax.kwargs.get("head_size")
                scale = 1.0 / (head_size**0.5) if head_size is not None else None

                # Check if softmax output goes to a view
                view2 = self._find_exclusive_user_of_type(softmax, ttnn.experimental.view)
                if not view2:
                    continue

                # Find matching value candidate
                for v_candidate in value_candidates:
                    v_linear, v_view1, v_reshape, v_permute, v_view2, v_matmul = v_candidate

                    # Check if view output goes to matmul with value
                    matmul_sv = self._find_exclusive_user_of_type(view2, ttnn.matmul)
                    if not matmul_sv or matmul_sv is not v_matmul:
                        continue

                    # We found a complete attention pattern
                    matches.append(
                        (
                            q_linear,
                            q_view1,
                            q_reshape,
                            q_permute,
                            q_view2,
                            k_linear,
                            k_view1,
                            k_reshape,
                            k_permute,
                            k_transpose,
                            k_view2,
                            v_linear,
                            v_view1,
                            v_reshape,
                            v_permute,
                            v_view2,
                            q_matmul,
                            view1,
                            softmax,
                            view2,
                            matmul_sv,
                            attn_mask,
                            scale,
                        )
                    )

        return matches

    def replace_pattern(self, matches: List[Tuple[torch.fx.Node, ...]]) -> None:
        for match in matches:
            (
                q_linear,
                q_view1,
                q_reshape,
                q_permute,
                q_view2,
                k_linear,
                k_view1,
                k_reshape,
                k_permute,
                k_transpose,
                k_view2,
                v_linear,
                v_view1,
                v_reshape,
                v_permute,
                v_view2,
                matmul_qk,
                view1,
                softmax,
                view2,
                matmul_sv,
                attn_mask,
                scale,
            ) = match

            #
            head_size = softmax.kwargs.get("head_size")
            num_heads = q_view1.meta["val"].shape[-1] // head_size
            with self.gm.graph.inserting_after(matmul_sv):
                # Lets concatenate the qkv tensors for weights and biases
                concatenated_qkv_weights_node = self.gm.graph.call_function(
                    ttnn.concat,
                    args=([q_linear.args[1], k_linear.args[1], v_linear.args[1]], -1),  # Input tensors
                    kwargs={},
                )

            with self.gm.graph.inserting_after(concatenated_qkv_weights_node):
                # _find_qkv_pattern ensures that the bias is not None
                # this is not entirely true, because the bias is optional
                # but since I want to control the replacement, I will make it a requirement
                # for now.
                q_bias = q_linear.kwargs["bias"]
                k_bias = k_linear.kwargs["bias"]
                v_bias = v_linear.kwargs["bias"]

                # concatenate the biases
                concatenated_qkv_biases_node = self.gm.graph.call_function(
                    ttnn.concat,
                    args=([q_bias, k_bias, v_bias], -1),  # Input tensors
                    kwargs={},
                )

            with self.gm.graph.inserting_after(concatenated_qkv_biases_node):
                qvk_node = self.gm.graph.call_function(
                    ttnn.linear,
                    args=(
                        q_linear.args[0],
                        concatenated_qkv_weights_node,
                    ),
                    kwargs={"bias": concatenated_qkv_biases_node},
                )

            with self.gm.graph.inserting_after(qvk_node):
                shape = list(q_view1.meta["val"].shape)
                shape[-1] = shape[-1] * 3

                linear_view_node = self.gm.graph.call_function(
                    ttnn.experimental.view,
                    args=(qvk_node, shape),
                    kwargs={},
                )

            with self.gm.graph.inserting_after(linear_view_node):
                # Time to split the qvk into q, k, v
                split_qkv_node = self.gm.graph.call_function(
                    ttnn.transformer.split_query_key_value_and_split_heads,
                    args=(linear_view_node, None),  # Input tensors as tuple
                    kwargs={"num_heads": num_heads, "transpose_key": False},
                )

            # Hack: TTNN is expecting the mask in a format [b, 1, s, s]
            # but what we have is [b, 1, 1, s]
            # so in order to do an operation that is fast and does the trick
            # we will insert this
            # ttnn_mask = ttnn_decorators_ttnn_view(ttnn_multiply, [1, 1, 256, 1])
            # ttnn_mask = ttnn.add(ttnn_mask, ttnn_multiply) # <---- hack

            mask_new_shape = list(attn_mask.meta["val"].shape)
            mask_new_shape[2], mask_new_shape[3] = mask_new_shape[3], mask_new_shape[2]
            with self.gm.graph.inserting_after(split_qkv_node):
                get_q_node = self.gm.graph.call_function(
                    operator.getitem,
                    args=(split_qkv_node, 0),
                    kwargs={},
                )
            with self.gm.graph.inserting_after(get_q_node):
                get_k_node = self.gm.graph.call_function(
                    operator.getitem,
                    args=(split_qkv_node, 1),
                    kwargs={},
                )

            with self.gm.graph.inserting_after(get_k_node):
                get_v_node = self.gm.graph.call_function(
                    operator.getitem,
                    args=(split_qkv_node, 2),
                    kwargs={},
                )

            with self.gm.graph.inserting_after(get_v_node):
                mask_node = self.gm.graph.call_function(
                    ttnn.experimental.view,
                    args=(attn_mask, mask_new_shape),
                    kwargs={},
                )

            with self.gm.graph.inserting_after(mask_node):
                mask_hacked_node = self.gm.graph.call_function(
                    ttnn.add,
                    args=(mask_node, attn_mask),  # Input tensors
                    kwargs={},
                )

            with self.gm.graph.inserting_after(mask_hacked_node):
                kwargs = {}
                if attn_mask is not None:
                    kwargs["attn_mask"] = mask_hacked_node
                    kwargs["is_causal"] = False
                if scale is not None:
                    kwargs["scale"] = scale

                # Create the fused attention node with weights and biases
                fused_node = self.gm.graph.call_function(
                    ttnn.transformer.scaled_dot_product_attention,
                    args=(
                        get_q_node,
                        get_k_node,
                        get_v_node,
                    ),  # Input tensors
                    kwargs=kwargs,
                )
                matmul_sv.replace_all_uses_with(fused_node)

            # Remove old nodes in reverse order
            nodes_to_remove = [
                matmul_sv,
                view2,
                softmax,
                view1,
                matmul_qk,
                q_view2,
                q_permute,
                q_reshape,
                k_view2,
                k_transpose,
                k_permute,
                k_reshape,
                v_view2,
                v_permute,
                v_reshape,
                q_view1,
                k_view1,
                v_view1,
                q_linear,
                k_linear,
                v_linear,
            ]
            self.safe_remove_nodes(nodes_to_remove)

        self.gm.graph.lint()
        self.gm.recompile()
        return matches

    def _find_qkv_pattern(self, linear, require_transpose=False, matmul_arg_idx=0):
        """Common helper method for finding query/key/value patterns.

        Args:
            linear: The linear node to start from
            require_transpose: Whether to require a transpose operation
            matmul_arg_idx: Which argument of matmul should be the view2 node (0 for query, 1 for key/value)

        Returns:
            Tuple of nodes if pattern matches, None otherwise
        """

        # Even though the bias is optional, I want to restrict the pattern to only include nodes with a bias
        if linear.kwargs["bias"] is None:
            return None

        view1 = self._find_exclusive_user_of_type(linear, ttnn.experimental.view)
        if not view1:
            return None

        reshape = self._find_exclusive_user_of_type(view1, ttnn.reshape)
        if not reshape:
            return None

        permute = self._find_exclusive_user_of_type(reshape, ttnn.permute)
        if not permute:
            return None

        if require_transpose:
            transpose = self._find_exclusive_user_of_type(permute, ttnn.transpose)
            if not transpose:
                return None
            view2 = self._find_exclusive_user_of_type(transpose, ttnn.experimental.view)
        else:
            view2 = self._find_exclusive_user_of_type(permute, ttnn.experimental.view)

        if not view2:
            return None

        matmul = self._find_exclusive_user_of_type(view2, ttnn.matmul)
        if not matmul or matmul.args[matmul_arg_idx] is not view2:
            return None

        if require_transpose:
            return (linear, view1, reshape, permute, transpose, view2, matmul)
        return (linear, view1, reshape, permute, view2, matmul)

    def _find_query_candidates(self):
        query_candidates = []
        linear_nodes = self._find_nodes_of_type(ttnn.linear)
        for linear in linear_nodes:
            candidate = self._find_qkv_pattern(linear, require_transpose=False, matmul_arg_idx=0)
            if candidate:
                query_candidates.append(candidate)
        return query_candidates

    def _find_key_candidates(self):
        key_candidates = []
        linear_nodes = self._find_nodes_of_type(ttnn.linear)
        for linear in linear_nodes:
            candidate = self._find_qkv_pattern(linear, require_transpose=True, matmul_arg_idx=1)
            if candidate:
                key_candidates.append(candidate)
        return key_candidates

    def _find_value_candidates(self):
        value_candidates = []
        linear_nodes = self._find_nodes_of_type(ttnn.linear)
        for linear in linear_nodes:
            candidate = self._find_qkv_pattern(linear, require_transpose=False, matmul_arg_idx=1)
            if candidate:
                value_candidates.append(candidate)
        return value_candidates

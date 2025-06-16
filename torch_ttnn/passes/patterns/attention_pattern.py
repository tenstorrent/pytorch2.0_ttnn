# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0

import torch
import ttnn
import operator
from torch._guards import detect_fake_mode
from torch_ttnn.passes.patterns.pattern_matcher_base import PatternMatcherBase
from typing import List, Tuple


class AttentionPatterns(PatternMatcherBase):
    """Pattern matcher for attention operations."""

    def match_pattern(self) -> List[Tuple[torch.fx.Node, ...]]:
        """
        Match the attention pattern:
        linear -> view -> reshape -> permute -> view -> matmul(q, k) -> view -> softmax -> view -> matmul(softmax, v) -> view -> view -> permute -> reshape -> view

        Returns a list of tuples: (q_linear, q_view1, q_reshape, q_permute, q_view2,
                                 k_linear, k_view1, k_reshape, k_permute, k_transpose, k_view2,
                                 v_linear, v_view1, v_reshape, v_permute, v_view2,
                                 matmul_qk, view1, softmax, view2, matmul_sv, view3, permute, reshape, view5,
                                 attn_mask, scale)
        """
        matches = []

        # Find all potential QKV candidates
        query_candidates = self._find_qkv_candidates(False, 0)
        key_candidates = self._find_qkv_candidates(True, 1)
        value_candidates = self._find_qkv_candidates(False, 1)

        # For each query candidate, try to find matching key and value candidates
        for q_candidate in query_candidates:
            q_linear, q_view1, q_reshape, q_permute, q_view2, q_matmul = q_candidate

            # Find matching key candidate where the matmul connects q and k
            for k_candidate in key_candidates:
                k_linear, k_view1, k_reshape, k_permute, k_transpose, k_view2, k_matmul = k_candidate

                # check that the weights have the same shape
                if q_linear.args[1].meta["val"].shape != k_linear.args[1].meta["val"].shape:
                    continue

                # Check if this is the QK matmul
                if k_matmul is not q_matmul:
                    continue

                # Check if QK matmul output goes to a view
                view1 = self._find_exclusive_user_of_type(q_matmul, ttnn.experimental.view)
                if not view1:
                    continue

                # Check if view output goes to softmax and get the mask if it exists
                softmax = self._find_exclusive_user_of_type(view1, ttnn.transformer.attention_softmax)
                if not softmax:
                    continue

                # Get attention mask if it exists (it would be an additional argument to softmax)
                attn_mask = softmax.kwargs.get("attention_mask")
                # Get scale if it exists in kwargs
                head_size = softmax.kwargs.get("head_size")

                # If head_size is not provided, we cannot proceed
                # at least for now...
                if not head_size:
                    continue

                scale = 1.0 / (head_size**0.5) if head_size is not None else None

                # Check if softmax output goes to a view
                view2 = self._find_exclusive_user_of_type(softmax, ttnn.experimental.view)
                if not view2:
                    continue

                # Find matching value candidate
                for v_candidate in value_candidates:
                    v_linear, v_view1, v_reshape, v_permute, v_view2, v_matmul = v_candidate

                    # check that the weights have the same shape
                    if q_linear.args[1].meta["val"].shape != v_linear.args[1].meta["val"].shape:
                        continue

                    # Check if view output goes to matmul with value
                    matmul_sv = self._find_exclusive_user_of_type(view2, ttnn.matmul)
                    if not matmul_sv or matmul_sv is not v_matmul:
                        continue

                    # Check for additional operations after matmul_sv
                    view3 = self._find_exclusive_user_of_type(matmul_sv, ttnn.experimental.view)
                    if not view3:
                        continue

                    permute = self._find_exclusive_user_of_type(view3, ttnn.permute)
                    if not permute:
                        continue

                    reshape = self._find_exclusive_user_of_type(permute, ttnn.reshape)
                    if not reshape:
                        continue

                    view5 = self._find_exclusive_user_of_type(reshape, ttnn.experimental.view)
                    if not view5:
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
                            view3,
                            permute,
                            reshape,
                            view5,
                            attn_mask,
                            scale,
                        )
                    )

        return matches

    def python_split_qkv(self, input_tensor, kv_input_tensor, num_heads, num_kv_heads=None, transpose_key=True):
        if kv_input_tensor is not None:
            input_tensor = torch.cat([input_tensor, kv_input_tensor], dim=-1)

        if num_kv_heads is None:
            num_kv_heads = num_heads

        batch_size, sequence_size, hidden_size = input_tensor.shape
        # Subtract head sizes for key and value
        head_size = (hidden_size) // (num_heads + num_kv_heads * 2)
        tensor = torch.reshape(input_tensor, (batch_size, sequence_size, num_heads + num_kv_heads * 2, head_size))
        query, key, value = (
            tensor[..., :num_heads, :],
            tensor[..., num_heads : num_heads + num_kv_heads, :],
            tensor[..., num_heads + num_kv_heads :, :],
        )

        query = torch.reshape(query, (batch_size, sequence_size, num_heads, head_size))
        key = torch.reshape(key, (batch_size, sequence_size, num_kv_heads, head_size))
        value = torch.reshape(value, (batch_size, sequence_size, num_kv_heads, head_size))

        query = torch.permute(query, (0, 2, 1, 3)).contiguous().clone()
        key = torch.permute(key, (0, 2, 1, 3)).contiguous().clone()
        value = torch.permute(value, (0, 2, 1, 3)).contiguous().clone()
        if transpose_key:
            key = torch.permute(key, (0, 1, 3, 2)).contiguous().clone()

        return (query, key, value)

    def call_function_update_meta(self, target, args=(), kwargs={}):
        new_node = self.gm.graph.call_function(target, args, kwargs)

        if target == ttnn.transpose:
            new_val = torch.transpose(self._get_val(args[0]), args[1], args[2])
        elif target == ttnn.concat:
            vals = list(map(self._get_val, args[0]))
            new_val = torch.concat(vals, args[1])
        elif target == ttnn.linear:  # TODO
            new_val = torch.matmul(self._get_val(args[0]), self._get_val(args[1]))
        elif target == ttnn.transformer.split_query_key_value_and_split_heads:  # TODO
            new_val = self.python_split_qkv(*map(self._get_val, args), **kwargs)
        elif target == ttnn.matmul:
            new_val = torch.matmul(self._get_val(args[0]), self._get_val(args[1]))
        elif target == ttnn.transformer.attention_softmax:
            new_val = self._get_val(args[0])
        elif target == ttnn.transformer.concatenate_heads:
            old_shape = self._get_val(args[0]).shape
            new_val = torch.reshape(self._get_val(args[0]), (old_shape[0], old_shape[2], old_shape[1] * old_shape[3]))
        elif target == ttnn.experimental.view:
            new_val = torch.reshape(self._get_val(args[0]), args[1])
        elif target == operator.getitem:
            new_val = self._get_val(args[0])[args[1]]
        else:
            new_val = self._get_val(new_node)

        new_node.meta["val"] = new_val
        new_node.meta["tensor_meta"] = new_val

        return new_node

    def _get_val(self, obj):
        if not isinstance(obj, torch.fx.node.Node):
            return obj
        if obj.op == "get_attr":
            val = getattr(self.gm, obj.target)
            fake_mode = detect_fake_mode()
            if isinstance(val, torch.Tensor) and fake_mode is not None:
                val = fake_mode.fake_tensor_converter.from_real_tensor(fake_mode, val)
            return val
        return obj.meta["val"]

    # Hack! TTNN does not support concat with tensors of 1D
    # https://github.com/tenstorrent/tt-metal/issues/20205
    # bias is 1D tensor, so we need to make it 2D
    def _hack_1D_bias(self, bias_node):
        """Reshape bias node to 2D Shape

        Args:
            bias_node: The bias node to reshape

        Returns:
            The reshaped node
        """
        new_bias_node = self.call_function_update_meta(
            ttnn.experimental.view,
            args=(bias_node, (1, -1)),
            kwargs={},
        )

        return new_bias_node

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
                view3,
                permute,
                reshape,
                view5,
                attn_mask,
                scale,
            ) = match

            head_size = softmax.kwargs.get("head_size")
            num_heads = q_view1.meta["val"].shape[-1] // head_size

            with self.gm.graph.inserting_before(view5):
                transposed_q_weights_node = self.call_function_update_meta(
                    ttnn.transpose,
                    args=(q_linear.args[1], -2, -1),
                )

                transposed_k_weights_node = self.call_function_update_meta(
                    ttnn.transpose,
                    args=(k_linear.args[1], -2, -1),
                    kwargs={},
                )

                transposed_v_weights_node = self.call_function_update_meta(
                    ttnn.transpose,
                    args=(v_linear.args[1], -2, -1),
                    kwargs={},
                )

                # Lets concatenate the qkv tensors for weights and biases
                concatenated_qkv_weights_node = self.call_function_update_meta(
                    ttnn.concat,
                    args=([transposed_q_weights_node, transposed_k_weights_node, transposed_v_weights_node], -1),
                    kwargs={},
                )

                # _find_qkv_pattern ensures that the bias is not None
                # this is not entirely true, because the bias is optional
                # but since I want to control the replacement, I will make it a requirement
                # for now.
                q_bias = q_linear.kwargs["bias"]
                k_bias = k_linear.kwargs["bias"]
                v_bias = v_linear.kwargs["bias"]

                # Reshape biases if needed
                q_bias_node = self._hack_1D_bias(q_bias)
                k_bias_node = self._hack_1D_bias(k_bias)
                v_bias_node = self._hack_1D_bias(v_bias)

                # concatenate the biases
                concatenated_qkv_biases_node = self.call_function_update_meta(
                    ttnn.concat,
                    args=([q_bias_node, k_bias_node, v_bias_node], -1),
                    kwargs={},
                )

                qvk_node = self.call_function_update_meta(
                    ttnn.linear,
                    args=(
                        q_linear.args[0],
                        concatenated_qkv_weights_node,
                    ),
                    kwargs={"bias": concatenated_qkv_biases_node},
                )

                shape = list(q_view1.meta["val"].shape)
                shape[-1] = shape[-1] * 3

                linear_view_node = self.call_function_update_meta(
                    ttnn.experimental.view,
                    args=(qvk_node, shape),
                    kwargs={},
                )

                # Time to split the qvk into q, k, v
                split_qkv_node = self.call_function_update_meta(
                    ttnn.transformer.split_query_key_value_and_split_heads,
                    args=(linear_view_node, None),
                    kwargs={"num_heads": num_heads, "transpose_key": True},
                )

                get_q_node = self.call_function_update_meta(
                    operator.getitem,
                    args=(split_qkv_node, 0),
                    kwargs={},
                )

                get_k_node = self.call_function_update_meta(
                    operator.getitem,
                    args=(split_qkv_node, 1),
                    kwargs={},
                )

                get_v_node = self.call_function_update_meta(
                    operator.getitem,
                    args=(split_qkv_node, 2),
                    kwargs={},
                )

                attention_scores_node = self.call_function_update_meta(
                    ttnn.matmul,
                    args=(get_q_node, get_k_node),
                )

                attention_probabilities_node = self.call_function_update_meta(
                    ttnn.transformer.attention_softmax,
                    args=(attention_scores_node,),
                    kwargs={
                        "attention_mask": attn_mask,
                        "head_size": head_size,
                    },
                )

                matmul_sv_node = self.call_function_update_meta(
                    ttnn.matmul,
                    args=(attention_probabilities_node, get_v_node),
                    kwargs={},
                )

                concatenated_head_node = self.call_function_update_meta(
                    ttnn.transformer.concatenate_heads,
                    args=(matmul_sv_node,),
                    kwargs={},
                )

            view5.replace_all_uses_with(concatenated_head_node)

            # Remove old nodes in reverse order
            nodes_to_remove = [
                view5,
                reshape,
                permute,
                view3,
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

    def _find_qkv_candidates(self, require_transpose, matmul_arg_idx):
        key_candidates = []
        linear_nodes = self._find_nodes_of_type(ttnn.linear)
        for linear in linear_nodes:
            candidate = self._find_qkv_pattern(
                linear, require_transpose=require_transpose, matmul_arg_idx=matmul_arg_idx
            )

            if candidate:
                key_candidates.append(candidate)
        return key_candidates

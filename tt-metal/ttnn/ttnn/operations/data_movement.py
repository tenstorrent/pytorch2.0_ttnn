# SPDX-FileCopyrightText: © 2023 Tenstorrent Inc.

# SPDX-License-Identifier: Apache-2.0

from typing import Tuple, Union, List

import ttnn
import ttnn.decorators


def _preprocess_golden_function_inputs(args, kwargs):
    input_tensor, args, kwargs = ttnn.reflection.pop_argument("input_tensor", args, kwargs)
    padding, args, kwargs = ttnn.reflection.pop_argument("padding", args, kwargs)

    if len(padding) != len(input_tensor.shape):
        raise RuntimeError("ttnn.pad: padding must be the same length as the input tensor rank")

    for start, end in padding:
        if start < 0 or end < 0:
            raise RuntimeError("ttnn.pad: padding must be non-negative")

    pad_start = tuple(start for start, _ in padding)
    *_, pad_start_height, pad_start_width = pad_start
    if input_tensor.layout == ttnn.TILE_LAYOUT:
        if pad_start_height % ttnn.TILE_SIZE != 0 or pad_start_width % ttnn.TILE_SIZE != 0:
            raise RuntimeError(
                "ttnn.pad: padding end must be a multiple of the tile size on height and width for a tensor in tile layout"
            )

    pad_end = tuple(end for _, end in padding)
    *_, pad_end_height, pad_end_width = pad_end
    if input_tensor.layout == ttnn.TILE_LAYOUT:
        if pad_end_height % ttnn.TILE_SIZE != 0 or pad_end_width % ttnn.TILE_SIZE != 0:
            raise RuntimeError(
                "ttnn.pad: padding end must be a multiple of the tile size on height and width for a tensor in tile layout"
            )

    input_tensor = ttnn.to_torch(input_tensor)

    return (input_tensor, padding, *args), kwargs


def _golden_function(input_tensor: ttnn.Tensor, padding, value):
    import torch

    torch_padding = []
    for dimension in reversed(padding):
        torch_padding.append(dimension[0])
        torch_padding.append(dimension[1])
    return torch.nn.functional.pad(input_tensor, pad=torch_padding, mode="constant", value=value)


def _postprocess_golden_function_outputs(output_tensor, args, kwargs):
    output_tensor = ttnn.decorators.default_postprocess_golden_function_outputs(output_tensor, args, kwargs)
    # Padding always turns the intended shape to the shape with tile padding. For simplicity of the operation
    output_tensor = ttnn.reshape(output_tensor, shape=output_tensor.padded_shape)
    return output_tensor


ttnn.attach_golden_function(
    ttnn.pad,
    golden_function=_golden_function,
    preprocess_golden_function_inputs=_preprocess_golden_function_inputs,
    postprocess_golden_function_outputs=_postprocess_golden_function_outputs,
)


def _golden_function(input_tensor: ttnn.Tensor, order: Tuple[int, ...], **_):
    if len(input_tensor.shape) != len(order):
        raise RuntimeError(
            "The number of dimensions in the tensor input does not match the length of the desired ordering"
        )

    return input_tensor.permute(order).contiguous().clone()


def _golden_function(input_tensor, dims, **_):
    import torch

    return torch.permute(input_tensor, dims)


ttnn.attach_golden_function(ttnn.permute, golden_function=_golden_function)


def _golden_function(tensors, dim=0, groups=1, **_):
    import torch

    def grouped_concat(activations, residuals, groups):
        """
        Concatenate activations and residuals with flexible interleaving based on groups.

        Args:
            activations (torch.Tensor): Activation tensor with shape [N, H, W, C].
            residuals (torch.Tensor): Residual tensor with shape [N, H, W, C].
            groups (int): Number of groups to split channels into.

        Returns:
            torch.Tensor: Concatenated tensor with interleaved groups.
        """

        assert (
            activations.shape[:-1] == residuals.shape[:-1]
        ), "Activations and residuals must have the same shape in all dims but -1"

        N, H, W, activation_channels = activations.shape
        assert activation_channels % groups == 0, "Channel count must be divisible by the number of groups"

        N, H, W, residual_channels = residuals.shape
        assert residual_channels % groups == 0, "Channel count must be divisible by the number of groups"

        act_groups = activations.view(N, H, W, groups, activation_channels // groups)
        res_groups = residuals.view(N, H, W, groups, residual_channels // groups)

        # Interleave activations and residuals along the channel axis
        interleaved = torch.cat([act_groups, res_groups], dim=-1)  # Shape: [N, H, W, groups, 2 * group_size]

        # Reshape to combine groups and channels correctly
        interleaved = interleaved.permute(0, 1, 2, 3, 4).reshape(N, H, W, residual_channels + activation_channels)

        return interleaved

    return grouped_concat(tensors[0], tensors[1], groups=groups) if groups > 1 else torch.concat(tensors, dim)


ttnn.attach_golden_function(
    ttnn.concat,
    golden_function=_golden_function,
)


def _golden_function(tensor, repeats, dim=0, **_):
    import torch

    return torch.repeat_interleave(tensor, repeats, dim=dim)


ttnn.attach_golden_function(ttnn.repeat_interleave, golden_function=_golden_function)


def _golden_function(tensor, shape, **_):
    return tensor.repeat(shape[0], shape[1], shape[2], shape[3])


ttnn.attach_golden_function(ttnn.repeat, golden_function=_golden_function)


def _golden_function(input_tensor: ttnn.Tensor, scale_factor: Tuple[float, float], **_):
    import torch

    input_tensor = input_tensor.permute(0, 3, 1, 2)
    ret = torch.nn.functional.upsample(input_tensor, scale_factor=scale_factor)
    ret = ret.permute(0, 2, 3, 1)
    return ret


ttnn.attach_golden_function(
    ttnn.upsample,
    golden_function=_golden_function,
)

__all__ = []

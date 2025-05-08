# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import ttnn
import torch

from torch_ttnn.utils import TtnnDevice

run_once_count = 0
run_once_ans = tuple()


class mutable_schema:
    is_mutable = True


@torch.fx.wrap
def run_once(fun, *args):
    global run_once_count
    global run_once_ans

    if run_once_count > 0:
        return run_once_ans
    print("running once!")
    run_once_ans = fun(*args)
    run_once_count += 1
    return run_once_ans


@torch.fx.wrap
def clone(t):
    return ttnn.clone(t, memory_config=t.memory_config(), dtype=t.dtype)


@torch.fx.wrap
def repeat(t, sizes):
    return ttnn.repeat(t, ttnn.Shape(sizes))


# Helper function to pack multiple values into a tuple on the graph
@torch.fx.wrap
def pack_to_tuple(*args):
    return tuple(args)


@torch.fx.wrap
def move_to_host(device_tensor, layout):
    if len(ttnn.get_device_tensors(device_tensor)) > 1:
        device_tensor = ttnn.get_device_tensors(device_tensor)[0]
    host_tensor = ttnn.from_device(device_tensor)
    return ttnn.to_layout(host_tensor, layout)


@torch.fx.wrap
def conv(
    input_tensor,
    weight_tensor,
    bias_tensor,
    batch_size,
    in_channels,
    out_channels,
    in_spatial_shape,
    kernel_spatial_shape,
    stride,
    padding,
    dilation,
    groups,
    device,
    transposed,
    output_padding=None,
):
    if len(in_spatial_shape) == 1:
        # TODO(tt-metal#16258): conv1d API doesn't support transposed yet
        assert not transposed, "conv1d doesn't support transposed yet"
        return ttnn.conv1d(
            input_tensor=input_tensor,
            weight_tensor=weight_tensor,
            bias_tensor=bias_tensor,
            batch_size=batch_size,
            in_channels=in_channels,
            out_channels=out_channels,
            input_length=in_spatial_shape[0],
            kernel_size=kernel_spatial_shape[0],
            stride=stride[0],
            padding=padding[0],
            dilation=dilation[0],
            groups=groups,
            device=device,
        )
    if len(in_spatial_shape) == 2:
        in_h, in_w = in_spatial_shape
        if transposed:
            return ttnn.conv_transpose2d(
                input_tensor=input_tensor,
                weight_tensor=weight_tensor,
                bias_tensor=bias_tensor,
                batch_size=batch_size,
                in_channels=in_channels,
                out_channels=out_channels,
                input_height=in_h,
                input_width=in_w,
                kernel_size=kernel_spatial_shape,
                stride=stride,
                padding=padding,
                output_padding=output_padding,
                dilation=dilation,
                groups=groups,
                device=device,
            )
        else:
            assert output_padding is None, "conv2d has no output padding"
            return ttnn.conv2d(
                input_tensor=input_tensor,
                weight_tensor=weight_tensor,
                bias_tensor=bias_tensor,
                batch_size=batch_size,
                in_channels=in_channels,
                out_channels=out_channels,
                input_height=in_h,
                input_width=in_w,
                kernel_size=kernel_spatial_shape,
                stride=stride,
                padding=padding,
                dilation=dilation,
                groups=groups,
                device=device,
            )
    assert False, "unsupported conv shape"


@torch.fx.wrap
def roll(tensor, input_shape, shifts, dims):
    rolled_tensor = tensor
    for shift, dim in zip(shifts, dims):
        # slice tensor into two parts and concat them in reverse order
        end = (input_shape[dim] - shift) % input_shape[dim]

        # part1 = tensor[..., :end]
        slice_start, slice_end = [0] * len(input_shape), list(input_shape)
        slice_end[dim] = end
        sub_tensor1 = ttnn.slice(rolled_tensor, slice_start, slice_end)

        # part2 = tensor[..., end:]
        slice_start, slice_end = [0] * len(input_shape), list(input_shape)
        slice_start[dim] = end
        sub_tensor2 = ttnn.slice(rolled_tensor, slice_start, slice_end)

        # concat([part2, part1], dim)
        rolled_tensor = ttnn.concat([sub_tensor2, sub_tensor1], dim)

    return rolled_tensor


@torch.fx.wrap
def stack(tensors, dim, output_shape):
    # Handle negative dims by wrapping around
    dim = (dim + len(output_shape)) % len(output_shape)

    # Create shape for unsqueezed tensors - same as output but with size 1
    # in the stack dimension
    unsqueezed_shape = output_shape.copy()
    unsqueezed_shape[dim] = 1

    # Reshape each input tensor to add the new dimension
    unsqueezed_tensors = []
    for tensor in tensors:
        # TODO: remove when reshape supports tiled uint32 inputs
        if tensor.layout == ttnn.TILE_LAYOUT and tensor.dtype == ttnn.uint32:
            tensor = ttnn.to_layout(tensor, ttnn.ROW_MAJOR_LAYOUT)
        unsqueezed_tensors.append(ttnn.reshape(tensor, unsqueezed_shape))

    # Concatenate all reshaped tensors along the stack dimension
    return ttnn.concat(unsqueezed_tensors, dim)


@torch.fx.wrap
def all(tensor, num_elements):
    """
    Check if all elements in the tensor are non-zero.

    Args:
        tensor (Tensor): The input tensor to check.
        num_elements (int): The number of elements in the tensor.

    Returns:
        bool: True if all elements in the tensor are non-zero, False otherwise.
    """
    # Check if all elements in the tensor are non-zero
    # by comparing the sum of non-zero elements to the total number of elements
    neq_zero = ttnn.ne(tensor, 0)
    total_none_zero = ttnn.sum(neq_zero)
    return ttnn.eq(total_none_zero, num_elements)


"""
replicate_tensor, shard_tensor, and concat_tensor are needed to propagate shape data throughout the computation graph. These wrappers just replicate the shape change that occurs from the actual ttnn ops without requiring access to a TtnnDevice. It is expected that they are substituted back out during the ToTtPass.
TODO: Find a better way to propagate shapes
"""


@torch.fx.wrap
def replicate_tensor(tensor):
    return tensor


@torch.fx.wrap
def shard_tensor(tensor, dim, num_devices):
    return torch.chunk(tensor, num_devices, dim)[0]


@torch.fx.wrap
def concat_tensor(tensor, dim, num_devices):
    sharded_version = [tensor] * num_devices
    return torch.concat(sharded_version, dim)

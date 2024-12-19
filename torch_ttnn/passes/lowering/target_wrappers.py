import ttnn
import torch


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
    host_tensor = ttnn.from_device(device_tensor)
    return ttnn.to_layout(host_tensor, layout)


@torch.fx.wrap
def conv2d(
    input_tensor,
    weight_tensor,
    bias_tensor,
    batch_size,
    in_channels,
    out_channels,
    input_height,
    input_width,
    kernel_size,
    stride,
    padding,
    dilation,
    groups,
    device,
    transposed,
    output_padding=None,
):
    if transposed:
        conv_config = ttnn.Conv2dConfig(
            shard_layout=ttnn.TensorMemoryLayout.HEIGHT_SHARDED,
        )
        output_tensor, _, _, _, _ = ttnn.conv_transpose2d(
            input_tensor=input_tensor,
            weight_tensor=weight_tensor,
            bias_tensor=bias_tensor,
            batch_size=batch_size,
            in_channels=in_channels,
            out_channels=out_channels,
            input_height=input_height,
            input_width=input_width,
            kernel_size=kernel_size,
            stride=stride,
            padding=padding,
            output_padding=output_padding,
            dilation=dilation,
            groups=groups,
            device=device,
            conv_config=conv_config,
        )
    else:
        assert output_padding is None, "conv2d has no output padding"
        output_tensor = ttnn.conv2d(
            input_tensor=input_tensor,
            weight_tensor=weight_tensor,
            bias_tensor=bias_tensor,
            batch_size=batch_size,
            in_channels=in_channels,
            out_channels=out_channels,
            input_height=input_height,
            input_width=input_width,
            kernel_size=kernel_size,
            stride=stride,
            padding=padding,
            dilation=dilation,
            groups=groups,
            device=device,
        )
    return output_tensor


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
        unsqueezed_tensors.append(ttnn.reshape(tensor, unsqueezed_shape))

    # Concatenate all reshaped tensors along the stack dimension
    return ttnn.concat(unsqueezed_tensors, dim)

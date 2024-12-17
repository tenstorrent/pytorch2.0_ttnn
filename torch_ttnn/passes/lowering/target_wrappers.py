import ttnn
import torch


@torch.fx.wrap
def clone(t):
    return ttnn.clone(t, memory_config=t.memory_config(), dtype=t.dtype)


@torch.fx.wrap
def repeat(t, sizes):
    return ttnn.repeat(t, ttnn.Shape(sizes))


@torch.fx.wrap
def is_sharded(tensor):
    return tensor.is_sharded()


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

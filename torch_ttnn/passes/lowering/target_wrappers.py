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
def group_norm(
    input_tensor, input_mask, weight, bias, num_groups, epsilon, inplace, grid_size_x, grid_size_y, shard_shape
):
    grid_coord = ttnn.CoreCoord(grid_size_x - 1, grid_size_y - 1)
    shard_grid = ttnn.CoreRangeSet({ttnn.CoreRange(ttnn.CoreCoord(0, 0), grid_coord)})
    shard_spec = ttnn.ShardSpec(shard_grid, shard_shape, ttnn.ShardOrientation.COL_MAJOR, False)
    sharded_mem_config = ttnn.MemoryConfig(
        ttnn.types.TensorMemoryLayout.BLOCK_SHARDED, ttnn.types.BufferType.L1, shard_spec
    )
    input_tensor_sharded = ttnn.to_memory_config(input_tensor, sharded_mem_config)
    output_tensor = ttnn.group_norm(
        input_tensor_sharded,
        num_groups=num_groups,
        epsilon=epsilon,
        input_mask=input_mask,
        weight=weight,
        bias=bias,
        memory_config=sharded_mem_config,
        core_grid=ttnn.CoreGrid(y=grid_size_y, x=grid_size_x),
        inplace=inplace,
    )

    output_tensor_l1 = ttnn.to_memory_config(output_tensor, ttnn.L1_MEMORY_CONFIG)
    return output_tensor_l1

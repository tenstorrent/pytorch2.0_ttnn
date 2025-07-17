# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from operator import getitem
import ttnn
import torch
import pickle

from torch_ttnn.utils import TtnnDevice

run_once_count = 0
run_once_ans = tuple()


@torch.fx.wrap
@dataclass(frozen=True)
class RunOnceIdx:
    idx: int


@torch.fx.wrap
def run_once(*args):
    global run_once_count
    global run_once_ans

    if run_once_count == 0:
        temp_results = []
        return_results = []
        to_deallocate = []
        temp_idx_to_return_idx = dict()

        def lookup_function(str_name):
            # assume function is of form `ttnn.from_torch`, look up in globals()
            parts = str_name.split(".")
            base = globals()[parts[0]]
            for part in parts[1:]:
                base = getattr(base, part)
            return base

        def lookup_prev_result_idx(maybe_pickled_run_once_idx):
            try:
                run_once_idx = pickle.loads(maybe_pickled_run_once_idx)
                return run_once_idx.idx
            except pickle.UnpicklingError:
                pass
            return None

        def rewrite_args(arg_tuple):
            args = list(arg_tuple)
            for i, arg in enumerate(args):
                if isinstance(arg, (tuple, list, torch.fx.immutable_collections.immutable_list)):
                    original_version = list(arg)
                    decoded_version = [
                        lookup_prev_result_idx(entry) if isinstance(entry, bytes) else None
                        for entry in original_version
                    ]
                    decoded_version = [temp_results[idx] if idx is not None else None for idx in decoded_version]
                    new_arg = [
                        decoded if decoded is not None else original
                        for decoded, original in zip(decoded_version, original_version)
                    ]
                    args[i] = new_arg
                elif isinstance(arg, bytes):
                    maybe_prev_result_idx = lookup_prev_result_idx(arg)
                    if maybe_prev_result_idx is not None:
                        prev_val = temp_results[maybe_prev_result_idx]
                        args[i] = prev_val
            return tuple(args)

        def rewrite_kwargs(kwargs_dict):
            for k, v in kwargs_dict.items():
                if isinstance(v, (tuple, list, torch.fx.immutable_collections.immutable_list)):
                    original_version = list(v)
                    decoded_version = [
                        lookup_prev_result_idx(entry) if isinstance(entry, bytes) else None
                        for entry in original_version
                    ]
                    decoded_version = [temp_results[idx] if idx is not None else None for idx in decoded_version]
                    new_value = [
                        decoded if decoded is not None else original
                        for decoded, original in zip(decoded_version, original_version)
                    ]
                    kwargs_dict[k] = new_value
                elif isinstance(v, bytes):
                    maybe_prev_result_idx = lookup_prev_result_idx(v)
                    if maybe_prev_result_idx is not None:
                        prev_val = temp_results[maybe_prev_result_idx]
                        kwargs_dict[k] = prev_val
            return kwargs_dict

        def convert_input(spec):
            should_return, func_name, args, kwargs = spec
            found_func = lookup_function(func_name)
            # convert any args that reference previous results
            new_args = rewrite_args(args)
            kwargs = rewrite_kwargs(kwargs)
            temp_results.append(found_func(*new_args, **kwargs))
            if should_return:
                return_results.append(temp_results[-1])
                temp_idx_to_return_idx[len(temp_results) - 1] = len(return_results) - 1
            elif found_func == conv:
                # special case conv to preprocess weights and optional bias
                (dummy_output, (new_weights, new_bias)) = temp_results[-1]
                ttnn.deallocate(dummy_output)

                if (weight_idx := lookup_prev_result_idx(args[1])) is not None:
                    return_idx = temp_idx_to_return_idx[weight_idx]
                    return_results[return_idx] = new_weights
                    to_deallocate.append(weight_idx)

                bias_arg = args[2]
                if bias_arg is not None:
                    if (bias_idx := lookup_prev_result_idx(bias_arg)) is not None:
                        return_idx = temp_idx_to_return_idx[bias_idx]
                        return_results[return_idx] = new_bias
                        to_deallocate.append(bias_idx)
            else:
                to_deallocate.append(len(temp_results) - 1)

        for function_call in args:
            convert_input(function_call)

        # deallocate temporaries unless they alias a return value
        # this can happen when a returned value is calculated from a temp, but the operation doesn't actually do anything (e.g. to_layout(temp, ttnn.TILE_LAYOUT) but temp is already TILE_LAYOUT)
        # we only need to worry about device tensors here
        returned_addresses = [
            r.buffer_address()
            for r in return_results
            if isinstance(r, ttnn.Tensor) and r.storage_type() == ttnn.StorageType.DEVICE
        ]
        # only deallocate ttnn tensors
        to_deallocate = [temp_results[idx] for idx in to_deallocate if isinstance(temp_results[idx], ttnn.Tensor)]
        # only deallocate device tensors that do not alias a returned tensor
        to_deallocate = filter(
            lambda tens: tens.storage_type == ttnn.StorageType.DEVICE
            and tens.buffer_address() not in returned_addresses,
            to_deallocate,
        )
        for temp_tensor in to_deallocate:
            ttnn.deallocate(temp_tensor)

        run_once_ans = tuple(return_results)
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
    device_tensor = ttnn.to_layout(device_tensor, layout)
    return ttnn.from_device(device_tensor)


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
    return_weights_and_bias=False,
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
            return_weights_and_bias=return_weights_and_bias,
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
                return_weights_and_bias=return_weights_and_bias,
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
                return_weights_and_bias=return_weights_and_bias,
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
        # TODO: remove when concat supports tiled uint32
        tensor = ttnn.reshape(tensor, unsqueezed_shape)
        if tensor.layout == ttnn.TILE_LAYOUT and tensor.dtype == ttnn.uint32:
            tensor = ttnn.to_layout(tensor, ttnn.ROW_MAJOR_LAYOUT)
        unsqueezed_tensors.append(tensor)

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


# TODO: Support compute kernel config
@torch.fx.wrap
def native_layer_norm(
    input_tensor: ttnn.Tensor,
    in_tensor_shape: torch.Size,
    mean_rstd_shape: torch.Size,
    ttnn_mean_rstd_shape: torch.Size,
    ttnn_dtype: ttnn.DataType,
    norm_dims: int,
    gamma: ttnn.Tensor,
    beta: ttnn.Tensor,
    epsilon: ttnn.Tensor,
    use_mean: bool,
    use_rstd: bool,
    device: ttnn.Device,
):
    if not use_mean and not use_rstd:
        output = ttnn.layer_norm(
            input_tensor, epsilon=epsilon, weight=gamma, bias=beta, memory_config=ttnn.L1_MEMORY_CONFIG
        )
        return (output, None, None)

    output = ttnn.empty(in_tensor_shape, device=device, layout=ttnn.TILE_LAYOUT, dtype=ttnn_dtype)

    # moreh.layer_norm does not generate correct mean or rstd if the shape keeps the normalized dims
    # https://github.com/tenstorrent/tt-metal/issues/22110
    if use_mean:
        mean = ttnn.empty(ttnn_mean_rstd_shape, device=device, layout=ttnn.TILE_LAYOUT, dtype=ttnn_dtype)
    else:
        mean = None

    if use_rstd:
        rstd = ttnn.empty(ttnn_mean_rstd_shape, device=device, layout=ttnn.TILE_LAYOUT, dtype=ttnn_dtype)
    else:
        rstd = None

    output, mean, rstd = ttnn.operations.moreh.layer_norm(
        input_tensor, norm_dims, epsilon, gamma, beta, output=output, mean=mean, rstd=rstd
    )

    if use_mean:
        mean = ttnn.reshape(mean, mean_rstd_shape)
    if use_rstd:
        rstd = ttnn.reshape(rstd, mean_rstd_shape)

    return (output, mean, rstd)

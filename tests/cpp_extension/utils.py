from typing import Any, Callable
from pydantic import BaseModel, Field, model_validator
import torch
import ttnn
from torch_ttnn.cpp_extension import ttnn_module
import pytest


def transform_to_complex(tensor: ttnn.Tensor) -> ttnn.Tensor:
    """Creates a complex tensor with zero imaginary part from a real tensor."""
    ttnn_imag = ttnn.zeros_like(tensor)
    return ttnn.complex_tensor(tensor, ttnn_imag)


def transform_to_real(tensor: ttnn.Tensor) -> ttnn.Tensor:
    """Extracts real part from complex tensor."""
    return tensor.real


class AllCloseFloat(BaseModel):
    """
    Comparison criteria for floating-point tensors using torch.allclose.
    Tolerances are relative (rtol) and absolute (atol).
    """

    rtol: float = 0.1
    atol: float = 0.1

    def compare(self, expected: torch.Tensor, actual: torch.Tensor, op_name: str) -> None:
        """Compare two floating-point tensors using allclose with specified tolerances."""
        assert expected.is_floating_point(), f"Expected tensor ({expected.dtype}) is not floating point"
        assert actual.is_floating_point(), f"Actual tensor ({actual.dtype}) is not floating point"

        assert torch.allclose(expected, actual, rtol=self.rtol, atol=self.atol), f"Mismatch for {op_name}. "


class ExactInt(BaseModel):
    """
    Comparison criteria for integer tensors using torch.equal.
    Requires exact match of all elements.
    """

    def compare(self, expected: torch.Tensor, actual: torch.Tensor, op_name: str) -> None:
        """Compare two integer tensors for exact equality."""
        assert expected.dtype in (
            torch.int,
            torch.int32,
            torch.int64,
            torch.long,
        ), f"ExactInt used for non-integer expected tensor ({expected.dtype}) in {op_name}"
        assert actual.dtype in (
            torch.int,
            torch.int32,
            torch.int64,
            torch.long,
        ), f"ExactInt: Type mismatch for {op_name}. Expected integer, got {actual.dtype}"

        assert (
            expected.shape == actual.shape
        ), f"ExactInt: Shape mismatch for {op_name}: {expected.shape} vs {actual.shape}"

        diff_count = (expected != actual).sum().item()
        assert torch.equal(expected, actual), f"ExactInt: Mismatch for {op_name}. {diff_count} elements differ."


class ExactBool(BaseModel):
    """
    Comparison criteria for boolean tensors using torch.equal.
    Requires exact match of all elements.
    """

    def compare(self, expected: torch.Tensor, actual: torch.Tensor, op_name: str) -> None:
        """Compare two boolean tensors for exact equality."""
        # if expected.dtype != torch.bool:
        #     pytest.fail(f"ExactBool used for non-bool expected tensor ({expected.dtype}) in {op_name}")
        assert (
            expected.dtype == torch.bool
        ), f"ExactBool used for non-bool expected tensor ({expected.dtype}) in {op_name}"

        assert actual.dtype == torch.bool, f"ExactBool: Type mismatch for {op_name}. Expected bool, got {actual.dtype}"
        assert (
            expected.shape == actual.shape
        ), f"ExactBool: Shape mismatch for {op_name}: {expected.shape} vs {actual.shape}"
        diff_count = (expected != actual).sum().item()
        assert torch.equal(expected, actual), f"ExactBool: Mismatch for {op_name}. {diff_count} elements differ."


class OpTestConfig(BaseModel):
    """
    Configuration for running an operation test.
    Defines supported types, input domains, comparison criteria, and other constraints.
    """

    op_name: str
    ttnn_op_name: str | None = None
    dtypes: list[torch.dtype] = Field(default_factory=lambda: [torch.bfloat16])
    low: float = -100.0
    high: float = 100.0
    result_comparison: AllCloseFloat | ExactInt | ExactBool = Field(default_factory=lambda: AllCloseFloat())
    pre_op_transform: Callable[[Any], Any] | None = None
    post_op_transform: Callable[[Any], Any] | None = None

    @model_validator(mode="after")
    def set_ttnn_op_name(self) -> "OpTestConfig":
        if self.ttnn_op_name is None:
            self.ttnn_op_name = self.op_name

        if not hasattr(ttnn, self.ttnn_op_name):
            raise ValueError(
                f"TTNN operation {self.op_name} (mapped to {self.ttnn_op_name}) not found directly in ttnn namespace"
            )

        return self

    class Config:
        arbitrary_types_allowed = True


def get_random_tensor(shape: tuple[int, ...], dtype: torch.dtype, low: float, high: float) -> torch.Tensor:
    if dtype == torch.bfloat16 or dtype == torch.float32:
        return torch.empty(shape, dtype=dtype).uniform_(low, high)
    elif dtype == torch.int or dtype == torch.long:
        return torch.randint(int(low), int(high), shape, dtype=dtype)
    elif dtype == torch.complex64:
        real = torch.empty(shape, dtype=torch.float32).uniform_(low, high)
        imag = torch.empty(shape, dtype=torch.float32).uniform_(low, high)
        return torch.complex(real, imag)
    else:
        raise NotImplementedError(f"Dtype {dtype} not supported for random tensor generation")


def check_dispatcher_registration(
    device: Any,
    config: OpTestConfig,
    input_shape: tuple[int, ...],
    dtype: torch.dtype,
) -> None:
    """
    Verifies that the operation is correctly registered in the PyTorch dispatcher
    and translates to the corresponding TTNN operation.
    """
    ttnn_torch_device = ttnn_module.as_torch_device(device)
    torch_input = get_random_tensor(input_shape, dtype, config.low, config.high)
    torch_input_dev = torch_input.to(ttnn_torch_device)

    torch_op = getattr(torch, config.op_name, None) or getattr(torch.special, config.op_name, None)
    assert torch_op is not None, f"Operation {config.op_name} not found in torch or torch.special"

    # Run via Dispatcher
    dispatcher_output_dev = torch_op(torch_input_dev)
    dispatcher_output = dispatcher_output_dev.to("cpu")

    # Run via Direct ttnn call
    ttnn_op = getattr(ttnn, config.ttnn_op_name)

    ttnn_tensor_input = ttnn_module.get_ttnn_tensor(torch_input_dev)
    ttnn_tensor_input = ttnn.to_layout(ttnn_tensor_input, ttnn.TILE_LAYOUT)

    if config.pre_op_transform:
        ttnn_tensor_input = config.pre_op_transform(ttnn_tensor_input)

    ttnn_out_tensor = ttnn_op(ttnn_tensor_input)

    if config.post_op_transform:
        ttnn_out_tensor = config.post_op_transform(ttnn_out_tensor)

    direct_output = ttnn.to_torch(ttnn_out_tensor)

    # Compare using configured result_comparison
    config.result_comparison.compare(dispatcher_output, direct_output, config.op_name)


def check_ttnn_correctness(device: Any, config: OpTestConfig, input_shape: tuple[int, ...], dtype: torch.dtype) -> None:
    """
    Verifies the numerical correctness of the TTNN operation by comparing it
    against the CPU (Golden) implementation.
    """
    ttnn_torch_device = ttnn_module.as_torch_device(device)
    torch_input = get_random_tensor(input_shape, dtype, config.low, config.high)
    torch_input_dev = torch_input.to(ttnn_torch_device)

    torch_op = getattr(torch, config.op_name, None) or getattr(torch.special, config.op_name, None)
    if torch_op is None:
        pytest.skip(f"Operation {config.op_name} not found in torch or torch.special")

    # 1. Get Golden Result (CPU)
    try:
        golden_output = torch_op(torch_input)
    except Exception as e:
        pytest.skip(f"Golden (CPU) execution failed for {config.op_name}: {e}")

    # 2. Run via Dispatcher (Device)
    dispatcher_output_dev = torch_op(torch_input_dev)
    dispatcher_output = dispatcher_output_dev.to("cpu")

    # 3. Compare
    if dtype == torch.long and dispatcher_output.dtype == torch.int32:
        # Allow casting if we are specifically testing long inputs but receiving int32 outputs (common in ttnn)
        dispatcher_output = dispatcher_output.to(dtype)

    config.result_comparison.compare(golden_output, dispatcher_output, config.op_name)

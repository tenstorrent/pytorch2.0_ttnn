import torch
import pytest
from tests.cpp_extension.utils import (
    check_dispatcher_registration,
    check_ttnn_correctness,
    OpTestConfig,
    ExactInt,
    ExactBool,
)

# Standard floating point types supported by most TTNN operations
FLOAT_DTYPES = [torch.bfloat16]
# Integer types for bitwise/logical operations
INT_DTYPES = [torch.int32]
# Boolean types
BOOL_DTYPES = [torch.bool]

# Define test configurations for each operation
# Pydantic ensures validation and provides a clear schema
UNARY_OPS: list[OpTestConfig] = [
    # Standard Math (float results, default AllCloseFloat comparison)
    OpTestConfig(op_name="abs", dtypes=FLOAT_DTYPES),
    OpTestConfig(op_name="absolute", dtypes=FLOAT_DTYPES),
    OpTestConfig(op_name="neg", dtypes=FLOAT_DTYPES),
    OpTestConfig(op_name="reciprocal", dtypes=FLOAT_DTYPES, low=0.1),  # Avoid 0
    OpTestConfig(op_name="sqrt", dtypes=FLOAT_DTYPES, low=0.001),  # Positive domain
    OpTestConfig(op_name="rsqrt", dtypes=FLOAT_DTYPES, low=0.001),  # Positive domain
    OpTestConfig(op_name="square", dtypes=FLOAT_DTYPES),
    OpTestConfig(op_name="floor", dtypes=FLOAT_DTYPES),
    OpTestConfig(op_name="ceil", dtypes=FLOAT_DTYPES),
    OpTestConfig(op_name="trunc", dtypes=FLOAT_DTYPES),
    OpTestConfig(op_name="frac", dtypes=FLOAT_DTYPES),
    OpTestConfig(op_name="sign", dtypes=FLOAT_DTYPES),
    OpTestConfig(op_name="round", dtypes=FLOAT_DTYPES),
    # Trigonometric
    OpTestConfig(op_name="sin", dtypes=FLOAT_DTYPES),
    OpTestConfig(op_name="cos", dtypes=FLOAT_DTYPES),
    OpTestConfig(op_name="tan", dtypes=FLOAT_DTYPES, low=-9, high=9),  # Avoid poles
    OpTestConfig(op_name="asin", dtypes=FLOAT_DTYPES, low=-0.999, high=0.999),  # Domain
    OpTestConfig(op_name="acos", dtypes=FLOAT_DTYPES, low=-0.999, high=0.999),  # Domain
    OpTestConfig(op_name="atan", dtypes=FLOAT_DTYPES),
    OpTestConfig(op_name="deg2rad", dtypes=FLOAT_DTYPES),
    OpTestConfig(op_name="rad2deg", dtypes=FLOAT_DTYPES),
    # Hyperbolic
    OpTestConfig(op_name="sinh", dtypes=FLOAT_DTYPES, low=-9, high=9),  # Explodes fast
    OpTestConfig(op_name="cosh", dtypes=FLOAT_DTYPES, low=-9, high=9),  # Explodes fast
    OpTestConfig(op_name="tanh", dtypes=FLOAT_DTYPES),
    OpTestConfig(op_name="asinh", dtypes=FLOAT_DTYPES),
    OpTestConfig(op_name="acosh", dtypes=FLOAT_DTYPES, low=1.001),  # Domain > 1
    OpTestConfig(op_name="atanh", dtypes=FLOAT_DTYPES, low=-0.999, high=0.999),
    # Exponential / Logarithmic
    OpTestConfig(op_name="exp", dtypes=FLOAT_DTYPES, low=-10, high=10),
    OpTestConfig(op_name="expm1", dtypes=FLOAT_DTYPES, low=-10, high=10),
    OpTestConfig(op_name="log", dtypes=FLOAT_DTYPES, low=0.001),  # Positive domain
    OpTestConfig(op_name="log10", dtypes=FLOAT_DTYPES, low=0.001),  # Positive domain
    OpTestConfig(op_name="log2", dtypes=FLOAT_DTYPES, low=0.001),  # Positive domain
    OpTestConfig(op_name="log1p", dtypes=FLOAT_DTYPES, low=0.001),  # Positive domain
    OpTestConfig(op_name="sigmoid", dtypes=FLOAT_DTYPES, low=-10, high=10),
    # Special
    OpTestConfig(op_name="i0", dtypes=FLOAT_DTYPES),
    OpTestConfig(op_name="erf", dtypes=FLOAT_DTYPES),
    OpTestConfig(op_name="erfc", dtypes=FLOAT_DTYPES),
    OpTestConfig(op_name="erfinv", dtypes=FLOAT_DTYPES, low=-0.999, high=0.999),
    OpTestConfig(op_name="digamma", dtypes=FLOAT_DTYPES, low=0.001),
    OpTestConfig(op_name="lgamma", dtypes=FLOAT_DTYPES, low=0.001),
    # Activation / Clamp
    OpTestConfig(op_name="relu", dtypes=FLOAT_DTYPES),
    # Complex / Other
    OpTestConfig(op_name="angle", dtypes=FLOAT_DTYPES),
    OpTestConfig(op_name="conj", dtypes=FLOAT_DTYPES),
    # Bitwise/Logical (exact integer match)
    OpTestConfig(op_name="bitwise_not", dtypes=INT_DTYPES, result_comparison=ExactInt()),
    OpTestConfig(op_name="logical_not", dtypes=INT_DTYPES, result_comparison=ExactInt()),
    # Boolean check ops (exact match for bool results)
    OpTestConfig(op_name="signbit", dtypes=FLOAT_DTYPES, result_comparison=ExactBool()),
    OpTestConfig(op_name="isfinite", dtypes=FLOAT_DTYPES, result_comparison=ExactBool()),
    OpTestConfig(op_name="isinf", dtypes=FLOAT_DTYPES, result_comparison=ExactBool()),
    OpTestConfig(op_name="isnan", dtypes=FLOAT_DTYPES, result_comparison=ExactBool()),
]


def get_test_cases() -> list[tuple[OpTestConfig, torch.dtype, tuple[int, ...]]]:
    """
    Generates all test cases (combinations of config, dtype, shape).
    """
    shapes = [(32, 1, 32, 32), (1, 32), (128,)]

    cases = []
    for config in UNARY_OPS:
        for dtype in config.dtypes:
            for shape in shapes:
                cases.append((config, dtype, shape))
    return cases


TEST_CASES = get_test_cases()
TEST_IDS = [f"{c.op_name}-{d}-{s}" for c, d, s in TEST_CASES]


@pytest.mark.dispatcher_registration
@pytest.mark.parametrize("config,dtype,input_shape", TEST_CASES, ids=TEST_IDS)
def test_dispatcher_registration(
    device: object, config: OpTestConfig, dtype: torch.dtype, input_shape: tuple[int, ...]
) -> None:
    check_dispatcher_registration(device, config, input_shape, dtype)


@pytest.mark.ttnn_op_correctness
@pytest.mark.parametrize("config,dtype,input_shape", TEST_CASES, ids=TEST_IDS)
def test_ttnn_op_correctness(
    device: object, config: OpTestConfig, dtype: torch.dtype, input_shape: tuple[int, ...]
) -> None:
    check_ttnn_correctness(device, config, input_shape, dtype)

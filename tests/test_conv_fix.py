# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import ast
from pathlib import Path

import pytest


TARGET_WRAPPERS_PATH = Path(__file__).resolve().parents[1] / "torch_ttnn/passes/lowering/target_wrappers.py"


def _parse_target_wrappers():
    return ast.parse(TARGET_WRAPPERS_PATH.read_text())


def _extract_function(function_name):
    module_ast = _parse_target_wrappers()
    function_node = next(
        node for node in module_ast.body if isinstance(node, ast.FunctionDef) and node.name == function_name
    )
    isolated_module = ast.Module(body=[function_node], type_ignores=[])
    ast.fix_missing_locations(isolated_module)
    namespace = {}
    exec(compile(isolated_module, str(TARGET_WRAPPERS_PATH), "exec"), namespace)
    return namespace[function_name]


@pytest.mark.parametrize(
    "kernel_size,expected",
    [
        (1, False),
        (3, True),
        (5, False),
    ],
)
def test_conv2d_3x3_policy(kernel_size, expected):
    should_use_dram = _extract_function("_should_use_dram_for_conv2d")
    assert should_use_dram((kernel_size, kernel_size)) is expected


def test_conv_lowering_uses_dram_memory_config_for_3x3():
    module_ast = _parse_target_wrappers()
    conv_node = next(node for node in module_ast.body if isinstance(node, ast.FunctionDef) and node.name == "conv")

    helper_calls = [
        node
        for node in ast.walk(conv_node)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "_should_use_dram_for_conv2d"
    ]
    assert helper_calls, "Expected conv wrapper to call _should_use_dram_for_conv2d"

    found_dram_assignment = False
    for node in ast.walk(conv_node):
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if (
            isinstance(target, ast.Subscript)
            and isinstance(target.value, ast.Name)
            and target.value.id == "conv2d_kwargs"
            and isinstance(target.slice, ast.Constant)
            and target.slice.value == "memory_config"
            and isinstance(node.value, ast.Attribute)
            and isinstance(node.value.value, ast.Name)
            and node.value.value.id == "ttnn"
            and node.value.attr == "DRAM_MEMORY_CONFIG"
        ):
            found_dram_assignment = True
            break

    assert found_dram_assignment, "Expected conv wrapper to assign DRAM memory config for 3x3 conv2d"

#!/bin/bash

# Test runner for C++ extension
# Usage: ./run_cpp_extension_tests.sh [pytest-args...]
#
# This script handles all environment setup needed to run C++ extension tests:
# - Activates the Python virtual environment
# - Sets TT_METAL_HOME workaround for tt-metal runtime
# - Runs pytest with provided arguments
#
# Prerequisites:
# - Build completed (run ./build_cpp_extension.sh first)
#
# Examples:
#   ./run_cpp_extension_tests.sh                          # Run all C++ extension tests
#   ./run_cpp_extension_tests.sh -v                       # Verbose output
#   ./run_cpp_extension_tests.sh -k test_specific         # Run specific test
#   ./run_cpp_extension_tests.sh --native_integration    # Run with native integration flag

set -euo pipefail

# ============================================================================
# Configuration
# ============================================================================

# Current directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "=========================================="
echo "C++ Extension Test Runner"
echo "=========================================="
echo "> Script directory: ${SCRIPT_DIR}"

# Project root (two directories up from cpp_extension)
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
echo "> Project root: ${PROJECT_ROOT}"

# TT-Metal directory
TT_METAL_DIR="${SCRIPT_DIR}/third-party/tt-metal"
echo "> TT-Metal directory: ${TT_METAL_DIR}"

# Python virtual environment
PYTHON_ENV_DIR="${PYTHON_ENV_DIR:-${TT_METAL_DIR}/python_env}"
echo "> Python venv: ${PYTHON_ENV_DIR}"

# ============================================================================
# Validation
# ============================================================================

# Check if virtual environment exists
if [[ ! -d "${PYTHON_ENV_DIR}" || ! -f "${PYTHON_ENV_DIR}/bin/activate" ]]; then
    echo ""
    echo "ERROR: Python virtual environment not found"
    echo "Expected location: ${PYTHON_ENV_DIR}"
    echo ""
    echo "Please run the build script first:"
    echo "  cd ${SCRIPT_DIR}"
    echo "  ./build_cpp_extension.sh"
    echo ""
    exit 1
fi

# Check if tt-metal exists
if [[ ! -d "${TT_METAL_DIR}" ]]; then
    echo ""
    echo "ERROR: TT-Metal directory not found"
    echo "Expected location: ${TT_METAL_DIR}"
    echo ""
    echo "Please initialize submodules:"
    echo "  git submodule update --init --recursive"
    echo ""
    exit 1
fi

# ============================================================================
# Environment Setup
# ============================================================================

echo ""
echo "Setting up test environment..."
echo "--------------------------------------------"

# Activate virtual environment
echo "> Activating virtual environment..."
source "${PYTHON_ENV_DIR}/bin/activate"

# WORKAROUND: tt-metal runtime requires TT_METAL_HOME
# library_tweaks.py incorrectly looks for runtime at ttnn/ttnn/runtime/hw
# but in source builds it's at tt-metal/runtime/hw (parent directory)
# See: https://github.com/tenstorrent/pytorch2.0_ttnn/issues/...
echo "> Setting TT_METAL_HOME (workaround for tt-metal runtime)..."
export TT_METAL_HOME="${TT_METAL_DIR}"
echo "  TT_METAL_HOME=${TT_METAL_HOME}"

# ============================================================================
# Run Tests
# ============================================================================

echo ""
echo "Running tests..."
echo "--------------------------------------------"

cd "${PROJECT_ROOT}"

# If no arguments provided, run default test suite
if [[ $# -eq 0 ]]; then
    echo "> Running C++ extension tests..."
    python -m pytest tests/cpp_extension/test_cpp_extension_functionality.py -v
    
    echo ""
    echo "> Running BERT C++ extension tests..."
    python -m pytest tests/cpp_extension/test_bert_cpp_extension.py -v
    
    echo ""
    echo "> Running PyTorch Dispatcher registration tests..."
    python -m pytest tests/cpp_extension/ops/unary/ -m dispatcher_registration -v
    
    echo ""
    echo "> Running TTNN operation correctness tests..."
    python -m pytest tests/cpp_extension/ops/unary/ -m ttnn_op_correctness -v || true
    
    echo ""
    echo "> Running model tests with native integration..."
    python -m pytest tests/models/ --native_integration -v
else
    # Pass all arguments to pytest
    echo "> Running: pytest $@"
    python -m pytest "$@"
fi

# ============================================================================
# Complete
# ============================================================================

echo ""
echo "=========================================="
echo "✓ Tests Complete!"
echo "=========================================="
echo ""


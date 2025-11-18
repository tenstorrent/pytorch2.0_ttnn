#!/bin/bash

# Build script for C++ extension with tt-metal
# Usage: ./build_cpp_extension.sh [BUILD_TYPE] [--test-pypi-ttnn]
# 
# Arguments:
#   BUILD_TYPE: Release (default), Debug, RelWithDebInfo, ASan, TSan, ASanCoverage
#   --test-pypi-ttnn: Install with [pypi,dev] to test ttnn from PyPI (for CI ttnn update PRs)
#
# This script handles the complete build pipeline:
# - Phase 1: Build TT-Metal with the specified build type
# - Phase 2: Create/reuse Python virtual environment
# - Phase 3: Build and install torch-ttnn C++ extension
#
# Prerequisites (one-time setup):
# - System dependencies installed (see tt-metal/install_dependencies.sh)
# - Git submodules initialized (git submodule update --init --recursive)
#
# Features:
# - Smart caching: Reuses existing virtual environment and dependencies
# - Per-build-type artifacts: Switching build types rebuilds only what's needed
# - Clear output and error messages
# - Automatic environment setup

set -euo pipefail

# ============================================================================
# Configuration
# ============================================================================

# Parse arguments
BUILD_TYPE=${1:-Release}
TEST_PYPI_TTNN=false

# Check for --test-pypi-ttnn flag
for arg in "$@"; do
    if [[ "$arg" == "--test-pypi-ttnn" ]]; then
        TEST_PYPI_TTNN=true
    fi
done

# Validate build type
BUILD_TYPE_ARG=""
for arg in "$@"; do
    if [[ "$arg" != "--test-pypi-ttnn" ]]; then
        BUILD_TYPE_ARG="$arg"
        break
    fi
done
BUILD_TYPE="${BUILD_TYPE_ARG:-Release}"
case "${BUILD_TYPE}" in
    Release|Debug|RelWithDebInfo|ASan|TSan|ASanCoverage)
        echo "=========================================="
        echo "Building with: ${BUILD_TYPE}"
        echo "=========================================="
        ;;
    *)
        echo "ERROR: Invalid build type '${BUILD_TYPE}'"
        echo "Valid options: Release, Debug, RelWithDebInfo, ASan, TSan, ASanCoverage"
        echo "Note: Most common are Release (default), Debug, RelWithDebInfo"
        exit 1
        ;;
esac

# Current directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "> Script directory: ${SCRIPT_DIR}"

# Project root (two directories up from cpp_extension)
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
echo "> Project root: ${PROJECT_ROOT}"

# TT-Metal directory
TT_METAL_DIR="${SCRIPT_DIR}/third-party/tt-metal"
echo "> TT-Metal directory: ${TT_METAL_DIR}"

# Check if tt-metal submodule exists
if [[ ! -d "${TT_METAL_DIR}/.git" ]]; then
    echo ""
    echo "ERROR: tt-metal submodule not initialized"
    echo "Please run: git submodule update --init --recursive"
    echo ""
    exit 1
fi

# ============================================================================
# Environment Setup
# ============================================================================

# Python virtual environment (create if not exists, reuse if exists)
export PYTHON_ENV_DIR="${PYTHON_ENV_DIR:-${TT_METAL_DIR}/python_env}"
export CPM_SOURCE_CACHE="${CPM_SOURCE_CACHE:-${HOME}/.cache/cpm}"
export TT_METAL_TOOLS_DIR="${TT_METAL_DIR}/.local/bin"

# Compiler selection
export CC="${CC:-$(command -v clang-17 2>/dev/null || command -v clang)}"
export CXX="${CXX:-$(command -v clang++-17 2>/dev/null || command -v clang++)}"
export CMAKE_C_COMPILER="${CC}"
export CMAKE_CXX_COMPILER="${CXX}"
export CMAKE_MAKE_PROGRAM="${CMAKE_MAKE_PROGRAM:-$(command -v ninja)}"

echo "> Compiler: ${CXX}"
echo "> CMake generator: ${CMAKE_MAKE_PROGRAM}"
echo "> Python venv: ${PYTHON_ENV_DIR}"

# Create necessary directories
mkdir -p "${CPM_SOURCE_CACHE}" "${TT_METAL_TOOLS_DIR}"
export PATH="${TT_METAL_TOOLS_DIR}:${PATH}"

# ============================================================================
# Phase 1: Build TT-Metal
# ============================================================================

echo ""
echo "Phase 1: Build TT-Metal (${BUILD_TYPE})"
echo "--------------------------------------------"

cd "${TT_METAL_DIR}"

# Determine build directory name (tt-metal convention: build_<TYPE>)
TT_METAL_BUILD_DIR="build_${BUILD_TYPE}"
echo "> TT-Metal build directory: ${TT_METAL_BUILD_DIR}"

# Clean only the specific build type directory and generic 'build' dir
echo "> Cleaning previous ${BUILD_TYPE} build..."
rm -rf "${TT_METAL_BUILD_DIR}" build

# Build tt-metal with specified build type
# Use -b flag which is the canonical way to specify build type
echo "> Building tt-metal..."
./build_metal.sh -b "${BUILD_TYPE}" --enable-ccache

# Verify build output
if [[ ! -d "${TT_METAL_BUILD_DIR}" ]]; then
    echo ""
    echo "ERROR: TT-Metal build failed - ${TT_METAL_BUILD_DIR} not found"
    echo "Please check build_metal.sh output for errors"
    echo ""
    exit 1
fi

echo "> TT-Metal build complete: ${TT_METAL_BUILD_DIR}/"

# ============================================================================
# Phase 2: Create/Reuse Python Virtual Environment
# ============================================================================

echo ""
echo "Phase 2: Python Virtual Environment"
echo "--------------------------------------------"

if [[ -d "${PYTHON_ENV_DIR}" && -f "${PYTHON_ENV_DIR}/bin/activate" ]]; then
    echo "> Virtual environment already exists (reusing)"
    echo "  Location: ${PYTHON_ENV_DIR}"
    echo "  To force recreate, remove this directory"
else
    echo "> Creating new virtual environment..."
    rm -rf "${PYTHON_ENV_DIR}"
    ./create_venv.sh
    echo "> Virtual environment created: ${PYTHON_ENV_DIR}"
fi

# Activate virtual environment
echo "> Activating virtual environment..."
source "${PYTHON_ENV_DIR}/bin/activate"

# Ensure tools are in PATH
export PATH="${TT_METAL_TOOLS_DIR}:${PATH}"

# Configure pip
echo "> Configuring pip for PyTorch CPU wheels..."
python -m pip config set global.extra-index-url https://download.pytorch.org/whl/cpu

# Upgrade build dependencies
echo "> Updating build dependencies..."
python -m pip install --upgrade pip
python -m pip install --upgrade "scikit-build-core<0.11" cmake ninja

# ============================================================================
# Phase 3: Build and Install torch-ttnn C++ Extension
# ============================================================================

echo ""
echo "Phase 3: Build torch-ttnn C++ Extension (${BUILD_TYPE})"
echo "--------------------------------------------"

cd "${PROJECT_ROOT}"

# Pass build type to CMake via CMAKE_ARGS
export CMAKE_ARGS="-DCMAKE_BUILD_TYPE=${BUILD_TYPE}"
echo "> CMake args: ${CMAKE_ARGS}"

# Determine which extras to install based on flag
if [[ "${TEST_PYPI_TTNN}" == "true" ]]; then
    echo "> Installing with [pypi,dev] (testing ttnn from PyPI)"
    INSTALL_EXTRAS="[pypi,dev]"
else
    echo "> Installing with [dev] (using local ttnn from submodule)"
    INSTALL_EXTRAS="[dev]"
fi

# Install torch-ttnn with C++ extension
echo "> Installing torch-ttnn..."
python -m pip install -e ".${INSTALL_EXTRAS}"

# ============================================================================
# Build Complete
# ============================================================================

echo ""
echo "=========================================="
echo "✓ Build Complete!"
echo "=========================================="
echo ""
echo "Build Configuration:"
echo "  - Build type: ${BUILD_TYPE}"
echo "  - TT-Metal: ${TT_METAL_DIR}/${TT_METAL_BUILD_DIR}/"
echo "  - Virtual env: ${PYTHON_ENV_DIR}"
echo "  - Extensions: ${INSTALL_EXTRAS}"
echo ""
echo "To run tests:"
echo "  ./run_cpp_extension_tests.sh              # Run all tests (recommended)"
echo "  ./run_cpp_extension_tests.sh -v           # Verbose output"
echo "  ./run_cpp_extension_tests.sh -k test_name # Run specific test"
echo ""
echo "To rebuild with a different build type:"
echo "  ./build_cpp_extension.sh Debug              # Debug build"
echo "  ./build_cpp_extension.sh RelWithDebInfo     # Release with debug info"
echo "  ./build_cpp_extension.sh ASan               # AddressSanitizer build"
echo ""
echo "To test with ttnn from PyPI (for CI ttnn update validation):"
echo "  ./build_cpp_extension.sh Release --test-pypi-ttnn"
echo ""
echo "Notes:"
echo "  - Virtual environment is reused across builds (faster)"
echo "  - Only the ${BUILD_TYPE} build artifacts are cleaned"
echo "  - To force clean build: remove ${TT_METAL_BUILD_DIR}/ and build/"
echo ""

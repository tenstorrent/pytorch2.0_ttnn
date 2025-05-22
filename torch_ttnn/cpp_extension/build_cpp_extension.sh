#!/bin/bash

# parse build type
BUILD_TYPE=${1:-Release}
echo "> Build type: $BUILD_TYPE"

# Current directory
CUR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "> Current directory: $CUR_DIR"

# ABI flags used when compiling torch
TORCH_ABI_FLAGS=$(python3 $CUR_DIR/utils/get_torch_abi_flags.py)
echo "> TORCH_ABI_FLAGS: $TORCH_ABI_FLAGS"

# Configure ttnn
# TODO: check if c++17 is enough
echo "> Configuring ttnn"
cmake -B $CUR_DIR/third-party/tt-metal/build \
    -G Ninja \
    -DCMAKE_BUILD_TYPE=$BUILD_TYPE \
    -DCMAKE_INSTALL_PREFIX=$CUR_DIR/third-party/tt-metal/build \
    -DCMAKE_DISABLE_PRECOMPILE_HEADERS=TRUE \
    -DENABLE_CCACHE=TRUE \
    -DCMAKE_EXPORT_COMPILE_COMMANDS=OFF \
    -DTT_UNITY_BUILDS=ON \
    -DTT_ENABLE_LIGHT_METAL_TRACE=ON \
    -DWITH_PYTHON_BINDINGS=ON \
    -DCMAKE_TOOLCHAIN_FILE=$CUR_DIR/cmake/x86_64-linux-torch-toolchain.cmake \
    -DCMAKE_CXX_FLAGS="${TORCH_ABI_FLAGS} -std=c++20" \
    -S $CUR_DIR/third-party/tt-metal


# Build ttnn
echo "> Building ttnn"
ninja -C $CUR_DIR/third-party/tt-metal/build install

pip3 install -e $CUR_DIR/third-party/tt-metal/

export TT_METAL_HOME=$CUR_DIR/third-party/tt-metal
echo "> TT_METAL_HOME: $TT_METAL_HOME"
echo "> Building cpp extension"
CMAKE_FLAGS="-DCMAKE_BUILD_TYPE=${BUILD_TYPE};-DCMAKE_C_COMPILER_LAUNCHER=ccache;-DCMAKE_CXX_COMPILER_LAUNCHER=ccache;-DCMAKE_CXX_COMPILER=g++-12;-DCMAKE_C_COMPILER=gcc-12" python3 setup.py develop

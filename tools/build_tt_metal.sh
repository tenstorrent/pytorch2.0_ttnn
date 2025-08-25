#!/bin/bash

set -e 

while [ $# -gt 0 ]
do
    case "$1" in
        -p|--profiling) ENABLE_PROFILING=1;;
        -t|--torch) TORCH_COMPAT=1;;
    esac
    shift
done

# parse build type
BUILD_TYPE=${1:-Release}
echo "> Build type: $BUILD_TYPE"

# Current directory
CUR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "> Current directory: $CUR_DIR"

# ABI flags used when compiling torch
# if [ -n $TORCH_COMPAT ]; then
#     TORCH_ABI_FLAGS=$(python3 $CUR_DIR/get_torch_abi_flags.py)
#     echo "> TORCH_ABI_FLAGS: $TORCH_ABI_FLAGS"
#     CMAKE_CXX_FLAGS="${TORCH_ABI_FLAGS} -std=c++20"

#     CPP_EXT_DIR="$CUR_DIR/../torch_ttnn/cpp_extension"
#     CMAKE_TOOLCHAIN_FILE=$CPP_EXT_DIR/cmake/x86_64-linux-torch-toolchain.cmake
# fi

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
    ${CMAKE_TOOLCHAIN_FILE:+-DCMAKE_TOOLCHAIN_FILE=${CMAKE_TOOLCHAIN_FILE}} \
    ${ENABLE_PROFILING:+-DENABLE_TRACY=ON} \
    ${CMAKE_CXX_FLAGS:+-DCMAKE_CXX_FLAGS=${CMAKE_CXX_FLAGS}} \
    -S $CUR_DIR/third-party/tt-metal


# Build ttnn
echo "> Building ttnn"
ninja -C $CUR_DIR/third-party/tt-metal/build install

# if [ -n $TORCH_COMPAT ]; then
#     pip3 install -e $CUR_DIR/third-party/tt-metal/

#     export TT_METAL_HOME=$CUR_DIR/third-party/tt-metal
#     echo "> TT_METAL_HOME: $TT_METAL_HOME"

#     echo "> Building cpp extension"
#     cd "$CPP_EXT_DIR"
#     CMAKE_FLAGS="-DCMAKE_BUILD_TYPE=${BUILD_TYPE};-DCMAKE_C_COMPILER_LAUNCHER=ccache;-DCMAKE_CXX_COMPILER_LAUNCHER=ccache;-DCMAKE_CXX_COMPILER=g++-12;-DCMAKE_C_COMPILER=gcc-12" python3 setup.py develop
# fi

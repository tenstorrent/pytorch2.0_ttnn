#!/bin/bash

while [ $# -gt 0 ]
do
    case "$1" in
        -p|--profiling) ENABLE_PROFILING=1;;
    esac
    shift
done

# parse build type
BUILD_TYPE=${1:-Release}
echo "> Build type: $BUILD_TYPE"

# Current directory
CUR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "> Current directory: $CUR_DIR"

# Configure ttnn
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
    -DWITH_PYTHON_BINDINGS=ON ${ENABLE_PROFILING:+-DENABLE_TRACY=ON} \
    -S $CUR_DIR/third-party/tt-metal


# Build ttnn
echo "> Building ttnn"
ninja -C $CUR_DIR/third-party/tt-metal/build install

#pip3 install -r $CUR_DIR/third-party/tt-metal/tt_metal/python_env/requirements-dev.txt
# pip3 install -e $CUR_DIR/third-party/tt-metal/

# export TT_METAL_HOME=$CUR_DIR/third-party/tt-metal
# export PYTHONPATH="${TT_METAL_HOME}"
# echo "> TT_METAL_HOME: $TT_METAL_HOME"
# ls "$TT_METAL_HOME/build/include"
# python3 -c "import tracy"
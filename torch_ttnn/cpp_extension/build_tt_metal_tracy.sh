#!/bin/bash

# parse build type
BUILD_TYPE=${1:-Release}
echo "> Build type: $BUILD_TYPE"

echo "> Pytorch2.0_ttnn commit:"
git rev-parse HEAD
cat .gitmodules

# Current directory
CUR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "> Current directory: $CUR_DIR"

pushd "$CUR_DIR/third-party/tt-metal"
CURR_COMMIT=$(git rev-parse HEAD)
echo "> Current commit: $CURR_COMMIT"
popd

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
    -DWITH_PYTHON_BINDINGS=ON \
    -DCMAKE_TOOLCHAIN_FILE=$CUR_DIR/cmake/x86_64-linux-torch-toolchain.cmake \
    -DENABLE_TRACY=ON \
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
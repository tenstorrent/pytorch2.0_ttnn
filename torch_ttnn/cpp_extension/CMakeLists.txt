cmake_minimum_required(VERSION 3.18)

set(CMAKE_CXX_COMPILER /usr/bin/clang++-17)
set(CMAKE_CXX_STANDARD 20) 

project(ttnn_device_extension CXX)

list(PREPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake")
include(CPM)
include(NoMKLWorkaround)

find_package(Torch REQUIRED)
find_package(Python COMPONENTS Development REQUIRED)

CPMAddPackage(NAME pybind11 GITHUB_REPOSITORY pybind/pybind11 GIT_TAG v2.13.6 OPTIONS "CMAKE_MESSAGE_LOG_LEVEL NOTICE")

if(NOT DEFINED ENV{TT_METAL_HOME})
    message(FATAL_ERROR "TT_METAL_HOME environment variable is not set")
endif()

set(TT_METAL_HOME $ENV{TT_METAL_HOME})

set(TTNN_INCLUDE_DIRS
    ${CMAKE_CURRENT_SOURCE_DIR}/include
    ${TT_METAL_HOME}/ttnn/cpp
    ${TT_METAL_HOME}/ttnn
    ${TT_METAL_HOME}/ttnn/cpp/cpp
    ${TT_METAL_HOME}/tt_metal/api
    ${TT_METAL_HOME}/tt_metal/third_party/umd/device/api
    ${TT_METAL_HOME}/tt_metal/hostdevcommon/api
    ${TT_METAL_HOME}/tt_metal/third_party/tracy/public
    ${TT_METAL_HOME}/tt_stl
    ${TT_METAL_HOME}/.cpmcache/reflect/e75434c4c5f669e4a74e4d84e0a30d7249c1e66f
    # ${TT_METAL_HOME}/.cpmcache/nanomsg/28cc32d5bdb6a858fe53b3ccf7e923957e53eada/include
    ${TT_METAL_HOME}/.cpmcache/fmt/69912fb6b71fcb1f7e5deca191a2bb4748c4e7b6//include
    ${TT_METAL_HOME}/.cpmcache/magic_enum/4d76fe0a5b27a0e62d6c15976d02b33c54207096/include
    ${TT_METAL_HOME}/.cpmcache/nlohmann_json/798e0374658476027d9723eeb67a262d0f3c8308/include
    # ${TT_METAL_HOME}/.cpmcache/boost/1359e136761ab2d10afa1c4e21086c8d824735cd/libs/core/include
    # ${TT_METAL_HOME}/.cpmcache/xtensor/4a957e26c765b48cbec4a4235fe9e518d5a85d3d/include
    # ${TT_METAL_HOME}/.cpmcache/xtensor-blas/190c3a4314355b67291a7d78b20a2100de3f8f54/include
    # ${TT_METAL_HOME}/.cpmcache/xtl/0918808959d33a292c551b9f014a0e808bc4a95c/include
)


set(TTNN_CPP_EXTENSION_SOURCES 
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/open_registration_extension.cpp

    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/core/copy.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/core/TtnnCustomAllocator.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/core/TtnnGuard.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/core/TtnnTensorImpl.cpp

    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/ops/binary.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/ops/creation.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/ops/unary.cpp

    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/utils/device.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/utils/vector_utils.cpp

)

add_library(ttnn_device_extension SHARED ${TTNN_CPP_EXTENSION_SOURCES})
target_compile_options(ttnn_device_extension PRIVATE -g -DFMT_HEADER_ONLY -UPYBIND11_COMPILER_TYPE -UPYBIND11_BUILD_ABI)
target_include_directories(ttnn_device_extension PRIVATE 
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/include
    ${TTNN_INCLUDE_DIRS}
)
target_link_directories(ttnn_device_extension PRIVATE "${TORCH_INSTALL_PREFIX}/lib")
target_link_libraries(ttnn_device_extension PUBLIC 
    # torch::torch
    ${TORCH_LIBRARIES} 
    Python::Python
    torch_python
    pybind11::module

    -L${TT_METAL_HOME}/build/lib -Wl,-rpath=${TT_METAL_HOME}/build/lib
    -ltt_metal
    -l:_ttnn.so
    -ldevice
)


add_subdirectory(demo)
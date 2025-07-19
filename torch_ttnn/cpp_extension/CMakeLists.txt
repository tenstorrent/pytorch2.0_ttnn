cmake_minimum_required(VERSION 3.18)

set(CMAKE_CXX_STANDARD 20)

project(ttnn_device_extension CXX)

# Options
option(ENABLE_LOCAL_TT_METAL_BUILD "Enable local TT_Metal build" OFF)
option(ENABLE_SUBMODULE_TT_METAL_BUILD "Enable submodule TT_Metal build" OFF)
option(BUILD_EXAMPLES "Build examples" OFF)

list(PREPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake")
include(utils)

# Prepare tt-metal build
# TODO: Add debian integration with ttnn once ready
include(find_prebuilt_ttnn)

check_ubuntu_version_at_least(24 IS_UBUNTU_GE_24)
message(STATUS "Ubuntu version > 24: ${IS_UBUNTU_GE_24}")
message(STATUS "CMAKE_BUILD_TYPE: ${CMAKE_BUILD_TYPE}")

# NOTE: ttnn reauires to downrade python version to 3.10, which break find_package
# TODO: Remove this once ttnn is updated to support python 3.12+
if (IS_UBUNTU_GE_24)
    include(find_python_workaround_ubuntu24)
else()
    set(Python_FIND_VIRTUALENV FIRST)
    find_package(PythonLibs COMPONENTS Interpreter Development REQUIRED)
endif()

find_package(Torch REQUIRED)

set(TTNN_CPP_EXTENSION_SOURCES 
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/open_registration_extension.cpp

    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/core/copy.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/core/TtnnCustomAllocator.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/core/TtnnGuard.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/core/TtnnTensorImpl.cpp

    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/ops/binary.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/ops/creation.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/ops/unary.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/ops/embedding.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/ops/norm.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/ops/softmax.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/ops/to_copy.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/ops/view.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/ops/linear.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/ops/matmul.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/ops/as_strided.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/ops/clone.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/ops/expand.cpp

    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/utils/device.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/utils/vector_utils.cpp

)

add_library(ttnn_device_extension SHARED ${TTNN_CPP_EXTENSION_SOURCES})
target_compile_options(ttnn_device_extension PRIVATE
    -DFMT_HEADER_ONLY
    -DTORCH_EXTENSION_NAME=ttnn_device_extension
    -DTORCH_API_INCLUDE_EXTENSION_H
)
if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    target_compile_definitions(ttnn_device_extension PRIVATE DISABLE_NAMESPACE_STATIC_ASSERT)
endif()
target_include_directories(ttnn_device_extension PRIVATE 
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/include
    ${PYTHON_INCLUDE_DIRS}
)

# Needed for torch_python
target_link_directories(ttnn_device_extension PRIVATE "${TORCH_INSTALL_PREFIX}/lib")

target_link_libraries(ttnn_device_extension PUBLIC
    Metalium::Metal
    Metalium::TTNN
)

target_link_libraries(ttnn_device_extension PUBLIC 
    ${TORCH_LIBRARIES} 
    ${PYTHON_LIBRARIES}
    torch_python
)

if(NOT DEFINED OUTPUT_NAME)
  set(OUTPUT_NAME "ttnn_device_extension")
endif()

set_target_properties(ttnn_device_extension PROPERTIES
    PREFIX ""
    SUFFIX ""
    OUTPUT_NAME ${OUTPUT_NAME}
)

if (BUILD_EXAMPLES)
    message(STATUS "Building examples")
    add_subdirectory(ttnn_cpp_extension/examples)
endif()
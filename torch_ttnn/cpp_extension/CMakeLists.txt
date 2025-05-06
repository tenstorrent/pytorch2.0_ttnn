cmake_minimum_required(VERSION 3.18)

set(CMAKE_CXX_STANDARD 20)

project(ttnn_device_extension CXX)

option(ENABLE_LOCAL_TT_METAL_BUILD "Enable local TT_Metal build" OFF)

list(PREPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake")
include(utils)

check_ubuntu_version_at_least(24 IS_UBUNTU_GE_24)
message(STATUS "Ubuntu version > 24: ${IS_UBUNTU_GE_24}")

if (IS_UBUNTU_GE_24)
    include(find_python_workaround_ubuntu24)
else()
    set(Python_FIND_VIRTUALENV FIRST)
    find_package(Python COMPONENTS Interpreter Development REQUIRED)
endif()

find_package(Torch REQUIRED)

if(NOT DEFINED ENV{TT_METAL_HOME})
    message(FATAL_ERROR "TT_METAL_HOME environment variable is not set")
endif()

if (ENABLE_LOCAL_TT_METAL_BUILD)
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
        ${TT_METAL_HOME}/.cpmcache/fmt/69912fb6b71fcb1f7e5deca191a2bb4748c4e7b6//include
        ${TT_METAL_HOME}/.cpmcache/magic_enum/4d76fe0a5b27a0e62d6c15976d02b33c54207096/include
        ${TT_METAL_HOME}/.cpmcache/nlohmann_json/798e0374658476027d9723eeb67a262d0f3c8308/include
    )
else()
    message(FATAL_ERROR "TT_Metal build is not enabled. Please set ENABLE_LOCAL_TT_METAL_BUILD to ON.")
endif()


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
target_compile_options(ttnn_device_extension PRIVATE
    -g -DFMT_HEADER_ONLY
    -DTORCH_EXTENSION_NAME=ttnn_device_extension
    -DTORCH_API_INCLUDE_EXTENSION_H
)
target_include_directories(ttnn_device_extension PRIVATE 
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/include
    ${TTNN_INCLUDE_DIRS}
    ${PYTHON_INCLUDE_DIRS}
)
# Needed for torch_python
target_link_directories(ttnn_device_extension PRIVATE "${TORCH_INSTALL_PREFIX}/lib")

target_link_libraries(ttnn_device_extension PUBLIC 
    ${TORCH_LIBRARIES} 
    ${PYTHON_LIBRARIES}
    torch_python
)

if (ENABLE_LOCAL_TT_METAL_BUILD)
    target_link_libraries(ttnn_device_extension PUBLIC 
        -L${TT_METAL_HOME}/build/lib -Wl,-rpath=${TT_METAL_HOME}/build/lib
        -ltt_metal
        -l:_ttnn.so
        -ldevice
    )
endif()

if(NOT DEFINED OUTPUT_NAME)
  set(OUTPUT_NAME "ttnn_device_extension")
endif()

set_target_properties(ttnn_device_extension PROPERTIES
    PREFIX ""
    SUFFIX ""
    OUTPUT_NAME ${OUTPUT_NAME}
)

add_subdirectory(demo)
cmake_minimum_required(VERSION 3.18)
project(ttnn_device_extension LANGUAGES CXX)

#——————————————————————————————————————————————
# 0) Work around boost.container / boost.move clashes under C++20:
add_compile_definitions(
  BOOST_MOVE_USE_STANDARD_LIBRARY_MOVE
  BOOST_MOVE_USE_STANDARD_LIBRARY_TYPE_TRAITS
  BOOST_CONTAINER_PERFECT_FORWARDING
)

#——————————————————————————————————————————————
# 1) Enforce C++20 and PIC
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

#——————————————————————————————————————————————
# 2) Make sure CMake can find your custom modules
list(PREPEND CMAKE_MODULE_PATH
  "${CMAKE_CURRENT_SOURCE_DIR}/cmake"
)

#——————————————————————————————————————————————
# 3) Bootstrap CPM.cmake automatically
set(CPM_DOWNLOAD_VERSION 0.38.2)
if (NOT CPM_LOADED)
  message(STATUS "Downloading CPM.cmake v${CPM_DOWNLOAD_VERSION}…")
  file(DOWNLOAD
    https://github.com/cpm-cmake/CPM.cmake/releases/download/v${CPM_DOWNLOAD_VERSION}/CPM.cmake
    "${CMAKE_BINARY_DIR}/CPM.cmake"
    INACTIVITY_TIMEOUT 60
  )
  include("${CMAKE_BINARY_DIR}/CPM.cmake")
endif()

#——————————————————————————————————————————————
# 4) Pull in spdlog (header-only, bundled fmt)
CPMAddPackage(
  NAME spdlog
  GITHUB_REPOSITORY gabime/spdlog
  VERSION 1.11.0
  OPTIONS
    "SPDLOG_FMT_EXTERNAL OFF"
    "SPDLOG_INSTALL OFF"
)

#——————————————————————————————————————————————
# 5) Find Python, Torch, and your prebuilt TT-Metal libs
include(utils)              # cmake/utils.cmake
include(find_prebuilt_ttnn) # cmake/find_prebuilt_ttnn.cmake

find_package(Torch    REQUIRED)
find_package(PythonLibs COMPONENTS Interpreter Development REQUIRED)

#——————————————————————————————————————————————
# 6) Locate TT-Metal root (submodule vs sibling checkout)
if (EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/third-party/tt-metal")
  set(TT_METAL_ROOT "${CMAKE_CURRENT_SOURCE_DIR}/third-party/tt-metal")
elseif (EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/../../tt-metal")
  set(TT_METAL_ROOT "${CMAKE_CURRENT_SOURCE_DIR}/../../tt-metal")
else()
  message(FATAL_ERROR "Не знайдено TT-Metal у third-party/tt-metal або ../../tt-metal")
endif()
message(STATUS "Using TT-Metal from: ${TT_METAL_ROOT}")

#——————————————————————————————————————————————
# 7) Gather your extension’s sources
set(TTNN_SOURCES
  ttnn_cpp_extension/src/open_registration_extension.cpp

  ttnn_cpp_extension/src/core/copy.cpp
  ttnn_cpp_extension/src/core/TtnnCustomAllocator.cpp
  ttnn_cpp_extension/src/core/TtnnGuard.cpp
  ttnn_cpp_extension/src/core/TtnnTensorImpl.cpp

  ttnn_cpp_extension/src/ops/binary.cpp
  ttnn_cpp_extension/src/ops/creation.cpp
  ttnn_cpp_extension/src/ops/unary.cpp
  ttnn_cpp_extension/src/ops/softmax.cpp
  ttnn_cpp_extension/src/ops/to_copy.cpp
  ttnn_cpp_extension/src/ops/embedding.cpp
  ttnn_cpp_extension/src/ops/view.cpp
  ttnn_cpp_extension/src/ops/norm.cpp

  ttnn_cpp_extension/src/utils/device.cpp
  ttnn_cpp_extension/src/utils/vector_utils.cpp
)

#——————————————————————————————————————————————
# 8) Declare your shared library
add_library(ttnn_device_extension SHARED ${TTNN_SOURCES})

# compile-time flags
target_compile_options(ttnn_device_extension PRIVATE
  -DFMT_HEADER_ONLY
  -DTORCH_EXTENSION_NAME=ttnn_device_extension
  -DTORCH_API_INCLUDE_EXTENSION_H
)
if (CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
  target_compile_definitions(ttnn_device_extension PRIVATE DISABLE_NAMESPACE_STATIC_ASSERT)
endif()

#——————————————————————————————————————————————
# 9) Include directories
target_include_directories(ttnn_device_extension
  PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/include
    ${PYTHON_INCLUDE_DIRS}
    ${CMAKE_CURRENT_SOURCE_DIR}/third-party/tt-metal/ttnn/cpp

  SYSTEM PRIVATE
    ${TT_METAL_ROOT}/ttnn/cpp
    ${TT_METAL_ROOT}/tt_metal/api
    ${TT_METAL_ROOT}/build_Release/include
)

#——————————————————————————————————————————————
# 10) Link libraries
target_link_libraries(ttnn_device_extension
  PRIVATE
    spdlog::spdlog_header_only
    ${TORCH_LIBRARIES}
    ${PYTHON_LIBRARIES}
    torch_python

  PUBLIC
    Metalium::Metal
    Metalium::TTNN
)

# add Torch’s lib path so torch_python знайдеся
target_link_directories(ttnn_device_extension PRIVATE
  "${TORCH_INSTALL_PREFIX}/lib"
)

#——————————————————————————————————————————————
# 11) Output naming (so PyTorch can load it by name)
set_target_properties(ttnn_device_extension PROPERTIES
  PREFIX ""
  SUFFIX ""
  OUTPUT_NAME "ttnn_device_extension"
)

#——————————————————————————————————————————————
# 12) (Optional) build examples
option(BUILD_EXAMPLES "Build examples" OFF)
if (BUILD_EXAMPLES)
  add_subdirectory(ttnn_cpp_extension/examples)
endif()

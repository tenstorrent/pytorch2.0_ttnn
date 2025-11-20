cmake_minimum_required(VERSION 3.23)

if(DEFINED ENV{SKIP_CPP_EXTENSION} AND "$ENV{SKIP_CPP_EXTENSION}" STREQUAL "1")
    message(STATUS "SKIP_CPP_EXTENSION=1 - skipping C++ extension build")
    return()
endif()

list(PREPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")
include(utils)

function(ttnn_log_list_var heading var_name)
    if(NOT DEFINED ${var_name} OR "${${var_name}}" STREQUAL "")
        message(STATUS "${heading}: <empty>")
        return()
    endif()
    set(_formatted "")
    foreach(_entry IN LISTS ${var_name})
        string(APPEND _formatted "\n    - ${_entry}")
    endforeach()
    message(STATUS "${heading}:${_formatted}")
endfunction()

# Toolchain selection
if(NOT CMAKE_TOOLCHAIN_FILE OR CMAKE_TOOLCHAIN_FILE STREQUAL "")
    set(_toolchain_candidates "")
    set(_tt_metal_submodule_path "${CMAKE_CURRENT_SOURCE_DIR}/third-party/tt-metal")
    if(IS_DIRECTORY "${_tt_metal_submodule_path}/cmake")
        foreach(_toolchain_name IN ITEMS
                "x86_64-linux-clang-17-libstdcpp-toolchain.cmake"
                "x86_64-linux-clang-17-libcpp-toolchain.cmake")
            set(_candidate "${_tt_metal_submodule_path}/cmake/${_toolchain_name}")
            if(EXISTS "${_candidate}")
                list(APPEND _toolchain_candidates "${_candidate}")
            endif()
        endforeach()
    endif()
    set(_fallback_toolchain "${CMAKE_CURRENT_SOURCE_DIR}/cmake/x86_64-linux-torch-toolchain.cmake")
    if(EXISTS "${_fallback_toolchain}")
        list(APPEND _toolchain_candidates "${_fallback_toolchain}")
    endif()
    ttnn_log_list_var("Toolchain candidates (priority order)" _toolchain_candidates)
    foreach(_toolchain IN LISTS _toolchain_candidates)
        if(NOT CMAKE_TOOLCHAIN_FILE OR CMAKE_TOOLCHAIN_FILE STREQUAL "")
            set(CMAKE_TOOLCHAIN_FILE "${_toolchain}" CACHE FILEPATH "Toolchain file" FORCE)
            message(STATUS "Selected toolchain: ${CMAKE_TOOLCHAIN_FILE}")
            break()
        endif()
    endforeach()
endif()

project(ttnn_device_extension LANGUAGES CXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON CACHE BOOL "Generate compile_commands.json")
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

find_program(CCACHE_PROGRAM ccache)
if(CCACHE_PROGRAM)
    set(CMAKE_C_COMPILER_LAUNCHER "${CCACHE_PROGRAM}" CACHE STRING "C compiler launcher" FORCE)
    set(CMAKE_CXX_COMPILER_LAUNCHER "${CCACHE_PROGRAM}" CACHE STRING "CXX compiler launcher" FORCE)
    message(STATUS "Enabled ccache")
endif()

# TT-Metal detection
if(DEFINED ENV{TT_METAL_HOME} AND NOT "$ENV{TT_METAL_HOME}" STREQUAL "")
    message(WARNING "TT_METAL_HOME is deprecated and ignored. Using submodule auto-detection.")
    unset(ENV{TT_METAL_HOME})
endif()

set(_submodule_path "${CMAKE_CURRENT_SOURCE_DIR}/third-party/tt-metal")
if(IS_DIRECTORY "${_submodule_path}")
    set(TT_METAL_SUBMODULE_DIR "${_submodule_path}" CACHE PATH "TT-Metal submodule directory")
    message(STATUS "TT-Metal submodule: ${TT_METAL_SUBMODULE_DIR}")
else()
    message(FATAL_ERROR
        "TT-Metal submodule not found at ${_submodule_path}\n"
        "Run: git submodule update --init --recursive")
endif()

set(VERSION_NUMERIC "" CACHE STRING "tt-metal version")
if(VERSION_NUMERIC STREQUAL "")
    if(DEFINED ENV{TT_METAL_VERSION} AND NOT "$ENV{TT_METAL_VERSION}" STREQUAL "")
        set(VERSION_NUMERIC "$ENV{TT_METAL_VERSION}" CACHE STRING "tt-metal version" FORCE)
    elseif(DEFINED TT_METAL_SUBMODULE_DIR AND EXISTS "${TT_METAL_SUBMODULE_DIR}/.git")
        execute_process(
            COMMAND git describe --abbrev=0 --tags
            WORKING_DIRECTORY "${TT_METAL_SUBMODULE_DIR}"
            OUTPUT_VARIABLE _tt_metal_tag
            OUTPUT_STRIP_TRAILING_WHITESPACE
            ERROR_QUIET
        )
        if(NOT _tt_metal_tag STREQUAL "")
            string(REGEX REPLACE "^v" "" _tt_metal_version "${_tt_metal_tag}")
            set(VERSION_NUMERIC "${_tt_metal_version}" CACHE STRING "tt-metal version" FORCE)
        endif()
    endif()
endif()
if(VERSION_NUMERIC STREQUAL "")
    set(VERSION_NUMERIC "0.60.1" CACHE STRING "tt-metal version" FORCE)
endif()

# TT-Metal dependency discovery
set(CMAKE_FIND_PACKAGE_PREFER_CONFIG ON)
set(_expected_build_dir "build_${CMAKE_BUILD_TYPE}")
set(_build_dir "${TT_METAL_SUBMODULE_DIR}/${_expected_build_dir}")

if(NOT IS_DIRECTORY "${_build_dir}")
    message(FATAL_ERROR
        "TT-Metal build directory not found: ${_build_dir}\n"
        "Build TT-Metal first: cd ${TT_METAL_SUBMODULE_DIR} && ./build_metal.sh -b ${CMAKE_BUILD_TYPE} --enable-ccache")
endif()

set(_tt_metal_search_paths "${_build_dir}" "${TT_METAL_SUBMODULE_DIR}")

if(IS_DIRECTORY "${_build_dir}/_deps")
    file(GLOB _tt_metal_deps_dirs "${_build_dir}/_deps/*-build")
    foreach(_dep_dir ${_tt_metal_deps_dirs})
        if(EXISTS "${_dep_dir}" AND NOT _dep_dir MATCHES ".*tt-logger-build$")
            list(APPEND CMAKE_PREFIX_PATH "${_dep_dir}")
        endif()
    endforeach()
    if(EXISTS "${_build_dir}/lib/cmake")
        list(APPEND CMAKE_PREFIX_PATH "${_build_dir}/lib/cmake")
    endif()
endif()

# WORKAROUND: tt-logger CMake targets location inconsistency
if(EXISTS "${_build_dir}/_deps/tt-logger-build/CMakeFiles")
    file(GLOB _tt_logger_export_dirs "${_build_dir}/_deps/tt-logger-build/CMakeFiles/Export/*")
    foreach(_export_dir ${_tt_logger_export_dirs})
        if(EXISTS "${_export_dir}/tt-logger-targets.cmake")
            list(PREPEND CMAKE_PREFIX_PATH "${_export_dir}")
            break()
        endif()
    endforeach()
endif()

list(REMOVE_DUPLICATES CMAKE_PREFIX_PATH)

find_package(TT-Metalium CONFIG REQUIRED HINTS ${_tt_metal_search_paths} PATH_SUFFIXES lib/cmake)
find_package(TT-NN CONFIG QUIET HINTS ${_tt_metal_search_paths} PATH_SUFFIXES lib/cmake)

if(NOT TARGET TT::Metalium)
    message(FATAL_ERROR "TT::Metalium target not found. Rebuild TT-Metal.")
endif()

# Python discovery
set(Python_FIND_VIRTUALENV FIRST)
find_package(Python QUIET COMPONENTS Interpreter Development.Module)

if(Python_Interpreter_FOUND)
    set(PYTHON_EXECUTABLE "${Python_EXECUTABLE}")
endif()
if(Python_Development_Module_FOUND)
    set(PYTHON_INCLUDE_DIRS "${Python_INCLUDE_DIRS}")
    set(PYTHON_LIBRARIES "${Python_LIBRARIES}")
endif()

if(PYTHON_EXECUTABLE)
    if(NOT PYTHON_INCLUDE_DIRS)
        execute_process(
            COMMAND "${PYTHON_EXECUTABLE}" -c
                "import sysconfig, pathlib; candidates=[sysconfig.get_path('include'), sysconfig.get_path('platinclude')]; print(next((str(pathlib.Path(p)) for p in candidates if p), ''), end='')"
            OUTPUT_VARIABLE PYTHON_INCLUDE_DIRS
            OUTPUT_STRIP_TRAILING_WHITESPACE
            ERROR_QUIET
        )
    endif()
    if(NOT PYTHON_LIBRARIES)
        execute_process(
            COMMAND "${PYTHON_EXECUTABLE}" -c
                "import sysconfig, pathlib; libdir=sysconfig.get_config_var('LIBDIR') or ''; ldlib=sysconfig.get_config_var('LDLIBRARY') or ''; path=(pathlib.Path(libdir) / ldlib) if ldlib else pathlib.Path(); print(str(path) if ldlib else '', end='')"
            OUTPUT_VARIABLE PYTHON_LIBRARIES
            OUTPUT_STRIP_TRAILING_WHITESPACE
            ERROR_QUIET
        )
    endif()
endif()

if(NOT PYTHON_EXECUTABLE OR NOT PYTHON_INCLUDE_DIRS OR NOT PYTHON_LIBRARIES)
    include(find_python_workaround_ubuntu24 OPTIONAL)
endif()

if(NOT PYTHON_EXECUTABLE OR NOT PYTHON_INCLUDE_DIRS OR NOT PYTHON_LIBRARIES)
    message(FATAL_ERROR
        "Python development environment not found.\n"
        "Install: sudo apt-get install python3-dev\n"
        "Or set: PYTHON_EXECUTABLE, PYTHON_INCLUDE_DIRS, PYTHON_LIBRARIES")
endif()

if(NOT TARGET Python::Module)
    add_library(Python::Module UNKNOWN IMPORTED)
    set_target_properties(Python::Module PROPERTIES
        IMPORTED_LOCATION "${PYTHON_LIBRARIES}"
        INTERFACE_INCLUDE_DIRECTORIES "${PYTHON_INCLUDE_DIRS}")
endif()

# PyTorch discovery
if(PYTHON_EXECUTABLE)
    execute_process(
        COMMAND "${PYTHON_EXECUTABLE}" -c "import torch, sys; sys.stdout.write(torch.utils.cmake_prefix_path)"
        OUTPUT_VARIABLE _torch_prefix
        OUTPUT_STRIP_TRAILING_WHITESPACE
        ERROR_QUIET
    )
    if(NOT _torch_prefix STREQUAL "")
        string(REPLACE ":" ";" _torch_prefix_list "${_torch_prefix}")
        list(APPEND CMAKE_PREFIX_PATH ${_torch_prefix_list})
        list(REMOVE_DUPLICATES CMAKE_PREFIX_PATH)
        set(CMAKE_PREFIX_PATH "${CMAKE_PREFIX_PATH}" CACHE STRING "CMake search prefixes" FORCE)
    endif()
endif()

find_package(Torch REQUIRED CONFIG)

function(ttnn_link_torch_python target)
    if(TARGET Torch::Python)
        target_link_libraries(${target} PRIVATE Torch::Python)
        return()
    endif()
    if(PYTHON_EXECUTABLE)
        execute_process(
            COMMAND "${PYTHON_EXECUTABLE}" -c "import torch, pathlib; print(pathlib.Path(torch.__file__).resolve().parent / 'lib')"
            OUTPUT_VARIABLE _torch_lib_dir
            OUTPUT_STRIP_TRAILING_WHITESPACE
            ERROR_QUIET
        )
        if(_torch_lib_dir AND EXISTS "${_torch_lib_dir}")
            find_library(_torch_python_library NAMES torch_python PATHS "${_torch_lib_dir}" NO_DEFAULT_PATH)
        endif()
    endif()
    if(_torch_python_library)
        target_link_libraries(${target} PRIVATE "${_torch_python_library}")
    else()
        message(WARNING "torch_python library not found. Extension may fail to load.")
    endif()
endfunction()

# PyTorch ABI detection
set(ttnn_torch_abi_flags "")
if(DEFINED ENV{TORCH_ABI_FLAGS} AND NOT "$ENV{TORCH_ABI_FLAGS}" STREQUAL "")
    string(REPLACE " " ";" ttnn_torch_abi_flags "$ENV{TORCH_ABI_FLAGS}")
else()
    execute_process(
        COMMAND "${PYTHON_EXECUTABLE}" -c "import torch; print(torch.__config__.show())"
        OUTPUT_VARIABLE _torch_config
        ERROR_QUIET
    )
    if(_torch_config MATCHES "-D_GLIBCXX_USE_CXX11_ABI=([01])")
        set(ttnn_torch_abi_flags "-D_GLIBCXX_USE_CXX11_ABI=${CMAKE_MATCH_1}")
    endif()
endif()

# Extension target
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

add_library(ttnn_device_extension MODULE ${TTNN_CPP_EXTENSION_SOURCES})

target_include_directories(ttnn_device_extension PRIVATE
    ${Python_INCLUDE_DIRS}
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/include
)
if(TORCH_INCLUDE_DIRS)
    target_include_directories(ttnn_device_extension SYSTEM PRIVATE ${TORCH_INCLUDE_DIRS})
endif()

set(_torch_lib_dir "")
set(_tt_metal_lib_dir "")
if(PYTHON_EXECUTABLE)
    execute_process(
        COMMAND "${PYTHON_EXECUTABLE}" -c "import torch, pathlib; print(pathlib.Path(torch.__file__).parent / 'lib', end='')"
        OUTPUT_VARIABLE _torch_lib_dir
        OUTPUT_STRIP_TRAILING_WHITESPACE
        ERROR_QUIET
    )
endif()
if(EXISTS "${_build_dir}/lib")
    set(_tt_metal_lib_dir "${_build_dir}/lib")
endif()

set(_build_rpath "$ORIGIN")
set(_install_rpath "$ORIGIN")
if(_torch_lib_dir)
    set(_build_rpath "${_build_rpath}:${_torch_lib_dir}")
    set(_install_rpath "${_install_rpath}:\$ORIGIN/../torch/lib")
endif()
if(_tt_metal_lib_dir)
    set(_build_rpath "${_build_rpath}:${_tt_metal_lib_dir}")
endif()

set_target_properties(ttnn_device_extension PROPERTIES
    CXX_STANDARD 20
    PREFIX ""
    SUFFIX ""
    BUILD_RPATH "${_build_rpath}"
    INSTALL_RPATH "${_install_rpath}"
)

if(ttnn_torch_abi_flags)
    target_compile_options(ttnn_device_extension PRIVATE ${ttnn_torch_abi_flags})
endif()

target_compile_definitions(ttnn_device_extension PRIVATE
    FMT_HEADER_ONLY
    TORCH_EXTENSION_NAME=ttnn_device_extension
    TORCH_API_INCLUDE_EXTENSION_H
    NTEST
)

if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    target_compile_definitions(ttnn_device_extension PRIVATE DISABLE_NAMESPACE_STATIC_ASSERT)
endif()

# Linking
if(NOT TARGET TTNN::TTNN)
    message(FATAL_ERROR "TTNN::TTNN target not found. Rebuild TT-Metal.")
endif()

target_link_libraries(ttnn_device_extension PRIVATE
    TT::Metalium
    TTNN::TTNN
    Python::Module
)

if(TORCH_LIBRARIES)
    target_link_libraries(ttnn_device_extension PRIVATE ${TORCH_LIBRARIES})
endif()
if(TARGET Torch::Torch)
    target_link_libraries(ttnn_device_extension PRIVATE Torch::Torch)
endif()

ttnn_link_torch_python(ttnn_device_extension)

if(TORCH_CXX_FLAGS)
    string(REPLACE " " ";" TORCH_CXX_FLAGS_LIST "${TORCH_CXX_FLAGS}")
    target_compile_options(ttnn_device_extension PRIVATE ${TORCH_CXX_FLAGS_LIST})
endif()

set(_ttnn_output_name "ttnn_device_extension")
if(DEFINED OUTPUT_NAME AND NOT OUTPUT_NAME STREQUAL "")
    set(_ttnn_output_name "${OUTPUT_NAME}")
elseif(DEFINED ENV{OUTPUT_NAME} AND NOT "$ENV{OUTPUT_NAME}" STREQUAL "")
    set(_ttnn_output_name "$ENV{OUTPUT_NAME}")
endif()
set_target_properties(ttnn_device_extension PROPERTIES OUTPUT_NAME "${_ttnn_output_name}")

if(TTNN_BUILD_EXAMPLES)
    add_subdirectory(ttnn_cpp_extension/examples)
endif()

# Installation
set(_ttnn_install_destination "${SKBUILD_PLATLIB_DIR}/torch_ttnn_cpp_extension")
install(TARGETS ttnn_device_extension LIBRARY DESTINATION "${_ttnn_install_destination}")

set(_required_tt_libs
    libtt_metal.so
    libtt_stl.so
    libdevice.so
    libtracy.so
    libtracy.so.0.10.0
    _ttnncpp.so
)

foreach(_lib_name ${_required_tt_libs})
    set(_lib_path "${_build_dir}/lib/${_lib_name}")
    if(EXISTS "${_lib_path}")
        install(FILES "${_lib_path}" DESTINATION "${_ttnn_install_destination}" OPTIONAL)
    endif()
endforeach()

cmake_minimum_required(VERSION 3.23)

# Skip C++ extension build if SKIP_CPP_EXTENSION is set (for pure Python installations)
if(DEFINED ENV{SKIP_CPP_EXTENSION} AND "$ENV{SKIP_CPP_EXTENSION}" STREQUAL "1")
    message(STATUS "====================================================================")
    message(STATUS "SKIP_CPP_EXTENSION=1 detected - skipping C++ extension build")
    message(STATUS "Pure Python mode: torch-ttnn will be installed without native device support")
    message(STATUS "To enable C++ extension:")
    message(STATUS "  1. Unset SKIP_CPP_EXTENSION, or")
    message(STATUS "  2. Build tt-metal and install normally")
    message(STATUS "====================================================================")
    return()
endif()

# =============================================================================
# torch_ttnn C++ Extension Build System
# =============================================================================
#
# Builds ttnn_device_extension module for PyTorch-TTNN integration
#
# Prerequisites: ./build_cpp_extension.sh [BUILD_TYPE]
# Documentation: docs/BuildFlow.md
#
# Key Features:
# - Strict build type matching (CMAKE_BUILD_TYPE must match TT-Metal)
# - Auto-detects TT-Metal from submodule (third-party/tt-metal/build_${CMAKE_BUILD_TYPE})
# - Self-contained via RPATH (no LD_LIBRARY_PATH needed)
# - TT_METAL_HOME deprecated and ignored
#
# Dependencies:
# - TT-Metal: Pre-built, discovered via find_package(CONFIG)
# - PyTorch: Discovered from Python environment
# - Python: Development headers via find_package(Python)
# =============================================================================

# =============================================================================
# Toolchain Setup
# =============================================================================

if(NOT CMAKE_TOOLCHAIN_FILE OR CMAKE_TOOLCHAIN_FILE STREQUAL "")
    set(_toolchain_candidates "")

    # Check for TT-Metal provided toolchains (clang-17 based) in submodule
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

    # Fallback to torch toolchain (works with system compilers)
    set(_fallback_toolchain "${CMAKE_CURRENT_SOURCE_DIR}/cmake/x86_64-linux-torch-toolchain.cmake")
    if(EXISTS "${_fallback_toolchain}")
        list(APPEND _toolchain_candidates "${_fallback_toolchain}")
    endif()

    # Use first available toolchain
    foreach(_toolchain IN LISTS _toolchain_candidates)
        if(NOT CMAKE_TOOLCHAIN_FILE OR CMAKE_TOOLCHAIN_FILE STREQUAL "")
            set(CMAKE_TOOLCHAIN_FILE "${_toolchain}" CACHE FILEPATH "Toolchain file" FORCE)
            message(STATUS "Selected toolchain: ${CMAKE_TOOLCHAIN_FILE}")
            break()
        endif()
    endforeach()
endif()

project(ttnn_device_extension LANGUAGES CXX)

# =============================================================================
# Section 2: Project Declaration and Fundamental Configuration
# =============================================================================
#
# After toolchain selection, declare the project and set base properties.
#
# CMake best practices:
#   1. Declare project early (after toolchain is set)
#   2. Set standards and compile flags globally (applied to all targets)
#   3. Enable CMAKE_EXPORT_COMPILE_COMMANDS for IDE integration
#   4. Use CMAKE_POSITION_INDEPENDENT_CODE for shared libraries

set(CMAKE_EXPORT_COMPILE_COMMANDS ON CACHE BOOL
    "Generate compile_commands.json for IDE integration and debugging")

# Use C++20 standard (required for TT-Metal compatibility)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)  # Required for Python extensions

# =============================================================================
# Section 3: Build Tooling and Performance Optimization
# =============================================================================
#
# Enable compiler caching (ccache) when available.
#
# WHY: This significantly speeds up incremental builds, especially important
#      for development when you're modifying code frequently.
#
# HOW: We search for ccache in PATH and set it as the compiler launcher.
#      This intercepts all compile commands and caches their results.
#
# NOTE: ccache is optional. If not found, builds proceed normally (just slower).

find_program(CCACHE_PROGRAM ccache)
if(CCACHE_PROGRAM)
    set(CMAKE_C_COMPILER_LAUNCHER "${CCACHE_PROGRAM}" CACHE STRING "C compiler launcher" FORCE)
    set(CMAKE_CXX_COMPILER_LAUNCHER "${CCACHE_PROGRAM}" CACHE STRING "CXX compiler launcher" FORCE)
    message(STATUS "Enabled ccache for faster compilation")
endif()

# Add our CMake utilities to the module search path
list(PREPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")
include(utils)

# =============================================================================
# Section 4: TT-Metal Location and Version Detection
# =============================================================================
#
# TT-Metal is auto-detected from submodule at third-party/tt-metal
# $ENV{TT_METAL_HOME} is DEPRECATED and actively IGNORED (prevents build conflicts)
# Version detected from git tag, TT_METAL_VERSION env var, or hardcoded default

# Detect and ignore TT_METAL_HOME environment variable if set
if(DEFINED ENV{TT_METAL_HOME} AND NOT "$ENV{TT_METAL_HOME}" STREQUAL "")
    message(WARNING
        "\n"
        "========================================================================\n"
        "WARNING: TT_METAL_HOME environment variable detected and IGNORED\n"
        "========================================================================\n"
        "\n"
        "Detected: TT_METAL_HOME=$ENV{TT_METAL_HOME}\n"
        "\n"
        "This environment variable is DEPRECATED and will be IGNORED to prevent\n"
        "build conflicts when switching between TT projects (tt-metal, tt-train, etc.).\n"
        "\n"
        "TT-Metal will be auto-detected from the submodule at:\n"
        "  ${CMAKE_CURRENT_SOURCE_DIR}/third-party/tt-metal\n"
        "\n"
        "To suppress this warning: unset TT_METAL_HOME\n"
        "========================================================================\n")
    # Explicitly unset to prevent any accidental usage
    unset(ENV{TT_METAL_HOME})
endif()

# TT-Metal is always at: third-party/tt-metal (git submodule)
set(_submodule_path "${CMAKE_CURRENT_SOURCE_DIR}/third-party/tt-metal")
if(IS_DIRECTORY "${_submodule_path}")
    set(TT_METAL_SUBMODULE_DIR "${_submodule_path}" CACHE PATH
        "Path to the tt-metal submodule directory (auto-detected)")
    message(STATUS "✓ TT-Metal auto-detected from submodule: ${TT_METAL_SUBMODULE_DIR}")
else()
    message(FATAL_ERROR
        "\n"
        "========================================================================\n"
        "FATAL: TT-Metal submodule not found\n"
        "========================================================================\n"
        "\n"
        "Expected location: ${_submodule_path}\n"
        "\n"
        "SOLUTION: Initialize git submodules:\n"
        "  cd ${CMAKE_SOURCE_DIR}\n"
        "  git submodule update --init --recursive\n"
        "\n"
        "NOTE: TT_METAL_HOME environment variable is deprecated and ignored.\n"
        "      TT-Metal is always auto-detected from the submodule location.\n"
        "========================================================================\n")
endif()

# Determine TT-Metal version for metadata and compatibility checking
set(VERSION_NUMERIC "" CACHE STRING "tt-metal version used to build the extension")
if(VERSION_NUMERIC STREQUAL "")
    # Try environment variable first (CI override)
    if(DEFINED ENV{TT_METAL_VERSION} AND NOT "$ENV{TT_METAL_VERSION}" STREQUAL "")
        set(VERSION_NUMERIC "$ENV{TT_METAL_VERSION}" CACHE STRING "tt-metal version used to build the extension" FORCE)
    # Fall back to git tag detection
    elseif(DEFINED TT_METAL_SUBMODULE_DIR AND EXISTS "${TT_METAL_SUBMODULE_DIR}/.git")
        execute_process(
            COMMAND git describe --abbrev=0 --tags
            WORKING_DIRECTORY "${TT_METAL_SUBMODULE_DIR}"
            OUTPUT_VARIABLE _tt_metal_tag
            OUTPUT_STRIP_TRAILING_WHITESPACE
            ERROR_QUIET
        )
        if(NOT _tt_metal_tag STREQUAL "")
            # Remove 'v' prefix if present (e.g., "v0.63.0" -> "0.63.0")
            string(REGEX REPLACE "^v" "" _tt_metal_version "${_tt_metal_tag}")
            set(VERSION_NUMERIC "${_tt_metal_version}" CACHE STRING "tt-metal version used to build the extension" FORCE)
        endif()
    endif()
endif()

# Default fallback version (updated when switching tt-metal branches)
if(VERSION_NUMERIC STREQUAL "")
    set(VERSION_NUMERIC "0.60.1" CACHE STRING "tt-metal version used to build the extension" FORCE)
endif()

message(STATUS "Building extension for tt-metal version: ${VERSION_NUMERIC}")

# =============================================================================
# Section 5: TT-Metal Dependency Discovery
# =============================================================================
#
# Discovers TT-Metal CMake package configs from the build tree.
# Phase 1 (build_metal.sh) creates configs in build_${CMAKE_BUILD_TYPE}/lib/cmake/.
# STRICT: Uses ONLY the directory matching CMAKE_BUILD_TYPE (e.g., Debug → build_Debug)
# Imports TT::Metalium and TTNN::* targets for linking.

# Prefer config-mode packages (TT-MetaliumConfig.cmake) over MODULE mode
# This is the modern CMake approach
set(CMAKE_FIND_PACKAGE_PREFER_CONFIG ON)

# Build the list of directories to search for TT-Metal package configs
# STRICT: We ONLY use the directory matching CMAKE_BUILD_TYPE
# No fallbacks - Debug build must use Debug tt-metal, Release must use Release, etc.
set(_tt_metal_search_paths "")

# Determine expected build directory based on CMAKE_BUILD_TYPE
# Note: TT_METAL_SUBMODULE_DIR is already validated above, always defined at this point
set(_expected_build_dir "build_${CMAKE_BUILD_TYPE}")
    
# Check that the matching build directory exists
if(NOT IS_DIRECTORY "${TT_METAL_SUBMODULE_DIR}/${_expected_build_dir}")
    message(FATAL_ERROR 
        "========================================================================\n"
        "TT-Metal build directory not found for CMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}\n"
        "\n"
        "Expected: ${TT_METAL_SUBMODULE_DIR}/${_expected_build_dir}\n"
        "\n"
        "You must build TT-Metal in ${CMAKE_BUILD_TYPE} mode first:\n"
        "  cd torch_ttnn/cpp_extension\n"
        "  ./build_cpp_extension.sh ${CMAKE_BUILD_TYPE}\n"
        "\n"
        "Or manually:\n"
        "  cd torch_ttnn/cpp_extension/third-party/tt-metal\n"
        "  ./build_metal.sh -b ${CMAKE_BUILD_TYPE} --enable-ccache\n"
        "========================================================================\n"
    )
endif()

# Add ONLY the matching build directory (strict)
list(APPEND _tt_metal_search_paths "${TT_METAL_SUBMODULE_DIR}/${_expected_build_dir}")
message(STATUS "Using TT-Metal build directory: ${_expected_build_dir} (matches CMAKE_BUILD_TYPE)")

# Add submodule root for toolchain files and other configs
list(APPEND _tt_metal_search_paths "${TT_METAL_SUBMODULE_DIR}")

# CRITICAL FIX: Add TT-Metal's dependency paths to CMAKE_PREFIX_PATH
# This allows CMake to find transitive dependencies (fmt, protobuf, umd, etc.)
# that tt-metalium-config.cmake and tt-nn-config.cmake require

# Priority 1: Add transitive deps from the actual TT-Metal build directory
# (these are packages that tt-metalium depends on)
# Use ONLY the directory matching CMAKE_BUILD_TYPE
set(_expected_build_dir "build_${CMAKE_BUILD_TYPE}")
set(_build_dir "${TT_METAL_SUBMODULE_DIR}/${_expected_build_dir}")
if(IS_DIRECTORY "${_build_dir}/_deps")
    # Add cmake configs from _deps/*-build directories
    # EXCEPTION: Skip tt-logger-build because its config file has incorrect hardcoded paths
    # to tt-logger-targets.cmake. The workaround below adds the correct Export directory instead.
    file(GLOB _tt_metal_deps_dirs "${_build_dir}/_deps/*-build")
    foreach(_dep_dir ${_tt_metal_deps_dirs})
        if(EXISTS "${_dep_dir}" AND NOT _dep_dir MATCHES ".*tt-logger-build$")
            list(APPEND CMAKE_PREFIX_PATH "${_dep_dir}")
            message(STATUS "Added TT-Metal dep: ${_dep_dir}")
        endif()
    endforeach()
    
    # Also add the main lib/cmake directory for packages like umd that are installed there
    if(EXISTS "${_build_dir}/lib/cmake")
        list(APPEND CMAKE_PREFIX_PATH "${_build_dir}/lib/cmake")
        message(STATUS "Added TT-Metal build cmake: ${_build_dir}/lib/cmake")
    endif()
    message(STATUS "Added TT-Metal transitive dependency paths from: ${_build_dir}/_deps")
else()
    message(STATUS "No TT-Metal transitive dependencies directory found (may not be needed)")
endif()

list(REMOVE_DUPLICATES CMAKE_PREFIX_PATH)

# WORKAROUND: tt-logger CMake targets file location inconsistency (APPLY FIRST)
# During CPM builds in TT-Metal, tt-logger-targets.cmake is generated in 
# CMakeFiles/Export/*/tt-logger-targets.cmake instead of cmake/
# This workaround MUST run BEFORE find_package calls that depend on tt-logger

# Use ONLY the directory matching CMAKE_BUILD_TYPE
set(_expected_build_dir "build_${CMAKE_BUILD_TYPE}")
if(EXISTS "${TT_METAL_SUBMODULE_DIR}/${_expected_build_dir}/_deps/tt-logger-build/CMakeFiles")
    # Find the actual export directory
    file(GLOB _tt_logger_export_dirs 
        "${TT_METAL_SUBMODULE_DIR}/${_expected_build_dir}/_deps/tt-logger-build/CMakeFiles/Export/*")
    foreach(_export_dir ${_tt_logger_export_dirs})
        if(EXISTS "${_export_dir}/tt-logger-targets.cmake")
            list(PREPEND CMAKE_PREFIX_PATH "${_export_dir}")
            message(STATUS "WORKAROUND: Added tt-logger export path: ${_export_dir}")
            break()
        endif()
    endforeach()
endif()

# Try to find TT-Metalium (uppercase variant first for compatibility)
find_package(TT-Metalium CONFIG QUIET
    HINTS ${_tt_metal_search_paths}
    PATH_SUFFIXES lib/cmake
)

# Fallback: try lowercase variant (tt-metalium) which is what TT-Metal actually installs
if(NOT TT-Metalium_FOUND)
    find_package(tt-metalium CONFIG QUIET
        HINTS ${_tt_metal_search_paths}
        PATH_SUFFIXES lib/cmake
    )
    # If found, create an alias so the rest of the code uses uppercase names
    if(tt-metalium_FOUND AND NOT TT-Metalium_FOUND)
        if(TARGET tt-metalium::tt-metalium)
            add_library(TT::Metalium ALIAS tt-metalium::tt-metalium)
            set(TT-Metalium_FOUND TRUE)
        endif()
    endif()
endif()

# Try to find TT-NN (uppercase variant first for compatibility)
find_package(TT-NN CONFIG QUIET
    HINTS ${_tt_metal_search_paths}
    PATH_SUFFIXES lib/cmake
)

# Fallback: try lowercase variant (tt-nn) which is what TT-Metal actually installs
if(NOT TT-NN_FOUND)
    find_package(tt-nn CONFIG QUIET
        HINTS ${_tt_metal_search_paths}
        PATH_SUFFIXES lib/cmake
    )
    # TT-Metal's tt-nn package exports uppercase targets (TTNN::TTNN, TTNN::Python)
    # so we just mark that we found them
    if(tt-nn_FOUND AND NOT TT-NN_FOUND)
        set(TT-NN_FOUND TRUE)
        message(STATUS "Found tt-nn (lowercase) package - targets already use TTNN:: names")
    endif()
endif()

# Check for TT::Metalium (core library) - this MUST exist
if(NOT TARGET TT::Metalium)
    message(FATAL_ERROR
        "\n"
        "========================================================================\n"
        "FATAL: TT-Metalium CMake target not found!\n"
        "========================================================================\n"
        "\n"
        "TT-Metal submodule location: ${TT_METAL_SUBMODULE_DIR}\n"
        "But it doesn't provide the expected TT::Metalium imported target.\n"
        "\n"
        "This usually means:\n"
        "  1. Phase 1 (TT-Metal build) has not completed successfully\n"
        "  2. TT-Metal was built without generating CMake package configs\n"
        "\n"
        "To fix this, rebuild TT-Metal:\n"
        "\n"
        "  cd torch_ttnn/cpp_extension/third-party/tt-metal\n"
        "  ./build_metal.sh --release --enable-ccache\n"
        "\n"
        "This generates CMake package configs at:\n"
        "  torch_ttnn/cpp_extension/third-party/tt-metal/build_<TYPE>/lib/cmake/TT-MetaliumConfig.cmake\n"
        "  (where <TYPE> is Release, Debug, RelWithDebInfo, etc.)\n"
        "\n"
        "After rebuilding, retry this project:\n"
        "  python -m pip install -e . --no-build-isolation --force-reinstall\n"
        "\n"
        "========================================================================\n"
    )
endif()

# Check for TTNN targets (at least one should be available)
set(_ttnn_targets_found FALSE)
foreach(_ttnn_target IN ITEMS TTNN::CPP TTNN::TTNN)
    if(TARGET ${_ttnn_target})
        set(_ttnn_targets_found TRUE)
        message(STATUS "Found TTNN target: ${_ttnn_target}")
        break()
    endif()
endforeach()

if(NOT _ttnn_targets_found)
    message(FATAL_ERROR
        "\n"
        "========================================================================\n"
        "FATAL: TTNN CMake targets not found!\n"
        "========================================================================\n"
        "\n"
        "TT-Metal submodule location: ${TT_METAL_SUBMODULE_DIR}\n"
        "And it provides TT::Metalium, but no TTNN targets are available.\n"
        "\n"
        "This usually means TT-Metal was built without TTNN support.\n"
        "\n"
        "To fix this, rebuild TT-Metal:\n"
        "\n"
        "  cd torch_ttnn/cpp_extension/third-party/tt-metal\n"
        "  ./build_metal.sh --release --enable-ccache\n"
        "\n"
        "By default, TT-Metal builds WITH_PYTHON_BINDINGS=ON, which includes\n"
        "TTNN support. If you see this error, the build may have been\n"
        "interrupted or misconfigured.\n"
        "\n"
        "After rebuilding, retry:\n"
        "  python -m pip install -e . --no-build-isolation --force-reinstall\n"
        "\n"
        "========================================================================\n"
    )
endif()

# Debug Information: Provide diagnostic information for troubleshooting
message(STATUS "TT-Metal Discovery Results:")
message(STATUS "  TT-Metal location (auto-detected): ${TT_METAL_SUBMODULE_DIR}")
if(TT-Metalium_FOUND)
    message(STATUS "  TT-MetaliumConfig.cmake: ${TT-Metalium_CONFIG}")
else()
    message(STATUS "  TT-Metalium: Not found")
endif()

if(TT-NN_FOUND)
    message(STATUS "  TT-NNConfig.cmake: ${TT-NN_CONFIG}")
else()
    message(STATUS "  TT-NN: Not found (optional)")
endif()

# List available targets for user reference
message(STATUS "Available TTNN targets:")
foreach(_ttnn_target IN ITEMS TTNN::CPP TTNN::TTNN)
    if(TARGET ${_ttnn_target})
        message(STATUS "  ✓ ${_ttnn_target}")
    endif()
endforeach()

message(STATUS "TT-Metal package discovery completed successfully.")

# =============================================================================
# Section 6: Python Development Environment Discovery
# =============================================================================
#
# WHAT THIS SECTION DOES:
#   Locates Python interpreter, headers, and libraries needed to build extensions
#
# THREE REQUIRED COMPONENTS:
#   1. Python interpreter (python executable)
#      Used for: running setup code, importing torch, extracting ABI flags
#
#   2. Python development headers (Python.h)
#      Used for: compiling extension code that calls Python C API
#
#   3. Python library (libpython)
#      Used for: linking the extension module
#
# WHY THIS IS TRICKY:
#   In virtual environments, Python detection sometimes fails because:
#     - CMake looks in system paths first
#     - Virtual env headers aren't always symlinked
#     - Ubuntu 24.04 has known CMake Python discovery issues
#   We work around this with fallback mechanisms
#
# STRATEGY (in order of preference):
#   1. Try standard CMake find_package(Python ...) - works 90% of the time
#   2. Fallback: Use sysconfig to find paths manually
#   3. Last resort: Ubuntu 24.04 workaround
#
# CMake best practices:
#   - Development.Module = header-only module (preferred for extensions)
#   - Development = full Python library (more general but heavier)
#   - Python_FIND_VIRTUALENV = FIRST (prefer venv over system Python)

# Request specific Python components we need
set(_python_components Interpreter Development.Module)
set(Python_FIND_VIRTUALENV FIRST)  # Prefer virtualenv Python when active

# Try standard CMake Python discovery first
find_package(Python QUIET COMPONENTS ${_python_components})

# Extract the discovered paths (CMake 3.15+ style variables)
if(Python_Interpreter_FOUND)
    set(PYTHON_EXECUTABLE "${Python_EXECUTABLE}")
endif()
if(Python_Development_Module_FOUND)
    set(PYTHON_INCLUDE_DIRS "${Python_INCLUDE_DIRS}")
    set(PYTHON_LIBRARIES "${Python_LIBRARIES}")
endif()

# Fallback: Use sysconfig to discover paths when CMake fails
# This is common in virtual environments where CMake can't find the headers
if(PYTHON_EXECUTABLE)
    # Get include directory using Python's sysconfig
    if(NOT PYTHON_INCLUDE_DIRS)
        execute_process(
            COMMAND "${PYTHON_EXECUTABLE}" -c
                "import sysconfig, pathlib; candidates=[sysconfig.get_path('include'), sysconfig.get_path('platinclude')]; print(next((str(pathlib.Path(p)) for p in candidates if p), ''), end='')"
            OUTPUT_VARIABLE _python_include_guess
            OUTPUT_STRIP_TRAILING_WHITESPACE
        )
        if(_python_include_guess AND EXISTS "${_python_include_guess}")
            set(PYTHON_INCLUDE_DIRS "${_python_include_guess}")
            message(STATUS "Found Python include dir via sysconfig: ${PYTHON_INCLUDE_DIRS}")
        endif()
    endif()

    # Get library path using Python's sysconfig
    if(NOT PYTHON_LIBRARIES)
        execute_process(
            COMMAND "${PYTHON_EXECUTABLE}" -c
                "import sysconfig, pathlib; libdir=sysconfig.get_config_var('LIBDIR') or ''; ldlib=sysconfig.get_config_var('LDLIBRARY') or ''; path=(pathlib.Path(libdir) / ldlib) if ldlib else pathlib.Path(); print(str(path) if ldlib else '', end='')"
            OUTPUT_VARIABLE _python_library_guess
            OUTPUT_STRIP_TRAILING_WHITESPACE
        )
        if(_python_library_guess AND EXISTS "${_python_library_guess}")
            set(PYTHON_LIBRARIES "${_python_library_guess}")
            message(STATUS "Found Python library via sysconfig: ${PYTHON_LIBRARIES}")
        endif()
    endif()
endif()

# Last resort: Ubuntu 24.04 specific workarounds
# Some systems have issues with standard Python discovery
if(NOT PYTHON_EXECUTABLE OR NOT PYTHON_INCLUDE_DIRS OR NOT PYTHON_LIBRARIES)
    include(find_python_workaround_ubuntu24 OPTIONAL)
endif()

# Final validation: Ensure we have all required components
if(NOT PYTHON_EXECUTABLE OR NOT PYTHON_INCLUDE_DIRS OR NOT PYTHON_LIBRARIES)
    message(FATAL_ERROR
        "Unable to locate a complete Python development environment.\n"
        "\n"
        "Required components:\n"
        "  - Python interpreter: ${PYTHON_EXECUTABLE}\n"
        "  - Include directories: ${PYTHON_INCLUDE_DIRS}\n"
        "  - Library: ${PYTHON_LIBRARIES}\n"
        "\n"
        "Solutions:\n"
        "  1. Install python3-dev: sudo apt-get install python3-dev\n"
        "  2. Set environment variables: PYTHON_EXECUTABLE, PYTHON_INCLUDE_DIRS, PYTHON_LIBRARIES\n"
        "  3. Activate a virtual environment with development headers\n"
        "  4. Use a conda environment with python installed")
endif()

# Ensure we have the Python::Module imported target for linking
# This is the standard CMake target that extensions should link against
if(NOT TARGET Python::Module)
    add_library(Python::Module UNKNOWN IMPORTED)
    set_target_properties(Python::Module PROPERTIES
        IMPORTED_LOCATION "${PYTHON_LIBRARIES}"
        INTERFACE_INCLUDE_DIRECTORIES "${PYTHON_INCLUDE_DIRS}"
    )
    message(STATUS "Created Python::Module imported target")
endif()

# =============================================================================
# Section 7: PyTorch Discovery and ABI Compatibility Detection
# =============================================================================
#
# WHAT THIS SECTION DOES:
#   1. Locates PyTorch installation and CMake configuration
#   2. Auto-detects C++ ABI compatibility flags
#   3. Provides PyTorch imported targets for linking
#
# WHY THIS IS COMPLEX:
#   PyTorch has two different C++ standard library ABIs:
#     - Old ABI: _GLIBCXX_USE_CXX11_ABI=0 (pre-C++11, rare now)
#     - New ABI: _GLIBCXX_USE_CXX11_ABI=1 (C++11+, standard now)
#   
#   If our extension uses a different ABI than PyTorch:
#     → Runtime crashes with "undefined symbol" errors
#     → Very hard to debug (looks like missing library)
#   
#   Solution: Auto-detect PyTorch's ABI and force our code to match
#
# STRATEGY FOR PYTORCH DISCOVERY:
#   1. Call torch.utils.cmake_prefix_path to get PyTorch's CMake dir
#   2. Add that to CMAKE_PREFIX_PATH (let PyTorch recommend its path)
#   3. Call find_package(Torch CONFIG) to import targets
#   4. Use Torch::Torch, Torch::Python, etc.
#
# STRATEGY FOR ABI DETECTION:
#   1. Check TORCH_ABI_FLAGS env var (user override)
#   2. Parse torch.__config__.show() output for ABI flags
#   3. Apply these flags when compiling our code
#
# NOTE: This is the ONE place where we modify CMAKE_PREFIX_PATH.
#       We do it AFTER finding TT-Metal so it doesn't interfere.

# Use PyTorch's utility to find its installation paths
# This is the recommended way to locate PyTorch for CMake integration
if(PYTHON_EXECUTABLE)
    execute_process(
        COMMAND "${PYTHON_EXECUTABLE}" -c "import torch, sys; sys.stdout.write(torch.utils.cmake_prefix_path)"
        OUTPUT_VARIABLE _torch_prefix
        OUTPUT_STRIP_TRAILING_WHITESPACE
        ERROR_QUIET
    )
    if(NOT _torch_prefix STREQUAL "")
        # torch.utils.cmake_prefix_path returns colon-separated paths
        string(REPLACE ":" ";" _torch_prefix_list "${_torch_prefix}")
        foreach(_prefix IN LISTS _torch_prefix_list)
            list(APPEND CMAKE_PREFIX_PATH "${_prefix}")
        endforeach()
        list(REMOVE_DUPLICATES CMAKE_PREFIX_PATH)
        set(CMAKE_PREFIX_PATH "${CMAKE_PREFIX_PATH}" CACHE STRING "CMake search prefixes" FORCE)
        message(STATUS "Added PyTorch paths to CMAKE_PREFIX_PATH: ${_torch_prefix_list}")
    endif()
endif()

# Find PyTorch using its CMake configuration
find_package(Torch REQUIRED CONFIG)

# =============================================================================
# PyTorch Python Integration Helper
# =============================================================================
#
# PyTorch provides a torch_python library that enables Python extension integration.
# However, different PyTorch installations may expose this library differently:
# - Some provide Torch::Python imported target
# - Others require manual library discovery
#
# This helper function abstracts away these differences and ensures proper linking.
#
# CMake best practice: Encapsulate complex discovery logic in helper functions
# rather than duplicating it throughout the build system.

function(ttnn_link_torch_python target)
    # First, try the standard PyTorch imported target (preferred)
    if(TARGET Torch::Python)
        target_link_libraries(${target} PRIVATE Torch::Python)
        message(STATUS "Linked ${target} against Torch::Python imported target")
        return()
    endif()

    # Fallback: Manually locate torch_python library
    # This handles PyTorch installations that don't provide imported targets
    set(_torch_python_hint_dirs "")

    # Check PyTorch's reported library directories
    if(DEFINED TORCH_LIBRARY_DIRS AND TORCH_LIBRARY_DIRS)
        list(APPEND _torch_python_hint_dirs ${TORCH_LIBRARY_DIRS})
    endif()

    # Infer from torch target's location
    if(TARGET torch)
        get_target_property(_torch_imported_location torch IMPORTED_LOCATION)
        if(_torch_imported_location)
            get_filename_component(_torch_library_dir "${_torch_imported_location}" DIRECTORY)
            list(APPEND _torch_python_hint_dirs "${_torch_library_dir}")
        endif()
    endif()

    # Infer from Torch_DIR (where PyTorch's CMake files are located)
    if(DEFINED Torch_DIR AND NOT Torch_DIR STREQUAL "")
        get_filename_component(_torch_cmake_dir "${Torch_DIR}" REALPATH)
        # Torch_DIR is typically .../lib/python3.x/site-packages/torch/share/cmake/Torch
        # We want .../lib/python3.x/site-packages/torch/lib
        get_filename_component(_torch_prefix "${_torch_cmake_dir}/../../.." REALPATH)
        list(APPEND _torch_python_hint_dirs "${_torch_prefix}/lib")
    endif()

    # Use Python to find torch installation directory
    if(DEFINED PYTHON_EXECUTABLE AND NOT PYTHON_EXECUTABLE STREQUAL "")
        execute_process(
            COMMAND "${PYTHON_EXECUTABLE}" -c "import torch, pathlib; print(pathlib.Path(torch.__file__).resolve().parent / 'lib')"
            OUTPUT_VARIABLE _torch_python_libdir
            OUTPUT_STRIP_TRAILING_WHITESPACE
            ERROR_QUIET
        )
        if(_torch_python_libdir AND EXISTS "${_torch_python_libdir}")
            list(APPEND _torch_python_hint_dirs "${_torch_python_libdir}")
        endif()
    endif()

    list(REMOVE_DUPLICATES _torch_python_hint_dirs)
    message(STATUS "Searching for torch_python library in: ${_torch_python_hint_dirs}")

    # Perform the actual library search
    if(_torch_python_hint_dirs)
        find_library(_torch_python_library
            NAMES torch_python
            PATHS ${_torch_python_hint_dirs}
        )
    else()
        find_library(_torch_python_library NAMES torch_python)
    endif()

    # Apply the linking
    if(_torch_python_library)
        target_link_libraries(${target} PRIVATE "${_torch_python_library}")
        message(STATUS "Linked ${target} against torch_python library: ${_torch_python_library}")
    else()
        message(WARNING
            "torch_python library not found. The TTNN device extension may fail to load.\n"
            "This usually indicates an incomplete PyTorch installation.")
    endif()
endfunction()


# =============================================================================
# PyTorch ABI Compatibility Detection
# =============================================================================
#
# The GNU C++ standard library has two ABI versions:
# - Old ABI (pre-C++11): _GLIBCXX_USE_CXX11_ABI=0
# - New ABI (C++11 and later): _GLIBCXX_USE_CXX11_ABI=1
#
# PyTorch wheels are built with a specific ABI, and our extension must match it.
# Failure to match causes runtime crashes due to incompatible standard library.
#
# CMake best practice: Detect and propagate ABI flags automatically rather than
# hardcoding them. Allow user override via environment variables.

set(ttnn_torch_abi_flags "")
if(DEFINED ENV{TORCH_ABI_FLAGS} AND NOT "$ENV{TORCH_ABI_FLAGS}" STREQUAL "")
    # Allow user override via environment variable
    string(REPLACE " " ";" ttnn_torch_abi_flags "$ENV{TORCH_ABI_FLAGS}")
    message(STATUS "Using user-specified Torch ABI flags: ${ttnn_torch_abi_flags}")
else()
    # Auto-detect from PyTorch's configuration
    execute_process(
        COMMAND "${PYTHON_EXECUTABLE}" -c "import torch; print(torch.__config__.show())"
        OUTPUT_VARIABLE _torch_config
        ERROR_QUIET
    )
    if(_torch_config MATCHES "-D_GLIBCXX_USE_CXX11_ABI=([01])")
        set(ttnn_torch_abi_flags "-D_GLIBCXX_USE_CXX11_ABI=${CMAKE_MATCH_1}")
        message(STATUS "Auto-detected Torch ABI flag: ${ttnn_torch_abi_flags}")
    else()
        message(WARNING
            "Could not detect PyTorch ABI flags from torch.__config__.show().\n"
            "The extension may fail at runtime due to ABI mismatches.\n"
            "Set TORCH_ABI_FLAGS environment variable if you encounter issues.")
    endif()
endif()

# =============================================================================
# Source Files and Target Definition
# =============================================================================
#
# Define the source files that comprise the TTNN device extension. These implement
# the bridge between PyTorch and TTNN hardware acceleration.
#
# The extension provides:
# - Core TTNN integration (TtnnTensorImpl, TtnnGuard, etc.)
# - PyTorch operation implementations (binary, unary, creation ops)
# - Device management utilities
# - Python extension bindings

set(TTNN_CPP_EXTENSION_SOURCES
    # Main extension entry point and registration
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/open_registration_extension.cpp

    # Core TTNN integration components
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/core/copy.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/core/TtnnCustomAllocator.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/core/TtnnGuard.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/core/TtnnTensorImpl.cpp

    # PyTorch operation implementations
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/ops/binary.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/ops/creation.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/ops/unary.cpp

    # Utility functions and device management
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/utils/device.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/src/utils/vector_utils.cpp
)

# =============================================================================
# Section: Build the TTNN Device Extension
# =============================================================================
#
# Create the Python extension module. This is a MODULE library (not SHARED) because
# it's loaded by Python's import system, not linked by other C++ code.
#
# CMake best practices for Python extensions:
# - Use MODULE library type for Python extensions
# - Set PREFIX "" and SUFFIX "" to avoid library prefixes/suffixes
# - Use $ORIGIN in RPATH for self-contained distribution
# - Enable POSITION_INDEPENDENT_CODE for shared library compatibility

add_library(ttnn_device_extension MODULE ${TTNN_CPP_EXTENSION_SOURCES})

# Include directories (SYSTEM to suppress warnings from external headers)
target_include_directories(ttnn_device_extension PRIVATE
    ${Python_INCLUDE_DIRS}  # Python headers for extension API
)
if(DEFINED TORCH_INCLUDE_DIRS AND TORCH_INCLUDE_DIRS)
    target_include_directories(ttnn_device_extension SYSTEM PRIVATE ${TORCH_INCLUDE_DIRS})
endif()
target_include_directories(ttnn_device_extension PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/ttnn_cpp_extension/include  # Our own headers
)

# Detect PyTorch library directory for RPATH
# This ensures the extension can find PyTorch's C++ libraries at runtime without LD_LIBRARY_PATH
set(_torch_lib_dir "")
if(PYTHON_EXECUTABLE)
    execute_process(
        COMMAND "${PYTHON_EXECUTABLE}" -c "import torch, pathlib; print(pathlib.Path(torch.__file__).parent / 'lib', end='')"
        OUTPUT_VARIABLE _torch_lib_dir
        OUTPUT_STRIP_TRAILING_WHITESPACE
        ERROR_QUIET
    )
    if(_torch_lib_dir AND EXISTS "${_torch_lib_dir}")
        message(STATUS "Detected PyTorch library directory for RPATH: ${_torch_lib_dir}")
    else()
        message(WARNING "Could not detect PyTorch library directory. Extension may require LD_LIBRARY_PATH at runtime.")
        set(_torch_lib_dir "")
    endif()
endif()

# Detect TT-Metal library directory for RPATH
# This ensures the extension can find TT-Metal's libraries (libtracy, libtt_metal, etc.) at runtime
# STRICT: We ONLY use the directory matching CMAKE_BUILD_TYPE (no fallbacks)
set(_expected_build_dir "build_${CMAKE_BUILD_TYPE}")
set(_tt_metal_lib_dir "")

# Use ONLY the matching build directory (strict)
if(EXISTS "${TT_METAL_SUBMODULE_DIR}/${_expected_build_dir}/lib")
    set(_tt_metal_lib_dir "${TT_METAL_SUBMODULE_DIR}/${_expected_build_dir}/lib")
    message(STATUS "Detected TT-Metal library directory for RPATH: ${_tt_metal_lib_dir}")
else()
    message(WARNING "TT-Metal library directory not found: ${TT_METAL_SUBMODULE_DIR}/${_expected_build_dir}/lib")
    message(WARNING "Extension may fail to load TT-Metal libraries at runtime.")
endif()

# Build comprehensive RPATH that includes PyTorch and TT-Metal library directories
# This allows the extension to find all dependencies at runtime without LD_LIBRARY_PATH
set(_build_rpath "$ORIGIN")
set(_install_rpath "$ORIGIN")

# Add PyTorch library directory
if(_torch_lib_dir)
    # BUILD_RPATH: Use absolute path to PyTorch for build-time linking
    set(_build_rpath "${_build_rpath}:${_torch_lib_dir}")
    # INSTALL_RPATH: Use relative path - at runtime, torch_ttnn and torch are both in site-packages
    # The extension is at: site-packages/torch_ttnn_cpp_extension/ttnn_device_extension
    # PyTorch is at:       site-packages/torch/lib/
    # Relative path:       ../torch/lib (ONE level up, not two!)
    set(_install_rpath "${_install_rpath}:\$ORIGIN/../torch/lib")
endif()

# Add TT-Metal library directory (for development builds)
if(_tt_metal_lib_dir)
    # BUILD_RPATH: Use absolute path to TT-Metal libraries for development builds
    set(_build_rpath "${_build_rpath}:${_tt_metal_lib_dir}")
    # INSTALL_RPATH: Use ttnn package's libraries instead of bundling duplicates
    # The extension is at: site-packages/torch_ttnn_cpp_extension/ttnn_device_extension
    # ttnn package is at:  site-packages/ttnn/build/lib/ (wheel structure)
    # We rely on ttnn package (hard dependency) to provide TT-Metal libraries
    # Try both locations for compatibility with different ttnn wheel structures
    set(_install_rpath "${_install_rpath}:\$ORIGIN/../../ttnn/build/lib:\$ORIGIN/../../ttnn")
endif()

# Module properties for Python extension
set_target_properties(ttnn_device_extension PROPERTIES
    CXX_STANDARD 20
    PREFIX ""           # No 'lib' prefix for Python modules
    SUFFIX ""           # No '.so' suffix (Python handles this)
    BUILD_RPATH "${_build_rpath}"    # Find dependencies relative to module location + PyTorch
    INSTALL_RPATH "${_install_rpath}"  # Same for installed module
)

# Apply PyTorch ABI compatibility flags
if(ttnn_torch_abi_flags)
    target_compile_options(ttnn_device_extension PRIVATE ${ttnn_torch_abi_flags})
endif()

# Compile-time definitions for the extension
target_compile_definitions(ttnn_device_extension PRIVATE
    FMT_HEADER_ONLY                    # Use fmt library as header-only
    TORCH_EXTENSION_NAME=ttnn_device_extension  # Extension registration name
    TORCH_API_INCLUDE_EXTENSION_H      # Include Torch extension API
    NTEST                             # Disable test-specific code
)

# GCC-specific workarounds for TT-Metal compatibility
if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    target_compile_definitions(ttnn_device_extension PRIVATE
        DISABLE_NAMESPACE_STATIC_ASSERT  # Work around GCC issues with TT-Metal
    )
endif()

# =============================================================================
# Target Linking and Dependencies
# =============================================================================
#
# Link the extension against all required dependencies. This is the critical
# step where we connect our code to TT-Metal, PyTorch, and Python.
#
# CMake best practices:
# - Use imported targets whenever possible (TT::Metalium, TTNN::*, Torch::*)
# - Prefer target_link_libraries() over manual library lists
# - Let CMake handle transitive dependencies automatically
# - Use helper functions for complex linking logic

# Determine which TTNN target to link against (TTNN::CPP is preferred)
set(_ttnn_link_target "")
if(TARGET TTNN::CPP)
    set(_ttnn_link_target TTNN::CPP)
    message(STATUS "Linking against TTNN::CPP (preferred TTNN target)")
elseif(TARGET TTNN::TTNN)
    set(_ttnn_link_target TTNN::TTNN)
    message(STATUS "Linking against TTNN::TTNN (fallback TTNN target)")
endif()

if(NOT _ttnn_link_target)
    message(FATAL_ERROR
        "No TTNN library targets found. TT-Metal must be built with TTNN support.\n"
        "\n"
        "Required: Either TTNN::CPP or TTNN::TTNN imported target\n"
        "\n"
        "Build TT-Metal with:\n"
        "  cd torch_ttnn/cpp_extension/third-party/tt-metal\n"
        "  ./build_metal.sh --release --enable-ccache")
endif()

# Core linking dependencies for the extension
set(_ttnn_link_libraries
    TT::Metalium        # Core TT-Metal functionality
    ${_ttnn_link_target} # TTNN C++ API
    Python::Module      # Python extension API
)

# Add PyTorch libraries (both imported targets and manual library lists)
if(TORCH_LIBRARIES)
    list(APPEND _ttnn_link_libraries ${TORCH_LIBRARIES})
endif()
if(TARGET Torch::Torch)
    list(APPEND _ttnn_link_libraries Torch::Torch)
endif()

# Apply all the linking
target_link_libraries(ttnn_device_extension PRIVATE ${_ttnn_link_libraries})

# Handle torch_python linking (this is complex due to PyTorch packaging variations)
ttnn_link_torch_python(ttnn_device_extension)

# Apply any additional compiler flags that PyTorch requires
if(NOT TORCH_CXX_FLAGS STREQUAL "")
    string(REPLACE " " ";" TORCH_CXX_FLAGS_LIST "${TORCH_CXX_FLAGS}")
    message(STATUS "Applying PyTorch compiler flags: ${TORCH_CXX_FLAGS_LIST}")
    target_compile_options(ttnn_device_extension PRIVATE ${TORCH_CXX_FLAGS_LIST})
endif()

# =============================================================================
# Output Name Configuration
# =============================================================================
#
# Allow customization of the extension module name for advanced use cases.
# Most users will use the default "ttnn_device_extension".

set(_ttnn_output_name "ttnn_device_extension")
if(DEFINED OUTPUT_NAME AND NOT OUTPUT_NAME STREQUAL "")
    set(_ttnn_output_name "${OUTPUT_NAME}")
elseif(DEFINED ENV{OUTPUT_NAME} AND NOT "$ENV{OUTPUT_NAME}" STREQUAL "")
    set(_ttnn_output_name "$ENV{OUTPUT_NAME}")
endif()
set_target_properties(ttnn_device_extension PROPERTIES OUTPUT_NAME "${_ttnn_output_name}")

# =============================================================================
# Examples (Optional Build Component)
# =============================================================================
#
# Build example programs that demonstrate extension usage. Only built when
# TTNN_BUILD_EXAMPLES is enabled (typically for development/testing).

if(TTNN_BUILD_EXAMPLES)
    add_subdirectory(ttnn_cpp_extension/examples)
endif()

# =============================================================================
# Installation Configuration
# =============================================================================
#
# Install the extension and its runtime dependencies. For Python packages,
# scikit-build-core sets SKBUILD_PLATLIB_DIR to the appropriate location.
#
# The extension must bundle TT-Metal shared libraries because they're not
# installed system-wide. We use $ORIGIN RPATH to make the extension self-contained.

set(_ttnn_install_destination "${SKBUILD_PLATLIB_DIR}/torch_ttnn_cpp_extension")

# Install the main extension module
install(TARGETS ttnn_device_extension
        LIBRARY DESTINATION "${_ttnn_install_destination}")

# NOTE: We do NOT bundle TT-Metal libraries here.
# The ttnn package (hard dependency) already provides them in ttnn/build/lib/:
#   - libtt_metal.so, libtt_stl.so, libdevice.so, libtracy.so, _ttnncpp.so
# INSTALL_RPATH is configured to find them via ../../ttnn/build/lib.


cmake_minimum_required(VERSION 3.16)

include(cmake/compilers.cmake)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_POSITION_INDEPENDENT_CODE ON) # This also impacts dependencies brought in through CPM
set(CMAKE_POLICY_VERSION_MINIMUM 3.5)

if(DEFINED ENV{CMAKE_C_COMPILER} AND DEFINED ENV{CMAKE_CXX_COMPILER})
    message(STATUS "Setting C and C++ compiler from environment variables")
    set(CMAKE_C_COMPILER $ENV{CMAKE_C_COMPILER})
    set(CMAKE_CXX_COMPILER $ENV{CMAKE_CXX_COMPILER})
endif()

if(CMAKE_CXX_COMPILER AND CMAKE_C_COMPILER)
    message(STATUS "Using specifed C++ compiler: ${CMAKE_CXX_COMPILER}")
    message(STATUS "Using specifed C compiler: ${CMAKE_C_COMPILER}")
else()
    message(STATUS "No C or C++ compiler specified, defaulting to Clang-17")
    FIND_AND_SET_CLANG17()
endif()

project(
    umd
    VERSION 0.1.0
    DESCRIPTION "Tenstorrent User Mode Driver"
    HOMEPAGE_URL "https://github.com/tenstorrent/tt-umd"
    LANGUAGES
        CXX
)

list(PREPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake)
CHECK_COMPILERS()
include(check_libcpp)

include(GNUInstallDirs)
set(MASTER_PROJECT OFF)
if(PROJECT_SOURCE_DIR STREQUAL CMAKE_SOURCE_DIR)
    set(MASTER_PROJECT ON)
endif()

if(MASTER_PROJECT)
    message(STATUS "UMD: Building as master project")
    if(NOT CMAKE_BUILD_TYPE)
        message(STATUS "Setting build type to 'Release' as none was specified.")
        set(CMAKE_BUILD_TYPE "Release" CACHE STRING "Release build is the default" FORCE)
    endif()

    include(sanitizers)
endif()

message(STATUS "UMD build type: ${CMAKE_BUILD_TYPE}")

option(TT_UMD_BUILD_TESTS "Enables build of tt_umd tests" OFF)
option(TT_UMD_BUILD_SIMULATION "Enables build of tt_umd simulation harnessing" OFF)

# Control compile time logging
if(NOT DEFINED TT_UMD_ENABLE_LOGGING)
    if(CMAKE_BUILD_TYPE STREQUAL "Debug")
        set(_default_enable_logging ON)
    else()
        set(_default_enable_logging OFF)
    endif()
endif()
option(TT_UMD_ENABLE_LOGGING "Enables inclusion of log_trace and log_debug into the binary." ${_default_enable_logging})
if(TT_UMD_ENABLE_LOGGING)
    add_compile_definitions(SPDLOG_ACTIVE_LEVEL=SPDLOG_LEVEL_TRACE)
endif()

add_subdirectory(third_party)

# Enable all warnings and treat them as errors
# Ignore unused variables and functions since there is no harm.
# TODO: Re-enable sign-compare
add_compile_options(
    -Wall
    -Werror
    -Wno-unused-variable
    -Wno-unused-function
    -Wno-unused-but-set-variable
    -Wno-sign-compare
)

# Conditionally add -Wno-maybe-uninitialized for GCC
# If this is left enabled it produces a hard to track down issue in stimulus_generators.hpp with ConstrainedTemplateTemplateGenerator
# TODO: Fix the issue and re-enable this warning
if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    add_compile_options(-Wno-maybe-uninitialized)
    add_compile_options(-Wno-nonnull)
endif()

add_subdirectory(common)
add_subdirectory(device)
add_subdirectory(src)
add_subdirectory(tools)

if(TT_UMD_BUILD_TESTS)
    add_subdirectory(tests)
endif(TT_UMD_BUILD_TESTS)

include(packaging)

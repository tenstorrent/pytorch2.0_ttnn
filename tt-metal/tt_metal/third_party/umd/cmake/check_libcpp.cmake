# Only perform the check if Clang is the compiler
if(CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
    include(CheckCXXCompilerFlag)

    check_cxx_compiler_flag(
        "-stdlib=libc++"
        HAS_LIBCPP
    )

    if(HAS_LIBCPP)
        message(STATUS "libc++ is available")
    else()
        message(
            WARNING
            "libc++ was not detected! If you are intending to use Clang's implementation of the c++ library, please ensure that libc++ is installed and available."
        )
    endif()
endif()

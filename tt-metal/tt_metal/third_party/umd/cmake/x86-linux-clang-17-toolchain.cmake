set(CMAKE_SYSTEM_NAME Linux)

set(CMAKE_CXX_COMPILER clang++-17 CACHE STRING "C++ compiler")
set(CMAKE_C_COMPILER clang-17 CACHE STRING "C compiler")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -stdlib=libc++" CACHE STRING "CXX FLAGS for clang")

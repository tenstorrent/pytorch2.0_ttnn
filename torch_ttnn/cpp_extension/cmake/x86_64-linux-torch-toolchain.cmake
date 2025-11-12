set(CMAKE_SYSTEM_PROCESSOR "x86_64")

# Prefer clang-17 if available, fall back to gcc-12
find_program(CLANG17_C clang-17)
find_program(CLANG17_CXX clang++-17)
if(CLANG17_C AND CLANG17_CXX)
    set(CMAKE_C_COMPILER ${CLANG17_C} CACHE INTERNAL "C compiler")
    set(CMAKE_CXX_COMPILER ${CLANG17_CXX} CACHE INTERNAL "C++ compiler")
else()
    set(CMAKE_C_COMPILER gcc-12 CACHE INTERNAL "C compiler")
    set(CMAKE_CXX_COMPILER g++-12 CACHE INTERNAL "C++ compiler")
endif()

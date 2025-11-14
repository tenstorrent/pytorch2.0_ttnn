cmake_minimum_required(VERSION 3.23)

project(torch_ttnn LANGUAGES CXX)

# Allow consumers to opt-in to building the C++ examples that ship with the extension.
option(TTNN_BUILD_EXAMPLES "Build the TTNN C++ extension examples" OFF)

# The actual extension logic lives in the cpp_extension directory.
add_subdirectory(torch_ttnn/cpp_extension)

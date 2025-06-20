cmake_minimum_required(VERSION 3.16)
enable_language(CXX)
set(CMAKE_CXX_STANDARD 20) # C++20...
set(CMAKE_CXX_STANDARD_REQUIRED ON) #...is required...
set(CMAKE_CXX_EXTENSIONS OFF) #...without compiler extensions like gnu++11

option(BUILD_WANDBCPP_EXE OFF)
option(USE_OPENCV OFF)

project(wandb-cpp)

include(FetchContent)

find_library(PTHREAD_LIBRARY pthread)
find_package(Python3 COMPONENTS Interpreter Development NumPy)

# find OpenCV
if (USE_OPENCV)
  find_package(OpenCV REQUIRED)
  # add definitions for OpenCV
  add_definitions(-DUSE_OPENCV)
endif (USE_OPENCV)


file(GLOB src_files src/*.cpp)

add_library(wandbcpp ${src_files})
add_library(wandbcpp::wandbcpp ALIAS wandbcpp)

target_compile_options(wandbcpp PRIVATE -O3 -Wall -Wextra -Wno-long-long -pedantic)

target_include_directories(wandbcpp PUBLIC 
  ${CMAKE_CURRENT_SOURCE_DIR}
)

target_link_libraries(wandbcpp PUBLIC
  Python3::NumPy
  Python3::Python
  ${PTHREAD_LIBRARY}
)

if (USE_OPENCV)
  target_include_directories(wandbcpp PUBLIC
    ${OpenCV_INCLUDE_DIRS})
  target_link_libraries(wandbcpp PUBLIC
    ${OpenCV_LIBS}
  )
endif (USE_OPENCV)

if(BUILD_WANDBCPP_EXE)
  add_subdirectory(examples)
endif(BUILD_WANDBCPP_EXE)

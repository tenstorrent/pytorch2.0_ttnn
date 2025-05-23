add_executable(ttnn_backend_demo main.cpp)
target_link_directories(ttnn_backend_demo PRIVATE "${TORCH_INSTALL_PREFIX}/lib")
target_include_directories(ttnn_backend_demo PRIVATE
    ${CMAKE_SOURCE_DIR}/ttnn_cpp_extension/include
    ${TTNN_INCLUDE_DIRS}
)
target_link_libraries(ttnn_backend_demo
    PRIVATE
        ttnn_device_extension
)

add_executable(ttnn_backend_demo main.cpp)
target_link_directories(ttnn_backend_demo PRIVATE "${TORCH_INSTALL_PREFIX}/lib")
target_include_directories(ttnn_backend_demo PRIVATE
    ${CMAKE_SOURCE_DIR}/ttnn_cpp_extension/include
    ${TTNN_INCLUDE_DIRS}
)
target_link_libraries(ttnn_backend_demo
    PRIVATE
        # -Wl,--no-as-needed
        ttnn_device_extension
)



add_executable(ttnn_demo main_ttnn_only.cpp)
target_include_directories(ttnn_demo PRIVATE
    ${TTNN_INCLUDE_DIRS}
)
target_link_directories(ttnn_demo PRIVATE "${TORCH_INSTALL_PREFIX}/lib")
target_link_libraries(ttnn_demo
    PRIVATE
    ttnn_device_extension
    # -L${TT_METAL_HOME}/build/lib -Wl,-rpath=${TT_METAL_HOME}/build/lib
    # -ltt_metal
    # -l:_ttnn.so
    # -ldevice
)
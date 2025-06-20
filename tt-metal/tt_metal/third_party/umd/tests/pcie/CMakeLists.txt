add_executable(test_pcie_device test_pcie_device.cpp)
target_link_libraries(test_pcie_device PRIVATE test_common)
set_target_properties(
    test_pcie_device
    PROPERTIES
        RUNTIME_OUTPUT_DIRECTORY
            ${CMAKE_BINARY_DIR}/test/umd/test_pcie_device
        OUTPUT_NAME
            test_pcie_device
)

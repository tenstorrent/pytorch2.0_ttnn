set(UNIFIED_TESTS_SRCS
    multiprocess.cpp
    test_tlb.cpp
)

add_executable(unified_tests ${UNIFIED_TESTS_SRCS})
target_link_libraries(unified_tests PRIVATE test_common)
set_target_properties(
    unified_tests
    PROPERTIES
        RUNTIME_OUTPUT_DIRECTORY
            ${CMAKE_BINARY_DIR}/test/umd/unified
        OUTPUT_NAME
            unified_tests
)

set(UMD_MISC_TESTS_SRCS test_semver.cpp)

add_executable(umd_misc_tests ${UMD_MISC_TESTS_SRCS})
target_link_libraries(umd_misc_tests PRIVATE test_common)
set_target_properties(
    umd_misc_tests
    PROPERTIES
        RUNTIME_OUTPUT_DIRECTORY
            ${CMAKE_BINARY_DIR}/test/umd/misc
        OUTPUT_NAME
            umd_misc_tests
)

set(UNIT_TESTS_GLX_SRCS
    test_galaxy_common.cpp
    test_umd_concurrent_threads.cpp
    test_umd_remote_api_stability.cpp
    test_umd_remote_api.cpp
)

add_executable(unit_tests_glx ${UNIT_TESTS_GLX_SRCS})
target_link_libraries(unit_tests_glx PRIVATE test_common)
set_target_properties(
    unit_tests_glx
    PROPERTIES
        RUNTIME_OUTPUT_DIRECTORY
            ${CMAKE_BINARY_DIR}/test/umd/galaxy
)

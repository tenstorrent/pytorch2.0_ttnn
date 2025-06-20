set(UNIT_TESTS_BH_SRCS
    test_cluster_bh.cpp
    test_arc_messages_bh.cpp
    test_arc_telemetry_bh.cpp
    test_chip_info_bh.cpp
)

add_executable(unit_tests_blackhole ${UNIT_TESTS_BH_SRCS})
target_link_libraries(unit_tests_blackhole PRIVATE test_common)
set_target_properties(
    unit_tests_blackhole
    PROPERTIES
        RUNTIME_OUTPUT_DIRECTORY
            ${CMAKE_BINARY_DIR}/test/umd/blackhole
        OUTPUT_NAME
            unit_tests
)

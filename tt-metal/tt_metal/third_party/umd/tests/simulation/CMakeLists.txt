set(SIMULATION_TEST_SRCS test_simulation_device.cpp)

foreach(TEST ${SIMULATION_TEST_SRCS})
    get_filename_component(TEST_NAME ${TEST} NAME_WE)
    add_executable(${TEST_NAME} ${TEST})
    target_link_libraries(${TEST_NAME} PRIVATE test_common)
    target_include_directories(${TEST_NAME} PRIVATE ${PROJECT_SOURCE_DIR}/device/simulation)
    set_target_properties(
        ${TEST_NAME}
        PROPERTIES
            RUNTIME_OUTPUT_DIRECTORY
                ${CMAKE_BINARY_DIR}/test/simulation
    )

    list(APPEND SIM_TESTS ${TEST_NAME})
endforeach()

add_custom_target(simulation_tests DEPENDS ${SIM_TESTS})

set(UBENCH_SRC
    test_perf_tlb.cpp
    test_perf_dma.cpp
)
add_executable(ubench ${UBENCH_SRC})
target_link_libraries(
    ubench
    PRIVATE
        test_common
        nanobench
)
target_include_directories(ubench PRIVATE ${nanobench_SOURCE_DIR}/src/include)
set_target_properties(
    ubench
    PROPERTIES
        RUNTIME_OUTPUT_DIRECTORY
            ${CMAKE_BINARY_DIR}/test/umd/ubenchmarks
)

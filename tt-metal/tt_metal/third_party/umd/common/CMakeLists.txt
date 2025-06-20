add_library(umd_common INTERFACE)
add_library(${PROJECT_NAME}::Common ALIAS umd_common)

target_sources(
    umd_common
    INTERFACE
        assert.hpp
        backtrace.hpp
        gtest_initializer.hpp # FIXME: this should be tucked away with the tests
)

target_include_directories(umd_common INTERFACE .)

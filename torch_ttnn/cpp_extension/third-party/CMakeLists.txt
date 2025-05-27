# Some flags for tt-metal -- ccache + unity build + make sure that cpm cache stays in tt-metal dir
set(CMAKE_DISABLE_PRECOMPILE_HEADERS TRUE)
set(ENABLE_CCACHE TRUE)
set(TT_UNITY_BUILDS ON)
set(WITH_PYTHON_BINDINGS ON)
set(CPM_SOURCE_CACHE "${CMAKE_SOURCE_DIR}/third-party/tt-metal/.cpmcache" CACHE STRING "Path to CPM source cache")

add_subdirectory(tt-metal)

set(METALIUM_INCLUDE_DIRS
    ${CMAKE_SOURCE_DIR}/third-party/tt-metal/ttnn
    ${CMAKE_SOURCE_DIR}/third-party/tt-metal/ttnn/cpp
    ${CMAKE_SOURCE_DIR}/third-party/tt-metal/ttnn/cpp/ttnn/deprecated
    ${CMAKE_SOURCE_DIR}/third-party/tt-metal/tt_metal/api
    ${CMAKE_SOURCE_DIR}/third-party/tt-metal/tt_metal
    ${CMAKE_SOURCE_DIR}/third-party/tt-metal/tt_metal/include
    ${CMAKE_SOURCE_DIR}/third-party/tt-metal/tt_metal/hostdevcommon/api
    ${CMAKE_SOURCE_DIR}/third-party/tt-metal/tt_metal/third_party/umd
    ${CMAKE_SOURCE_DIR}/third-party/tt-metal/tt_metal/third_party/umd/device/api
    ${CMAKE_SOURCE_DIR}/third-party/tt-metal/tt_metal/hw/inc
    ${CMAKE_SOURCE_DIR}/third-party/tt-metal/tt_stl
    ${CMAKE_SOURCE_DIR}/third-party/tt-metal/tt_stl/tt_stl
)

# Now wrap all the headers and .so files nicely into one target
if(NOT TARGET Metalium::TTNN)
    set(METALIUM_LIB_PATH "${CMAKE_BINARY_DIR}/lib")
    find_library(TT_METAL_LIBRARY NAMES "tt_metal" PATHS "${METALIUM_LIB_PATH}" NO_DEFAULT_PATH)
    find_library(DEVICE_LIBRARY NAMES "device" PATHS "${METALIUM_LIB_PATH}" NO_DEFAULT_PATH)
    find_library(TTNN_LIBRARY NAMES "_ttnn.so" PATHS "${METALIUM_LIB_PATH}" NO_DEFAULT_PATH)

    if(TT_METAL_LIBRARY)
        add_library(Metalium::Metal SHARED IMPORTED GLOBAL)
        set_target_properties(Metalium::Metal PROPERTIES
            IMPORTED_LOCATION "${TT_METAL_LIBRARY}"
            INTERFACE_INCLUDE_DIRECTORIES "${METALIUM_INCLUDE_DIRS}"
        )
        target_link_libraries(
        Metalium::Metal
        INTERFACE
            ${DEVICE_LIBRARY}
            nlohmann_json::nlohmann_json
        )
        message(STATUS "Successfully found libtt_metal.so at ${TT_METAL_LIBRARY}")
    else()
        message(FATAL_ERROR "libtt_metal.so not found in ${METALIUM_LIB_PATH}")
    endif()
    if(TTNN_LIBRARY)
        add_library(Metalium::TTNN SHARED IMPORTED)
        set_target_properties(
            Metalium::TTNN
            PROPERTIES
                IMPORTED_LOCATION "${TTNN_LIBRARY}"
                INTERFACE_INCLUDE_DIRECTORIES "${METALIUM_INCLUDE_DIRS}"
        )
        message(STATUS "Successfully found _ttnn.so at ${TTNN_LIBRARY}")
    else()
        message(FATAL_ERROR "_ttnn.so not found in ${METALIUM_LIB_PATH}")
    endif()
else()
    message(STATUS "Metalium targets already exists")
endif()

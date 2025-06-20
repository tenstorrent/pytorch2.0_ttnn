set(POSITION_INDEPENDENT_CODE ON)

if(TT_UMD_BUILD_SIMULATION)
    set(FBS_FILE ${PROJECT_SOURCE_DIR}/device/simulation/tt_simulation_device.fbs)
    get_filename_component(FBS_FILE_NAME ${FBS_FILE} NAME_WLE)
    set(FBS_GENERATED_HEADER "${CMAKE_CURRENT_BINARY_DIR}/${FBS_FILE_NAME}_generated.h")
    set(FBS_DEPENDS "")
    if(TARGET flatc)
        set(FBS_DEPENDS flatc)
    endif()
    add_custom_command(
        OUTPUT
            ${FBS_GENERATED_HEADER}
        COMMAND
            flatc --cpp -o "${CMAKE_CURRENT_BINARY_DIR}" ${FBS_FILE}
        DEPENDS
            ${FBS_DEPENDS}
            ${FBS_FILE}
        COMMENT "Generating FlatBuffers header ${FBS_GENERATED_HEADER}"
        VERBATIM
    )
endif()

add_library(device SHARED)
add_library(${PROJECT_NAME}::device ALIAS device)

target_sources(
    device
    PRIVATE
        architecture_implementation.cpp
        chip/chip.cpp
        chip/local_chip.cpp
        chip/mock_chip.cpp
        chip/remote_chip.cpp
        chip_helpers/sysmem_manager.cpp
        chip_helpers/sysmem_buffer.cpp
        chip_helpers/tlb_manager.cpp
        tt_device/tlb_window.cpp
        tt_device/tlb_handle.cpp
        cluster.cpp
        coordinate_manager.cpp
        cpuset_lib.cpp
        wormhole/wormhole_implementation.cpp
        blackhole/blackhole_implementation.cpp
        hugepage.cpp
        logging/config.cpp
        pcie/pci_device.cpp
        tlb.cpp
        tt_cluster_descriptor.cpp
        tt_device/blackhole_tt_device.cpp
        tt_device/tt_device.cpp
        tt_device/wormhole_tt_device.cpp
        tt_device/remote_wormhole_tt_device.cpp
        tt_device/remote_blackhole_tt_device.cpp
        tt_silicon_driver_common.cpp
        tt_soc_descriptor.cpp
        wormhole/wormhole_coordinate_manager.cpp
        blackhole/blackhole_coordinate_manager.cpp
        arc_telemetry_reader.cpp
        wormhole/wormhole_arc_telemetry_reader.cpp
        blackhole/blackhole_arc_telemetry_reader.cpp
        arc_messenger.cpp
        wormhole/wormhole_arc_messenger.cpp
        blackhole/blackhole_arc_messenger.cpp
        blackhole/blackhole_arc_message_queue.cpp
        xy_pair.cpp
        utils/lock_manager.cpp
        utils/robust_mutex.cpp
        topology_discovery.cpp
        remote_communication.cpp
)

if(TT_UMD_BUILD_SIMULATION)
    target_sources(
        device
        PRIVATE
            simulation/tt_simulation_device.cpp
            simulation/tt_simulation_host.cpp
            ${FBS_GENERATED_HEADER}
    )
    target_compile_definitions(device PRIVATE TT_UMD_BUILD_SIMULATION)
endif()

if(CMAKE_VERSION VERSION_GREATER_EQUAL 3.23)
    target_sources(
        device
        PUBLIC
            FILE_SET api
            TYPE HEADERS
            BASE_DIRS ${CMAKE_CURRENT_SOURCE_DIR}/api
            FILES
                api/umd/device/architecture_implementation.h
                api/umd/device/blackhole_arc_message_queue.h
                api/umd/device/blackhole_coordinate_manager.h
                api/umd/device/blackhole_implementation.h
                api/umd/device/chip/chip.h
                api/umd/device/chip/local_chip.h
                api/umd/device/chip/mock_chip.h
                api/umd/device/chip/remote_chip.h
                api/umd/device/chip_helpers/sysmem_manager.h
                api/umd/device/chip_helpers/sysmem_buffer.h
                api/umd/device/chip_helpers/tlb_manager.h
                api/umd/device/cluster.h
                api/umd/device/coordinate_manager.h
                api/umd/device/device_api_metal.h
                api/umd/device/driver_atomics.h
                api/umd/device/hugepage.h
                api/umd/device/logging/config.h
                api/umd/device/utils/lock_manager.h
                api/umd/device/pci_device.hpp
                api/umd/device/semver.hpp
                api/umd/device/utils/robust_mutex.h
                api/umd/device/tt_cluster_descriptor.h
                api/umd/device/tt_core_coordinates.h
                api/umd/device/tt_device/blackhole_tt_device.h
                api/umd/device/tt_device/tt_device.h
                api/umd/device/tt_device/wormhole_tt_device.h
                api/umd/device/tt_device/remote_wormhole_tt_device.h
                api/umd/device/tt_device/remote_blackhole_tt_device.h
                api/umd/device/tt_io.hpp
                api/umd/device/tt_silicon_driver_common.hpp
                api/umd/device/tt_simulation_device.h
                api/umd/device/tt_simulation_host.hpp
                api/umd/device/tt_soc_descriptor.h
                api/umd/device/tt_xy_pair.h
                api/umd/device/types/arch.h
                api/umd/device/types/blackhole_arc.h
                api/umd/device/types/cluster_descriptor_types.h
                api/umd/device/types/cluster_types.h
                api/umd/device/types/harvesting.h
                api/umd/device/types/tlb.h
                api/umd/device/types/xy_pair.h
                api/umd/device/wormhole_coordinate_manager.h
                api/umd/device/wormhole_implementation.h
    )
endif()

target_include_directories(
    device
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/api>
    PRIVATE
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>
)

target_link_libraries(
    device
    PRIVATE
        umd::Common
        umd::Firmware
        hwloc
        rt
        spdlog::spdlog_header_only
        fmt::fmt-header-only
        tt-logger::tt-logger
        yaml-cpp::yaml-cpp
)

if(TT_UMD_BUILD_SIMULATION)
    target_link_libraries(
        device
        PRIVATE
            flatbuffers::flatbuffers
            nng
            uv_a
    )
endif()

if(CMAKE_VERSION VERSION_GREATER_EQUAL 3.23)
    install(
        TARGETS
            device
        EXPORT ${PROJECT_NAME}Targets
        ARCHIVE
            DESTINATION ${CMAKE_INSTALL_LIBDIR}
        LIBRARY
            DESTINATION ${CMAKE_INSTALL_LIBDIR}
            COMPONENT umd-runtime
        FILE_SET
        api
            COMPONENT umd-dev
    )

    install(
        EXPORT ${PROJECT_NAME}Targets
        FILE ${PROJECT_NAME}Targets.cmake
        DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}
        NAMESPACE ${PROJECT_NAME}::
        COMPONENT umd-dev
    )
endif()

# Add a custom command to copy the library to build/lib
add_custom_command(
    TARGET device
    POST_BUILD
    COMMAND
        ${CMAKE_COMMAND} -E make_directory ${CMAKE_BINARY_DIR}/lib
    COMMAND
        ${CMAKE_COMMAND} -E copy $<TARGET_FILE:device> ${CMAKE_BINARY_DIR}/lib/
    COMMENT "Copying device library to build/lib"
)

# No separation of public and private header files
# I can only assume everything is public
install(
    DIRECTORY
        ${PROJECT_SOURCE_DIR}/device
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/${PROJECT_NAME}/device
    FILES_MATCHING
    PATTERN
    "*.h"
    PATTERN
    "*.hpp"
)
install(
    DIRECTORY
        ${PROJECT_SOURCE_DIR}/common
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/${PROJECT_NAME}/common
    FILES_MATCHING
    PATTERN
    "*.h"
    PATTERN
    "*.hpp"
)

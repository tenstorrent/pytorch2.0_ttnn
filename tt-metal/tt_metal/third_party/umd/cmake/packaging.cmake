include(CMakePackageConfigHelpers)

write_basic_package_version_file(
    ${PROJECT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY AnyNewerVersion
)

# Configure the Config file
configure_package_config_file(
    ${PROJECT_SOURCE_DIR}/cmake/${PROJECT_NAME}Config.cmake.in
    ${PROJECT_BINARY_DIR}/${PROJECT_NAME}Config.cmake
    INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}
)

# Install the Config and ConfigVersion files
install(
    FILES
        ${PROJECT_BINARY_DIR}/${PROJECT_NAME}Config.cmake
        ${PROJECT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}
    COMPONENT umd-dev
)

set(CPACK_PACKAGE_NAME "${PROJECT_NAME}-dev")
set(CPACK_GENERATOR "DEB")
set(CPACK_PACKAGE_VENDOR "Tenstorrent, Inc.")
set(CPACK_DEBIAN_PACKAGE_MAINTAINER "support@tenstorrent.com")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "Tenstorrent User Mode Driver")
#set(CPACK_DEBIAN_PACKAGE_DEPENDS "")

include(CPack)

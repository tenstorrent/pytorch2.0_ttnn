function(check_ubuntu_version_at_least REQUIRED_MAJOR RESULT_VAR)
    execute_process(
        COMMAND lsb_release -rs
        OUTPUT_VARIABLE UBUNTU_VERSION
        OUTPUT_STRIP_TRAILING_WHITESPACE
        ERROR_QUIET
    )

    if(NOT UBUNTU_VERSION)
        message(WARNING "Unable to detect Ubuntu version.")
        set(${RESULT_VAR} FALSE PARENT_SCOPE)
        return()
    endif()

    string(REPLACE "." ";" UBUNTU_VERSION_LIST ${UBUNTU_VERSION})
    list(GET UBUNTU_VERSION_LIST 0 UBUNTU_MAJOR)

    if(UBUNTU_MAJOR VERSION_GREATER_EQUAL ${REQUIRED_MAJOR})
        set(${RESULT_VAR} TRUE PARENT_SCOPE)
    else()
        set(${RESULT_VAR} FALSE PARENT_SCOPE)
    endif()
endfunction()

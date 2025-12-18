if (NOT DEFINED PYTHON_EXECUTABLE)
  # Try to get an interpreter from CMake's Python3 package first
  find_package(Python3 COMPONENTS Interpreter QUIET)
  if (DEFINED Python3_EXECUTABLE)
    set(PYTHON_EXECUTABLE "${Python3_EXECUTABLE}")
  else()
    # Fallback to querying the active python3 on PATH
    execute_process(
      COMMAND python3 -c "import sys; print(sys.executable)"
      OUTPUT_VARIABLE PYTHON_EXECUTABLE
      OUTPUT_STRIP_TRAILING_WHITESPACE
      ERROR_QUIET
    )
  endif()
endif()

if (NOT PYTHON_EXECUTABLE)
  message(FATAL_ERROR "Unable to determine Python interpreter. Set PYTHON_EXECUTABLE explicitly.")
endif()

execute_process(
  COMMAND ${PYTHON_EXECUTABLE} -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"
  OUTPUT_VARIABLE PYTHON_VERSION
  OUTPUT_STRIP_TRAILING_WHITESPACE
)

execute_process(
  COMMAND ${PYTHON_EXECUTABLE} -c "import sysconfig; print(sysconfig.get_path('include'))"
  OUTPUT_VARIABLE PYTHON_INCLUDE_DIRS
  OUTPUT_STRIP_TRAILING_WHITESPACE
)

execute_process(
  COMMAND ${PYTHON_EXECUTABLE} -c "import sysconfig; print(sysconfig.get_config_var('LIBDIR'))"
  OUTPUT_VARIABLE PYTHON_LIBRARY_DIR
  OUTPUT_STRIP_TRAILING_WHITESPACE
)

execute_process(
  COMMAND ${PYTHON_EXECUTABLE} -c "import sysconfig; print(sysconfig.get_config_var('LDLIBRARY'))"
  OUTPUT_VARIABLE PYTHON_LIBRARY_NAME
  OUTPUT_STRIP_TRAILING_WHITESPACE
)

execute_process(
  COMMAND ${PYTHON_EXECUTABLE} -c "import sysconfig; print(sysconfig.get_config_var('EXT_SUFFIX') or '.so')"
  OUTPUT_VARIABLE PYTHON_MODULE_EXTENSION
  OUTPUT_STRIP_TRAILING_WHITESPACE
)

set(PYTHON_LIBRARIES "${PYTHON_LIBRARY_DIR}/${PYTHON_LIBRARY_NAME}")

message(STATUS "Python version: ${PYTHON_VERSION}")
message(STATUS "Python executable: ${PYTHON_EXECUTABLE}")
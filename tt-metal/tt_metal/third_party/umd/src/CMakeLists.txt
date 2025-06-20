add_library(firmware INTERFACE)
add_library(${PROJECT_NAME}::Firmware ALIAS firmware)

target_include_directories(firmware INTERFACE firmware/riscv)

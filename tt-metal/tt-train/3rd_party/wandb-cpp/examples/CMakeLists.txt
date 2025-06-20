file(GLOB example_files RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} *.cpp)

foreach(file ${example_files})
  string(REPLACE ".cpp" "" name ${file})
  message(${name})
  add_executable(${name} ${file})
  target_link_libraries(${name}
    wandbcpp
  )  
endforeach(file ${example_files})
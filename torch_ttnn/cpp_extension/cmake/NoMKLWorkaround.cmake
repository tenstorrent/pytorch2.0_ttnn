if(NOT DEFINED MKL_FOUND OR NOT MKL_FOUND)
  add_library(caffe2::mkl INTERFACE IMPORTED)
  return()          # skip the rest of mkl.cmake
endif()

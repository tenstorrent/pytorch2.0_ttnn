#include "src/np_object.hpp"

#include <iostream>
#include <thread>
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#define NO_IMPORT_ARRAY
#define PY_ARRAY_UNIQUE_SYMBOL cool_ARRAY_API
#include "numpy/arrayobject.h"
namespace wandbcpp::numpy {
using namespace std::literals;
ndarray::ndarray(const internal::object::PyList& data)
    : data_(data), dtype_(dtype::np_notype) {}

ndarray::ndarray(const internal::object::PyList& data, dtype dtype)
    : data_(data), dtype_(dtype) {}

// ndarray::ndarray(const internal::object::PyList& data) : data_(data) {}

PyObject* ndarray::get_pyobject() const {
  return PyArray_FromObject(data_.get_pyobject(),
                            static_cast<NPY_TYPES>(dtype_), 0, 0);
}

}  // namespace wandbcpp::numpy

#ifndef WANDBCPP_NP_OBJECT_HPP_
#define WANDBCPP_NP_OBJECT_HPP_
#include <iterator>
#include <memory>
#include <type_traits>
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include "numpy/ndarraytypes.h"
#include "src/py_object.hpp"
namespace wandbcpp {

namespace numpy {

enum class dtype : std::underlying_type_t<NPY_TYPES> {
  np_notype = NPY_NOTYPE,
  np_short = NPY_SHORT,
  np_int = NPY_INT,
  np_double = NPY_DOUBLE,
  np_float = NPY_FLOAT,
  np_object = NPY_OBJECT
};
class ndarray : public internal::object::PyObjectBaseClonable<ndarray> {
  internal::object::PyList data_;
  dtype dtype_;

 public:
  explicit ndarray(const internal::object::PyList& data);

  explicit ndarray(const internal::object::PyList& data, dtype dtype);

  ~ndarray() {}

  PyObject* get_pyobject() const override;
};

}  // namespace numpy

}  // namespace wandbcpp
#endif
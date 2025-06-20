#ifndef WANDBCPP_PY_UTIL_HPP_
#define WANDBCPP_PY_UTIL_HPP_

#include "src/py_object.hpp"

namespace wandbcpp::internal::util {

object::SharedPyObjectPtr PyCall(const object::SharedPyObjectPtr& func);
object::SharedPyObjectPtr PyCall(const object::SharedPyObjectPtr& func,
                                 const object::PyDict& kwargs);
object::SharedPyObjectPtr PyCall(const object::SharedPyObjectPtr& func,
                                 const object::PyTuple& args);
void print_pyobject(PyObject* obj, int idx = 0);

}  // namespace wandbcpp::internal::util

#endif
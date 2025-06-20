#include "src/py_object.hpp"

#include "src/py_util.hpp"
namespace wandbcpp::internal::object {

// SharedPyObjectPtr
SharedPyObjectPtr::SharedPyObjectPtr() : ptr_(nullptr) {}
SharedPyObjectPtr::SharedPyObjectPtr(PyObject* ptr) : ptr_(ptr) {}
SharedPyObjectPtr& SharedPyObjectPtr::operator=(PyObject* ptr) {
  if (!is_null()) Py_DECREF(ptr_);
  ptr_ = ptr;
  return *this;
}
SharedPyObjectPtr& SharedPyObjectPtr::operator=(const SharedPyObjectPtr& src) {
  if (!is_null()) Py_DECREF(ptr_);
  ptr_ = src.ptr_;
  if (!is_null()) Py_INCREF(ptr_);
  return *this;
}
SharedPyObjectPtr::~SharedPyObjectPtr() {
  if (!is_null()) {
    Py_DECREF(ptr_);
  }
}
SharedPyObjectPtr::SharedPyObjectPtr(const SharedPyObjectPtr& src)
    : ptr_(src.ptr_) {
  if (!is_null()) Py_INCREF(ptr_);
}
SharedPyObjectPtr::SharedPyObjectPtr(SharedPyObjectPtr&& src) {
  ptr_ = src.ptr_;
  src.ptr_ = nullptr;
}
SharedPyObjectPtr& SharedPyObjectPtr::operator=(SharedPyObjectPtr&& src) {
  if (!is_null()) Py_DECREF(ptr_);
  ptr_ = src.ptr_;
  src.ptr_ = nullptr;
  return *this;
}

PyObject* SharedPyObjectPtr::get() const { return ptr_; }
bool SharedPyObjectPtr::is_null() const { return ptr_ == nullptr; }
PyObject* SharedPyObjectPtr::operator->() { return ptr_; }
PyObject* SharedPyObjectPtr::release() {
  PyObject* ptr = ptr_;
  ptr_ = nullptr;
  return ptr;
}

std::ostream& operator<<(std::ostream& os, const PyObjectBase& obj) {
  if (Py_IsInitialized() == 0) {
    throw std::runtime_error("Python Interpreter is not initialized!");
  } else {
    SharedPyObjectPtr ptr(obj.get_pyobject());
    SharedPyObjectPtr repr(PyObject_Repr(ptr.get()));
    SharedPyObjectPtr str_ptr(
        PyUnicode_AsEncodedString(repr.get(), "utf-8", "~E~"));
    const char* bytes = PyBytes_AsString(str_ptr.get());
    os << bytes;
  }
  return os;
}

// PyBasicType
template <>
PyObject* PyBasicType<double>::get_pyobject() const {
  return PyFloat_FromDouble(value);
}
template <>
PyObject* PyBasicType<float>::get_pyobject() const {
  return PyFloat_FromDouble(value);
}
template <>
PyObject* PyBasicType<int>::get_pyobject() const {
  return PyLong_FromLong(value);
}

template <>
PyObject* PyBasicType<long>::get_pyobject() const {
  return PyLong_FromLong(value);
}

template <>
PyObject* PyBasicType<bool>::get_pyobject() const {
  return PyBool_FromLong(value);
}
template <>
PyObject* PyBasicType<char const*>::get_pyobject() const {
  return PyUnicode_FromString(value);
}
template <>
PyObject* PyBasicType<std::string>::get_pyobject() const {
  return PyUnicode_FromString(value.c_str());
}

// PyDictItem
PyDictItem::PyDictItem(std::string key) : key_(key), value_() {}
const char* PyDictItem::key() const { return key_.c_str(); }
PyObject* PyDictItem::get_pyobject_of_value() const {
  return value_->get_pyobject();
}

// PyDict
PyDict::PyDict(const std::initializer_list<PyDictItem>& items)
    : items_(items.begin(), items.end()) {}
PyDict::PyDict() = default;
PyDict::PyDict(const PyDict& other) = default;
void PyDict::update(const PyDict& other) {
  items_.reserve(items_.size() + other.items_.size());
  std::copy(other.items_.begin(), other.items_.end(),
            std::back_inserter(items_));
}
void PyDict::clear() { items_.clear(); }
bool PyDict::empty() const { return items_.empty(); }
PyDictItem& PyDict::operator[](std::string key) {
  items_.emplace_back(PyDictItem(key));
  return items_.back();
}
PyObject* PyDict::get_pyobject() const {
  PyObject* pydict = PyDict_New();
  for (auto& item : items_) {
    PyDict_SetItemString(pydict, item.key(), item.get_pyobject_of_value());
  }
  return pydict;
}

// PyList
size_t PyList::size() const { return items_.size(); }

const PyObjectBase& PyList::operator[](size_t i) const { return *items_[i]; }

PyObjectBase& PyList::operator[](size_t i) { return *items_[i]; }

PyList& PyList::reverse() {
  std::reverse(items_.begin(), items_.end());
  return *this;
}

PyObject* PyList::get_pyobject() const {
  PyObject* lst = PyList_New(items_.size());
  for (uint i = 0; i < items_.size(); i++) {
    PyList_SetItem(lst, i, items_[i]->get_pyobject());
  }
  return lst;
}
// PyTuple
PyTuple::PyTuple() {}
PyObject* PyTuple::get_pyobject() const {
  PyObject* tup = PyTuple_New(items_.size());
  for (uint i = 0; i < items_.size(); i++) {
    PyTuple_SetItem(tup, i, items_[i]->get_pyobject());
  }
  return tup;
}
}  // namespace wandbcpp::internal::object

#ifndef WANDBCPP_PY_OBJECTS_HPP_
#define WANDBCPP_PY_OBJECTS_HPP_

#include <Python.h>

#include <algorithm>
#include <iostream>
#include <iterator>
#include <memory>
#include <type_traits>
#include <utility>
#include <vector>

namespace wandbcpp::internal::object {

struct PyObjectBase {
  virtual ~PyObjectBase() {}
  virtual PyObject* get_pyobject() const = 0;
  virtual PyObjectBase* clone() const = 0;
};

template <class Derived>
struct PyObjectBaseClonable : public PyObjectBase {
  PyObjectBase* clone() const override {
    return new Derived(static_cast<Derived const&>(*this));
  }
};

class SharedPyObjectPtr {
  PyObject* ptr_;

 public:
  SharedPyObjectPtr();
  explicit SharedPyObjectPtr(PyObject* ptr);
  SharedPyObjectPtr(const SharedPyObjectPtr& src);
  SharedPyObjectPtr(SharedPyObjectPtr&& src);
  ~SharedPyObjectPtr();
  SharedPyObjectPtr& operator=(PyObject* ptr);
  SharedPyObjectPtr& operator=(const SharedPyObjectPtr& src);
  SharedPyObjectPtr& operator=(SharedPyObjectPtr&& src);
  PyObject* get() const;
  bool is_null() const;
  PyObject* operator->();
  PyObject* release();
};

std::ostream& operator<<(std::ostream& os, const PyObjectBase& obj);

template <class ValueType>
class PyBasicType : public PyObjectBaseClonable<PyBasicType<ValueType>> {
 private:
  ValueType value;

 public:
  PyBasicType(const ValueType& value) : value(value) {}
  ~PyBasicType() {}
  PyObject* get_pyobject() const override;
};

template <class T>
PyObjectBase* create_pybjectbase_ptr(const T& t) {
  if constexpr (std::is_base_of_v<PyObjectBase, T> ||
                std::is_same_v<PyObjectBase, T>) {
    return t.clone();
  } else {
    return new PyBasicType<T>(t);
  }
}

template <size_t N>
class PyBasicType<char[N]> : public PyObjectBaseClonable<PyBasicType<char[N]>> {
 private:
  PyBasicType<std::string> str;

 public:
  PyBasicType(const char (&arr)[N]) : str(arr) {}
  ~PyBasicType() {}
  PyObject* get_pyobject() const override { return str.get_pyobject(); }
};

class PyDictItem {
  std::string key_;
  std::shared_ptr<PyObjectBase> value_;

 public:
  PyDictItem(std::string key);
  ~PyDictItem(){}
  PyDictItem(const std::string& key, const PyObjectBase& value);
  template <class ValueType>
  PyDictItem(const std::string& key, const ValueType& value)
      : key_(key), value_(create_pybjectbase_ptr(value)) {}
  template <class ValueType>
  explicit PyDictItem(const std::pair<std::string, ValueType>& key_value_pair)
      : key_(key_value_pair.first),
        value_(create_pybjectbase_ptr(key_value_pair.second)) {}

  const char* key() const;
  template <class ValueType>
  PyDictItem& operator=(const ValueType value) {
    value_.reset(create_pybjectbase_ptr(value));
    return *this;
  }
  PyObject* get_pyobject_of_value() const;
};

class PyDict : public PyObjectBaseClonable<PyDict> {
 private:
  std::vector<PyDictItem> items_;

 public:
  PyDict(const std::initializer_list<PyDictItem>& items);
  PyDict();
  PyDict(const PyDict& other);
  ~PyDict(){}
  PyDictItem& operator[](std::string key);
  void update(const PyDict& other);
  void clear();
  bool empty() const;
  PyObject* get_pyobject() const override;
};

class PyList : public PyObjectBaseClonable<PyList> {
 public:
  std::vector<std::shared_ptr<PyObjectBase>> items_;

  PyList() {}
  // copy constructor
  PyList(const PyList& other) {
    for (const auto& item : other.items_) {
      items_.emplace_back(item->clone());
    }
  }

  template <std::input_iterator InputIterator>
  PyList(InputIterator first, InputIterator last) {
    for (InputIterator it = first; it != last; it++) {
      append(*it);
    }
  }

  template <class... Items>
  PyList(const Items&... items) {
    using swallow = int[];
    (void)swallow{(append(items), 0)...};
  }

  template <class T>
  void append(const T& v) {
    items_.emplace_back(create_pybjectbase_ptr(v));
  }

  PyList& reverse();

  size_t size() const;

  const PyObjectBase& operator[](size_t i) const;

  PyObjectBase& operator[](size_t i);

  PyObject* get_pyobject() const override;
};

class PyTuple : public PyObjectBaseClonable<PyTuple> {
  std::vector<std::shared_ptr<PyObjectBase>> items_;

 public:
  PyTuple();
  ~PyTuple(){}
  template <class... Items>
  PyTuple(const Items&... items) {
    using swallow = int[];
    (void)swallow{(append(items), 0)...};
  }

  template <class T>
  void append(const T& v) {
    items_.emplace_back(create_pybjectbase_ptr(v));
  }
  PyObject* get_pyobject() const override;
};
}  // namespace wandbcpp::internal::object

#endif  // WANDBCPP_PY_OBJECTS_HPP_
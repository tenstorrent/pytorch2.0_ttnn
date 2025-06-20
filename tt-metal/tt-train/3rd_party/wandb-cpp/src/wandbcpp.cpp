#include "wandbcpp.hpp"

#include <Python.h>

#include <fstream>
#include <iterator>
#include <optional>

#include "src/async_logging.hpp"
#define PY_ARRAY_UNIQUE_SYMBOL cool_ARRAY_API
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include "numpy/arrayobject.h"

namespace wandbcpp {
using namespace std::literals;
using namespace internal;
using namespace internal::object;
using namespace internal::util;

wandb::wandb() {}

void wandb::init(const init_args& ia) {
  if (Py_IsInitialized() == 0) {
    throw std::runtime_error("Error Python is not initialized!");
  }

  wandb_module_ = PyImport_ImportModule("wandb");
  int i = _import_array();
  if (i < 0) {
    throw std::runtime_error("import numpy failed");
  }

  if (wandb_module_.is_null()) {
    PyErr_Print();
    throw std::runtime_error("Error loading module wandb!");
  }
  init_ = PyObject_GetAttrString(wandb_module_.get(), "init");
  if (init_.is_null() || !PyCallable_Check(init_.get())) {
    PyErr_Print();
    throw std::runtime_error("Error loading wandb.init()!");
  }

  PyDict init_kwargs({{"project", ia.project},
                      {"name", ia.name},
                      {"tags", PyList(ia.tags.begin(), ia.tags.end())}});
  if (!ia.entity.empty()) init_kwargs["entity"] = ia.entity;
  if (!ia.group.empty()) init_kwargs["group"] = ia.group;
  run_ = PyCall(init_, init_kwargs);

  log_ = PyObject_GetAttrString(wandb_module_.get(), "log");
  config_ = PyObject_GetAttrString(wandb_module_.get(), "config");
  config_update_ = PyObject_GetAttrString(config_.get(), "update");
  summary_ = PyObject_GetAttrString(wandb_module_.get(), "summary");
  summary_update_ = PyObject_GetAttrString(summary_.get(), "update");

  save_ = PyObject_GetAttrString(wandb_module_.get(), "save");
  finish_ = PyObject_GetAttrString(wandb_module_.get(), "finish");
  Table::TablePointer() = PyObject_GetAttrString(wandb_module_.get(), "Table");
  Object3D::Object3DPointer() =
      PyObject_GetAttrString(wandb_module_.get(), "Object3D");
#ifdef USE_OPENCV
  Image::ImagePointer() = PyObject_GetAttrString(wandb_module_.get(), "Image");
  Video::VideoPointer() = PyObject_GetAttrString(wandb_module_.get(), "Video");
#endif
}

void wandb::log(const PyDict& logs) { PyCall(log_, PyTuple(logs)); }

void wandb::save(const std::string& file_path) {
  PyCall(save_, PyTuple(file_path));
}

void wandb::update_config(const internal::object::PyDict& conf) {
  PyCall(config_update_, PyTuple(conf));
}

void wandb::update_summary(const internal::object::PyDict& summ) {
  PyCall(summary_update_, PyTuple(summ));
}

void wandb::finish() { PyCall(finish_); }

wandb::wandb_mode wandb::get_mode() {
  static std::optional<wandb_mode> mode;

  if (!mode) {
    std::ifstream ifs("wandb/settings");
    if (ifs.is_open()) {
      std::string wandb_settings((std::istreambuf_iterator<char>(ifs)),
                                 std::istreambuf_iterator<char>());
      if (wandb_settings.find("mode") == std::string::npos) {
        mode = wandb_mode::online;
      } else {
        if (wandb_settings.find("mode = online") != std::string::npos) {
          mode = wandb_mode::online;
        } else if (wandb_settings.find("mode = offline") != std::string::npos) {
          mode = wandb_mode::offline;
        } else if (wandb_settings.find("disabled = true") !=
                   std::string::npos) {
          mode = wandb_mode::disabled;
        } else {
          mode = wandb_mode::online;
        }
      }
    } else {
      mode = wandb_mode::online;
    }
  }

  return mode.value();
}

using namespace internal::async;

std::unique_ptr<AsyncLoggingWorker> logging_worker;

void preprocessing() {
  if (!logging_worker) {
    logging_worker = std::make_unique<internal::async::AsyncLoggingWorker>();
  }
}

void init(const wandb::init_args& ia, bool wait_initialized) {
  if (wandb::get_mode() == wandb::wandb_mode::disabled) {
    return;
  }
  preprocessing();
  logging_worker->initialize_wandb(ia);
  if (wait_initialized) logging_worker->wait_initialized();
}

void log(const PyDict& logs) {
  if (wandb::get_mode() == wandb::wandb_mode::disabled) {
    return;
  }
  preprocessing();
  logging_worker->append_log(logs);
}

void log(PyDict&& logs) {
  if (wandb::get_mode() == wandb::wandb_mode::disabled) {
    return;
  }
  preprocessing();
  logging_worker->append_log(std::forward<PyDict>(logs));
}

void save(const std::string& file_path) {
  if (wandb::get_mode() == wandb::wandb_mode::disabled) {
    return;
  }
  preprocessing();
  logging_worker->append_file_path(file_path);
}

void update_config(const PyDict& conf) {
  if (wandb::get_mode() == wandb::wandb_mode::disabled) {
    return;
  }
  preprocessing();
  logging_worker->append_config(conf);
}

void update_config(PyDict&& confs) {
  if (wandb::get_mode() == wandb::wandb_mode::disabled) {
    return;
  }
  preprocessing();
  logging_worker->append_config(std::forward<PyDict>(confs));
}

void update_summary(const PyDict& summs) {
  if (wandb::get_mode() == wandb::wandb_mode::disabled) {
    return;
  }
  preprocessing();
  logging_worker->append_summary(summs);
}

void update_summary(PyDict&& summs) {
  if (wandb::get_mode() == wandb::wandb_mode::disabled) {
    return;
  }
  preprocessing();
  logging_worker->append_summary(std::forward<PyDict>(summs));
}

void finish() {
  if (wandb::get_mode() == wandb::wandb_mode::disabled) {
    return;
  }
  if (logging_worker) {
    logging_worker.reset();
  }
}

}  // namespace wandbcpp
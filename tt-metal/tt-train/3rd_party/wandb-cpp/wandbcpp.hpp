#ifndef WANDBCPP_HPP_
#define WANDBCPP_HPP_

#include <Python.h>

#include <string>
#include <vector>

#include "src/py_object.hpp"
#include "src/py_util.hpp"
#include "src/utils.hpp"
#include "src/wandb_object.hpp"

namespace wandbcpp {

class wandb {
  internal::object::SharedPyObjectPtr wandb_module_;   // wandb module
  internal::object::SharedPyObjectPtr run_;            // run object
  internal::object::SharedPyObjectPtr init_;           // init function
  internal::object::SharedPyObjectPtr log_;            // log function
  internal::object::SharedPyObjectPtr config_;         // config object
  internal::object::SharedPyObjectPtr config_update_;  // config.update function
  internal::object::SharedPyObjectPtr summary_;        // summary object
  internal::object::SharedPyObjectPtr
      summary_update_;                          // summary.update function
  internal::object::SharedPyObjectPtr save_;    // save function
  internal::object::SharedPyObjectPtr finish_;  // finish function

 public:
  wandb();
  ~wandb() {}

  struct init_args {
    std::string project;
    std::string entity = "";
    std::string name = "";
    std::vector<std::string> tags = {};
    std::string group = "";
  };

  void init(const init_args& ia);

  void log(const internal::object::PyDict& logs);

  // void log(internal::object::PyDict&& logs);

  void save(const std::string& file_path);

  void update_config(const internal::object::PyDict& conf);

  void update_summary(const internal::object::PyDict& summ);

  void finish();

  enum class wandb_mode { online, offline, disabled };
  static wandb_mode get_mode();
};

using log_dict = internal::object::PyDict;
using py_list = internal::object::PyList;
using py_dict = internal::object::PyDict;

void init(const wandb::init_args& ia, bool wait_initialized = true);

void log(const internal::object::PyDict& logs);

void log(internal::object::PyDict&& logs);

void save(const std::string& file_path);

void update_config(const internal::object::PyDict& confs);

void update_config(internal::object::PyDict&& confs);

void update_summary(const internal::object::PyDict& summs);

void update_summary(internal::object::PyDict&& summs);

void finish();

}  // namespace wandbcpp

#endif
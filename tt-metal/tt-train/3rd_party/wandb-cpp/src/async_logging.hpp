#ifndef WANDBCPP_ASYNC_LOGGING_HPP_
#define WANDBCPP_ASYNC_LOGGING_HPP_

#include <condition_variable>
#include <mutex>
#include <optional>
#include <queue>
#include <thread>

#include "wandbcpp.hpp"

namespace wandbcpp::internal::async {
class AsyncLoggingWorker {
  /**
   * @brief A worker class to handle asynchronous logging.
   *
   * This class is used to handle asynchronous logging.
   *
   */
 private:
  std::mutex init_mtx_;
  std::optional<wandb::init_args> init_args_;
  std::condition_variable cv_do_init_;
  bool is_initialized_;
  std::mutex is_initialized_mtx_;
  std::condition_variable cv_is_initialized_;

  bool terminal_ = false;

  std::mutex buffers_mtx_;
  std::condition_variable cv_buffers_not_empty_;

  // log
  std::queue<object::PyDict> log_buffer_;

  // config
  std::queue<object::PyDict> config_buffer_;

  // summary
  std::queue<object::PyDict> summary_buffer_;

  // save
  std::vector<std::string> file_path_buffer_;

  std::thread logging_worker_thread;

  wandb* wandb_;

 public:
  AsyncLoggingWorker();
  ~AsyncLoggingWorker();
  AsyncLoggingWorker(const AsyncLoggingWorker& other) = delete;
  AsyncLoggingWorker& operator=(const AsyncLoggingWorker& other) = delete;
  void initialize_wandb(const wandb::init_args& ia);
  void wait_initialized();
  void worker();

  bool is_buffers_empty();

  bool is_log_buffer_empty();
  void append_log(const object::PyDict& log);
  void append_log(object::PyDict&& log);

  bool is_config_buffer_empty();
  void append_config(const object::PyDict& config);
  void append_config(object::PyDict&& config);

  bool is_summary_buffer_empty();
  void append_summary(const object::PyDict& summary);
  void append_summary(object::PyDict&& summary);

  bool is_file_path_buffer_empty();
  void append_file_path(const std::string& file_path);

  void finish();
};

}  // namespace wandbcpp::internal::async

#endif
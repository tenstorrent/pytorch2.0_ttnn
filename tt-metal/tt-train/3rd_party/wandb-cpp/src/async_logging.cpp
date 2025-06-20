#include "src/async_logging.hpp"

#include <utility>
namespace wandbcpp::internal::async {
using namespace std::literals;

AsyncLoggingWorker::AsyncLoggingWorker()
    : is_initialized_(false),
      terminal_(false),
      logging_worker_thread(std::thread(&AsyncLoggingWorker::worker, this)) {}

AsyncLoggingWorker::~AsyncLoggingWorker() {
  finish();
  logging_worker_thread.join();
}

void AsyncLoggingWorker::initialize_wandb(const wandb::init_args& ia) {
  std::unique_lock lk(init_mtx_);
  init_args_ = ia;
  cv_do_init_.notify_all();
}

void AsyncLoggingWorker::wait_initialized() {
  std::unique_lock lk(is_initialized_mtx_);
  cv_is_initialized_.wait(lk, [this] { return is_initialized_; });
}

void AsyncLoggingWorker::worker() {
  {
    std::unique_lock lk(init_mtx_);
    cv_do_init_.wait(lk,
                     [this] { return init_args_.has_value() || terminal_; });
    if (terminal_) {
      return;
    } else {
      if (Py_IsInitialized() == 0) Py_Initialize();
      wandb_ = new wandb();
      {
        std::unique_lock lk(is_initialized_mtx_);
        wandb_->init(init_args_.value());
        is_initialized_ = true;
        cv_is_initialized_.notify_all();
      }
    }
  }
  while (true) {
    {
      std::unique_lock lk(buffers_mtx_);
      cv_buffers_not_empty_.wait(lk, [this] {
        return terminal_ ||                 //
               !log_buffer_.empty() ||      //
               !config_buffer_.empty() ||   //
               !summary_buffer_.empty() ||  //
               !file_path_buffer_.empty();
      });
    }
    if (terminal_ && is_buffers_empty()) {
      wandb_->finish();
      delete wandb_;
      Py_Finalize();
      return;
    }
    if (!is_log_buffer_empty()) {
      std::queue<object::PyDict> log_buffer_moved_;
      {
        std::lock_guard<std::mutex> lk(buffers_mtx_);
        log_buffer_moved_ = std::move(log_buffer_);
      }
      while (!log_buffer_moved_.empty()) {
        wandb_->log(log_buffer_moved_.front());
        log_buffer_moved_.pop();
      }
    }
    if (!is_config_buffer_empty()) {
      std::queue<object::PyDict> config_buffer_moved_;
      {
        std::lock_guard<std::mutex> lk(buffers_mtx_);
        config_buffer_moved_ = std::move(config_buffer_);
      }
      while (!config_buffer_moved_.empty()) {
        wandb_->update_config(config_buffer_moved_.front());
        config_buffer_moved_.pop();
      }
    }
    if (!is_summary_buffer_empty()) {
      std::queue<object::PyDict> summary_buffer_moved_;
      {
        std::lock_guard<std::mutex> lk(buffers_mtx_);
        summary_buffer_moved_ = std::move(summary_buffer_);
      }
      while (!summary_buffer_moved_.empty()) {
        wandb_->update_summary(summary_buffer_moved_.front());
        summary_buffer_moved_.pop();
      }
    }
    if (!is_file_path_buffer_empty()) {
      std::vector<std::string> file_path_buffer_moved_;
      {
        std::lock_guard<std::mutex> lk(buffers_mtx_);
        file_path_buffer_moved_ = std::move(file_path_buffer_);
      }
      for (auto& file_path : file_path_buffer_moved_) {
        wandb_->save(file_path);
      }
    }
  }
}

bool AsyncLoggingWorker::is_buffers_empty() {
  std::lock_guard<std::mutex> lk(buffers_mtx_);
  return log_buffer_.empty() &&      //
         config_buffer_.empty() &&   //
         summary_buffer_.empty() &&  //
         file_path_buffer_.empty();
}

bool AsyncLoggingWorker::is_log_buffer_empty() {
  std::lock_guard<std::mutex> lk(buffers_mtx_);
  return log_buffer_.empty();
}

void AsyncLoggingWorker::append_log(const object::PyDict& log) {
  std::lock_guard<std::mutex> lk(buffers_mtx_);
  log_buffer_.push(log);
  cv_buffers_not_empty_.notify_all();
}

void AsyncLoggingWorker::append_log(object::PyDict&& log) {
  std::lock_guard<std::mutex> lk(buffers_mtx_);
  log_buffer_.push(std::forward<object::PyDict>(log));
  cv_buffers_not_empty_.notify_all();
}

bool AsyncLoggingWorker::is_config_buffer_empty() {
  std::lock_guard<std::mutex> lk(buffers_mtx_);
  return config_buffer_.empty();
}

void AsyncLoggingWorker::append_config(const object::PyDict& config) {
  std::lock_guard<std::mutex> lk(buffers_mtx_);
  config_buffer_.push(config);
  cv_buffers_not_empty_.notify_all();
}

void AsyncLoggingWorker::append_config(object::PyDict&& config) {
  std::lock_guard<std::mutex> lk(buffers_mtx_);
  config_buffer_.push(std::forward<object::PyDict>(config));
  cv_buffers_not_empty_.notify_all();
}

bool AsyncLoggingWorker::is_summary_buffer_empty() {
  std::lock_guard<std::mutex> lk(buffers_mtx_);
  return summary_buffer_.empty();
}

void AsyncLoggingWorker::append_summary(const object::PyDict& summary) {
  std::lock_guard<std::mutex> lk(buffers_mtx_);
  summary_buffer_.push(summary);
  cv_buffers_not_empty_.notify_all();
}

void AsyncLoggingWorker::append_summary(object::PyDict&& summary) {
  std::lock_guard<std::mutex> lk(buffers_mtx_);
  summary_buffer_.push(std::forward<object::PyDict>(summary));
  cv_buffers_not_empty_.notify_all();
}

bool AsyncLoggingWorker::is_file_path_buffer_empty() {
  std::lock_guard<std::mutex> lk(buffers_mtx_);
  return file_path_buffer_.empty();
}

void AsyncLoggingWorker::append_file_path(const std::string& file_path) {
  std::lock_guard<std::mutex> lk(buffers_mtx_);
  file_path_buffer_.emplace_back(file_path);
  cv_buffers_not_empty_.notify_all();
}

void AsyncLoggingWorker::finish() {
  terminal_ = true;
  cv_do_init_.notify_all();
  cv_buffers_not_empty_.notify_all();
}

}  // namespace wandbcpp::internal::async
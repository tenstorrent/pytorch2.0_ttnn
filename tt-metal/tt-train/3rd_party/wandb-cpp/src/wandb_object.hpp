#ifndef WANDB_OBJECT_HPP_
#define WANDB_OBJECT_HPP_
#include <iterator>
#include <optional>
#include <string>
#include <vector>

#include "src/np_object.hpp"
#include "src/py_object.hpp"
#include "wandbcpp.hpp"

#ifdef USE_OPENCV
#include <opencv2/opencv.hpp>
#endif

namespace wandbcpp {

class Table : public internal::object::PyObjectBaseClonable<Table> {
  friend class wandb;
  internal::object::PyList columns_;
  std::vector<internal::object::PyList> data_;
  static internal::object::SharedPyObjectPtr& TablePointer();

 public:
  Table() = default;
  ~Table() {}
  explicit Table(const std::vector<std::string>& columns);
  Table(const std::vector<std::string>& columns,
        const std::vector<internal::object::PyList>& data);
  void add_data(const internal::object::PyList& l);
  void add_data(internal::object::PyList&& l);
  void add_column(std::string name, const internal::object::PyList& l);
  PyObject* get_pyobject() const override;
};

class Object3D : public internal::object::PyObjectBaseClonable<Object3D> {
  friend class wandb;
  static internal::object::SharedPyObjectPtr& Object3DPointer();

 private:
  std::optional<internal::object::PyDict> dict_;
  std::optional<numpy::ndarray> arr_;

 public:
  Object3D() = default;
  ~Object3D() {}
  explicit Object3D(const internal::object::PyDict& dict);
  explicit Object3D(const numpy::ndarray& arr);

  PyObject* get_pyobject() const override;
};

#ifdef USE_OPENCV

class Image : public internal::object::PyObjectBaseClonable<Image> {
  friend class wandb;
  static internal::object::SharedPyObjectPtr& ImagePointer();

 private:
  std::optional<cv::Mat> cv_mat_;
  std::optional<std::string> path_to_image_;

 public:
  Image() = default;
  explicit Image(const cv::Mat& cv_mat) : cv_mat_(cv_mat) {}
  explicit Image(cv::Mat&& cv_mat) : cv_mat_(std::move(cv_mat)) {}
  explicit Image(const std::string& path_to_image)
      : path_to_image_(path_to_image) {}
  ~Image() {}
  PyObject* get_pyobject() const override;
};

class Video : public internal::object::PyObjectBaseClonable<Video> {
  friend class wandb;
  static internal::object::SharedPyObjectPtr& VideoPointer();

 private:
  std::vector<cv::Mat> frames_;
  std::optional<std::string> path_to_video_;

 public:
  Video() = default;
  template <std::input_iterator I>
  explicit Video(I begin, I end) : frames_(begin, end) {}
  explicit Video(const std::string& path_to_video);
  ~Video() {}
  PyObject* get_pyobject() const override;
};

#endif

}  // namespace wandbcpp

#endif
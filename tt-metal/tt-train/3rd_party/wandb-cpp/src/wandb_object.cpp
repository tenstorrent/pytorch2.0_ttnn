#include "src/wandb_object.hpp"

#include <iostream>
#include <utility>

#include "src/np_object.hpp"
#include "src/py_util.hpp"

namespace wandbcpp {

using namespace internal::object;
using namespace internal::util;

internal::object::SharedPyObjectPtr& Table::TablePointer() {
  static internal::object::SharedPyObjectPtr table_;
  return table_;
}

Table::Table(const std::vector<std::string>& columns)
    : columns_(columns.begin(), columns.end()) {}

Table::Table(const std::vector<std::string>& columns,
             const std::vector<internal::object::PyList>& data)
    : columns_(columns.begin(), columns.end()), data_(data) {}

void Table::add_data(const internal::object::PyList& l) {
  data_.emplace_back(l);
}

void Table::add_data(internal::object::PyList&& l) {
  data_.emplace_back(std::forward<internal::object::PyList>(l));
}

void Table::add_column(std::string name, const internal::object::PyList& l) {
  columns_.append(name);
  if (data_.size() != l.size()) {
    data_.resize(l.size());
  }
  for (size_t i = 0; i < l.size(); i++) {
    data_[i].append(l[i]);
  }
}

PyObject* Table::get_pyobject() const {
  SharedPyObjectPtr args(PyTuple().get_pyobject());
  SharedPyObjectPtr kwargs(
      PyDict(
          {{"columns", columns_}, {"data", PyList(data_.begin(), data_.end())}})
          .get_pyobject());
  return PyObject_Call(TablePointer().get(), args.get(), kwargs.get());
}

internal::object::SharedPyObjectPtr& Object3D::Object3DPointer() {
  static internal::object::SharedPyObjectPtr object3d_;
  return object3d_;
}

Object3D::Object3D(const internal::object::PyDict& dict)
    : dict_(dict), arr_(std::nullopt) {}

Object3D::Object3D(const numpy::ndarray& arr)
    : dict_(std::nullopt), arr_(arr) {}

PyObject* Object3D::get_pyobject() const {
  if (dict_) {
    SharedPyObjectPtr args(PyTuple(dict_.value()).get_pyobject());
    SharedPyObjectPtr kwargs(PyDict().get_pyobject());
    return PyObject_Call(Object3DPointer().get(), args.get(), kwargs.get());
  } else if (arr_) {
    SharedPyObjectPtr args(PyTuple(arr_.value()).get_pyobject());
    SharedPyObjectPtr kwargs(PyDict().get_pyobject());
    return PyObject_Call(Object3DPointer().get(), args.get(), kwargs.get());
  }
  return nullptr;
}

#ifdef USE_OPENCV

internal::object::SharedPyObjectPtr& Image::ImagePointer() {
  static internal::object::SharedPyObjectPtr image_;
  return image_;
}

PyObject* Image::get_pyobject() const {
  if (cv_mat_) {
    PyList data;
    for (int i = 0; i < cv_mat_->rows; i++) {
      PyList row;
      for (int j = 0; j < cv_mat_->cols; j++) {
        PyList pixel;
        for (int k = 0; k < cv_mat_->channels(); k++) {
          pixel.append((int)(cv_mat_->at<cv::Vec3b>(i, j)[k]));
        }
        // convert GBR to RGB
        pixel.reverse();
        row.append(pixel);
      }
      data.append(row);
    }

    auto ret = PyCall(ImagePointer(), PyTuple(numpy::ndarray(data)));

    return ret.release();

  } else if (path_to_image_) {
    auto ret = PyCall(ImagePointer(), PyTuple(path_to_image_.value()));
    return ret.release();
  }
  return nullptr;
}

internal::object::SharedPyObjectPtr& Video::VideoPointer() {
  static internal::object::SharedPyObjectPtr video_;
  return video_;
}

Video::Video(const std::string& path_to_video)
    : path_to_video_(path_to_video) {}

PyObject* Video::get_pyobject() const {
  if (frames_.size() > 0) {
    std::cout << "frames size: " << frames_.size() << std::endl;
    PyList data;
    for (const auto& frame : frames_) {
      PyList channel_data;
      for (int k = 0; k < frame.channels(); k++) {
        PyList ch_data;
        for (int i = 0; i < frame.rows; i++) {
          PyList row;
          for (int j = 0; j < frame.cols; j++) {
            // GBR -> RGB
            row.append((int)(frame.at<cv::Vec3b>(i, j)[2 - k]));
          }
          ch_data.append(row);
        }
        channel_data.append(ch_data);
      }
      data.append(channel_data);
    }
    auto ret = PyCall(VideoPointer(), PyTuple(numpy::ndarray(data)));
    return ret.release();
  } else if (path_to_video_) {
    auto ret = PyCall(VideoPointer(), PyTuple(path_to_video_.value()));
    return ret.release();
  }
  return nullptr;
}

#endif

}  // namespace wandbcpp

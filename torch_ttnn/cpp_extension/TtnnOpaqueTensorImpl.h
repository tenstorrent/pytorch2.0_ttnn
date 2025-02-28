#pragma once

#include <ATen/OpaqueTensorImpl.h>
#include "ttnn/tensor/tensor.hpp"
#include <iostream>
#include <string.h>

template <typename Arg, typename... Args>
void doPrint(std::ostream& out, const std::string_view& filename, int lineno, const std::string_view& fn, Arg&& arg, Args&&... args)
{
  out << std::format("{}({})({}): ", filename, lineno, fn);
  out << std::forward<Arg>(arg);
  ((out << std::forward<Args>(args)), ...);
  out << std::endl;
}
#define LOGGING(...) doPrint(std::cout, __FILE_NAME__, __LINE__, __FUNCTION__, __VA_ARGS__)

namespace at {

struct TtnnTensorImpl : public TensorImpl {
  TtnnTensorImpl(
      at::DispatchKeySet key_set,
      const caffe2::TypeMeta data_type,
      c10::Device device,
      ttnn::Tensor& ttnn_tensor,
      c10::intrusive_ptr<c10::StorageImpl> storage) : TensorImpl(key_set, data_type, device), ttnn_tensor_(ttnn_tensor), ttnn_tensor_string_(ttnn_tensor.write_to_string()) {
        storage_ = std::move(storage);
        auto view = ttnn_tensor_.get_logical_shape().view();
        std::vector<int64_t> view_int64;
        std::copy(view.begin(), view.end(), std::back_inserter(view_int64));
        IntArrayRef int_array_ref(&(*view_int64.begin()), &(*view_int64.end()));
        sizes_and_strides_.set_sizes(int_array_ref);
      }

  TtnnTensorImpl(
    at::DispatchKeySet key_set,
    const caffe2::TypeMeta data_type,
    c10::Device device,
    const ttnn::Tensor& ttnn_tensor,
    const Storage& storage) : TensorImpl(key_set, data_type, device), ttnn_tensor_(ttnn_tensor), ttnn_tensor_string_(ttnn_tensor.write_to_string()) {
      storage_ = std::move(storage);
      auto view = ttnn_tensor_.get_logical_shape().view();
      std::vector<int64_t> view_int64;
      std::copy(view.begin(), view.end(), std::back_inserter(view_int64));
      IntArrayRef int_array_ref(&(*view_int64.begin()), &(*view_int64.end()));
      sizes_and_strides_.set_sizes(int_array_ref);
    }

  void set_sizes_and_strides(const IntArrayRef& int_array_ref) {
      sizes_and_strides_.set_sizes(int_array_ref);
  }

  void set_sizes_and_strides_as(const at::Tensor& the_template) {
    sizes_and_strides_.set_sizes(the_template.sizes());
  }

  ttnn::Tensor get_ttnn_tensor() {
    // LOGGING(ttnn_tensor_string_);
    LOGGING(ttnn_tensor_.write_to_string());
    return ttnn_tensor_;
  }

  void set_ttnn_tensor(const ttnn::Tensor& tensor) {
    ttnn_tensor_ = tensor;
  }

  /**
   * Return a TensorImpl that is a shallow-copy of this TensorImpl.
   *
   * For usage of `version_counter` and `allow_tensor_metadata_change`,
   * see NOTE [ TensorImpl Shallow-Copying ].
   */
  c10::intrusive_ptr<TensorImpl> shallow_copy_and_detach(
    const c10::VariableVersion& version_counter,
    bool allow_tensor_metadata_change) const override {
    auto impl = c10::make_intrusive<TtnnTensorImpl>(
        key_set(),
        dtype(),
        device(),
        ttnn_tensor_,
        storage_);
    copy_tensor_metadata(
        /*src_opaque_impl=*/this,
        /*dest_opaque_impl=*/impl.get(),
        /*version_counter=*/version_counter,
        /*allow_tensor_metadata_change=*/allow_tensor_metadata_change);
    impl->refresh_numel();
    return impl;
}

  /**
   * Return a TensorImpl that is a shallow-copy of this TensorImpl.
   *
   * For usage of `version_counter` and `allow_tensor_metadata_change`,
   * see NOTE [ TensorImpl Shallow-Copying ].
   */
  c10::intrusive_ptr<TensorImpl> shallow_copy_and_detach(
    c10::VariableVersion&& version_counter,
    bool allow_tensor_metadata_change) const override {
  auto impl = c10::make_intrusive<TtnnTensorImpl>(
      key_set(),
      dtype(),
      device(),
      ttnn_tensor_,
      storage_);
  copy_tensor_metadata(
      /*src_opaque_impl=*/this,
      /*dest_opaque_impl=*/impl.get(),
      /*version_counter=*/std::move(version_counter),
      /*allow_tensor_metadata_change=*/allow_tensor_metadata_change);
  impl->refresh_numel();
  return impl;
}

/**
 * Shallow-copies data from another TensorImpl into this TensorImpl.
 *
 * For why this function doesn't check this TensorImpl's
 * `allow_tensor_metadata_change_`, see NOTE [ TensorImpl Shallow-Copying ].
 */
void shallow_copy_from(const c10::intrusive_ptr<TensorImpl>& impl) override {
  AT_ASSERT(has_compatible_shallow_copy_type(impl->key_set()));
  auto ttnn_impl =
      static_cast<const TtnnTensorImpl*>(impl.get());
  copy_tensor_metadata(
      /*src_impl=*/ttnn_impl,
      /*dest_impl=*/this,
      /*version_counter=*/version_counter(),
      /*allow_tensor_metadata_change=*/allow_tensor_metadata_change());
  refresh_numel();
}

  // protected:
  //   static void copy_tensor_metadata(
  //     const TtnnTensorImpl* src_impl,
  //     TtnnTensorImpl* dest_impl,
  //     const c10::VariableVersion& version_counter,
  //     bool allow_tensor_metadata_change) {
  //     TensorImpl::copy_tensor_metadata(
  //         src_impl,
  //         dest_impl,
  //         version_counter,
  //         allow_tensor_metadata_change);

  //     // TtnnTensorImpl-specific fields.
  //     dest_impl->ttnn_tensor_ = src_impl->ttnn_tensor_;
  //     dest_impl->ttnn_tensor_string_ = src_impl->ttnn_tensor_string_;
  //   }

  //   static void copy_tensor_metadata(
  //     const TtnnTensorImpl* src_impl,
  //     TtnnTensorImpl* dest_impl,
  //     c10::VariableVersion&& version_counter,
  //     bool allow_tensor_metadata_change) {
  //       TensorImpl::copy_tensor_metadata(
  //           src_impl,
  //           dest_impl,
  //           std::move(version_counter),
  //           allow_tensor_metadata_change);

  //     // TtnnTensorImpl-specific fields.
  //     dest_impl->ttnn_tensor_ = src_impl->ttnn_tensor_;
  //     dest_impl->ttnn_tensor_string_ = src_impl->ttnn_tensor_string_;
  //   }

  private:
    ttnn::Tensor ttnn_tensor_;
    std::string ttnn_tensor_string_;
};

} // namespace at
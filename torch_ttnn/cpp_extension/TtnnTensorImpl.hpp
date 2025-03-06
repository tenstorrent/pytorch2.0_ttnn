#pragma once

#include "ttnn/tensor/tensor.hpp"
#include "extension_utils.hpp"
#include <iostream>
#include <string.h>

namespace at {

struct TtnnTensorImpl : public TensorImpl {
  // TODO: Only difference is the storage type, combine these two
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
    LOGGING("");
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
  private:
    ttnn::Tensor ttnn_tensor_;
    // TODO: Debug only, should probably remove as it might be costly
    std::string ttnn_tensor_string_;
};

} // namespace at
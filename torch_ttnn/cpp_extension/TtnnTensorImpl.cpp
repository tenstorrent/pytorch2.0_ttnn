#include "TtnnTensorImpl.hpp"

namespace at {

// TODO: Only difference is the storage type, combine these two
TtnnTensorImpl::TtnnTensorImpl(
    at::DispatchKeySet key_set,
    const caffe2::TypeMeta data_type,
    c10::Device device,
    ttnn::Tensor& ttnn_tensor,
    c10::intrusive_ptr<c10::StorageImpl> storage) :
    TensorImpl(key_set, data_type, device),
    ttnn_tensor_(ttnn_tensor),
    ttnn_tensor_string_(ttnn_tensor.write_to_string()) {
    storage_ = std::move(storage);
    auto view = ttnn_tensor_.get_logical_shape().view();
    std::vector<int64_t> view_int64;
    std::copy(view.begin(), view.end(), std::back_inserter(view_int64));
    IntArrayRef int_array_ref(&(*view_int64.begin()), &(*view_int64.end()));
    sizes_and_strides_.set_sizes(int_array_ref);
}

TtnnTensorImpl::TtnnTensorImpl(
    at::DispatchKeySet key_set,
    const caffe2::TypeMeta data_type,
    c10::Device device,
    const ttnn::Tensor& ttnn_tensor,
    const c10::Storage& storage) :
    TensorImpl(key_set, data_type, device),
    ttnn_tensor_(ttnn_tensor),
    ttnn_tensor_string_(ttnn_tensor.write_to_string()) {
    storage_ = std::move(storage);
    auto view = ttnn_tensor_.get_logical_shape().view();
    std::vector<int64_t> view_int64;
    std::copy(view.begin(), view.end(), std::back_inserter(view_int64));
    IntArrayRef int_array_ref(&(*view_int64.begin()), &(*view_int64.end()));
    sizes_and_strides_.set_sizes(int_array_ref);
}

void TtnnTensorImpl::set_sizes_and_strides(const IntArrayRef& int_array_ref) {
    sizes_and_strides_.set_sizes(int_array_ref);
}

void TtnnTensorImpl::set_sizes_and_strides_as(const at::Tensor& the_template) {
    sizes_and_strides_.set_sizes(the_template.sizes());
}

ttnn::Tensor TtnnTensorImpl::get_ttnn_tensor() {
    LOGGING("");
    return ttnn_tensor_;
}

void TtnnTensorImpl::set_ttnn_tensor(const ttnn::Tensor& tensor) { ttnn_tensor_ = tensor; }

c10::intrusive_ptr<TensorImpl> TtnnTensorImpl::shallow_copy_and_detach(
    const c10::VariableVersion& version_counter, bool allow_tensor_metadata_change) const {
    auto impl = c10::make_intrusive<TtnnTensorImpl>(key_set(), dtype(), device(), ttnn_tensor_, storage_);
    copy_tensor_metadata(
        /*src_opaque_impl=*/this,
        /*dest_opaque_impl=*/impl.get(),
        /*version_counter=*/version_counter,
        /*allow_tensor_metadata_change=*/allow_tensor_metadata_change);
    impl->refresh_numel();
    return impl;
}

c10::intrusive_ptr<TensorImpl> TtnnTensorImpl::shallow_copy_and_detach(
    c10::VariableVersion&& version_counter, bool allow_tensor_metadata_change) const {
    auto impl = c10::make_intrusive<TtnnTensorImpl>(key_set(), dtype(), device(), ttnn_tensor_, storage_);
    copy_tensor_metadata(
        /*src_opaque_impl=*/this,
        /*dest_opaque_impl=*/impl.get(),
        /*version_counter=*/std::move(version_counter),
        /*allow_tensor_metadata_change=*/allow_tensor_metadata_change);
    impl->refresh_numel();
    return impl;
}

void TtnnTensorImpl::shallow_copy_from(const c10::intrusive_ptr<TensorImpl>& impl) {
    AT_ASSERT(has_compatible_shallow_copy_type(impl->key_set()));
    auto ttnn_impl = static_cast<const TtnnTensorImpl*>(impl.get());
    copy_tensor_metadata(
        /*src_impl=*/ttnn_impl,
        /*dest_impl=*/this,
        /*version_counter=*/version_counter(),
        /*allow_tensor_metadata_change=*/allow_tensor_metadata_change());
    refresh_numel();
}

}  // namespace at
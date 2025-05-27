#include <ttnn/device.hpp>
#include <ttnn/operations/creation.hpp>

#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"

#include "ttnn_cpp_extension/utils/extension_utils.hpp"

namespace {
std::vector<int64_t> get_row_major_strides(const std::vector<int64_t>& sizes) {
    std::vector<int64_t> strides(sizes.size());
    size_t stride = 1;
    for (int i = sizes.size() - 1; i >= 0; --i) {
        strides[i] = stride;
        stride *= sizes[i];
    }
    return strides;
}
}  // namespace

namespace at {

TtnnTensorImpl::TtnnTensorImpl(
    at::DispatchKeySet key_set,
    const caffe2::TypeMeta data_type,
    c10::Device device,
    const at::IntArrayRef& size,
    const c10::Storage& storage) :
    TensorImpl(key_set, data_type, device) {
    storage_ = std::move(storage);

    sizes_ = std::vector<int64_t>(size.begin(), size.end());
    strides_ = get_row_major_strides(sizes_);

    sizes_and_strides_.set_sizes(sizes_);
    sizes_and_strides_.set_strides(strides_);
    ttnn::SmallVector<uint32_t> small_vector(size.begin(), size.end());
    logical_shape_ = ttnn::Shape(small_vector);
}

void TtnnTensorImpl::set_sizes_and_strides(const IntArrayRef& int_array_ref) {
    sizes_and_strides_.set_sizes(int_array_ref);
}

void TtnnTensorImpl::set_sizes_and_strides_as(const at::Tensor& the_template) {
    sizes_and_strides_.set_sizes(the_template.sizes());
}

ttnn::Tensor TtnnTensorImpl::get_ttnn_tensor() const {
    LOGGING("");
    TORCH_CHECK(ttnn_tensor_.tensor_attributes != nullptr);
    return ttnn_tensor_;
}

void TtnnTensorImpl::set_ttnn_tensor(const ttnn::Tensor& tensor) {
    LOGGING("");
    ttnn_tensor_ = tensor;
}

c10::intrusive_ptr<TensorImpl> TtnnTensorImpl::shallow_copy_and_detach(
    const c10::VariableVersion& version_counter, bool allow_tensor_metadata_change) const {
    auto impl = c10::make_intrusive<TtnnTensorImpl>(
        key_set(), dtype(), device(), sizes_and_strides_.sizes_arrayref(), storage_);
    impl->set_ttnn_tensor(ttnn_tensor_);
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
    auto impl = c10::make_intrusive<TtnnTensorImpl>(
        key_set(), dtype(), device(), sizes_and_strides_.sizes_arrayref(), storage_);
    impl->set_ttnn_tensor(ttnn_tensor_);
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

ttnn::Shape TtnnTensorImpl::get_logical_shape() const {
    // TODO: Do we need to check if this is valid?
    return logical_shape_;
}

}  // namespace at

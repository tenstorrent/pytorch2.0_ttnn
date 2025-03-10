#include "TtnnTensorImpl.hpp"
#include "ttnn/device.hpp"
#include "ttnn/operations/creation.hpp"
#include "TtnnGuard.hpp"

namespace at {

TtnnTensorImpl::TtnnTensorImpl(
    at::DispatchKeySet key_set,
    const caffe2::TypeMeta data_type,
    c10::Device device,
    const at::IntArrayRef& size,
    const c10::Storage& storage) :
    TensorImpl(key_set, data_type, device) {
    storage_ = std::move(storage);
    sizes_and_strides_.set_sizes(size);
    ttnn::SmallVector<uint32_t> small_vector(size.begin(), size.end());
    logical_shape_ = ttnn::Shape(small_vector);
    is_empty_initialized_ = true;
}

void TtnnTensorImpl::set_sizes_and_strides(const IntArrayRef& int_array_ref) {
    sizes_and_strides_.set_sizes(int_array_ref);
}

void TtnnTensorImpl::set_sizes_and_strides_as(const at::Tensor& the_template) {
    sizes_and_strides_.set_sizes(the_template.sizes());
}

ttnn::Tensor TtnnTensorImpl::get_ttnn_tensor() {
    LOGGING("");
    if (is_empty_initialized_) {
        at::Device at_device = GET_OPTIONAL_OR_ASSERT(device_opt_);
        TtnnGuard device_guard(at_device);
        IDevice* ttnn_device = device_guard.get_ttnn_device();

        auto ttnn_dtype = dtype_torch_to_ttnn(c10::typeMetaToScalarType(this->dtype()));
        ttnn_tensor_ = ttnn::empty(
            get_logical_shape(),
            ttnn_dtype,
            ttnn::TILE_LAYOUT,
            ttnn_device,
            MemoryConfig{TensorMemoryLayout::INTERLEAVED, BufferType::DRAM, std::nullopt});
        is_empty_initialized_ = false;
    }

    TORCH_CHECK(ttnn_tensor_.tensor_attributes != nullptr);
    return ttnn_tensor_;
}

void TtnnTensorImpl::set_ttnn_tensor(const ttnn::Tensor& tensor) {
    LOGGING("");
    // TORCH_CHECK(ttnn_tensor_.tensor_attributes == nullptr);
    is_empty_initialized_ = false;
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

ttnn::Shape TtnnTensorImpl::get_logical_shape() {
    // TODO: Do we need to check if this is valid?
    return logical_shape_;
}

}  // namespace at
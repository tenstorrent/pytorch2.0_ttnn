#pragma once

#include <cstdint>

#include "c10/core/TensorImpl.h"
#include "ATen/core/Tensor.h"
#include "ttnn/tensor/tensor.hpp"

namespace at {

struct TtnnTensorImpl : public TensorImpl {
    TtnnTensorImpl(
        at::DispatchKeySet key_set,
        const caffe2::TypeMeta data_type,
        c10::Device device,
        const at::IntArrayRef& size,
        const c10::Storage& storage);

    void set_sizes_and_strides(const IntArrayRef& int_array_ref);

    void set_sizes_and_strides_as(const at::Tensor& the_template);

    ttnn::Tensor get_ttnn_tensor() const;

    void set_ttnn_tensor(const ttnn::Tensor& tensor);

    ttnn::Shape get_logical_shape() const;

    /**
     * Return a TensorImpl that is a shallow-copy of this TensorImpl.
     *
     * For usage of `version_counter` and `allow_tensor_metadata_change`,
     * see NOTE [ TensorImpl Shallow-Copying ].
     */
    c10::intrusive_ptr<TensorImpl> shallow_copy_and_detach(
        const c10::VariableVersion& version_counter, bool allow_tensor_metadata_change) const override;

    /**
     * Return a TensorImpl that is a shallow-copy of this TensorImpl.
     *
     * For usage of `version_counter` and `allow_tensor_metadata_change`,
     * see NOTE [ TensorImpl Shallow-Copying ].
     */
    c10::intrusive_ptr<TensorImpl> shallow_copy_and_detach(
        c10::VariableVersion&& version_counter, bool allow_tensor_metadata_change) const override;

    /**
     * Shallow-copies data from another TensorImpl into this TensorImpl.
     *
     * For why this function doesn't check this TensorImpl's
     * `allow_tensor_metadata_change_`, see NOTE [ TensorImpl Shallow-Copying ].
     */
    void shallow_copy_from(const c10::intrusive_ptr<TensorImpl>& impl) override;

private:
    ttnn::Tensor ttnn_tensor_;
    ttnn::Shape logical_shape_;

    std::vector<int64_t> sizes_;
    std::vector<int64_t> strides_;
};

}  // namespace at

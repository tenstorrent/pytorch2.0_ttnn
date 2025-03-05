#pragma once

#include <string.h>

#include <iostream>

#include "c10/core/TensorImpl.h"
#include "ATen/core/Tensor.h"
#include "extension_utils.hpp"
#include "ttnn/tensor/tensor.hpp"

namespace at {

struct TtnnTensorImpl : public TensorImpl {
    // TODO: Only difference is the storage type, combine these two
    TtnnTensorImpl(
        at::DispatchKeySet key_set,
        const caffe2::TypeMeta data_type,
        c10::Device device,
        ttnn::Tensor& ttnn_tensor,
        c10::intrusive_ptr<c10::StorageImpl> storage);

    TtnnTensorImpl(
        at::DispatchKeySet key_set,
        const caffe2::TypeMeta data_type,
        c10::Device device,
        const ttnn::Tensor& ttnn_tensor,
        const c10::Storage& storage);

    void set_sizes_and_strides(const IntArrayRef& int_array_ref);

    void set_sizes_and_strides_as(const at::Tensor& the_template);

    ttnn::Tensor get_ttnn_tensor();

    void set_ttnn_tensor(const ttnn::Tensor& tensor);

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
    // TODO: Debug only, should probably remove as it might be costly
    std::string ttnn_tensor_string_;
};

}  // namespace at
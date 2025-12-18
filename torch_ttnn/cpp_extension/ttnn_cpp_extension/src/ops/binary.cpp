#include <c10/util/Optional.h>

#include <ttnn/operations/eltwise/binary/binary.hpp>

#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"

#include "ttnn_cpp_extension/ops/binary.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"

#include "ttnn_cpp_extension/utils/extension_utils.hpp"

namespace tt_eager::ops::binary {
at::Tensor& ttnn_add_out(const at::Tensor& input, const at::Tensor& other, const at::Scalar& alpha, at::Tensor& out) {
    LOGGING("input device: {}, other device: {}", input.device(), other.device());
    TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(other.device().type() == c10::DeviceType::PrivateUse1);

    at::TtnnTensorImpl* tensor_impl = static_cast<at::TtnnTensorImpl*>(input.unsafeGetTensorImpl());
    auto ttnn_tensor_input = tensor_impl->get_ttnn_tensor();
    if (ttnn_tensor_input.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_tensor_input = ttnn::to_layout(ttnn_tensor_input, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt);
    }

    at::TtnnTensorImpl* other_tensor_impl = static_cast<at::TtnnTensorImpl*>(other.unsafeGetTensorImpl());
    auto ttnn_tensor_other = other_tensor_impl->get_ttnn_tensor();
    if (ttnn_tensor_other.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_tensor_other = ttnn::to_layout(ttnn_tensor_other, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt);
    }

    auto result = ttnn::add(ttnn_tensor_input, ttnn_tensor_other);

    // tensor_impl->set_ttnn_tensor(result);
    // Get underlying TTNN tensor object from output
    at::TtnnTensorImpl* out_tensor_impl = static_cast<at::TtnnTensorImpl*>(out.unsafeGetTensorImpl());
    out_tensor_impl->set_sizes_and_strides_as(input);

    // Set output TTNN tensor to result
    auto out_ttnn_tensor = out_tensor_impl->get_ttnn_tensor();
    out_tensor_impl->set_ttnn_tensor(result);
    return out;
}

// Add this function to your open_registration_extension.cpp
at::Tensor ttnn_add_tensor(const at::Tensor& input, const at::Tensor& other, const at::Scalar& alpha) {
    LOGGING("Creating new output tensor");
    // Create a new output tensor on the right device
    // auto output = at::empty(input.sizes(), input.options());
    auto output = tt_eager::ops::create::custom_empty_memory_format(
        input.sizes(),
        c10::optional<at::ScalarType>(input.scalar_type()),
        c10::nullopt,  // layout
        c10::optional<at::Device>(input.device()),
        c10::nullopt  // pin_memory
    );

    // Call the existing out version
    return ttnn_add_out(input, other, alpha, output);
}
}  // namespace tt_eager::ops::binary

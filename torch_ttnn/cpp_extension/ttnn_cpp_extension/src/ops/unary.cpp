#include "ttnn_cpp_extension/ops/unary.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"

#include <ttnn/operations/eltwise/unary/unary.hpp>
#include <ttnn/operations/creation.hpp>
#include <ttnn/operations/activation/tanh.hpp>

namespace tt_eager::ops::unary {
at::Tensor& ttnn_abs_out(const at::Tensor& self, at::Tensor& out) {
    LOGGING("");
    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(out.device().type() == c10::DeviceType::PrivateUse1);

    // Get underlying TTNN tensor object from input
    at::TtnnTensorImpl* tensor_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = tensor_impl->get_ttnn_tensor();

    // Call TTNN operation
    auto result = ttnn::abs(ttnn_tensor);

    // Get underlying TTNN tensor object from output
    at::TtnnTensorImpl* out_tensor_impl = static_cast<at::TtnnTensorImpl*>(out.unsafeGetTensorImpl());
    out_tensor_impl->set_sizes_and_strides_as(self);

    // Set output TTNN tensor to result
    auto out_ttnn_tensor = out_tensor_impl->get_ttnn_tensor();
    out_tensor_impl->set_ttnn_tensor(result);

    return out;
}

at::Tensor ttnn_clone(const at::Tensor& self, c10::optional<at::MemoryFormat> memory_format_opt) {
    LOGGING("Running aten::clone.default");

    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);

    // Get the TTNN tensor
    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = self_impl->get_ttnn_tensor();

    // Perform the TTNN clone
    auto cloned = ttnn::clone(ttnn_tensor);

    // Create the output tensor
    auto output = tt_eager::ops::create::custom_empty_memory_format(
        self.sizes(),
        c10::optional<at::ScalarType>(self.scalar_type()),
        c10::nullopt,
        c10::optional<at::Device>(self.device()),
        c10::nullopt,
        memory_format_opt
    );

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(self);
    out_impl->set_ttnn_tensor(cloned);

    return output;
}

at::Tensor ttnn_gelu(const at::Tensor& self) {
    LOGGING("Running aten::gelu.default");

    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);

    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = self_impl->get_ttnn_tensor();

    // Convert to TILE layout if needed
    if (ttnn_tensor.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_tensor = ttnn::to_layout(ttnn_tensor, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_tensor.device());
    }

    auto result_tensor = ttnn::gelu(ttnn_tensor);  // TTNN implementation

    // Wrap in at::Tensor
    auto output = tt_eager::ops::create::custom_empty_memory_format(
        self.sizes(),
        c10::optional<at::ScalarType>(self.scalar_type()),
        c10::nullopt,
        c10::optional<at::Device>(self.device()),
        c10::nullopt
    );

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(self);
    out_impl->set_ttnn_tensor(result_tensor);

    return output;
}

at::Tensor ttnn_tanh(const at::Tensor& self) {
    LOGGING("Running aten::tanh.default");

    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);

    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = self_impl->get_ttnn_tensor();

    if (ttnn_tensor.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_tensor = ttnn::to_layout(ttnn_tensor, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_tensor.device());
    }

    auto result = ttnn::tanh(ttnn_tensor);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        self.sizes(),
        c10::optional<at::ScalarType>(self.scalar_type()),
        c10::nullopt,
        c10::optional<at::Device>(self.device()),
        c10::nullopt
    );

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(self);
    out_impl->set_ttnn_tensor(result);

    return output;
}


}  // namespace tt_eager::ops::unary

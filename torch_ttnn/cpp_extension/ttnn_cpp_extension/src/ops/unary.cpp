#include "ttnn_cpp_extension/ops/unary.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/utils/layout_utils.hpp"

#include <ttnn/operations/eltwise/unary/unary.hpp>

namespace tt_eager::ops::unary {

at::Tensor& ttnn_abs_out(const at::Tensor& self, at::Tensor& out) {
    LOGGING("");
    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(out.device().type() == c10::DeviceType::PrivateUse1);

    at::TtnnTensorImpl* tensor_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = tensor_impl->get_ttnn_tensor();

    auto result = ttnn::abs(ttnn_tensor);

    at::TtnnTensorImpl* out_tensor_impl = static_cast<at::TtnnTensorImpl*>(out.unsafeGetTensorImpl());
    out_tensor_impl->set_sizes_and_strides_as(self);

    auto out_ttnn_tensor = out_tensor_impl->get_ttnn_tensor();
    out_tensor_impl->set_ttnn_tensor(result);

    return out;
}

// Helper for simple unary ops
template <typename TtnnOp>
at::Tensor ttnn_unary_op(const at::Tensor& self, TtnnOp&& ttnn_operation, const char* op_name) {
    LOGGING("Running", op_name);
    TORCH_CHECK(
        self.device().type() == c10::DeviceType::PrivateUse1,
        std::string(op_name) + ": only PrivateUse1 device is supported");

    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = self_impl->get_ttnn_tensor();
    ttnn_tensor = tt_eager::utils::ensure_tile_layout(ttnn_tensor);
    auto result = ttnn_operation(ttnn_tensor);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        self.sizes(),
        self.scalar_type(),
        /*strides=*/c10::nullopt,
        self.device(),
        /*pin_memory=*/c10::nullopt);

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(self);
    out_impl->set_ttnn_tensor(result);
    return output;
}

// Helper for unary ops with validation
template <typename TtnnOp, typename ValidationFn>
at::Tensor ttnn_unary_op_with_validation(
    const at::Tensor& self, TtnnOp&& ttnn_operation, ValidationFn&& validation, const char* op_name) {
    LOGGING("Running", op_name);
    TORCH_CHECK(
        self.device().type() == c10::DeviceType::PrivateUse1,
        std::string(op_name) + ": only PrivateUse1 device is supported");
    validation();
    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = self_impl->get_ttnn_tensor();
    ttnn_tensor = tt_eager::utils::ensure_tile_layout(ttnn_tensor);
    auto result = ttnn_operation(ttnn_tensor);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        self.sizes(),
        self.scalar_type(),
        /*strides=*/c10::nullopt,
        self.device(),
        /*pin_memory=*/c10::nullopt);

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(self);
    out_impl->set_ttnn_tensor(result);
    return output;
}

at::Tensor ttnn_gelu(const at::Tensor& self, c10::string_view approximate) {
    return ttnn_unary_op_with_validation(
        self,
        ttnn::gelu,
        [approximate]() { TORCH_CHECK(approximate == "none", "ttnn_gelu: only approximate='none' is supported"); },
        "aten::gelu.default");
}

at::Tensor ttnn_tanh(const at::Tensor& self) { return ttnn_unary_op(self, ttnn::tanh, "aten::tanh.default"); }

}  // namespace tt_eager::ops::unary

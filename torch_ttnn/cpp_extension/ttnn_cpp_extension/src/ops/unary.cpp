// src/ops/unary.cpp

#include "ttnn_cpp_extension/ops/unary.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"

#include <ttnn/operations/data_movement/clone/clone.hpp>
#include <ttnn/tensor/types.hpp>
#include <ttnn/operations/core/compute_kernel/compute_kernel_config.hpp>
#include <tt-metalium/base_types.hpp>

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

at::Tensor ttnn_clone(const at::Tensor& self, c10::optional<at::MemoryFormat> memory_format_opt) {
    LOGGING("Running aten::clone.default");
    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);

    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = self_impl->get_ttnn_tensor();

    auto cloned =
        ttnn::operations::data_movement::clone::Clone::invoke(ttnn_tensor, std::nullopt, std::nullopt, std::nullopt);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        self.sizes(),
        self.scalar_type(),
        /*strides=*/c10::nullopt,
        /*device=*/self.device(),
        /*pin_memory=*/c10::nullopt,
        memory_format_opt);
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(self);
    out_impl->set_ttnn_tensor(cloned);

    return output;
}

at::Tensor ttnn_gelu(const at::Tensor& self, c10::string_view approximate) {
    LOGGING("Running aten::gelu.default");

    TORCH_CHECK(
        self.device().type() == c10::DeviceType::PrivateUse1, "ttnn_gelu: only PrivateUse1 device is supported");

    TORCH_CHECK(approximate == "none", "ttnn_gelu: only approximate='none' is supported");

    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = self_impl->get_ttnn_tensor();

    if (ttnn_tensor.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_tensor = ttnn::to_layout(
            ttnn_tensor,
            ttnn::TILE_LAYOUT,
            /*queue_id=*/std::nullopt,
            /*kernel_cfg=*/std::nullopt,
            ttnn_tensor.device());
    }

    auto result = ttnn::gelu(ttnn_tensor);

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

at::Tensor ttnn_tanh(const at::Tensor& self) {
    LOGGING("Running aten::tanh.default");
    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);

    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = self_impl->get_ttnn_tensor();
    if (ttnn_tensor.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_tensor = ttnn::to_layout(
            ttnn_tensor,
            ttnn::TILE_LAYOUT,
            /*queue_id=*/std::nullopt,
            /*kernel_cfg=*/std::nullopt,
            ttnn_tensor.device());
    }

    auto result = ttnn::tanh(ttnn_tensor);

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

}  // namespace tt_eager::ops::unary

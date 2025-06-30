#include "ttnn_cpp_extension/ops/norm.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"

#include <ttnn/operations/normalization/layernorm/layernorm.hpp>

namespace tt_eager::ops::norm {

std::tuple<at::Tensor, at::Tensor, at::Tensor> ttnn_native_layer_norm(
    const at::Tensor& input,
    at::IntArrayRef normalized_shape,
    const c10::optional<at::Tensor>& weight,
    const c10::optional<at::Tensor>& bias,
    double eps) {

    LOGGING("Running aten::native_layer_norm.default");

    TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1);
    if (weight.has_value()) TORCH_CHECK(weight->device().type() == c10::DeviceType::PrivateUse1);
    if (bias.has_value()) TORCH_CHECK(bias->device().type() == c10::DeviceType::PrivateUse1);

    auto* input_impl = static_cast<at::TtnnTensorImpl*>(input.unsafeGetTensorImpl());
    auto ttnn_input = input_impl->get_ttnn_tensor();

    if (ttnn_input.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_input = ttnn::to_layout(ttnn_input, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_input.device());
    }

    std::optional<ttnn::Tensor> ttnn_weight = std::nullopt;
    std::optional<ttnn::Tensor> ttnn_bias = std::nullopt;

    if (weight.has_value()) {
        auto* w_impl = static_cast<at::TtnnTensorImpl*>(weight->unsafeGetTensorImpl());
        ttnn_weight = w_impl->get_ttnn_tensor();
    }
    if (bias.has_value()) {
        auto* b_impl = static_cast<at::TtnnTensorImpl*>(bias->unsafeGetTensorImpl());
        ttnn_bias = b_impl->get_ttnn_tensor();
    }

    auto ttnn_output = ttnn::operations::normalization::ExecuteLayerNorm::invoke(
        ttnn_input,
        static_cast<float>(eps),
        ttnn_weight,
        ttnn_bias,
        std::nullopt,   // residual_input_tensor
        std::nullopt,   // memory_config
        std::nullopt,   // program_config
        std::nullopt    // compute_kernel_config
    );


    auto wrap = [&](const ttnn::Tensor& t, const at::Tensor& ref) {
        // Convert TTNN tensor's shape (likely uint32_t) to int64_t for ATen compatibility
        std::vector<int64_t> shape_vec;
        for (auto it = t.logical_shape().cbegin(); it != t.logical_shape().cend(); ++it) {
            shape_vec.push_back(static_cast<int64_t>(*it));
        }

        // Create an empty ATen tensor with the correct shape, dtype, and device
        auto out = tt_eager::ops::create::custom_empty_memory_format(
            shape_vec,
            ref.scalar_type(),
            c10::nullopt,        // layout
            ref.device(),
            c10::nullopt         // memory_format
        );

        // Attach TTNN tensor to ATen wrapper
        auto* impl = static_cast<at::TtnnTensorImpl*>(out.unsafeGetTensorImpl());
        impl->set_ttnn_tensor(t);

        return out;
    };

    auto out_tensor = wrap(ttnn_output, input);

    // Return empty mean/rstd tensors (dummy)
    auto dummy_shape = std::vector<int64_t>{1};
    auto mean_tensor = at::empty(dummy_shape, input.options());
    auto rstd_tensor = at::empty(dummy_shape, input.options());

    return std::make_tuple(out_tensor, mean_tensor, rstd_tensor);
}

}

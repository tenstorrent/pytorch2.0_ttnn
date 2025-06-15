#include "ttnn_cpp_extension/ops/norm.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"

#include <ttnn/operations/normalization/layer_norm.hpp>

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

    ttnn::Tensor ttnn_weight, ttnn_bias;
    if (weight.has_value()) {
        auto* w_impl = static_cast<at::TtnnTensorImpl*>(weight->unsafeGetTensorImpl());
        ttnn_weight = w_impl->get_ttnn_tensor();
    }
    if (bias.has_value()) {
        auto* b_impl = static_cast<at::TtnnTensorImpl*>(bias->unsafeGetTensorImpl());
        ttnn_bias = b_impl->get_ttnn_tensor();
    }

    // Convert normalized_shape to TTNN::Shape
    ttnn::SmallVector<uint32_t> norm_dims(normalized_shape.begin(), normalized_shape.end());
    ttnn::Shape ttnn_norm_shape(norm_dims);

    // Run TTNN native layer norm
    auto [ttnn_output, ttnn_mean, ttnn_rstd] = ttnn::native_layer_norm(
        ttnn_input, ttnn_norm_shape, weight.has_value() ? &ttnn_weight : nullptr,
        bias.has_value() ? &ttnn_bias : nullptr, eps);

    // Wrap each result
    auto make_tensor = [&](const ttnn::Tensor& t, const at::Tensor& ref) {
        auto out = tt_eager::ops::create::custom_empty_memory_format(
            t.shape().to_sizes(),
            ref.scalar_type(),
            c10::nullopt,
            ref.device(),
            c10::nullopt);
        auto* impl = static_cast<at::TtnnTensorImpl*>(out.unsafeGetTensorImpl());
        impl->set_ttnn_tensor(t);
        return out;
    };

    auto out_tensor = make_tensor(ttnn_output, input);
    auto mean_tensor = make_tensor(ttnn_mean, input);
    auto rstd_tensor = make_tensor(ttnn_rstd, input);

    return std::make_tuple(out_tensor, mean_tensor, rstd_tensor);
}

}  // namespace tt_eager::ops::norm

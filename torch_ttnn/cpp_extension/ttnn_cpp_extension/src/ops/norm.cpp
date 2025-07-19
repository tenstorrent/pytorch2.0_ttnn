#include "ttnn_cpp_extension/ops/norm.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"
#include "ttnn_cpp_extension/utils/layout_utils.hpp"

#include <ttnn/operations/normalization/layernorm/layernorm.hpp>
#include <ttnn/operations/data_movement/reshape_view/reshape.hpp>

#include <sstream>

namespace tt_eager::ops::norm {

constexpr int TILE_WIDTH = 32;

std::tuple<at::Tensor, at::Tensor, at::Tensor> ttnn_native_layer_norm(
    const at::Tensor& input,
    at::IntArrayRef normalized_shape,
    const c10::optional<at::Tensor>& weight,
    const c10::optional<at::Tensor>& bias,
    double eps) {
    LOGGING("Running aten::native_layer_norm.default");
    TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1, "Expected TTNN tensor");

    const auto orig_sizes = input.sizes();
    TORCH_CHECK(orig_sizes.size() == 3, "Expected input with shape [B, N, D]");
    TORCH_CHECK(orig_sizes.back() == 1024, "Expected input.shape[-1] == 1024");
    TORCH_CHECK(normalized_shape.back() == 1024, "Expected normalized_shape[-1] == 1024");

    const int64_t batch = orig_sizes[0];
    const int64_t blocks = orig_sizes[1];
    const int64_t dim = orig_sizes[2];
    TORCH_CHECK(dim % TILE_WIDTH == 0, "Last dim must be divisible by TILE_WIDTH");

    const int64_t reshaped_blocks = blocks * (dim / TILE_WIDTH);
    at::Tensor reshaped_input = input.view({batch, reshaped_blocks, TILE_WIDTH});

    auto* input_impl = static_cast<at::TtnnTensorImpl*>(reshaped_input.unsafeGetTensorImpl());
    auto ttnn_input = input_impl->get_ttnn_tensor();

    ttnn_input = tt_eager::utils::ensure_tile_layout(ttnn_input);

    auto convert_tensor = [](const at::Tensor& tensor) -> ttnn::Tensor {
        TORCH_CHECK(tensor.numel() == 1024, "Expected 1024-element weight or bias tensor");
        at::Tensor reshaped = tensor.view({TILE_WIDTH, TILE_WIDTH});
        auto* impl = static_cast<at::TtnnTensorImpl*>(reshaped.unsafeGetTensorImpl());
        return impl->get_ttnn_tensor();
    };

    std::optional<ttnn::Tensor> ttnn_weight =
        weight.has_value() ? std::make_optional(convert_tensor(weight.value())) : std::nullopt;
    std::optional<ttnn::Tensor> ttnn_bias =
        bias.has_value() ? std::make_optional(convert_tensor(bias.value())) : std::nullopt;

    auto result = ttnn::layer_norm(ttnn_input, static_cast<float>(eps), ttnn_weight, ttnn_bias);

    std::vector<uint32_t> shape_vec(orig_sizes.begin(), orig_sizes.end());
    auto reshaped_result = ttnn::reshape(result, ttnn::Shape{shape_vec});

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        orig_sizes, input.scalar_type(), std::nullopt, input.device(), std::nullopt);

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(input);
    out_impl->set_ttnn_tensor(reshaped_result);

    auto mean_rstd_shape = orig_sizes.vec();
    std::fill(mean_rstd_shape.end() - normalized_shape.size(), mean_rstd_shape.end(), 1);

    auto mean_tensor = tt_eager::ops::create::custom_empty_memory_format(
        mean_rstd_shape, input.scalar_type(), std::nullopt, input.device(), std::nullopt);

    auto rstd_tensor = tt_eager::ops::create::custom_empty_memory_format(
        mean_rstd_shape, input.scalar_type(), std::nullopt, input.device(), std::nullopt);

    return std::make_tuple(output, mean_tensor, rstd_tensor);
}

}  // namespace tt_eager::ops::norm

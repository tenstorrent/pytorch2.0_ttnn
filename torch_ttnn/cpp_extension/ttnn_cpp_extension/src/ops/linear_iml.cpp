#include "ttnn_cpp_extension/ops/linear_iml.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"

#include <vector>
#include <numeric>
#include <sstream>
#include <iostream>

#include <ttnn/operations/matmul/matmul.hpp>
#include <ttnn/operations/eltwise/binary/binary.hpp>
#include <ttnn/operations/data_movement/reshape_view/reshape.hpp>
#include <ttnn/operations/data_movement/transpose/transpose.hpp>

namespace tt_eager::ops::linear {

static ttnn::Tensor ensure_tile(ttnn::Tensor t) {
    if (t.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        t = ttnn::to_layout(t, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, t.device());
    }
    return t;
}

at::Tensor ttnn_linear(const at::Tensor& input, const at::Tensor& weight, const c10::optional<at::Tensor>& bias) {
    LOGGING("Running aten::linear");
    TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(weight.device().type() == c10::DeviceType::PrivateUse1);

    if (input.dim() == 0 || input.size(0) == 0) {
        throw std::runtime_error("Input tensor has invalid dimensions");
    }

    auto* input_impl = static_cast<at::TtnnTensorImpl*>(input.unsafeGetTensorImpl());
    auto* weight_impl = static_cast<at::TtnnTensorImpl*>(weight.unsafeGetTensorImpl());

    auto ttnn_input = ensure_tile(input_impl->get_ttnn_tensor());
    auto ttnn_weight = ensure_tile(weight_impl->get_ttnn_tensor());

    auto input_shape = input.sizes();
    auto weight_shape = weight.sizes();

    int64_t batch_size, seq_len, in_features, out_features;

    if (input.dim() == 3) {
        batch_size = input_shape[0];
        seq_len = input_shape[1];
        in_features = input_shape[2];
    } else if (input.dim() == 2) {
        batch_size = input_shape[0];
        seq_len = 1;
        in_features = input_shape[1];
    } else {
        TORCH_CHECK(false, "ttnn_linear: Unsupported input dimensions: ", input.dim());
    }

    out_features = weight_shape[0];

    tt::stl::SmallVector<int32_t> reshaped_input_shape = {(int32_t)(batch_size * seq_len), (int32_t)in_features};

    ttnn::Tensor ttnn_reshaped_input;
    if (input.dim() == 2 && batch_size * seq_len == ttnn_input.logical_shape()[0] &&
        in_features == ttnn_input.logical_shape()[1]) {
        ttnn_reshaped_input = ttnn_input;
    } else {
        ttnn_reshaped_input = ttnn::reshape(ttnn_input, reshaped_input_shape);
    }

    auto ttnn_weight_t = ttnn::transpose(ttnn_weight, -2, -1);

    auto ttnn_result = ttnn::matmul(ttnn_reshaped_input, ttnn_weight_t);

    if (bias.has_value()) {
        TORCH_CHECK(bias.value().device().type() == c10::DeviceType::PrivateUse1);
        auto* bias_impl = static_cast<at::TtnnTensorImpl*>(bias.value().unsafeGetTensorImpl());
        auto ttnn_bias = ensure_tile(bias_impl->get_ttnn_tensor());
        ttnn_result = ttnn::add(ttnn_result, ttnn_bias);
    }

    ttnn::Tensor ttnn_final;
    if (input.dim() == 3) {
        tt::stl::SmallVector<int32_t> final_shape = {(int32_t)batch_size, (int32_t)seq_len, (int32_t)out_features};
        ttnn_final = ttnn::reshape(ttnn_result, final_shape);
    } else if (input.dim() == 2) {
        ttnn_final = ttnn_result;
    }

    std::vector<int64_t> output_shape;
    if (input.dim() == 3) {
        output_shape = {batch_size, seq_len, out_features};
    } else if (input.dim() == 2) {
        output_shape = {batch_size, out_features};
    }

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        output_shape, input.scalar_type(), c10::nullopt, input.device(), c10::nullopt);
    auto* output_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    output_impl->set_ttnn_tensor(ttnn_final);

    return output;
}
}  // namespace tt_eager::ops::linear

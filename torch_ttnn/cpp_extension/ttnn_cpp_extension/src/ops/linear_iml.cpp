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

at::Tensor ttnn_view_infer(const at::Tensor& self, at::IntArrayRef shape) {
    std::ostringstream oss;
    oss << "[TTNN] aten::view/reshape called with sizes:";
    for (auto d : shape) {
        oss << " " << d;
    }
    LOGGING(oss.str());

    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1, "ttnn_view_infer requires TTNN backend");

    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = ensure_tile(self_impl->get_ttnn_tensor());

    int64_t old_numel = self.numel();

    auto ttnn_shape = ttnn_tensor.logical_shape();
    std::cout << "[DEBUG] ttnn_view_infer: PyTorch tensor numel=" << old_numel;
    std::cout << ", TTNN tensor shape=[";
    for (int i = 0; i < ttnn_shape.rank(); i++) {
        std::cout << ttnn_shape[i];
        if (i < ttnn_shape.rank() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "]" << std::endl;

    if (old_numel == 0) {
        std::cout << "[DEBUG] PyTorch tensor numel() returned 0, calculating from shape" << std::endl;
        old_numel = 1;
        for (int i = 0; i < self.dim(); i++) {
            old_numel *= self.size(i);
        }
        std::cout << "[DEBUG] Calculated numel from PyTorch shape=" << old_numel << std::endl;
    }

    int unknown = -1;
    int64_t known_prod = 1;
    std::vector<int64_t> dims(shape.begin(), shape.end());
    for (int i = 0; i < (int)dims.size(); ++i) {
        int64_t d = dims[i];
        if (d == -1) {
            TORCH_CHECK(unknown < 0, "only one -1 allowed in view/reshape");
            unknown = i;
        } else {
            TORCH_CHECK(d >= 0, "view/reshape dims must be >=0 or -1");
            known_prod *= d;
        }
    }
    if (unknown >= 0) {
        TORCH_CHECK(known_prod != 0 && old_numel % known_prod == 0, "cannot infer dimension size for view/reshape");
        dims[unknown] = old_numel / known_prod;
    }

    int64_t new_numel = 1;
    for (auto d : dims) {
        new_numel *= d;
    }
    TORCH_CHECK(
        new_numel == old_numel,
        "View/reshape size is incompatible with input tensor size: ",
        "old = ",
        old_numel,
        ", new = ",
        new_numel);

    std::cout << "[DEBUG] ttnn_view_infer: old_numel=" << old_numel << ", new_numel=" << new_numel << std::endl;
    std::cout << "[DEBUG] ttnn_view_infer: original shape = [";
    for (int i = 0; i < self.dim(); i++) {
        std::cout << self.size(i);
        if (i < self.dim() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "], new shape = [";
    for (int i = 0; i < dims.size(); i++) {
        std::cout << dims[i];
        if (i < dims.size() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "]" << std::endl;

    tt::stl::SmallVector<int32_t> shape_i32(dims.begin(), dims.end());
    auto reshaped = ttnn::reshape(ttnn_tensor, shape_i32);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        dims, self.scalar_type(), c10::nullopt, self.device(), c10::nullopt);
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_ttnn_tensor(reshaped);
    return output;
}

at::Tensor ttnn_linear(const at::Tensor& input, const at::Tensor& weight, const c10::optional<at::Tensor>& bias) {
    LOGGING("Running aten::linear");
    TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(weight.device().type() == c10::DeviceType::PrivateUse1);

    std::cout << "[DEBUG] ttnn_linear: input.shape = [";
    for (int i = 0; i < input.dim(); i++) {
        std::cout << input.size(i);
        if (i < input.dim() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "], weight.shape = [";
    for (int i = 0; i < weight.dim(); i++) {
        std::cout << weight.size(i);
        if (i < weight.dim() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "], input.numel()=" << input.numel() << std::endl;

    if (input.dim() == 0 || input.size(0) == 0) {
        std::cout << "[ERROR] Input tensor has invalid dimensions!" << std::endl;
        throw std::runtime_error("Input tensor has invalid dimensions");
    }

    auto* input_impl = static_cast<at::TtnnTensorImpl*>(input.unsafeGetTensorImpl());
    auto* weight_impl = static_cast<at::TtnnTensorImpl*>(weight.unsafeGetTensorImpl());

    auto ttnn_input = ensure_tile(input_impl->get_ttnn_tensor());
    auto ttnn_weight = ensure_tile(weight_impl->get_ttnn_tensor());

    auto ttnn_input_shape = ttnn_input.logical_shape();
    auto ttnn_weight_shape = ttnn_weight.logical_shape();
    std::cout << "[DEBUG] ttnn_input.shape = [";
    for (int i = 0; i < ttnn_input_shape.rank(); i++) {
        std::cout << ttnn_input_shape[i];
        if (i < ttnn_input_shape.rank() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "], ttnn_weight.shape = [";
    for (int i = 0; i < ttnn_weight_shape.rank(); i++) {
        std::cout << ttnn_weight_shape[i];
        if (i < ttnn_weight_shape.rank() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "]" << std::endl;

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

    std::cout << "[DEBUG] Calculated dims: batch=" << batch_size << ", seq=" << seq_len << ", in_feat=" << in_features
              << ", out_feat=" << out_features << std::endl;

    tt::stl::SmallVector<int32_t> reshaped_input_shape = {(int32_t)(batch_size * seq_len), (int32_t)in_features};

    ttnn::Tensor ttnn_reshaped_input;
    if (input.dim() == 2 && batch_size * seq_len == ttnn_input.logical_shape()[0] &&
        in_features == ttnn_input.logical_shape()[1]) {
        ttnn_reshaped_input = ttnn_input;
        std::cout << "[DEBUG] Using input tensor as-is (already correct shape)" << std::endl;
    } else {
        ttnn_reshaped_input = ttnn::reshape(ttnn_input, reshaped_input_shape);
        std::cout << "[DEBUG] Reshaped input tensor" << std::endl;
    }

    std::cout << "[DEBUG] After reshape: ttnn_reshaped_input.shape = [";
    auto reshaped_shape = ttnn_reshaped_input.logical_shape();
    for (int i = 0; i < reshaped_shape.rank(); i++) {
        std::cout << reshaped_shape[i];
        if (i < reshaped_shape.rank() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "]" << std::endl;

    auto ttnn_weight_t = ttnn::transpose(ttnn_weight, -2, -1);

    std::cout << "[DEBUG] After transpose: ttnn_weight_t.shape = [";
    auto weight_t_shape = ttnn_weight_t.logical_shape();
    for (int i = 0; i < weight_t_shape.rank(); i++) {
        std::cout << weight_t_shape[i];
        if (i < weight_t_shape.rank() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "]" << std::endl;

    auto ttnn_result = ttnn::matmul(ttnn_reshaped_input, ttnn_weight_t);

    std::cout << "[DEBUG] After matmul: ttnn_result.shape = [";
    auto result_shape = ttnn_result.logical_shape();
    for (int i = 0; i < result_shape.rank(); i++) {
        std::cout << result_shape[i];
        if (i < result_shape.rank() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "]" << std::endl;

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

    std::cout << "[DEBUG] After final reshape: ttnn_final.shape = [";
    auto final_ttnn_shape = ttnn_final.logical_shape();
    for (int i = 0; i < final_ttnn_shape.rank(); i++) {
        std::cout << final_ttnn_shape[i];
        if (i < final_ttnn_shape.rank() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "]" << std::endl;

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

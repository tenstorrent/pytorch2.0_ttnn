#include "ttnn_cpp_extension/ops/embedding.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"

#include <ttnn/operations/gather/gather.hpp>



namespace tt_eager::ops::embedding {

at::Tensor ttnn_embedding(
    const at::Tensor& weight,
    const at::Tensor& indices,
    int64_t padding_idx,
    bool scale_grad_by_freq,
    bool sparse) {

    LOGGING("Running aten::embedding.default");

    // Device/type checks
    TORCH_CHECK(weight.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(indices.device().type() == c10::DeviceType::PrivateUse1);

    // Warn for unsupported options
    TORCH_CHECK(!scale_grad_by_freq, "scale_grad_by_freq is not supported on TTNN backend");
    TORCH_CHECK(!sparse, "sparse embedding is not supported on TTNN backend");

    auto* weight_impl = static_cast<at::TtnnTensorImpl*>(weight.unsafeGetTensorImpl());
    auto* indices_impl = static_cast<at::TtnnTensorImpl*>(indices.unsafeGetTensorImpl());

    auto ttnn_weight = weight_impl->get_ttnn_tensor();
    auto ttnn_indices = indices_impl->get_ttnn_tensor();

    // Ensure TILE layout
    if (ttnn_weight.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_weight = ttnn::to_layout(ttnn_weight, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_weight.device());
    }

    // Gather along dimension 0
    auto ttnn_result = ttnn::gather(ttnn_weight, ttnn_indices, /*dim=*/0, padding_idx);

    // Create output tensor
    auto output = tt_eager::ops::create::custom_empty_memory_format(
        ttnn_result.shape().to_sizes(),
        c10::optional<at::ScalarType>(weight.scalar_type()),
        c10::nullopt,
        c10::optional<at::Device>(weight.device()),
        c10::nullopt
    );

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_ttnn_tensor(ttnn_result);

    return output;
}

}  // namespace tt_eager::ops::embedding

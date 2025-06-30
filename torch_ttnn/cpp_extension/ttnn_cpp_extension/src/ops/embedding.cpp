#include "ttnn_cpp_extension/ops/embedding.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"

#include <ttnn/operations/embedding/embedding.hpp>

namespace tt_eager::ops::embedding {

at::Tensor ttnn_embedding(
    const at::Tensor& weight,
    const at::Tensor& indices,
    int64_t padding_idx,
    bool scale_grad_by_freq,
    bool sparse) {

    LOGGING("Running aten::embedding.default");

    TORCH_CHECK(weight.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(indices.device().type() == c10::DeviceType::PrivateUse1);

    TORCH_CHECK(!scale_grad_by_freq, "scale_grad_by_freq is not supported on TTNN backend");
    TORCH_CHECK(!sparse, "sparse embedding is not supported on TTNN backend");

    auto* weight_impl = static_cast<at::TtnnTensorImpl*>(weight.unsafeGetTensorImpl());
    auto* indices_impl = static_cast<at::TtnnTensorImpl*>(indices.unsafeGetTensorImpl());

    auto ttnn_weight = weight_impl->get_ttnn_tensor();
    auto ttnn_indices = indices_impl->get_ttnn_tensor();

    auto ttnn_result = ttnn::operations::embedding::EmbeddingOperation::invoke(
        ttnn_indices,
        ttnn_weight,
        /*pad_token=*/(padding_idx >= 0 ? std::optional<int>(padding_idx) : std::nullopt),
        /*layout=*/std::optional<ttnn::Layout>(ttnn_weight.layout()),
        /*embeddings_type=*/ttnn::operations::embedding::EmbeddingsType::GENERIC,
        /*dtype=*/std::nullopt,
        /*memory_config=*/std::nullopt,
        /*optional_output_tensor=*/std::nullopt
    );

    std::vector<int64_t> shape(
        ttnn_result.logical_shape().cbegin(),
        ttnn_result.logical_shape().cend()
    );

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        c10::IntArrayRef(shape),
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

#include <ttnn/operations/normalization/softmax/softmax.hpp>

#include "ttnn_cpp_extension/ops/softmax.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"

namespace tt_eager::ops::normalization {

at::Tensor ttnn_softmax(const at::Tensor& input, int64_t dim, bool /*half_to_float*/) {
    LOGGING("");
    TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1);

    auto* tensor_impl = static_cast<at::TtnnTensorImpl*>(input.unsafeGetTensorImpl());
    auto ttnn_tensor = tensor_impl->get_ttnn_tensor();
    if (ttnn_tensor.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_tensor = ttnn::to_layout(
            ttnn_tensor,
            ttnn::TILE_LAYOUT,
            std::nullopt,
            std::nullopt,
            ttnn_tensor.device());
    }

    auto result = ttnn::softmax(ttnn_tensor, dim);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        input.sizes(),
        c10::optional<at::ScalarType>(input.scalar_type()),
        c10::nullopt,
        c10::optional<at::Device>(input.device()),
        c10::nullopt);

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_ttnn_tensor(result);

    return output;
}

} // namespace tt_eager::ops::normalization

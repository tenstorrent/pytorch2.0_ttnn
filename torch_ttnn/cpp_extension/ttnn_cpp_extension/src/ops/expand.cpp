#include "ttnn_cpp_extension/ops/expand.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"

#include <ttnn/operations/data_movement/expand/expand.hpp>

namespace tt_eager::ops::expand {

at::Tensor ttnn_expand(const at::Tensor& self, at::IntArrayRef size, bool implicit) {
    LOGGING("Running aten::expand.default");

    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);

    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = self_impl->get_ttnn_tensor();

    if (ttnn_tensor.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_tensor = ttnn::to_layout(ttnn_tensor, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_tensor.device());
    }

    std::vector<int32_t> target_shape_vec;
    target_shape_vec.reserve(size.size());
    for (auto s : size) {
        target_shape_vec.push_back(static_cast<int32_t>(s));
    }

    tt::stl::Span<const int32_t> shape_span(target_shape_vec);

    auto expanded_tensor = ttnn::expand(ttnn_tensor, shape_span, std::nullopt, );

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        size, self.scalar_type(), c10::nullopt, self.device(), c10::nullopt);

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_ttnn_tensor(expanded_tensor);

    return output;
}

}  // namespace tt_eager::ops::expand

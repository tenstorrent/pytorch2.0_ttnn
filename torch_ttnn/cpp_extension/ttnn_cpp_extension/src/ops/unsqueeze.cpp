
#include "ttnn_cpp_extension/ops/unsqueeze.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include <ttnn/operations/data_movement/unsqueeze/unsqueeze.hpp>
#include "ttnn_cpp_extension/utils/extension_utils.hpp"
#include "ttnn_cpp_extension/utils/layout_utils.hpp"


namespace tt_eager::ops::unsqueeze {

at::Tensor ttnn_unsqueeze(const at::Tensor& self, int64_t dim) {
    LOGGING("Running aten::unsqueeze.default");
    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);
    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = tt_eager::utils::ensure_tile_layout(self_impl->get_ttnn_tensor());
    int rank = static_cast<int>(self.dim());
    TORCH_CHECK(dim >= -rank - 1 && dim <= rank, "Invalid dimension for unsqueeze");
    if (dim < 0) {
        dim += rank + 1;
    }
    auto ttnn_result = ttnn::unsqueeze(ttnn_tensor, dim);
    const auto& logical_shape = ttnn_result.logical_shape();
    std::vector<int64_t> shape_vec(logical_shape.cbegin(), logical_shape.cend());
    auto output = tt_eager::ops::create::custom_empty_memory_format(
        shape_vec, self.scalar_type(), c10::nullopt, self.device(), c10::nullopt);
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_ttnn_tensor(ttnn_result);
    return output;
}

}  // namespace tt_eager::ops::unsqueeze

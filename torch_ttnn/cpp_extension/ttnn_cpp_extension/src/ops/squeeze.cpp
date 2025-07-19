#include "ttnn_cpp_extension/ops/squeeze.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"
#include <ttnn/operations/data_movement/squeeze/squeeze.hpp>
#include "ttnn_cpp_extension/utils/layout_utils.hpp"

namespace tt_eager::ops::squeeze {

at::Tensor ttnn_squeeze_dim(const at::Tensor& self, int64_t dim) {
    LOGGING("Running aten::squeeze.dim");
    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);
    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = tt_eager::utils::ensure_tile_layout(self_impl->get_ttnn_tensor());
    int rank = static_cast<int>(self.dim());
    TORCH_CHECK(dim >= -rank && dim < rank, "Invalid dimension for squeeze");
    if (dim < 0) {
        dim += rank;
    }
    TORCH_CHECK(self.size(dim) == 1, "Cannot squeeze dimension that is not of size 1");
    auto ttnn_result = ttnn::squeeze(ttnn_tensor, static_cast<int>(dim));
    const auto& logical_shape = ttnn_result.logical_shape();
    std::vector<int64_t> shape_vec(logical_shape.cbegin(), logical_shape.cend());
    auto output = tt_eager::ops::create::custom_empty_memory_format(
        shape_vec, self.scalar_type(), c10::nullopt, self.device(), c10::nullopt);
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_ttnn_tensor(ttnn_result);
    return output;
}

}  // namespace tt_eager::ops::squeeze

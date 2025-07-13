#include "ttnn_cpp_extension/ops/matmul.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"

#include <vector>
#include <iostream>

#include <ttnn/operations/matmul/matmul.hpp>

namespace tt_eager::ops::matmul {

static ttnn::Tensor ensure_tile(ttnn::Tensor t) {
    if (t.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        t = ttnn::to_layout(t, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, t.device());
    }
    return t;
}

at::Tensor ttnn_matmul(const at::Tensor& self, const at::Tensor& other) {
    TORCH_CHECK(
        self.device().type() == c10::DeviceType::PrivateUse1, "ttnn_matmul requires TTNN backend for self tensor");
    TORCH_CHECK(
        other.device().type() == c10::DeviceType::PrivateUse1, "ttnn_matmul requires TTNN backend for other tensor");

    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto* other_impl = static_cast<at::TtnnTensorImpl*>(other.unsafeGetTensorImpl());

    auto ttnn_self = ensure_tile(self_impl->get_ttnn_tensor());
    auto ttnn_other = ensure_tile(other_impl->get_ttnn_tensor());

    auto ttnn_self_shape = ttnn_self.logical_shape();
    auto ttnn_other_shape = ttnn_other.logical_shape();

    auto ttnn_result = ttnn::matmul(ttnn_self, ttnn_other);

    auto ttnn_result_shape = ttnn_result.logical_shape();

    std::vector<int64_t> output_shape;
    auto self_shape = self.sizes();
    auto other_shape = other.sizes();

    if (self.dim() > 2 && other.dim() > 2) {
        int64_t batch_dims = std::max(self.dim(), other.dim()) - 2;
        for (int i = 0; i < batch_dims; i++) {
            int64_t self_dim = (i < self.dim() - 2) ? self_shape[i] : 1;
            int64_t other_dim = (i < other.dim() - 2) ? other_shape[i] : 1;
            output_shape.push_back(std::max(self_dim, other_dim));
        }
    }

    output_shape.push_back(self_shape[self.dim() - 2]);
    output_shape.push_back(other_shape[other.dim() - 1]);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        output_shape, self.scalar_type(), c10::nullopt, self.device(), c10::nullopt);
    auto* output_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    output_impl->set_ttnn_tensor(ttnn_result);

    return output;
}
}  // namespace tt_eager::ops::matmul

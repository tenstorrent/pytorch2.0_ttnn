#include "ttnn_cpp_extension/ops/matmul.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"
#include "ttnn_cpp_extension/utils/layout_utils.hpp"

#include <vector>
#include <iostream>

#include <ttnn/operations/matmul/matmul.hpp>
#include <ttnn/operations/eltwise/binary/binary.hpp>

namespace tt_eager::ops::matmul {

at::Tensor ttnn_matmul(const at::Tensor& self, const at::Tensor& other) {
    TORCH_CHECK(
        self.device().type() == c10::DeviceType::PrivateUse1, "ttnn_matmul requires TTNN backend for self tensor");
    TORCH_CHECK(
        other.device().type() == c10::DeviceType::PrivateUse1, "ttnn_matmul requires TTNN backend for other tensor");

    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto* other_impl = static_cast<at::TtnnTensorImpl*>(other.unsafeGetTensorImpl());

    auto ttnn_self = tt_eager::utils::ensure_tile_layout(self_impl->get_ttnn_tensor());
    auto ttnn_other = tt_eager::utils::ensure_tile_layout(other_impl->get_ttnn_tensor());

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

at::Tensor ttnn_addmm(
    const at::Tensor& self,
    const at::Tensor& mat1,
    const at::Tensor& mat2,
    const at::Scalar& beta,
    const at::Scalar& alpha) {
    LOGGING("Running aten::addmm");
    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(mat1.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(mat2.device().type() == c10::DeviceType::PrivateUse1);

    auto* impl_self = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto* impl1 = static_cast<at::TtnnTensorImpl*>(mat1.unsafeGetTensorImpl());
    auto* impl2 = static_cast<at::TtnnTensorImpl*>(mat2.unsafeGetTensorImpl());
    ttnn::Tensor t_self = tt_eager::utils::ensure_tile_layout(impl_self->get_ttnn_tensor());
    ttnn::Tensor t1 = tt_eager::utils::ensure_tile_layout(impl1->get_ttnn_tensor());
    ttnn::Tensor t2 = tt_eager::utils::ensure_tile_layout(impl2->get_ttnn_tensor());

    auto t_res = ttnn::matmul(t1, t2);

    if (alpha.toDouble() != 1.0) {
        t_res = ttnn::multiply(t_res, static_cast<float>(alpha.toDouble()));
    }

    if (beta.toDouble() != 1.0) {
        t_self = ttnn::multiply(t_self, static_cast<float>(beta.toDouble()));
    }

    auto result = ttnn::add(t_self, t_res);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        self.sizes(),
        self.scalar_type(),
        /*strides=*/c10::nullopt,
        /*device=*/self.device(),
        /*pin_memory=*/c10::nullopt);
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(self);
    out_impl->set_ttnn_tensor(result);
    return output;
}

at::Tensor ttnn_bmm(const at::Tensor& batch1, const at::Tensor& batch2) {
    LOGGING("Running aten::bmm");
    LOGGING("Batch1 device type: ", static_cast<int>(batch1.device().type()));
    LOGGING("Batch2 device type: ", static_cast<int>(batch2.device().type()));

    TORCH_CHECK(batch1.device().type() == c10::DeviceType::PrivateUse1);

    if (batch2.device().type() != c10::DeviceType::PrivateUse1) {
        LOGGING("Batch2 tensor not on TTNN device, using _to_copy to transfer");
        auto batch2_ttnn = batch2.to(batch1.device(), /*non_blocking=*/false);
        return ttnn_bmm(batch1, batch2_ttnn);
    }

    auto* batch1_impl = static_cast<at::TtnnTensorImpl*>(batch1.unsafeGetTensorImpl());
    auto* batch2_impl = static_cast<at::TtnnTensorImpl*>(batch2.unsafeGetTensorImpl());

    auto ttnn_batch1 = tt_eager::utils::ensure_tile_layout(batch1_impl->get_ttnn_tensor());
    auto ttnn_batch2 = tt_eager::utils::ensure_tile_layout(batch2_impl->get_ttnn_tensor());

    auto result = ttnn::matmul(ttnn_batch1, ttnn_batch2);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        batch1.sizes(),
        batch1.scalar_type(),
        /*strides=*/c10::nullopt,
        /*device=*/batch1.device(),
        /*pin_memory=*/c10::nullopt);
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(batch1);
    out_impl->set_ttnn_tensor(result);
    return output;
}

}  // namespace tt_eager::ops::matmul

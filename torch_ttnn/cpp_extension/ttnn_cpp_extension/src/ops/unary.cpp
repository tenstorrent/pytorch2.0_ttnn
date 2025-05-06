#include <ttnn/operations/eltwise/unary/unary.hpp>

#include "ttnn_cpp_extension/ops/unary.hpp"

#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"

#include "ttnn_cpp_extension/utils/extension_utils.hpp"

namespace tt_eager::ops::unary {
at::Tensor& ttnn_abs_out(const at::Tensor& self, at::Tensor& out) {
    LOGGING("");
    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(out.device().type() == c10::DeviceType::PrivateUse1);

    // Get underlying TTNN tensor object from input
    at::TtnnTensorImpl* tensor_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = tensor_impl->get_ttnn_tensor();

    // Call TTNN operation
    auto result = ttnn::abs(ttnn_tensor);

    // Get underlying TTNN tensor object from output
    at::TtnnTensorImpl* out_tensor_impl = static_cast<at::TtnnTensorImpl*>(out.unsafeGetTensorImpl());
    out_tensor_impl->set_sizes_and_strides_as(self);

    // Set output TTNN tensor to result
    auto out_ttnn_tensor = out_tensor_impl->get_ttnn_tensor();
    out_tensor_impl->set_ttnn_tensor(result);

    return out;
}

}  // namespace tt_eager::ops::unary

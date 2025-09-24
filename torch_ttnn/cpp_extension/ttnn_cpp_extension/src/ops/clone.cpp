#include <cstddef>
#include "ttnn_cpp_extension/ops/clone.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"

#include <ttnn/operations/data_movement/clone/clone.hpp>

namespace tt_eager::ops::clone {

at::Tensor ttnn_clone(const at::Tensor& self, c10::optional<at::MemoryFormat> memory_format_opt) {
    LOGGING("Running aten::clone.default");
    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);

    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = self_impl->get_ttnn_tensor();

    auto cloned = ttnn::clone(
        ttnn_tensor, /*dtype=*/std::nullopt, /*memory_config=*/std::nullopt, /*compute_kernel_config=*/std::nullopt);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        self.sizes(),
        self.scalar_type(),
        /*strides=*/c10::nullopt,
        /*device=*/self.device(),
        /*pin_memory=*/c10::nullopt,
        memory_format_opt);
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(self);
    out_impl->set_ttnn_tensor(cloned);

    return output;
}

}  // namespace tt_eager::ops::clone

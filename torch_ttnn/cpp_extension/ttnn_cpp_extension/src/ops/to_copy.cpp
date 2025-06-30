#include "ttnn_cpp_extension/core/copy.hpp"
#include <ttnn/operations/copy.hpp>
#include <torch/extension.h>

namespace ttnn_extension {

at::Tensor ttnn_to_copy(const at::Tensor& self, c10::optional<at::Device> device_opt, bool non_blocking, c10::optional<at::ScalarType> dtype_opt) {
    TORCH_CHECK(device_opt.has_value(), "Device must be specified for to_copy.");
    auto device = device_opt.value();
    auto dtype = dtype_opt.value_or(self.scalar_type());
    auto options = self.options().dtype(dtype).device(device);
    auto out = at::empty_like(self, options, c10::nullopt);
    ttnn_copy_from(out, self, non_blocking);
    return out;
}

} // namespace ttnn_extension

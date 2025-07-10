#include <ttnn/operations/copy.hpp>
#include <torch/extension.h>

#include "ttnn_cpp_extension/ops/to_copy.hpp"
#include "ttnn_cpp_extension/core/copy.hpp"

namespace tt_eager::ops::to_copy {

at::Tensor ttnn_to_copy(
    const at::Tensor& self,
    c10::optional<at::ScalarType> dtype,
    c10::optional<at::Layout> layout,
    c10::optional<at::Device> device,
    c10::optional<bool> pin_memory,
    bool non_blocking,
    c10::optional<at::MemoryFormat> memory_format
) {
    // These checks match PyTorch's constraints and TTNN backend limitations
    TORCH_CHECK(!layout.has_value() || layout.value() == self.layout(),
                "ttnn_to_copy: layout conversion is not supported");
    TORCH_CHECK(!pin_memory.has_value() || !pin_memory.value(),
                "ttnn_to_copy: pin_memory=True is not supported on TTNN backend");

    // PyTorch always calls this with copy=True, we hardcode that logic here
    const bool copy = true;
    TORCH_CHECK(copy, "ttnn_to_copy: copy must be true");

    TORCH_CHECK(device.has_value(), "ttnn_to_copy: device must be specified");

    // Resolve dtype and device
    auto target_dtype = dtype.value_or(self.scalar_type());
    auto target_device = device.value();

    // Create empty output tensor with new dtype/device
    auto options = self.options().dtype(target_dtype).device(target_device);
    auto out = at::empty_like(self, options, memory_format);

    // Perform the actual copy
    ttnn_copy_from(out, self, non_blocking);
    return out;
}

} // namespace tt_eager::ops::to_copy

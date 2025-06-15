// ttnn_cpp_extension/ops/to_copy.cpp

#include "ttnn_cpp_extension/ops/to_copy.hpp"

#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"

#include <ttnn/operations/creation.hpp>
#include <ttnn/operations/transform/convert.hpp>

namespace tt_eager::ops::to_copy {

at::Tensor ttnn_to_copy(
    const at::Tensor& self,
    c10::optional<at::ScalarType> dtype,
    c10::optional<at::Layout> layout,
    c10::optional<at::Device> device,
    c10::optional<bool> pin_memory,
    bool non_blocking,
    bool copy,
    c10::optional<at::MemoryFormat> memory_format) {

    LOGGING("ttnn_to_copy called with device: {}", device.has_value() ? device->str() : "None");

    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1,
        "ttnn_to_copy: only supports TTNN input tensor");

    // Get TTNN tensor from input
    at::TtnnTensorImpl* tensor_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto input_tensor = tensor_impl->get_ttnn_tensor();

    auto new_device = device.value_or(self.device());
    TORCH_CHECK(new_device.type() == c10::DeviceType::PrivateUse1,
        "ttnn_to_copy: destination device must be TTNN");

    at::ScalarType dtype_value = dtype.value_or(self.scalar_type());
    auto ttnn_dtype = dtype_torch_to_ttnn(dtype_value);

    // If dtype is different, convert tensor
    if (ttnn_dtype != input_tensor.dtype()) {
        input_tensor = ttnn::transform::convert(input_tensor, ttnn_dtype);
    }

    // If device index is different, move tensor
    if (new_device.index() != self.device().index()) {
        TtnnGuard guard(new_device);
        ttnn::MeshDevice* ttnn_device = guard.get_open_ttnn_device(new_device.index());
        input_tensor = ttnn::to_device(input_tensor, ttnn_device);
    }

    // Create new torch::Tensor wrapper with same size, dtype, device
    auto output = tt_eager::ops::create::custom_empty_memory_format(
        self.sizes(), dtype_value, layout, new_device, pin_memory, memory_format);

    at::TtnnTensorImpl* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_ttnn_tensor(input_tensor);
    out_impl->set_sizes_and_strides_as(self);

    return output;
}

}  // namespace tt_eager::ops::to_copy

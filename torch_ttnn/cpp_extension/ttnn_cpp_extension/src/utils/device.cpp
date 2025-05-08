
#include <tt-metalium/assert.hpp>
#include <c10/core/Device.h>

#include "ttnn_cpp_extension/core/TtnnGuard.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"

#include "ttnn_cpp_extension/utils/device.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"

// This function can be used when the TTNN device is initialized separately,
// for example, `device = ttnn.open_device(device_index = 0)`. Pass that
// device object to this function so that the cpp extension can use it.
c10::Device as_torch_device(ttnn::MeshDevice* ttnn_device) {
    LOGGING("");
    // TODO: Lacks a proper mesh support. We need to have mapping (shape, offset) -> index.
    // It's quiet difficult to do since c10::DeviceIndex is int8
    auto index = ttnn_device->get_device(0, 0)->id();
    auto device = c10::Device(c10::DeviceType::PrivateUse1, static_cast<c10::DeviceIndex>(index));
    if (TtnnGuard::ttnn_device == nullptr) {
        TtnnGuard::ttnn_device = ttnn_device;
    }
    return device;
}

// Manually closes the torch and ttnn device
void close_torch_device(c10::Device device) {
    LOGGING("");
    TtnnGuard device_guard(device);
    ttnn::MeshDevice* ttnn_device = device_guard.get_open_ttnn_device();
    TORCH_INTERNAL_ASSERT(ttnn_device != nullptr);
    ttnn::close_device(*ttnn_device);
    ttnn_device = nullptr;
}

// TODO: Lacks proper mesh support
c10::Device open_torch_device(at::DeviceIndex device_index) {
    auto device = c10::Device(c10::DeviceType::PrivateUse1, device_index);
    TtnnGuard device_guard(device);
    ttnn::MeshDevice* ttnn_device = device_guard.get_open_ttnn_device(device_index);
    TT_FATAL(ttnn_device != nullptr, "Failed to open TTNN device");
    return device;
}

// Get the underlying TTNN tensor from a Torch tensor
ttnn::Tensor get_ttnn_tensor(at::Tensor& tensor) {
    LOGGING("");
    at::TtnnTensorImpl* tensor_impl = static_cast<at::TtnnTensorImpl*>(tensor.unsafeGetTensorImpl());
    auto ttnn_tensor = tensor_impl->get_ttnn_tensor();
    return ttnn_tensor;
}

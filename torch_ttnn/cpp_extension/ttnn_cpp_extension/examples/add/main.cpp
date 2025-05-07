#include <iostream>

#include <torch/torch.h>
#include <c10/core/ScalarType.h>

#include "tt-metalium/dispatch_core_common.hpp"
#include <ttnn/device.hpp>

#include <ttnn_cpp_extension/utils/device.hpp>

int main() {
    auto ttnn_device = ttnn::open_mesh_device(
        0, 16384, DEFAULT_TRACE_REGION_SIZE, tt::tt_metal::DispatchCoreConfig(tt::tt_metal::DispatchCoreType::ETH));
    auto device = as_torch_device(ttnn_device.get());

    // Use the correct device type syntax - lowercase and with index
    // auto device = c10::Device(c10::DeviceType::PrivateUse1, 0);
    at::TensorOptions options;
    options = options.dtype(at::kBFloat16).requires_grad(false);
    auto a = torch::randn({3, 3}, options);
    std::cout << "a: \n" << a << std::endl;
    auto b = torch::ones_like(a, options);
    std::cout << "b: \n" << b << std::endl;

    a = a.to(device);
    b = b.to(device);

    auto c = torch::add(a, b);  // dispatched to our kernel
    c = c.to("cpu");
    std::cout << "c: \n" << c << std::endl;
}

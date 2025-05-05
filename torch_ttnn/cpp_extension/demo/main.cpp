#include <torch/torch.h>
// #include <torch/library.h>
#include <iostream>
#include "tt-metalium/dispatch_core_common.hpp"
#include "utils/device.hpp"  // Include the header that contains your device utilities
#include <ttnn/device.hpp>

int main() {
    auto ttnn_device = ttnn::open_mesh_device(
        0, 16384, DEFAULT_TRACE_REGION_SIZE, tt::tt_metal::DispatchCoreConfig(tt::tt_metal::DispatchCoreType::ETH));
    auto device = as_torch_device(ttnn_device.get());

    // Use the correct device type syntax - lowercase and with index
    // auto device = c10::Device(c10::DeviceType::PrivateUse1, 0);
    auto a = torch::randn({3, 3});
    auto b = torch::ones_like(a);

    a.to(device);
    b.to(device);

    auto c = torch::add(a, b, /*alpha=*/1);  // dispatched to our kernel
    c.to("cpu");
    std::cout << c << std::endl;
}

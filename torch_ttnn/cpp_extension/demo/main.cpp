#include <torch/torch.h>
// #include <torch/library.h>
#include <iostream>
#include "utils/device.hpp"  // Include the header that contains your device utilities
#include <ttnn/device.hpp>

int main() {
    // Force the backend library to be loaded at run time as well,
    // so that you can test without linking (-l) if you want.
    // (Not necessary once the linker flag is in place)
    //   torch::library::load_library("libttnn_cpp_extension.so");

    auto* ttnn_device = ttnn::open_mesh_device(0).get();
    auto device = as_torch_device(ttnn_device);  // This should initialize the device if not already done

    // Use the correct device type syntax - lowercase and with index
    // auto device = c10::Device(c10::DeviceType::PrivateUse1, 0);
    auto a = torch::randn({3, 3});
    auto b = torch::ones_like(a);

    a.to(device);
    b.to(device);

    auto c = torch::add(a, b, /*alpha=*/1);  // dispatched to our kernel
    c.to("cpu");
    std::cout << c << std::endl;
    // ttnn_device->close()
}

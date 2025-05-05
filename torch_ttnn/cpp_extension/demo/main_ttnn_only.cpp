#include <iostream>
#include <ttnn/device.hpp>

int main() {
    auto* ttnn_device = ttnn::open_mesh_device(0).get();
    std::cout << "ttnn_device: " << ttnn_device << std::endl;
    ttnn_device->close();
}

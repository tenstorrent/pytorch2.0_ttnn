#pragma once

#include <ATen/core/Tensor.h>
#include <c10/core/Device.h>

#include <ttnn/operations/core/core.hpp>

c10::Device as_torch_device(ttnn::MeshDevice* ttnn_device);

// Get the underlying TTNN tensor from a Torch tensor
ttnn::Tensor get_ttnn_tensor(at::Tensor& tensor);

c10::Device open_torch_device(at::DeviceIndex device_index);

// Manually closes the torch and ttnn device
void close_torch_device(c10::Device device);

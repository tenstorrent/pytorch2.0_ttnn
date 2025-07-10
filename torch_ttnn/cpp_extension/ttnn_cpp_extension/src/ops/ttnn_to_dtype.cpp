// torch_ttnn/cpp_extension/ttnn_to_dtype.cpp

#include "ttnn_cpp_extension/ops/ttnn_to_dtype.hpp"      // ваш hpp
#include <ATen/ATen.h>

using at::Tensor;

Tensor ttnn_to_dtype(
    const Tensor& self,
    at::ScalarType dtype,
    bool non_blocking,
    bool copy,
    c10::optional<c10::MemoryFormat> memory_format
) {
    // Ігноруємо memory_format — робимо все на CPU, як раніше
    Tensor cpu = self.to(at::kCPU);
    Tensor casted = cpu.to(dtype);
    return casted.to(self.device(), non_blocking);
}



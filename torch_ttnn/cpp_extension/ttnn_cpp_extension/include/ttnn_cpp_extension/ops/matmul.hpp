#pragma once

#include <ATen/Tensor.h>

namespace tt_eager::ops::matmul {
    at::Tensor ttnn_matmul(const at::Tensor& self, const at::Tensor& other);
}

#pragma once

#include <ATen/core/Tensor.h>

at::Tensor ttnn_copy_from(const at::Tensor& self, const at::Tensor& dst, bool non_blocking);

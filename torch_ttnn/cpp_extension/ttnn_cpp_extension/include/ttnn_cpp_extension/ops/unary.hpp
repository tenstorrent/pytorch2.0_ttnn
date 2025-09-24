#pragma once

#include <ATen/core/Tensor.h>

namespace tt_eager::ops::unary {
at::Tensor& ttnn_abs_out(const at::Tensor& input, at::Tensor& out);
at::Tensor ttnn_gelu(const at::Tensor& self, c10::string_view approximate);
at::Tensor ttnn_tanh(const at::Tensor& self);
}  // namespace tt_eager::ops::unary

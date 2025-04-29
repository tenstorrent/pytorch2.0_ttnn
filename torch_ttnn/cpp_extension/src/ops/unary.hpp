#pragma once

#include <ATen/core/Tensor.h>

namespace tt_eager::ops::unary {
at::Tensor& ttnn_abs_out(const at::Tensor& input, at::Tensor& out);
}
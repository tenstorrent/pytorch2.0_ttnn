#pragma once

#include <ATen/core/Tensor.h>
#include <ATen/core/Scalar.h>

namespace tt_eager::ops::binary {
at::Tensor& ttnn_add_out(const at::Tensor& input, const at::Tensor& other, const at::Scalar& alpha, at::Tensor& out);
at::Tensor ttnn_add_tensor(const at::Tensor& input, const at::Tensor& other, const at::Scalar& alpha);
}  // namespace tt_eager::ops::binary

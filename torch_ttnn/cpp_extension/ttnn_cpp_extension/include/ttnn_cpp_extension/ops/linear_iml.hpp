#pragma once

#include <ATen/Tensor.h>
#include <c10/util/Optional.h>

namespace tt_eager::ops::linear {

// at::Tensor ttnn_view_infer(const at::Tensor& self, at::IntArrayRef shape);

at::Tensor ttnn_linear(const at::Tensor& input, const at::Tensor& weight, const c10::optional<at::Tensor>& bias);

}  // namespace tt_eager::ops::linear

#pragma once

#include <ATen/ATen.h>

namespace tt_eager::ops::norm {

// Implementation of aten::native_layer_norm.default
std::tuple<at::Tensor, at::Tensor, at::Tensor> ttnn_native_layer_norm(
    const at::Tensor& input,
    at::IntArrayRef normalized_shape,
    const c10::optional<at::Tensor>& weight,
    const c10::optional<at::Tensor>& bias,
    double eps);

}

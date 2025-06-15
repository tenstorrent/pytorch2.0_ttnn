#pragma once

#include <ATen/core/Tensor.h>

namespace tt_eager::ops::normalization {

at::Tensor ttnn_softmax(const at::Tensor& input, int64_t dim, bool half_to_float);

} // namespace tt_eager::ops::normalization
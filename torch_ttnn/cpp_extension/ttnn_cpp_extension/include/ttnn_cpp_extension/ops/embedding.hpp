#pragma once

#include <ATen/ATen.h>

namespace tt_eager::ops::embedding {

at::Tensor ttnn_embedding(
    const at::Tensor& weight, const at::Tensor& indices, int64_t padding_idx, bool scale_grad_by_freq, bool sparse);

}  // namespace tt_eager::ops::embedding

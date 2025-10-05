#pragma once

#include <torch/torch.h>

namespace tt_eager::ops::permute {

at::Tensor ttnn_permute(const at::Tensor& input, at::IntArrayRef dims);

}  // namespace tt_eager::ops::permute

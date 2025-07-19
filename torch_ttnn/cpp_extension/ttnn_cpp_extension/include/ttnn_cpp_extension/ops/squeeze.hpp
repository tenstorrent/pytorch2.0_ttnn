#pragma once
#include <torch/torch.h>

namespace tt_eager::ops::squeeze {
at::Tensor ttnn_squeeze_dim(const at::Tensor& self, int64_t dim);
} // namespace tt_eager::ops::squeeze

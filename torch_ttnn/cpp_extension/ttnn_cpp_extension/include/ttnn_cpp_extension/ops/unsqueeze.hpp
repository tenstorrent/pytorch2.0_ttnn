#pragma once
#include <torch/torch.h>

namespace tt_eager::ops::unsqueeze {
at::Tensor ttnn_unsqueeze(const at::Tensor& self, int64_t dim);
} // namespace tt_eager::ops::unsqueeze

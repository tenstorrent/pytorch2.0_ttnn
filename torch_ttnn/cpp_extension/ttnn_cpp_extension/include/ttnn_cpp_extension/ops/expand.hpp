#pragma once

#include <torch/torch.h>

namespace tt_eager::ops::expand {

at::Tensor ttnn_expand(const at::Tensor& self, at::IntArrayRef size, bool implicit);

}  // namespace tt_eager::ops::expand
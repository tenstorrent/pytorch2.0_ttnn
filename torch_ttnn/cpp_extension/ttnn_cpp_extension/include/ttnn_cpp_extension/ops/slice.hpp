#pragma once

#include <torch/torch.h>
#include <c10/util/Optional.h>

namespace tt_eager::ops::slice {

at::Tensor ttnn_slice_tensor(
    const at::Tensor& input,
    int64_t dim,
    c10::optional<c10::SymInt> start,
    c10::optional<c10::SymInt> end,
    c10::SymInt step);

}  // namespace tt_eager::ops::slice

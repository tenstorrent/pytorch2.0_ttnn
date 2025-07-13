#pragma once

#include <ATen/Tensor.h>
#include <c10/util/Optional.h>

namespace tt_eager::ops::as_strided {
at::Tensor ttnn_as_strided(
    const at::Tensor& self,
    at::IntArrayRef size,
    at::IntArrayRef stride,
    c10::optional<int64_t> storage_offset = c10::nullopt);
}  // namespace tt_eager::ops::as_strided

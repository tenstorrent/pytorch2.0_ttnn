#pragma once

#include <ATen/Tensor.h>
#include <c10/core/MemoryFormat.h>

namespace tt_eager::ops::clone {

at::Tensor ttnn_clone(
    const at::Tensor& self,
    c10::optional<c10::MemoryFormat> memory_format_opt = c10::nullopt);

}  // namespace tt_eager::ops::clone

#pragma once

#include <ATen/core/Tensor.h>
#include <c10/core/MemoryFormat.h>
#include <c10/util/Optional.h>

namespace tt_eager::ops::clone {

at::Tensor ttnn_clone(const at::Tensor& self, c10::optional<at::MemoryFormat> memory_format_opt);

}  // namespace tt_eager::ops::clone

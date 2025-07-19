#pragma once

#include <ATen/core/Tensor.h>
#include <c10/core/ScalarType.h>
#include <c10/core/Layout.h>
#include <c10/core/Device.h>
#include <c10/core/MemoryFormat.h>
#include <c10/util/Optional.h>

namespace tt_eager::ops::to_copy {

at::Tensor ttnn_to_copy(
    const at::Tensor& self,
    c10::optional<at::ScalarType> dtype,
    c10::optional<at::Layout> layout,
    c10::optional<at::Device> device,
    c10::optional<bool> pin_memory,
    bool non_blocking,
    c10::optional<at::MemoryFormat> memory_format);

}  // namespace tt_eager::ops::to_copy

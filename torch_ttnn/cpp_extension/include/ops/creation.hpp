#pragma once

#include <ATen/core/Tensor.h>
#include <c10/util/Optional.h>
#include <c10/util/ArrayRef.h>
#include <c10/core/ScalarType.h>
#include <c10/core/Layout.h>
#include <c10/core/Device.h>

namespace tt_eager::ops::create {
at::Tensor custom_empty_strided(
    c10::IntArrayRef size,
    c10::IntArrayRef stride,
    c10::optional<at::ScalarType> dtype_opt,
    c10::optional<at::Layout> layout_opt,
    c10::optional<at::Device> device_opt,
    c10::optional<bool> pin_memory_opt);

at::Tensor custom_empty_memory_format(
    at::IntArrayRef size,
    c10::optional<at::ScalarType> dtype_opt,
    c10::optional<at::Layout> layout_opt,
    c10::optional<at::Device> device_opt,
    c10::optional<bool> pin_memory_opt,
    c10::optional<at::MemoryFormat> memory_format_opt = c10::nullopt);

}  // namespace tt_eager::ops::create

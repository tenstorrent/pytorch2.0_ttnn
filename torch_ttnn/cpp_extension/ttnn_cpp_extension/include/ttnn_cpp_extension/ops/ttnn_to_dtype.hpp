#pragma once
#include <ATen/ATen.h>
#include <c10/core/ScalarType.h>
#include <c10/core/MemoryFormat.h>
#include <c10/util/Optional.h>

at::Tensor ttnn_to_dtype(
    const at::Tensor& self,
    at::ScalarType dtype,
    bool non_blocking,
    bool copy,
    c10::optional<c10::MemoryFormat> memory_format  // додано
);

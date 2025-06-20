#pragma once

#include <ATen/ATen.h>

namespace tt_eager::ops::view {

// Implementation of aten::expand.default
at::Tensor ttnn_view(const at::Tensor& self, at::IntArrayRef size);
at::Tensor ttnn_expand(const at::Tensor& self, at::IntArrayRef size, bool implicit);
at::Tensor ttnn_permute(const at::Tensor& input, at::IntArrayRef dims);
at::Tensor ttnn_select_int(const at::Tensor& input, int64_t dim, int64_t index);
at::Tensor ttnn_slice_tensor(const at::Tensor& self, int64_t dim, int64_t start, int64_t end, int64_t step);
at::Tensor ttnn_t_default(const at::Tensor& self);
at::Tensor ttnn_transpose_int(const at::Tensor& input, int64_t dim0, int64_t dim1);
at::Tensor ttnn_unsqueeze(const at::Tensor& self, int64_t dim);

}
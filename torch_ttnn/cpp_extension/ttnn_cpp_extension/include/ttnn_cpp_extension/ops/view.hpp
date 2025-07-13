#pragma once

#include "ttnn_cpp_extension/utils/extension_utils.hpp"

#include <ATen/core/Tensor.h>
#include <ATen/core/Scalar.h>
#include <ATen/core/Dimname.h>
#include <ATen/core/ScalarType.h>
#include <c10/util/Optional.h>
#include <vector>
#include <c10/core/SymInt.h>

namespace tt_eager::ops::view {

using TtnnTensor = ttnn::Tensor;
using Shape = ttnn::Shape;

TtnnTensor select(const TtnnTensor& input, int dim, int index);

TtnnTensor broadcast(const TtnnTensor& input, const Shape& target_shape);

at::Tensor ttnn_view(const at::Tensor& self, at::IntArrayRef size);

at::Tensor ttnn_expand(const at::Tensor& self, at::IntArrayRef size, bool implicit);

at::Tensor ttnn_permute(const at::Tensor& input, at::IntArrayRef dims);

at::Tensor ttnn_slice_tensor(
    const at::Tensor& input,
    int64_t dim,
    c10::optional<c10::SymInt> start,
    c10::optional<c10::SymInt> end,
    c10::SymInt step);

std::vector<at::Tensor> ttnn_split_tensor_fixed(const at::Tensor& self, c10::SymInt split_size, int64_t dim);
std::vector<at::Tensor> ttnn_split_tensor_sections(const at::Tensor& self, at::IntArrayRef sections, int64_t dim);

at::Tensor ttnn_t_default(const at::Tensor& self);

at::Tensor ttnn_transpose_int(const at::Tensor& input, int64_t dim0, int64_t dim1);

at::Tensor ttnn_unsqueeze(const at::Tensor& self, int64_t dim);

at::Tensor ttnn_squeeze_dim(const at::Tensor& self, int64_t dim);

}  // namespace tt_eager::ops::view

#pragma once
#include "ttnn_cpp_extension/utils/extension_utils.hpp"

#include <ATen/core/Tensor.h>                    // at::Tensor, at::TensorList
#include <ATen/core/Scalar.h>                    // at::Scalar
#include <ATen/core/Dimname.h>                   // at::IntArrayRef
#include <ATen/core/ScalarType.h>                // scalar types
#include <c10/util/Optional.h>                   // c10::optional
#include <vector>


namespace tt_eager::ops::view {

using TtnnTensor = ttnn::Tensor;
using Shape = ttnn::Shape;

/**
 * Select a slice along a dimension (removes that dimension).
 */
TtnnTensor select(const TtnnTensor& input, int dim, int index);

/**
 * Broadcast input tensor to target shape as a view.
 */
TtnnTensor broadcast(const TtnnTensor& input, const Shape& target_shape);

/**
 * Implementation of aten::view.default
 */
at::Tensor ttnn_view(const at::Tensor& self, at::IntArrayRef size);

/**
 * Implementation of aten::expand.default
 */
at::Tensor ttnn_expand(const at::Tensor& self, at::IntArrayRef size, bool implicit);

/**
 * Implementation of aten::permute.default
 */
at::Tensor ttnn_permute(const at::Tensor& input, at::IntArrayRef dims);

/**
 * Implementation of aten::slice.Tensor
 */
at::Tensor ttnn_slice_tensor(const at::Tensor& self, int64_t dim, int64_t start, int64_t end, int64_t step);

/**
 * Implementation of aten::split.Tensor
 */
at::TensorList ttnn_split_tensor_fixed(const at::Tensor& self, int64_t split_size, int64_t dim);
at::TensorList ttnn_split_tensor_sections(const at::Tensor& self, at::IntArrayRef sections, int64_t dim);

/**
 * Implementation of aten::t.default
 */
at::Tensor ttnn_t_default(const at::Tensor& self);

/**
 * Implementation of aten::transpose.int
 */
at::Tensor ttnn_transpose_int(const at::Tensor& input, int64_t dim0, int64_t dim1);

/**
 * Implementation of aten::unsqueeze.default
 */
at::Tensor ttnn_unsqueeze(const at::Tensor& self, int64_t dim);

}  // namespace tt_eager::ops::view
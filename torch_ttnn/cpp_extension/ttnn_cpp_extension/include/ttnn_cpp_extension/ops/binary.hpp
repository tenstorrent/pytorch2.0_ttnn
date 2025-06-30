#pragma once

#include <ATen/core/Tensor.h>
#include <ATen/core/Scalar.h>

namespace tt_eager::ops::binary {

// Element-wise addition: out = input + alpha * other
at::Tensor& ttnn_add_out(
    const at::Tensor& input,
    const at::Tensor& other,
    const at::Scalar& alpha,
    at::Tensor& out);

// Element-wise addition creating a new tensor
at::Tensor ttnn_add_tensor(
    const at::Tensor& input,
    const at::Tensor& other,
    const at::Scalar& alpha);

// Matrix multiplication with addition: result = beta * self + alpha * (mat1 @ mat2)
at::Tensor ttnn_addmm(
    const at::Tensor& self,
    const at::Tensor& mat1,
    const at::Tensor& mat2,
    const at::Scalar& beta,
    const at::Scalar& alpha);

// Batch matrix multiplication
at::Tensor ttnn_bmm(
    const at::Tensor& batch1,
    const at::Tensor& batch2);

// Element-wise multiplication
at::Tensor ttnn_mul_tensor(
    const at::Tensor& input,
    const at::Tensor& other);

// Element-wise division
at::Tensor ttnn_div_tensor(
    const at::Tensor& input,
    const at::Tensor& other);

// Reverse subtraction: result = other - alpha * self
at::Tensor ttnn_rsub_scalar(
    const at::Tensor& self,
    const at::Scalar& other,
    const at::Scalar& alpha);

}  // namespace tt_eager::ops::binary

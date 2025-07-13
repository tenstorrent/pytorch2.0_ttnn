#pragma once

#include <ATen/core/Tensor.h>
#include <ATen/core/Scalar.h>

namespace tt_eager::ops::binary {

at::Tensor& ttnn_add_out(const at::Tensor& input, const at::Tensor& other, const at::Scalar& alpha, at::Tensor& out);

at::Tensor ttnn_add_tensor(const at::Tensor& input, const at::Tensor& other, const at::Scalar& alpha);

at::Tensor ttnn_addmm(
    const at::Tensor& self,
    const at::Tensor& mat1,
    const at::Tensor& mat2,
    const at::Scalar& beta,
    const at::Scalar& alpha);

at::Tensor ttnn_bmm(const at::Tensor& batch1, const at::Tensor& batch2);

at::Tensor ttnn_mul_tensor(const at::Tensor& input, const at::Tensor& other);

at::Tensor ttnn_mul_scalar(const at::Tensor& self, const at::Scalar& other);

at::Tensor ttnn_div_tensor(const at::Tensor& input, const at::Tensor& other);

at::Tensor ttnn_rsub_scalar(const at::Tensor& self, const at::Scalar& other, const at::Scalar& alpha);

at::Tensor ttnn_rsub_tensor(const at::Tensor& self, const at::Tensor& other, const at::Scalar& alpha);

at::Tensor ttnn_sub_tensor(const at::Tensor& input, const at::Tensor& other, const at::Scalar& alpha = 1.0);

at::Tensor ttnn_sub_scalar(const at::Tensor& self, const at::Scalar& other, const at::Scalar& alpha = 1.0);

}  // namespace tt_eager::ops::binary

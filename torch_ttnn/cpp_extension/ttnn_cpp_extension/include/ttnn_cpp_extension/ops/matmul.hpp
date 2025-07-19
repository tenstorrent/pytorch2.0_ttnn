#pragma once

#include <ATen/Tensor.h>
#include <ATen/core/Scalar.h>

namespace tt_eager::ops::matmul {
    at::Tensor ttnn_matmul(const at::Tensor& self, const at::Tensor& other);
    
    at::Tensor ttnn_addmm(
        const at::Tensor& self,
        const at::Tensor& mat1,
        const at::Tensor& mat2,
        const at::Scalar& beta,
        const at::Scalar& alpha);
    
    at::Tensor ttnn_bmm(const at::Tensor& batch1, const at::Tensor& batch2);
}

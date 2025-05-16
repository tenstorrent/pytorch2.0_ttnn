#pragma once

#include <cstdint>
#include <variant>
#include <vector>

#include <ttnn/tensor/tensor.hpp>
#include <ATen/core/Tensor.h>

using VariantVectorTy = std::variant<std::vector<float>, std::vector<int>>;

void convert_vector_from_uint32_to_int(std::vector<int>& dst_vector, const std::vector<uint32_t>& src_vector);

VariantVectorTy tensor_to_vector(const at::Tensor& tensor);

VariantVectorTy tensor_to_vector(const ttnn::Tensor& ttnn_tensor);

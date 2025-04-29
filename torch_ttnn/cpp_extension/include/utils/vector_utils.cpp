#include <cmath>

#include "vector_utils.hpp"
#include "extension_utils.hpp"

namespace {
// Debug Utils
template <typename T>
void vector_compare(const std::vector<T>& first, const std::vector<T>& second) {
    TORCH_INTERNAL_ASSERT(first.size() == second.size());
    for (int i = 0; i < first.size(); ++i) {
        if (std::fabs(first[i] - second[i]) > 0.000001) {
            LOGGING("mismatch: ", first[i], " vs ", second[i]);
        }
    }
}
}  // namespace
void convert_vector_from_uint32_to_int(std::vector<int>& dst_vector, const std::vector<uint32_t>& src_vector) {
    std::transform(src_vector.begin(), src_vector.end(), std::back_inserter(dst_vector), [](const uint32_t value) {
        return static_cast<int>(value);
    });
}

VariantVectorTy tensor_to_vector(const at::Tensor& tensor) {
    auto dtype = tensor.dtype();
    if (dtype == at::ScalarType::BFloat16) {
        auto torch_float = tensor.to(at::kFloat);
        std::vector<float> v(torch_float.data_ptr<float>(), torch_float.data_ptr<float>() + torch_float.numel());
        LOGGING("torch_tensor: ", v);
        return v;
    } else if (dtype == at::ScalarType::Int || dtype == at::ScalarType::Long) {
        auto torch_int = tensor.toType(at::ScalarType::Int);
        std::vector<int> v(torch_int.data_ptr<int>(), torch_int.data_ptr<int>() + torch_int.numel());
        LOGGING("torch_tensor: ", v);
        return v;
    } else {
        TORCH_INTERNAL_ASSERT(false);
    }
}

VariantVectorTy tensor_to_vector(const ttnn::Tensor& ttnn_tensor) {
    auto ttnn_dtype = ttnn_tensor.dtype();
    auto is_tensor_on_device = ttnn::is_tensor_on_device_or_multidevice(ttnn_tensor);

    ttnn::Tensor ttnn_tensor_tmp = ttnn_tensor;
    if (is_tensor_on_device) {
        auto logical_shape = ttnn_tensor.get_logical_shape();
        auto logical_rank = logical_shape.rank();
        if (logical_rank == 1) {
            ttnn::Shape new_shape({1, logical_shape[0]});
            ttnn_tensor_tmp = ttnn_tensor.reshape(new_shape);
        }
    }
    if (ttnn_dtype == ttnn::DataType::BFLOAT16) {
        std::vector<float> ttnn_vector = ttnn_tensor_tmp.to_vector<float>();
        LOGGING("src_dev: ", ttnn_vector);
        return ttnn_vector;
    } else if (ttnn_dtype == ttnn::DataType::UINT32) {
        auto ttnn_vector = ttnn_tensor_tmp.to_vector<uint32_t>();
        std::vector<int> src_vector_int;
        convert_vector_from_uint32_to_int(src_vector_int, ttnn_vector);
        LOGGING("src_dev: ", src_vector_int);
        return src_vector_int;
    } else {
        TORCH_INTERNAL_ASSERT(false);
    }
}

void compare_torch_and_ttnn_tensors(const at::Tensor& torch_tensor, const ttnn::Tensor& ttnn_tensor) {
    const auto DEBUG_CPP_EXT = std::getenv("DEBUG_CPP_EXT") != nullptr;
    if (DEBUG_CPP_EXT) {
        auto ttnn_dtype = ttnn_tensor.dtype();
        if (ttnn_dtype == ttnn::DataType::BFLOAT16) {
            auto torch_vector = std::get<std::vector<float>>(tensor_to_vector(torch_tensor));
            auto ttnn_vector = std::get<std::vector<float>>(tensor_to_vector(ttnn_tensor));

            vector_compare(torch_vector, ttnn_vector);
        } else if (ttnn_dtype == ttnn::DataType::UINT32) {
            auto torch_vector = std::get<std::vector<int>>(tensor_to_vector(torch_tensor));
            auto ttnn_vector = std::get<std::vector<int>>(tensor_to_vector(ttnn_tensor));

            vector_compare(torch_vector, ttnn_vector);
        }
    }
}
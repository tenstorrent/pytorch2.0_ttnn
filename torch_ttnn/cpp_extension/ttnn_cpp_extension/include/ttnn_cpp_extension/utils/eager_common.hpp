#pragma once

#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"

#include <ttnn/operations/copy/typecast/typecast.hpp>
#include <ttnn/operations/core/core.hpp>
#include <ttnn/tensor/tensor.hpp>
#include <ttnn/types.hpp>

#include <ATen/core/Tensor.h>
#include <ATen/core/Scalar.h>
#include <ATen/core/Generator.h>
#include <c10/core/ScalarType.h>
#include <c10/util/Exception.h>
#include <c10/util/Optional.h>
#include <cmath>
#include <optional>

namespace tt_eager::ext {

inline ttnn::Tensor tileify(const at::Tensor& t) {
    TORCH_CHECK(t.device().type() == c10::DeviceType::PrivateUse1, "Tensor must be on TTNN device");
    at::TtnnTensorImpl* impl = static_cast<at::TtnnTensorImpl*>(t.unsafeGetTensorImpl());
    auto tt = impl->get_ttnn_tensor();
    if (tt.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        tt = ttnn::to_layout(tt, ttnn::TILE_LAYOUT);
    }
    return tt;
}

inline at::Tensor make_empty_like_tt(const at::Tensor& t, c10::optional<at::ScalarType> dtype_override = c10::nullopt) {
    c10::optional<at::ScalarType> dtype_opt = dtype_override.has_value()
                                                  ? c10::optional<at::ScalarType>(*dtype_override)
                                                  : c10::optional<at::ScalarType>(t.scalar_type());
    return tt_eager::ops::create::custom_empty_memory_format(
        t.sizes(), dtype_opt, c10::nullopt, c10::optional<at::Device>(t.device()), c10::nullopt);
}

inline at::Tensor& write_from_ttnn(at::Tensor& out, const at::Tensor& like, const ttnn::Tensor& result) {
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(out.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(like);
    out_impl->set_ttnn_tensor(result);
    return out;
}

inline std::optional<std::variant<int, ttnn::SmallVector<int>>> to_ttnn_dim_variant(c10::IntArrayRef dims) {
    if (dims.size() == 0) {
        return std::nullopt;
    }
    if (dims.size() == 1) {
        return static_cast<int>(dims[0]);
    }
    ttnn::SmallVector<int> dv;
    dv.reserve(dims.size());
    for (auto d : dims) {
        dv.push_back(static_cast<int>(d));
    }
    return dv;
}

inline ttnn::DataType to_ttnn_dtype(const at::ScalarType st) {
    switch (st) {
        case at::kFloat: return ttnn::DataType::FLOAT32;
        case at::kBFloat16: return ttnn::DataType::BFLOAT16;
        case at::kInt: return ttnn::DataType::INT32;
        case at::kByte: return ttnn::DataType::UINT8;
        case at::kBool: return ttnn::DataType::BFLOAT16;
        default: TORCH_CHECK(false, "Unsupported dtype for TTNN reduction: ", st);
    }
}

}  // namespace tt_eager::ext

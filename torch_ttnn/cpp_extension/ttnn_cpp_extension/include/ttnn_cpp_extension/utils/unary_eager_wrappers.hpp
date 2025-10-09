#pragma once

#include "ttnn_cpp_extension/utils/eager_common.hpp"

#include <ttnn/operations/eltwise/unary/unary.hpp>
#include <ttnn/operations/eltwise/binary/binary.hpp>
#include <ttnn/operations/eltwise/complex/complex.hpp>

namespace tt_eager::ext {

// Concepts (unary-only)
template <auto Op>
concept TTNNUnaryFn = requires(const ttnn::Tensor& a) {
    { Op(a) } -> std::same_as<ttnn::Tensor>;
};

template <auto Op>
concept TTNNUnaryOptIntFn = requires(const ttnn::Tensor& a, std::optional<int32_t> p) {
    { Op(a, p) } -> std::same_as<ttnn::Tensor>;
};

// Unary: expects Op(a) → ttnn::Tensor
template <auto Op>
    requires TTNNUnaryFn<Op>
struct unary_tensor {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& a) {
        at::Tensor out = tt_eager::ext::make_empty_like_tt(a);
        return invoke_into(a, out);
    }
    [[nodiscard]] static at::Tensor& invoke_inplace(at::Tensor& self) { return invoke_into(self, self); }
    [[nodiscard]] static at::Tensor& invoke_into(const at::Tensor& in, at::Tensor& out) {
        ttnn::Tensor a_tile = tt_eager::ext::tilize(in);
        ttnn::Tensor result = Op(a_tile);
        return tt_eager::ext::write_from_ttnn(out, in, result);
    }
};

// Optional-int variants
template <auto Op>
    requires TTNNUnaryOptIntFn<Op>
struct unary_tensor_opt_int_none {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& a) {
        at::Tensor out = tt_eager::ext::make_empty_like_tt(a);
        return invoke_into(a, out);
    }
    [[nodiscard]] static at::Tensor& invoke_inplace(at::Tensor& self) { return invoke_into(self, self); }
    [[nodiscard]] static at::Tensor& invoke_into(const at::Tensor& in, at::Tensor& out) {
        ttnn::Tensor a_tile = tt_eager::ext::tilize(in);
        ttnn::Tensor result = Op(a_tile, std::nullopt);
        return tt_eager::ext::write_from_ttnn(out, in, result);
    }
};

template <auto Op>
    requires TTNNUnaryOptIntFn<Op>
struct unary_tensor_opt_int {
    [[nodiscard]] static at::Tensor invoke_decimals(const at::Tensor& a, int64_t decimals) {
        at::Tensor out = tt_eager::ext::make_empty_like_tt(a);
        return invoke_decimals_into(a, decimals, out);
    }
    [[nodiscard]] static at::Tensor& invoke_decimals_inplace(at::Tensor& self, int64_t decimals) {
        return invoke_decimals_into(self, decimals, self);
    }
    [[nodiscard]] static at::Tensor& invoke_decimals_into(const at::Tensor& in, int64_t decimals, at::Tensor& out) {
        ttnn::Tensor a_tile = tt_eager::ext::tilize(in);
        std::optional<int32_t> dec_opt = std::optional<int32_t>(static_cast<int32_t>(decimals));
        ttnn::Tensor result = Op(a_tile, dec_opt);
        return tt_eager::ext::write_from_ttnn(out, in, result);
    }
};

// Complex unary from real
template <auto Op>
struct complex_unary_from_real {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& a) {
        at::Tensor out = tt_eager::ext::make_empty_like_tt(a);
        return invoke_into(a, out);
    }
    [[nodiscard]] static at::Tensor& invoke_inplace(at::Tensor& self) { return invoke_into(self, self); }
    [[nodiscard]] static at::Tensor& invoke_into(const at::Tensor& in, at::Tensor& out) {
        ttnn::Tensor real_tt = tt_eager::ext::tilize(in);
        ttnn::Tensor zero_tt = ttnn::multiply(real_tt, 0.0f);
        ttnn::operations::complex::ComplexTensor ct({real_tt, zero_tt});
        auto ret = Op(ct, ttnn::L1_MEMORY_CONFIG);
        using ReturnT = decltype(ret);
        if constexpr (std::is_same_v<ReturnT, ttnn::Tensor>) {
            return tt_eager::ext::write_from_ttnn(out, in, ret);
        } else {
            ttnn::Tensor real_tt_out = ret.real();
            return tt_eager::ext::write_from_ttnn(out, in, real_tt_out);
        }
    }
};

}  // namespace tt_eager::ext

#pragma once

#include "ttnn_cpp_extension/utils/eager_common.hpp"

#include <ttnn/operations/eltwise/unary/unary.hpp>
#include <ttnn/operations/eltwise/binary/binary.hpp>
#include <ttnn/operations/eltwise/complex/complex.hpp>

#include <ATen/ops/view_as_real.h>

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
template <auto Op, auto TTNNMemoryConfig = ttnn::DRAM_MEMORY_CONFIG>
    requires TTNNUnaryFn<Op>
struct unary_tensor {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& a) {
        at::Tensor out = tt_eager::ext::make_empty_like_ttnn(a);
        return invoke_into(a, out);
    }
    [[nodiscard]] static at::Tensor& invoke_inplace(at::Tensor& self) { return invoke_into(self, self); }
    [[nodiscard]] static at::Tensor& invoke_into(const at::Tensor& in, at::Tensor& out) {
        ttnn::Tensor a_tile = tt_eager::ext::tilize(in);
        ttnn::Tensor result = Op(a_tile, TTNNMemoryConfig);
        return tt_eager::ext::write_from_ttnn(out, in, result);
    }
};

// Unary with boolean output (e.g. signbit, isfinite, etc.)
template <auto Op, auto TTNNMemoryConfig = ttnn::DRAM_MEMORY_CONFIG>
    requires TTNNUnaryFn<Op>
struct unary_tensor_bool {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& a) {
        at::Tensor out = tt_eager::ext::make_empty_like_ttnn(a, at::kBool);
        return invoke_into(a, out);
    }
    // No inplace for boolean checks usually
    [[nodiscard]] static at::Tensor& invoke_into(const at::Tensor& in, at::Tensor& out) {
        ttnn::Tensor a_tile = tt_eager::ext::tilize(in);
        ttnn::Tensor result = Op(a_tile, TTNNMemoryConfig);
        return tt_eager::ext::write_from_ttnn(out, in, result);
    }
};

// Optional-int variants
template <auto Op, auto TTNNMemoryConfig = ttnn::DRAM_MEMORY_CONFIG>
    requires TTNNUnaryOptIntFn<Op>
struct unary_tensor_opt_int_none {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& a) {
        at::Tensor out = tt_eager::ext::make_empty_like_ttnn(a);
        return invoke_into(a, out);
    }
    [[nodiscard]] static at::Tensor& invoke_inplace(at::Tensor& self) { return invoke_into(self, self); }
    [[nodiscard]] static at::Tensor& invoke_into(const at::Tensor& in, at::Tensor& out) {
        ttnn::Tensor a_tile = tt_eager::ext::tilize(in);
        ttnn::Tensor result = Op(a_tile, std::nullopt, TTNNMemoryConfig);
        return tt_eager::ext::write_from_ttnn(out, in, result);
    }
};

template <auto Op, auto TTNNMemoryConfig = ttnn::DRAM_MEMORY_CONFIG>
    requires TTNNUnaryOptIntFn<Op>
struct unary_tensor_opt_int {
    [[nodiscard]] static at::Tensor invoke_decimals(const at::Tensor& a, int64_t decimals) {
        at::Tensor out = tt_eager::ext::make_empty_like_ttnn(a);
        return invoke_decimals_into(a, decimals, out);
    }
    [[nodiscard]] static at::Tensor& invoke_decimals_inplace(at::Tensor& self, int64_t decimals) {
        return invoke_decimals_into(self, decimals, self);
    }
    [[nodiscard]] static at::Tensor& invoke_decimals_into(const at::Tensor& in, int64_t decimals, at::Tensor& out) {
        ttnn::Tensor a_tile = tt_eager::ext::tilize(in);
        std::optional<int32_t> dec_opt = std::optional<int32_t>(static_cast<int32_t>(decimals));
        ttnn::Tensor result = Op(a_tile, dec_opt, TTNNMemoryConfig);
        return tt_eager::ext::write_from_ttnn(out, in, result);
    }
};

// Complex unary (real->complex and complex->complex support)
template <auto Op, auto TTNNMemoryConfig = ttnn::DRAM_MEMORY_CONFIG>
struct complex_unary {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& a) {
        c10::optional<at::ScalarType> out_dtype = c10::nullopt;

        // Handle dtype correction for Complex Input -> Real Output (e.g. angle)
        if (a.is_complex()) {
            // Check the return type of the operation Op when called with a ComplexTensor
            using ReturnT = decltype(Op(std::declval<ttnn::operations::complex::ComplexTensor>(), TTNNMemoryConfig));

            // If Op returns a standard Tensor (implying Real) but input was Complex,
            // we must explicitly allocate a Real output tensor.
            if constexpr (!std::is_same_v<ReturnT, ttnn::operations::complex::ComplexTensor>) {
                out_dtype = c10::toRealValueType(a.scalar_type());
            }
        }

        at::Tensor out = tt_eager::ext::make_empty_like_ttnn(a, out_dtype);
        return invoke_into(a, out);
    }
    [[nodiscard]] static at::Tensor& invoke_inplace(at::Tensor& self) { return invoke_into(self, self); }
    [[nodiscard]] static at::Tensor& invoke_into(const at::Tensor& in, at::Tensor& out) {
        // Handle real inputs
        if (!in.is_complex()) {
            ttnn::Tensor real_tt = tt_eager::ext::tilize(in);
            ttnn::Tensor zero_tt = ttnn::multiply(real_tt, 0.0f);
            ttnn::operations::complex::ComplexTensor ct({real_tt, zero_tt});
            auto ret = Op(ct, TTNNMemoryConfig);
            using ReturnT = decltype(ret);
            if constexpr (std::is_same_v<ReturnT, ttnn::Tensor>) {
                return tt_eager::ext::write_from_ttnn(out, in, ret);
            } else {
                ttnn::Tensor real_tt_out = ret.real();
                return tt_eager::ext::write_from_ttnn(out, in, real_tt_out);
            }
        }

        // Handle complex inputs
        // Expected format: contiguous tensor with last dim size 2 (real, imag)
        // or a standard PyTorch complex tensor (which is viewed as float with last dim 2 in some contexts,
        // but we need to separate it for TTNN).
        // PyTorch complex tensors are internally stored as [..., 2] of floats.
        // at::view_as_real is the standard way to access real/imag parts as a float view.
        at::Tensor in_view = at::view_as_real(in);  // [..., 2]
        at::Tensor real_part = in_view.select(-1, 0).contiguous();
        at::Tensor imag_part = in_view.select(-1, 1).contiguous();

        ttnn::Tensor real_tt = tt_eager::ext::tilize(real_part);
        ttnn::Tensor imag_tt = tt_eager::ext::tilize(imag_part);

        ttnn::operations::complex::ComplexTensor ct({real_tt, imag_tt});
        auto ret = Op(ct, TTNNMemoryConfig);

        using ReturnT = decltype(ret);
        if constexpr (std::is_same_v<ReturnT, ttnn::Tensor>) {
            // Op returns real tensor (e.g. angle)
            return tt_eager::ext::write_from_ttnn(out, real_part, ret);
        } else {
            // Op returns complex tensor (e.g. conj)
            // We need to write back to 'out' which is complex
            // out should be pre-allocated as complex
            ttnn::Tensor out_real = ret.real();
            ttnn::Tensor out_imag = ret.imag();

            // We need to construct the output PyTorch complex tensor from these two components.
            // Since 'out' is provided, we write into its real and imag views.
            at::Tensor out_view = at::view_as_real(out);
            at::Tensor out_real_part = out_view.select(-1, 0);
            at::Tensor out_imag_part = out_view.select(-1, 1);

            tt_eager::ext::write_from_ttnn(out_real_part, real_part, out_real);
            tt_eager::ext::write_from_ttnn(out_imag_part, imag_part, out_imag);

            return out;
        }
    }
};

}  // namespace tt_eager::ext

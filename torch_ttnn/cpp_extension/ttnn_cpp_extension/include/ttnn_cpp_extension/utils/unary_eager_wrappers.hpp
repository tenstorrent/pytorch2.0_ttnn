#pragma once

#include "ttnn_cpp_extension/utils/eager_common.hpp"

#include <ttnn/operations/eltwise/unary/unary.hpp>
#include <ttnn/operations/eltwise/binary/binary.hpp>
#include <ttnn/operations/eltwise/complex/complex.hpp>

#include <ATen/ops/view_as_real.h>
#include <ATen/ops/view_as_complex.h>
#include <ATen/ops/real.h>
#include <ATen/ops/imag.h>
#include <ATen/ops/stack.h>

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

template <auto Op>
concept TTNNUnaryBoolFn = requires(const ttnn::Tensor& a, bool b) {
    { Op(a, b, ttnn::DRAM_MEMORY_CONFIG) } -> std::same_as<ttnn::Tensor>;
};

template <auto Op>
concept TTNNUnaryIntBoolFn = requires(const ttnn::Tensor& a, int i, bool b) {
    { Op(a, i, b, ttnn::DRAM_MEMORY_CONFIG) } -> std::same_as<ttnn::Tensor>;
};

// Unary: expects Op(a) → ttnn::Tensor
template <auto Op>
    requires TTNNUnaryFn<Op>
struct unary_tensor {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& a) {
        at::Tensor out = tt_eager::ext::make_empty_like_ttnn(a);
        return invoke_into(a, out);
    }
    [[nodiscard]] static at::Tensor& invoke_inplace(at::Tensor& self) { return invoke_into(self, self); }
    [[nodiscard]] static at::Tensor& invoke_into(const at::Tensor& in, at::Tensor& out) {
        ttnn::Tensor a_tile = tt_eager::ext::tilize(in);
        ttnn::Tensor result = Op(a_tile, ttnn::DRAM_MEMORY_CONFIG);
        return tt_eager::ext::write_from_ttnn(out, in, result);
    }
};

// Unary with boolean output (e.g. signbit, isfinite, etc.)
template <auto Op>
    requires TTNNUnaryFn<Op>
struct unary_tensor_bool {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& a) {
        at::Tensor out = tt_eager::ext::make_empty_like_ttnn(a, at::kBool);
        return invoke_into(a, out);
    }
    // No inplace for boolean checks usually
    [[nodiscard]] static at::Tensor& invoke_into(const at::Tensor& in, at::Tensor& out) {
        ttnn::Tensor a_tile = tt_eager::ext::tilize(in);
        ttnn::Tensor result = Op(a_tile, ttnn::DRAM_MEMORY_CONFIG);
        return tt_eager::ext::write_from_ttnn(out, in, result);
    }
};

// Optional-int variants
template <auto Op>
    requires TTNNUnaryOptIntFn<Op>
struct unary_tensor_opt_int_none {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& a) {
        at::Tensor out = tt_eager::ext::make_empty_like_ttnn(a);
        return invoke_into(a, out);
    }
    [[nodiscard]] static at::Tensor& invoke_inplace(at::Tensor& self) { return invoke_into(self, self); }
    [[nodiscard]] static at::Tensor& invoke_into(const at::Tensor& in, at::Tensor& out) {
        ttnn::Tensor a_tile = tt_eager::ext::tilize(in);
        ttnn::Tensor result = Op(a_tile, std::nullopt, ttnn::DRAM_MEMORY_CONFIG);
        return tt_eager::ext::write_from_ttnn(out, in, result);
    }
};

template <auto Op>
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
        ttnn::Tensor result = Op(a_tile, dec_opt, ttnn::DRAM_MEMORY_CONFIG);
        return tt_eager::ext::write_from_ttnn(out, in, result);
    }
};

// Unary with bool parameter (e.g. erf, erfc, exp, log, log10, log2, log1p)
template <auto Op>
    requires TTNNUnaryBoolFn<Op>
struct unary_tensor_bool_param {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& a) {
        at::Tensor out = tt_eager::ext::make_empty_like_ttnn(a);
        return invoke_into(a, out);
    }
    [[nodiscard]] static at::Tensor& invoke_inplace(at::Tensor& self) { return invoke_into(self, self); }
    [[nodiscard]] static at::Tensor& invoke_into(const at::Tensor& in, at::Tensor& out) {
        ttnn::Tensor a_tile = tt_eager::ext::tilize(in);
        // Default to false for fast_and_approximate_mode (most operations use false)
        // For log operations, true is typically used, but we'll use false as default
        ttnn::Tensor result = Op(a_tile, false, ttnn::DRAM_MEMORY_CONFIG);
        return tt_eager::ext::write_from_ttnn(out, in, result);
    }
};

// Unary with int and bool parameters (e.g. sigmoid)
template <auto Op>
    requires TTNNUnaryIntBoolFn<Op>
struct unary_tensor_int_bool_param {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& a) {
        at::Tensor out = tt_eager::ext::make_empty_like_ttnn(a);
        return invoke_into(a, out);
    }
    [[nodiscard]] static at::Tensor& invoke_inplace(at::Tensor& self) { return invoke_into(self, self); }
    [[nodiscard]] static at::Tensor& invoke_into(const at::Tensor& in, at::Tensor& out) {
        ttnn::Tensor a_tile = tt_eager::ext::tilize(in);
        // Default values: vector_mode = VecMode::RC (4), fast_and_approximate_mode = false
        ttnn::Tensor result = Op(a_tile, 4, false, ttnn::DRAM_MEMORY_CONFIG);
        return tt_eager::ext::write_from_ttnn(out, in, result);
    }
};

// Complex unary (real->complex and complex->complex support)
template <auto Op>
struct complex_unary {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& a) {
        c10::optional<at::ScalarType> out_dtype = c10::nullopt;

        // Handle dtype correction for Complex Input -> Real Output (e.g. angle)
        if (a.is_complex()) {
            // Check the return type of the operation Op when called with a ComplexTensor
            using ReturnT = decltype(Op(std::declval<ttnn::operations::complex::ComplexTensor>(), ttnn::DRAM_MEMORY_CONFIG));

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
            // Create zero tensor with same shape and layout as real_tt
            ttnn::Tensor zero_tt = ttnn::multiply(real_tt, 0.0f, std::nullopt, ttnn::DRAM_MEMORY_CONFIG);
            ttnn::operations::complex::ComplexTensor ct({real_tt, zero_tt});
            auto ret = Op(ct, ttnn::DRAM_MEMORY_CONFIG);
            using ReturnT = decltype(ret);
            if constexpr (std::is_same_v<ReturnT, ttnn::Tensor>) {
                return tt_eager::ext::write_from_ttnn(out, in, ret);
            } else {
                ttnn::Tensor real_tt_out = ret.real();
                return tt_eager::ext::write_from_ttnn(out, in, real_tt_out);
            }
        }

        // Handle complex inputs
        // Extract real and imaginary parts from complex tensor.
        // Since view_as_real is not available for PrivateUse1 backend,
        // we convert to CPU first, extract parts, then convert back.
        at::Tensor in_cpu = in.to(c10::DeviceType::CPU);
        at::Tensor real_part_cpu = at::real(in_cpu).contiguous();
        at::Tensor imag_part_cpu = at::imag(in_cpu).contiguous();
        
        // Convert back to TTNN device
        at::Tensor real_part = real_part_cpu.to(in.device());
        at::Tensor imag_part = imag_part_cpu.to(in.device());

        ttnn::Tensor real_tt = tt_eager::ext::tilize(real_part);
        ttnn::Tensor imag_tt = tt_eager::ext::tilize(imag_part);

        ttnn::operations::complex::ComplexTensor ct({real_tt, imag_tt});
        auto ret = Op(ct, ttnn::DRAM_MEMORY_CONFIG);

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

            // Write real and imag parts separately, then combine into complex tensor
            // We need to create separate tensors for real and imag parts
            at::Tensor out_real_part = tt_eager::ext::make_empty_like_ttnn(real_part);
            at::Tensor out_imag_part = tt_eager::ext::make_empty_like_ttnn(imag_part);
            
            tt_eager::ext::write_from_ttnn(out_real_part, real_part, out_real);
            tt_eager::ext::write_from_ttnn(out_imag_part, imag_part, out_imag);
            
            // Combine real and imag parts into complex tensor
            // Stack real and imag along last dimension, then use view_as_complex
            // Convert to CPU first to use standard PyTorch operations
            at::Tensor out_real_cpu = out_real_part.to(c10::DeviceType::CPU);
            at::Tensor out_imag_cpu = out_imag_part.to(c10::DeviceType::CPU);
            
            // Stack along last dimension: [..., 2] where [..., 0] is real and [..., 1] is imag
            at::Tensor out_stacked_cpu = at::stack({out_real_cpu, out_imag_cpu}, -1);
            // Use view_as_complex to convert [..., 2] to complex tensor
            at::Tensor out_complex_cpu = at::view_as_complex(out_stacked_cpu);
            at::Tensor out_complex = out_complex_cpu.to(out.device());
            
            // Copy the complex tensor data to the output tensor
            out.copy_(out_complex);

            return out;
        }
    }
};

}  // namespace tt_eager::ext

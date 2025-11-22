#pragma once

#include "ttnn_cpp_extension/utils/unary_eager_wrappers.hpp"

#include <ttnn/operations/eltwise/unary/unary_composite.hpp>
#include <ttnn/operations/eltwise/complex_unary/complex_unary.hpp>
#include <ttnn/operations/eltwise/binary/binary_composite.hpp>
#include <ttnn/operations/reduction/generic/generic_reductions.hpp>
#include <ttnn/operations/eltwise/unary/unary.hpp>

#include <ATen/native/DispatchStub.h>
#include <torch/csrc/utils/pybind.h>
#include <torch/extension.h>
#include <torch/library.h>

#include <string>

namespace tt_eager::ext {

// Helper templates for concise unary registrations
// - register_unary_base_out_inplace: registers base, base.out, base_
// - register_unary_base_out:         registers base, base.out
// - register_unary_base_inplace:     registers base, base_
template <template <auto> class Wrapper, auto Op>
static inline void register_unary_base_out_inplace(torch::Library& m, const std::string& base) {
    const std::string out = base + ".out";
    const std::string inplace = base + "_";
    m.impl(base.c_str(), TORCH_FN(Wrapper<Op>::invoke));
    m.impl(out.c_str(), TORCH_FN(Wrapper<Op>::invoke_into));
    m.impl(inplace.c_str(), TORCH_FN(Wrapper<Op>::invoke_inplace));
}

template <template <auto> class Wrapper, auto Op>
static inline void register_unary_base_out(torch::Library& m, const std::string& base) {
    const std::string out = base + ".out";
    m.impl(base.c_str(), TORCH_FN(Wrapper<Op>::invoke));
    m.impl(out.c_str(), TORCH_FN(Wrapper<Op>::invoke_into));
}

template <template <auto> class Wrapper, auto Op>
static inline void register_unary_base_inplace(torch::Library& m, const std::string& base) {
    const std::string inplace = base + "_";
    m.impl(base.c_str(), TORCH_FN(Wrapper<Op>::invoke));
    m.impl(inplace.c_str(), TORCH_FN(Wrapper<Op>::invoke_inplace));
}

static inline void register_unary_ops(torch::Library& m) {
    // =========================
    // Unary ops
    // =========================
    // Standard unary (base/out/_). Example schema:
    //   schema [::invoke        ]: op(Tensor self) -> Tensor
    //   schema [::invoke_into   ]: op.out(Tensor self, *, Tensor(a!) out) -> Tensor(a!)
    //   schema [::invoke_inplace]: op_(Tensor(a!) self) -> Tensor(a!)
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::abs>(m, "abs");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::abs>(m, "absolute");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::neg>(m, "neg");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::reciprocal>(m, "reciprocal");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::sqrt>(m, "sqrt");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::rsqrt>(m, "rsqrt");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::square>(m, "square");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::sin>(m, "sin");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::cos>(m, "cos");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::tan>(m, "tan");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::sinh>(m, "sinh");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::cosh>(m, "cosh");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::tanh>(m, "tanh");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::floor>(m, "floor");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::ceil>(m, "ceil");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::trunc>(m, "trunc");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::frac>(m, "frac");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::bitwise_not>(m, "bitwise_not");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::logical_not>(m, "logical_not");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::sign>(m, "sign");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::i0>(m, "i0");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::erf>(m, "erf");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::erfc>(m, "erfc");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::erfinv>(m, "erfinv");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::exp>(m, "exp");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::log>(m, "log");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::log10>(m, "log10");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::log2>(m, "log2");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::log1p>(m, "log1p");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::acos>(m, "acos");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::acosh>(m, "acosh");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::acosh>(m, "arccosh");
    // Complex unary (real->complex adapter). Example schema:
    //   schema [::invoke        ]: angle(Tensor self) -> Tensor
    //   schema [::invoke_into   ]: angle.out(Tensor self, *, Tensor(a!) out) -> Tensor(a!)
    //   schema [::invoke_inplace]: angle_(Tensor(a!) self) -> Tensor(a!)
    register_unary_base_out_inplace<tt_eager::ext::complex_unary_from_real, ttnn::angle>(m, "angle");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::asin>(m, "asin");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::asinh>(m, "asinh");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::atan>(m, "atan");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::atanh>(m, "atanh");
    register_unary_base_out_inplace<tt_eager::ext::complex_unary_from_real, ttnn::conj>(m, "conj");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::deg2rad>(m, "deg2rad");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::digamma>(m, "digamma");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::expm1>(m, "expm1");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::lgamma>(m, "lgamma");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::rad2deg>(m, "rad2deg");
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor, ttnn::sigmoid>(m, "sigmoid");

    // Round family (optional decimals). Example schema:
    //   schema [::invoke]: round(Tensor self) -> Tensor
    //   schema [::invoke_into]: round.out(Tensor self, *, Tensor(a!) out) -> Tensor(a!)
    //   schema [::invoke_inplace]: round_(Tensor(a!) self) -> Tensor(a!)
    //   schema [::invoke_decimals]: round.decimals(Tensor self, *, int decimals) -> Tensor
    //   schema [::invoke_decimals_into]: round.decimals_out(Tensor self, *, int decimals, Tensor(a!) out) -> Tensor(a!)
    register_unary_base_out_inplace<tt_eager::ext::unary_tensor_opt_int_none, ttnn::round>(m, "round");
    m.impl("round.decimals", TORCH_FN(tt_eager::ext::unary_tensor_opt_int<ttnn::round>::invoke_decimals));
    m.impl("round.decimals_out", TORCH_FN(tt_eager::ext::unary_tensor_opt_int<ttnn::round>::invoke_decimals_into));

    // Base + inplace only. Example schema:
    //   schema [::invoke        ]: op(Tensor self) -> Tensor
    //   schema [::invoke_inplace]: op_(Tensor(a!) self) -> Tensor(a!)
    register_unary_base_inplace<tt_eager::ext::unary_tensor, ttnn::relu>(m, "relu");

    // Base + out only (no inplace). Example schema:
    //   schema [::invoke      ]: op(Tensor self) -> Tensor
    //   schema [::invoke_into ]: op.out(Tensor self, *, Tensor(a!) out) -> Tensor(a!)
    register_unary_base_out<tt_eager::ext::unary_tensor_bool, ttnn::signbit>(m, "signbit");
    register_unary_base_out<tt_eager::ext::unary_tensor_bool, ttnn::isfinite>(m, "isfinite");
    register_unary_base_out<tt_eager::ext::unary_tensor_bool, ttnn::isinf>(m, "isinf");
    register_unary_base_out<tt_eager::ext::unary_tensor_bool, ttnn::isnan>(m, "isnan");
}

}  // namespace tt_eager::ext

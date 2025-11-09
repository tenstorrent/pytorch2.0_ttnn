#pragma once

#include "ttnn_cpp_extension/utils/binary_eager_wrappers.hpp"

#include <ttnn/operations/eltwise/binary/binary.hpp>
#include <ttnn/operations/eltwise/unary/unary.hpp>
#include <torch/library.h>

namespace tt_eager::ext {

static inline void register_binary_ops(torch::Library& m) {
    // =========================
    // Binary ops
    // =========================
    // schema: add.out(Tensor self, Tensor other, *, Scalar alpha=1, Tensor(a!) out) -> Tensor(a!)
    m.impl("add.out", TORCH_FN(tt_eager::ext::binary_tensor_tensor_alpha<ttnn::addalpha>::invoke_into));
    // schema: add.Tensor(Tensor self, Tensor other, *, Scalar alpha=1) -> Tensor
    m.impl("add.Tensor", TORCH_FN(tt_eager::ext::binary_tensor_tensor_alpha<ttnn::addalpha>::invoke));
    // schema: add.Scalar(Tensor self, Scalar other, Scalar alpha=1) -> Tensor
    m.impl("add.Scalar", TORCH_FN(tt_eager::ext::binary_tensor_float_with_alpha_adapter<ttnn::add>::invoke));
    // schema: add_.Scalar(Tensor(a!) self, Scalar other, Scalar alpha=1) -> Tensor(a!)
    m.impl("add_.Scalar", TORCH_FN(tt_eager::ext::binary_tensor_float_with_alpha_adapter<ttnn::add_>::invoke_inplace));
    // schema: add_.Tensor(Tensor(a!) self, Tensor other, *, Scalar alpha=1) -> Tensor(a!)
    m.impl("add_.Tensor", TORCH_FN(tt_eager::ext::binary_tensor_tensor_alpha<ttnn::addalpha>::invoke_inplace));
    // _add_relu.* = relu(add.Tensor with alpha=1)
    // Match aten schema: (Tensor, Tensor, Scalar alpha=1)
    using AddReluAlphaWrapper = tt_eager::ext::binary_tensor_tensor_alpha_then_unary<ttnn::addalpha, ttnn::relu>;
    // schema: _add_relu.Tensor(Tensor self, Tensor other, *, Scalar alpha=1) -> Tensor
    m.impl("_add_relu.Tensor", TORCH_FN(AddReluAlphaWrapper::invoke));
    // schema: _add_relu.out(Tensor self, Tensor other, *, Scalar alpha=1, Tensor(a!) out) -> Tensor(a!)
    m.impl("_add_relu.out", TORCH_FN(AddReluAlphaWrapper::invoke_into));
    // schema: _add_relu_.Tensor(Tensor(a!) self, Tensor other, *, Scalar alpha=1) -> Tensor(a!)
    m.impl("_add_relu_.Tensor", TORCH_FN(AddReluAlphaWrapper::invoke_inplace));

    // schema: sub.out(Tensor self, Tensor other, *, Scalar alpha=1, Tensor(a!) out) -> Tensor(a!)
    m.impl("sub.out", TORCH_FN(tt_eager::ext::binary_tensor_tensor_alpha<ttnn::subalpha>::invoke_into));
    // schema: sub.Tensor(Tensor self, Tensor other, *, Scalar alpha=1) -> Tensor
    m.impl("sub.Tensor", TORCH_FN(tt_eager::ext::binary_tensor_tensor_alpha<ttnn::subalpha>::invoke));
    // schema: sub.Scalar(Tensor self, Scalar other, Scalar alpha=1) -> Tensor
    m.impl("sub.Scalar", TORCH_FN(tt_eager::ext::binary_tensor_float_with_alpha_adapter<ttnn::subtract>::invoke));
    // schema: sub_.Scalar(Tensor(a!) self, Scalar other, Scalar alpha=1) -> Tensor(a!)
    m.impl(
        "sub_.Scalar",
        TORCH_FN(tt_eager::ext::binary_tensor_float_with_alpha_adapter<ttnn::subtract_>::invoke_inplace));
    // schema: sub_.Tensor(Tensor(a!) self, Tensor other, *, Scalar alpha=1) -> Tensor(a!)
    m.impl("sub_.Tensor", TORCH_FN(tt_eager::ext::binary_tensor_tensor_alpha<ttnn::subalpha>::invoke_inplace));
    // rsub: reverse subtract
    // rsub.Tensor: rsub(self, other, alpha) = other - alpha*self
    // rsub.Scalar: rsub(self, other, alpha) = other - alpha*self
    // schema: rsub.Tensor(Tensor self, Tensor other, *, Scalar alpha=1) -> Tensor
    m.impl(
        "rsub.Tensor",
        TORCH_FN(tt_eager::ext::binary_tensor_tensor_alpha_swapped<ttnn::subalpha>::invoke));  // TODO: to check
    // schema: rsub.Scalar(Tensor self, Scalar other, Scalar alpha=1) -> Tensor
    m.impl(
        "rsub.Scalar",
        TORCH_FN(tt_eager::ext::binary_tensor_float_with_alpha_adapter<ttnn::rsub>::invoke));  // TODO: to check

    // Arithmetic ops
    // schema: mul.out(Tensor self, Tensor other, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("mul.out", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::multiply>::invoke_into));
    // schema: mul.Tensor(Tensor self, Tensor other) -> Tensor
    m.impl("mul.Tensor", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::multiply>::invoke));
    // schema: mul_.Tensor(Tensor(a!) self, Tensor other) -> Tensor(a!)
    m.impl("mul_.Tensor", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::multiply_>::invoke_inplace));

    // schema: div.out(Tensor self, Tensor other, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("div.out", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::divide>::invoke_into));
    // schema: div.Tensor(Tensor self, Tensor other) -> Tensor
    m.impl("div.Tensor", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::divide>::invoke));
    // schema: div.Scalar(Tensor self, Scalar other) -> Tensor
    m.impl("div.Scalar", TORCH_FN(tt_eager::ext::binary_tensor_float<ttnn::divide>::invoke));
    // schema: div_.Scalar(Tensor(a!) self, Scalar other) -> Tensor(a!)
    m.impl("div_.Scalar", TORCH_FN(tt_eager::ext::binary_tensor_float<ttnn::divide_>::invoke_inplace));
    // schema: div_.Tensor(Tensor(a!) self, Tensor other) -> Tensor(a!)
    m.impl("div_.Tensor", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::divide_>::invoke_inplace));

    // schema: floor_divide(Tensor self, Tensor other) -> Tensor
    m.impl("floor_divide", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::floor_div>::invoke));
    // schema: floor_divide.Scalar(Tensor self, Scalar other) -> Tensor
    m.impl("floor_divide.Scalar", TORCH_FN(tt_eager::ext::binary_tensor_float<ttnn::floor_div>::invoke));
    // schema: floor_divide.out(Tensor self, Tensor other, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("floor_divide.out", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::floor_div>::invoke_into));
    // schema: floor_divide_.Scalar(Tensor(a!) self, Scalar other) -> Tensor(a!)
    m.impl("floor_divide_.Scalar", TORCH_FN(tt_eager::ext::binary_tensor_float<ttnn::floor_div>::invoke_inplace));
    // schema: floor_divide_.Tensor(Tensor(a!) self, Tensor other) -> Tensor(a!)
    m.impl("floor_divide_.Tensor", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::floor_div>::invoke_inplace));
    // true_divide.Scalar
    // true_divide.out
    // true_divide_.Scalar
    // true_divide_.Tensor
    // (handled via divide) no direct ttnn::true_divide
    // schema: pow.Scalar(Scalar self, Tensor exponent) -> Tensor
    m.impl("pow.Scalar", TORCH_FN(tt_eager::ext::binary_scalar_tensor_as_tensor<ttnn::pow>::invoke));
    // schema: pow.Scalar_out(Scalar self, Tensor exponent, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("pow.Scalar_out", TORCH_FN(tt_eager::ext::binary_scalar_tensor_as_tensor<ttnn::pow>::invoke_into));
    // schema: pow.Tensor_Scalar(Tensor self, Scalar exponent) -> Tensor
    m.impl("pow.Tensor_Scalar", TORCH_FN(tt_eager::ext::unary_tensor_int<ttnn::power>::invoke));
    // schema: pow.Tensor_Scalar_out(Tensor self, Scalar exponent, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("pow.Tensor_Scalar_out", TORCH_FN(tt_eager::ext::unary_tensor_int<ttnn::power>::invoke_into));
    // schema: pow_.Scalar(Tensor(a!) self, Scalar exponent) -> Tensor(a!)
    m.impl("pow_.Scalar", TORCH_FN(tt_eager::ext::unary_tensor_int<ttnn::power>::invoke_inplace));
    // schema: pow_.Tensor(Tensor(a!) self, Tensor exponent) -> Tensor(a!)
    m.impl("pow_.Tensor", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::pow>::invoke_inplace));
    // schema: nextafter.out(Tensor self, Tensor other, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("nextafter.out", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::nextafter>::invoke_into));
    // schema: nextafter(Tensor self, Tensor other) -> Tensor
    m.impl("nextafter", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::nextafter>::invoke));
    // schema: dot(Tensor self, Tensor tensor) -> Tensor
    m.impl("dot", TORCH_FN(tt_eager::ext::binary_tensor_tensor_outlike<ttnn::moreh_dot>::invoke));
    // schema: dot.out(Tensor self, Tensor tensor, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("dot.out", TORCH_FN(tt_eager::ext::binary_tensor_tensor_outlike<ttnn::moreh_dot>::invoke_into));
    // schema: hypot.out(Tensor self, Tensor other, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("hypot.out", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::hypot>::invoke_into));
    // schema: hypot(Tensor self, Tensor other) -> Tensor
    m.impl("hypot", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::hypot>::invoke));

    // schema: matmul.out(Tensor self, Tensor other, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("matmul.out", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::matmul>::invoke_into));
    // schema: matmul(Tensor self, Tensor other) -> Tensor
    m.impl("matmul", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::matmul>::invoke));
    // mm
    // mm.out
    // mv
    // mv.out
    // bmm
    // bmm.out

    // Logical ops
    // schema: logical_and.out(Tensor self, Tensor other, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("logical_and.out", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::logical_and>::invoke_into));
    // schema: logical_and(Tensor self, Tensor other) -> Tensor
    m.impl("logical_and", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::logical_and>::invoke));
    // schema: logical_and_(Tensor(a!) self, Tensor other) -> Tensor(a!)
    m.impl("logical_and_", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::logical_and_>::invoke_inplace));

    // schema: logical_or.out(Tensor self, Tensor other, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("logical_or.out", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::logical_or>::invoke_into));
    // schema: logical_or(Tensor self, Tensor other) -> Tensor
    m.impl("logical_or", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::logical_or>::invoke));
    // schema: logical_or_(Tensor(a!) self, Tensor other) -> Tensor(a!)
    m.impl("logical_or_", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::logical_or_>::invoke_inplace));

    // schema: logical_xor.out(Tensor self, Tensor other, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("logical_xor.out", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::logical_xor>::invoke_into));
    // schema: logical_xor(Tensor self, Tensor other) -> Tensor
    m.impl("logical_xor", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::logical_xor>::invoke));
    // schema: logical_xor_(Tensor(a!) self, Tensor other) -> Tensor(a!)
    m.impl("logical_xor_", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::logical_xor_>::invoke_inplace));

    // Trigonometric binary ops
    // schema: atan2.out(Tensor self, Tensor other, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("atan2.out", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::atan2>::invoke_into));
    // schema: atan2(Tensor self, Tensor other) -> Tensor
    m.impl("atan2", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::atan2>::invoke));
    // schema: atan2_(Tensor(a!) self, Tensor other) -> Tensor(a!)
    m.impl("atan2_", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::atan2>::invoke_inplace));

    // Relational ops (Tensor versions only)
    // schema: eq.Tensor_out(Tensor self, Tensor other, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("eq.Tensor_out", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::eq>::invoke_into));
    // schema: eq.Tensor(Tensor self, Tensor other) -> Tensor
    m.impl("eq.Tensor", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::eq>::invoke));

    // schema: eq.Scalar(Tensor self, Scalar other) -> Tensor
    m.impl("eq.Scalar", TORCH_FN(tt_eager::ext::binary_tensor_scalar_as_tensor<ttnn::eq>::invoke));
    // schema: eq.Scalar_out(Tensor self, Scalar other, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("eq.Scalar_out", TORCH_FN(tt_eager::ext::binary_tensor_scalar_as_tensor<ttnn::eq>::invoke_into));

    // schema: ne.Tensor_out(Tensor self, Tensor other, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("ne.Tensor_out", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::ne>::invoke_into));
    // schema: ne.Tensor(Tensor self, Tensor other) -> Tensor
    m.impl("ne.Tensor", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::ne>::invoke));

    // schema: ne.Scalar(Tensor self, Scalar other) -> Tensor
    m.impl("ne.Scalar", TORCH_FN(tt_eager::ext::binary_tensor_scalar_as_tensor<ttnn::ne>::invoke));
    // schema: ne.Scalar_out(Tensor self, Scalar other, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("ne.Scalar_out", TORCH_FN(tt_eager::ext::binary_tensor_scalar_as_tensor<ttnn::ne>::invoke_into));

    // schema: ge.Tensor_out(Tensor self, Tensor other, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("ge.Tensor_out", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::ge>::invoke_into));
    // schema: ge.Tensor(Tensor self, Tensor other) -> Tensor
    m.impl("ge.Tensor", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::ge>::invoke));

    // schema: ge.Scalar(Tensor self, Scalar other) -> Tensor
    m.impl("ge.Scalar", TORCH_FN(tt_eager::ext::binary_tensor_scalar_as_tensor<ttnn::ge>::invoke));
    // schema: ge.Scalar_out(Tensor self, Scalar other, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("ge.Scalar_out", TORCH_FN(tt_eager::ext::binary_tensor_scalar_as_tensor<ttnn::ge>::invoke_into));

    // schema: gt.Tensor_out(Tensor self, Tensor other, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("gt.Tensor_out", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::gt>::invoke_into));
    // schema: gt.Tensor(Tensor self, Tensor other) -> Tensor
    m.impl("gt.Tensor", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::gt>::invoke));

    // schema: gt.Scalar(Tensor self, Scalar other) -> Tensor
    m.impl("gt.Scalar", TORCH_FN(tt_eager::ext::binary_tensor_scalar_as_tensor<ttnn::gt>::invoke));
    // schema: gt.Scalar_out(Tensor self, Scalar other, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("gt.Scalar_out", TORCH_FN(tt_eager::ext::binary_tensor_scalar_as_tensor<ttnn::gt>::invoke_into));

    // schema: le.Tensor_out(Tensor self, Tensor other, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("le.Tensor_out", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::le>::invoke_into));
    // schema: le.Tensor(Tensor self, Tensor other) -> Tensor
    m.impl("le.Tensor", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::le>::invoke));

    // schema: le.Scalar(Tensor self, Scalar other) -> Tensor
    m.impl("le.Scalar", TORCH_FN(tt_eager::ext::binary_tensor_scalar_as_tensor<ttnn::le>::invoke));
    // schema: le.Scalar_out(Tensor self, Scalar other, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("le.Scalar_out", TORCH_FN(tt_eager::ext::binary_tensor_scalar_as_tensor<ttnn::le>::invoke_into));

    // schema: lt.Tensor_out(Tensor self, Tensor other, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("lt.Tensor_out", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::lt>::invoke_into));
    // schema: lt.Tensor(Tensor self, Tensor other) -> Tensor
    m.impl("lt.Tensor", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::lt>::invoke));

    // schema: lt.Scalar(Tensor self, Scalar other) -> Tensor
    m.impl("lt.Scalar", TORCH_FN(tt_eager::ext::binary_tensor_scalar_as_tensor<ttnn::lt>::invoke));
    // schema: lt.Scalar_out(Tensor self, Scalar other, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("lt.Scalar_out", TORCH_FN(tt_eager::ext::binary_tensor_scalar_as_tensor<ttnn::lt>::invoke_into));

    // Special ops
    // schema: logaddexp.out(Tensor self, Tensor other, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("logaddexp.out", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::logaddexp>::invoke_into));
    // schema: logaddexp(Tensor self, Tensor other) -> Tensor
    m.impl("logaddexp", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::logaddexp>::invoke));
    // schema: logaddexp2.out(Tensor self, Tensor other, *, Tensor(a!) out) -> Tensor(a!)
    m.impl("logaddexp2.out", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::logaddexp2>::invoke_into));
    // schema: logaddexp2(Tensor self, Tensor other) -> Tensor
    m.impl("logaddexp2", TORCH_FN(tt_eager::ext::binary_tensor_tensor<ttnn::logaddexp2>::invoke));
}

}  // namespace tt_eager::ext

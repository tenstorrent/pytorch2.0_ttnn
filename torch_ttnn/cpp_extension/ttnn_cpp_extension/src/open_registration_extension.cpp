#include <ATen/native/DispatchStub.h>
#include <torch/csrc/utils/pybind.h>
#include <torch/extension.h>

#include "ttnn_cpp_extension/utils/device.hpp"

#include "ttnn_cpp_extension/core/TtnnCustomAllocator.hpp"
#include "ttnn_cpp_extension/core/copy.hpp"

#include "ttnn_cpp_extension/ops/creation.hpp"

#include "ttnn_cpp_extension/utils/eager_wrap.hpp"
// #include "ttnn_cpp_extension/utils/autograd_wrap.hpp"

#include <ttnn/operations/eltwise/unary/unary.hpp>
#include <ttnn/operations/eltwise/unary/unary_composite.hpp>
#include <ttnn/operations/eltwise/complex_unary/complex_unary.hpp>
#include <ttnn/operations/eltwise/binary/binary.hpp>
#include <ttnn/operations/eltwise/binary_backward/binary_backward.hpp>
#include <ttnn/operations/eltwise/binary/binary_composite.hpp>
#include <ttnn/operations/reduction/generic/generic_reductions.hpp>
#include <ttnn/operations/bernoulli/bernoulli.hpp>

// Register custom allocator. Only used to create dummy Torch tensor object.
REGISTER_ALLOCATOR(c10::DeviceType::PrivateUse1, &get_ttnn_custom_allocator());


namespace {

static inline void register_core_creation_and_copy(torch::Library& m) {
    // =========================
    // Core ops: creation and copy
    // =========================
    // From Pytorch's NamesRegistrations.cpp
    m.impl("aten::empty_strided", &tt_eager::ops::create::custom_empty_strided);
    m.impl("empty.memory_format", &tt_eager::ops::create::custom_empty_memory_format);
    m.impl("_copy_from", &ttnn_copy_from);
    // Pending TTNN core ops to register (from ttnn_ops_grouped.txt)
    // ttnn::to_dtype
    // ttnn::to_layout
    // ttnn::to_memory_config
}

static inline void register_unary_ops(torch::Library& m) {
    // =========================
    // Unary ops
    // =========================
    m.impl("abs", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::abs>::invoke));
    m.impl("abs.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::abs>::invoke_out));
    m.impl("abs_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::abs>::invoke_inplace));
    // absolute
    // absolute.out
    // absolute_
    m.impl("neg", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::neg>::invoke));
    m.impl("neg.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::neg>::invoke_out));
    m.impl("neg_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::neg>::invoke_inplace));
    m.impl("reciprocal", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::reciprocal>::invoke));
    m.impl("reciprocal.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::reciprocal>::invoke_out));
    m.impl("reciprocal_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::reciprocal>::invoke_inplace));
    m.impl("sqrt", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::sqrt>::invoke));
    m.impl("sqrt.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::sqrt>::invoke_out));
    m.impl("sqrt_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::sqrt>::invoke_inplace));
    m.impl("rsqrt", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::rsqrt>::invoke));
    m.impl("rsqrt.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::rsqrt>::invoke_out));
    m.impl("rsqrt_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::rsqrt>::invoke_inplace));
    m.impl("square", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::square>::invoke));
    m.impl("square.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::square>::invoke_out));
    m.impl("square_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::square>::invoke_inplace));
    m.impl("sin", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::sin>::invoke));
    m.impl("sin.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::sin>::invoke_out));
    m.impl("sin_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::sin>::invoke_inplace));
    m.impl("cos", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::cos>::invoke));
    m.impl("cos.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::cos>::invoke_out));
    m.impl("cos_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::cos>::invoke_inplace));
    m.impl("tan", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::tan>::invoke));
    m.impl("tan.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::tan>::invoke_out));
    m.impl("tan_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::tan>::invoke_inplace));
    m.impl("sinh", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::sinh>::invoke));
    m.impl("sinh.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::sinh>::invoke_out));
    m.impl("sinh_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::sinh>::invoke_inplace));
    m.impl("cosh", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::cosh>::invoke));
    m.impl("cosh.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::cosh>::invoke_out));
    m.impl("cosh_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::cosh>::invoke_inplace));
    m.impl("tanh", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::tanh>::invoke));
    m.impl("tanh.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::tanh>::invoke_out));
    m.impl("tanh_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::tanh>::invoke_inplace));
    m.impl("floor", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::floor>::invoke));
    m.impl("floor.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::floor>::invoke_out));
    m.impl("floor_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::floor>::invoke_inplace));
    m.impl("ceil", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::ceil>::invoke));
    m.impl("ceil.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::ceil>::invoke_out));
    m.impl("ceil_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::ceil>::invoke_inplace));
    m.impl("trunc", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::trunc>::invoke));
    m.impl("trunc.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::trunc>::invoke_out));
    m.impl("trunc_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::trunc>::invoke_inplace));
    m.impl("frac", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::frac>::invoke));
    m.impl("frac.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::frac>::invoke_out));
    m.impl("frac_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::frac>::invoke_inplace));
    m.impl("bitwise_not", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::bitwise_not>::invoke));
    m.impl("bitwise_not.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::bitwise_not>::invoke_out));
    m.impl("bitwise_not_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::bitwise_not>::invoke_inplace));
    m.impl("logical_not", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::logical_not>::invoke));
    m.impl("logical_not.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::logical_not>::invoke_out));
    m.impl("logical_not_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::logical_not>::invoke_inplace));
    m.impl("sign", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::sign>::invoke));
    m.impl("sign.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::sign>::invoke_out));
    m.impl("sign_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::sign>::invoke_inplace));
    m.impl("signbit", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::signbit>::invoke));
    m.impl("signbit.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::signbit>::invoke_out));
    m.impl("i0", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::i0>::invoke));
    m.impl("i0.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::i0>::invoke_out));
    m.impl("i0_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::i0>::invoke_inplace));
    m.impl("erf", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::erf>::invoke));
    m.impl("erf.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::erf>::invoke_out));
    m.impl("erf_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::erf>::invoke_inplace));
    m.impl("erfc", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::erfc>::invoke));
    m.impl("erfc.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::erfc>::invoke_out));
    m.impl("erfc_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::erfc>::invoke_inplace));
    m.impl("erfinv", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::erfinv>::invoke));
    m.impl("erfinv.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::erfinv>::invoke_out));
    m.impl("erfinv_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::erfinv>::invoke_inplace));
    m.impl("exp", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::exp>::invoke));
    m.impl("exp.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::exp>::invoke_out));
    m.impl("exp_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::exp>::invoke_inplace));
    m.impl("log", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::log>::invoke));
    m.impl("log.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::log>::invoke_out));
    m.impl("log_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::log>::invoke_inplace));
    m.impl("log10", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::log10>::invoke));
    m.impl("log10.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::log10>::invoke_out));
    m.impl("log10_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::log10>::invoke_inplace));
    m.impl("log2", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::log2>::invoke));
    m.impl("log2.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::log2>::invoke_out));
    m.impl("log2_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::log2>::invoke_inplace));
    m.impl("log1p", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::log1p>::invoke));
    m.impl("log1p.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::log1p>::invoke_out));
    m.impl("log1p_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::log1p>::invoke_inplace));
    m.impl("acos", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::acos>::invoke));
    m.impl("acos.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::acos>::invoke_out));
    m.impl("acos_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::acos>::invoke_inplace));
    m.impl("acosh", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::acosh>::invoke));
    m.impl("acosh.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::acosh>::invoke_out));
    m.impl("acosh_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::acosh>::invoke_inplace));
    // m.impl("angle", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::angle>::invoke)); // TODO: to move to binary?
    // m.impl("angle.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::angle>::invoke_out)); // TODO: to move to binary?
    // m.impl("angle_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::angle>::invoke_inplace)); // TODO: to move to binary?
    // m.impl("arccosh", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::arccosh>::invoke));
    // m.impl("arccosh.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::arccosh>::invoke_out));
    // m.impl("arccosh_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::arccosh>::invoke_inplace));
    m.impl("asin", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::asin>::invoke));
    m.impl("asin.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::asin>::invoke_out));
    m.impl("asin_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::asin>::invoke_inplace));
    
    m.impl("asinh", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::asinh>::invoke));
    m.impl("asinh.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::asinh>::invoke_out));
    m.impl("asinh_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::asinh>::invoke_inplace));
    m.impl("atan", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::atan>::invoke));
    m.impl("atan.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::atan>::invoke_out));
    m.impl("atan_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::atan>::invoke_inplace));
    
    m.impl("atanh", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::atanh>::invoke));
    m.impl("atanh.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::atanh>::invoke_out));
    m.impl("atanh_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::atanh>::invoke_inplace));
    // m.impl("conj", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::conj>::invoke)); // TODO: to move to binary?
    // m.impl("conj.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::conj>::invoke_out)); // TODO: to move to binary?
    // m.impl("conj_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::conj>::invoke_inplace)); // TODO: to move to binary?
    // ttnn::conj_bw
    m.impl("deg2rad", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::deg2rad>::invoke));
    m.impl("deg2rad.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::deg2rad>::invoke_out));
    m.impl("deg2rad_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::deg2rad>::invoke_inplace));
    
    m.impl("digamma", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::digamma>::invoke));
    m.impl("digamma.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::digamma>::invoke_out));
    m.impl("digamma_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::digamma>::invoke_inplace));
    
    m.impl("expm1", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::expm1>::invoke));
    m.impl("expm1.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::expm1>::invoke_out));
    m.impl("expm1_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::expm1>::invoke_inplace));
    
    // imag
    m.impl("isfinite", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::isfinite>::invoke));
    m.impl("isfinite.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::isfinite>::invoke_out));
    m.impl("isinf", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::isinf>::invoke));
    m.impl("isinf.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::isinf>::invoke_out));
    m.impl("isnan", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::isnan>::invoke));
    m.impl("isnan.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::isnan>::invoke_out));
    
    m.impl("lgamma", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::lgamma>::invoke));
    m.impl("lgamma.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::lgamma>::invoke_out));
    m.impl("lgamma_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::lgamma>::invoke_inplace));
    
    m.impl("rad2deg", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::rad2deg>::invoke));
    m.impl("rad2deg.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::rad2deg>::invoke_out));
    m.impl("rad2deg_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::rad2deg>::invoke_inplace));
    
    
    m.impl("relu", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::relu>::invoke));
    m.impl("relu_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::relu>::invoke_inplace));
    // real
    // round
    // round.out
    // ttnn::round (requires optional integer parameter); add specialized wrapper later
    // round_
    // ttnn::round_bw
    m.impl("sigmoid", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::sigmoid>::invoke));
    m.impl("sigmoid.out", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::sigmoid>::invoke_out));
    m.impl("sigmoid_", TORCH_FN(tt_eager::ext::unary_wrapper<ttnn::sigmoid>::invoke_inplace));
    
}

static inline void register_binary_ops(torch::Library& m) {
    // =========================
    // Binary ops
    // =========================
    m.impl("add.out", TORCH_FN(tt_eager::ext::binary_alpha_wrapper<ttnn::addalpha>::invoke_out));
    m.impl("add.Tensor", TORCH_FN(tt_eager::ext::binary_alpha_wrapper<ttnn::addalpha>::invoke));
    // add.Scalar
    // add_.Scalar
    m.impl("add_.Tensor", TORCH_FN(tt_eager::ext::binary_alpha_wrapper<ttnn::addalpha>::invoke_inplace));
    // _add_relu.Tensor
    // _add_relu.out
    // _add_relu_.Tensor

    m.impl("sub.out", TORCH_FN(tt_eager::ext::binary_alpha_wrapper<ttnn::subalpha>::invoke_out));
    m.impl("sub.Tensor", TORCH_FN(tt_eager::ext::binary_alpha_wrapper<ttnn::subalpha>::invoke));
    // sub.Scalar
    // sub_.Scalar
    m.impl("sub_.Tensor", TORCH_FN(tt_eager::ext::binary_alpha_wrapper<ttnn::subalpha>::invoke_inplace));
    // rsub.Scalar
    // rsub.Tensor

    // Arithmetic ops
    m.impl("mul.out", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::multiply>::invoke_out));
    m.impl("mul.Tensor", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::multiply>::invoke));
    m.impl("mul_.Tensor", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::multiply>::invoke_inplace));

    m.impl("div.out", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::divide>::invoke_out));
    m.impl("div.Tensor", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::divide>::invoke));
    // div.Scalar
    // div_.Scalar
    m.impl("div_.Tensor", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::divide>::invoke_inplace));
    // floor_divide
    // floor_divide.Scalar
    // floor_divide.out
    // floor_divide_.Scalar
    // floor_divide_.Tensor
    // ttnn::floor_div
    // true_divide.Scalar
    // true_divide.out
    // true_divide_.Scalar
    // true_divide_.Tensor
    // (handled via divide) no direct ttnn::true_divide
    // pow.Scalar
    // pow.Scalar_out
    // pow.Tensor_Scalar
    // pow.Tensor_Scalar_out
    // pow.Tensor_Tensor
    // pow.Tensor_Tensor_out
    // pow_.Scalar
    // pow_.Tensor
    // ttnn::pow
    m.impl("nextafter.out", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::nextafter>::invoke_out));
    m.impl("nextafter", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::nextafter>::invoke));
    // dot
    // dot.out
    m.impl("hypot.out", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::hypot>::invoke_out));
    m.impl("hypot", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::hypot>::invoke));
    
    // matmul
    // matmul.out
    // mm
    // mm.out
    // mv
    // mv.out
    // bmm
    // bmm.out

    // Logical ops
    m.impl("logical_and.out", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::logical_and>::invoke_out));
    m.impl("logical_and", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::logical_and>::invoke));
    m.impl("logical_and_", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::logical_and>::invoke_inplace));
    // ttnn::logical_and_

    m.impl("logical_or.out", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::logical_or>::invoke_out));
    m.impl("logical_or", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::logical_or>::invoke));
    m.impl("logical_or_", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::logical_or>::invoke_inplace));
    // ttnn::logical_or_

    m.impl("logical_xor.out", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::logical_xor>::invoke_out));
    m.impl("logical_xor", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::logical_xor>::invoke));
    m.impl("logical_xor_", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::logical_xor>::invoke_inplace));
    // ttnn::logical_xor_

    // Trigonometric binary ops
    m.impl("atan2.out", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::atan2>::invoke_out));
    m.impl("atan2", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::atan2>::invoke));
    m.impl("atan2_", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::atan2>::invoke_inplace));
    

    // Relational ops (Tensor versions only)
    m.impl("eq.Tensor_out", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::eq>::invoke_out));
    m.impl("eq.Tensor", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::eq>::invoke));
    // eq.Scalar
    // eq.Scalar_out

    m.impl("ne.Tensor_out", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::ne>::invoke_out));
    m.impl("ne.Tensor", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::ne>::invoke));
    // ne.Scalar
    // ne.Scalar_out

    m.impl("ge.Tensor_out", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::ge>::invoke_out));
    m.impl("ge.Tensor", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::ge>::invoke));
    // ge.Scalar
    // ge.Scalar_out

    m.impl("gt.Tensor_out", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::gt>::invoke_out));
    m.impl("gt.Tensor", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::gt>::invoke));
    // gt.Scalar
    // gt.Scalar_out

    m.impl("le.Tensor_out", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::le>::invoke_out));
    m.impl("le.Tensor", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::le>::invoke));
    // le.Scalar
    // le.Scalar_out

    m.impl("lt.Tensor_out", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::lt>::invoke_out));
    m.impl("lt.Tensor", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::lt>::invoke));
    // lt.Scalar
    // lt.Scalar_out

    // Special ops
    m.impl("logaddexp.out", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::logaddexp>::invoke_out));
    m.impl("logaddexp", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::logaddexp>::invoke));
    m.impl("logaddexp2.out", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::logaddexp2>::invoke_out));
    m.impl("logaddexp2", TORCH_FN(tt_eager::ext::binary_wrapper<ttnn::logaddexp2>::invoke));
}

static inline void register_reductions(torch::Library& m) {
    // =========================
    // Reductions
    // =========================
    // Sum
    // sum
    // sum.DimnameList_out
    // sum.IntList_out
    // sum.dim_DimnameList
    // sum.dim_IntList
    // ttnn::sum

    // Mean
    // mean
    // mean.dim
    // mean.names_dim
    // mean.names_out
    // mean.out
    // ttnn::mean

    // Max / Min
    // max
    // max.dim
    // max.dim_max
    // max.names_dim
    // max.names_dim_max
    // ttnn::max
    // min
    // min.dim
    // min.dim_min
    // min.names_dim
    // min.names_dim_min
    // ttnn::min

    // Std / Var
    // std
    // std.dim
    // std.names_dim
    // std.names_out
    // std.out
    // std.correction
    // std.correction_out
    // std.correction_names
    // std.correction_names_out
    // ttnn::std
    // var
    // var.dim
    // var.names_dim
    // var.names_out
    // var.out
    // var.correction
    // var.correction_out
    // var.correction_names
    // var.correction_names_out
    // ttnn::var
}

static inline void register_random_ops(torch::Library& m) {
    // =========================
    // Random
    // =========================
    m.impl("bernoulli", TORCH_FN(tt_eager::ext::random_wrapper<ttnn::bernoulli>::invoke));
    m.impl("bernoulli.out", TORCH_FN(tt_eager::ext::random_wrapper<ttnn::bernoulli>::invoke_out));
    // bernoulli_.Tensor
    // bernoulli_.float
    // cauchy_
    // exponential_
    // geometric_
    // normal_
    // random_
    // random_.from
    // random_.to
    // uniform_

    // Pending TTNN random ops to register
    // ttnn::prim::rand
    // ttnn::prim::uniform
    // ttnn::rand
    // ttnn::uniform
}

} // namespace

// This macro registers the kernels to the PyTorch Dispatcher.
// More details on the dispatcher can be found at
// http://blog.ezyang.com/2020/09/lets-talk-about-the-pytorch-dispatcher/.
TORCH_LIBRARY_IMPL(aten, PrivateUse1, m) {
    register_core_creation_and_copy(m);
    register_unary_ops(m);
    register_binary_ops(m);
    register_reductions(m);
    register_random_ops(m);
}

// TORCH_LIBRARY_IMPL(aten, AutogradPrivateUse1, m) {
//     // Unary
//     using AsinAutograd = tt_eager::ext::autograd_unary_wrapper<ttnn::asin, ttnn::asin_bw>;
//     m.impl("asin", TORCH_FN(AsinAutograd::invoke));

//     using AtanAutograd = tt_eager::ext::autograd_unary_wrapper<ttnn::atan, ttnn::atan_bw>;
//     m.impl("atan", TORCH_FN(AtanAutograd::invoke));

//     using DigammaAutograd = tt_eager::ext::autograd_unary_wrapper<ttnn::digamma, ttnn::digamma_bw>;
//     m.impl("digamma", TORCH_FN(DigammaAutograd::invoke));

//     using Expm1Autograd = tt_eager::ext::autograd_unary_wrapper<ttnn::expm1, ttnn::expm1_bw>;
//     m.impl("expm1", TORCH_FN(Expm1Autograd::invoke));

//     using Rad2DegAutograd = tt_eager::ext::autograd_unary_wrapper<ttnn::rad2deg, ttnn::rad2deg_bw>;
//     m.impl("rad2deg", TORCH_FN(Rad2DegAutograd::invoke));

//     using SigmoidAutograd = tt_eager::ext::autograd_unary_wrapper<ttnn::sigmoid, ttnn::sigmoid_bw>;
//     m.impl("sigmoid", TORCH_FN(SigmoidAutograd::invoke));

//     // Binary
//     using MulAutograd = tt_eager::ext::autograd_binary_wrapper<ttnn::multiply, ttnn::mul_bw>;
//     m.impl("mul.Tensor", TORCH_FN(MulAutograd::invoke));

//     using DivAutograd = tt_eager::ext::autograd_binary_wrapper<ttnn::divide, ttnn::div_bw>;
//     m.impl("div.Tensor", TORCH_FN(DivAutograd::invoke));

//     using HypotAutograd = tt_eager::ext::autograd_binary_wrapper<ttnn::hypot, ttnn::hypot_bw>;
//     m.impl("hypot", TORCH_FN(HypotAutograd::invoke));

//     using Atan2Autograd = tt_eager::ext::autograd_binary_wrapper<ttnn::atan2, ttnn::atan2_bw>;
//     m.impl("atan2", TORCH_FN(Atan2Autograd::invoke));

//     // Binary + alpha (add/sub with alpha)
//     using AddAlphaAutograd = tt_eager::ext::autograd_binary_alpha_wrapper<ttnn::addalpha, ttnn::addalpha_bw>;
//     m.impl("add.Tensor", TORCH_FN(AddAlphaAutograd::invoke));

//     using SubAlphaAutograd = tt_eager::ext::autograd_binary_alpha_wrapper<ttnn::subalpha, ttnn::subalpha_bw>;
//     m.impl("sub.Tensor", TORCH_FN(SubAlphaAutograd::invoke));
// }

// This macro registers helper functions associated with the ttnn_device_mode module that can be used in Python
PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
    m.def("as_torch_device", &as_torch_device, "get torch device from existing ttnn device");
    m.def("get_ttnn_tensor", &get_ttnn_tensor, "open ttnn device and get torch device");
    m.def("open_torch_device", &open_torch_device, "get torch device from existing ttnn device");
    m.def("close_torch_device", &close_torch_device, "close torch device and associated ttnn device");
}

#pragma once

#include "ttnn_cpp_extension/utils/eager_common.hpp"

#include <ttnn/operations/eltwise/binary/binary.hpp>
#include <ttnn/operations/eltwise/unary/unary.hpp>

namespace tt_eager::ext {

// Concepts (binary)
template <auto Op>
concept TTNNBinaryFn = requires(const ttnn::Tensor& a, const ttnn::Tensor& b) {
    { Op(a, b) } -> std::same_as<ttnn::Tensor>;
};

template <auto Op>
concept TTNNBinaryAlphaFn = requires(const ttnn::Tensor& a, const ttnn::Tensor& b, float alpha) {
    { Op(a, b, alpha) } -> std::same_as<ttnn::Tensor>;
};

template <auto Op>
concept TTNNBinaryScalarFn = requires(const ttnn::Tensor& a, float rhs) {
    { Op(a, rhs) } -> std::same_as<ttnn::Tensor>;
};

template <auto Op>
concept TTNNBinaryOutLikeFn = requires(const ttnn::Tensor& a, const ttnn::Tensor& b) {
    { Op(a, b, std::nullopt, std::nullopt, std::nullopt, std::nullopt) } -> std::same_as<ttnn::Tensor>;
};

// Binary alpha then unary (e.g., _add_relu)
template <auto BinaryAlphaOp, auto UnaryOp>
struct binary_tensor_tensor_alpha_then_unary {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& a, const at::Tensor& b, const c10::Scalar& alpha) {
        at::Tensor out = make_empty_like_tt(a);
        return invoke_into(a, b, alpha, out);
    }
    [[nodiscard]] static at::Tensor& invoke_inplace(
        at::Tensor& self, const at::Tensor& other, const c10::Scalar& alpha) {
        return invoke_into(self, other, alpha, self);
    }
    [[nodiscard]] static at::Tensor& invoke_into(
        const at::Tensor& a, const at::Tensor& b, const c10::Scalar& alpha, at::Tensor& out) {
        ttnn::Tensor a_tile = tileify(a);
        ttnn::Tensor b_tile = tileify(b);
        const float alpha_value = static_cast<float>(alpha.toDouble());
        ttnn::Tensor tmp = BinaryAlphaOp(a_tile, b_tile, alpha_value);
        ttnn::Tensor result = UnaryOp(tmp);
        return write_from_ttnn(out, a, result);
    }
};

// Binary alpha swapped (rsub)
template <auto Op>
struct binary_tensor_tensor_alpha_swapped {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& a, const at::Tensor& b, const c10::Scalar& alpha) {
        at::Tensor out = make_empty_like_tt(a);
        return invoke_into(a, b, alpha, out);
    }
    [[nodiscard]] static at::Tensor& invoke_inplace(
        at::Tensor& self, const at::Tensor& other, const c10::Scalar& alpha) {
        return invoke_into(self, other, alpha, self);
    }
    [[nodiscard]] static at::Tensor& invoke_into(
        const at::Tensor& a, const at::Tensor& b, const c10::Scalar& alpha, at::Tensor& out) {
        ttnn::Tensor a_tile = tileify(a);
        ttnn::Tensor b_tile = tileify(b);
        const float alpha_value = static_cast<float>(alpha.toDouble());
        ttnn::Tensor result = Op(b_tile, a_tile, alpha_value);
        return write_from_ttnn(out, a, result);
    }
};
// (concepts moved above)

// Binary tensor-tensor
template <auto Op>
    requires TTNNBinaryFn<Op>
struct binary_tensor_tensor {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& a, const at::Tensor& b) {
        at::Tensor out = make_empty_like_tt(a);
        return invoke_into(a, b, out);
    }
    [[nodiscard]] static at::Tensor& invoke_inplace(at::Tensor& self, const at::Tensor& other) {
        return invoke_into(self, other, self);
    }
    [[nodiscard]] static at::Tensor& invoke_into(const at::Tensor& a, const at::Tensor& b, at::Tensor& out) {
        ttnn::Tensor a_tile = tileify(a);
        ttnn::Tensor b_tile = tileify(b);
        ttnn::Tensor result = Op(a_tile, b_tile);
        return write_from_ttnn(out, a, result);
    }
};

// Binary tensor-float
template <auto Op>
    requires TTNNBinaryScalarFn<Op>
struct binary_tensor_float {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& a, const c10::Scalar& other) {
        at::Tensor out = make_empty_like_tt(a);
        return invoke_into(a, other, out);
    }
    [[nodiscard]] static at::Tensor& invoke_inplace(at::Tensor& self, const c10::Scalar& other) {
        return invoke_into(self, other, self);
    }
    [[nodiscard]] static at::Tensor& invoke_into(const at::Tensor& a, const c10::Scalar& other, at::Tensor& out) {
        ttnn::Tensor a_tile = tileify(a);
        const float rhs = static_cast<float>(other.toDouble());
        ttnn::Tensor result = Op(a_tile, rhs);
        return write_from_ttnn(out, a, result);
    }
};

// Binary alpha
template <auto Op>
    requires TTNNBinaryAlphaFn<Op>
struct binary_tensor_tensor_alpha {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& a, const at::Tensor& b, const c10::Scalar& alpha) {
        at::Tensor out = make_empty_like_tt(a);
        return invoke_into(a, b, alpha, out);
    }
    [[nodiscard]] static at::Tensor& invoke_inplace(
        at::Tensor& self, const at::Tensor& other, const c10::Scalar& alpha) {
        return invoke_into(self, other, alpha, self);
    }
    [[nodiscard]] static at::Tensor& invoke_into(
        const at::Tensor& a, const at::Tensor& b, const c10::Scalar& alpha, at::Tensor& out) {
        ttnn::Tensor a_tile = tileify(a);
        ttnn::Tensor b_tile = tileify(b);
        const float alpha_value = static_cast<float>(alpha.toDouble());
        ttnn::Tensor result = Op(a_tile, b_tile, alpha_value);
        return write_from_ttnn(out, a, result);
    }
};

// Tensor-Scalar adapter: materialize scalar as tensor like `a` and apply binary Op(a, rhs_tensor)
template <auto Op>
    requires TTNNBinaryFn<Op>
struct binary_tensor_scalar_as_tensor {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& a, const c10::Scalar& other) {
        at::Tensor out = make_empty_like_tt(a);
        return invoke_into(a, other, out);
    }
    [[nodiscard]] static at::Tensor& invoke_into(const at::Tensor& a, const c10::Scalar& other, at::Tensor& out) {
        ttnn::Tensor a_tile = tileify(a);
        ttnn::Tensor zero = ttnn::multiply(a_tile, 0.0f);
        const float rhs_f = static_cast<float>(other.toDouble());
        ttnn::Tensor rhs_tt = ttnn::add(zero, rhs_f);
        ttnn::Tensor result = Op(a_tile, rhs_tt);
        return write_from_ttnn(out, a, result);
    }
};

// Scalar-Tensor adapter: materialize scalar base like exponent and apply Op(base_tt, exponent)
template <auto Op>
    requires TTNNBinaryFn<Op>
struct binary_scalar_tensor_as_tensor {
    [[nodiscard]] static at::Tensor invoke(const c10::Scalar& base, const at::Tensor& exponent) {
        at::Tensor out = make_empty_like_tt(exponent);
        return invoke_into(base, exponent, out);
    }
    [[nodiscard]] static at::Tensor& invoke_into(const c10::Scalar& base, const at::Tensor& exponent, at::Tensor& out) {
        ttnn::Tensor exp_tt = tileify(exponent);
        ttnn::Tensor zero = ttnn::multiply(exp_tt, 0.0f);
        const float base_f = static_cast<float>(base.toDouble());
        ttnn::Tensor base_tt = ttnn::add(zero, base_f);
        ttnn::Tensor result = Op(base_tt, exp_tt);
        return write_from_ttnn(out, exponent, result);
    }
};

// Binary with out-like optional parameters forwarded as nullopts
template <auto Op>
    requires TTNNBinaryOutLikeFn<Op>
struct binary_tensor_tensor_outlike {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& a, const at::Tensor& b) {
        at::Tensor out = make_empty_like_tt(a);
        return invoke_into(a, b, out);
    }
    [[nodiscard]] static at::Tensor& invoke_into(const at::Tensor& a, const at::Tensor& b, at::Tensor& out) {
        ttnn::Tensor a_tile = tileify(a);
        ttnn::Tensor b_tile = tileify(b);
        ttnn::Tensor result = Op(a_tile, b_tile, std::nullopt, std::nullopt, std::nullopt, std::nullopt);
        return write_from_ttnn(out, a, result);
    }
};

// Binary Tensor + Scalar with separate alpha (e.g., add.Scalar, sub.Scalar)
template <auto Op>
    requires TTNNBinaryScalarFn<Op>
struct binary_tensor_float_with_alpha_adapter {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& a, const c10::Scalar& other, const c10::Scalar& alpha) {
        at::Tensor out = make_empty_like_tt(a);
        return invoke_into(a, other, alpha, out);
    }
    [[nodiscard]] static at::Tensor& invoke_inplace(
        at::Tensor& self, const c10::Scalar& other, const c10::Scalar& alpha) {
        return invoke_into(self, other, alpha, self);
    }
    [[nodiscard]] static at::Tensor& invoke_into(
        const at::Tensor& a, const c10::Scalar& other, const c10::Scalar& alpha, at::Tensor& out) {
        ttnn::Tensor a_tile = tileify(a);
        const float rhs = static_cast<float>(other.toDouble()) * static_cast<float>(alpha.toDouble());
        ttnn::Tensor result = Op(a_tile, rhs);
        return write_from_ttnn(out, a, result);
    }
};

}  // namespace tt_eager::ext

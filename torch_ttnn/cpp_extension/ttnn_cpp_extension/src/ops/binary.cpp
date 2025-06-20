// SPDX-FileCopyrightText: © 2024 Tenstorrent Inc.
// SPDX-License-Identifier: Apache-2.0

#include <c10/util/Optional.h>

#include <ttnn/operations/matmul/matmul.hpp>
#include <ttnn/operations/eltwise/binary/binary.hpp>
#include <ttnn/operations/full/full.hpp>
#include <ttnn/operations/core/core.hpp>      // for ttnn::to_layout, etc.
#include <ttnn/operations/shape/shape.hpp>    // for GetShape::invoke()
#include <ttnn/operations/arithmetic/multiply/multiply.hpp>
#include <ttnn/operations/arithmetic/divide/divide.hpp>
#include <ttnn/operations/arithmetic/subtract/subtract.hpp>
#include <ttnn/operations/shape/get_shape.hpp>


#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/ops/binary.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"

namespace tt_eager::ops::binary {

// --- ADD (out) ---
at::Tensor& ttnn_add_out(
    const at::Tensor& input,
    const at::Tensor& other,
    const at::Scalar& /*alpha*/,
    at::Tensor& out)
{
    LOGGING("Running aten::add.out");
    TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(other.device().type() == c10::DeviceType::PrivateUse1);

    auto t0 = static_cast<at::TtnnTensorImpl*>(input.unsafeGetTensorImpl())->get_ttnn_tensor();
    auto t1 = static_cast<at::TtnnTensorImpl*>(other.unsafeGetTensorImpl())->get_ttnn_tensor();

    // normalize to TILE layout
    if (t0.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        t0 = ttnn::to_layout(t0, ttnn::TILE_LAYOUT);
    }
    if (t1.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        t1 = ttnn::to_layout(t1, ttnn::TILE_LAYOUT);
    }

    auto result = ttnn::add(t0, t1);

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(out.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(input);
    out_impl->set_ttnn_tensor(result);
    return out;
}

// --- ADD (new tensor) ---
at::Tensor ttnn_add_tensor(
    const at::Tensor& input,
    const at::Tensor& other,
    const at::Scalar& alpha)
{
    LOGGING("Running aten::add.Tensor");
    auto output = tt_eager::ops::create::custom_empty_memory_format(
        input.sizes(),
        input.scalar_type(),
        c10::nullopt,
        input.device(),
        c10::nullopt);
    return ttnn_add_out(input, other, alpha, output);
}

// --- ADDMM ---
at::Tensor ttnn_addmm(
    const at::Tensor& self,
    const at::Tensor& mat1,
    const at::Tensor& mat2,
    const at::Scalar& beta,
    const at::Scalar& alpha)
{
    LOGGING("Running aten::addmm.default");
    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(mat1.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(mat2.device().type() == c10::DeviceType::PrivateUse1);

    auto t_self = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl())->get_ttnn_tensor();
    auto t_mat1 = static_cast<at::TtnnTensorImpl*>(mat1.unsafeGetTensorImpl())->get_ttnn_tensor();
    auto t_mat2 = static_cast<at::TtnnTensorImpl*>(mat2.unsafeGetTensorImpl())->get_ttnn_tensor();

    if (t_mat1.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        t_mat1 = ttnn::to_layout(t_mat1, ttnn::TILE_LAYOUT);
    }
    if (t_mat2.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        t_mat2 = ttnn::to_layout(t_mat2, ttnn::TILE_LAYOUT);
    }

    auto t_res = ttnn::matmul(t_mat1, t_mat2);

    if (alpha.toDouble() != 1.0) {
        auto alpha_t = ttnn::operations::full::Full::invoke(
            ttnn::operations::shape::GetShape::invoke(t_res),
            alpha.toDouble(),
            t_res,
            t_res.dtype(),
            t_res.layout(),
            std::nullopt);
        t_res = ttnn::operations::arithmetic::Multiply::invoke(t_res, alpha_t);
    }
    if (beta.toDouble() != 1.0) {
        auto beta_t = ttnn::operations::full::Full::invoke(
            ttnn::operations::shape::GetShape::invoke(t_self),
            beta.toDouble(),
            t_self,
            t_self.dtype(),
            t_self.layout(),
            std::nullopt);
        t_self = ttnn::operations::arithmetic::Multiply::invoke(t_self, beta_t);
    }

    auto result = ttnn::add(t_self, t_res);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        self.sizes(),
        self.scalar_type(),
        c10::nullopt,
        self.device(),
        c10::nullopt);
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(self);
    out_impl->set_ttnn_tensor(result);
    return output;
}

// --- BMM ---
at::Tensor ttnn_bmm(
    const at::Tensor& batch1,
    const at::Tensor& batch2)
{
    LOGGING("Running aten::bmm");
    TORCH_CHECK(batch1.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(batch2.device().type() == c10::DeviceType::PrivateUse1);

    auto t0 = static_cast<at::TtnnTensorImpl*>(batch1.unsafeGetTensorImpl())->get_ttnn_tensor();
    auto t1 = static_cast<at::TtnnTensorImpl*>(batch2.unsafeGetTensorImpl())->get_ttnn_tensor();

    if (t0.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        t0 = ttnn::to_layout(t0, ttnn::TILE_LAYOUT);
    }
    if (t1.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        t1 = ttnn::to_layout(t1, ttnn::TILE_LAYOUT);
    }

    auto result = ttnn::matmul(t0, t1);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        batch1.sizes(),
        batch1.scalar_type(),
        c10::nullopt,
        batch1.device(),
        c10::nullopt);
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(batch1);
    out_impl->set_ttnn_tensor(result);
    return output;
}

// --- MUL ---
at::Tensor ttnn_mul_tensor(
    const at::Tensor& input,
    const at::Tensor& other)
{
    LOGGING("Running aten::mul.Tensor");
    TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(other.device().type() == c10::DeviceType::PrivateUse1);

    auto t0 = static_cast<at::TtnnTensorImpl*>(input.unsafeGetTensorImpl())->get_ttnn_tensor();
    auto t1 = static_cast<at::TtnnTensorImpl*>(other.unsafeGetTensorImpl())->get_ttnn_tensor();

    if (t0.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        t0 = ttnn::to_layout(t0, ttnn::TILE_LAYOUT);
    }
    if (t1.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        t1 = ttnn::to_layout(t1, ttnn::TILE_LAYOUT);
    }

    auto result = ttnn::operations::arithmetic::Multiply::invoke(t0, t1);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        input.sizes(),
        input.scalar_type(),
        c10::nullopt,
        input.device(),
        c10::nullopt);
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(input);
    out_impl->set_ttnn_tensor(result);
    return output;
}

// --- DIV ---
at::Tensor ttnn_div_tensor(
    const at::Tensor& input,
    const at::Tensor& other)
{
    LOGGING("Running aten::div.Tensor");
    TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(other.device().type() == c10::DeviceType::PrivateUse1);

    auto t0 = static_cast<at::TtnnTensorImpl*>(input.unsafeGetTensorImpl())->get_ttnn_tensor();
    auto t1 = static_cast<at::TtnnTensorImpl*>(other.unsafeGetTensorImpl())->get_ttnn_tensor();

    if (t0.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        t0 = ttnn::to_layout(t0, ttnn::TILE_LAYOUT);
    }
    if (t1.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        t1 = ttnn::to_layout(t1, ttnn::TILE_LAYOUT);
    }

    auto result = ttnn::operations::arithmetic::Divide::invoke(t0, t1);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        input.sizes(),
        input.scalar_type(),
        c10::nullopt,
        input.device(),
        c10::nullopt);
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(input);
    out_impl->set_ttnn_tensor(result);
    return output;
}

// --- RSUB ---
at::Tensor ttnn_rsub_scalar(
    const at::Tensor& self,
    const at::Scalar& other,
    const at::Scalar& alpha)
{
    LOGGING("Running aten::rsub.Scalar");
    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);

    auto t0 = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl())->get_ttnn_tensor();

    if (alpha.toDouble() != 1.0) {
        auto a_t = ttnn::operations::full::Full::invoke(
            ttnn::operations::shape::GetShape::invoke(t0),
            alpha.toDouble(),
            t0,
            t0.dtype(),
            t0.layout(),
            std::nullopt);
        t0 = ttnn::operations::arithmetic::Multiply::invoke(t0, a_t);
    }

    auto o_t = ttnn::operations::full::Full::invoke(
        ttnn::operations::shape::GetShape::invoke(t0),
        other.toDouble(),
        t0,
        t0.dtype(),
        t0.layout(),
        std::nullopt);

    auto result = ttnn::operations::arithmetic::Subtract::invoke(o_t, t0);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        self.sizes(),
        self.scalar_type(),
        c10::nullopt,
        self.device(),
        c10::nullopt);
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(self);
    out_impl->set_ttnn_tensor(result);
    return output;
}

}  // namespace tt_eager::ops::binary

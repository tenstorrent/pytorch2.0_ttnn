// src/ops/binary.cpp

#include "ttnn_cpp_extension/ops/binary.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"

#include <ttnn/operations/eltwise/binary/binary.hpp>  // brings in ttnn::add, multiply, etc.
#include <ttnn/operations/matmul/matmul.hpp>          // brings in ttnn::matmul
#include <ttnn/tensor/types.hpp>                      // for DataType, Layout

namespace tt_eager::ops::binary {

// Ensure we’re in TILE_LAYOUT before doing TT-NN ops:
static ttnn::Tensor ensure_tile(ttnn::Tensor t) {
    if (t.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        t = ttnn::to_layout(
            t,
            ttnn::TILE_LAYOUT,
            /*queue_id=*/std::nullopt,
            /*kernel_cfg=*/std::nullopt,
            t.device()
        );
    }
    return t;
}

at::Tensor& ttnn_add_out(
    const at::Tensor& input,
    const at::Tensor& other,
    const at::Scalar& alpha,
    at::Tensor& out
) {
    LOGGING("Running aten::add.out");
    TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(other.device().type() == c10::DeviceType::PrivateUse1);

    // unwrap our ATen→TT-NN tensors
    auto* impl0 = static_cast<at::TtnnTensorImpl*>(input.unsafeGetTensorImpl());
    auto* impl1 = static_cast<at::TtnnTensorImpl*>(other.unsafeGetTensorImpl());
    ttnn::Tensor t0 = ensure_tile(impl0->get_ttnn_tensor());
    ttnn::Tensor t1 = ensure_tile(impl1->get_ttnn_tensor());

    // alpha * t1
    if (alpha.toDouble() != 1.0) {
        t1 = ttnn::multiply(t1, static_cast<float>(alpha.toDouble()));
    }

    // add
    auto result = ttnn::add(t0, t1);

    // write back into `out`
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(out.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(input);
    out_impl->set_ttnn_tensor(result);
    return out;
}

at::Tensor ttnn_add_tensor(
    const at::Tensor& input,
    const at::Tensor& other,
    const at::Scalar& alpha
) {
    LOGGING("Running aten::add.Tensor");
    auto output = tt_eager::ops::create::custom_empty_memory_format(
        input.sizes(),
        input.scalar_type(),
        /*strides=*/c10::nullopt,
        /*device=*/input.device(),
        /*pin_memory=*/c10::nullopt
    );
    return ttnn_add_out(input, other, alpha, output);
}

at::Tensor ttnn_addmm(
    const at::Tensor& self,
    const at::Tensor& mat1,
    const at::Tensor& mat2,
    const at::Scalar& beta,
    const at::Scalar& alpha
) {
    LOGGING("Running aten::addmm");
    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(mat1.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(mat2.device().type() == c10::DeviceType::PrivateUse1);

    auto* impl_self = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto* impl1     = static_cast<at::TtnnTensorImpl*>(mat1.unsafeGetTensorImpl());
    auto* impl2     = static_cast<at::TtnnTensorImpl*>(mat2.unsafeGetTensorImpl());
    ttnn::Tensor t_self = impl_self->get_ttnn_tensor();
    ttnn::Tensor t1     = ensure_tile(impl1->get_ttnn_tensor());
    ttnn::Tensor t2     = ensure_tile(impl2->get_ttnn_tensor());

    // matmul
    auto t_res = ttnn::matmul(t1, t2);

    // scale by alpha
    if (alpha.toDouble() != 1.0) {
        t_res = ttnn::multiply(t_res, static_cast<float>(alpha.toDouble()));
    }

    // scale self by beta
    if (beta.toDouble() != 1.0) {
        t_self = ttnn::multiply(t_self, static_cast<float>(beta.toDouble()));
    }

    // add them
    auto result = ttnn::add(t_self, t_res);

    // make and return a fresh ATen tensor
    auto output = tt_eager::ops::create::custom_empty_memory_format(
        self.sizes(),
        self.scalar_type(),
        /*strides=*/c10::nullopt,
        /*device=*/self.device(),
        /*pin_memory=*/c10::nullopt
    );
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(self);
    out_impl->set_ttnn_tensor(result);
    return output;
}

at::Tensor ttnn_bmm(
    const at::Tensor& batch1,
    const at::Tensor& batch2
) {
    LOGGING("Running aten::bmm");
    TORCH_CHECK(batch1.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(batch2.device().type() == c10::DeviceType::PrivateUse1);

    auto* impl0 = static_cast<at::TtnnTensorImpl*>(batch1.unsafeGetTensorImpl());
    auto* impl1 = static_cast<at::TtnnTensorImpl*>(batch2.unsafeGetTensorImpl());
    ttnn::Tensor t0 = ensure_tile(impl0->get_ttnn_tensor());
    ttnn::Tensor t1 = ensure_tile(impl1->get_ttnn_tensor());

    auto result = ttnn::matmul(t0, t1);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        batch1.sizes(),
        batch1.scalar_type(),
        /*strides=*/c10::nullopt,
        /*device=*/batch1.device(),
        /*pin_memory=*/c10::nullopt
    );
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(batch1);
    out_impl->set_ttnn_tensor(result);
    return output;
}

at::Tensor ttnn_mul_tensor(
    const at::Tensor& input,
    const at::Tensor& other
) {
    LOGGING("Running aten::mul.Tensor");
    TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(other.device().type() == c10::DeviceType::PrivateUse1);

    auto* impl0 = static_cast<at::TtnnTensorImpl*>(input.unsafeGetTensorImpl());
    auto* impl1 = static_cast<at::TtnnTensorImpl*>(other.unsafeGetTensorImpl());
    ttnn::Tensor t0 = ensure_tile(impl0->get_ttnn_tensor());
    ttnn::Tensor t1 = ensure_tile(impl1->get_ttnn_tensor());

    auto result = ttnn::multiply(t0, t1);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        input.sizes(),
        input.scalar_type(),
        /*strides=*/c10::nullopt,
        /*device=*/input.device(),
        /*pin_memory=*/c10::nullopt
    );
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(input);
    out_impl->set_ttnn_tensor(result);
    return output;
}

at::Tensor ttnn_div_tensor(
    const at::Tensor& input,
    const at::Tensor& other
) {
    LOGGING("Running aten::div.Tensor");
    TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(other.device().type() == c10::DeviceType::PrivateUse1);

    auto* impl0 = static_cast<at::TtnnTensorImpl*>(input.unsafeGetTensorImpl());
    auto* impl1 = static_cast<at::TtnnTensorImpl*>(other.unsafeGetTensorImpl());
    ttnn::Tensor t0 = ensure_tile(impl0->get_ttnn_tensor());
    ttnn::Tensor t1 = ensure_tile(impl1->get_ttnn_tensor());

    auto result = ttnn::divide(t0, t1);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        input.sizes(),
        input.scalar_type(),
        /*strides=*/c10::nullopt,
        /*device=*/input.device(),
        /*pin_memory=*/c10::nullopt
    );
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(input);
    out_impl->set_ttnn_tensor(result);
    return output;
}

at::Tensor ttnn_rsub_scalar(
    const at::Tensor& self,
    const at::Scalar& other,
    const at::Scalar& alpha
) {
    LOGGING("Running aten::rsub.Scalar");
    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);

    auto* impl0 = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    ttnn::Tensor t0 = impl0->get_ttnn_tensor();

    // alpha * t0
    if (alpha.toDouble() != 1.0) {
        t0 = ttnn::multiply(t0, static_cast<float>(alpha.toDouble()));
    }

    // other - t0  ===  (-t0) + other
    auto neg_t0 = ttnn::multiply(t0, -1.f);
    auto result = ttnn::add(neg_t0, static_cast<float>(other.toDouble()));

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        self.sizes(),
        self.scalar_type(),
        /*strides=*/c10::nullopt,
        /*device=*/self.device(),
        /*pin_memory=*/c10::nullopt
    );
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(self);
    out_impl->set_ttnn_tensor(result);
    return output;
}

}  // namespace tt_eager::ops::binary

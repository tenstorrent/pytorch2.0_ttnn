#include "ttnn_cpp_extension/ops/binary.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"

#include <torch/torch.h>
#include <ttnn/operations/eltwise/binary/binary.hpp>
#include <ttnn/operations/matmul/matmul.hpp>
#include <ttnn/tensor/types.hpp>

namespace tt_eager::ops::binary {

static ttnn::Tensor ensure_tile(ttnn::Tensor t) {
    if (t.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        t = ttnn::to_layout(
            t,
            ttnn::TILE_LAYOUT,
            /*queue_id=*/std::nullopt,
            /*kernel_cfg=*/std::nullopt,
            t.device());
    }
    return t;
}

at::Tensor& ttnn_add_out(const at::Tensor& input, const at::Tensor& other, const at::Scalar& alpha, at::Tensor& out) {
    LOGGING("Running aten::add.out");
    TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1);

    if (other.device().type() != c10::DeviceType::PrivateUse1) {
        LOGGING("Other tensor not on TTNN device, using _to_copy to transfer");
        auto other_ttnn = other.to(input.device(), /*non_blocking=*/false);
        return ttnn_add_out(input, other_ttnn, alpha, out);
    }

    auto* impl0 = static_cast<at::TtnnTensorImpl*>(input.unsafeGetTensorImpl());
    auto* impl1 = static_cast<at::TtnnTensorImpl*>(other.unsafeGetTensorImpl());
    ttnn::Tensor t0 = ensure_tile(impl0->get_ttnn_tensor());
    ttnn::Tensor t1 = ensure_tile(impl1->get_ttnn_tensor());

    if (alpha.toDouble() != 1.0) {
        t1 = ttnn::multiply(t1, static_cast<float>(alpha.toDouble()));
    }

    auto result = ttnn::add(t0, t1);

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(out.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(input);
    out_impl->set_ttnn_tensor(result);
    return out;
}

at::Tensor ttnn_add_tensor(const at::Tensor& input, const at::Tensor& other, const at::Scalar& alpha) {
    LOGGING("Running aten::add.Tensor");
    auto output = tt_eager::ops::create::custom_empty_memory_format(
        input.sizes(),
        input.scalar_type(),
        /*strides=*/c10::nullopt,
        /*device=*/input.device(),
        /*pin_memory=*/c10::nullopt);
    return ttnn_add_out(input, other, alpha, output);
}

at::Tensor ttnn_mul_tensor(const at::Tensor& input, const at::Tensor& other) {
    LOGGING("Running aten::mul.Tensor");
    LOGGING("Input device type: ", static_cast<int>(input.device().type()));
    LOGGING("Other device type: ", static_cast<int>(other.device().type()));

    TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1);

    if (other.device().type() != c10::DeviceType::PrivateUse1) {
        LOGGING("Other tensor not on TTNN device, using _to_copy to transfer");
        auto other_ttnn = other.to(input.device(), /*non_blocking=*/false);
        return ttnn_mul_tensor(input, other_ttnn);
    }

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
        /*pin_memory=*/c10::nullopt);
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(input);
    out_impl->set_ttnn_tensor(result);
    return output;
}

at::Tensor ttnn_div_tensor(const at::Tensor& self, const at::Tensor& other) {
    if (other.dim() == 0) {
        TORCH_CHECK(
            self.device().type() == c10::DeviceType::PrivateUse1, "ttnn_div_tensor requires TTNN backend for tensor");

        auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
        auto ttnn_self = ensure_tile(self_impl->get_ttnn_tensor());

        float scalar_value = other.item<float>();

        auto ttnn_result = ttnn::multiply(ttnn_self, 1.0f / scalar_value);

        auto output = tt_eager::ops::create::custom_empty_memory_format(
            self.sizes().vec(), self.scalar_type(), c10::nullopt, self.device(), c10::nullopt);
        auto* output_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
        output_impl->set_ttnn_tensor(ttnn_result);

        return output;
    }

    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1, "ttnn_div_tensor requires TTNN backend");
    TORCH_CHECK(other.device().type() == c10::DeviceType::PrivateUse1, "ttnn_div_tensor requires TTNN backend");

    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto* other_impl = static_cast<at::TtnnTensorImpl*>(other.unsafeGetTensorImpl());

    auto ttnn_self = ensure_tile(self_impl->get_ttnn_tensor());
    auto ttnn_other = ensure_tile(other_impl->get_ttnn_tensor());

    auto ttnn_result = ttnn::divide(ttnn_self, ttnn_other);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        self.sizes().vec(), self.scalar_type(), c10::nullopt, self.device(), c10::nullopt);
    auto* output_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    output_impl->set_ttnn_tensor(ttnn_result);

    return output;
}

at::Tensor ttnn_rsub_scalar(const at::Tensor& self, const at::Scalar& other, const at::Scalar& alpha) {
    LOGGING("Running aten::rsub.Scalar");
    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);

    auto* impl0 = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    ttnn::Tensor t0 = ensure_tile(impl0->get_ttnn_tensor());

    if (alpha.toDouble() != 1.0) {
        t0 = ttnn::multiply(t0, static_cast<float>(alpha.toDouble()));
    }

    auto neg_t0 = ttnn::multiply(t0, -1.f);
    auto result = ttnn::add(neg_t0, static_cast<float>(other.toDouble()));

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        self.sizes(),
        self.scalar_type(),
        /*strides=*/c10::nullopt,
        /*device=*/self.device(),
        /*pin_memory=*/c10::nullopt);
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(self);
    out_impl->set_ttnn_tensor(result);
    return output;
}

at::Tensor ttnn_rsub_tensor(const at::Tensor& self, const at::Tensor& other, const at::Scalar& alpha) {
    LOGGING("Running aten::rsub.Tensor");
    LOGGING("Self device type: ", static_cast<int>(self.device().type()));
    LOGGING("Other device type: ", static_cast<int>(other.device().type()));

    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);

    if (other.device().type() != c10::DeviceType::PrivateUse1) {
        LOGGING("Other tensor not on TTNN device, using _to_copy to transfer");
        auto other_ttnn = other.to(self.device(), /*non_blocking=*/false);
        return ttnn_rsub_tensor(self, other_ttnn, alpha);
    }

    auto* impl0 = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto* impl1 = static_cast<at::TtnnTensorImpl*>(other.unsafeGetTensorImpl());
    ttnn::Tensor t0 = ensure_tile(impl0->get_ttnn_tensor());
    ttnn::Tensor t1 = ensure_tile(impl1->get_ttnn_tensor());

    if (alpha.toDouble() != 1.0) {
        t0 = ttnn::multiply(t0, static_cast<float>(alpha.toDouble()));
    }
    auto neg_t0 = ttnn::multiply(t0, -1.f);
    auto result = ttnn::add(neg_t0, t1);

    at::Tensor output = tt_eager::ops::create::custom_empty_memory_format(
        self.sizes(),
        self.scalar_type(),
        /*strides=*/c10::nullopt,
        /*device=*/self.device(),
        /*pin_memory=*/c10::nullopt);
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(self);
    out_impl->set_ttnn_tensor(result);
    return output;
}

at::Tensor ttnn_sub_tensor(const at::Tensor& input, const at::Tensor& other, const at::Scalar& alpha) {
    LOGGING("Running aten::sub.Tensor");
    LOGGING("Input device type: ", static_cast<int>(input.device().type()));
    LOGGING("Other device type: ", static_cast<int>(other.device().type()));

    TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1);

    if (other.device().type() != c10::DeviceType::PrivateUse1) {
        LOGGING("Other tensor not on TTNN device, using _to_copy to transfer");
        auto other_ttnn = other.to(input.device(), /*non_blocking=*/false);
        return ttnn_sub_tensor(input, other_ttnn, alpha);
    }

    auto* impl0 = static_cast<at::TtnnTensorImpl*>(input.unsafeGetTensorImpl());
    auto* impl1 = static_cast<at::TtnnTensorImpl*>(other.unsafeGetTensorImpl());
    ttnn::Tensor t0 = ensure_tile(impl0->get_ttnn_tensor());
    ttnn::Tensor t1 = ensure_tile(impl1->get_ttnn_tensor());

    float a = static_cast<float>(alpha.toDouble());
    if (a != 1.0f) {
        t1 = ttnn::multiply(t1, a);
    }

    auto neg_t1 = ttnn::multiply(t1, -1.0f);
    auto result = ttnn::add(t0, neg_t1);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        input.sizes(),
        input.scalar_type(),
        /*strides=*/c10::nullopt,
        /*device=*/input.device(),
        /*pin_memory=*/c10::nullopt);
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(input);
    out_impl->set_ttnn_tensor(result);
    return output;
}

at::Tensor ttnn_sub_scalar(const at::Tensor& self, const at::Scalar& other, const at::Scalar& alpha) {
    LOGGING("Running aten::sub.Scalar");
    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);

    auto* impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    ttnn::Tensor t0 = ensure_tile(impl->get_ttnn_tensor());

    float o = static_cast<float>(other.toDouble());
    float a = static_cast<float>(alpha.toDouble());
    float sub_val = o * a;

    auto result = ttnn::add(t0, -sub_val);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        self.sizes(),
        self.scalar_type(),
        /*strides=*/c10::nullopt,
        /*device=*/self.device(),
        /*pin_memory=*/c10::nullopt);
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(self);
    out_impl->set_ttnn_tensor(result);
    return output;
}
}  // namespace tt_eager::ops::binary

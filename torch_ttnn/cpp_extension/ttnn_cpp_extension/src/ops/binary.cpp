#include <c10/util/Optional.h>
#include <ttnn/operations/matmul/matmul.hpp>
#include <ttnn/operations/eltwise/binary/binary.hpp>
#include <ttnn/operations/full/full.hpp>  

#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/ops/binary.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"


namespace tt_eager::ops::binary {
at::Tensor& ttnn_add_out(const at::Tensor& input, const at::Tensor& other, const at::Scalar& alpha, at::Tensor& out) {
    LOGGING("input device: {}, other device: {}", input.device(), other.device());
    TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(other.device().type() == c10::DeviceType::PrivateUse1);

    at::TtnnTensorImpl* tensor_impl = static_cast<at::TtnnTensorImpl*>(input.unsafeGetTensorImpl());
    auto ttnn_tensor_input = tensor_impl->get_ttnn_tensor();
    if (ttnn_tensor_input.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_tensor_input = ttnn::to_layout(
            ttnn_tensor_input, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_tensor_input.device());
    }

    at::TtnnTensorImpl* other_tensor_impl = static_cast<at::TtnnTensorImpl*>(other.unsafeGetTensorImpl());

    auto ttnn_tensor_other = other_tensor_impl->get_ttnn_tensor();
    if (ttnn_tensor_other.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_tensor_other = ttnn::to_layout(
            ttnn_tensor_other, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_tensor_other.device());
    }

    auto result = ttnn::add(ttnn_tensor_input, ttnn_tensor_other);

    // tensor_impl->set_ttnn_tensor(result);
    // Get underlying TTNN tensor object from output
    at::TtnnTensorImpl* out_tensor_impl = static_cast<at::TtnnTensorImpl*>(out.unsafeGetTensorImpl());
    out_tensor_impl->set_sizes_and_strides_as(input);

    // Set output TTNN tensor to result
    auto out_ttnn_tensor = out_tensor_impl->get_ttnn_tensor();
    out_tensor_impl->set_ttnn_tensor(result);
    return out;
}

// Add this function to your open_registration_extension.cpp
at::Tensor ttnn_add_tensor(const at::Tensor& input, const at::Tensor& other, const at::Scalar& alpha) {
    LOGGING("Creating new output tensor");
    // Create a new output tensor on the right device
    // auto output = at::empty(input.sizes(), input.options());
    auto output = tt_eager::ops::create::custom_empty_memory_format(
        input.sizes(),
        c10::optional<at::ScalarType>(input.scalar_type()),
        c10::nullopt,  // layout
        c10::optional<at::Device>(input.device()),
        c10::nullopt  // pin_memory
    );

    // Call the existing out version
    return ttnn_add_out(input, other, alpha, output);
}
}  // namespace tt_eager::ops::binary

at::Tensor ttnn_addmm(const at::Tensor& self, const at::Tensor& mat1, const at::Tensor& mat2, const at::Scalar& beta, const at::Scalar& alpha) {
    LOGGING("Running aten::addmm on TTNN device");

    // Check devices
    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(mat1.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(mat2.device().type() == c10::DeviceType::PrivateUse1);

    // Extract TTNN tensors
    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto* mat1_impl = static_cast<at::TtnnTensorImpl*>(mat1.unsafeGetTensorImpl());
    auto* mat2_impl = static_cast<at::TtnnTensorImpl*>(mat2.unsafeGetTensorImpl());

    auto ttnn_self = self_impl->get_ttnn_tensor();
    auto ttnn_mat1 = mat1_impl->get_ttnn_tensor();
    auto ttnn_mat2 = mat2_impl->get_ttnn_tensor();

    // Ensure TILE_LAYOUT
    if (ttnn_mat1.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_mat1 = ttnn::to_layout(ttnn_mat1, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_mat1.device());
    }
    if (ttnn_mat2.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_mat2 = ttnn::to_layout(ttnn_mat2, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_mat2.device());
    }
    if (ttnn_self.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_self = ttnn::to_layout(ttnn_self, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_self.device());
    }

    // Perform matmul
    auto ttnn_matmul = ttnn::matmul(ttnn_mat1, ttnn_mat2);

    // Apply alpha scaling if alpha != 1
    if (!alpha.isEqualTo(1.0)) {
        auto ttnn_alpha = ttnn::from_scalar(alpha.toDouble(), ttnn_matmul.shape(), ttnn_matmul.dtype(), ttnn_matmul.device());
        ttnn_matmul = ttnn::mul(ttnn_matmul, ttnn_alpha);
    }

    // Apply beta scaling if beta != 1
    if (!beta.isEqualTo(1.0)) {
        auto ttnn_beta = ttnn::from_scalar(beta.toDouble(), ttnn_self.shape(), ttnn_self.dtype(), ttnn_self.device());
        ttnn_self = ttnn::mul(ttnn_self, ttnn_beta);
    }

    // Final addition
    auto ttnn_result = ttnn::add(ttnn_self, ttnn_matmul);

    // Create output tensor
    auto output = tt_eager::ops::create::custom_empty_memory_format(
        self.sizes(),
        c10::optional<at::ScalarType>(self.scalar_type()),
        c10::nullopt,
        c10::optional<at::Device>(self.device()),
        c10::nullopt
    );

    auto* output_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    output_impl->set_sizes_and_strides_as(self);
    output_impl->set_ttnn_tensor(ttnn_result);

    return output;
}

at::Tensor ttnn_bmm(const at::Tensor& batch1, const at::Tensor& batch2) {
    LOGGING("Running aten::bmm.default on TTNN device");

    // Check device
    TORCH_CHECK(batch1.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(batch2.device().type() == c10::DeviceType::PrivateUse1);

    // Get TTNN tensors
    auto* batch1_impl = static_cast<at::TtnnTensorImpl*>(batch1.unsafeGetTensorImpl());
    auto* batch2_impl = static_cast<at::TtnnTensorImpl*>(batch2.unsafeGetTensorImpl());

    auto ttnn_batch1 = batch1_impl->get_ttnn_tensor();
    auto ttnn_batch2 = batch2_impl->get_ttnn_tensor();

    // Convert to TILE_LAYOUT if needed
    if (ttnn_batch1.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_batch1 = ttnn::to_layout(ttnn_batch1, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_batch1.device());
    }
    if (ttnn_batch2.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_batch2 = ttnn::to_layout(ttnn_batch2, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_batch2.device());
    }

    // Perform bmm
    auto ttnn_result = ttnn::bmm(ttnn_batch1, ttnn_batch2);

    // Create output tensor
    auto output = tt_eager::ops::create::custom_empty_memory_format(
        batch1.sizes(), // size will be overwritten to match result
        c10::optional<at::ScalarType>(batch1.scalar_type()),
        c10::nullopt,
        c10::optional<at::Device>(batch1.device()),
        c10::nullopt
    );

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(batch1); // fallback; real shape comes from TTNN tensor
    out_impl->set_ttnn_tensor(ttnn_result);

    return output;
}

at::Tensor ttnn_div_tensor(const at::Tensor& input, const at::Tensor& other) {
    LOGGING("Running aten::div.Tensor");

    // Device checks
    TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(other.device().type() == c10::DeviceType::PrivateUse1);

    // Unwrap TTNN tensors
    auto* input_impl = static_cast<at::TtnnTensorImpl*>(input.unsafeGetTensorImpl());
    auto* other_impl = static_cast<at::TtnnTensorImpl*>(other.unsafeGetTensorImpl());

    auto ttnn_input = input_impl->get_ttnn_tensor();
    auto ttnn_other = other_impl->get_ttnn_tensor();

    // Ensure TILE_LAYOUT
    if (ttnn_input.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_input = ttnn::to_layout(ttnn_input, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_input.device());
    }
    if (ttnn_other.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_other = ttnn::to_layout(ttnn_other, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_other.device());
    }

    // Perform elementwise division
    auto ttnn_result = ttnn::div(ttnn_input, ttnn_other);

    // Create and wrap result
    auto output = tt_eager::ops::create::custom_empty_memory_format(
        input.sizes(),
        c10::optional<at::ScalarType>(input.scalar_type()),
        c10::nullopt,
        c10::optional<at::Device>(input.device()),
        c10::nullopt
    );

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(input);
    out_impl->set_ttnn_tensor(ttnn_result);

    return output;
}

at::Tensor ttnn_mul_tensor(const at::Tensor& input, const at::Tensor& other) {
    LOGGING("Running aten::mul.Tensor");

    TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(other.device().type() == c10::DeviceType::PrivateUse1);

    auto* input_impl = static_cast<at::TtnnTensorImpl*>(input.unsafeGetTensorImpl());
    auto* other_impl = static_cast<at::TtnnTensorImpl*>(other.unsafeGetTensorImpl());

    auto ttnn_input = input_impl->get_ttnn_tensor();
    auto ttnn_other = other_impl->get_ttnn_tensor();

    if (ttnn_input.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_input = ttnn::to_layout(ttnn_input, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_input.device());
    }
    if (ttnn_other.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_other = ttnn::to_layout(ttnn_other, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_other.device());
    }

    auto ttnn_result = ttnn::mul(ttnn_input, ttnn_other);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        input.sizes(),
        c10::optional<at::ScalarType>(input.scalar_type()),
        c10::nullopt,
        c10::optional<at::Device>(input.device()),
        c10::nullopt
    );

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(input);
    out_impl->set_ttnn_tensor(ttnn_result);

    return output;
}

at::Tensor ttnn_rsub_scalar(const at::Tensor& self, const at::Scalar& other, const at::Scalar& alpha) {
    LOGGING("Running aten::rsub.Scalar");

    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);

    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_self = self_impl->get_ttnn_tensor();

    if (ttnn_self.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_self = ttnn::to_layout(ttnn_self, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_self.device());
    }

    // Compute alpha * self
    ttnn::Tensor scaled_self = ttnn_self;
    if (!alpha.isEqualTo(1.0)) {
        auto alpha_tensor = ttnn::full(
            ttnn_self.shape(),
            alpha.to<double>(),
            ttnn_self.dtype(),
            ttnn::TILE_LAYOUT,
            ttnn_self.device(),
            ttnn::MemoryConfig{ttnn::TensorMemoryLayout::INTERLEAVED, ttnn::BufferType::DRAM, std::nullopt}
        );
        scaled_self = ttnn::mul(ttnn_self, alpha_tensor);
    }

    // Compute other - scaled_self
    auto other_tensor = ttnn::full(
        scaled_self.shape(),
        other.to<double>(),
        scaled_self.dtype(),
        ttnn::TILE_LAYOUT,
        scaled_self.device(),
        ttnn::MemoryConfig{ttnn::TensorMemoryLayout::INTERLEAVED, ttnn::BufferType::DRAM, std::nullopt}
    );

    auto result_tensor = ttnn::sub(other_tensor, scaled_self);  // reversed subtraction

    // Wrap output
    auto output = tt_eager::ops::create::custom_empty_memory_format(
        self.sizes(),
        self.scalar_type(),
        c10::nullopt,
        self.device(),
        c10::nullopt
    );

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(self);
    out_impl->set_ttnn_tensor(result_tensor);

    return output;
}
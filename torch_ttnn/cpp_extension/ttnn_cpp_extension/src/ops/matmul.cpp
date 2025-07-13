#include "ttnn_cpp_extension/ops/matmul.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"

#include <vector>
#include <iostream>

#include <ttnn/operations/matmul/matmul.hpp>

namespace tt_eager::ops::matmul {

    // Ensure we're in TILE_LAYOUT before doing TT-NN ops:
    static ttnn::Tensor ensure_tile(ttnn::Tensor t) {
        if (t.layout() == ttnn::ROW_MAJOR_LAYOUT) {
            t = ttnn::to_layout(
                t,
                ttnn::TILE_LAYOUT,
                std::nullopt,
                std::nullopt,
                t.device());
        }
        return t;
    }

    at::Tensor ttnn_matmul(const at::Tensor& self, const at::Tensor& other) {
        std::cout << "[DEBUG] ttnn_matmul called" << std::endl;
        
        TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1,
                    "ttnn_matmul requires TTNN backend for self tensor");
        TORCH_CHECK(other.device().type() == c10::DeviceType::PrivateUse1,
                    "ttnn_matmul requires TTNN backend for other tensor");

        // Print input tensor info
        std::cout << "[DEBUG] self tensor shape: [";
        for (int i = 0; i < self.dim(); i++) {
            std::cout << self.size(i);
            if (i < self.dim() - 1) std::cout << ", ";
        }
        std::cout << "], other tensor shape: [";
        for (int i = 0; i < other.dim(); i++) {
            std::cout << other.size(i);
            if (i < other.dim() - 1) std::cout << ", ";
        }
        std::cout << "]" << std::endl;

        auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
        auto* other_impl = static_cast<at::TtnnTensorImpl*>(other.unsafeGetTensorImpl());
        
        auto ttnn_self = ensure_tile(self_impl->get_ttnn_tensor());
        auto ttnn_other = ensure_tile(other_impl->get_ttnn_tensor());

        // Debug TTNN tensor shapes
        auto ttnn_self_shape = ttnn_self.logical_shape();
        auto ttnn_other_shape = ttnn_other.logical_shape();
        std::cout << "[DEBUG] ttnn_self.shape = [";
        for (int i = 0; i < ttnn_self_shape.rank(); i++) {
            std::cout << ttnn_self_shape[i];
            if (i < ttnn_self_shape.rank() - 1) std::cout << ", ";
        }
        std::cout << "], ttnn_other.shape = [";
        for (int i = 0; i < ttnn_other_shape.rank(); i++) {
            std::cout << ttnn_other_shape[i];
            if (i < ttnn_other_shape.rank() - 1) std::cout << ", ";
        }
        std::cout << "]" << std::endl;

        // Perform matrix multiplication
        auto ttnn_result = ttnn::matmul(ttnn_self, ttnn_other);

        // Debug output shape
        auto ttnn_result_shape = ttnn_result.logical_shape();
        std::cout << "[DEBUG] ttnn_result.shape = [";
        for (int i = 0; i < ttnn_result_shape.rank(); i++) {
            std::cout << ttnn_result_shape[i];
            if (i < ttnn_result_shape.rank() - 1) std::cout << ", ";
        }
        std::cout << "]" << std::endl;

        // Calculate output shape based on matrix multiplication rules
        std::vector<int64_t> output_shape;
        auto self_shape = self.sizes();
        auto other_shape = other.sizes();
        
        // For batched matrix multiplication
        if (self.dim() > 2 && other.dim() > 2) {
            // Batch dimensions should match or be broadcastable
            int64_t batch_dims = std::max(self.dim(), other.dim()) - 2;
            for (int i = 0; i < batch_dims; i++) {
                int64_t self_dim = (i < self.dim() - 2) ? self_shape[i] : 1;
                int64_t other_dim = (i < other.dim() - 2) ? other_shape[i] : 1;
                output_shape.push_back(std::max(self_dim, other_dim));
            }
        }
        
        // Matrix dimensions
        output_shape.push_back(self_shape[self.dim() - 2]);  // rows from self
        output_shape.push_back(other_shape[other.dim() - 1]); // cols from other
        
        std::cout << "[DEBUG] PyTorch output shape: [";
        for (int i = 0; i < output_shape.size(); i++) {
            std::cout << output_shape[i];
            if (i < output_shape.size() - 1) std::cout << ", ";
        }
        std::cout << "]" << std::endl;

        auto output = tt_eager::ops::create::custom_empty_memory_format(
            output_shape,
            self.scalar_type(),
            c10::nullopt,
            self.device(),
            c10::nullopt);
        auto* output_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
        output_impl->set_ttnn_tensor(ttnn_result);
        
        return output;
    }
}

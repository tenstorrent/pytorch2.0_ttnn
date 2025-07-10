#include "ttnn_cpp_extension/ops/linear_iml.hpp"

#include <vector>
#include <numeric>
#include <sstream>
#include <iostream>

#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"

namespace tt_eager::ops::linear {

    at::Tensor ttnn_view_infer(const at::Tensor& self, at::IntArrayRef shape) {
        std::ostringstream oss;
        oss << "[TTNN] aten::view/reshape called with sizes:";
        for (auto d : shape) {
            oss << " " << d;
        }
        LOGGING(oss.str());

        TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1,
                    "ttnn_view_infer requires TTNN backend");

        auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
        auto ttnn_tensor = self_impl->get_ttnn_tensor();

        if (ttnn_tensor.layout() == ttnn::ROW_MAJOR_LAYOUT) {
            ttnn_tensor = ttnn::to_layout(
                ttnn_tensor,
                ttnn::TILE_LAYOUT,
                std::nullopt,
                std::nullopt,
                ttnn_tensor.device());
        }

        int64_t old_numel = self.numel();

        int unknown = -1;
        int64_t known_prod = 1;
        std::vector<int64_t> dims(shape.begin(), shape.end());
        for (int i = 0; i < (int)dims.size(); ++i) {
            int64_t d = dims[i];
            if (d == -1) {
                TORCH_CHECK(unknown < 0, "only one -1 allowed in view/reshape");
                unknown = i;
            } else {
                TORCH_CHECK(d >= 0, "view/reshape dims must be >=0 or -1");
                known_prod *= d;
            }
        }
        if (unknown >= 0) {
            TORCH_CHECK(known_prod != 0 && old_numel % known_prod == 0,
                        "cannot infer dimension size for view/reshape");
            dims[unknown] = old_numel / known_prod;
        }

        int64_t new_numel = 1;
        for (auto d : dims) new_numel *= d;
        TORCH_CHECK(new_numel == old_numel,
                    "View/reshape size is incompatible with input tensor size: ",
                    "old = ", old_numel, ", new = ", new_numel);

        tt::stl::SmallVector<int32_t> shape_i32(dims.begin(), dims.end());
        auto reshaped = ttnn::reshape(ttnn_tensor, shape_i32);

        auto output = tt_eager::ops::create::custom_empty_memory_format(
            dims,
            self.scalar_type(),
            c10::nullopt,
            self.device(),
            c10::nullopt);
        auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
        out_impl->set_ttnn_tensor(reshaped);
        return output;
    }

    at::Tensor ttnn_linear(
        const at::Tensor& input,
        const at::Tensor& weight,
        const c10::optional<at::Tensor>& bias) 
    {
        auto orig_sizes = input.sizes();
        int64_t in_features = orig_sizes.back();
        int64_t out_features = weight.size(0);

        // DEBUG
        std::cout << "[DEBUG] input.shape: ";
        for (auto s : orig_sizes) std::cout << s << " ";
        std::cout << std::endl;
        std::cout << "[DEBUG] in_features: " << in_features << std::endl;

        at::Tensor flat = ttnn_view_infer(input, {-1, in_features});
        at::Tensor out2d = flat.matmul(weight.t());
        if (bias.has_value()) {
            out2d = out2d.add(*bias);
        }

        std::vector<int64_t> new_sizes(orig_sizes.begin(), orig_sizes.end());
        new_sizes.back() = out_features;

        // Діагностика
        int64_t expected_numel = 1;
        for (auto s : new_sizes) expected_numel *= s;
        int64_t actual_numel = out2d.numel();

        std::cout << "[DEBUG] out2d.shape: ";
        for (auto s : out2d.sizes()) std::cout << s << " ";
        std::cout << "\n[DEBUG] new_sizes: ";
        for (auto s : new_sizes) std::cout << s << " ";
        std::cout << "\n[DEBUG] actual_numel = " << actual_numel
                << ", expected_numel = " << expected_numel << std::endl;

        TORCH_CHECK(actual_numel == expected_numel,
                    "Mismatch in reshape: out2d.numel() = ", actual_numel,
                    ", expected from new shape = ", expected_numel);

        return ttnn_view_infer(out2d, new_sizes);
    }

}

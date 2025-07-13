#include "ttnn_cpp_extension/ops/as_strided.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/core/TtnnCustomAllocator.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include <ttnn/operations/core/core.hpp>
#include <ttnn/operations/data_movement/squeeze/squeeze.hpp>
#include <ttnn/operations/data_movement/slice/slice.hpp>
#include <iostream>
#include <sstream>

namespace tt_eager::ops::as_strided {

std::string arrayref_to_string(at::IntArrayRef arr) {
    std::ostringstream oss;
    oss << "[";
    for (size_t i = 0; i < arr.size(); i++) {
        oss << arr[i];
        if (i < arr.size() - 1) {
            oss << ", ";
        }
    }
    oss << "]";
    return oss.str();
}

at::Tensor ttnn_as_strided(
    const at::Tensor& self, at::IntArrayRef size, at::IntArrayRef stride, c10::optional<int64_t> storage_offset) {
    int64_t requested_volume = 1;
    for (int i = 0; i < size.size(); i++) {
        requested_volume *= size[i];
    }

    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = self_impl->get_ttnn_tensor();

    auto input_shape = ttnn_tensor.logical_shape();

    if (self.dim() == 2 && size.size() == 1) {
        if (size[0] == self.size(1)) {
            ttnn::SmallVector<uint32_t> begins = {0, 0};
            ttnn::SmallVector<uint32_t> ends = {1, (uint32_t)self.size(1)};
            ttnn::SmallVector<uint32_t> step = {1, 1};

            auto sliced = ttnn::slice(ttnn_tensor, begins, ends, step);

            auto squeezed = ttnn::squeeze(sliced, 0);

            std::vector<int64_t> output_shape = {self.size(1)};  // [seq]
            auto output_tensor = tt_eager::ops::create::custom_empty_memory_format(
                output_shape, self.scalar_type(), c10::nullopt, self.device(), c10::nullopt);

            auto* output_impl = static_cast<at::TtnnTensorImpl*>(output_tensor.unsafeGetTensorImpl());
            output_impl->set_ttnn_tensor(squeezed);

            output_tensor.unsafeGetTensorImpl()->set_sizes_contiguous(output_shape);
            return output_tensor;
        }
    }

    if (self.dim() == 3 && size.size() == 2) {
        if (size[0] == self.size(0) && size[1] == self.size(2)) {
            ttnn::SmallVector<uint32_t> begins = {0, 0, 0};
            ttnn::SmallVector<uint32_t> ends = {(uint32_t)self.size(0), 1, (uint32_t)self.size(2)};
            ttnn::SmallVector<uint32_t> step = {1, 1, 1};

            auto sliced = ttnn::slice(ttnn_tensor, begins, ends, step);

            auto squeezed = ttnn::squeeze(sliced, 1);

            std::vector<int64_t> output_shape = {self.size(0), self.size(2)};
            auto output_tensor = tt_eager::ops::create::custom_empty_memory_format(
                output_shape, self.scalar_type(), c10::nullopt, self.device(), c10::nullopt);

            auto* output_impl = static_cast<at::TtnnTensorImpl*>(output_tensor.unsafeGetTensorImpl());
            output_impl->set_ttnn_tensor(squeezed);

            output_tensor.unsafeGetTensorImpl()->set_sizes_contiguous(output_shape);

            return output_tensor;
        }
    }

    std::string error_msg = "ttnn_as_strided: Only [0] and [:, 0] slicing are currently supported. ";
    error_msg += "Input shape: " + arrayref_to_string(self.sizes()) + ", ";
    error_msg += "target size: " + arrayref_to_string(size);
    throw std::runtime_error(error_msg);
}

}  // namespace tt_eager::ops::as_strided

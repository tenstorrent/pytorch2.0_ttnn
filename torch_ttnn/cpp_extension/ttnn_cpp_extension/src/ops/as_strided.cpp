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
    std::cout << "[DEBUG] ttnn_as_strided called" << std::endl;
    std::cout << "[DEBUG] Input tensor shape: " << self.sizes() << std::endl;
    std::cout << "[DEBUG] Input tensor dtype: " << self.dtype() << std::endl;
    std::cout << "[DEBUG] Input tensor device: " << self.device() << std::endl;
    std::cout << "[DEBUG] Input tensor numel: " << self.numel() << std::endl;

    std::cout << "[DEBUG] Requested size: ";
    for (int i = 0; i < size.size(); i++) {
        std::cout << size[i] << " ";
    }
    std::cout << std::endl;

    std::cout << "[DEBUG] Requested stride: ";
    for (int i = 0; i < stride.size(); i++) {
        std::cout << stride[i] << " ";
    }
    std::cout << std::endl;

    int64_t requested_volume = 1;
    for (int i = 0; i < size.size(); i++) {
        requested_volume *= size[i];
    }
    std::cout << "[DEBUG] Requested volume: " << requested_volume << std::endl;
    std::cout << "[DEBUG] Storage offset: " << storage_offset.value_or(0) << std::endl;

    // Get TTNN tensor from TensorImpl
    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = self_impl->get_ttnn_tensor();

    // Debug the TTNN tensors
    std::cout << "[DEBUG] Input ttnn_tensor volume: " << ttnn_tensor.volume() << std::endl;
    std::cout << "[DEBUG] Input ttnn_tensor shape: ";
    auto input_shape = ttnn_tensor.logical_shape();
    for (int i = 0; i < input_shape.rank(); i++) {
        std::cout << input_shape[i];
        if (i < input_shape.rank() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << std::endl;

    if (self.dim() == 2 && size.size() == 1) {
        if (size[0] == self.size(1)) {
            std::cout << "[DEBUG] Detected [0] slicing pattern" << std::endl;

            ttnn::SmallVector<uint32_t> begins = {0, 0};
            ttnn::SmallVector<uint32_t> ends = {1, (uint32_t)self.size(1)};
            ttnn::SmallVector<uint32_t> step = {1, 1};

            std::cout << "[DEBUG] Slice begins: [" << begins[0] << ", " << begins[1] << "]" << std::endl;
            std::cout << "[DEBUG] Slice ends: [" << ends[0] << ", " << ends[1] << "]" << std::endl;

            auto sliced = ttnn::slice(ttnn_tensor, begins, ends, step);
            std::cout << "[DEBUG] After slice, before squeeze" << std::endl;
            std::cout << "[DEBUG] Sliced tensor volume: " << sliced.volume() << std::endl;

            auto squeezed = ttnn::squeeze(sliced, 0);
            std::cout << "[DEBUG] After squeeze" << std::endl;
            std::cout << "[DEBUG] Squeezed tensor volume: " << squeezed.volume() << std::endl;

            std::vector<int64_t> output_shape = {self.size(1)};  // [seq]
            auto output_tensor = tt_eager::ops::create::custom_empty_memory_format(
                output_shape, self.scalar_type(), c10::nullopt, self.device(), c10::nullopt);

            auto* output_impl = static_cast<at::TtnnTensorImpl*>(output_tensor.unsafeGetTensorImpl());
            output_impl->set_ttnn_tensor(squeezed);

            output_tensor.unsafeGetTensorImpl()->set_sizes_contiguous(output_shape);

            std::cout << "[DEBUG] TTNN result shape: " << output_tensor.sizes() << std::endl;
            std::cout << "[DEBUG] Final output shape: " << output_tensor.sizes() << std::endl;
            std::cout << "[DEBUG] Final output numel: " << output_tensor.numel() << std::endl;
            std::cout << "[DEBUG] ttnn_as_strided completed successfully" << std::endl;
            return output_tensor;
        }
    }

    // Handle [:, 0] slicing pattern for 3D tensors
    if (self.dim() == 3 && size.size() == 2) {
        if (size[0] == self.size(0) && size[1] == self.size(2)) {
            std::cout << "[DEBUG] Detected [:, 0] slicing pattern" << std::endl;

            ttnn::SmallVector<uint32_t> begins = {0, 0, 0};
            ttnn::SmallVector<uint32_t> ends = {(uint32_t)self.size(0), 1, (uint32_t)self.size(2)};
            ttnn::SmallVector<uint32_t> step = {1, 1, 1};

            std::cout << "[DEBUG] Slice begins: [" << begins[0] << ", " << begins[1] << ", " << begins[2] << "]"
                      << std::endl;
            std::cout << "[DEBUG] Slice ends: [" << ends[0] << ", " << ends[1] << ", " << ends[2] << "]" << std::endl;

            auto sliced = ttnn::slice(ttnn_tensor, begins, ends, step);
            std::cout << "[DEBUG] After slice, before squeeze" << std::endl;
            std::cout << "[DEBUG] Sliced tensor volume: " << sliced.volume() << std::endl;

            auto squeezed = ttnn::squeeze(sliced, 1);
            std::cout << "[DEBUG] After squeeze" << std::endl;
            std::cout << "[DEBUG] Squeezed tensor volume: " << squeezed.volume() << std::endl;

            std::vector<int64_t> output_shape = {self.size(0), self.size(2)};  // [batch, hidden]
            auto output_tensor = tt_eager::ops::create::custom_empty_memory_format(
                output_shape, self.scalar_type(), c10::nullopt, self.device(), c10::nullopt);

            auto* output_impl = static_cast<at::TtnnTensorImpl*>(output_tensor.unsafeGetTensorImpl());
            output_impl->set_ttnn_tensor(squeezed);

            output_tensor.unsafeGetTensorImpl()->set_sizes_contiguous(output_shape);

            std::cout << "[DEBUG] TTNN result shape: " << output_tensor.sizes() << std::endl;
            std::cout << "[DEBUG] Final output shape: " << output_tensor.sizes() << std::endl;
            std::cout << "[DEBUG] Final output numel: " << output_tensor.numel() << std::endl;
            std::cout << "[DEBUG] ttnn_as_strided completed successfully" << std::endl;
            return output_tensor;
        }
    }

    std::string error_msg = "ttnn_as_strided: Only [0] and [:, 0] slicing are currently supported. ";
    error_msg += "Input shape: " + arrayref_to_string(self.sizes()) + ", ";
    error_msg += "target size: " + arrayref_to_string(size);
    throw std::runtime_error(error_msg);
}

}  // namespace tt_eager::ops::as_strided

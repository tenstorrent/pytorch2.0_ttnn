#include <ttnn/operations/copy.hpp>
#include <ttnn/operations/experimental/copy/typecast/typecast.hpp>
#include <ttnn/operations/data_movement/transpose/transpose.hpp>
#include <ttnn/operations/core/to_layout/to_layout_op.hpp>
#include <torch/extension.h>

#include "ttnn_cpp_extension/ops/to_copy.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/core/copy.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"

namespace tt_eager::ops::to_copy {

at::Tensor ttnn_to_copy(
    const at::Tensor& self,
    c10::optional<at::ScalarType> dtype,
    c10::optional<at::Layout> layout,
    c10::optional<at::Device> device,
    c10::optional<bool> pin_memory,
    bool non_blocking,
    c10::optional<at::MemoryFormat> memory_format) {
    LOGGING("Running aten::_to_copy.default");

    auto target_dtype = dtype.value_or(self.scalar_type());
    auto target_device = device.value_or(self.device());
    auto target_layout = layout.value_or(self.layout());

    bool is_ttnn_source = self.device().type() == c10::DeviceType::PrivateUse1;
    bool is_ttnn_target = target_device.type() == c10::DeviceType::PrivateUse1;

    if (is_ttnn_source && is_ttnn_target) {
        TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1, "Source tensor must be on TTNN device");
        TORCH_CHECK(target_device.type() == c10::DeviceType::PrivateUse1, "Target device must be TTNN device");

        auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
        auto ttnn_tensor = self_impl->get_ttnn_tensor();

        if (target_dtype != self.scalar_type()) {
            auto target_ttnn_dtype = dtype_torch_to_ttnn(target_dtype);
            ttnn_tensor = ttnn::typecast(ttnn_tensor, target_ttnn_dtype);
        }

        if (ttnn_tensor.layout() == ttnn::ROW_MAJOR_LAYOUT) {
            ttnn_tensor =
                ttnn::to_layout(ttnn_tensor, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_tensor.device());
        }

        auto output = tt_eager::ops::create::custom_empty_memory_format(
            self.sizes(), target_dtype, target_layout, target_device, pin_memory, memory_format);

        auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
        out_impl->set_ttnn_tensor(ttnn_tensor);

        return output;
    } else if (is_ttnn_source && !is_ttnn_target) {
        TORCH_CHECK(target_device.is_cpu(), "Currently only support copying from TTNN device to CPU");

        auto cpu_tensor = at::empty(
            self.sizes(),
            at::TensorOptions()
                .dtype(target_dtype)
                .layout(target_layout)
                .device(target_device)
                .pinned_memory(pin_memory.value_or(false)));

        return ttnn_copy_from(self, cpu_tensor, non_blocking);
    } else if (!is_ttnn_source && is_ttnn_target) {
        TORCH_CHECK(self.is_cpu(), "Currently only support copying from CPU to TTNN device");

        auto output = tt_eager::ops::create::custom_empty_memory_format(
            self.sizes(), target_dtype, target_layout, target_device, pin_memory, memory_format);

        auto converted_self = self;
        if (target_dtype != self.scalar_type()) {
            converted_self = self.to(target_dtype);
        }

        return ttnn_copy_from(converted_self, output, non_blocking);
    } else {
        auto output = at::empty_like(self, target_dtype, target_layout, target_device, pin_memory, memory_format);
        output.copy_(self, non_blocking);
        return output;
    }
}

}  // namespace tt_eager::ops::to_copy

#include "ttnn_cpp_extension/core/TtnnCustomAllocator.hpp"
#include "ttnn_cpp_extension/core/copy.hpp"

#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/ops/binary.hpp"

#include "ttnn_cpp_extension/utils/device.hpp"
#include "ttnn_cpp_extension/utils/unary_eager_register.hpp"

#include <ttnn/operations/eltwise/unary/unary.hpp>
#include <ttnn/operations/eltwise/unary/unary_composite.hpp>
#include <ttnn/operations/eltwise/complex_unary/complex_unary.hpp>

// Register custom allocator. Only used to create dummy Torch tensor object.
REGISTER_ALLOCATOR(c10::DeviceType::PrivateUse1, &get_ttnn_custom_allocator());

namespace {

static inline void register_core_creation_and_copy(torch::Library& m) {
    // =========================
    // Core ops: creation and copy
    // =========================

    // schema: empty_strided(SymInt[] size, SymInt[] stride, *, ScalarType? dtype=None, Layout? layout=None, Device?
    // device=None, bool? pin_memory=None) -> Tensor
    m.impl("aten::empty_strided", &tt_eager::ops::create::custom_empty_strided);

    // schema: empty.memory_format(SymInt[] size, *, ScalarType? dtype=None, Layout? layout=None, Device? device=None,
    // bool? pin_memory=None, MemoryFormat? memory_format=None) -> Tensor
    m.impl("empty.memory_format", &tt_eager::ops::create::custom_empty_memory_format);

    // schema: _copy_from(Tensor self, Tensor dst, bool non_blocking=False) -> Tensor
    m.impl("_copy_from", &ttnn_copy_from);

    // Pending TTNN core ops to register:
    // ttnn::to_dtype
    // ttnn::to_layout
    // ttnn::to_memory_config
}

static inline void register_binary_ops(torch::Library& m) {
    m.impl("add.out", &tt_eager::ops::binary::ttnn_add_out);
    m.impl("add.Tensor", &tt_eager::ops::binary::ttnn_add_tensor);
}

}  // namespace

// This macro registers the kernels to the PyTorch Dispatcher.
// More details on the dispatcher can be found at
// http://blog.ezyang.com/2020/09/lets-talk-about-the-pytorch-dispatcher/.
TORCH_LIBRARY_IMPL(aten, PrivateUse1, m) {
    using namespace tt_eager::ext;

    register_core_creation_and_copy(m);
    register_unary_ops(m);
    register_binary_ops(m);
}

// This macro registers helper functions associated with the ttnn_device_mode module that can be used in Python
PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
    m.def("as_torch_device", &as_torch_device, "get torch device from existing ttnn device");
    m.def("get_ttnn_tensor", &get_ttnn_tensor, "open ttnn device and get torch device");
    m.def("open_torch_device", &open_torch_device, "get torch device from existing ttnn device");
    m.def("close_torch_device", &close_torch_device, "close torch device and associated ttnn device");
}

// Fallbacks
TORCH_LIBRARY_IMPL(_, PrivateUse1, m) { m.fallback(torch::CppFunction::makeFallthrough()); }

TORCH_LIBRARY_IMPL(_, AutogradPrivateUse1, m) { m.fallback(torch::CppFunction::makeFallthrough()); }

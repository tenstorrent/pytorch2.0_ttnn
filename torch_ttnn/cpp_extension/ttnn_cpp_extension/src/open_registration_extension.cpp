#include <ATen/native/DispatchStub.h>
#include <torch/csrc/utils/pybind.h>
#include <torch/extension.h>

#include "ttnn_cpp_extension/utils/device.hpp"

#include "ttnn_cpp_extension/core/TtnnCustomAllocator.hpp"
#include "ttnn_cpp_extension/core/copy.hpp"

#include "ttnn_cpp_extension/ops/unary.hpp"
#include "ttnn_cpp_extension/ops/binary.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/ops/softmax.hpp"
#include "ttnn_cpp_extension/ops/to_copy.hpp"
#include "ttnn_cpp_extension/ops/embedding.hpp"
#include "ttnn_cpp_extension/ops/view.hpp"
#include "ttnn_cpp_extension/ops/norm.hpp"
#include "ttnn_cpp_extension/ops/linear.hpp"
#include "ttnn_cpp_extension/ops/matmul.hpp"
#include "ttnn_cpp_extension/ops/as_strided.hpp"
#include "ttnn_cpp_extension/ops/clone.hpp"

REGISTER_ALLOCATOR(c10::DeviceType::PrivateUse1, &get_ttnn_custom_allocator());

// This macro registers the kernels to the PyTorch Dispatcher.
// More details on the dispatcher can be found at
TORCH_LIBRARY_IMPL(aten, PrivateUse1, m) {
    m.impl("aten::empty_strided", &tt_eager::ops::create::custom_empty_strided);
    m.impl("empty.memory_format", &tt_eager::ops::create::custom_empty_memory_format);
    m.impl("_copy_from", &ttnn_copy_from);
    m.impl("abs.out", &tt_eager::ops::unary::ttnn_abs_out);
    m.impl("add.out", &tt_eager::ops::binary::ttnn_add_out);

    m.impl("_softmax", &tt_eager::ops::normalization::ttnn_softmax);
    m.impl("_to_copy", &tt_eager::ops::to_copy::ttnn_to_copy);
    m.impl("add.Tensor", &tt_eager::ops::binary::ttnn_add_tensor);
    m.impl("addmm", &tt_eager::ops::matmul::ttnn_addmm);
    m.impl("bmm", &tt_eager::ops::matmul::ttnn_bmm);
    m.impl("clone", &tt_eager::ops::clone::ttnn_clone);
    m.impl("div.Tensor", &tt_eager::ops::binary::ttnn_div_tensor);
    m.impl("embedding", &tt_eager::ops::embedding::ttnn_embedding);
    m.impl("expand", &tt_eager::ops::view::ttnn_expand);
    m.impl("gelu", &tt_eager::ops::unary::ttnn_gelu);
    m.impl("mul.Tensor", &tt_eager::ops::binary::ttnn_mul_tensor);
    m.impl("native_layer_norm", &tt_eager::ops::norm::ttnn_native_layer_norm);
    m.impl("permute", &tt_eager::ops::view::ttnn_permute);
    m.impl("rsub.Scalar", &tt_eager::ops::binary::ttnn_rsub_scalar);
    m.impl("slice.Tensor", &tt_eager::ops::view::ttnn_slice_tensor);
    m.impl("split.Tensor", &tt_eager::ops::view::ttnn_split_tensor);
    m.impl("t", &tt_eager::ops::view::ttnn_t_default);
    m.impl("tanh", &tt_eager::ops::unary::ttnn_tanh);
    m.impl("transpose.int", &tt_eager::ops::view::ttnn_transpose_int);
    m.impl("unsqueeze", &tt_eager::ops::view::ttnn_unsqueeze);
    m.impl("squeeze.dim", &tt_eager::ops::view::ttnn_squeeze_dim);
    m.impl("view", &tt_eager::ops::view::ttnn_view);

    m.impl("linear", &tt_eager::ops::linear::ttnn_linear);
    m.impl("matmul", &tt_eager::ops::matmul::ttnn_matmul);
    m.impl("as_strided", &tt_eager::ops::as_strided::ttnn_as_strided);
}

// This macro registers helper functions associated with the ttnn_device_mode module that can be used in Python
PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
    m.def("as_torch_device", &as_torch_device, "get torch device from existing ttnn device");
    m.def("get_ttnn_tensor", &get_ttnn_tensor, "open ttnn device and get torch device");
    m.def("open_torch_device", &open_torch_device, "get torch device from existing ttnn device");
    m.def("close_torch_device", &close_torch_device, "close torch device and associated ttnn device");
}

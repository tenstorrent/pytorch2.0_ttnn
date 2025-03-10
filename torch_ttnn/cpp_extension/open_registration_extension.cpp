#include <ATen/native/DispatchStub.h>
#include <ATen/native/UnaryOps.h>  // abs_stub
#include <torch/csrc/Device.h>
#include <torch/csrc/utils/pybind.h>
#include <torch/extension.h>

#include <iostream>
#include <list>

// Order of header matters here because c10 has a Layout type as well. If this is before Aten headers, there will be
// errors about ambiguity.
#include "ttnn/device.hpp"
#include "ttnn/operations/creation.hpp"
#include "ttnn/tensor/tensor_utils.hpp"
#include "tt-metalium/bfloat16.hpp"
#include "ttnn/operations/core/core.hpp"

#include "extension_utils.hpp"
#include "TtnnCustomAllocator.h"
#include "TtnnTensorImpl.hpp"
#include "TtnnGuard.hpp"

// Debug Utils
template <typename T>
void vector_compare(const std::vector<T>& first, const std::vector<T>& second) {
    TORCH_INTERNAL_ASSERT(first.size() == second.size());
    for (int i = 0; i < first.size(); ++i) {
        if (fabs(first[i] - second[i]) > 0.000001) {
            LOGGING("mismatch: ", first[i], " vs ", second[i]);
        }
    }
}

using VariantVectorTy = std::variant<std::vector<float>, std::vector<int>>;

VariantVectorTy tensor_to_vector(const at::Tensor& tensor) {
    auto dtype = tensor.dtype();
    if (dtype == at::ScalarType::BFloat16) {
        auto torch_float = tensor.to(at::kFloat);
        std::vector<float> v(torch_float.data_ptr<float>(), torch_float.data_ptr<float>() + torch_float.numel());
        LOGGING("torch_tensor: ", v);
        return v;
    } else if (dtype == at::ScalarType::Int || dtype == at::ScalarType::Long) {
        auto torch_int = tensor.toType(at::ScalarType::Int);
        std::vector<int> v(torch_int.data_ptr<int>(), torch_int.data_ptr<int>() + torch_int.numel());
        LOGGING("torch_tensor: ", v);
        return v;
    } else {
        TORCH_INTERNAL_ASSERT(false);
    }
}

VariantVectorTy tensor_to_vector(const ttnn::Tensor& ttnn_tensor) {
    auto ttnn_dtype = ttnn_tensor.dtype();
    auto is_tensor_on_device = ttnn::is_tensor_on_device_or_multidevice(ttnn_tensor);

    ttnn::Tensor ttnn_tensor_tmp = ttnn_tensor;
    if (is_tensor_on_device) {
        auto logical_shape = ttnn_tensor.get_logical_shape();
        auto logical_rank = logical_shape.rank();
        if (logical_rank == 1) {
            ttnn::Shape new_shape({1, logical_shape[0]});
            ttnn_tensor_tmp = ttnn_tensor.reshape(new_shape);
        }
    }
    if (ttnn_dtype == ttnn::DataType::BFLOAT16) {
        std::vector<float> ttnn_vector = ttnn_tensor_tmp.to_vector<float>();
        LOGGING("src_dev: ", ttnn_vector);
        return ttnn_vector;
    } else if (ttnn_dtype == ttnn::DataType::UINT32) {
        auto ttnn_vector = ttnn_tensor_tmp.to_vector<uint32_t>();
        std::vector<int> src_vector_int;
        convert_vector_from_uint32_to_int(src_vector_int, ttnn_vector);
        LOGGING("src_dev: ", src_vector_int);
        return src_vector_int;
    } else {
        TORCH_INTERNAL_ASSERT(false);
    }
}

void compare_torch_and_ttnn_tensors(const at::Tensor& torch_tensor, const ttnn::Tensor& ttnn_tensor) {
    const auto DEBUG_CPP_EXT = std::getenv("DEBUG_CPP_EXT") != nullptr;
    if (DEBUG_CPP_EXT) {
        auto ttnn_dtype = ttnn_tensor.dtype();
        if (ttnn_dtype == ttnn::DataType::BFLOAT16) {
            auto torch_vector = std::get<std::vector<float>>(tensor_to_vector(torch_tensor));
            auto ttnn_vector = std::get<std::vector<float>>(tensor_to_vector(ttnn_tensor));

            vector_compare(torch_vector, ttnn_vector);
        } else if (ttnn_dtype == ttnn::DataType::UINT32) {
            auto torch_vector = std::get<std::vector<int>>(tensor_to_vector(torch_tensor));
            auto ttnn_vector = std::get<std::vector<int>>(tensor_to_vector(ttnn_tensor));

            vector_compare(torch_vector, ttnn_vector);
        }
    }
}

namespace {

void abs_kernel(at::TensorIteratorBase& iter) {
    // empty because we don't need it, but it has to be defined if we're intercepting torch.abs
}

}  // namespace

namespace at::native {
REGISTER_PRIVATEUSE1_DISPATCH(abs_stub, &abs_kernel);
}

// Register custom allocator. Only used to create dummy Torch tensor object.
static TtnnCustomAllocator ttnn_custom_alloc;
REGISTER_ALLOCATOR(c10::DeviceType::PrivateUse1, &ttnn_custom_alloc);

// Common helper function to create an empty tensor
// Does not handle strides or memory format yet.
at::Tensor create_empty_tensor(
    at::IntArrayRef size,
    c10::optional<at::ScalarType> dtype_opt,
    c10::optional<at::Layout> layout_opt,
    c10::optional<at::Device> device_opt,
    c10::optional<bool> pin_memory_opt) {
    constexpr c10::DispatchKeySet private_use_ks(c10::DispatchKey::PrivateUse1);
    auto dtype = GET_OPTIONAL_OR_ASSERT(dtype_opt);
    auto dtype_meta = c10::scalarTypeToTypeMeta(dtype);
    at::Device device = GET_OPTIONAL_OR_ASSERT(device_opt);

    LOGGING("size: ", size);
    LOGGING("dtype: ", dtype_opt.value());

    // Create torch storage with 0 size
    auto storage_impl = c10::make_intrusive<c10::StorageImpl>(
        c10::StorageImpl::use_byte_size_t(),
        0,
        &ttnn_custom_alloc,
        /*resizeable=*/true);

    TtnnGuard device_guard(device);
    IDevice* ttnn_device = device_guard.get_ttnn_device();
    auto ttnn_dtype = dtype_torch_to_ttnn(dtype);
    ttnn::SmallVector<uint32_t> small_vector(size.begin(), size.end());
    auto logical_shape = ttnn::Shape(small_vector);

    // Create ttnn::empty tensor on device
    auto ttnn_tensor = ttnn::empty(
        logical_shape,
        ttnn_dtype,
        ttnn::TILE_LAYOUT,
        ttnn_device,
        MemoryConfig{TensorMemoryLayout::INTERLEAVED, BufferType::DRAM, std::nullopt});

    // Equivalent to at::detail::make_tensor<at::TtnnTensorImpl>(Args...)
    auto ttnn_impl = c10::make_intrusive<at::TtnnTensorImpl>(private_use_ks, dtype_meta, device, size, storage_impl);
    ttnn_impl->set_ttnn_tensor(ttnn_tensor);

    return at::Tensor(ttnn_impl);
}

// =====================================
// ============= KERNELS ===============
// =====================================

at::Tensor custom_empty_memory_format(
    at::IntArrayRef size,
    c10::optional<at::ScalarType> dtype_opt,
    c10::optional<at::Layout> layout_opt,
    c10::optional<at::Device> device_opt,
    c10::optional<bool> pin_memory_opt,
    c10::optional<at::MemoryFormat> memory_format_opt) {
    LOGGING("");
    return create_empty_tensor(size, dtype_opt, layout_opt, device_opt, pin_memory_opt);
}

// TODO: Support "ttnn ==> cpu" and "ttnn ==> ttnn"
at::Tensor custom__copy_from(const at::Tensor& self, const at::Tensor& dst, bool non_blocking) {
    LOGGING(self.device().type(), " ==> ", dst.device().type());

    if (self.is_cpu() && dst.device().type() == c10::DeviceType::PrivateUse1) {
        TtnnGuard device_guard(at::device_of(dst).value());
        TORCH_CHECK(self.sizes() == dst.sizes());
        TORCH_CHECK(self.scalar_type() == dst.scalar_type());
        TORCH_CHECK(self.is_contiguous() && dst.is_contiguous());

        at::TtnnTensorImpl* tensor_impl = static_cast<at::TtnnTensorImpl*>(dst.unsafeGetTensorImpl());
        auto logical_shape = tensor_impl->get_logical_shape();
        LOGGING("TTNN Tensor logical shape: ", logical_shape);

        IDevice* ttnn_device = device_guard.get_ttnn_device();
        auto logical_volume = logical_shape.volume();

        auto on_creation_callback = [] {};
        auto on_destruction_callback = [] {};

        auto dtype = dtype_torch_to_ttnn(dst.scalar_type());
        LOGGING("ttnn dtype: ", (int)dtype);

        // TODO: Combine and remove duplicate code for different dtype support
        if (dtype == ttnn::DataType::BFLOAT16) {
            LOGGING("");

            auto self_bfloat16_storage_ptr = static_cast<bfloat16*>(self.storage().data_ptr().get());

            // Create TTNN Tensor on CPU
            ttnn::Tensor src_cpu = ttnn::Tensor(
                tt::tt_metal::BorrowedStorage{
                    borrowed_buffer::Buffer(self_bfloat16_storage_ptr, logical_volume),
                    on_creation_callback,
                    on_destruction_callback},
                logical_shape,
                dtype,
                ttnn::Layout::ROW_MAJOR);

            // Verify the data is created on TTNN tensor correctly
            compare_torch_and_ttnn_tensors(self, src_cpu);

            // TODO: Find out why there are problems when passing device directly to `to_layout` function
            ttnn::Tensor src_layout =
                ttnn::to_layout(src_cpu, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, (IDevice*)nullptr);
            ttnn::Tensor src_dev = src_layout.to_device(ttnn_device);

            // Verify the device data is correct
            compare_torch_and_ttnn_tensors(self, src_dev);

            // Finally save ttnn tensor on device to custom TorchImpl
            tensor_impl->set_ttnn_tensor(src_dev);
        }
        if (dtype == ttnn::DataType::UINT32) {
            // torch 2.2.1 does not have uint32_t ScalarType, so we cast it separately
            // This should typically be fine since int and uint32_t should have the same size
            auto self_int = self.toType(at::ScalarType::Int);
            auto self_int_storage_ptr = static_cast<uint32_t*>(self_int.storage().data_ptr().get());

            // First create ttnn Tensor on CPU
            ttnn::Tensor src_cpu = ttnn::Tensor(
                tt::tt_metal::BorrowedStorage{
                    borrowed_buffer::Buffer(self_int_storage_ptr, logical_volume),
                    on_creation_callback,
                    on_destruction_callback},
                logical_shape,
                dtype,
                ttnn::Layout::ROW_MAJOR);

            // Debug only: Convert torch tensor to vector
            std::vector<int> v(self_int.data_ptr<int>(), self_int.data_ptr<int>() + self_int.numel());
            LOGGING("src_ten: ", v);

            // Debug only: Convert ttnn tensor on cpu to vector
            auto src_cpu_vector = src_cpu.to_vector<uint32_t>();
            std::vector<int> src_cpu_vector_int;
            convert_vector_from_uint32_to_int(src_cpu_vector_int, src_cpu_vector);
            LOGGING("src_cpu: ", src_cpu_vector_int);
            vector_compare(v, src_cpu_vector_int);

            // Verify the data is created on TTNN tensor correctly
            compare_torch_and_ttnn_tensors(self, src_cpu);

            // TODO: Find out why there are problems when passing device directly to `to_layout` function
            ttnn::Tensor src_layout =
                ttnn::to_layout(src_cpu, ttnn::ROW_MAJOR_LAYOUT, std::nullopt, std::nullopt, (IDevice*)nullptr);
            ttnn::Tensor src_dev = src_cpu.to_device(ttnn_device);

            // Verify the device data is correct
            compare_torch_and_ttnn_tensors(self, src_dev);

            // Finally save ttnn tensor on device to custom TorchImpl
            tensor_impl->set_ttnn_tensor(src_dev);
        }
    } else {
        TORCH_INTERNAL_ASSERT(false, "Current do not support direction.");
    }

    return dst;
}

at::Tensor custom_empty_strided(
    c10::IntArrayRef size,
    c10::IntArrayRef stride,
    c10::optional<at::ScalarType> dtype_opt,
    c10::optional<at::Layout> layout_opt,
    c10::optional<at::Device> device_opt,
    c10::optional<bool> pin_memory_opt) {
    LOGGING("");
    return create_empty_tensor(size, dtype_opt, layout_opt, device_opt, pin_memory_opt);
}

// Example of intercepting torch.abs
at::Tensor& custom_abs_out(const at::Tensor& self, at::Tensor& out) {
    LOGGING("");
    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(out.device().type() == c10::DeviceType::PrivateUse1);

    // Get underlying TTNN tensor object from input
    at::TtnnTensorImpl* tensor_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = tensor_impl->get_ttnn_tensor();

    // Call TTNN operation
    auto result = ttnn::abs(ttnn_tensor);

    // Get underlying TTNN tensor object from output
    at::TtnnTensorImpl* out_tensor_impl = static_cast<at::TtnnTensorImpl*>(out.unsafeGetTensorImpl());
    out_tensor_impl->set_sizes_and_strides_as(self);

    // Set output TTNN tensor to result
    auto out_ttnn_tensor = out_tensor_impl->get_ttnn_tensor();
    out_tensor_impl->set_ttnn_tensor(result);

    return out;
}

// This macro registers the kernels to the PyTorch Dispatcher.
// More details on the dispatcher can be found at
// http://blog.ezyang.com/2020/09/lets-talk-about-the-pytorch-dispatcher/.
TORCH_LIBRARY_IMPL(aten, PrivateUse1, m) {
    m.impl("aten::empty_strided", &custom_empty_strided);
    m.impl("empty.memory_format", &custom_empty_memory_format);
    m.impl("_copy_from", &custom__copy_from);
    m.impl("abs.out", &custom_abs_out);
}

// ==============================================
// ============== PYBIND FUNCTIONS ==============
// ==============================================

// This function can be used when the TTNN device is initialized separately,
// for example, `device = ttnn.open_device(device_index = 0)`. Pass that
// device object to this function so that the cpp extension can use it.
c10::Device as_torch_device(IDevice* ttnn_device) {
    LOGGING("");
    // TODO: Fix the index
    auto device = c10::Device(c10::DeviceType::PrivateUse1, 0);
    if (TtnnGuard::ttnn_device == nullptr) {
        TtnnGuard::ttnn_device = ttnn_device;
    }
    return device;
}

// Manually closes the torch and ttnn device
void close_torch_device(c10::Device device) {
    LOGGING("");
    TtnnGuard device_guard(device);
    IDevice* ttnn_device = device_guard.get_ttnn_device();
    // TODO: Perform better error handling
    TORCH_INTERNAL_ASSERT(ttnn_device != nullptr);
    ttnn::close_device(*ttnn_device);
    ttnn_device = nullptr;
}

// Get the underlying TTNN tensor from a Torch tensor
ttnn::Tensor get_ttnn_tensor(at::Tensor& tensor) {
    LOGGING("");
    // TODO: Check if this cast fails
    at::TtnnTensorImpl* tensor_impl = static_cast<at::TtnnTensorImpl*>(tensor.unsafeGetTensorImpl());
    auto ttnn_tensor = tensor_impl->get_ttnn_tensor();
    return ttnn_tensor;
}

// This macro registers helper functions associated with the ttnn_device_mode module that can be used in Python
PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
    m.def("as_torch_device", &as_torch_device, "get torch device from existing ttnn device");
    m.def("close_torch_device", &close_torch_device, "close torch device and associated ttnn device");
    m.def("get_ttnn_tensor", &get_ttnn_tensor, "get underlying ttnn tensor");
}

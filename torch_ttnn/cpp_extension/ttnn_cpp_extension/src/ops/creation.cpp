#include <ttnn/operations/creation.hpp>

#include "ttnn_cpp_extension/utils/extension_utils.hpp"

#include "ttnn_cpp_extension/ops/creation.hpp"

#include "ttnn_cpp_extension/core/TtnnCustomAllocator.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/core/TtnnGuard.hpp"

namespace tt_eager::ops::create {
namespace {
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
        &get_ttnn_custom_allocator(),
        /*resizeable=*/true);

    TtnnGuard device_guard(device);
    ttnn::MeshDevice* ttnn_device = device_guard.get_ttnn_device();
    auto ttnn_dtype = dtype_torch_to_ttnn(dtype);
    ttnn::SmallVector<uint32_t> small_vector(size.begin(), size.end());
    auto logical_shape = ttnn::Shape(small_vector);

    // Create ttnn::empty tensor on device
    auto ttnn_tensor = ttnn::empty(
        logical_shape,
        ttnn_dtype,
        ttnn::TILE_LAYOUT,
        ttnn_device,
        ttnn::MemoryConfig{ttnn::TensorMemoryLayout::INTERLEAVED, ttnn::BufferType::DRAM, std::nullopt});

    // Equivalent to at::detail::make_tensor<at::TtnnTensorImpl>(Args...)
    auto ttnn_impl = c10::make_intrusive<at::TtnnTensorImpl>(private_use_ks, dtype_meta, device, size, storage_impl);
    ttnn_impl->set_ttnn_tensor(ttnn_tensor);

    auto res = at::Tensor(ttnn_impl);
    return res;
}
}  // namespace

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
}  // namespace tt_eager::ops::create

#include <ATen/DeviceGuard.h>
#include <ATen/core/Tensor.h>

#include <ttnn/tensor/tensor.hpp>
#include <tt-metalium/bfloat16.hpp>
#include <ttnn/tensor/storage.hpp>

#include "ttnn_cpp_extension/core/TtnnGuard.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"

#include "ttnn_cpp_extension/utils/extension_utils.hpp"

at::Tensor ttnn_copy_from(const at::Tensor& self, const at::Tensor& dst, bool non_blocking) {
    LOGGING(self.device().type(), " ==> ", dst.device().type());
    TORCH_CHECK(self.sizes() == dst.sizes());
    TORCH_CHECK(self.scalar_type() == dst.scalar_type());
    TORCH_CHECK(self.is_contiguous() && dst.is_contiguous());

    if (self.is_cpu() && dst.device().type() == c10::DeviceType::PrivateUse1) {
        TtnnGuard device_guard(at::device_of(dst).value());
        at::TtnnTensorImpl* tensor_impl = static_cast<at::TtnnTensorImpl*>(dst.unsafeGetTensorImpl());
        auto logical_shape = tensor_impl->get_logical_shape();
        LOGGING("TTNN Tensor logical shape: ", logical_shape);

        auto device_idx = dst.device().index();
        ttnn::MeshDevice* ttnn_device = device_guard.get_open_ttnn_device(device_idx);
        auto logical_volume = logical_shape.volume();

        auto dtype = dtype_torch_to_ttnn(dst.scalar_type());
        LOGGING("ttnn dtype: ", (int)dtype);

        if (dtype == ttnn::DataType::BFLOAT16) {
            LOGGING("");

            auto self_bfloat16_storage_ptr = static_cast<bfloat16*>(self.storage().data_ptr().get());

            // Create TTNN Tensor on CPU
            ttnn::Tensor src_cpu = ttnn::Tensor(
                tt::tt_metal::HostStorage{tt::tt_metal::host_buffer::create<bfloat16>(
                    tt::stl::Span(self_bfloat16_storage_ptr, logical_volume))},
                logical_shape,
                dtype,
                ttnn::Layout::ROW_MAJOR);

            ttnn::Tensor src_dev = src_cpu.to_device(ttnn_device);

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
                tt::tt_metal::HostStorage{
                    tt::tt_metal::host_buffer::create<uint32_t>(tt::stl::Span(self_int_storage_ptr, logical_volume))},
                logical_shape,
                dtype,
                ttnn::Layout::ROW_MAJOR);

            // Initialized as ROW_MAJOR for this dtype because of an issue with ttnn.embedding if this tensor was
            // converted later: https://github.com/tenstorrent/tt-metal/issues/22257
            ttnn::Tensor src_dev = src_cpu.to_device(ttnn_device);

            // Finally save ttnn tensor on device to custom TorchImpl
            tensor_impl->set_ttnn_tensor(src_dev);
        }
    } else if (self.device().type() == c10::DeviceType::PrivateUse1 && dst.is_cpu()) {
        // Handle TTNN => CPU copy
        LOGGING("Copying from TTNN to CPU");
        dst.reshape_as(self);

        at::TtnnTensorImpl* tensor_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
        auto ttnn_tensor = tensor_impl->get_ttnn_tensor();

        auto dtype = ttnn_tensor.dtype();

        // TODO: Add fp32 handling
        if (dtype == ttnn::DataType::BFLOAT16) {
            // TODO: Is this making extra copy?
            auto ttnn_vec = ttnn_tensor.to_vector<bfloat16>();
            auto* dst_ptr = dst.data_ptr<at::BFloat16>();
            std::memcpy(dst_ptr, ttnn_vec.data(), ttnn_vec.size() * sizeof(bfloat16));
        } else if (dtype == ttnn::DataType::INT32) {
            auto ttnn_vec = ttnn_tensor.to_vector<int32_t>();
            auto* dst_ptr = dst.data_ptr<int32_t>();
            std::memcpy(dst_ptr, ttnn_vec.data(), ttnn_vec.size() * sizeof(int32_t));
        } else if (dtype == ttnn::DataType::UINT32) {
            auto ttnn_vec = ttnn_tensor.to_vector<uint32_t>();
            auto dst_uint32_t = dst.to(at::ScalarType::Int);
            auto* dst_ptr = dst_uint32_t.data_ptr<int>();
            std::memcpy(dst_ptr, ttnn_vec.data(), ttnn_vec.size() * sizeof(uint32_t));
            dst.copy_(dst_uint32_t);
        }

    } else {
        TORCH_INTERNAL_ASSERT(false, "Current do not support direction.");
    }

    return dst;
}

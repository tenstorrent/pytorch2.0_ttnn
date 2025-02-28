#include <c10/core/impl/alloc_cpu.h>
#include <c10/core/Allocator.h>
#include <c10/core/DeviceGuard.h>
#include <c10/core/impl/DeviceGuardImplInterface.h>

#include <torch/csrc/Device.h>
#include <torch/extension.h>

#include <ATen/native/cpu/Loops.h>
#include <ATen/native/DispatchStub.h>
#include <ATen/EmptyTensor.h>
#include <ATen/ops/empty_strided.h>
#include <ATen/ops/abs_native.h>

#include <iostream>
#include <string.h>

#include <ATen/native/Resize.h>
#include <ATen/native/UnaryOps.h> // abs_stub

#include <list>

// Order of header matters here because c10 has a Layout type as well. If this is before Aten headers, there will be errors about ambiguity.
#include "ttnn/device.hpp"
#include "ttnn/operations/creation.hpp"
#include "tt-metalium/small_vector.hpp"
#include "ttnn/common/queue_id.hpp"
#include <tt-metalium/bfloat16.hpp>
#include "ttnn/operations/core/core.hpp"

#include "TtnnTensorImpl.hpp"
#include "extension_utils.hpp"
#include "tt-metalium/event.hpp"
#include "ttnn/async_runtime.hpp"

#include <torch/csrc/utils/pybind.h>

#include <format>

namespace {

void abs_kernel(at::TensorIteratorBase& iter) {
  // empty because we don't need it, but it has to be defined if we're intercepting torch.abs
}

} // namespace

namespace at::native {
REGISTER_PRIVATEUSE1_DISPATCH(abs_stub, &abs_kernel);
}

// A dummy allocator for the custom device, that secretly uses the CPU
// TODO: Do we have to implement this for the use of TTNN?
struct DummyCustomAllocator final : at::Allocator {
  DummyCustomAllocator() = default;
  // at::DataPtr allocate(size_t nbytes) override {
  at::DataPtr allocate(size_t nbytes) const override {
    LOGGING("");
    void* data = c10::alloc_cpu(nbytes);
    return {data, data, &ReportAndDelete, c10::Device(c10::DeviceType::PrivateUse1, 0)};
  }

  static void ReportAndDelete(void* ptr) {
    LOGGING("");
    if (!ptr) {
      return;
    }
    c10::free_cpu(ptr);
  }

  at::DeleterFnPtr raw_deleter() const override {
    return &ReportAndDelete;
  }
};

// Register our dummy allocator
static DummyCustomAllocator global_custom_alloc;
REGISTER_ALLOCATOR(c10::DeviceType::PrivateUse1, &global_custom_alloc);


// =====================================
// ============= Device Guards =========
// =====================================

// PyTorch has an API for registering device guards.
// Device guards can be used to set the current "active" device,
// and e.g. error if the user provides an invalid device index.
//
// If your device doesn't support indices (e.g. foo:0 vs. foo:1),
// then the guards probably aren't needed.
//
// You can use it by creating a DeviceGuard class, registering it
// in PyTorch, and invoking the device guard before any kernels are called.
// For a more full-featured example of a device guard,
// check out the code at c10/cuda/CUDAGuard.h

// Represents the current "active" device.
// The device guard registered below is meant to show how a backend
// can integrate custom device guard with pytorch.
// For something like cuda this represents the current active cuda device,
// which is directly set using the cuda API calls cudaGetDevice/cudaSetDevice.
static uint16_t CURR_DEVICE = -1;

// Create and register a dummy device guard.
struct TtnnDeviceGuard final : public c10::impl::DeviceGuardImplInterface {
  static constexpr c10::DeviceType static_type = c10::DeviceType::PrivateUse1;
  TtnnDeviceGuard() {
    LOGGING("");
  }
  explicit TtnnDeviceGuard(c10::DeviceType t) {
    LOGGING("");
    TORCH_INTERNAL_ASSERT(t == c10::DeviceType::PrivateUse1);
  }
  at::DeviceType type() const override {
    LOGGING("");
    return at::DeviceType::PrivateUse1;
  }
  at::Device exchangeDevice(at::Device d) const override {
    LOGGING("");
    TORCH_INTERNAL_ASSERT(d.type() == at::DeviceType::PrivateUse1);
    TORCH_INTERNAL_ASSERT(d.index() < deviceCount(), "Error: device index ", d.index(), " does not exist.");
    at::Device old_device = getDevice();
    if (old_device.index() != d.index()) {
      // "set the active device"
      CURR_DEVICE = d.index();
    }
    return old_device;
  }
  at::Device getDevice() const override {
    LOGGING("");
    return at::Device(at::DeviceType::PrivateUse1, CURR_DEVICE);
  }
  void setDevice(at::Device d) const override {
    LOGGING("");
    TORCH_INTERNAL_ASSERT(d.type() == at::DeviceType::PrivateUse1);
    TORCH_INTERNAL_ASSERT(d.index() < deviceCount(), "Error: device index ", d.index(), " does not exist.");
    at::Device current_device = getDevice();
    if (current_device != d) {
      CURR_DEVICE = d.index();
    }
  }
  void uncheckedSetDevice(at::Device d) const noexcept override {
    LOGGING("");
    auto current_device = getDevice();
    if (current_device != d) {
      CURR_DEVICE = d.index();
    }
  }
  at::Stream getStream(at::Device d) const noexcept override {
    // no-op
    return at::Stream(at::Stream::DEFAULT, d);
  }
  // NB: These do NOT set the current device
  at::Stream exchangeStream(at::Stream) const noexcept override {
    // no-op
    return at::Stream(at::Stream::DEFAULT, at::Device(at::DeviceType::PrivateUse1, CURR_DEVICE));
  }
  at::DeviceIndex deviceCount() const noexcept override {
    // Hardcoding the number of "valid" devices here at 2.
    return 2;
  }

  // Event-related functions
  void record(
      void** /*event*/,
      const at::Stream& /*stream*/,
      const at::DeviceIndex /*device_index*/,
      const c10::EventFlag /*flag*/) const override {
    TORCH_CHECK(false, at::DeviceType::PrivateUse1, " backend doesn't support events.");
  }
  void block(void* /*event*/, const at::Stream& /*stream*/) const override {
    LOGGING("");
    TORCH_CHECK(false, at::DeviceType::PrivateUse1, " backend doesn't support events.")
  }
  bool queryEvent(void* /*event*/) const override {
    LOGGING("");
    TORCH_CHECK(false, at::DeviceType::PrivateUse1, " backend doesn't support events.")
  }
  void destroyEvent(void* /*event*/, const at::DeviceIndex /*device_index*/)
      const noexcept override {}

  // Stream-related functions
  bool queryStream(const at::Stream& /*stream*/) const override {
    return true;
  }
  void synchronizeStream(const at::Stream& /*stream*/) const override {
    // Don't wait for anything.
  }
};

struct TtnnGuard {
  explicit TtnnGuard() = delete;
  explicit TtnnGuard(at::DeviceIndex device_index) : guard_(device_index) {}
  explicit TtnnGuard(at::Device device) : guard_(device) {}
  TtnnGuard(const TtnnGuard&) = delete;
  TtnnGuard& operator=(const TtnnGuard&) = delete;
  TtnnGuard(TtnnGuard&& other) = delete;
  TtnnGuard& operator=(TtnnGuard&& other) = delete;

  void set_device(at::Device device) {
    guard_.set_device(device);
  }

  void reset_device(at::Device device) {
    guard_.reset_device(device);
  }

  void set_index(at::DeviceIndex device_index) {
    guard_.set_index(device_index);
  }

  at::Device original_device() const {
    return guard_.original_device();
  }

  at::Device current_device() const {
    return guard_.current_device();
  }

  IDevice* get_ttnn_device() {
    LOGGING("");
    if (!ttnn_device) {
      ttnn_device = &ttnn::open_device(0);
    }
    return ttnn_device;
  }

  static IDevice * ttnn_device;
 private:
  c10::impl::InlineDeviceGuard<TtnnDeviceGuard> guard_;
};

IDevice* TtnnGuard::ttnn_device = nullptr;

C10_REGISTER_GUARD_IMPL(PrivateUse1, TtnnDeviceGuard);




// =====================================
// ============= KERNELS ===============
// =====================================

at::Tensor custom_empty_memory_format(at::IntArrayRef size, c10::optional<at::ScalarType> dtype_opt, c10::optional<at::Layout> layout_opt, c10::optional<at::Device> device_opt, c10::optional<bool> pin_memory_opt, c10::optional<at::MemoryFormat> memory_format_opt) {
  LOGGING("");
  constexpr c10::DispatchKeySet private_use_ks(c10::DispatchKey::PrivateUse1);
  // TODO: Check for value to be safe
  auto dtype = c10::scalarTypeToTypeMeta(dtype_opt.value());
  LOGGING("dtype: ", dtype);
  at::Device device = device_opt.value();
  LOGGING("device: ", device);
  TtnnGuard device_guard(device);
  IDevice* ttnn_device = device_guard.get_ttnn_device();
  LOGGING("size: ", size);
  ttnn::SmallVector<uint32_t> small_vector(size.begin(), size.end());

  // TODO: This preallocated data doesn't get used, but the metadata does. Needs fixing.
  auto tensor = ttnn::empty(ttnn::Shape(small_vector),
    ttnn::DataType::BFLOAT16,
    ttnn::TILE_LAYOUT,
    ttnn_device,
    MemoryConfig{TensorMemoryLayout::INTERLEAVED, BufferType::DRAM, std::nullopt});

  LOGGING("");

  // TODO: We can probably allocate 0 bytes here since we're not using CPU storage
  auto size_bytes = at::detail::computeStorageNbytesContiguous(size, dtype.itemsize());
  auto storage_impl = c10::make_intrusive<c10::StorageImpl>(
    c10::StorageImpl::use_byte_size_t(),
    0,
    &global_custom_alloc,
    /*resizeable=*/true);

  // Store ttnn tensor to torch tensor impl
  auto tensor_ret = at::detail::make_tensor<at::TtnnTensorImpl>(private_use_ks, dtype, device, tensor, storage_impl);
  LOGGING("");

  return tensor_ret;
}

at::Tensor & custom_fill__scalar(at::Tensor & self, const at::Scalar & value) {
  LOGGING("");
  return self;
}

// basic copy_() function, so we can copy from the custom device to/from CPU
at::Tensor custom__copy_from(const at::Tensor& self, const at::Tensor& dst, bool non_blocking) {
  LOGGING(self.device().type(), " ==> ", dst.device().type());
  // TODO: Only supports cpu ==> ttnn or ttnn ==> cpu
  // TODO: Check direction of copy
  if (self.is_cpu() && dst.device().type() == c10::DeviceType::PrivateUse1) {
    LOGGING("Copying from cpu to ttnn...");

    TtnnGuard device_guard(at::device_of(dst).value());

    // Some dummy asserts for the basic use case: inputs are the same size / dtype, all contiguous.
    LOGGING("CPU Tensor Size: ", self.sizes(), " dtype: ", self.dtype());
    LOGGING("CPU Tensor Scalar Type: ", self.scalar_type());
    LOGGING("CPU is Contiguous: ", self.is_contiguous());

    LOGGING("TTNN Torch Tensor size: ", dst.sizes(), " dtype: ", dst.dtype());
    // TORCH_CHECK(self.sizes() == dst.sizes());
    TORCH_CHECK(self.scalar_type() == dst.scalar_type());
    TORCH_CHECK(self.is_contiguous() && dst.is_contiguous());

    at::TtnnTensorImpl* tensor_impl = static_cast<at::TtnnTensorImpl*>(dst.unsafeGetTensorImpl());
    auto dst_tensor = tensor_impl->get_ttnn_tensor();
    auto padded_shape = dst_tensor.get_padded_shape();
    auto logical_shape = dst_tensor.get_logical_shape();
    LOGGING("TTNN Tensor padded shape: ", padded_shape);
    LOGGING("TTNN Tensor logical shape: ", logical_shape);

    IDevice* ttnn_device = device_guard.get_ttnn_device();
    // LOGGING(dst_tensor.write_to_string());
    LOGGING("dst_tensor is contiguous: ", dst_tensor.is_contiguous());

    // Get Device attributes
    auto volume = dst_tensor.volume();
    auto element_size = dst_tensor.element_size();
    auto logical_volume = dst_tensor.get_logical_volume();
    auto dtype = dst_tensor.get_dtype();
    LOGGING("volume: ", volume);
    LOGGING("element_size: ", element_size);
    LOGGING("logical_volume: ", logical_volume);
    LOGGING("dtype: ", static_cast<int>(dtype));

    auto on_creation_callback = [] {};
    auto on_destruction_callback = [] {};

    // TODO: Combine and remove duplicate code for different dtype support
    if (dtype == ttnn::DataType::BFLOAT16) {
      LOGGING("");

      // First create ttnn Tensor on CPU
      ttnn::Tensor src_cpu = ttnn::Tensor(
        tt::tt_metal::BorrowedStorage{
          borrowed_buffer::Buffer(static_cast<bfloat16*>(self.storage().data_ptr().get()), logical_volume),
          on_creation_callback,
          on_destruction_callback},
        logical_shape,
        dtype,
        ttnn::Layout::ROW_MAJOR);

      // Debug only: Convert torch tensor to vector
      auto self_float = self.to(at::kFloat);
      std::vector<float> v(self_float.data_ptr<float>(), self_float.data_ptr<float>() + self_float.numel());
      LOGGING("src_ten: ", v);

      // Debug only: Convert ttnn tensor on cpu to vector
      auto src_cpu_vector = src_cpu.to_vector<float>();
      LOGGING("src_cpu: ", src_cpu_vector);
      vector_compare(v, src_cpu_vector);

      // TODO: Find out why there are problems when passing device directly to `to_layout` function
      ttnn::Tensor src_layout = ttnn::to_layout(src_cpu, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, (IDevice*)nullptr);
      ttnn::Tensor src_dev = src_layout.to_device(ttnn_device);

      // Debug only: Convert ttnn tensor on device to vector
      auto logical_rank = logical_shape.rank();
      if (logical_rank == 1) {
        ttnn::Shape new_shape({1, logical_shape[0]});
        Tensor src_reshaped = src_dev.reshape(new_shape);
        LOGGING("src_dev: ", src_reshaped.to_vector<float>());
      } else {
        LOGGING("src_dev: ", src_dev.to_vector<float>());
      }

      // Finally save ttnn tensor on device to custom TorchImpl
      tensor_impl->set_ttnn_tensor(src_dev);
    }
    if (dtype == ttnn::DataType::UINT32) {

      // TODO: Distinguish between int32 and uint32
      std::vector<uint32_t> self_cast;
      for (int i = 0; i < logical_volume; ++i) {
        auto long_storage_ptr = static_cast<uint32_t*>(self.storage().data_ptr().get());
        self_cast.push_back(long_storage_ptr[i]);
      }

      // First create ttnn Tensor on CPU
      ttnn::Tensor src_cpu = ttnn::Tensor(
        tt::tt_metal::BorrowedStorage{
          borrowed_buffer::Buffer(self_cast.data(), logical_volume),
          on_creation_callback,
          on_destruction_callback},
        logical_shape,
        dtype,
        ttnn::Layout::ROW_MAJOR);

      // Debug only: Convert torch tensor to vector
      // torch 2.2.1 does not have at::kUint32, but later versions do
      auto self_int = self.to(at::kInt);
      std::vector<int> v(self_int.data_ptr<int>(), self_int.data_ptr<int>() + self_int.numel());
      LOGGING("src_ten: ", v);

      // Debug only: Convert ttnn tensor on cpu to vector
      auto src_cpu_vector = src_cpu.to_vector<uint32_t>();
      std::vector<int> src_cpu_vector_int;
      std::transform(src_cpu_vector.begin(), src_cpu_vector.end(), std::back_inserter(src_cpu_vector_int), [](const uint32_t value)
      { 
          return static_cast<int>(value); 
      });
      LOGGING("src_cpu: ", src_cpu_vector_int);
      vector_compare(v, src_cpu_vector_int);

      // TODO: Find out why there are problems when passing device directly to `to_layout` function
      ttnn::Tensor src_layout = ttnn::to_layout(src_cpu, ttnn::ROW_MAJOR_LAYOUT, std::nullopt, std::nullopt, (IDevice*)nullptr);
      ttnn::Tensor src_dev = src_cpu.to_device(ttnn_device);

      // Debug only: Convert ttnn tensor on device to vector
      auto logical_rank = logical_shape.rank();
      if (logical_rank == 1) {
        ttnn::Shape new_shape({1, logical_shape[0]});
        Tensor src_reshaped = src_dev.reshape(new_shape);
        if (dtype == ttnn::DataType::UINT32) {
          auto src_reshaped_vector = src_reshaped.to_vector<uint32_t>();
          std::vector<int> src_vector_int;
          std::transform(src_reshaped_vector.begin(), src_reshaped_vector.end(), std::back_inserter(src_vector_int), [](const uint32_t value)
          { 
              return static_cast<int>(value); 
          });
          LOGGING("src_dev: ", src_vector_int);
        }
      } else {
        auto src_vector = src_dev.to_vector<uint32_t>();
        std::vector<int> src_vector_int;
        std::transform(src_vector.begin(), src_vector.end(), std::back_inserter(src_vector_int), [](const uint32_t value)
        { 
            return static_cast<int>(value); 
        });
        LOGGING("src_dev: ", src_vector_int);
      }

      // Finally save ttnn tensor on device to custom TorchImpl
      tensor_impl->set_ttnn_tensor(src_dev);
    }
  }
  // TODO: This part, ttnn => cpu needs to be redone
  else if (self.device().type() == c10::DeviceType::PrivateUse1 && dst.is_cpu()) {
    LOGGING("");
    TtnnGuard device_guard(at::device_of(self).value());

    // same as custom_resize_?
    at::TensorImpl* dst_tensor_impl = dst.unsafeGetTensorImpl();
    LOGGING(dst_tensor_impl->storage_initialized());
    at::IntArrayRef size = self.sizes();
    dst_tensor_impl->set_sizes_contiguous(size);
    const auto itemsize = dst_tensor_impl->dtype().itemsize();
    const auto offset = dst_tensor_impl->storage_offset();
    const auto storage_size = at::detail::computeStorageNbytesContiguous(size, itemsize, offset);
    LOGGING(storage_size);
    LOGGING(dst_tensor_impl->numel());
    at::native::maybe_resize_storage_cpu(dst_tensor_impl, storage_size);

    LOGGING(dst_tensor_impl->storage_initialized());

    // Some dummy asserts for the basic use case: inputs are the same size / dtype, all contiguous.
    LOGGING(self.sizes());
    LOGGING(dst.sizes());
    // TORCH_CHECK(self.sizes() == dst.sizes());
    TORCH_CHECK(self.scalar_type() == dst.scalar_type());

    // ttnn tensor has contiguous check too
    LOGGING(self.is_contiguous());
    LOGGING(dst.is_contiguous());
    TORCH_CHECK(self.is_contiguous() && dst.is_contiguous());

    at::TtnnTensorImpl* tensor_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto self_tensor = tensor_impl->get_ttnn_tensor();
    // LOGGING(self_tensor.write_to_string());
    LOGGING(self_tensor.get_padded_shape());
    LOGGING(self_tensor.logical_shape());
    auto volume = self_tensor.volume();
    auto element_size = self_tensor.element_size();
    auto logical_volume = self_tensor.get_logical_volume();
    LOGGING(volume);

    LOGGING("");
    // better type for bytes?
    uint8_t* temp_host_ptr = new uint8_t[volume * element_size];
    tt::tt_metal::memcpy(temp_host_ptr, self_tensor);
    // use better copy?
    memcpy(dst.storage().data_ptr().get(), temp_host_ptr, logical_volume * element_size);
    delete[] temp_host_ptr;
  }

  return dst;
}

// TODO: Can possibly combine with custom_empty_memory_format
at::Tensor custom_empty_strided(c10::IntArrayRef size,
                                c10::IntArrayRef stride,
                                c10::optional<at::ScalarType> dtype_opt,
                                c10::optional<at::Layout> layout_opt,
                                c10::optional<at::Device> device_opt,
                                c10::optional<bool> pin_memory_opt) {

  LOGGING("Creating empty strided tensor...");
  constexpr c10::DispatchKeySet private_use_ks(c10::DispatchKey::PrivateUse1);
  // TODO: Check if value exists before accessing
  auto dtype = c10::scalarTypeToTypeMeta(dtype_opt.value());

  LOGGING("Size: ", size);
  LOGGING("Stride: ", stride);
  LOGGING("dtype: ", dtype_opt.value());

  at::Device device = device_opt.value();
  LOGGING("Using at::Device: ", device);
  TtnnGuard device_guard(device);
  IDevice* ttnn_device = device_guard.get_ttnn_device();
  ttnn::SmallVector<uint32_t> small_vector(size.begin(), size.end());

  auto ttnn_dtype = dtype_torch_to_ttnn(dtype_opt.value());
  LOGGING("ttnn_dtype: ", static_cast<int>(ttnn_dtype));

  // TODO: This preallocated data doesn't get used, but the metadata does. Needs fixing.
  auto ttnn_tensor = ttnn::empty(ttnn::Shape(small_vector),
    ttnn_dtype,
    ttnn::TILE_LAYOUT,
    ttnn_device,
    MemoryConfig{TensorMemoryLayout::INTERLEAVED, BufferType::DRAM, std::nullopt});

  // TODO: Can probably allocate only 0 bytes here
  auto size_bytes = at::detail::computeStorageNbytesContiguous(size, dtype.itemsize());
  auto storage_impl = c10::make_intrusive<c10::StorageImpl>(
    c10::StorageImpl::use_byte_size_t(),
    0,
    &global_custom_alloc,
    /*resizeable=*/true);

  auto ttnn_tensor_ret = at::detail::make_tensor<at::TtnnTensorImpl>(private_use_ks, dtype, device, ttnn_tensor, storage_impl);
  return ttnn_tensor_ret;
}

// TODO: Example of intercepting torch.abs
at::Tensor& custom_abs_out(const at::Tensor& self, at::Tensor& out) {
  LOGGING("");
  LOGGING(self.device().type());
  LOGGING(out.device().type());
  at::TtnnTensorImpl* tensor_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
  LOGGING("");
  auto ttnn_tensor = tensor_impl->get_ttnn_tensor();
  LOGGING("");

  LOGGING("");
  auto result = ttnn::abs(ttnn_tensor);

  LOGGING("");
  at::TtnnTensorImpl* out_tensor_impl = static_cast<at::TtnnTensorImpl*>(out.unsafeGetTensorImpl());
  LOGGING(out.device().type());
  out_tensor_impl->set_sizes_and_strides_as(self);
  LOGGING(out.device().type());
  LOGGING("");

  auto out_ttnn_tensor = out_tensor_impl->get_ttnn_tensor();
  LOGGING("");
  out_tensor_impl->set_ttnn_tensor(result);
  LOGGING("");
  
  return out;
}

// This macro does the heavy lifting.
// With TORCH_LIBRARY_IMPL, you can register custom kernels for your backend.
// For open registration, we're registering all of our kernels to the PrivateUse1 dispatch key.
// Later in this file, we map a custom device to the PrivateUse1 device type,
// which allows user code that puts a tensor on your custom_device to eventually get plumbed
// into the kernels registered here.
//
// This macro registers your kernels to the PyTorch Dispatcher.
// More details on the dispatcher can be found at http://blog.ezyang.com/2020/09/lets-talk-about-the-pytorch-dispatcher/.
TORCH_LIBRARY_IMPL(aten, PrivateUse1, m) {
  m.impl("aten::empty_strided", &custom_empty_strided);
  m.impl("empty.memory_format", &custom_empty_memory_format);
  m.impl("_copy_from", &custom__copy_from);
  m.impl("abs.out", &custom_abs_out); 
}

// This basic implementation doesn't bother dealing with different device indices
// (e.g. custom_device:0 vs. custom_device:1).
// We could do that by letting the user pass in a device index in our exposed device function.
// Note that if you do that, you'll also need to register a device guard to core.
// See `c10/core/impl/DeviceGuardImplInterface.h:C10_REGISTER_GUARD_IMPL`.
c10::Device get_custom_device(int idx) {
  LOGGING("");
  auto device = c10::Device(c10::DeviceType::PrivateUse1, idx);
  return device;
}

c10::Device get_custom_device_from_ttnn(IDevice* ttnn_device) {
  LOGGING("");
  // TODO: Fix the index
  auto device = c10::Device(c10::DeviceType::PrivateUse1, 0);
  if (TtnnGuard::ttnn_device == nullptr) {
    TtnnGuard::ttnn_device = ttnn_device;
  }
  return device;
}

// TODO: Automatically close device without explicit calling
void close_custom_device(c10::Device device) {
  LOGGING("");
  TtnnGuard device_guard(device);
  IDevice* ttnn_device = device_guard.get_ttnn_device();
  TORCH_INTERNAL_ASSERT(ttnn_device != nullptr);
  ttnn::close_device(*ttnn_device);
  ttnn_device = nullptr;
}

// Get underlying ttnn tensor
ttnn::Tensor get_ttnn_tensor(at::Tensor& tensor) {
  LOGGING("");
  // TODO: Check if this cast fails
  at::TtnnTensorImpl* tensor_impl = static_cast<at::TtnnTensorImpl*>(tensor.unsafeGetTensorImpl());
  auto ttnn_tensor = tensor_impl->get_ttnn_tensor();
  return ttnn_tensor;
}

// Here, we're exposing a custom device object that corresponds to our custom backend.
// We do this using pybind: exposing an "extension_name.custom_device()" function in python,
// that's implemented in C++.
// The implementation in this file maps directly to the `PrivateUse1` device type.
PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
    m.def("custom_device", &get_custom_device, "get custom device object");
    m.def("custom_device_from_ttnn", &get_custom_device_from_ttnn, "get custom device object from existing ttnn device");
    m.def("close_custom_device", &close_custom_device, "close custom device object");
    m.def("get_ttnn_tensor", &get_ttnn_tensor, "get underlying ttnn tensor");
}

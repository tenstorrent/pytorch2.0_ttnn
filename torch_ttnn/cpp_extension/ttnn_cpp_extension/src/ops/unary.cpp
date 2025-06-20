// src/ops/unary.cpp

#include "ttnn_cpp_extension/ops/unary.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"

#include <ttnn/operations/data_movement/clone/clone.hpp>
#include <ttnn/typedefs.hpp>       // ttnn::DType, ttnn::MemFormat
#include <ttnn/kernel_config.hpp>  // ttnn::KernelConfig

#include <ttnn/operations/eltwise/unary/unary.hpp>

namespace {

/// Convert ATen scalar type to your TTNN data‐type enum
ttnn::DType to_ttnn_dtype(at::ScalarType st) {
  switch (st) {
    case at::kFloat:  return ttnn::DType::Float32;
    case at::kDouble: return ttnn::DType::Float64;
    case at::kInt:    return ttnn::DType::Int32;
    case at::kLong:   return ttnn::DType::Int64;
    default:
      TORCH_CHECK(false, "ttnn_clone: unsupported dtype ", st);
  }
}

/// Convert ATen MemoryFormat into your TTNN memory‐format enum
ttnn::MemFormat to_ttnn_memformat(at::MemoryFormat mf) {
  if (mf == at::MemoryFormat::Contiguous)    return ttnn::MemFormat::Contiguous;
  if (mf == at::MemoryFormat::ChannelsLast)  return ttnn::MemFormat::ChannelsLast;
  TORCH_WARN("ttnn_clone: unknown MemoryFormat, defaulting to Contiguous");
  return ttnn::MemFormat::Contiguous;
}

/// A sensible default KernelConfig for your TTNN backend
ttnn::KernelConfig default_ttnn_kernel_config() {
  ttnn::KernelConfig cfg;
  cfg.queue_id = 0;
  // …set any other fields your backend requires…
  return cfg;
}

} // anonymous

namespace tt_eager::ops::unary {

at::Tensor& ttnn_abs_out(const at::Tensor& self, at::Tensor& out) {
    LOGGING("");
    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(out.device().type()  == c10::DeviceType::PrivateUse1);

    // grab the TTNN tensor handle
    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto  ttnn_tensor = self_impl->get_ttnn_tensor();

    // TTNN abs
    auto result = ttnn::abs(ttnn_tensor);

    // set up the output
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(out.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(self);
    out_impl->set_ttnn_tensor(result);
    return out;
}

at::Tensor ttnn_clone(
    const at::Tensor& self,
    c10::optional<at::MemoryFormat> memory_format_opt
) {
    LOGGING("Running aten::clone.default");
    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);

    // 1) extract TTNN tensor
    auto* self_impl   = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto  ttnn_tensor = self_impl->get_ttnn_tensor();

    // 2) build TTNN options
    ttnn::DType     dtype      = to_ttnn_dtype(self.scalar_type());
    at::MemoryFormat mf = memory_format_opt.value_or(at::MemoryFormat::Contiguous);
    ttnn::MemFormat mem_fmt    = to_ttnn_memformat(mf);
    ttnn::KernelConfig kernel_cfg = default_ttnn_kernel_config();

    // 3) invoke the TTNN clone
    auto cloned = ttnn::operations::data_movement::clone::Clone::invoke(
      ttnn_tensor,
      dtype,
      mem_fmt,
      kernel_cfg
    );

    // 4) wrap result back into an at::Tensor
    auto output = tt_eager::ops::create::custom_empty_memory_format(
      self.sizes(),
      self.scalar_type(),
      /*strides=*/c10::nullopt,
      /*device=*/self.device(),
      /*pin_memory=*/c10::nullopt,
      memory_format_opt
    );
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(self);
    out_impl->set_ttnn_tensor(cloned);

    return output;
}

at::Tensor ttnn_gelu(const at::Tensor& self) {
    LOGGING("Running aten::gelu.default");
    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);

    auto* self_impl   = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto  ttnn_tensor = self_impl->get_ttnn_tensor();

    if (ttnn_tensor.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_tensor = ttnn::to_layout(
          ttnn_tensor,
          ttnn::TILE_LAYOUT,
          /*queue_id=*/std::nullopt,
          /*kernel_cfg=*/std::nullopt,
          ttnn_tensor.device()
        );
    }
    auto result = ttnn::gelu(ttnn_tensor);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
      self.sizes(),
      self.scalar_type(),
      /*strides=*/c10::nullopt,
      self.device(),
      /*pin_memory=*/c10::nullopt
    );
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(self);
    out_impl->set_ttnn_tensor(result);
    return output;
}

at::Tensor ttnn_tanh(const at::Tensor& self) {
    LOGGING("Running aten::tanh.default");
    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);

    auto* self_impl   = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto  ttnn_tensor = self_impl->get_ttnn_tensor();
    if (ttnn_tensor.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_tensor = ttnn::to_layout(
          ttnn_tensor,
          ttnn::TILE_LAYOUT,
          /*queue_id=*/std::nullopt,
          /*kernel_cfg=*/std::nullopt,
          ttnn_tensor.device()
        );
    }
    auto result = ttnn::tanh(ttnn_tensor);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
      self.sizes(),
      self.scalar_type(),
      /*strides=*/c10::nullopt,
      self.device(),
      /*pin_memory=*/c10::nullopt
    );
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(self);
    out_impl->set_ttnn_tensor(result);
    return output;
}

}  // namespace tt_eager::ops::unary

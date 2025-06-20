#include "ttnn_cpp_extension/ops/view.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"

#include <ttnn/operations/data_movement/permute/permute.hpp>
#include <ttnn/operations/view/select.hpp>
#include <ttnn/operations/data_movement/slice/slice.hpp>
#include <ttnn/operations/data_movement/transpose/transpose.hpp>
#include <ttnn/operations/data_movement/unsqueeze/unsqueeze.hpp>
#include <ttnn/operations/view/reshape.hpp>

namespace tt_eager::ops::view {

TtnnTensor broadcast(const TtnnTensor& input, const Shape& target_shape) {
    // 1️⃣ Перевірка: чи можливий broadcast
    TORCH_CHECK(input.shape().rank() <= target_shape.rank(), "Incompatible ranks for broadcast");
    
    // Додати leading 1s якщо треба
    auto input_shape = input.shape().with_leading_ones(target_shape.rank());

    for (size_t i = 0; i < target_shape.rank(); ++i) {
        TORCH_CHECK(
            input_shape[i] == target_shape[i] || input_shape[i] == 1,
            "Cannot broadcast dim ", i, " from ", input_shape[i], " to ", target_shape[i]
        );
    }

    // 2️⃣ Обчислити strides
    SmallVector<uint32_t> new_strides(target_shape.rank());
    auto input_strides = input.strides().with_leading_zeros(target_shape.rank());

    for (size_t i = 0; i < target_shape.rank(); ++i) {
        new_strides[i] = (input_shape[i] == 1) ? 0 : input_strides[i];
    }

    // 3️⃣ Створити новий тензор (view)
    return TtnnTensor(
        input.buffer(),
        target_shape,
        new_strides,
        input.layout(),
        input.device()
    );
}

at::Tensor ttnn_view(const at::Tensor& self, at::IntArrayRef size) {
    LOGGING("Running aten::view.default");

    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);

    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = self_impl->get_ttnn_tensor();

    if (ttnn_tensor.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_tensor = ttnn::to_layout(
            ttnn_tensor, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_tensor.device());
    }

    // Check number of elements
    int64_t old_numel = self.numel();
    int64_t new_numel = 1;
    for (auto d : size) new_numel *= d;
    TORCH_CHECK(old_numel == new_numel, "View size is incompatible with input tensor size");

    // Convert shape
    ttnn::SmallVector<uint32_t> shape_u32(size.begin(), size.end());
    auto reshaped = ttnn::reshape(ttnn_tensor, ttnn::Shape(shape_u32));

    // Wrap result in at::Tensor
    auto output = tt_eager::ops::create::custom_empty_memory_format(
        size,
        self.scalar_type(),
        c10::nullopt,
        self.device(),
        c10::nullopt
    );

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_ttnn_tensor(reshaped);

    return output;
}  
at::Tensor ttnn_expand(const at::Tensor& self, at::IntArrayRef size, bool implicit) {
    LOGGING("Running aten::expand.default");

    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);

    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = self_impl->get_ttnn_tensor();

    if (ttnn_tensor.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_tensor = ttnn::to_layout(ttnn_tensor, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_tensor.device());
    }

    // Convert size to ttnn::Shape
    ttnn::SmallVector<uint32_t> target_shape_vec(size.begin(), size.end());
    ttnn::Shape target_shape(target_shape_vec);

    auto broadcasted_tensor = ttnn::broadcast(ttnn_tensor, target_shape);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        size,
        c10::optional<at::ScalarType>(self.scalar_type()),
        c10::nullopt,
        c10::optional<at::Device>(self.device()),
        c10::nullopt
    );

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_sizes_and_strides_as(self);  // Optional: may adjust for view-like API
    out_impl->set_ttnn_tensor(broadcasted_tensor);

    return output;
}
at::Tensor ttnn_permute(const at::Tensor& input, at::IntArrayRef dims) {
    LOGGING("Running aten::permute.default");

    TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK((int64_t)dims.size() == input.dim(), "Mismatched permute dims and input rank");

    auto* input_impl = static_cast<at::TtnnTensorImpl*>(input.unsafeGetTensorImpl());
    auto ttnn_input = input_impl->get_ttnn_tensor();

    if (ttnn_input.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_input = ttnn::to_layout(ttnn_input, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_input.device());
    }

    // Convert dims to SmallVector
    ttnn::SmallVector<uint32_t> perm(dims.begin(), dims.end());

    // Perform permute
    auto ttnn_output = ttnn::permute(ttnn_input, perm);

    // Wrap into output tensor
    auto output = tt_eager::ops::create::custom_empty_memory_format(
        ttnn_output.shape().to_sizes(),
        c10::optional<at::ScalarType>(input.scalar_type()),
        c10::nullopt,
        c10::optional<at::Device>(input.device()),
        c10::nullopt
    );

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_ttnn_tensor(ttnn_output);

    return output;
}
at::Tensor ttnn_select_int(const at::Tensor& input, int64_t dim, int64_t index) {
    LOGGING("Running aten::select.int");

    TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1);

    auto* input_impl = static_cast<at::TtnnTensorImpl*>(input.unsafeGetTensorImpl());
    auto ttnn_input = input_impl->get_ttnn_tensor();

    if (ttnn_input.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_input = ttnn::to_layout(ttnn_input, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_input.device());
    }

    // Run select
    auto ttnn_output = ttnn::select(ttnn_input, static_cast<int>(dim), static_cast<int>(index));

    // Wrap into new tensor
    auto output = tt_eager::ops::create::custom_empty_memory_format(
        ttnn_output.shape().to_sizes(),
        c10::optional<at::ScalarType>(input.scalar_type()),
        c10::nullopt,
        c10::optional<at::Device>(input.device()),
        c10::nullopt
    );

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_ttnn_tensor(ttnn_output);

    return output;
}
at::Tensor ttnn_slice_tensor(const at::Tensor& self, int64_t dim, int64_t start, int64_t end, int64_t step) {
    LOGGING("Running aten::slice.Tensor");

    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(step > 0, "Only positive step is supported in TTNN slice");

    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = self_impl->get_ttnn_tensor();

    if (ttnn_tensor.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_tensor = ttnn::to_layout(ttnn_tensor, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_tensor.device());
    }

    // Clamp end if it's out of bounds
    int64_t dim_size = static_cast<int64_t>(self.size(dim));
    if (end > dim_size) end = dim_size;

    // Call TTNN slice kernel
    auto ttnn_result = ttnn::slice(
        ttnn_tensor,
        static_cast<int>(dim),
        static_cast<int>(start),
        static_cast<int>(end),
        static_cast<int>(step)
    );

    // Wrap the result
    auto output = tt_eager::ops::create::custom_empty_memory_format(
        ttnn_result.shape().to_sizes(),
        c10::optional<at::ScalarType>(self.scalar_type()),
        c10::nullopt,
        c10::optional<at::Device>(self.device()),
        c10::nullopt
    );

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_ttnn_tensor(ttnn_result);

    return output;
}
at::Tensor ttnn_t_default(const at::Tensor& self) {
    LOGGING("Running aten::t.default");

    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(self.dim() == 2, "aten::t.default only supports 2D tensors");

    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = self_impl->get_ttnn_tensor();

    if (ttnn_tensor.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_tensor = ttnn::to_layout(ttnn_tensor, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_tensor.device());
    }

    auto ttnn_result = ttnn::transpose(ttnn_tensor, 0, 1);  // transpose the two dims

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        ttnn_result.shape().to_sizes(),
        self.scalar_type(),
        c10::nullopt,
        self.device(),
        c10::nullopt
    );

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_ttnn_tensor(ttnn_result);

    return output;
}
at::Tensor ttnn_transpose_int(const at::Tensor& input, int64_t dim0, int64_t dim1) {
    LOGGING("Running aten::transpose.int");

    TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(input.dim() >= 2, "transpose requires tensor with 2 or more dimensions");

    auto* input_impl = static_cast<at::TtnnTensorImpl*>(input.unsafeGetTensorImpl());
    auto ttnn_input = input_impl->get_ttnn_tensor();

    if (ttnn_input.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_input = ttnn::to_layout(ttnn_input, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_input.device());
    }

    auto ttnn_output = ttnn::transpose(ttnn_input, static_cast<int>(dim0), static_cast<int>(dim1));

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        ttnn_output.shape().to_sizes(),
        input.scalar_type(),
        c10::nullopt,
        input.device(),
        c10::nullopt
    );

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_ttnn_tensor(ttnn_output);

    return output;
}
at::Tensor ttnn_unsqueeze(const at::Tensor& self, int64_t dim) {
    LOGGING("Running aten::unsqueeze.default");

    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);

    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = self_impl->get_ttnn_tensor();

    if (ttnn_tensor.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_tensor = ttnn::to_layout(ttnn_tensor, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_tensor.device());
    }

    int rank = static_cast<int>(self.dim());
    TORCH_CHECK(dim >= -rank - 1 && dim <= rank, "Invalid dimension for unsqueeze");

    // Normalize dim
    if (dim < 0) dim += rank + 1;

    // Apply TTNN unsqueeze
    auto ttnn_result = ttnn::unsqueeze(ttnn_tensor, dim);

    // Wrap result in at::Tensor
    auto output = tt_eager::ops::create::custom_empty_memory_format(
        ttnn_result.shape().to_sizes(),
        self.scalar_type(),
        c10::nullopt,
        self.device(),
        c10::nullopt
    );

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_ttnn_tensor(ttnn_result);

    return output;
}

}  // namespace tt_eager::ops::view

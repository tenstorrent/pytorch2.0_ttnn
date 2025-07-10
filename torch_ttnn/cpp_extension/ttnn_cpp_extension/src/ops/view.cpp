#include "ttnn_cpp_extension/ops/view.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"

#include <ttnn/operations/data_movement/permute/permute.hpp>
#include <ttnn/operations/data_movement/slice/slice.hpp>
#include <ttnn/operations/data_movement/transpose/transpose.hpp>
#include <ttnn/operations/data_movement/unsqueeze/unsqueeze.hpp>
#include <ttnn/operations/data_movement/reshape_view/reshape.hpp>
#include "ttnn/operations/data_movement/split/split.hpp"


namespace tt_eager::ops::view {

    TtnnTensor select(const TtnnTensor& input, int dim, int index) {
        TORCH_CHECK(dim >= 0 && dim < input.logical_shape().rank(), "Invalid dim for select");
        TORCH_CHECK(index >= 0 && index < input.logical_shape()[dim], "Index out of bounds");

        auto new_shape = std::vector<uint32_t>(input.logical_shape().cbegin(), input.logical_shape().cend());
        new_shape.erase(new_shape.begin() + dim);

        return TtnnTensor(
            std::shared_ptr<tt::tt_metal::Buffer>(input.buffer()),                     // HostBuffer
            ttnn::Shape(new_shape),              // Shape (логічна + паддинг однакова)
            input.dtype(),                       // DataType
            input.layout(),                      // Layout
            std::nullopt                         // Tile — якщо не потрібен спеціальний
        );
    }

    TtnnTensor broadcast(const TtnnTensor& input, const ttnn::Shape& target_shape) {
        TORCH_CHECK(input.logical_shape().rank() <= target_shape.rank(), "Incompatible ranks for broadcast");

        auto raw_shape = input.logical_shape();
        ttnn::SmallVector<uint32_t> input_shape(target_shape.rank(), 1);

        for (size_t i = 0; i < raw_shape.rank(); ++i) {
            input_shape[target_shape.rank() - raw_shape.rank() + i] = raw_shape[i];
        }

        for (size_t i = 0; i < target_shape.rank(); ++i) {
            TORCH_CHECK(
                input_shape[i] == target_shape[i] || input_shape[i] == 1,
                "Cannot broadcast dim ", i, " from ", input_shape[i], " to ", target_shape[i]
            );
        }

        // Створення broadcast view — нові strides (але не використовуються явно в конструкторі)
        ttnn::SmallVector<uint32_t> new_strides(target_shape.rank());
        auto raw_input_strides = input.strides();
        ttnn::SmallVector<uint32_t> input_strides(target_shape.rank(), 0);

        for (int i = 0; i < raw_input_strides.rank(); ++i) {
            input_strides[target_shape.rank() - raw_input_strides.rank() + i] = raw_input_strides[i];
        }

        for (size_t i = 0; i < target_shape.rank(); ++i) {
            new_strides[i] = (input_shape[i] == 1) ? 0 : input_strides[i];
        }

        return TtnnTensor(
            std::shared_ptr<tt::tt_metal::Buffer>(input.buffer()),
            target_shape,            // logical_shape
            target_shape,            // padded_shape (можна окремо, якщо потрібно)
            input.dtype(),           // DataType
            input.layout(),          // Layout
            std::nullopt             // Tile
        );
    }

    at::Tensor ttnn_view(const at::Tensor& self, at::IntArrayRef size) {
        std::cerr << "[TTNN] ttnn_view/reshape called with sizes: ";
        for (auto d : size) std::cerr << d << " ";
        std::cerr << "\n";
        
        LOGGING("Running aten::view.default");

        TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);

        auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
        auto ttnn_tensor = self_impl->get_ttnn_tensor();

        if (ttnn_tensor.layout() == ttnn::ROW_MAJOR_LAYOUT) {
            ttnn_tensor = ttnn::to_layout(
                ttnn_tensor, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_tensor.device());
        }

        int64_t old_numel = self.numel();

        // 1) Find any “-1” and compute prod of known dims
        int unknown_idx = -1;
        int64_t known_prod = 1;
        auto size_vec = size.vec();  // copy into a mutable vector
        for (int i = 0; i < (int)size_vec.size(); ++i) {
            int64_t dim = size_vec[i];
            if (dim == -1) {
                TORCH_CHECK(unknown_idx == -1, "only one dimension can be inferred");
                unknown_idx = i;
            } else {
                TORCH_CHECK(dim >= 0, "view dims must be non-negative or -1");
                known_prod *= dim;
            }
        }

        // 2) If there was a “-1”, infer it now
        if (unknown_idx != -1) {
            TORCH_CHECK(known_prod != 0 && old_numel % known_prod == 0,
                        "cannot infer dimension size for view");
            int64_t inferred = old_numel / known_prod;
            size_vec[unknown_idx] = static_cast<int32_t>(inferred);
        }

        // 3) Final check (now size_vec is all non-negative)
        int64_t new_numel = 1;
        for (auto d : size_vec) new_numel *= d;
        TORCH_CHECK(old_numel == new_numel,
                    "View size is incompatible with input tensor size");

        // 4) Do the reshape in TTNN
        tt::stl::SmallVector<int32_t> shape_i32(size_vec.begin(), size_vec.end());
        auto reshaped = ttnn::reshape(ttnn_tensor, shape_i32);

        auto output = tt_eager::ops::create::custom_empty_memory_format(
            size_vec,
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

        ttnn::SmallVector<uint32_t> target_shape_vec(size.begin(), size.end());
        ttnn::Shape target_shape(target_shape_vec);

        auto broadcasted_tensor = broadcast(ttnn_tensor, target_shape);

        auto output = tt_eager::ops::create::custom_empty_memory_format(
            size,
            c10::optional<at::ScalarType>(self.scalar_type()),
            c10::nullopt,
            c10::optional<at::Device>(self.device()),
            c10::nullopt
        );

        auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
        out_impl->set_sizes_and_strides_as(self);
        out_impl->set_ttnn_tensor(broadcasted_tensor);

        return output;
    }

    at::Tensor ttnn_permute(const at::Tensor& input, at::IntArrayRef dims) {
        TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1);
        TORCH_CHECK(dims.size() == (size_t)input.dim(), "Mismatched permute dims");

        // 1) Отримуємо внутрішній TTNN tensor
        auto* impl = static_cast<at::TtnnTensorImpl*>(input.unsafeGetTensorImpl());
        auto ttnn_input = impl->get_ttnn_tensor();

        // 2) Копіюємо dims у SmallVector<int64_t>
        ttnn::SmallVector<int64_t> perm_i64;
        perm_i64.reserve(dims.size());
        for (auto d : dims) {
            perm_i64.push_back(static_cast<int64_t>(d));
        }

        // 3а) Варіант A: виклик через декоратор
        auto ttnn_output = ttnn::permute(               // цей alias зареєстрований у permute.hpp
            ttnn_input,
            perm_i64
        );

        // 3b) Варіант B: прямий виклик invoke (обирай один із двох)
        // auto ttnn_output = ttnn::operations::data_movement::ExecutePermute::invoke(
        //     ttnn_input,
        //     perm_i64,
        //     /*memory_config=*/std::nullopt,
        //     /*pad_value=*/0.0f
        // );

        // 4) Створюємо порожню ATen-Tensorку з потрібними розмірами
        std::vector<int64_t> out_sizes(input.dim());
        for (int i = 0; i < input.dim(); ++i) {
            out_sizes[i] = input.size(dims[i]);
        }
        auto output = tt_eager::ops::create::custom_empty_memory_format(
            out_sizes,
            input.scalar_type(),
            c10::nullopt,
            input.device(),
            c10::nullopt
        );
        auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
        out_impl->set_ttnn_tensor(ttnn_output);
        return output;
    }

    at::Tensor ttnn_slice_tensor(const at::Tensor& input,
                                int64_t dim,
                                c10::optional<c10::SymInt> start,
                                c10::optional<c10::SymInt> end,
                                c10::SymInt step) {
        TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1,
                    "ttnn_slice: expected tensor on PrivateUse1 device");

        TORCH_CHECK(step.expect_int() == 1,
            "ttnn_slice: only step == 1 is currently supported");

        // Extract the start and end values from SymInt or default
        int64_t dim_size = input.sym_size(dim).expect_int();
        int64_t start_val = start.has_value() ? start->expect_int() : 0;
        int64_t end_val = end.has_value() ? end->expect_int() : dim_size;

        // Clamp to valid range
        start_val = std::clamp(start_val, int64_t(0), dim_size);
        end_val   = std::clamp(end_val, int64_t(0), dim_size);

        auto* impl = static_cast<at::TtnnTensorImpl*>(input.unsafeGetTensorImpl());
        auto ttnn_input = impl->get_ttnn_tensor();

        ttnn::SmallVector<int> begins(input.dim(), 0);
        ttnn::SmallVector<int> ends(input.dim(), 0);
        ttnn::SmallVector<int> steps(input.dim(), 1);

        for (int i = 0; i < input.dim(); ++i) {
            if (i == dim) {
                begins[i] = static_cast<int>(start_val);
                ends[i]   = static_cast<int>(end_val);
            } else {
                begins[i] = 0;
                ends[i] = static_cast<int>(input.size(i));
            }
        }

        auto ttnn_output = ttnn::slice(ttnn_input, begins, ends, steps);

        std::vector<int64_t> out_sizes = input.sizes().vec();
        out_sizes[dim] = end_val - start_val;

        auto output = tt_eager::ops::create::custom_empty_memory_format(
            out_sizes,
            input.scalar_type(),
            /*strides=*/c10::nullopt,
            input.device(),
            /*pin_memory=*/c10::nullopt
        );

        auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
        out_impl->set_sizes_and_strides_as(input);  // copy strides
        out_impl->set_ttnn_tensor(ttnn_output);

        return output;
    }

    std::vector<at::Tensor> ttnn_split_tensor_fixed(
    const at::Tensor& self,
    c10::SymInt split_size,
    int64_t dim
    ) {
        LOGGING("Running aten::split.Tensor (fixed size)");

        TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1,
                    "Tensor must be on PrivateUse1 device");
        // Перетворюємо SymInt у звичайне ціле
        int64_t split_sz = split_size.as_int_unchecked();
        TORCH_CHECK(split_sz > 0, "Split size must be positive");

        // Дістаємо внутрішній TTNN-тензор
        auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
        ttnn::Tensor ttnn_tensor = self_impl->get_ttnn_tensor();

        // За потреби конвертуємо layout
        if (ttnn_tensor.layout() == ttnn::ROW_MAJOR_LAYOUT) {
            ttnn_tensor = ttnn::to_layout(
                ttnn_tensor,
                ttnn::TILE_LAYOUT,
                std::nullopt,
                std::nullopt,
                ttnn_tensor.device()
            );
        }

        // Викликаємо TTNN split
        auto ttnn_outputs = ttnn::split(ttnn_tensor, split_sz, dim, std::nullopt);

        // Обгортаємо кожен результат у at::Tensor із власним TtnnTensorImpl
        std::vector<at::Tensor> outputs;
        outputs.reserve(ttnn_outputs.size());
        for (const auto& t : ttnn_outputs) {
            // Формуємо shape для нового тензора
            std::vector<int64_t> shape_vec(
                t.logical_shape().cbegin(),
                t.logical_shape().cend()
            );

            // Створюємо порожній at::Tensor з потрібним розміром та device
            auto output = tt_eager::ops::create::custom_empty_memory_format(
                shape_vec,
                self.scalar_type(),
                c10::nullopt,
                self.device(),
                c10::nullopt
            );

            // Встановлюємо внутрішній ttnn-об’єкт
            auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
            out_impl->set_ttnn_tensor(t);

            outputs.emplace_back(std::move(output));
        }

        return outputs;
    }

    std::vector<at::Tensor> ttnn_split_tensor_sections(const at::Tensor& self, at::IntArrayRef sections, int64_t dim) {
        LOGGING("Running aten::split.Tensor (section sizes)");

        TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);
        TORCH_CHECK(!sections.empty(), "Split sections cannot be empty");

        auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
        auto ttnn_tensor = self_impl->get_ttnn_tensor();

        if (ttnn_tensor.layout() == ttnn::ROW_MAJOR_LAYOUT) {
            ttnn_tensor = ttnn::to_layout(ttnn_tensor, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_tensor.device());
        }

        ttnn::SmallVector<int64_t> split_sizes(sections.begin(), sections.end());
        auto ttnn_outputs = ttnn::split(ttnn_tensor, split_sizes, dim, std::nullopt);

        std::vector<at::Tensor> outputs;
        for (const auto& t : ttnn_outputs) {
            std::vector<int64_t> shape_vec(t.logical_shape().cbegin(), t.logical_shape().cend());
            auto output = tt_eager::ops::create::custom_empty_memory_format(
                shape_vec, self.scalar_type(), c10::nullopt, self.device(), c10::nullopt
            );
            auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
            out_impl->set_ttnn_tensor(t);
            outputs.push_back(std::move(output));
        }

        return outputs;
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

        const auto& logical_shape = ttnn_result.logical_shape();
        std::vector<int64_t> shape_vec(logical_shape.cbegin(), logical_shape.cend());

        auto output = tt_eager::ops::create::custom_empty_memory_format(
            shape_vec,
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
        const auto& logical_shape = ttnn_output.logical_shape();
        std::vector<int64_t> shape_vec(logical_shape.cbegin(), logical_shape.cend());


        auto output = tt_eager::ops::create::custom_empty_memory_format(
            shape_vec,
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

        const auto& logical_shape = ttnn_result.logical_shape();
        std::vector<int64_t> shape_vec(logical_shape.cbegin(), logical_shape.cend());

        // Wrap result in at::Tensor
        auto output = tt_eager::ops::create::custom_empty_memory_format(
            shape_vec,
            self.scalar_type(),
            c10::nullopt,
            self.device(),
            c10::nullopt
        );

        auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
        out_impl->set_ttnn_tensor(ttnn_result);

        return output;
    }

    at::Tensor ttnn_as_strided(
        const at::Tensor& self,
        at::IntArrayRef size,
        at::IntArrayRef stride,
        c10::optional<int64_t> storage_offset
    ) {
        LOGGING("Running aten::as_strided");

        TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1, "Tensor must be on TTNN device");

        auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
        auto ttnn_tensor = self_impl->get_ttnn_tensor();

        // 1. Reject unsafe or unsupported cases
        TORCH_CHECK(!storage_offset.has_value() || storage_offset.value() == 0, "TTNN backend does not support storage_offset != 0");
        
        int64_t expected_stride = 1;
        for (int64_t i = size.size() - 1; i >= 0; --i) {
            if (stride[i] != expected_stride) {
                TORCH_CHECK(false, "TTNN as_strided only supports contiguous views for now");
            }
            expected_stride *= size[i];
        }

        // 2. Use reshape if compatible
        tt::stl::SmallVector<int32_t> new_shape(size.begin(), size.end());
        auto reshaped = ttnn::reshape(ttnn_tensor, new_shape);

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

}  // namespace tt_eager::ops::view
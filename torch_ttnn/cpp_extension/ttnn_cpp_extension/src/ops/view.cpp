#include "ttnn_cpp_extension/ops/view.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include "ttnn_cpp_extension/utils/extension_utils.hpp"

#include <ttnn/operations/data_movement/permute/permute.hpp>
#include <ttnn/operations/data_movement/slice/slice.hpp>
#include <ttnn/operations/data_movement/transpose/transpose.hpp>
#include <ttnn/operations/data_movement/unsqueeze/unsqueeze.hpp>
#include <ttnn/operations/data_movement/squeeze/squeeze.hpp>
#include <ttnn/operations/data_movement/reshape_view/reshape.hpp>
#include "ttnn/operations/data_movement/split/split.hpp"
#include <ttnn/operations/experimental/bcast_to/bcast_to.hpp>

namespace tt_eager::ops::view {

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

    auto broadcasted_tensor = ttnn::experimental::broadcast_to(
        ttnn_tensor,
        target_shape,
        std::nullopt,  // memory_config
        std::nullopt   // output
    );

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        size, self.scalar_type(), c10::nullopt, self.device(), c10::nullopt);

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_ttnn_tensor(broadcasted_tensor);

    return output;
}

at::Tensor ttnn_view(const at::Tensor& self, at::IntArrayRef size) {
    LOGGING("Running aten::view.default");

    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1, "Tensor must be on TTNN device");

    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = self_impl->get_ttnn_tensor();

    if (ttnn_tensor.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_tensor = ttnn::to_layout(ttnn_tensor, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_tensor.device());
    }

    auto ttnn_input_shape = ttnn_tensor.logical_shape();

    int64_t original_numel = 1;
    for (int i = 0; i < self.dim(); ++i) {
        original_numel *= self.size(i);
    }

    std::vector<int64_t> new_size(size.begin(), size.end());
    int unknown_idx = -1;
    int64_t known_product = 1;

    for (int i = 0; i < new_size.size(); i++) {
        if (new_size[i] == -1) {
            TORCH_CHECK(unknown_idx == -1, "only one dimension can be inferred");
            unknown_idx = i;
        } else {
            TORCH_CHECK(new_size[i] >= 0, "Negative size dimensions are not supported");
            known_product *= new_size[i];
        }
    }

    if (unknown_idx >= 0) {
        TORCH_CHECK(known_product != 0 && original_numel % known_product == 0, "cannot infer dimension size");
        new_size[unknown_idx] = original_numel / known_product;
    }

    int64_t new_numel = 1;
    for (int64_t s : new_size) {
        new_numel *= s;
    }

    TORCH_CHECK(
        original_numel == new_numel,
        "view size is not compatible with input tensor's size: old=",
        original_numel,
        ", new=",
        new_numel);

    tt::stl::SmallVector<int32_t> new_shape(new_size.begin(), new_size.end());
    auto reshaped_tensor = ttnn::reshape(ttnn_tensor, new_shape);

    auto reshaped_shape = reshaped_tensor.logical_shape();

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        new_size, self.scalar_type(), c10::nullopt, self.device(), c10::nullopt);

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_ttnn_tensor(reshaped_tensor);

    return output;
}

at::Tensor ttnn_permute(const at::Tensor& input, at::IntArrayRef dims) {
    TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1);
    TORCH_CHECK(dims.size() == (size_t)input.dim(), "Mismatched permute dims");

    auto* impl = static_cast<at::TtnnTensorImpl*>(input.unsafeGetTensorImpl());
    auto ttnn_input = impl->get_ttnn_tensor();

    ttnn::SmallVector<int64_t> perm_i64;
    perm_i64.reserve(dims.size());
    for (auto d : dims) {
        perm_i64.push_back(static_cast<int64_t>(d));
    }

    auto ttnn_output = ttnn::permute(ttnn_input, perm_i64);

    std::vector<int64_t> out_sizes(input.dim());
    for (int i = 0; i < input.dim(); ++i) {
        out_sizes[i] = input.size(dims[i]);
    }
    auto output = tt_eager::ops::create::custom_empty_memory_format(
        out_sizes, input.scalar_type(), c10::nullopt, input.device(), c10::nullopt);
    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_ttnn_tensor(ttnn_output);
    return output;
}

at::Tensor ttnn_slice_tensor(
    const at::Tensor& input,
    int64_t dim,
    c10::optional<c10::SymInt> start,
    c10::optional<c10::SymInt> end,
    c10::SymInt step) {
    TORCH_CHECK(
        input.device().type() == c10::DeviceType::PrivateUse1, "ttnn_slice: expected tensor on PrivateUse1 device");

    TORCH_CHECK(step.expect_int() == 1, "ttnn_slice: only step == 1 is currently supported");

    int64_t dim_size = input.sym_size(dim).expect_int();
    int64_t start_val = start.has_value() ? start->expect_int() : 0;
    int64_t end_val = end.has_value() ? end->expect_int() : dim_size;

    start_val = std::clamp(start_val, int64_t(0), dim_size);
    end_val = std::clamp(end_val, int64_t(0), dim_size);

    auto* impl = static_cast<at::TtnnTensorImpl*>(input.unsafeGetTensorImpl());
    auto ttnn_input = impl->get_ttnn_tensor();

    ttnn::SmallVector<int> begins(input.dim(), 0);
    ttnn::SmallVector<int> ends(input.dim(), 0);
    ttnn::SmallVector<int> steps(input.dim(), 1);

    for (int i = 0; i < input.dim(); ++i) {
        if (i == dim) {
            begins[i] = static_cast<int>(start_val);
            ends[i] = static_cast<int>(end_val);
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
        /*pin_memory=*/c10::nullopt);

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());

    out_impl->set_ttnn_tensor(ttnn_output);

    return output;
}

std::vector<at::Tensor> ttnn_split_tensor_fixed(const at::Tensor& self, c10::SymInt split_size, int64_t dim) {
    LOGGING("Running aten::split.Tensor (fixed size)");

    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1, "Tensor must be on PrivateUse1 device");
    int64_t split_sz;
    if (split_size.is_symbolic()) {
        split_sz = split_size.guard_int(__FILE__, __LINE__);
    } else {
        split_sz = split_size.as_int_unchecked();
    }
    TORCH_CHECK(split_sz > 0, "Split size must be positive");

    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    ttnn::Tensor ttnn_tensor = self_impl->get_ttnn_tensor();

    if (ttnn_tensor.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_tensor = ttnn::to_layout(ttnn_tensor, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_tensor.device());
    }

    int64_t normalized_dim = dim;
    if (normalized_dim < 0) {
        normalized_dim += ttnn_tensor.get_logical_shape().rank();
    }

    auto ttnn_outputs = ttnn::split(ttnn_tensor, split_sz, normalized_dim, std::nullopt);

    std::vector<at::Tensor> outputs;
    outputs.reserve(ttnn_outputs.size());
    for (const auto& t : ttnn_outputs) {
        std::vector<int64_t> shape_vec(t.get_logical_shape().cbegin(), t.get_logical_shape().cend());

        auto output = tt_eager::ops::create::custom_empty_memory_format(
            shape_vec, self.scalar_type(), c10::nullopt, self.device(), c10::nullopt);

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
            shape_vec, self.scalar_type(), c10::nullopt, self.device(), c10::nullopt);
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
        shape_vec, self.scalar_type(), c10::nullopt, self.device(), c10::nullopt);

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_ttnn_tensor(ttnn_result);

    return output;
}

at::Tensor ttnn_transpose_int(const at::Tensor& input, int64_t dim0, int64_t dim1) {
    LOGGING("Running aten::transpose.int");

    TORCH_CHECK(input.device().type() == c10::DeviceType::PrivateUse1);

    auto* input_impl = static_cast<at::TtnnTensorImpl*>(input.unsafeGetTensorImpl());
    auto ttnn_input = input_impl->get_ttnn_tensor();

    if (ttnn_input.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_input = ttnn::to_layout(ttnn_input, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_input.device());
    }

    auto ttnn_input_shape = ttnn_input.logical_shape();

    int64_t ndim = input.dim();
    if (dim0 < 0) {
        dim0 += ndim;
    }
    if (dim1 < 0) {
        dim1 += ndim;
    }

    TORCH_CHECK(dim0 >= 0 && dim0 < ndim, "dim0 out of range");
    TORCH_CHECK(dim1 >= 0 && dim1 < ndim, "dim1 out of range");

    auto ttnn_output = ttnn::transpose(ttnn_input, static_cast<int>(dim0), static_cast<int>(dim1));

    auto ttnn_output_shape = ttnn_output.logical_shape();

    std::vector<int64_t> output_shape(input.sizes().begin(), input.sizes().end());
    std::swap(output_shape[dim0], output_shape[dim1]);

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        output_shape, input.scalar_type(), c10::nullopt, input.device(), c10::nullopt);

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

    if (dim < 0) {
        dim += rank + 1;
    }

    auto ttnn_result = ttnn::unsqueeze(ttnn_tensor, dim);

    const auto& logical_shape = ttnn_result.logical_shape();
    std::vector<int64_t> shape_vec(logical_shape.cbegin(), logical_shape.cend());

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        shape_vec, self.scalar_type(), c10::nullopt, self.device(), c10::nullopt);

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_ttnn_tensor(ttnn_result);

    return output;
}

at::Tensor ttnn_squeeze_dim(const at::Tensor& self, int64_t dim) {
    LOGGING("Running aten::squeeze.dim");

    TORCH_CHECK(self.device().type() == c10::DeviceType::PrivateUse1);

    auto* self_impl = static_cast<at::TtnnTensorImpl*>(self.unsafeGetTensorImpl());
    auto ttnn_tensor = self_impl->get_ttnn_tensor();

    if (ttnn_tensor.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        ttnn_tensor = ttnn::to_layout(ttnn_tensor, ttnn::TILE_LAYOUT, std::nullopt, std::nullopt, ttnn_tensor.device());
    }

    int rank = static_cast<int>(self.dim());
    TORCH_CHECK(dim >= -rank && dim < rank, "Invalid dimension for squeeze");

    if (dim < 0) {
        dim += rank;
    }

    TORCH_CHECK(self.size(dim) == 1, "Cannot squeeze dimension that is not of size 1");

    auto ttnn_result = ttnn::squeeze(ttnn_tensor, static_cast<int>(dim));

    const auto& logical_shape = ttnn_result.logical_shape();
    std::vector<int64_t> shape_vec(logical_shape.cbegin(), logical_shape.cend());

    auto output = tt_eager::ops::create::custom_empty_memory_format(
        shape_vec, self.scalar_type(), c10::nullopt, self.device(), c10::nullopt);

    auto* out_impl = static_cast<at::TtnnTensorImpl*>(output.unsafeGetTensorImpl());
    out_impl->set_ttnn_tensor(ttnn_result);

    return output;
}

}  // namespace tt_eager::ops::view

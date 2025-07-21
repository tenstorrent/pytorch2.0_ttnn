#include "ttnn_cpp_extension/ops/slice.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include <ttnn/operations/data_movement/slice/slice.hpp>
#include <algorithm>

namespace tt_eager::ops::slice {

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

}  // namespace tt_eager::ops::slice

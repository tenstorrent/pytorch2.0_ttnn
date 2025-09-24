#include "ttnn_cpp_extension/ops/permute.hpp"
#include "ttnn_cpp_extension/ops/creation.hpp"
#include "ttnn_cpp_extension/core/TtnnTensorImpl.hpp"
#include <ttnn/operations/data_movement/permute/permute.hpp>

namespace tt_eager::ops::permute {

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

}  // namespace tt_eager::ops::permute

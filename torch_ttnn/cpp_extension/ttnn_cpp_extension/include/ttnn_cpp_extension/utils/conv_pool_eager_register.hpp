#pragma once

#include "ttnn_cpp_extension/utils/conv_pool_eager_wrappers.hpp"

#include <ttnn/operations/conv/conv1d/conv1d.hpp>
#include <ttnn/operations/conv/conv2d/conv2d.hpp>
#include <ttnn/operations/conv/conv_transpose2d/conv_transpose2d.hpp>
#include <ttnn/operations/experimental/conv3d/conv3d.hpp>
#include <ttnn/operations/pool/generic/generic_pools.hpp>
#include <ttnn/operations/pool/global_avg_pool/global_avg_pool.hpp>

#include <torch/library.h>

namespace {
// Generic convolution dispatcher matching aten.convolution/overrideable
// Signature must match native_functions.yaml schema
static at::Tensor aten_convolution_dispatch(
    const at::Tensor& input,
    const at::Tensor& weight,
    const c10::optional<at::Tensor>& bias,
    c10::IntArrayRef stride,
    c10::IntArrayRef padding,
    c10::IntArrayRef dilation,
    bool transposed,
    c10::IntArrayRef output_padding,
    int64_t groups) {
    const int64_t dim = input.dim();
    TORCH_CHECK(dim == weight.dim(), "convolution: input and weight must have same rank");
    if (!transposed) {
        if (dim == 3) {
            return tt_eager::ext::conv1d_aten::invoke(input, weight, bias, stride, padding, dilation, groups);
        } else if (dim == 4) {
            return tt_eager::ext::conv2d_aten::invoke(input, weight, bias, stride, padding, dilation, groups);
        } else if (dim == 5) {
            return tt_eager::ext::conv3d_aten::invoke(input, weight, bias, stride, padding, dilation, groups);
        }
        TORCH_CHECK(false, "convolution: unsupported input dim=", dim, " (expected 3,4,5)");
    } else {
        TORCH_CHECK(dim != 3, "convolution: transposed 1D not yet supported on TTNN");
        if (dim == 4) {
            return tt_eager::ext::conv_transpose2d_aten::invoke(
                input, weight, bias, stride, padding, output_padding, groups, dilation);
        }
        TORCH_CHECK(false, "convolution: transposed dim=", dim, " not yet supported on TTNN");
    }
}
}  // namespace

namespace tt_eager::ext {

static inline void register_conv_and_pool_ops(torch::Library& m) {
    // =========================
    // Convolution ops
    // =========================

    // Implemented via TTNN wrappers (Conv):
    // conv1d
    // schema: conv1d(Tensor input, Tensor weight, Tensor? bias=None, SymInt[1] stride=1, SymInt[1] padding=0, SymInt[1]
    // dilation=1, SymInt groups=1) -> Tensor
    m.impl("conv1d", TORCH_FN(tt_eager::ext::conv1d_aten::invoke));
    // conv2d
    // schema: conv2d(Tensor input, Tensor weight, Tensor? bias=None, SymInt[2] stride=1, SymInt[2] padding=0, SymInt[2]
    // dilation=1, SymInt groups=1) -> Tensor
    m.impl("conv2d", TORCH_FN(tt_eager::ext::conv2d_aten::invoke));
    // conv3d (uses ttnn::experimental::conv3d)
    // schema: conv3d(Tensor input, Tensor weight, Tensor? bias=None, SymInt[3] stride=1, SymInt[3] padding=0, SymInt[3]
    // dilation=1, SymInt groups=1) -> Tensor
    m.impl("conv3d", TORCH_FN(tt_eager::ext::conv3d_aten::invoke));
    // conv_transpose2d.input
    // schema: conv_transpose2d.input(Tensor input, Tensor weight, Tensor? bias=None, SymInt[2] stride=1, SymInt[2]
    // padding=0, SymInt[2] output_padding=0, SymInt groups=1, SymInt[2] dilation=1) -> Tensor
    m.impl("conv_transpose2d.input", TORCH_FN(tt_eager::ext::conv_transpose2d_aten::invoke));

    // Register generic convolution entry points
    // schema: convolution(Tensor input, Tensor weight, Tensor? bias, SymInt[] stride, SymInt[] padding, SymInt[]
    // dilation, bool transposed, SymInt[] output_padding, SymInt groups) -> Tensor
    m.impl("convolution", TORCH_FN(aten_convolution_dispatch));
    // schema: convolution_overrideable(Tensor input, Tensor weight, Tensor? bias, SymInt[] stride, SymInt[] padding,
    // SymInt[] dilation, bool transposed, SymInt[] output_padding, SymInt groups) -> Tensor
    m.impl("convolution_overrideable", TORCH_FN(aten_convolution_dispatch));

    // Pooling (2D):
    // schema: max_pool2d(Tensor self, int[2] kernel_size, int[2] stride=[], int[2] padding=0, int[2] dilation=1, bool
    // ceil_mode=False) -> Tensor
    m.impl("max_pool2d", TORCH_FN(tt_eager::ext::max_pool2d_aten::invoke));
    // schema: avg_pool2d(Tensor self, int[2] kernel_size, int[2] stride=[], int[2] padding=0, bool ceil_mode=False,
    // bool count_include_pad=True) -> Tensor
    m.impl("avg_pool2d", TORCH_FN(tt_eager::ext::avg_pool2d_aten::invoke));

    // schema: adaptive_avg_pool2d(Tensor self, SymInt[2] output_size) -> Tensor
    m.impl("adaptive_avg_pool2d", TORCH_FN(tt_eager::ext::adaptive_avg_pool2d_aten::invoke));

    // Not implemented yet:
    // m.impl("_convolution", ...);
    // m.impl("_convolution_mode", ...);
    // m.impl("conv1d.padding", ...);
    // m.impl("conv2d.padding", ...);
    // m.impl("conv3d.padding", ...);
    // m.impl("conv_tbc", ...);
    // m.impl("conv_transpose1d", ...);
    // m.impl("conv_transpose3d.input", ...);
}

}  // namespace tt_eager::ext

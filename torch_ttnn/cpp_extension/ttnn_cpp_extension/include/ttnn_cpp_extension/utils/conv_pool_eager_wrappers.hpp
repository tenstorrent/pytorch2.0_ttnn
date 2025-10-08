#pragma once

#include "ttnn_cpp_extension/utils/eager_common.hpp"

#include <ttnn/operations/conv/conv1d/conv1d.hpp>
#include <ttnn/operations/conv/conv2d/conv2d.hpp>
#include <ttnn/operations/conv/conv_transpose2d/conv_transpose2d.hpp>
#include <ttnn/operations/experimental/conv3d/conv3d.hpp>
#include <ttnn/operations/pool/generic/generic_pools.hpp>
#include <ttnn/operations/pool/global_avg_pool/global_avg_pool.hpp>
#include <cstdint>
#include <array>
#include <algorithm>

namespace tt_eager::ext {

// This header is the home for convolution and pooling eager wrappers.
// As part of the split, all conv/pool logic lives here; eager_wrap.hpp will be removed.

// -------- Helpers to parse IntArrayRefs into fixed-size arrays --------
static inline std::array<uint32_t, 1> to_tuple1(c10::OptionalArrayRef<int64_t> v, int64_t def = 1) {
    int64_t x0 = def;
    if (v.has_value() && v->size() >= 1) {
        x0 = (*v)[0];
    }
    return {static_cast<uint32_t>(x0)};
}

static inline std::array<uint32_t, 2> to_tuple2(c10::OptionalArrayRef<int64_t> v, int64_t def = 1) {
    int64_t x0 = def, x1 = def;
    if (v.has_value()) {
        if (v->size() >= 1) {
            x0 = (*v)[0];
        }
        if (v->size() >= 2) {
            x1 = (*v)[1];
        }
        if (v->size() == 1) {
            x1 = x0;  // broadcast single to both
        }
    }
    return {static_cast<uint32_t>(x0), static_cast<uint32_t>(x1)};
}

static inline std::array<uint32_t, 3> to_tuple3(c10::OptionalArrayRef<int64_t> v, int64_t def = 1) {
    int64_t x0 = def, x1 = def, x2 = def;
    if (v.has_value()) {
        if (v->size() >= 1) {
            x0 = (*v)[0];
        }
        if (v->size() >= 2) {
            x1 = (*v)[1];
        }
        if (v->size() >= 3) {
            x2 = (*v)[2];
        }
        if (v->size() == 1) {
            x1 = x0;
            x2 = x0;
        }
    }
    return {static_cast<uint32_t>(x0), static_cast<uint32_t>(x1), static_cast<uint32_t>(x2)};
}

// IntArrayRef overloads (non-optional args per aten schema)
static inline std::array<uint32_t, 1> to_tuple1(c10::IntArrayRef v, int64_t def = 1) {
    int64_t x0 = def;
    if (v.size() >= 1) {
        x0 = v[0];
    }
    return {static_cast<uint32_t>(x0)};
}

static inline std::array<uint32_t, 2> to_tuple2(c10::IntArrayRef v, int64_t def = 1) {
    int64_t x0 = def, x1 = def;
    if (v.size() >= 1) {
        x0 = v[0];
    }
    if (v.size() >= 2) {
        x1 = v[1];
    }
    if (v.size() == 1) {
        x1 = x0;
    }
    return {static_cast<uint32_t>(x0), static_cast<uint32_t>(x1)};
}

static inline std::array<uint32_t, 3> to_tuple3(c10::IntArrayRef v, int64_t def = 1) {
    int64_t x0 = def, x1 = def, x2 = def;
    if (v.size() >= 1) {
        x0 = v[0];
    }
    if (v.size() >= 2) {
        x1 = v[1];
    }
    if (v.size() >= 3) {
        x2 = v[2];
    }
    if (v.size() == 1) {
        x1 = x0;
        x2 = x0;
    }
    return {static_cast<uint32_t>(x0), static_cast<uint32_t>(x1), static_cast<uint32_t>(x2)};
}

// -------- Output size calculators (PyTorch-compatible) --------
static inline uint32_t conv_out_dim(uint32_t in, uint32_t pad, uint32_t dilation, uint32_t kernel, uint32_t stride) {
    int64_t num = static_cast<int64_t>(in) + 2 * static_cast<int64_t>(pad) -
                  static_cast<int64_t>(dilation) * (static_cast<int64_t>(kernel) - 1) - 1;
    int64_t out = num / static_cast<int64_t>(stride) + 1;
    return static_cast<uint32_t>(std::max<int64_t>(out, 0));
}

static inline uint32_t conv_transpose_out_dim(
    uint32_t in, uint32_t pad, uint32_t dilation, uint32_t kernel, uint32_t stride, uint32_t output_padding) {
    int64_t out = (static_cast<int64_t>(in) - 1) * static_cast<int64_t>(stride) - 2 * static_cast<int64_t>(pad) +
                  static_cast<int64_t>(dilation) * (static_cast<int64_t>(kernel) - 1) +
                  static_cast<int64_t>(output_padding) + 1;
    return static_cast<uint32_t>(std::max<int64_t>(out, 0));
}

// -------- Convolution wrappers --------
struct conv2d_aten {
    [[nodiscard]] static at::Tensor invoke(
        const at::Tensor& input,
        const at::Tensor& weight,
        const c10::optional<at::Tensor>& bias,
        c10::IntArrayRef stride,
        c10::IntArrayRef padding,
        c10::IntArrayRef dilation,
        int64_t groups) {
        TORCH_CHECK(input.dim() == 4, "conv2d expects 4D input [N, C, H, W]");
        TORCH_CHECK(weight.dim() == 4, "conv2d expects 4D weight [Cout, Cin/groups, Kh, Kw]");
        TORCH_CHECK(
            !bias.has_value() || bias->device().type() == c10::DeviceType::PrivateUse1, "bias must be on TTNN device");

        ttnn::Tensor in_tt = tt_eager::ext::tileify(input);
        ttnn::Tensor w_tt = tt_eager::ext::tileify(weight);
        std::optional<ttnn::Tensor> bias_local = std::nullopt;
        if (bias.has_value()) {
            bias_local = tt_eager::ext::tileify(*bias);
        }

        const int64_t N = input.size(0);
        const int64_t Cin = input.size(1);
        const int64_t H = input.size(2);
        const int64_t W = input.size(3);
        const int64_t Cout = weight.size(0);
        const int64_t Kh = weight.size(2);
        const int64_t Kw = weight.size(3);

        auto stride2 = to_tuple2(stride, 1);
        auto dilation2 = to_tuple2(dilation, 1);
        auto padding2 = to_tuple2(padding, 0);

        const uint32_t Hout =
            conv_out_dim(static_cast<uint32_t>(H), padding2[0], dilation2[0], static_cast<uint32_t>(Kh), stride2[0]);
        const uint32_t Wout =
            conv_out_dim(static_cast<uint32_t>(W), padding2[1], dilation2[1], static_cast<uint32_t>(Kw), stride2[1]);

        at::Tensor out = tt_eager::ops::create::custom_empty_memory_format(
            {N, Cout, static_cast<int64_t>(Hout), static_cast<int64_t>(Wout)},
            c10::optional<at::ScalarType>(input.scalar_type()),
            c10::nullopt,
            c10::optional<at::Device>(input.device()),
            c10::nullopt);

        std::array<uint32_t, 2> kernel = {static_cast<uint32_t>(Kh), static_cast<uint32_t>(Kw)};
        std::variant<std::array<uint32_t, 2>, std::array<uint32_t, 4>> pad_variant =
            std::array<uint32_t, 2>{padding2[0], padding2[1]};

        auto* device = in_tt.device();
        const uint32_t in_ch = static_cast<uint32_t>(Cin);
        const uint32_t out_ch = static_cast<uint32_t>(Cout);
        const uint32_t batch = static_cast<uint32_t>(N);
        const uint32_t in_h = static_cast<uint32_t>(H);
        const uint32_t in_w = static_cast<uint32_t>(W);
        const uint32_t grp = static_cast<uint32_t>(groups);

        auto res = ttnn::conv2d(
            in_tt,
            w_tt,
            device,
            in_ch,
            out_ch,
            batch,
            in_h,
            in_w,
            kernel,
            stride2,
            pad_variant,
            dilation2,
            grp,
            std::nullopt,
            (bias_local.has_value() ? std::optional<const ttnn::Tensor>(bias_local.value()) : std::nullopt),
            std::nullopt,
            std::nullopt,
            std::nullopt,
            std::nullopt,
            /*return_output_dim=*/false,
            /*return_weights_and_bias=*/false);

        ttnn::Tensor out_tt;
        if (std::holds_alternative<ttnn::Tensor>(res)) {
            out_tt = std::get<ttnn::Tensor>(res);
        } else if (std::holds_alternative<std::tuple<ttnn::Tensor, std::tuple<uint32_t, uint32_t>>>(res)) {
            out_tt = std::get<0>(std::get<std::tuple<ttnn::Tensor, std::tuple<uint32_t, uint32_t>>>(res));
        } else if (std::holds_alternative<
                       std::tuple<ttnn::Tensor, std::tuple<ttnn::Tensor, std::optional<ttnn::Tensor>>>>(res)) {
            out_tt = std::get<0>(
                std::get<std::tuple<ttnn::Tensor, std::tuple<ttnn::Tensor, std::optional<ttnn::Tensor>>>>(res));
        } else {
            out_tt = std::get<0>(std::get<std::tuple<
                                     ttnn::Tensor,
                                     std::tuple<uint32_t, uint32_t>,
                                     std::tuple<ttnn::Tensor, std::optional<ttnn::Tensor>>>>(res));
        }

        return tt_eager::ext::write_from_ttnn(out, out, out_tt);
    }
};

struct conv1d_aten {
    [[nodiscard]] static at::Tensor invoke(
        const at::Tensor& input,
        const at::Tensor& weight,
        const c10::optional<at::Tensor>& bias,
        c10::IntArrayRef stride,
        c10::IntArrayRef padding,
        c10::IntArrayRef dilation,
        int64_t groups) {
        TORCH_CHECK(input.dim() == 3, "conv1d expects 3D input [N, C, L]");
        TORCH_CHECK(weight.dim() == 3, "conv1d expects 3D weight [Cout, Cin/groups, K]");
        TORCH_CHECK(
            !bias.has_value() || bias->device().type() == c10::DeviceType::PrivateUse1, "bias must be on TTNN device");

        ttnn::Tensor in_tt = tt_eager::ext::tileify(input);
        ttnn::Tensor w_tt = tt_eager::ext::tileify(weight);
        std::optional<ttnn::Tensor> bias_local = std::nullopt;
        if (bias.has_value()) {
            bias_local = tt_eager::ext::tileify(*bias);
        }

        const int64_t N = input.size(0);
        const int64_t Cin = input.size(1);
        const int64_t L = input.size(2);
        const int64_t Cout = weight.size(0);
        const int64_t K = weight.size(2);

        auto stride1 = to_tuple1(stride, 1);
        auto dilation1 = to_tuple1(dilation, 1);
        uint32_t pad_val = 0;
        if (padding.size() >= 1) {
            pad_val = static_cast<uint32_t>(padding[0]);
        }

        const uint32_t Lout =
            conv_out_dim(static_cast<uint32_t>(L), pad_val, dilation1[0], static_cast<uint32_t>(K), stride1[0]);

        at::Tensor out = tt_eager::ops::create::custom_empty_memory_format(
            {N, Cout, static_cast<int64_t>(Lout)},
            c10::optional<at::ScalarType>(input.scalar_type()),
            c10::nullopt,
            c10::optional<at::Device>(input.device()),
            c10::nullopt);

        auto* device = in_tt.device();
        auto res = ttnn::conv1d(
            in_tt,
            w_tt,
            device,
            static_cast<uint32_t>(Cin),
            static_cast<uint32_t>(Cout),
            static_cast<uint32_t>(N),
            static_cast<uint32_t>(L),
            static_cast<uint32_t>(K),
            stride1[0],
            std::variant<std::array<uint32_t, 2>, uint32_t>{pad_val},
            dilation1[0],
            static_cast<uint32_t>(groups),
            std::nullopt,
            (bias_local.has_value() ? std::optional<const ttnn::Tensor>(bias_local.value()) : std::nullopt),
            std::nullopt,
            std::nullopt,
            std::nullopt,
            /*return_output_dim=*/true,
            /*return_weights_and_bias=*/false);

        ttnn::Tensor out_tt;
        if (std::holds_alternative<ttnn::Tensor>(res)) {
            out_tt = std::get<ttnn::Tensor>(res);
        } else if (std::holds_alternative<std::tuple<ttnn::Tensor, uint32_t>>(res)) {
            out_tt = std::get<0>(std::get<std::tuple<ttnn::Tensor, uint32_t>>(res));
        } else if (std::holds_alternative<
                       std::tuple<ttnn::Tensor, std::tuple<ttnn::Tensor, std::optional<ttnn::Tensor>>>>(res)) {
            out_tt = std::get<0>(
                std::get<std::tuple<ttnn::Tensor, std::tuple<ttnn::Tensor, std::optional<ttnn::Tensor>>>>(res));
        } else {
            out_tt = std::get<0>(
                std::get<std::tuple<ttnn::Tensor, uint32_t, std::tuple<ttnn::Tensor, std::optional<ttnn::Tensor>>>>(
                    res));
        }

        return tt_eager::ext::write_from_ttnn(out, out, out_tt);
    }
};

struct conv_transpose2d_aten {
    [[nodiscard]] static at::Tensor invoke(
        const at::Tensor& input,
        const at::Tensor& weight,
        const c10::optional<at::Tensor>& bias,
        c10::IntArrayRef stride,
        c10::IntArrayRef padding,
        c10::IntArrayRef output_padding,
        int64_t groups,
        c10::IntArrayRef dilation) {
        TORCH_CHECK(input.dim() == 4, "conv_transpose2d expects 4D input [N, C, H, W]");
        TORCH_CHECK(weight.dim() == 4, "conv_transpose2d expects 4D weight [Cin, Cout/groups, Kh, Kw]");
        TORCH_CHECK(
            !bias.has_value() || bias->device().type() == c10::DeviceType::PrivateUse1, "bias must be on TTNN device");

        ttnn::Tensor in_tt = tt_eager::ext::tileify(input);
        ttnn::Tensor w_tt = tt_eager::ext::tileify(weight);
        std::optional<ttnn::Tensor> bias_local = std::nullopt;
        if (bias.has_value()) {
            bias_local = tt_eager::ext::tileify(*bias);
        }

        const int64_t N = input.size(0);
        const int64_t Cin = input.size(1);
        const int64_t H = input.size(2);
        const int64_t W = input.size(3);
        const int64_t Cout = weight.size(1) * groups;
        const int64_t Kh = weight.size(2);
        const int64_t Kw = weight.size(3);

        auto stride2 = to_tuple2(stride, 1);
        auto dilation2 = to_tuple2(dilation, 1);
        auto padding2 = to_tuple2(padding, 0);
        auto outpad2 = to_tuple2(output_padding, 0);

        const uint32_t Hout = conv_transpose_out_dim(
            static_cast<uint32_t>(H), padding2[0], dilation2[0], static_cast<uint32_t>(Kh), stride2[0], outpad2[0]);
        const uint32_t Wout = conv_transpose_out_dim(
            static_cast<uint32_t>(W), padding2[1], dilation2[1], static_cast<uint32_t>(Kw), stride2[1], outpad2[1]);

        at::Tensor out = tt_eager::ops::create::custom_empty_memory_format(
            {N, Cout, static_cast<int64_t>(Hout), static_cast<int64_t>(Wout)},
            c10::optional<at::ScalarType>(input.scalar_type()),
            c10::nullopt,
            c10::optional<at::Device>(input.device()),
            c10::nullopt);

        auto* device = in_tt.device();

        auto res = ttnn::conv_transpose2d(
            in_tt,
            w_tt,
            device,
            static_cast<uint32_t>(Cin),
            static_cast<uint32_t>(Cout),
            static_cast<uint32_t>(N),
            static_cast<uint32_t>(H),
            static_cast<uint32_t>(W),
            std::array<uint32_t, 2>{static_cast<uint32_t>(Kh), static_cast<uint32_t>(Kw)},
            stride2,
            std::array<uint32_t, 2>{padding2[0], padding2[1]},
            std::array<uint32_t, 2>{outpad2[0], outpad2[1]},
            dilation2,
            static_cast<uint32_t>(groups),
            std::nullopt,
            (bias_local.has_value() ? std::optional<const ttnn::Tensor>(bias_local.value()) : std::nullopt),
            std::nullopt,
            std::nullopt,
            std::nullopt,
            /*mirror_kernel=*/true,
            /*return_output_dim=*/true,
            /*return_weights_and_bias=*/false);

        ttnn::Tensor out_tt;
        if (std::holds_alternative<ttnn::Tensor>(res)) {
            out_tt = std::get<ttnn::Tensor>(res);
        } else if (std::holds_alternative<std::tuple<ttnn::Tensor, std::tuple<uint32_t, uint32_t>>>(res)) {
            out_tt = std::get<0>(std::get<std::tuple<ttnn::Tensor, std::tuple<uint32_t, uint32_t>>>(res));
        } else if (std::holds_alternative<
                       std::tuple<ttnn::Tensor, std::tuple<ttnn::Tensor, std::optional<ttnn::Tensor>>>>(res)) {
            out_tt = std::get<0>(
                std::get<std::tuple<ttnn::Tensor, std::tuple<ttnn::Tensor, std::optional<ttnn::Tensor>>>>(res));
        } else {
            out_tt = std::get<0>(std::get<std::tuple<
                                     ttnn::Tensor,
                                     std::tuple<uint32_t, uint32_t>,
                                     std::tuple<ttnn::Tensor, std::optional<ttnn::Tensor>>>>(res));
        }

        return tt_eager::ext::write_from_ttnn(out, out, out_tt);
    }
};

struct conv3d_aten {
    [[nodiscard]] static at::Tensor invoke(
        const at::Tensor& input,
        const at::Tensor& weight,
        const c10::optional<at::Tensor>& bias,
        c10::IntArrayRef stride,
        c10::IntArrayRef padding,
        c10::IntArrayRef dilation,
        int64_t groups) {
        TORCH_CHECK(input.dim() == 5, "conv3d expects 5D input [N, C, T, H, W]");
        TORCH_CHECK(weight.dim() == 5, "conv3d expects 5D weight [Cout, Cin/groups, Kt, Kh, Kw]");
        TORCH_CHECK(
            !bias.has_value() || bias->device().type() == c10::DeviceType::PrivateUse1, "bias must be on TTNN device");

        ttnn::Tensor in_tt = tt_eager::ext::tileify(input);
        ttnn::Tensor w_tt = tt_eager::ext::tileify(weight);
        std::optional<ttnn::Tensor> b_tt = std::nullopt;
        if (bias.has_value()) {
            b_tt = tt_eager::ext::tileify(*bias);
        }

        const int64_t N = input.size(0);
        const int64_t Cin = input.size(1);
        const int64_t T = input.size(2);
        const int64_t H = input.size(3);
        const int64_t W = input.size(4);
        const int64_t Cout = weight.size(0);
        const int64_t Kt = weight.size(2);
        const int64_t Kh = weight.size(3);
        const int64_t Kw = weight.size(4);

        auto stride3 = to_tuple3(stride, 1);
        auto dilation3 = to_tuple3(dilation, 1);
        auto padding3 = to_tuple3(padding, 0);

        const uint32_t Tout =
            conv_out_dim(static_cast<uint32_t>(T), padding3[0], dilation3[0], static_cast<uint32_t>(Kt), stride3[0]);
        const uint32_t Hout =
            conv_out_dim(static_cast<uint32_t>(H), padding3[1], dilation3[1], static_cast<uint32_t>(Kh), stride3[1]);
        const uint32_t Wout =
            conv_out_dim(static_cast<uint32_t>(W), padding3[2], dilation3[2], static_cast<uint32_t>(Kw), stride3[2]);

        at::Tensor out = tt_eager::ops::create::custom_empty_memory_format(
            {N, Cout, static_cast<int64_t>(Tout), static_cast<int64_t>(Hout), static_cast<int64_t>(Wout)},
            c10::optional<at::ScalarType>(input.scalar_type()),
            c10::nullopt,
            c10::optional<at::Device>(input.device()),
            c10::nullopt);

        using ttnn::operations::experimental::conv3d::Conv3dConfig;
        Conv3dConfig cfg{
            tt::tt_metal::DataType::BFLOAT16,
            tt::tt_metal::DataType::BFLOAT16,
            tt::tt_metal::Layout::ROW_MAJOR,
            1,
            1,
            1,
            0,
            0,
            static_cast<uint32_t>(Cout),
            {static_cast<uint32_t>(Kt), static_cast<uint32_t>(Kh), static_cast<uint32_t>(Kw)},
            {stride3[0], stride3[1], stride3[2]},
            {padding3[0], padding3[1], padding3[2]},
            "zeros",
            static_cast<uint32_t>(groups),
            {1, 1}};

        ttnn::Tensor out_tt = ttnn::experimental::conv3d(in_tt, w_tt, b_tt, cfg, std::nullopt, std::nullopt);

        return tt_eager::ext::write_from_ttnn(out, out, out_tt);
    }
};

// -------- Pooling helpers --------
static inline uint32_t pool_out_dim(
    uint32_t in, uint32_t pad, uint32_t dilation, uint32_t kernel, uint32_t stride, bool ceil_mode) {
    int64_t effective = static_cast<int64_t>(in) + 2 * static_cast<int64_t>(pad) -
                        static_cast<int64_t>(dilation) * (static_cast<int64_t>(kernel) - 1) - 1;
    double val = static_cast<double>(effective) / static_cast<double>(stride) + 1.0;
    int64_t out = ceil_mode ? static_cast<int64_t>(std::ceil(val)) : static_cast<int64_t>(std::floor(val));
    return static_cast<uint32_t>(std::max<int64_t>(out, 0));
}

struct max_pool2d_aten {
    [[nodiscard]] static at::Tensor invoke(
        const at::Tensor& input,
        c10::IntArrayRef kernel_size,
        c10::IntArrayRef stride,
        c10::IntArrayRef padding,
        c10::IntArrayRef dilation,
        bool ceil_mode) {
        TORCH_CHECK(input.dim() == 4, "max_pool2d expects 4D input [N, C, H, W]");
        TORCH_CHECK(kernel_size.size() == 2, "max_pool2d: kernel_size must have 2 elements");

        ttnn::Tensor in_tt = tt_eager::ext::tileify(input);
        const int64_t N = input.size(0);
        const int64_t C = input.size(1);
        const int64_t H = input.size(2);
        const int64_t W = input.size(3);

        std::array<uint32_t, 2> k = {static_cast<uint32_t>(kernel_size[0]), static_cast<uint32_t>(kernel_size[1])};
        std::array<uint32_t, 2> s;
        if (stride.size() > 0) {
            auto s2 = to_tuple2(stride, 1);
            s = {s2[0], s2[1]};
        } else {
            s = k;
        }
        auto d = to_tuple2(dilation, 1);
        auto p = to_tuple2(padding, 0);

        const uint32_t Hout = pool_out_dim(static_cast<uint32_t>(H), p[0], d[0], k[0], s[0], ceil_mode);
        const uint32_t Wout = pool_out_dim(static_cast<uint32_t>(W), p[1], d[1], k[1], s[1], ceil_mode);

        at::Tensor out = tt_eager::ops::create::custom_empty_memory_format(
            {N, C, static_cast<int64_t>(Hout), static_cast<int64_t>(Wout)},
            c10::optional<at::ScalarType>(input.scalar_type()),
            c10::nullopt,
            c10::optional<at::Device>(input.device()),
            c10::nullopt);

        auto res = ttnn::max_pool2d(
            in_tt,
            static_cast<uint32_t>(N),
            static_cast<uint32_t>(H),
            static_cast<uint32_t>(W),
            static_cast<uint32_t>(C),
            k,
            s,
            std::variant<std::array<uint32_t, 2>, std::array<uint32_t, 4>>{std::array<uint32_t, 2>{p[0], p[1]}},
            d,
            /*ceil_mode*/ ceil_mode,
            /*memory_config*/ std::nullopt,
            /*applied_shard_scheme*/ std::nullopt,
            /*in_place_halo*/ false,
            /*deallocate_input*/ false,
            /*reallocate_halo_output*/ true,
            /*return_indices*/ false,
            /*dtype*/ ttnn::DataType::BFLOAT16,
            /*output_layout*/ ttnn::ROW_MAJOR_LAYOUT);

        ttnn::Tensor out_tt = std::holds_alternative<ttnn::Tensor>(res)
                                  ? std::get<ttnn::Tensor>(res)
                                  : std::get<ttnn::operations::pool::MaxPoolWithIndicesResult>(res).output;
        return tt_eager::ext::write_from_ttnn(out, out, out_tt);
    }
};

struct avg_pool2d_aten {
    [[nodiscard]] static at::Tensor invoke(
        const at::Tensor& input,
        c10::IntArrayRef kernel_size,
        c10::IntArrayRef stride,
        c10::IntArrayRef padding,
        bool ceil_mode,
        bool count_include_pad,
        c10::optional<int64_t> divisor_override) {
        TORCH_CHECK(input.dim() == 4, "avg_pool2d expects 4D input [N, C, H, W]");
        TORCH_CHECK(kernel_size.size() == 2, "avg_pool2d: kernel_size must have 2 elements");

        ttnn::Tensor in_tt = tt_eager::ext::tileify(input);
        const int64_t N = input.size(0);
        const int64_t C = input.size(1);
        const int64_t H = input.size(2);
        const int64_t W = input.size(3);

        std::array<uint32_t, 2> k = {static_cast<uint32_t>(kernel_size[0]), static_cast<uint32_t>(kernel_size[1])};
        std::array<uint32_t, 2> s;
        if (stride.size() > 0) {
            auto s2 = to_tuple2(stride, 1);
            s = {s2[0], s2[1]};
        } else {
            s = k;
        }
        auto p = to_tuple2(padding, 0);

        const uint32_t Hout = pool_out_dim(static_cast<uint32_t>(H), p[0], /*dilation*/ 1, k[0], s[0], ceil_mode);
        const uint32_t Wout = pool_out_dim(static_cast<uint32_t>(W), p[1], /*dilation*/ 1, k[1], s[1], ceil_mode);

        at::Tensor out = tt_eager::ops::create::custom_empty_memory_format(
            {N, C, static_cast<int64_t>(Hout), static_cast<int64_t>(Wout)},
            c10::optional<at::ScalarType>(input.scalar_type()),
            c10::nullopt,
            c10::optional<at::Device>(input.device()),
            c10::nullopt);

        std::optional<int32_t> div_opt = std::nullopt;
        if (divisor_override.has_value()) {
            div_opt = static_cast<int32_t>(divisor_override.value());
        }

        ttnn::Tensor out_tt = ttnn::avg_pool2d(
            in_tt,
            static_cast<uint32_t>(N),
            static_cast<uint32_t>(H),
            static_cast<uint32_t>(W),
            static_cast<uint32_t>(C),
            k,
            s,
            std::variant<std::array<uint32_t, 2>, std::array<uint32_t, 4>>{std::array<uint32_t, 2>{p[0], p[1]}},
            /*ceil_mode*/ ceil_mode,
            /*count_include_pad*/ count_include_pad,
            /*divisor_override*/ div_opt,
            /*memory_config*/ std::nullopt,
            /*applied_shard_scheme*/ std::nullopt,
            /*in_place_halo*/ false,
            /*deallocate_input*/ false,
            /*reallocate_halo_output*/ true,
            /*dtype*/ ttnn::DataType::BFLOAT16,
            /*output_layout*/ ttnn::ROW_MAJOR_LAYOUT);

        return tt_eager::ext::write_from_ttnn(out, out, out_tt);
    }
};

struct adaptive_avg_pool2d_aten {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& input, c10::IntArrayRef output_size) {
        TORCH_CHECK(input.dim() == 4, "adaptive_avg_pool2d expects 4D input [N, C, H, W]");
        TORCH_CHECK(output_size.size() == 2, "adaptive_avg_pool2d: output_size must be 2 elements");
        TORCH_CHECK(
            output_size[0] == 1 && output_size[1] == 1,
            "adaptive_avg_pool2d currently supports only output_size=[1,1] on TTNN");

        ttnn::Tensor in_tt = tt_eager::ext::tileify(input);
        ttnn::Tensor out_tt = ttnn::global_avg_pool2d(in_tt);
        at::Tensor out = tt_eager::ops::create::custom_empty_memory_format(
            {input.size(0), input.size(1), 1, 1},
            c10::optional<at::ScalarType>(input.scalar_type()),
            c10::nullopt,
            c10::optional<at::Device>(input.device()),
            c10::nullopt);
        return tt_eager::ext::write_from_ttnn(out, out, out_tt);
    }
};

}  // namespace tt_eager::ext

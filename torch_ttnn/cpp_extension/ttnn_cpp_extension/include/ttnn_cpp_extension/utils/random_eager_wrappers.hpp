#pragma once

#include "ttnn_cpp_extension/utils/eager_common.hpp"

#include <random>
#include <limits>

#include <ttnn/operations/rand/rand.hpp>
#include <ttnn/operations/bernoulli/bernoulli.hpp>
#include <ttnn/operations/uniform/uniform.hpp>
#include <ttnn/operations/eltwise/unary/unary.hpp>

namespace tt_eager::ext {

// Concepts for random
template <auto Op>
concept TTNNRandomFn = requires(const ttnn::Tensor& a, uint32_t seed) {
    { Op(a, seed, std::nullopt, std::nullopt, std::nullopt, std::nullopt) } -> std::same_as<ttnn::Tensor>;
};

template <auto Op>
concept TTNNUniformSeededFn = requires(const ttnn::Tensor& a, float from, float to, uint32_t seed) {
    { Op(a, from, to, seed, std::nullopt, std::nullopt) } -> std::same_as<ttnn::Tensor>;
};

// Seeded random wrapper (e.g., bernoulli)
template <auto Op>
    requires TTNNRandomFn<Op>
struct unary_random_seeded {
    [[nodiscard]] static at::Tensor invoke(
        const at::Tensor& input, c10::optional<at::Generator> generator = c10::nullopt) {
        at::Tensor out = tt_eager::ext::make_empty_like_tt(input);
        return invoke_into(input, generator, out);
    }
    [[nodiscard]] static at::Tensor& invoke_inplace(
        at::Tensor& self, c10::optional<at::Generator> generator = c10::nullopt) {
        return invoke_into(self, generator, self);
    }
    [[nodiscard]] static at::Tensor& invoke_into(
        const at::Tensor& input, c10::optional<at::Generator> generator, at::Tensor& out) {
        ttnn::Tensor in_tile = tt_eager::ext::tileify(input);
        static thread_local std::mt19937 rng(std::random_device{}());
        uint32_t seed = generator.has_value() ? static_cast<uint32_t>(generator.value().current_seed()) : rng();
        ttnn::Tensor result = Op(in_tile, seed, std::nullopt, std::nullopt, std::nullopt, std::nullopt);
        return tt_eager::ext::write_from_ttnn(out, input, result);
    }
};

// Uniform random [from, to)
template <auto Op>
    requires TTNNUniformSeededFn<Op>
struct unary_random_uniform {
    [[nodiscard]] static at::Tensor& invoke_inplace(
        at::Tensor& self, double from, double to, c10::optional<at::Generator> generator = c10::nullopt) {
        return invoke_into(self, from, to, generator, self);
    }
    [[nodiscard]] static at::Tensor& invoke_into(
        const at::Tensor& input, double from, double to, c10::optional<at::Generator> generator, at::Tensor& out) {
        ttnn::Tensor in_tile = tt_eager::ext::tileify(input);
        static thread_local std::mt19937 rng(std::random_device{}());
        uint32_t seed = generator.has_value() ? static_cast<uint32_t>(generator.value().current_seed()) : rng();
        const float low = static_cast<float>(from);
        const float high = static_cast<float>(to);
        ttnn::Tensor result = Op(in_tile, low, high, seed, std::nullopt, std::nullopt);
        return tt_eager::ext::write_from_ttnn(out, input, result);
    }
};

// Random_ family via rand + typecast
struct random_like_rand {
    static inline uint32_t seed_of(c10::optional<at::Generator> gen) {
        static thread_local std::mt19937 rng(std::random_device{}());
        return gen.has_value() ? static_cast<uint32_t>(gen.value().current_seed()) : rng();
    }
    static inline double mantissa_bound(at::ScalarType st) {
        return (st == at::kFloat) ? std::ldexp(1.0, 24) : std::ldexp(1.0, 7);
    }
    static inline std::pair<double, double> int_bounds_default(at::ScalarType st) {
        if (st == at::kByte) {
            return {0.0, 256.0};
        }
        return {
            static_cast<double>(std::numeric_limits<int32_t>::min()),
            static_cast<double>(static_cast<int64_t>(std::numeric_limits<int32_t>::max()) + 1)};
    }
    static inline ttnn::Tensor sample_f32_like(const ttnn::Tensor& like, double low, double high, uint32_t seed) {
        auto shape = like.logical_shape();
        auto* device = like.device();
        auto layout = like.layout();
        return ttnn::rand(
            shape,
            *device,
            ttnn::DataType::FLOAT32,
            layout,
            ttnn::DRAM_MEMORY_CONFIG,
            static_cast<float>(low),
            static_cast<float>(high),
            seed);
    }
    static inline ttnn::Tensor cast_after_sampling(const ttnn::Tensor& src, at::ScalarType st, bool is_int) {
        if (is_int) {
            auto floored = ttnn::floor(src);
            ttnn::DataType dt = (st == at::kByte) ? ttnn::DataType::UINT8 : ttnn::DataType::INT32;
            return ttnn::typecast(floored, dt);
        }
        if (st == at::kFloat) {
            return (src.dtype() == ttnn::DataType::FLOAT32) ? src : ttnn::typecast(src, ttnn::DataType::FLOAT32);
        }
        return (src.dtype() == ttnn::DataType::BFLOAT16) ? src : ttnn::typecast(src, ttnn::DataType::BFLOAT16);
    }
    static at::Tensor& fill(at::Tensor& self, double low, double high, bool is_int, c10::optional<at::Generator> gen) {
        ttnn::Tensor like = tt_eager::ext::tileify(self);
        uint32_t seed = seed_of(gen);
        ttnn::Tensor rnd = sample_f32_like(like, low, high, seed);
        ttnn::Tensor out_tt = cast_after_sampling(rnd, self.scalar_type(), is_int);
        return tt_eager::ext::write_from_ttnn(self, self, out_tt);
    }
    [[nodiscard]] static at::Tensor& invoke_inplace(at::Tensor& self, c10::optional<at::Generator> gen = c10::nullopt) {
        const auto st = self.scalar_type();
        if (st == at::kFloat) {
            return fill(self, 0.0, mantissa_bound(st), false, gen);
        }
        if (st == at::kBFloat16) {
            return fill(self, 0.0, mantissa_bound(st), false, gen);
        }
        if (st == at::kByte) {
            auto [l, h] = int_bounds_default(st);
            return fill(self, l, h, true, gen);
        }
        if (st == at::kInt) {
            auto [l, h] = int_bounds_default(st);
            return fill(self, l, h, true, gen);
        }
        TORCH_CHECK(false, "Unsupported dtype for random_ on TTNN");
    }
    [[nodiscard]] static at::Tensor& invoke_from_inplace(
        at::Tensor& self, int64_t from, c10::optional<int64_t> to, c10::optional<at::Generator> gen = c10::nullopt) {
        const auto st = self.scalar_type();
        TORCH_CHECK(st == at::kByte || st == at::kInt, "random_.from is supported only for uint8/int32 on TTNN");
        double low = static_cast<double>(from);
        double high = to.has_value() ? static_cast<double>(to.value()) : int_bounds_default(st).second;
        return fill(self, low, high, true, gen);
    }
    [[nodiscard]] static at::Tensor& invoke_to_inplace(
        at::Tensor& self, int64_t to, c10::optional<at::Generator> gen = c10::nullopt) {
        const auto st = self.scalar_type();
        TORCH_CHECK(st == at::kByte || st == at::kInt, "random_.to is supported only for uint8/int32 on TTNN");
        return fill(self, 0.0, static_cast<double>(to), true, gen);
    }
};

}  // namespace tt_eager::ext

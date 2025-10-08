#pragma once

#include "ttnn_cpp_extension/utils/eager_common.hpp"

#include <ttnn/operations/reduction/generic/generic_reductions.hpp>
#include <ttnn/operations/experimental/reduction/argmax/argmax.hpp>

namespace tt_eager::ext {

inline std::optional<std::variant<int, ttnn::SmallVector<int>>> to_ttnn_dim_variant(
    c10::OptionalArrayRef<int64_t> dims) {
    if (!dims.has_value()) {
        return std::nullopt;
    }
    return to_ttnn_dim_variant(*dims);
}

template <auto Op>
struct reduction_all {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& a, c10::optional<at::ScalarType> dtype = c10::nullopt) {
        at::Tensor out = make_empty_like_tt(a, dtype);
        return invoke_into(a, dtype, out);
    }
    [[nodiscard]] static at::Tensor& invoke_into(
        const at::Tensor& in, c10::optional<at::ScalarType> dtype, at::Tensor& out) {
        ttnn::Tensor a_tile = tileify(in);
        ttnn::Tensor result = Op(a_tile, std::nullopt, /*keepdim*/ false);
        if (dtype.has_value()) {
            result = ttnn::typecast(result, to_ttnn_dtype(*dtype));
        }
        return write_from_ttnn(out, in, result);
    }
};

template <auto Op>
struct reduction_all_nodtype {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& a) {
        at::Tensor out = make_empty_like_tt(a);
        return invoke_into(a, out);
    }
    [[nodiscard]] static at::Tensor& invoke_into(const at::Tensor& in, at::Tensor& out) {
        ttnn::Tensor a_tile = tileify(in);
        ttnn::Tensor result = Op(a_tile, std::nullopt, /*keepdim*/ false);
        return write_from_ttnn(out, in, result);
    }
};

template <auto Op>
struct reduction_dimlist {
    [[nodiscard]] static at::Tensor invoke(
        const at::Tensor& a,
        c10::OptionalArrayRef<int64_t> dim,
        bool keepdim,
        c10::optional<at::ScalarType> dtype = c10::nullopt) {
        at::Tensor out = make_empty_like_tt(a, dtype);
        return invoke_into(a, dim, keepdim, dtype, out);
    }
    [[nodiscard]] static at::Tensor& invoke_into(
        const at::Tensor& in,
        c10::OptionalArrayRef<int64_t> dim,
        bool keepdim,
        c10::optional<at::ScalarType> dtype,
        at::Tensor& out) {
        ttnn::Tensor a_tile = tileify(in);
        std::optional<std::variant<int, ttnn::SmallVector<int>>> dim_variant = to_ttnn_dim_variant(dim);
        ttnn::Tensor result = Op(a_tile, dim_variant, keepdim);
        if (dtype.has_value()) {
            result = ttnn::typecast(result, to_ttnn_dtype(*dtype));
        }
        return write_from_ttnn(out, in, result);
    }
    [[nodiscard]] static at::Tensor invoke_dimnames(
        const at::Tensor& a,
        at::DimnameList dimnames,
        bool keepdim,
        c10::optional<at::ScalarType> dtype = c10::nullopt) {
        auto names = a.names();
        std::vector<int64_t> positions;
        positions.reserve(dimnames.size());
        for (const auto& dn : dimnames) {
            bool found = false;
            for (int64_t i = 0; i < static_cast<int64_t>(names.size()); ++i) {
                if (names[i] == dn) {
                    positions.push_back(i);
                    found = true;
                    break;
                }
            }
            TORCH_CHECK(found, "Dimname not found in tensor");
        }
        return invoke(a, c10::OptionalArrayRef<int64_t>(positions), keepdim, dtype);
    }
    [[nodiscard]] static at::Tensor& invoke_dimnames_into(
        const at::Tensor& a,
        at::DimnameList dimnames,
        bool keepdim,
        c10::optional<at::ScalarType> dtype,
        at::Tensor& out) {
        auto names = a.names();
        std::vector<int64_t> positions;
        positions.reserve(dimnames.size());
        for (const auto& dn : dimnames) {
            bool found = false;
            for (int64_t i = 0; i < static_cast<int64_t>(names.size()); ++i) {
                if (names[i] == dn) {
                    positions.push_back(i);
                    found = true;
                    break;
                }
            }
            TORCH_CHECK(found, "Dimname not found in tensor");
        }
        return invoke_into(a, c10::OptionalArrayRef<int64_t>(positions), keepdim, dtype, out);
    }
};

// Unbiased (std/var) all-elements
template <auto Op>
struct reduction_all_unbiased {
    [[nodiscard]] static at::Tensor invoke(const at::Tensor& a, bool unbiased = false) {
        at::Tensor out = make_empty_like_tt(a);
        return invoke_into(a, unbiased, out);
    }
    [[nodiscard]] static at::Tensor& invoke_into(const at::Tensor& in, bool unbiased, at::Tensor& out) {
        ttnn::Tensor a_tile = tileify(in);
        ttnn::Tensor result = Op(a_tile, std::nullopt, /*keepdim*/ false, std::nullopt, std::nullopt, 1.0f, unbiased);
        return write_from_ttnn(out, in, result);
    }
};

// Unbiased dimlist (with out)
template <auto Op>
struct reduction_dimlist_unbiased_out {
    [[nodiscard]] static at::Tensor& invoke_into(
        const at::Tensor& in, c10::OptionalArrayRef<int64_t> dim, bool unbiased, bool keepdim, at::Tensor& out) {
        ttnn::Tensor a_tile = tileify(in);
        std::optional<std::variant<int, ttnn::SmallVector<int>>> dim_variant = to_ttnn_dim_variant(dim);
        ttnn::Tensor result = Op(a_tile, dim_variant, keepdim, std::nullopt, std::nullopt, 1.0f, unbiased);
        return write_from_ttnn(out, in, result);
    }
};

// Correction (0/1 -> unbiased flag)
template <auto Op>
struct reduction_dimlist_correction {
    static inline bool to_unbiased(const c10::optional<c10::Scalar>& correction_opt) {
        if (!correction_opt.has_value()) {
            return true;
        }
        return correction_opt.value().toLong() != 0;
    }
    [[nodiscard]] static at::Tensor invoke(
        const at::Tensor& a,
        c10::OptionalArrayRef<int64_t> dim,
        const c10::optional<c10::Scalar>& correction,
        bool keepdim) {
        at::Tensor out = make_empty_like_tt(a);
        return invoke_into(a, dim, correction, keepdim, out);
    }
    [[nodiscard]] static at::Tensor& invoke_into(
        const at::Tensor& in,
        c10::OptionalArrayRef<int64_t> dim,
        const c10::optional<c10::Scalar>& correction,
        bool keepdim,
        at::Tensor& out) {
        const bool unbiased = to_unbiased(correction);
        ttnn::Tensor a_tile = tileify(in);
        std::optional<std::variant<int, ttnn::SmallVector<int>>> dim_variant = to_ttnn_dim_variant(dim);
        ttnn::Tensor result = Op(a_tile, dim_variant, keepdim, std::nullopt, std::nullopt, 1.0f, unbiased);
        return write_from_ttnn(out, in, result);
    }
    [[nodiscard]] static at::Tensor invoke_dimnames(
        const at::Tensor& a, at::DimnameList dimnames, const c10::optional<c10::Scalar>& correction, bool keepdim) {
        // Map names → positions
        auto names = a.names();
        std::vector<int64_t> positions;
        positions.reserve(dimnames.size());
        for (const auto& dn : dimnames) {
            bool found = false;
            for (int64_t i = 0; i < static_cast<int64_t>(names.size()); ++i) {
                if (names[i] == dn) {
                    positions.push_back(i);
                    found = true;
                    break;
                }
            }
            TORCH_CHECK(found, "Dimname not found in tensor");
        }
        return invoke(a, c10::OptionalArrayRef<int64_t>(positions), correction, keepdim);
    }
    [[nodiscard]] static at::Tensor& invoke_dimnames_into(
        const at::Tensor& a,
        at::DimnameList dimnames,
        const c10::optional<c10::Scalar>& correction,
        bool keepdim,
        at::Tensor& out) {
        auto names = a.names();
        std::vector<int64_t> positions;
        positions.reserve(dimnames.size());
        for (const auto& dn : dimnames) {
            bool found = false;
            for (int64_t i = 0; i < static_cast<int64_t>(names.size()); ++i) {
                if (names[i] == dn) {
                    positions.push_back(i);
                    found = true;
                    break;
                }
            }
            TORCH_CHECK(found, "Dimname not found in tensor");
        }
        return invoke_into(a, c10::OptionalArrayRef<int64_t>(positions), correction, keepdim, out);
    }
};

// Add dimnames variants for reduction_dimlist and reduction_dim_pair
template <auto Op>
struct reduction_dimlist_with_names : reduction_dimlist<Op> {
    using Base = reduction_dimlist<Op>;
    [[nodiscard]] static at::Tensor invoke_dimnames(
        const at::Tensor& a,
        at::DimnameList dimnames,
        bool keepdim,
        c10::optional<at::ScalarType> dtype = c10::nullopt) {
        auto names = a.names();
        std::vector<int64_t> positions;
        positions.reserve(dimnames.size());
        for (const auto& dn : dimnames) {
            bool found = false;
            for (int64_t i = 0; i < static_cast<int64_t>(names.size()); ++i) {
                if (names[i] == dn) {
                    positions.push_back(i);
                    found = true;
                    break;
                }
            }
            TORCH_CHECK(found, "Dimname not found in tensor");
        }
        return Base::invoke(a, c10::OptionalArrayRef<int64_t>(positions), keepdim, dtype);
    }
    [[nodiscard]] static at::Tensor& invoke_dimnames_into(
        const at::Tensor& a,
        at::DimnameList dimnames,
        bool keepdim,
        c10::optional<at::ScalarType> dtype,
        at::Tensor& out) {
        auto names = a.names();
        std::vector<int64_t> positions;
        positions.reserve(dimnames.size());
        for (const auto& dn : dimnames) {
            bool found = false;
            for (int64_t i = 0; i < static_cast<int64_t>(names.size()); ++i) {
                if (names[i] == dn) {
                    positions.push_back(i);
                    found = true;
                    break;
                }
            }
            TORCH_CHECK(found, "Dimname not found in tensor");
        }
        return Base::invoke_into(a, c10::OptionalArrayRef<int64_t>(positions), keepdim, dtype, out);
    }
};

template <auto ReduceOp, auto ArgOp>
struct reduction_dim_pair {
    [[nodiscard]] static std::tuple<at::Tensor, at::Tensor> invoke(const at::Tensor& a, int64_t dim, bool keepdim) {
        ttnn::Tensor a_tile = tileify(a);
        auto dim_variant = std::optional<std::variant<int, ttnn::SmallVector<int>>>(static_cast<int>(dim));
        ttnn::Tensor v_tt = ReduceOp(a_tile, dim_variant, keepdim);
        ttnn::Tensor i_tt = ArgOp(a_tile, static_cast<int64_t>(dim), /*all=*/false);
        at::Tensor v_out = make_empty_like_tt(a);
        at::Tensor i_out = make_empty_like_tt(a, at::kInt);
        write_from_ttnn(v_out, a, v_tt);
        write_from_ttnn(i_out, a, i_tt);
        return {v_out, i_out};
    }
    [[nodiscard]] static std::tuple<at::Tensor&, at::Tensor&> invoke_into(
        const at::Tensor& a, int64_t dim, bool keepdim, at::Tensor& values_out, at::Tensor& indices_out) {
        ttnn::Tensor a_tile = tileify(a);
        auto dim_variant = std::optional<std::variant<int, ttnn::SmallVector<int>>>(static_cast<int>(dim));
        ttnn::Tensor v_tt = ReduceOp(a_tile, dim_variant, keepdim);
        ttnn::Tensor i_tt = ArgOp(a_tile, static_cast<int64_t>(dim), /*all=*/false);
        write_from_ttnn(values_out, a, v_tt);
        write_from_ttnn(indices_out, a, i_tt);
        return {values_out, indices_out};
    }
    [[nodiscard]] static std::tuple<at::Tensor, at::Tensor> invoke_dimnames(
        const at::Tensor& a, at::DimnameList dimnames, bool keepdim) {
        auto names = a.names();
        TORCH_CHECK(dimnames.size() == 1, "names_dim expects a single dimension name");
        int64_t pos = -1;
        for (int64_t i = 0; i < static_cast<int64_t>(names.size()); ++i) {
            if (names[i] == dimnames[0]) {
                pos = i;
                break;
            }
        }
        TORCH_CHECK(pos >= 0, "Dimname not found in tensor");
        return invoke(a, pos, keepdim);
    }
    [[nodiscard]] static std::tuple<at::Tensor, at::Tensor> invoke_dimname(
        const at::Tensor& a, at::Dimname dimname, bool keepdim) {
        auto names = a.names();
        int64_t pos = -1;
        for (int64_t i = 0; i < static_cast<int64_t>(names.size()); ++i) {
            if (names[i] == dimname) {
                pos = i;
                break;
            }
        }
        TORCH_CHECK(pos >= 0, "Dimname not found in tensor");
        return invoke(a, pos, keepdim);
    }
    [[nodiscard]] static std::tuple<at::Tensor&, at::Tensor&> invoke_dimnames_into(
        const at::Tensor& a, at::DimnameList dimnames, bool keepdim, at::Tensor& values_out, at::Tensor& indices_out) {
        auto names = a.names();
        TORCH_CHECK(dimnames.size() == 1, "names_dim expects a single dimension name");
        int64_t pos = -1;
        for (int64_t i = 0; i < static_cast<int64_t>(names.size()); ++i) {
            if (names[i] == dimnames[0]) {
                pos = i;
                break;
            }
        }
        TORCH_CHECK(pos >= 0, "Dimname not found in tensor");
        return invoke_into(a, pos, keepdim, values_out, indices_out);
    }
    [[nodiscard]] static std::tuple<at::Tensor&, at::Tensor&> invoke_dimname_into(
        const at::Tensor& a, at::Dimname dimname, bool keepdim, at::Tensor& values_out, at::Tensor& indices_out) {
        auto names = a.names();
        int64_t pos = -1;
        for (int64_t i = 0; i < static_cast<int64_t>(names.size()); ++i) {
            if (names[i] == dimname) {
                pos = i;
                break;
            }
        }
        TORCH_CHECK(pos >= 0, "Dimname not found in tensor");
        return invoke_into(a, pos, keepdim, values_out, indices_out);
    }
};

// Unbiased over dim list (no out)
template <auto Op>
struct reduction_dimlist_unbiased {
    [[nodiscard]] static at::Tensor invoke(
        const at::Tensor& a, c10::OptionalArrayRef<int64_t> dim, bool unbiased, bool keepdim) {
        at::Tensor out = make_empty_like_tt(a);
        return invoke_into(a, dim, unbiased, keepdim, out);
    }
    [[nodiscard]] static at::Tensor& invoke_into(
        const at::Tensor& in, c10::OptionalArrayRef<int64_t> dim, bool unbiased, bool keepdim, at::Tensor& out) {
        ttnn::Tensor a_tile = tileify(in);
        std::optional<std::variant<int, ttnn::SmallVector<int>>> dim_variant = to_ttnn_dim_variant(dim);
        ttnn::Tensor result = Op(a_tile, dim_variant, keepdim, std::nullopt, std::nullopt, 1.0f, unbiased);
        return write_from_ttnn(out, in, result);
    }
    [[nodiscard]] static at::Tensor invoke_dimnames(
        const at::Tensor& a, at::DimnameList dimnames, bool unbiased, bool keepdim) {
        auto names = a.names();
        std::vector<int64_t> positions;
        positions.reserve(dimnames.size());
        for (const auto& dn : dimnames) {
            bool found = false;
            for (int64_t i = 0; i < static_cast<int64_t>(names.size()); ++i) {
                if (names[i] == dn) {
                    positions.push_back(i);
                    found = true;
                    break;
                }
            }
            TORCH_CHECK(found, "Dimname not found in tensor");
        }
        return invoke(a, c10::OptionalArrayRef<int64_t>(positions), unbiased, keepdim);
    }
    [[nodiscard]] static at::Tensor& invoke_dimnames_into(
        const at::Tensor& a, at::DimnameList dimnames, bool unbiased, bool keepdim, at::Tensor& out) {
        auto names = a.names();
        std::vector<int64_t> positions;
        positions.reserve(dimnames.size());
        for (const auto& dn : dimnames) {
            bool found = false;
            for (int64_t i = 0; i < static_cast<int64_t>(names.size()); ++i) {
                if (names[i] == dn) {
                    positions.push_back(i);
                    found = true;
                    break;
                }
            }
            TORCH_CHECK(found, "Dimname not found in tensor");
        }
        return invoke_into(a, c10::OptionalArrayRef<int64_t>(positions), unbiased, keepdim, out);
    }
};

}  // namespace tt_eager::ext

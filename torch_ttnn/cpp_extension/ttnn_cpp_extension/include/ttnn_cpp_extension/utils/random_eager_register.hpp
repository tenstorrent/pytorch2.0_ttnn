#pragma once

#include "ttnn_cpp_extension/utils/random_eager_wrappers.hpp"
#include <torch/library.h>

namespace tt_eager::ext {

static inline void register_random_ops(torch::Library& m) {
    // =========================
    // Random
    // =========================
    // schema: bernoulli(Tensor self, *, Generator? generator=None) -> Tensor
    m.impl("bernoulli", TORCH_FN(tt_eager::ext::unary_random_seeded<ttnn::bernoulli>::invoke));
    // schema: bernoulli.out(Tensor self, *, Generator? generator=None, Tensor(a!) out) -> Tensor(a!)
    m.impl("bernoulli.out", TORCH_FN(tt_eager::ext::unary_random_seeded<ttnn::bernoulli>::invoke_into));
    // bernoulli_.Tensor
    // bernoulli_.float
    // cauchy_
    // exponential_
    // geometric_
    // normal_
    // random_ family: use ttnn::rand creator semantics to match PyTorch behavior
    // schema: random_(Tensor(a!) self, *, Generator? generator=None) -> Tensor(a!)
    m.impl("random_", TORCH_FN(tt_eager::ext::random_like_rand::invoke_inplace));
    // schema: random_.from(Tensor(a!) self, int from, int? to, *, Generator? generator=None) -> Tensor(a!)
    m.impl("random_.from", TORCH_FN(tt_eager::ext::random_like_rand::invoke_from_inplace));
    // schema: random_.to(Tensor(a!) self, int to, *, Generator? generator=None) -> Tensor(a!)
    m.impl("random_.to", TORCH_FN(tt_eager::ext::random_like_rand::invoke_to_inplace));
    // uniform_
    // schema: uniform_(Tensor(a!) self, float from=0, float to=1, *, Generator? generator=None) -> Tensor(a!)
    m.impl("uniform_", TORCH_FN(tt_eager::ext::unary_random_uniform<ttnn::uniform>::invoke_inplace));
}

}  // namespace tt_eager::ext

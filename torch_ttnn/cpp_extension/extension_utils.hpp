#pragma once

#include <vector>

#include "c10/core/ScalarType.h"
#include "c10/util/Exception.h"
#include "ttnn/operations/core/core.hpp"

template <typename Arg, typename... Args>
void doPrint(
    std::ostream& out,
    const std::string_view& filename,
    int lineno,
    const std::string_view& fn,
    Arg&& arg,
    Args&&... args) {
    out << std::format("{}({})({}): ", filename, lineno, fn);
    out << std::forward<Arg>(arg);
    ((out << std::forward<Args>(args)), ...);
    out << std::endl;
}
#define LOGGING(...) doPrint(std::cout, __FILE_NAME__, __LINE__, __FUNCTION__, __VA_ARGS__)

template <typename T>
void vector_compare(const std::vector<T>& first, const std::vector<T>& second) {
    TORCH_CHECK(first.size() == second.size());
    for (int i = 0; i < first.size(); ++i) {
        if (fabs(first[i] - second[i]) > 0.000001) {
            LOGGING("mismatch: ", first[i], " vs ", second[i]);
        }
    }
}

inline ttnn::DataType dtype_torch_to_ttnn(at::ScalarType dtype) {
    switch (dtype) {
        case at::ScalarType::Int:
        case at::ScalarType::Long: return ttnn::DataType::UINT32;
        case at::ScalarType::BFloat16: return ttnn::DataType::BFLOAT16;
        default: return ttnn::DataType::BFLOAT16;
    }
}

inline void convert_vector_from_uint32_to_int(std::vector<int>& dst_vector, const std::vector<uint32_t>& src_vector) {
    std::transform(
        src_vector.begin(),
        src_vector.end(),
        std::back_inserter(dst_vector),
        [](const uint32_t value) { return static_cast<int>(value); });
}

#define GET_OPTIONAL_OR_ASSERT(optional) ({TORCH_CHECK(optional.has_value()); optional.value();})

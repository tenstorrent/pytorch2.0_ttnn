#pragma once

#include <c10/core/ScalarType.h>
#include <c10/util/Exception.h>
#include <fmt/format.h>
#include <ttnn/operations/core/core.hpp>

template <typename T>
std::ostream& operator<<(std::ostream& os, const std::vector<T>& vec) {
    os << "[";
    for (size_t i = 0; i < vec.size(); ++i) {
        os << vec[i];
        if (i != vec.size() - 1) {
            os << ", ";
        }
    }
    os << "]";
    return os;
}

template <typename Arg, typename... Args>
void doPrint(
    std::ostream& out,
    const std::string_view& filename,
    int lineno,
    const std::string_view& fn,
    Arg&& arg,
    Args&&... args) {
    const auto DEBUG_CPP_EXT = std::getenv("DEBUG_CPP_EXT") != nullptr;
    if (DEBUG_CPP_EXT) {
        out << fmt::format("{}({})({}): ", filename, lineno, fn);
        out << std::forward<Arg>(arg);
        ((out << std::forward<Args>(args)), ...);
        out << std::endl;
    }
}

#define LOGGING(...) doPrint(std::cout, __FILE_NAME__, __LINE__, __FUNCTION__, __VA_ARGS__)

inline ttnn::DataType dtype_torch_to_ttnn(at::ScalarType dtype) {
    switch (dtype) {
        case at::ScalarType::Int:
        case at::ScalarType::Long: return ttnn::DataType::UINT32;
        case at::ScalarType::BFloat16: return ttnn::DataType::BFLOAT16;
        default: return ttnn::DataType::BFLOAT16;
    }
}

#define GET_OPTIONAL_OR_ASSERT(optional)             \
    ({                                               \
        TORCH_INTERNAL_ASSERT(optional.has_value()); \
        optional.value();                            \
    })

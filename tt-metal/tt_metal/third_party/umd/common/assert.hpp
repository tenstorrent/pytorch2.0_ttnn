/*
 * SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include <spdlog/spdlog.h>
#include <stdio.h>
#include <stdlib.h>

#include <iostream>
#include <sstream>
#include <vector>

#include "backtrace.hpp"

namespace tt {
template <typename A, typename B>
struct OStreamJoin {
    OStreamJoin(A const& a, B const& b, char const* delim = " ") : a(a), b(b), delim(delim) {}

    A const& a;
    B const& b;
    char const* delim;
};

template <typename A, typename B>
std::ostream& operator<<(std::ostream& os, tt::OStreamJoin<A, B> const& join) {
    os << join.a << join.delim << join.b;
    return os;
}
}  // namespace tt

namespace tt::assert {

inline void tt_assert_message(std::ostream& os) {}

template <typename T, typename... Ts>
void tt_assert_message(std::ostream& os, T const& t, Ts const&... ts) {
    os << t << std::endl;
    tt_assert_message(os, ts...);
}

template <typename... Ts>
[[noreturn]] void tt_throw(
    char const* file, int line, const std::string& assert_type, char const* condition_str, Ts const&... messages) {
    std::stringstream trace_message_ss = {};
    trace_message_ss << assert_type << " @ " << file << ":" << line << ": " << condition_str << std::endl;
    if constexpr (sizeof...(messages) > 0) {
        trace_message_ss << "info:" << std::endl;
        tt_assert_message(trace_message_ss, messages...);
    }
    trace_message_ss << "backtrace:\n";
    trace_message_ss << tt::assert::backtrace_to_string(100, 3, " --- ");
    trace_message_ss << std::flush;
    spdlog::default_logger()->flush();
    throw std::runtime_error(trace_message_ss.str());
}

template <typename... Ts>
void tt_assert(
    char const* file,
    int line,
    const std::string& assert_type,
    bool condition,
    char const* condition_str,
    Ts const&... messages) {
    if (not condition) {
        ::tt::assert::tt_throw(file, line, assert_type, condition_str, messages...);
    }
}

}  // namespace tt::assert

#define TT_ASSERT(condition, ...) \
    ::tt::assert::tt_assert(__FILE__, __LINE__, "TT_ASSERT", (condition), #condition, ##__VA_ARGS__)
#define TT_THROW(...) ::tt::assert::tt_throw(__FILE__, __LINE__, "TT_THROW", "tt::exception", ##__VA_ARGS__)

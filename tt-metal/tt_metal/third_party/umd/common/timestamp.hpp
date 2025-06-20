/*
 * SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include <fmt/format.h>

#include <chrono>
#include <string>

namespace tt::umd::util {

class Timestamp {
    std::chrono::steady_clock::time_point start;

public:
    Timestamp() : start(std::chrono::steady_clock::now()) {}

    void reset() { start = std::chrono::steady_clock::now(); }

    uint64_t nanoseconds() const {
        auto now = std::chrono::steady_clock::now();
        return std::chrono::duration_cast<std::chrono::nanoseconds>(now - start).count();
    }

    uint64_t microseconds() const {
        auto now = std::chrono::steady_clock::now();
        return std::chrono::duration_cast<std::chrono::microseconds>(now - start).count();
    }

    uint64_t milliseconds() const {
        auto now = std::chrono::steady_clock::now();
        return std::chrono::duration_cast<std::chrono::milliseconds>(now - start).count();
    }

    uint64_t seconds() const {
        auto now = std::chrono::steady_clock::now();
        return std::chrono::duration_cast<std::chrono::seconds>(now - start).count();
    }

    std::string to_string() const {
        auto ns = nanoseconds();
        if (ns < 1000) {
            return fmt::format("{} ns", ns);
        }
        auto us = microseconds();
        if (us < 1000) {
            return fmt::format("{} μs", us);
        }
        auto ms = milliseconds();
        if (ms < 1000) {
            return fmt::format("{} ms", ms);
        }
        return fmt::format("{} s", seconds());
    }
};

}  // namespace tt::umd::util

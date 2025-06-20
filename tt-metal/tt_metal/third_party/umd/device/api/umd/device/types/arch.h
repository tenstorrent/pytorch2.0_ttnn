/*
 * SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include <algorithm>
#include <ostream>

// Arch is common to everything related in TT, and not just UMD. It might move to some common folder someday.
// So we decided to put it in tt namespace instead of tt::umd.
namespace tt {

static inline std::string to_lower(const std::string &str) {
    std::string res = str;
    std::transform(res.begin(), res.end(), res.begin(), ::tolower);
    return res;
}

/**
 * Enums for different architectures.
 */
enum class ARCH {
    GRAYSKULL = 1,
    WORMHOLE_B0 = 2,
    BLACKHOLE = 3,
    QUASAR = 4,
    Invalid = 0xFF,
};

static inline tt::ARCH arch_from_str(const std::string &arch_str) {
    std::string arch_str_lower = to_lower(arch_str);

    if ((arch_str_lower == "wormhole") || (arch_str_lower == "wormhole_b0")) {
        return tt::ARCH::WORMHOLE_B0;
    } else if (arch_str_lower == "blackhole") {
        return tt::ARCH::BLACKHOLE;
    } else if (arch_str_lower == "quasar") {
        return tt::ARCH::QUASAR;
    } else {
        return tt::ARCH::Invalid;
    }
}

static inline std::string arch_to_str(const tt::ARCH arch) {
    switch (arch) {
        case tt::ARCH::WORMHOLE_B0:
            return "wormhole_b0";
        case tt::ARCH::BLACKHOLE:
            return "blackhole";
        case tt::ARCH::QUASAR:
            return "quasar";
        case tt::ARCH::Invalid:
        default:
            return "Invalid";
    }
}

static inline std::ostream &operator<<(std::ostream &out, const tt::ARCH &arch) { return out << arch_to_str(arch); }

}  // namespace tt

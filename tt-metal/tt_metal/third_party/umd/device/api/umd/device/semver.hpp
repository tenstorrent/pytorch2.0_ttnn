/*
 * SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include <cstdint>
#include <sstream>
#include <string>

#include "fmt/format.h"

namespace tt::umd {

/**
 * Based on Semantic Versioning 2.0.0 (https://semver.org/) but more permissive.
 * TT-KMD reports version strings that are technically not semver compliant.
 */

class semver_t {
public:
    uint64_t major;
    uint64_t minor;
    uint64_t patch;

    semver_t(uint64_t major, uint64_t minor, uint64_t patch) {
        this->major = major;
        this->minor = minor;
        this->patch = patch;
    }

    semver_t(const std::string& version_str) : semver_t(parse(version_str)) {}

    bool operator<(const semver_t& other) const {
        return std::tie(major, minor, patch) < std::tie(other.major, other.minor, other.patch);
    }

    bool operator>(const semver_t& other) const { return other < *this; }

    bool operator==(const semver_t& other) const {
        return std::tie(major, minor, patch) == std::tie(other.major, other.minor, other.patch);
    }

    bool operator!=(const semver_t& other) const { return !(*this == other); }

    bool operator<=(const semver_t& other) const { return !(other < *this); }

    bool operator>=(const semver_t& other) const { return !(*this < other); }

    std::string to_string() const { return fmt::format("{}.{}.{}", major, minor, patch); }

private:
    static semver_t parse(const std::string& version_str) {
        std::istringstream iss(version_str);
        std::string token;
        uint64_t major = 0;
        uint64_t minor = 0;
        uint64_t patch = 0;

        if (std::getline(iss, token, '.')) {
            major = std::stoull(token);

            if (std::getline(iss, token, '.')) {
                minor = std::stoull(token);

                if (std::getline(iss, token, '.')) {
                    patch = std::stoull(token);
                }
            }
        }
        return semver_t(major, minor, patch);
    }
};

}  // namespace tt::umd

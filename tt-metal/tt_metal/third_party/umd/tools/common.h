// SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0

#include <cxxopts.hpp>
#include <vector>

inline std::vector<int> extract_int_vector(const cxxopts::OptionValue& cxxoption) {
    std::vector<int> int_vector;
    for (std::string item : cxxoption.as<std::vector<std::string>>()) {
        int_vector.push_back(std::stoi(item));
    }
    return int_vector;
}

inline std::unordered_set<int> extract_int_set(const cxxopts::OptionValue& cxxoption) {
    std::unordered_set<int> int_set;
    for (std::string item : cxxoption.as<std::vector<std::string>>()) {
        int_set.insert(std::stoi(item));
    }
    return int_set;
}

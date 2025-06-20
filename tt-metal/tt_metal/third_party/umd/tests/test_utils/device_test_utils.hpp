/*
 * SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#pragma once

#include <cstdint>
#include <random>
#include <string>
#include <vector>

#include "umd/device/cluster.h"
#include "umd/device/tt_cluster_descriptor.h"

namespace test_utils {

template <typename T>
static void size_buffer_to_capacity(std::vector<T>& data_buf, std::size_t size_in_bytes) {
    std::size_t target_size = 0;
    if (size_in_bytes > 0) {
        target_size = ((size_in_bytes - 1) / sizeof(T)) + 1;
    }
    data_buf.resize(target_size);
}

static void read_data_from_device(
    tt::umd::Cluster& cluster,
    std::vector<uint32_t>& vec,
    chip_id_t chip_id,
    tt::umd::CoreCoord core,
    uint64_t addr,
    uint32_t size) {
    size_buffer_to_capacity(vec, size);
    cluster.read_from_device(vec.data(), chip_id, core, addr, size);
}

inline void fill_with_random_bytes(uint8_t* data, size_t n) {
    static std::random_device rd;
    static std::mt19937_64 gen(rd());
    uint64_t* data64 = reinterpret_cast<uint64_t*>(data);
    std::generate_n(data64, n / 8, [&]() { return gen(); });

    // Handle remaining bytes
    for (size_t i = (n / 8) * 8; i < n; ++i) {
        data[i] = static_cast<uint8_t>(gen());
    }
}

}  // namespace test_utils

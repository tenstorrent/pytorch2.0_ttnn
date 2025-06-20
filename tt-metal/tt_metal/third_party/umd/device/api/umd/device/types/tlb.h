/*
 * SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include <cstdint>
#include <optional>
#include <stdexcept>
#include <utility>

namespace tt::umd {

struct tlb_offsets {
    uint32_t local_offset;
    uint32_t x_end;
    uint32_t y_end;
    uint32_t x_start;
    uint32_t y_start;
    uint32_t noc_sel;
    uint32_t mcast;
    uint32_t ordering;
    uint32_t linked;
    uint32_t static_vc;
    uint32_t static_vc_end;
};

struct tlb_data {
    uint64_t local_offset = 0;
    uint64_t x_end = 0;
    uint64_t y_end = 0;
    uint64_t x_start = 0;
    uint64_t y_start = 0;
    uint64_t noc_sel = 0;
    uint64_t mcast = 0;
    uint64_t ordering = 0;
    uint64_t linked = 0;
    uint64_t static_vc = 0;

    // Orderings
    static constexpr uint64_t Relaxed = 0;
    static constexpr uint64_t Strict = 1;
    static constexpr uint64_t Posted = 2;

    bool check(const tlb_offsets &offset) const;
    std::pair<std::uint64_t, std::uint64_t> apply_offset(const tlb_offsets &offset) const;
};

struct tlb_configuration {
    uint64_t size;
    uint64_t base;
    uint64_t cfg_addr;
    uint64_t index_offset;
    uint64_t tlb_offset;
    tlb_offsets offset;
};

enum TlbMapping : uint8_t {
    UC = 0,  // Uncached
    WC = 1,  // Write-combined
};

}  // namespace tt::umd

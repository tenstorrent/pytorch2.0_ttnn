/*
 * SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include <cassert>
#include <ostream>
#include <vector>

#include "fmt/core.h"

enum tt_DevicePowerState { BUSY, SHORT_IDLE, LONG_IDLE };

enum tt_MemBarFlag {
    SET = 0xaa,
    RESET = 0xbb,
};

inline std::ostream& operator<<(std::ostream& os, const tt_DevicePowerState power_state) {
    switch (power_state) {
        case tt_DevicePowerState::BUSY:
            os << "Busy";
            break;
        case tt_DevicePowerState::SHORT_IDLE:
            os << "SHORT_IDLE";
            break;
        case tt_DevicePowerState::LONG_IDLE:
            os << "LONG_IDLE";
            break;
        default:
            throw("Unknown DevicePowerState");
    }
    return os;
}

struct barrier_address_params {
    std::uint32_t tensix_l1_barrier_base = 0;
    std::uint32_t eth_l1_barrier_base = 0;
    std::uint32_t dram_barrier_base = 0;
};

struct tt_device_dram_address_params {
    std::uint32_t DRAM_BARRIER_BASE = 0;
};

/**
 * Struct encapsulating all L1 Address Map parameters required by UMD.
 * These parameters are passed to the constructor.
 */
struct tt_device_l1_address_params {
    std::uint32_t tensix_l1_barrier_base = 0;
    std::uint32_t eth_l1_barrier_base = 0;
    std::uint32_t fw_version_addr = 0;
};

/**
 * Struct encapsulating all Host Address Map parameters required by UMD.
 * These parameters are passed to the constructor and are needed for non-MMIO transactions.
 */
struct tt_driver_host_address_params {
    std::uint32_t eth_routing_block_size = 0;
    std::uint32_t eth_routing_buffers_start = 0;
};

struct tt_driver_noc_params {
    std::uint32_t noc_addr_local_bits = 0;
    std::uint32_t noc_addr_node_id_bits = 0;
};

/**
 * Struct encapsulating all ERISC Firmware parameters required by UMD.
 * These parameters are passed to the constructor and are needed for non-MMIO transactions.
 */
struct tt_driver_eth_interface_params {
    std::uint32_t eth_rack_coord_width = 0;
    std::uint32_t cmd_buf_size_mask = 0;
    std::uint32_t max_block_size = 0;
    std::uint32_t request_cmd_queue_base = 0;
    std::uint32_t response_cmd_queue_base = 0;
    std::uint32_t cmd_counters_size_bytes = 0;
    std::uint32_t remote_update_ptr_size_bytes = 0;
    std::uint32_t cmd_data_block = 0;
    std::uint32_t cmd_wr_req = 0;
    std::uint32_t cmd_wr_ack = 0;
    std::uint32_t cmd_rd_req = 0;
    std::uint32_t cmd_rd_data = 0;
    std::uint32_t cmd_buf_size = 0;
    std::uint32_t cmd_data_block_dram = 0;
    std::uint32_t eth_routing_data_buffer_addr = 0;
    std::uint32_t request_routing_cmd_queue_base = 0;
    std::uint32_t response_routing_cmd_queue_base = 0;
    std::uint32_t cmd_buf_ptr_mask = 0;
    std::uint32_t cmd_ordered = 0;
    std::uint32_t cmd_broadcast = 0;
};

struct tt_version {
    std::uint16_t major = 0xffff;
    std::uint8_t minor = 0xff;
    std::uint8_t patch = 0xff;

    tt_version() {}

    tt_version(std::uint16_t major_, std::uint8_t minor_, std::uint8_t patch_) {
        major = major_;
        minor = minor_;
        patch = patch_;
    }

    tt_version(std::uint32_t version) {
        major = (version >> 16) & 0xff;
        minor = (version >> 12) & 0xf;
        patch = version & 0xfff;
    }

    std::string str() const { return fmt::format("{}.{}.{}", major, minor, patch); }
};

struct tt_device_params {
    bool register_monitor = false;
    bool enable_perf_scoreboard = false;
    std::vector<std::string> vcd_dump_cores;
    std::vector<std::string> plusargs;
    bool init_device = true;
    bool early_open_device = false;
    int aiclk = 0;

    // The command-line input for vcd_dump_cores can have the following format:
    // {"*-2", "1-*", "*-*", "1-2"}
    // '*' indicates we must dump all the cores in that dimension.
    // This function takes the vector above and unrolles the coords with '*' in one or both dimensions.
    std::vector<std::string> unroll_vcd_dump_cores(tt_xy_pair grid_size) const {
        std::vector<std::string> unrolled_dump_core;
        for (auto& dump_core : vcd_dump_cores) {
            // If the input is a single *, then dump all cores.
            if (dump_core == "*") {
                for (size_t x = 0; x < grid_size.x; x++) {
                    for (size_t y = 0; y < grid_size.y; y++) {
                        std::string current_core_coord = fmt::format("{}-{}", x, y);
                        if (std::find(
                                std::begin(unrolled_dump_core), std::end(unrolled_dump_core), current_core_coord) ==
                            std::end(unrolled_dump_core)) {
                            unrolled_dump_core.push_back(current_core_coord);
                        }
                    }
                }
                continue;
            }
            // Each core coordinate must contain three characters: "core.x-core.y".
            assert(dump_core.size() <= 5);
            size_t delimiter_pos = dump_core.find('-');
            assert(delimiter_pos != std::string::npos);  // y-dim should exist in core coord.

            std::string core_dim_x = dump_core.substr(0, delimiter_pos);
            size_t core_dim_y_start = delimiter_pos + 1;
            std::string core_dim_y = dump_core.substr(core_dim_y_start, dump_core.length() - core_dim_y_start);

            if (core_dim_x == "*" && core_dim_y == "*") {
                for (size_t x = 0; x < grid_size.x; x++) {
                    for (size_t y = 0; y < grid_size.y; y++) {
                        std::string current_core_coord = fmt::format("{}-{}", x, y);
                        if (std::find(
                                std::begin(unrolled_dump_core), std::end(unrolled_dump_core), current_core_coord) ==
                            std::end(unrolled_dump_core)) {
                            unrolled_dump_core.push_back(current_core_coord);
                        }
                    }
                }
            } else if (core_dim_x == "*") {
                for (size_t x = 0; x < grid_size.x; x++) {
                    std::string current_core_coord = fmt::format("{}-{}", x, core_dim_y);
                    if (std::find(std::begin(unrolled_dump_core), std::end(unrolled_dump_core), current_core_coord) ==
                        std::end(unrolled_dump_core)) {
                        unrolled_dump_core.push_back(current_core_coord);
                    }
                }
            } else if (core_dim_y == "*") {
                for (size_t y = 0; y < grid_size.y; y++) {
                    std::string current_core_coord = fmt::format("{}-{}", core_dim_x, y);
                    if (std::find(std::begin(unrolled_dump_core), std::end(unrolled_dump_core), current_core_coord) ==
                        std::end(unrolled_dump_core)) {
                        unrolled_dump_core.push_back(current_core_coord);
                    }
                }
            } else {
                unrolled_dump_core.push_back(dump_core);
            }
        }
        return unrolled_dump_core;
    }

    std::vector<std::string> expand_plusargs() const {
        std::vector<std::string> all_plusargs{
            fmt::format("+enable_perf_scoreboard={}", enable_perf_scoreboard),
            fmt::format("+register_monitor={}", register_monitor)};

        all_plusargs.insert(all_plusargs.end(), plusargs.begin(), plusargs.end());

        return all_plusargs;
    }
};

constexpr inline bool operator==(const tt_version& a, const tt_version& b) {
    return a.major == b.major && a.minor == b.minor && a.patch == b.patch;
}

constexpr inline bool operator>=(const tt_version& a, const tt_version& b) {
    bool fw_major_greater = a.major > b.major;
    bool fw_minor_greater = (a.major == b.major) && (a.minor > b.minor);
    bool patch_greater_or_equal = (a.major == b.major) && (a.minor == b.minor) && (a.patch >= b.patch);
    return fw_major_greater || fw_minor_greater || patch_greater_or_equal;
}

struct hugepage_mapping {
    void* mapping = nullptr;
    size_t mapping_size = 0;
    uint64_t physical_address = 0;  // or IOVA, if IOMMU is enabled
};

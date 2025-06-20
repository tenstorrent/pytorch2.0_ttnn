/*
 * SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include "umd/device/chip/chip.h"

namespace tt::umd {
class MockChip : public Chip {
public:
    MockChip(tt_SocDescriptor soc_descriptor);
    bool is_mmio_capable() const override;

    void start_device() override;
    void close_device() override;

    void write_to_device(tt_xy_pair core, const void* src, uint64_t l1_dest, uint32_t size) override;
    void read_from_device(tt_xy_pair core, void* dest, uint64_t l1_src, uint32_t size) override;

    int arc_msg(
        uint32_t msg_code,
        bool wait_for_done,
        uint32_t arg0,
        uint32_t arg1,
        uint32_t timeout_ms,
        uint32_t* return_3,
        uint32_t* return_4) override;

    void l1_membar(const std::unordered_set<tt::umd::CoreCoord>& cores = {}) override;
    void dram_membar(const std::unordered_set<tt::umd::CoreCoord>& cores = {}) override;
    void dram_membar(const std::unordered_set<uint32_t>& channels = {}) override;

    void deassert_risc_resets() override;
    void set_power_state(tt_DevicePowerState state) override;
    int get_clock() override;
};
}  // namespace tt::umd

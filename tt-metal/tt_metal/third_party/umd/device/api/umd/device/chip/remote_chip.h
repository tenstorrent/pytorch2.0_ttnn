/*
 * SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include "umd/device/chip/chip.h"
#include "umd/device/remote_communication.h"
#include "umd/device/tt_device/remote_wormhole_tt_device.h"

namespace tt::umd {
class LocalChip;

class RemoteChip : public Chip {
public:
    RemoteChip(tt_SocDescriptor soc_descriptor, std::unique_ptr<RemoteWormholeTTDevice> remote_tt_device);

    bool is_mmio_capable() const override;

    void start_device() override;
    void close_device() override;

    void write_to_device(tt_xy_pair core, const void* src, uint64_t l1_dest, uint32_t size) override;
    void read_from_device(tt_xy_pair core, void* dest, uint64_t l1_src, uint32_t size) override;

    void wait_for_non_mmio_flush() override;

    void l1_membar(const std::unordered_set<tt::umd::CoreCoord>& cores = {}) override;
    void dram_membar(const std::unordered_set<tt::umd::CoreCoord>& cores = {}) override;
    void dram_membar(const std::unordered_set<uint32_t>& channels = {}) override;

    void deassert_risc_resets() override;
    void set_power_state(tt_DevicePowerState state) override;
    int get_clock() override;

private:
    tt_xy_pair translate_chip_coord_virtual_to_translated(const tt_xy_pair core);

    LocalChip* local_chip_;
    RemoteCommunication* remote_communication_;
};
}  // namespace tt::umd

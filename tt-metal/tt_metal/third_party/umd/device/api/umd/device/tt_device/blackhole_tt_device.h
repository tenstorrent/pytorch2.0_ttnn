/*
 * SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include <set>

#include "umd/device/blackhole_arc_telemetry_reader.h"
#include "umd/device/tt_device/tt_device.h"

namespace tt::umd {
class BlackholeTTDevice : public TTDevice {
public:
    BlackholeTTDevice(std::shared_ptr<PCIDevice> pci_device);
    ~BlackholeTTDevice();

    void configure_iatu_region(size_t region, uint64_t target, size_t region_size) override;

    void wait_arc_core_start(const tt_xy_pair arc_core, const uint32_t timeout_ms = 1000) override;

    uint32_t get_clock() override;

    uint32_t get_max_clock_freq() override;

    uint32_t get_min_clock_freq() override;

    uint64_t get_board_id() override;

    bool get_noc_translation_enabled() override;

    void dma_d2h(void *dst, uint32_t src, size_t size) override;

    void dma_h2d(uint32_t dst, const void *src, size_t size) override;

    void dma_h2d_zero_copy(uint32_t dst, const void *src, size_t size) override;

    void dma_d2h_zero_copy(void *dst, uint32_t src, size_t size) override;

    std::vector<DramTrainingStatus> get_dram_training_status() override;

    ChipInfo get_chip_info() override;

    void wait_eth_core_training(const tt_xy_pair eth_core, const uint32_t timeout_ms = 60000) override;

protected:
    BlackholeTTDevice() = default;

private:
    static constexpr uint64_t ATU_OFFSET_IN_BH_BAR2 = 0x1200;
    std::set<size_t> iatu_regions_;
};
}  // namespace tt::umd

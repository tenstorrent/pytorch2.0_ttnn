/*
 * SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include <cstdint>
#include <filesystem>
#include <vector>

#include "umd/device/chip/chip.h"
#include "umd/device/cluster.h"
#include "umd/device/tt_simulation_host.hpp"

class tt_SimulationDeviceInit {
public:
    tt_SimulationDeviceInit(const std::filesystem::path& simulator_directory);

    tt::ARCH get_arch_name() const { return soc_descriptor.arch; }

    const tt_SocDescriptor& get_soc_descriptor() const { return soc_descriptor; }

    std::filesystem::path get_simulator_path() const { return simulator_directory / "run.sh"; }

private:
    std::filesystem::path simulator_directory;
    tt_SocDescriptor soc_descriptor;
};

class tt_SimulationDevice : public tt::umd::Chip {
public:
    tt_SimulationDevice(const std::filesystem::path& simulator_directory) :
        tt_SimulationDevice(tt_SimulationDeviceInit(simulator_directory)) {}

    tt_SimulationDevice(const tt_SimulationDeviceInit& init);
    ~tt_SimulationDevice();

    tt_SimulationHost host;

    void start_device() override;
    void close_device() override;

    bool is_mmio_capable() const override { return false; }

    void set_remote_transfer_ethernet_cores(const std::unordered_set<tt::umd::CoreCoord>& cores) override;

    // All tt_xy_pair cores in this class are defined in VIRTUAL coords.
    void write_to_device(tt_xy_pair core, const void* src, uint64_t l1_dest, uint32_t size) override;
    void read_from_device(tt_xy_pair core, void* dest, uint64_t l1_src, uint32_t size) override;
    void dma_write_to_device(const void* src, size_t size, tt_xy_pair core, uint64_t addr) override;
    void dma_read_from_device(void* dst, size_t size, tt_xy_pair core, uint64_t addr) override;

    void wait_for_non_mmio_flush() override;

    void l1_membar(const std::unordered_set<tt::umd::CoreCoord>& cores = {}) override;
    void dram_membar(const std::unordered_set<tt::umd::CoreCoord>& cores = {}) override;
    void dram_membar(const std::unordered_set<uint32_t>& channels = {}) override;

    void send_tensix_risc_reset(tt_xy_pair core, const TensixSoftResetOptions& soft_resets) override;
    void send_tensix_risc_reset(const TensixSoftResetOptions& soft_resets) override;
    void deassert_risc_resets() override;

    void set_power_state(tt_DevicePowerState state) override;
    int get_clock() override;

    int arc_msg(
        uint32_t msg_code,
        bool wait_for_done = true,
        uint32_t arg0 = 0,
        uint32_t arg1 = 0,
        uint32_t timeout_ms = 1000,
        uint32_t* return_3 = nullptr,
        uint32_t* return_4 = nullptr) override;

private:
    // State variables
    tt_driver_noc_params noc_params;
    std::set<chip_id_t> target_devices_in_cluster = {};
    std::set<chip_id_t> target_remote_chips = {};
    tt::ARCH arch_name;
    std::shared_ptr<tt_ClusterDescriptor> cluster_descriptor;
    std::unordered_map<chip_id_t, tt_SocDescriptor> soc_descriptor_per_chip = {};
};

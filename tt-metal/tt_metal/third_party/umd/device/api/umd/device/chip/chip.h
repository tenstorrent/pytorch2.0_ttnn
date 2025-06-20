/*
 * SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include <unordered_set>

#include "umd/device/tt_device/tt_device.h"
#include "umd/device/tt_silicon_driver_common.hpp"
#include "umd/device/tt_soc_descriptor.h"
#include "umd/device/types/cluster_descriptor_types.h"
#include "umd/device/types/cluster_types.h"
#include "umd/device/utils/lock_manager.h"

namespace tt::umd {

class TTDevice;
class SysmemManager;
class TLBManager;

// An abstract class that represents a chip.
class Chip {
public:
    Chip(tt_SocDescriptor soc_descriptor);

    Chip(const ChipInfo chip_info, tt_SocDescriptor soc_descriptor);

    virtual ~Chip() = default;

    virtual void start_device() = 0;
    virtual void close_device() = 0;

    tt_SocDescriptor& get_soc_descriptor();

    virtual bool is_mmio_capable() const = 0;

    void set_barrier_address_params(const barrier_address_params& barrier_address_params_);

    const ChipInfo& get_chip_info();

    virtual TTDevice* get_tt_device();
    virtual SysmemManager* get_sysmem_manager();
    virtual TLBManager* get_tlb_manager();

    virtual int get_num_host_channels();
    virtual int get_host_channel_size(std::uint32_t channel);
    virtual void write_to_sysmem(uint16_t channel, const void* src, uint64_t sysmem_dest, uint32_t size);
    virtual void read_from_sysmem(uint16_t channel, void* dest, uint64_t sysmem_src, uint32_t size);

    // All tt_xy_pair cores in this class are defined in VIRTUAL coords.
    virtual void write_to_device(tt_xy_pair core, const void* src, uint64_t l1_dest, uint32_t size) = 0;
    virtual void read_from_device(tt_xy_pair core, void* dest, uint64_t l1_src, uint32_t size) = 0;
    virtual void write_to_device_reg(tt_xy_pair core, const void* src, uint64_t reg_dest, uint32_t size);
    virtual void read_from_device_reg(tt_xy_pair core, void* dest, uint64_t reg_src, uint32_t size);

    // Will only ever work for LocalChip.
    virtual void dma_write_to_device(const void* src, size_t size, tt_xy_pair core, uint64_t addr);
    virtual void dma_read_from_device(void* dst, size_t size, tt_xy_pair core, uint64_t addr);

    virtual std::function<void(uint32_t, uint32_t, const uint8_t*)> get_fast_pcie_static_tlb_write_callable();

    virtual void wait_for_non_mmio_flush();

    virtual void l1_membar(const std::unordered_set<tt::umd::CoreCoord>& cores = {}) = 0;
    virtual void dram_membar(const std::unordered_set<tt::umd::CoreCoord>& cores = {}) = 0;
    virtual void dram_membar(const std::unordered_set<uint32_t>& channels = {}) = 0;

    virtual void send_tensix_risc_reset(tt_xy_pair core, const TensixSoftResetOptions& soft_resets);
    virtual void send_tensix_risc_reset(const TensixSoftResetOptions& soft_resets);
    virtual void deassert_risc_resets() = 0;

    virtual void set_power_state(tt_DevicePowerState state) = 0;
    virtual int get_clock() = 0;
    virtual int get_numa_node();

    virtual int arc_msg(
        uint32_t msg_code,
        bool wait_for_done = true,
        uint32_t arg0 = 0,
        uint32_t arg1 = 0,
        uint32_t timeout_ms = 1000,
        uint32_t* return_3 = nullptr,
        uint32_t* return_4 = nullptr);

    virtual void set_remote_transfer_ethernet_cores(const std::unordered_set<CoreCoord>& cores);
    virtual void set_remote_transfer_ethernet_cores(const std::set<uint32_t>& channel);

    // TODO: To be moved to private implementation once methods are moved to chip
    void enable_ethernet_queue(int timeout_s);

    // TODO: This should be private, once enough stuff is moved inside chip.
    // Probably also moved to LocalChip.
    tt_device_dram_address_params dram_address_params;
    tt_device_l1_address_params l1_address_params;
    tt_driver_host_address_params host_address_params;
    tt_driver_noc_params noc_params;
    tt_driver_eth_interface_params eth_interface_params;

protected:
    void wait_chip_to_be_ready();

    virtual void wait_eth_cores_training(const uint32_t timeout_ms = 60000);

    virtual void wait_dram_cores_training(const uint32_t timeout_ms = 60000);

    void set_default_params(ARCH arch);

    uint32_t get_power_state_arc_msg(tt_DevicePowerState state);

    ChipInfo chip_info_;

    tt_SocDescriptor soc_descriptor_;

    std::unique_ptr<TTDevice> tt_device_ = nullptr;
};

}  // namespace tt::umd

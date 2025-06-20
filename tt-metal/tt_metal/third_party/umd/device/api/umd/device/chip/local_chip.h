/*
 * SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include "umd/device/chip/chip.h"
#include "umd/device/chip_helpers/sysmem_manager.h"
#include "umd/device/chip_helpers/tlb_manager.h"
#include "umd/device/remote_communication.h"

namespace tt::umd {

class LocalChip : public Chip {
public:
    LocalChip(tt_SocDescriptor soc_descriptor, int pci_device_id, int num_host_mem_channels = 0);

    LocalChip(std::string sdesc_path, std::unique_ptr<TTDevice> tt_device);

    LocalChip(std::unique_ptr<TTDevice> tt_device);

    bool is_mmio_capable() const override;

    void start_device() override;
    void close_device() override;

    SysmemManager* get_sysmem_manager() override;
    TLBManager* get_tlb_manager() override;

    void set_remote_transfer_ethernet_cores(const std::unordered_set<CoreCoord>& cores) override;
    void set_remote_transfer_ethernet_cores(const std::set<uint32_t>& channels) override;
    // TODO: Figure out if this should remain public or used another way.
    tt_xy_pair get_remote_transfer_ethernet_core();
    void update_active_eth_core_idx();
    int get_active_eth_core_idx();
    std::vector<CoreCoord> get_remote_transfer_ethernet_cores();

    int get_num_host_channels() override;
    int get_host_channel_size(std::uint32_t channel) override;
    void write_to_sysmem(uint16_t channel, const void* src, uint64_t sysmem_dest, uint32_t size) override;
    void read_from_sysmem(uint16_t channel, void* dest, uint64_t sysmem_src, uint32_t size) override;

    void write_to_device(tt_xy_pair core, const void* src, uint64_t l1_dest, uint32_t size) override;
    void read_from_device(tt_xy_pair core, void* dest, uint64_t l1_src, uint32_t size) override;
    void write_to_device_reg(tt_xy_pair core, const void* src, uint64_t reg_dest, uint32_t size) override;
    void read_from_device_reg(tt_xy_pair core, void* dest, uint64_t reg_src, uint32_t size) override;

    void dma_write_to_device(const void* src, size_t size, tt_xy_pair core, uint64_t addr) override;
    void dma_read_from_device(void* dst, size_t size, tt_xy_pair core, uint64_t addr) override;

    std::function<void(uint32_t, uint32_t, const uint8_t*)> get_fast_pcie_static_tlb_write_callable() override;

    void ethernet_broadcast_write(
        const void* src, uint64_t core_dest, uint32_t size, std::vector<int> broadcast_header);

    void wait_for_non_mmio_flush() override;
    void set_flush_non_mmio(bool flush_non_mmio);
    bool get_flush_non_mmio() const;

    void l1_membar(const std::unordered_set<tt::umd::CoreCoord>& cores = {}) override;
    void dram_membar(const std::unordered_set<tt::umd::CoreCoord>& cores = {}) override;
    void dram_membar(const std::unordered_set<uint32_t>& channels = {}) override;

    void deassert_risc_resets() override;
    void set_power_state(tt_DevicePowerState state) override;
    int get_clock() override;
    int get_numa_node() override;

    std::unique_lock<RobustMutex> acquire_mutex(std::string mutex_name, int pci_device_id);
    std::unique_lock<RobustMutex> acquire_mutex(MutexType mutex_type, int pci_device_id);

private:
    std::unique_ptr<TLBManager> tlb_manager_;
    std::unique_ptr<SysmemManager> sysmem_manager_;
    LockManager lock_manager_;
    // Used only for ethernet broadcast to all remote chips.
    std::unique_ptr<RemoteCommunication> remote_communication_;

    std::vector<CoreCoord> remote_transfer_eth_cores_;
    int active_eth_core_idx = 0;
    bool flush_non_mmio_ = false;

    void initialize_local_chip(int num_host_mem_channels = 0);
    void initialize_tlb_manager();
    void initialize_default_chip_mutexes();
    void initialize_membars();

    tt_xy_pair translate_chip_coord_virtual_to_translated(const tt_xy_pair core) const;

    void check_pcie_device_initialized();
    int test_setup_interface();
    void init_pcie_iatus();

    void set_membar_flag(
        const std::vector<CoreCoord>& cores, const uint32_t barrier_value, const uint32_t barrier_addr);
    void insert_host_to_device_barrier(const std::vector<CoreCoord>& cores, const uint32_t barrier_addr);

    void wait_for_aiclk_value(tt_DevicePowerState power_state, const uint32_t timeout_ms = 5000);

protected:
    void wait_eth_cores_training(const uint32_t timeout_ms = 60000) override;

    void wait_dram_cores_training(const uint32_t timeout_ms = 60000) override;
};
}  // namespace tt::umd

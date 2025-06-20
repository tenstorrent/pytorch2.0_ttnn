/*
 * SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include "umd/device/chip/local_chip.h"

#include <tt-logger/tt-logger.hpp>

#include "assert.hpp"
#include "umd/device/chip_helpers/tlb_manager.h"
#include "umd/device/driver_atomics.h"
#include "umd/device/tt_device/tt_device.h"
#include "umd/device/types/blackhole_arc.h"
#include "umd/device/types/blackhole_eth.h"
#include "umd/device/wormhole_implementation.h"

extern bool umd_use_noc1;

namespace tt::umd {

// TLB size for DRAM on blackhole - 4GB
const uint64_t BH_4GB_TLB_SIZE = 4ULL * 1024 * 1024 * 1024;

LocalChip::LocalChip(tt_SocDescriptor soc_descriptor, int pci_device_id, int num_host_mem_channels) :
    Chip(soc_descriptor) {
    tt_device_ = TTDevice::create(pci_device_id);
    chip_info_ = tt_device_->get_chip_info();
    tlb_manager_ = std::make_unique<TLBManager>(tt_device_.get());
    sysmem_manager_ = std::make_unique<SysmemManager>(tlb_manager_.get());
    remote_communication_ = std::make_unique<RemoteCommunication>(this);
    initialize_local_chip(num_host_mem_channels);
}

LocalChip::LocalChip(std::string sdesc_path, std::unique_ptr<TTDevice> tt_device) :
    Chip(
        tt_device->get_chip_info(),
        tt_SocDescriptor(
            sdesc_path,
            tt_device->get_chip_info().noc_translation_enabled,
            tt_device->get_chip_info().harvesting_masks,
            tt_device->get_chip_info().board_type)),
    tlb_manager_(std::make_unique<TLBManager>(tt_device.get())),
    sysmem_manager_(std::make_unique<SysmemManager>(tlb_manager_.get())) {
    tt_device_ = std::move(tt_device);
    initialize_local_chip();
}

LocalChip::LocalChip(std::unique_ptr<TTDevice> tt_device) :
    Chip(
        tt_device->get_chip_info(),
        tt_SocDescriptor(
            tt_device->get_arch(),
            tt_device->get_chip_info().noc_translation_enabled,
            tt_device->get_chip_info().harvesting_masks,
            tt_device->get_chip_info().board_type)),
    tlb_manager_(std::make_unique<TLBManager>(tt_device.get())),
    sysmem_manager_(std::make_unique<SysmemManager>(tlb_manager_.get())) {
    tt_device_ = std::move(tt_device);
    initialize_local_chip();
}

void LocalChip::initialize_local_chip(int num_host_mem_channels) {
    initialize_tlb_manager();
    if (num_host_mem_channels > 0) {
        sysmem_manager_->init_hugepage(num_host_mem_channels);
    }
    wait_chip_to_be_ready();
    initialize_default_chip_mutexes();
}

void LocalChip::initialize_tlb_manager() {
    // Setup default dynamic tlbs.
    tlb_manager_->set_dynamic_tlb_config(
        "LARGE_READ_TLB", tt_device_->get_architecture_implementation()->get_mem_large_read_tlb());
    tlb_manager_->set_dynamic_tlb_config(
        "LARGE_WRITE_TLB", tt_device_->get_architecture_implementation()->get_mem_large_write_tlb());
    tlb_manager_->set_dynamic_tlb_config("REG_TLB", tt_device_->get_architecture_implementation()->get_reg_tlb());
    tlb_manager_->set_dynamic_tlb_config(
        "SMALL_READ_WRITE_TLB", tt_device_->get_architecture_implementation()->get_small_read_write_tlb());
}

void LocalChip::initialize_default_chip_mutexes() {
    // These mutexes are intended to be based on physical devices/pci-intf not logical. Set these up ahead of
    // time here (during device init) since it's unsafe to modify shared state during multithreaded runtime.
    // cleanup_mutexes_in_shm is tied to clean_system_resources from the constructor. The main process is
    // responsible for initializing the driver with this field set to cleanup after an aborted process.
    int pci_device_id = tt_device_->get_pci_device()->get_device_num();
    // Initialize Dynamic TLB mutexes
    for (auto& tlb : tlb_manager_->dynamic_tlb_config_) {
        lock_manager_.initialize_mutex(tlb.first, pci_device_id);
    }

    // Initialize non-MMIO mutexes for WH devices regardless of number of chips, since these may be used for
    // ethernet broadcast
    if (tt_device_->get_arch() == tt::ARCH::WORMHOLE_B0) {
        lock_manager_.initialize_mutex(MutexType::NON_MMIO, pci_device_id);
        lock_manager_.initialize_mutex(MutexType::REMOTE_ARC_MSG, pci_device_id);
    }

    // Initialize interprocess mutexes to make host -> device memory barriers atomic
    lock_manager_.initialize_mutex(MutexType::MEM_BARRIER, pci_device_id);
}

void LocalChip::initialize_membars() {
    set_membar_flag(
        soc_descriptor_.get_cores(CoreType::TENSIX, CoordSystem::VIRTUAL),
        tt_MemBarFlag::RESET,
        l1_address_params.tensix_l1_barrier_base);
    set_membar_flag(
        soc_descriptor_.get_cores(CoreType::ETH, CoordSystem::VIRTUAL),
        tt_MemBarFlag::RESET,
        l1_address_params.eth_l1_barrier_base);

    std::vector<CoreCoord> dram_cores_vector = {};
    for (std::uint32_t dram_idx = 0; dram_idx < soc_descriptor_.get_num_dram_channels(); dram_idx++) {
        dram_cores_vector.push_back(soc_descriptor_.get_dram_core_for_channel(dram_idx, 0, CoordSystem::VIRTUAL));
    }
    set_membar_flag(dram_cores_vector, tt_MemBarFlag::RESET, dram_address_params.DRAM_BARRIER_BASE);
}

SysmemManager* LocalChip::get_sysmem_manager() { return sysmem_manager_.get(); }

TLBManager* LocalChip::get_tlb_manager() { return tlb_manager_.get(); }

bool LocalChip::is_mmio_capable() const { return true; }

void LocalChip::start_device() {
    check_pcie_device_initialized();
    init_pcie_iatus();
    initialize_membars();
}

void LocalChip::close_device(){};

void LocalChip::wait_eth_cores_training(const uint32_t timeout_ms) {
    const std::vector<CoreCoord> eth_cores =
        get_soc_descriptor().get_cores(CoreType::ETH, umd_use_noc1 ? CoordSystem::NOC1 : CoordSystem::PHYSICAL);
    TTDevice* tt_device = get_tt_device();
    for (const CoreCoord& eth_core : eth_cores) {
        tt_device->wait_eth_core_training(eth_core, timeout_ms);
    }
}

int LocalChip::get_num_host_channels() { return sysmem_manager_->get_num_host_mem_channels(); }

int LocalChip::get_host_channel_size(std::uint32_t channel) {
    TT_ASSERT(channel < get_num_host_channels(), "Querying size for a host channel that does not exist.");
    hugepage_mapping hugepage_map = sysmem_manager_->get_hugepage_mapping(channel);
    TT_ASSERT(hugepage_map.mapping_size, "Host channel size can only be queried after the device has been started.");
    return hugepage_map.mapping_size;
}

void LocalChip::write_to_sysmem(uint16_t channel, const void* src, uint64_t sysmem_dest, uint32_t size) {
    sysmem_manager_->write_to_sysmem(channel, src, sysmem_dest, size);
}

void LocalChip::read_from_sysmem(uint16_t channel, void* dest, uint64_t sysmem_src, uint32_t size) {
    sysmem_manager_->read_from_sysmem(channel, dest, sysmem_src, size);
}

void LocalChip::write_to_device(tt_xy_pair core, const void* src, uint64_t l1_dest, uint32_t size) {
    const uint8_t* buffer_addr = static_cast<const uint8_t*>(src);

    log_debug(
        LogSiliconDriver,
        "Chip::write_to_device to pci dev {} core {}-{} at 0x{:x} size: {}",
        tt_device_->get_pci_device()->get_device_num(),
        core.x,
        core.y,
        l1_dest,
        size);

    if (tlb_manager_->is_tlb_mapped(core, l1_dest, size)) {
        tlb_configuration tlb_description = tlb_manager_->get_tlb_configuration(core);
        if (tt_device_->get_pci_device()->bar4_wc != nullptr && tlb_description.size == BH_4GB_TLB_SIZE) {
            // This is only for Blackhole. If we want to  write to DRAM (BAR4 space), we add offset
            // to which we write so write_block knows it needs to target BAR4
            tt_device_->write_block(
                (tlb_description.tlb_offset + l1_dest % tlb_description.size) + BAR0_BH_SIZE, size, buffer_addr);
        } else {
            tt_device_->write_block(tlb_description.tlb_offset + l1_dest % tlb_description.size, size, buffer_addr);
        }
    } else {
        std::string fallback_tlb = "LARGE_WRITE_TLB";
        const auto tlb_index = tlb_manager_->dynamic_tlb_config_.at(fallback_tlb);
        auto lock = acquire_mutex(fallback_tlb, tt_device_->get_pci_device()->get_device_num());

        while (size > 0) {
            auto [mapped_address, tlb_size] = tt_device_->set_dynamic_tlb(
                tlb_index,
                translate_chip_coord_virtual_to_translated(core),
                l1_dest,
                tlb_manager_->dynamic_tlb_ordering_modes_.at(fallback_tlb));
            uint32_t transfer_size = std::min((uint64_t)size, tlb_size);
            tt_device_->write_block(mapped_address, transfer_size, buffer_addr);

            size -= transfer_size;
            l1_dest += transfer_size;
            buffer_addr += transfer_size;
        }
        log_debug(LogSiliconDriver, "Write done Dynamic TLB with pid={}", (long)getpid());
    }
}

void LocalChip::read_from_device(tt_xy_pair core, void* dest, uint64_t l1_src, uint32_t size) {
    log_debug(
        LogSiliconDriver,
        "Chip::read_from_device from pci device {} core {}-{} at 0x{:x} size: {}",
        tt_device_->get_pci_device()->get_device_num(),
        core.x,
        core.y,
        l1_src,
        size);
    uint8_t* buffer_addr = static_cast<uint8_t*>(dest);

    if (tlb_manager_->is_tlb_mapped(core, l1_src, size)) {
        tlb_configuration tlb_description = tlb_manager_->get_tlb_configuration(core);
        if (tt_device_->get_pci_device()->bar4_wc != nullptr && tlb_description.size == BH_4GB_TLB_SIZE) {
            // This is only for Blackhole. If we want to  read from DRAM (BAR4 space), we add offset
            // from which we read so read_block knows it needs to target BAR4
            tt_device_->read_block(
                (tlb_description.tlb_offset + l1_src % tlb_description.size) + BAR0_BH_SIZE, size, buffer_addr);
        } else {
            tt_device_->read_block(tlb_description.tlb_offset + l1_src % tlb_description.size, size, buffer_addr);
        }
        log_debug(
            LogSiliconDriver,
            "  read_block called with tlb_offset: {}, tlb_size: {}",
            tlb_description.tlb_offset,
            tlb_description.size);
    } else {
        std::string fallback_tlb = "LARGE_READ_TLB";
        const auto tlb_index = tlb_manager_->dynamic_tlb_config_.at(fallback_tlb);
        auto lock = acquire_mutex(fallback_tlb, tt_device_->get_pci_device()->get_device_num());
        log_debug(LogSiliconDriver, "  dynamic tlb_index: {}", tlb_index);
        while (size > 0) {
            auto [mapped_address, tlb_size] = tt_device_->set_dynamic_tlb(
                tlb_index,
                translate_chip_coord_virtual_to_translated(core),
                l1_src,
                tlb_manager_->dynamic_tlb_ordering_modes_.at(fallback_tlb));
            uint32_t transfer_size = std::min((uint64_t)size, tlb_size);
            tt_device_->read_block(mapped_address, transfer_size, buffer_addr);

            size -= transfer_size;
            l1_src += transfer_size;
            buffer_addr += transfer_size;
        }
        log_debug(LogSiliconDriver, "Read done Dynamic TLB with pid={}", (long)getpid());
    }
}

void LocalChip::dma_write_to_device(const void* src, size_t size, tt_xy_pair core, uint64_t addr) {
    static const std::string tlb_name = "LARGE_WRITE_TLB";

    const uint8_t* buffer = static_cast<const uint8_t*>(src);

    auto tlb_index = tlb_manager_->dynamic_tlb_config_.at(tlb_name);
    auto ordering = tlb_manager_->dynamic_tlb_ordering_modes_.at(tlb_name);
    PCIDevice* pci_device = tt_device_->get_pci_device().get();
    size_t dmabuf_size = pci_device->get_dma_buffer().size;

    core = translate_chip_coord_virtual_to_translated(core);

    auto lock = acquire_mutex(tlb_name, pci_device->get_device_num());
    while (size > 0) {
        auto [axi_address, tlb_size] = tt_device_->set_dynamic_tlb(tlb_index, core, addr, ordering);

        size_t transfer_size = std::min({size, tlb_size, dmabuf_size});

        tt_device_->dma_h2d(axi_address, buffer, transfer_size);

        size -= transfer_size;
        addr += transfer_size;
        buffer += transfer_size;
    }
}

void LocalChip::dma_read_from_device(void* dst, size_t size, tt_xy_pair core, uint64_t addr) {
    static const std::string tlb_name = "LARGE_READ_TLB";
    uint8_t* buffer = static_cast<uint8_t*>(dst);
    auto tlb_index = tlb_manager_->dynamic_tlb_config_.at(tlb_name);
    auto ordering = tlb_manager_->dynamic_tlb_ordering_modes_.at(tlb_name);
    PCIDevice* pci_device = tt_device_->get_pci_device().get();
    size_t dmabuf_size = pci_device->get_dma_buffer().size;

    core = translate_chip_coord_virtual_to_translated(core);

    auto lock = acquire_mutex(tlb_name, pci_device->get_device_num());
    while (size > 0) {
        auto [axi_address, tlb_size] = tt_device_->set_dynamic_tlb(tlb_index, core, addr, ordering);

        size_t transfer_size = std::min({size, tlb_size, dmabuf_size});

        tt_device_->dma_d2h(buffer, axi_address, transfer_size);

        size -= transfer_size;
        addr += transfer_size;
        buffer += transfer_size;
    }
}

std::function<void(uint32_t, uint32_t, const uint8_t*)> LocalChip::get_fast_pcie_static_tlb_write_callable() {
    const auto callable = [this](uint32_t byte_addr, uint32_t num_bytes, const uint8_t* buffer_addr) {
        tt_device_->write_block(byte_addr, num_bytes, buffer_addr);
    };

    return callable;
}

void LocalChip::write_to_device_reg(tt_xy_pair core, const void* src, uint64_t reg_dest, uint32_t size) {
    if (size % sizeof(uint32_t) != 0) {
        throw std::runtime_error("Size must be a multiple of 4 bytes");
    }

    if (reg_dest % sizeof(uint32_t) != 0) {
        throw std::runtime_error("Register address must be 4-byte aligned");
    }

    std::string fallback_tlb = "REG_TLB";
    const auto tlb_index = tlb_manager_->dynamic_tlb_config_.at(fallback_tlb);
    auto lock = lock_manager_.acquire_mutex(fallback_tlb, tt_device_->get_pci_device()->get_device_num());
    log_debug(LogSiliconDriver, "  dynamic tlb_index: {}", tlb_index);

    auto [mapped_address, tlb_size] = tt_device_->set_dynamic_tlb(
        tlb_index, translate_chip_coord_virtual_to_translated(core), reg_dest, tt::umd::tlb_data::Strict);
    tt_device_->write_regs(mapped_address, size / sizeof(uint32_t), src);
}

void LocalChip::read_from_device_reg(tt_xy_pair core, void* dest, uint64_t reg_src, uint32_t size) {
    if (size % sizeof(uint32_t) != 0) {
        throw std::runtime_error("Size must be a multiple of 4 bytes");
    }

    if (reg_src % sizeof(uint32_t) != 0) {
        throw std::runtime_error("Register address must be 4-byte aligned");
    }

    std::string fallback_tlb = "REG_TLB";
    const auto tlb_index = tlb_manager_->dynamic_tlb_config_.at(fallback_tlb);
    auto lock = lock_manager_.acquire_mutex(fallback_tlb, tt_device_->get_pci_device()->get_device_num());
    log_debug(LogSiliconDriver, "  dynamic tlb_index: {}", tlb_index);

    auto [mapped_address, tlb_size] = tt_device_->set_dynamic_tlb(
        tlb_index, translate_chip_coord_virtual_to_translated(core), reg_src, tt::umd::tlb_data::Strict);
    tt_device_->read_regs(mapped_address, size / sizeof(uint32_t), dest);
}

void LocalChip::ethernet_broadcast_write(
    const void* src, uint64_t core_dest, uint32_t size, std::vector<int> broadcast_header) {
    // target_chip and target_core are ignored when broadcast is enabled.
    remote_communication_->write_to_non_mmio({0, 0, 0, 0}, {0, 0}, src, core_dest, size, true, broadcast_header);
}

void LocalChip::wait_for_non_mmio_flush() {
    // This is a local chip, so no need to flush remote communication.
}

void LocalChip::set_flush_non_mmio(bool flush_non_mmio) { flush_non_mmio_ = flush_non_mmio; }

bool LocalChip::get_flush_non_mmio() const { return flush_non_mmio_; }

tt_xy_pair LocalChip::translate_chip_coord_virtual_to_translated(const tt_xy_pair core) const {
    CoreCoord core_coord = soc_descriptor_.get_coord_at(core, CoordSystem::VIRTUAL);
    // Since NOC1 and translated coordinate space overlaps for Tensix cores on Blackhole,
    // Tensix cores are always used in translated space. Other cores are used either in
    // NOC1 or translated space depending on the umd_use_noc1 flag.
    // On Wormhole Tensix can use NOC1 space if umd_use_noc1 is set to true.
    if (soc_descriptor_.noc_translation_enabled) {
        if (soc_descriptor_.arch == tt::ARCH::BLACKHOLE) {
            return soc_descriptor_.translate_coord_to(core_coord, CoordSystem::TRANSLATED);
        } else {
            return soc_descriptor_.translate_coord_to(
                core_coord, umd_use_noc1 ? CoordSystem::NOC1 : CoordSystem::TRANSLATED);
        }
    } else {
        return soc_descriptor_.translate_coord_to(
            core_coord, umd_use_noc1 ? CoordSystem::NOC1 : CoordSystem::TRANSLATED);
    }
}

void LocalChip::set_remote_transfer_ethernet_cores(const std::unordered_set<CoreCoord>& active_eth_cores) {
    // Makes UMD aware of which ethernet cores have active links.
    // Based on this information, UMD determines which ethernet cores can be used for host->cluster non-MMIO transfers.
    // This overrides the default ethernet cores tagged for host to cluster routing in the constructor and must be
    // called for all MMIO devices, if default behaviour is not desired.
    TT_ASSERT(soc_descriptor_.arch == tt::ARCH::WORMHOLE_B0, "{} can only be called for Wormhole arch", __FUNCTION__);
    if (active_eth_cores.size() > 8) {
        // We cannot use more than 8 cores for umd access in one direction. Thats because of the available buffering in
        // the outgoing eth channels.
        log_warning(
            LogSiliconDriver, "Number of active ethernet cores {} exceeds the maximum of 8.", active_eth_cores.size());
    }
    remote_transfer_eth_cores_ = {};
    for (const auto& active_eth_core : active_eth_cores) {
        auto virtual_coord = soc_descriptor_.translate_coord_to(active_eth_core, CoordSystem::VIRTUAL);
        remote_transfer_eth_cores_.push_back(active_eth_core);
    }
}

void LocalChip::set_remote_transfer_ethernet_cores(const std::set<uint32_t>& channels) {
    std::unordered_set<CoreCoord> active_eth_cores;
    for (const auto& channel : channels) {
        active_eth_cores.insert(soc_descriptor_.get_eth_core_for_channel(channel));
    }
    set_remote_transfer_ethernet_cores(active_eth_cores);
}

tt_xy_pair LocalChip::get_remote_transfer_ethernet_core() {
    if (remote_transfer_eth_cores_.empty()) {
        throw std::runtime_error("No remote transfer ethernet cores set.");
    }
    return {remote_transfer_eth_cores_[active_eth_core_idx].x, remote_transfer_eth_cores_[active_eth_core_idx].y};
}

void LocalChip::update_active_eth_core_idx() {
    if (remote_transfer_eth_cores_.empty()) {
        throw std::runtime_error("Cannot update active Ethernet core index: no remote transfer Ethernet cores set.");
    }
    active_eth_core_idx = (active_eth_core_idx + 1) % remote_transfer_eth_cores_.size();
}

int LocalChip::get_active_eth_core_idx() { return active_eth_core_idx; }

std::vector<CoreCoord> LocalChip::get_remote_transfer_ethernet_cores() { return remote_transfer_eth_cores_; }

std::unique_lock<RobustMutex> LocalChip::acquire_mutex(std::string mutex_name, int pci_device_id) {
    return lock_manager_.acquire_mutex(mutex_name, pci_device_id);
}

std::unique_lock<RobustMutex> LocalChip::acquire_mutex(MutexType mutex_type, int pci_device_id) {
    return lock_manager_.acquire_mutex(mutex_type, pci_device_id);
}

void LocalChip::wait_dram_cores_training(const uint32_t timeout_ms) {
    TTDevice* tt_device = get_tt_device();

    auto start = std::chrono::system_clock::now();
    while (true) {
        std::vector<DramTrainingStatus> dram_training_status = tt_device->get_dram_training_status();

        if (dram_training_status.empty()) {
            // DRAM training status is not available, breaking the wait for DRAM training.
            break;
        }

        bool all_dram_channels_trained = true;
        const uint32_t chip_num_dram_channels =
            std::min(dram_training_status.size(), get_soc_descriptor().get_dram_cores().size());
        const uint32_t dram_harvesting_mask = get_soc_descriptor().harvesting_masks.dram_harvesting_mask;
        for (uint32_t dram_channel = 0; dram_channel < chip_num_dram_channels; dram_channel++) {
            // Skip the check for harvested channels.
            if (dram_harvesting_mask & (1 << dram_channel)) {
                continue;
            }

            // Check if there is an error in training for the channel.
            if (dram_training_status[dram_channel] == DramTrainingStatus::FAIL) {
                throw std::runtime_error("DRAM training failed");
            }

            // Verify whether the channel is trained.
            all_dram_channels_trained &= (dram_training_status[dram_channel] == DramTrainingStatus::SUCCESS);
        }

        if (all_dram_channels_trained) {
            break;
        }

        auto end = std::chrono::system_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
        if (duration.count() > timeout_ms) {
            throw std::runtime_error(fmt::format("DRAM training timed out after {} ms", timeout_ms));
            break;
        }
    }
}

void LocalChip::check_pcie_device_initialized() {
    if (test_setup_interface()) {
        throw std::runtime_error(
            "Device is incorrectly initialized. If this is a harvested Wormhole machine, it is likely that NOC "
            "Translation Tables are not enabled on device. These need to be enabled for the silicon driver to run.");
    }
}

int LocalChip::test_setup_interface() {
    int ret_val = 0;
    if (soc_descriptor_.arch == tt::ARCH::WORMHOLE_B0) {
        uint32_t mapped_reg = tt_device_
                                  ->set_dynamic_tlb(
                                      tt_device_->get_architecture_implementation()->get_reg_tlb(),
                                      translate_chip_coord_virtual_to_translated(tt_xy_pair(1, 0)),
                                      0xffb20108)
                                  .bar_offset;

        uint32_t regval = 0;
        tt_device_->read_regs(mapped_reg, 1, &regval);
        ret_val = (regval != HANG_READ_VALUE && (regval == 33)) ? 0 : 1;
        return ret_val;
    } else if (soc_descriptor_.arch == tt::ARCH::BLACKHOLE) {
        // TODO #768 figure out BH implementation
        return 0;
    } else {
        throw std::runtime_error(fmt::format("Unsupported architecture: {}", arch_to_str(soc_descriptor_.arch)));
    }
}

void LocalChip::init_pcie_iatus() {
    // TODO: this should go away soon; KMD knows how to do this at page pinning time.
    for (size_t channel = 0; channel < sysmem_manager_->get_num_host_mem_channels(); channel++) {
        hugepage_mapping hugepage_map = sysmem_manager_->get_hugepage_mapping(channel);
        size_t region_size = hugepage_map.mapping_size;

        if (!hugepage_map.mapping) {
            throw std::runtime_error(fmt::format("Hugepages are not allocated for ch: {}", channel));
        }

        if (soc_descriptor_.arch == tt::ARCH::WORMHOLE_B0) {
            // TODO: stop doing this.  The intent was good, but it's not
            // documented and nothing takes advantage of it.
            if (channel == 3) {
                region_size = HUGEPAGE_CHANNEL_3_SIZE_LIMIT;
            }
        }
        tt_device_->configure_iatu_region(channel, hugepage_map.physical_address, region_size);
    }
}

void LocalChip::set_membar_flag(
    const std::vector<CoreCoord>& cores, const uint32_t barrier_value, const uint32_t barrier_addr) {
    tt_driver_atomics::sfence();  // Ensure that writes before this do not get reordered
    std::unordered_set<CoreCoord> cores_synced = {};
    std::vector<uint32_t> barrier_val_vec = {barrier_value};
    for (const auto& core : cores) {
        write_to_device(
            soc_descriptor_.translate_coord_to(core, CoordSystem::VIRTUAL),
            barrier_val_vec.data(),
            barrier_addr,
            barrier_val_vec.size() * sizeof(uint32_t));
    }
    tt_driver_atomics::sfence();  // Ensure that all writes in the Host WC buffer are flushed
    while (cores_synced.size() != cores.size()) {
        for (const auto& core : cores) {
            if (cores_synced.find(core) == cores_synced.end()) {
                uint32_t readback_val;
                read_from_device(
                    soc_descriptor_.translate_coord_to(core, CoordSystem::VIRTUAL),
                    &readback_val,
                    barrier_addr,
                    sizeof(std::uint32_t));
                if (readback_val == barrier_value) {
                    cores_synced.insert(core);
                } else {
                    log_trace(
                        LogSiliconDriver,
                        "Waiting for core {} to recieve mem bar flag {} in function",
                        core.str(),
                        barrier_value);
                }
            }
        }
    }
    // Ensure that reads or writes after this do not get reordered.
    // Reordering can cause races where data gets transferred before the barrier has returned
    tt_driver_atomics::mfence();
}

void LocalChip::insert_host_to_device_barrier(const std::vector<CoreCoord>& cores, const uint32_t barrier_addr) {
    // Ensure that this memory barrier is atomic across processes/threads
    auto lock = lock_manager_.acquire_mutex(MutexType::MEM_BARRIER, tt_device_->get_pci_device()->get_device_num());
    set_membar_flag(cores, tt_MemBarFlag::SET, barrier_addr);
    set_membar_flag(cores, tt_MemBarFlag::RESET, barrier_addr);
}

void LocalChip::l1_membar(const std::unordered_set<tt::umd::CoreCoord>& cores) {
    if (cores.size()) {
        // Insert barrier on specific cores with L1
        std::vector<CoreCoord> workers_to_sync = {};
        std::vector<CoreCoord> eth_to_sync = {};

        for (const auto& core : cores) {
            auto core_from_soc = soc_descriptor_.get_coord_at(core, core.coord_system);
            if (core_from_soc.core_type == CoreType::TENSIX) {
                workers_to_sync.push_back(core);
            } else if (core_from_soc.core_type == CoreType::ETH) {
                eth_to_sync.push_back(core);
            } else {
                TT_THROW("Can only insert an L1 Memory barrier on Tensix or Ethernet cores.");
            }
        }
        insert_host_to_device_barrier(workers_to_sync, l1_address_params.tensix_l1_barrier_base);
        insert_host_to_device_barrier(eth_to_sync, l1_address_params.eth_l1_barrier_base);
    } else {
        // Insert barrier on all cores with L1
        insert_host_to_device_barrier(
            soc_descriptor_.get_cores(CoreType::TENSIX, CoordSystem::VIRTUAL),
            l1_address_params.tensix_l1_barrier_base);
        insert_host_to_device_barrier(
            soc_descriptor_.get_cores(CoreType::ETH, CoordSystem::VIRTUAL), l1_address_params.eth_l1_barrier_base);
    }
}

void LocalChip::dram_membar(const std::unordered_set<tt::umd::CoreCoord>& cores) {
    if (cores.size()) {
        for (const auto& core : cores) {
            TT_ASSERT(
                soc_descriptor_.get_coord_at(core, core.coord_system).core_type == CoreType::DRAM,
                "Can only insert a DRAM Memory barrier on DRAM cores.");
        }
        std::vector<CoreCoord> dram_cores_vector = std::vector<CoreCoord>(cores.begin(), cores.end());
        insert_host_to_device_barrier(dram_cores_vector, dram_address_params.DRAM_BARRIER_BASE);
    } else {
        // Insert Barrier on all DRAM Cores
        std::vector<CoreCoord> dram_cores_vector = {};
        for (std::uint32_t dram_idx = 0; dram_idx < soc_descriptor_.get_num_dram_channels(); dram_idx++) {
            dram_cores_vector.push_back(soc_descriptor_.get_dram_core_for_channel(dram_idx, 0, CoordSystem::VIRTUAL));
        }
        insert_host_to_device_barrier(dram_cores_vector, dram_address_params.DRAM_BARRIER_BASE);
    }
}

void LocalChip::dram_membar(const std::unordered_set<uint32_t>& channels) {
    std::unordered_set<CoreCoord> dram_cores_to_sync = {};
    for (const auto& chan : channels) {
        dram_cores_to_sync.insert(soc_descriptor_.get_dram_core_for_channel(chan, 0, CoordSystem::VIRTUAL));
    }
    dram_membar(dram_cores_to_sync);
}

void LocalChip::deassert_risc_resets() {
    if (soc_descriptor_.arch != tt::ARCH::BLACKHOLE) {
        arc_msg(
            wormhole::ARC_MSG_COMMON_PREFIX |
                tt_device_->get_architecture_implementation()->get_arc_message_deassert_riscv_reset(),
            true,
            0,
            0);
    }
}

void LocalChip::set_power_state(tt_DevicePowerState state) {
    int exit_code = 0;
    if (soc_descriptor_.arch == tt::ARCH::WORMHOLE_B0) {
        uint32_t msg = get_power_state_arc_msg(state);
        exit_code = arc_msg(wormhole::ARC_MSG_COMMON_PREFIX | msg, true, 0, 0);
    } else if (soc_descriptor_.arch == tt::ARCH::BLACKHOLE) {
        if (state == tt_DevicePowerState::BUSY) {
            exit_code = tt_device_->get_arc_messenger()->send_message(
                (uint32_t)tt::umd::blackhole::ArcMessageType::AICLK_GO_BUSY);
        } else {
            exit_code = tt_device_->get_arc_messenger()->send_message(
                (uint32_t)tt::umd::blackhole::ArcMessageType::AICLK_GO_LONG_IDLE);
        }
    }
    TT_ASSERT(exit_code == 0, "Failed to set power state to {} with exit code: {}", (int)state, exit_code);

    wait_for_aiclk_value(state);
}

void LocalChip::wait_for_aiclk_value(tt_DevicePowerState power_state, const uint32_t timeout_ms) {
    auto start = std::chrono::system_clock::now();
    uint32_t target_aiclk = 0;
    if (power_state == tt_DevicePowerState::BUSY) {
        target_aiclk = tt_device_->get_max_clock_freq();
    } else if (power_state == tt_DevicePowerState::LONG_IDLE) {
        target_aiclk = tt_device_->get_min_clock_freq();
    }
    uint32_t aiclk = tt_device_->get_clock();
    while (aiclk != target_aiclk) {
        auto end = std::chrono::system_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
        if (duration.count() > timeout_ms) {
            log_warning(
                LogSiliconDriver,
                "Waiting for AICLK value to settle failed on timeout after {}. Expected to see {}, last value "
                "observed {}",
                timeout_ms,
                target_aiclk,
                aiclk);
            return;
        }
        aiclk = tt_device_->get_clock();
    }
}

int LocalChip::get_clock() { return tt_device_->get_clock(); }

int LocalChip::get_numa_node() { return tt_device_->get_pci_device()->get_numa_node(); }
}  // namespace tt::umd

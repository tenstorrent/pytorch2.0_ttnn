/*
 * SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include "umd/device/chip_helpers/tlb_manager.h"

#include <tt-logger/tt-logger.hpp>

#include "assert.hpp"
#include "umd/device/tt_device/tt_device.h"
#include "umd/device/tt_io.hpp"
#include "umd/device/types/tlb.h"

namespace tt::umd {

static constexpr uint64_t DEFAULT_ORDERING_MODE = tlb_data::Relaxed;

TLBManager::TLBManager(TTDevice* tt_device) : tt_device_(tt_device) {}

void TLBManager::configure_tlb(
    tt_xy_pair core, tt_xy_pair translated_core, int32_t tlb_index, uint64_t address, uint64_t ordering) {
    TT_ASSERT(
        ordering == tlb_data::Strict || ordering == tlb_data::Posted || ordering == tlb_data::Relaxed,
        "Invalid ordering specified in Cluster::configure_tlb");
    log_debug(
        LogSiliconDriver,
        "Configuring TLB for chip: {} core: {} tlb_index: {} address: {} ordering: {}",
        tt_device_->get_pci_device()->get_device_num(),
        core.str(),
        tlb_index,
        address,
        ordering);
    TT_ASSERT(tlb_config_map_.find(tlb_index) == tlb_config_map_.end(), "TLB index already configured {}", tlb_index);

    tt_device_->set_dynamic_tlb(tlb_index, translated_core, address, ordering);
    auto tlb_size = tt_device_->get_architecture_implementation()->get_tlb_configuration(tlb_index).size;
    tlb_config_map_.insert({tlb_index, (address / tlb_size) * tlb_size});
    map_core_to_tlb_.insert({core, tlb_index});
}

void TLBManager::set_dynamic_tlb_config(std::string fallback_tlb_name, int32_t tlb_index) {
    TT_ASSERT(
        dynamic_tlb_config_.find(fallback_tlb_name) == dynamic_tlb_config_.end(),
        "Dynamic TLB already configured for {}",
        fallback_tlb_name);
    dynamic_tlb_config_.insert({fallback_tlb_name, tlb_index});
    dynamic_tlb_ordering_modes_[fallback_tlb_name] = DEFAULT_ORDERING_MODE;
}

void TLBManager::set_dynamic_tlb_config_ordering(std::string fallback_tlb_name, uint64_t ordering) {
    TT_ASSERT(
        ordering == tlb_data::Strict || ordering == tlb_data::Posted || ordering == tlb_data::Relaxed,
        "Invalid ordering specified in set_dynamic_tlb_config_ordering.");
    TT_ASSERT(
        fallback_tlb_name != "LARGE_READ_TLB" && fallback_tlb_name != "LARGE_WRITE_TLB",
        "Ordering modes for LARGE_READ_TLB and LARGE_WRITE_TLB cannot be modified.");
    TT_ASSERT(
        dynamic_tlb_config_.find(fallback_tlb_name) != dynamic_tlb_config_.end(),
        "Dynamic TLB not configured {}",
        fallback_tlb_name);

    dynamic_tlb_ordering_modes_[fallback_tlb_name] = ordering;
}

bool TLBManager::address_in_tlb_space(uint64_t address, uint32_t size_in_bytes, int32_t tlb_index, uint64_t tlb_size) {
    if (tlb_config_map_.find(tlb_index) != tlb_config_map_.end()) {
        auto mapped_address = tlb_config_map_.at(tlb_index);
        return address >= mapped_address && (address + size_in_bytes <= mapped_address + tlb_size);
    }
    return false;
}

bool TLBManager::is_tlb_mapped(tt_xy_pair core) { return map_core_to_tlb_.find(core) != map_core_to_tlb_.end(); }

bool TLBManager::is_tlb_mapped(tt_xy_pair core, uint64_t address, uint32_t size_in_bytes) {
    if (!is_tlb_mapped(core)) {
        return false;
    }

    int32_t tlb_index = map_core_to_tlb_.at(core);
    tlb_configuration tlb_description = tt_device_->get_architecture_implementation()->get_tlb_configuration(tlb_index);

    return address_in_tlb_space(address, size_in_bytes, tlb_index, tlb_description.size);
}

tt::Writer TLBManager::get_static_tlb_writer(tt_xy_pair core) {
    if (!is_tlb_mapped(core)) {
        throw std::runtime_error(fmt::format("TLBs not initialized for core: {}", core.str()));
    }

    if (!tt_device_->get_pci_device()->bar0_wc) {
        throw std::runtime_error("No write-combined mapping for BAR0");
    }

    auto tlb_index = map_core_to_tlb_.at(core);
    auto tlb_data = tt_device_->get_architecture_implementation()->get_tlb_configuration(tlb_index);

    auto* base = reinterpret_cast<uint8_t*>(tt_device_->get_pci_device()->bar0_wc);

    return tt::Writer(base + tlb_data.tlb_offset, tlb_data.size);
}

tlb_configuration TLBManager::get_tlb_configuration(tt_xy_pair core) {
    TT_ASSERT(is_tlb_mapped(core), "TLB not mapped for core: {}", core.str());

    int tlb_index = map_core_to_tlb_.at(core);
    return tt_device_->get_architecture_implementation()->get_tlb_configuration(tlb_index);
}

};  // namespace tt::umd

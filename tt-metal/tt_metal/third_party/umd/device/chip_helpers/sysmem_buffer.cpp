/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include "umd/device/chip_helpers/sysmem_buffer.h"

#include <tt-logger/tt-logger.hpp>

#include "umd/device/tt_device/tt_device.h"

namespace tt::umd {

SysmemBuffer::SysmemBuffer(TLBManager* tlb_manager, void* buffer_va, size_t buffer_size) :
    tlb_manager_(tlb_manager),
    buffer_va(buffer_va),
    buffer_size(buffer_size),
    device_io_addr(tlb_manager->get_tt_device()->get_pci_device()->map_for_dma(buffer_va, buffer_size)) {}

void SysmemBuffer::dma_write_to_device(size_t offset, size_t size, tt_xy_pair core, uint64_t addr) {
    static const std::string tlb_name = "LARGE_WRITE_TLB";

    TTDevice* tt_device_ = tlb_manager_->get_tt_device();
    const uint8_t* buffer = (uint8_t*)get_device_io_addr(offset);

    auto tlb_index = tlb_manager_->dynamic_tlb_config_.at(tlb_name);
    auto ordering = tlb_manager_->dynamic_tlb_ordering_modes_.at(tlb_name);
    PCIDevice* pci_device = tt_device_->get_pci_device().get();

    // TODO: these are chip functions, figure out how to have these
    // inside sysmem buffer, or we keep API as it is and make application send
    // proper coordinates.
    // core = translate_chip_coord_virtual_to_translated(core);
    // auto lock = acquire_mutex(tlb_name, pci_device->get_device_num());
    while (size > 0) {
        auto [axi_address, tlb_size] = tt_device_->set_dynamic_tlb(tlb_index, core, addr, ordering);

        size_t transfer_size = std::min({size, tlb_size});

        tt_device_->dma_h2d_zero_copy(axi_address, buffer, transfer_size);

        size -= transfer_size;
        addr += transfer_size;
        buffer += transfer_size;
    }
}

void SysmemBuffer::dma_read_from_device(size_t offset, size_t size, tt_xy_pair core, uint64_t addr) {
    static const std::string tlb_name = "LARGE_READ_TLB";
    uint8_t* buffer = (uint8_t*)get_device_io_addr(offset);
    TTDevice* tt_device_ = tlb_manager_->get_tt_device();
    auto tlb_index = tlb_manager_->dynamic_tlb_config_.at(tlb_name);
    auto ordering = tlb_manager_->dynamic_tlb_ordering_modes_.at(tlb_name);
    PCIDevice* pci_device = tt_device_->get_pci_device().get();
    size_t dmabuf_size = pci_device->get_dma_buffer().size;

    // TODO: these are chip functions, figure out how to have these
    // inside sysmem buffer, or we keep API as it is and make application send
    // proper coordinates.
    // core = translate_chip_coord_virtual_to_translated(core);
    // auto lock = acquire_mutex(tlb_name, pci_device->get_device_num());

    while (size > 0) {
        auto [axi_address, tlb_size] = tt_device_->set_dynamic_tlb(tlb_index, core, addr, ordering);

        size_t transfer_size = std::min({size, tlb_size});

        tt_device_->dma_d2h_zero_copy(buffer, axi_address, transfer_size);

        size -= transfer_size;
        addr += transfer_size;
        buffer += transfer_size;
    }
}

SysmemBuffer::~SysmemBuffer() {
    try {
        tlb_manager_->get_tt_device()->get_pci_device()->unmap_for_dma(buffer_va, buffer_size);
    } catch (...) {
        log_warning(
            LogSiliconDriver, "Failed to unmap sysmem buffer (size: {:#x}, IOVA: {:#x}).", buffer_size, device_io_addr);
    }
}

}  // namespace tt::umd

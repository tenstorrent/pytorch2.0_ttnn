/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#pragma once

#include <stddef.h>
#include <stdint.h>

#include "umd/device/chip_helpers/tlb_manager.h"
#include "umd/device/tt_xy_pair.h"

namespace tt::umd {

/**
 * SysmemBuffer class should represent the resource of the HOST memory that is visible to the device.
 * Currently, there are two types of sysmem buffers:
 * 1. Hugepage-based sysmem buffer, that represents old system memory scheme used, that we still want to support until
 * transition to IOMMU is complete.
 * 2. Sysmem buffer, that is used when the system is protected by an IOMMU. With IOMMU, the mappings can be requested at
 * much finer granularity than hugepages.
 *
 * Traditionally, we have referred to the sysmem buffer as something that is
 * visible to device, has its own NOC address. Without changes to KMD, this is still not fully supported for IOMMU
 * buffers.
 */
class SysmemBuffer {
public:
    SysmemBuffer(TLBManager* tlb_manager, void* buffer_va, size_t buffer_size);
    ~SysmemBuffer();

    void* get_buffer_va() const { return buffer_va; }

    size_t get_buffer_size() const { return buffer_size; }

    uint64_t get_device_io_addr(const size_t offset = 0) const { return device_io_addr + offset; }

    void dma_write_to_device(size_t offset, size_t size, tt_xy_pair core, uint64_t addr);

    void dma_read_from_device(size_t offset, size_t size, tt_xy_pair core, uint64_t addr);

private:
    TLBManager* tlb_manager_;

    // Virtual address in process addr space.
    void* buffer_va;

    size_t buffer_size;

    // Address that is used on the system bus to access the buffer.
    uint64_t device_io_addr;
};

}  // namespace tt::umd

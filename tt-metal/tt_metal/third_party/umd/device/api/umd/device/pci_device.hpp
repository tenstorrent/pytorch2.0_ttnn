/*
 * SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include <cstdint>
#include <cstdio>
#include <map>
#include <unordered_map>
#include <vector>

#include "fmt/format.h"
#include "umd/device/semver.hpp"
#include "umd/device/tt_device/tlb_handle.h"
#include "umd/device/tt_xy_pair.h"
#include "umd/device/types/arch.h"
#include "umd/device/types/tlb.h"

namespace tt::umd {
class semver_t;
}  // namespace tt::umd

struct PciDeviceInfo {
    uint16_t vendor_id;
    uint16_t device_id;
    uint16_t pci_domain;
    uint16_t pci_bus;
    uint16_t pci_device;
    uint16_t pci_function;

    tt::ARCH get_arch() const;
    // TODO: does it make sense to move attributes that we can read from sysfs
    // onto this struct as methods?  e.g. current_link_width etc.
};

// Do we want to put everything into this file into tt::umd namespace?
using tt::umd::semver_t;

struct DmaBuffer {
    uint8_t *buffer = nullptr;
    uint8_t *completion = nullptr;
    size_t size = 0;

    uint64_t buffer_pa = 0;
    uint64_t completion_pa = 0;
};

class PCIDevice {
    const std::string device_path;   // Path to character device: /dev/tenstorrent/N
    const int pci_device_num;        // N in /dev/tenstorrent/N
    const int pci_device_file_desc;  // Character device file descriptor
    const PciDeviceInfo info;        // PCI device info
    const int numa_node;             // -1 if non-NUMA
    const int revision;              // PCI revision value from sysfs
    const tt::ARCH arch;             // e.g. Wormhole, Blackhole
    const semver_t kmd_version;      // KMD version
    const bool iommu_enabled;        // Whether the system is protected from this device by an IOMMU
    DmaBuffer dma_buffer{};

public:
    /**
     * @return a list of integers corresponding to character devices in /dev/tenstorrent/
     */
    static std::vector<int> enumerate_devices();

    /**
     * @return a map of PCI device numbers (/dev/tenstorrent/N) to PciDeviceInfo
     */
    static std::map<int, PciDeviceInfo> enumerate_devices_info();

    /**
     * PCI device constructor.
     *
     * Opens the character device file descriptor, reads device information from
     * sysfs, and maps device memory region(s) into the process address space.
     *
     * @param pci_device_number     N in /dev/tenstorrent/N
     */
    PCIDevice(int pci_device_number);

    /**
     * PCIDevice destructor.
     * Unmaps device memory and closes chardev file descriptor.
     */
    ~PCIDevice();

    PCIDevice(const PCIDevice &) = delete;       // copy
    void operator=(const PCIDevice &) = delete;  // copy assignment

    /**
     * @return PCI device info
     */
    const PciDeviceInfo get_device_info() const { return info; }

    /**
     * @return which NUMA node this device is associated with, or -1 if non-NUMA
     */
    int get_numa_node() const { return numa_node; }

    /**
     * @return N in /dev/tenstorrent/N
     * TODO: target for removal; upper layers should not care about this.
     */
    int get_device_num() const { return pci_device_num; }

    /**
     * @return PCI device id
     */
    int get_pci_device_id() const { return info.device_id; }

    /**
     * @return PCI revision value from sysfs.
     * TODO: target for removal; upper layers should not care about this.
     */
    int get_pci_revision() const { return revision; }

    /**
     * @return what architecture this device is (e.g. Wormhole, Blackhole, etc.)
     */
    tt::ARCH get_arch() const { return arch; }

    /**
     * @return whether the system is protected from this device by an IOMMU
     */
    bool is_iommu_enabled() const { return iommu_enabled; }

    /**
     * Map a buffer for hugepage access.
     *
     * @param buffer must be page-aligned
     * @param size must be a multiple of the page size
     * @return uint64_t Physical Address of hugepage.
     */
    uint64_t map_for_hugepage(void *buffer, size_t size);

    /**
     * Map a buffer for DMA access by the device.
     *
     * Supports mapping physically-contiguous buffers (e.g. hugepages) for the
     * no-IOMMU case.
     *
     * @param buffer must be page-aligned
     * @param size must be a multiple of the page size
     * @return uint64_t PA (no IOMMU) or IOVA (with IOMMU) for use by the device
     */
    uint64_t map_for_dma(void *buffer, size_t size);

    /**
     * Access the device's DMA buffer.  This buffer is not guaranteed to exist.
     * It is the caller's responsibility to check if the buffer is valid and to
     * chunk the desired transfer size to fit within it.
     */
    DmaBuffer &get_dma_buffer() { return dma_buffer; }

    /**
     * Unmap a buffer that was previously mapped for DMA access.
     *
     * @param buffer must be page-aligned
     * @param size must be a multiple of the page size
     */
    void unmap_for_dma(void *buffer, size_t size);

    /**
     * Read KMD version installed on the system.
     */
    static semver_t read_kmd_version();

    /**
     * Allocate TLB resource from KMD.
     *
     * @param tlb_size Size of the TLB caller wants to allocate.
     * @param mapping_type Type of TLB mapping to allocate (UC or WC).
     */
    std::unique_ptr<tt::umd::TlbHandle> allocate_tlb(
        const size_t tlb_size, const tt::umd::TlbMapping tlb_mapping = tt::umd::TlbMapping::UC);

public:
    // TODO: we can and should make all of these private.
    void *bar0_uc = nullptr;
    size_t bar0_uc_size = 0;
    size_t bar0_uc_offset = 0;

    void *bar0_wc = nullptr;
    size_t bar0_wc_size = 0;

    void *bar2_uc = nullptr;
    size_t bar2_uc_size;

    void *bar4_wc = nullptr;
    uint64_t bar4_wc_size;

    // TODO: let's get rid of this unless we need to run UMD on WH systems with
    // shrunk BAR0.  If we don't (and we shouldn't), then we can just use BAR0
    // and simplify the code.
    void *system_reg_mapping = nullptr;
    size_t system_reg_mapping_size;
    uint32_t system_reg_start_offset;   // Registers >= this are system regs, use the mapping.
    uint32_t system_reg_offset_adjust;  // This is the offset of the first reg in the system reg mapping.

    uint32_t read_checking_offset;

    template <typename T>
    T *get_register_address(uint32_t register_offset) {
        // Right now, address can either be exposed register in BAR, or TLB window in BAR0 (BAR4 for Blackhole).
        // Should clarify this interface
        void *reg_mapping;
        if (system_reg_mapping != nullptr && register_offset >= system_reg_start_offset) {
            register_offset -= system_reg_offset_adjust;
            reg_mapping = system_reg_mapping;
        } else if (bar0_wc != bar0_uc && register_offset < bar0_wc_size) {
            reg_mapping = bar0_wc;
        } else {
            register_offset -= bar0_uc_offset;
            reg_mapping = bar0_uc;
        }
        return reinterpret_cast<T *>(static_cast<uint8_t *>(reg_mapping) + register_offset);
    }
};

/*
 * SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include "umd/device/pci_device.hpp"

#include <fcntl.h>      // for ::open
#include <linux/pci.h>  // for PCI_SLOT, PCI_FUNC
#include <sys/ioctl.h>  // for ioctl
#include <sys/mman.h>   // for mmap, munmap
#include <unistd.h>     // for ::close

#include <cstdint>
#include <cstring>  // for memcpy
#include <filesystem>
#include <fstream>
#include <optional>
#include <tt-logger/tt-logger.hpp>
#include <vector>

#include "assert.hpp"
#include "ioctl.h"
#include "umd/device/types/arch.h"

static const uint16_t GS_PCIE_DEVICE_ID = 0xfaca;
static const uint16_t WH_PCIE_DEVICE_ID = 0x401e;
static const uint16_t BH_PCIE_DEVICE_ID = 0xb140;

static const size_t DMABUF_SIZE = (1 << 20);                   // 1 MiB
static const size_t DMABUF_TOTAL_SIZE = DMABUF_SIZE + 0x1000;  // Extra page for completion

// TODO: we'll have to rethink this when KMD takes control of the inbound PCIe
// TLB windows and there is no longer a pre-defined WC/UC split.
static const uint32_t GS_BAR0_WC_MAPPING_SIZE = (156 << 20) + (10 << 21) + (18 << 24);

// Defines the address for WC region. addresses 0 to BH_BAR0_WC_MAPPING_SIZE are in WC, above that are UC
static const uint32_t BH_BAR0_WC_MAPPING_SIZE = 188 << 21;

using namespace tt;
using namespace tt::umd;

template <typename T>
static std::optional<T> try_read_sysfs(const PciDeviceInfo &device_info, const std::string &attribute_name) {
    const auto sysfs_path = fmt::format(
        "/sys/bus/pci/devices/{:04x}:{:02x}:{:02x}.{:x}/{}",
        device_info.pci_domain,
        device_info.pci_bus,
        device_info.pci_device,
        device_info.pci_function,
        attribute_name);
    std::ifstream attribute_file(sysfs_path);
    std::string value_str;
    T value;

    if (!attribute_file.is_open() || !std::getline(attribute_file, value_str)) {
        return std::nullopt;
    }

    std::istringstream iss(value_str);

    // Handle hexadecimal input for integer types
    if constexpr (std::is_integral_v<T>) {
        if (value_str.substr(0, 2) == "0x") {
            iss >> std::hex;
        }
    }

    if (!(iss >> value)) {
        return std::nullopt;
    }

    return value;
}

template <typename T>
static T read_sysfs(const PciDeviceInfo &device_info, const std::string &attribute_name) {
    auto result = try_read_sysfs<T>(device_info, attribute_name);
    if (!result) {
        const auto sysfs_path = fmt::format(
            "/sys/bus/pci/devices/{:04x}:{:02x}:{:02x}.{:x}/{}",
            device_info.pci_domain,
            device_info.pci_bus,
            device_info.pci_device,
            device_info.pci_function,
            attribute_name);
        TT_THROW("Failed reading or parsing sysfs attribute: {}", sysfs_path);
    }
    return *result;
}

template <typename T>
T read_sysfs(const PciDeviceInfo &device_info, const std::string &attribute_name, const T &default_value) {
    auto result = try_read_sysfs<T>(device_info, attribute_name);
    return result.value_or(default_value);
}

static bool detect_iommu(const PciDeviceInfo &device_info) {
    auto iommu_type = try_read_sysfs<std::string>(device_info, "iommu_group/type");
    if (iommu_type) {
        return iommu_type->substr(0, 3) == "DMA";  // DMA or DMA-FQ
    }
    return false;
}

static PciDeviceInfo read_device_info(int fd) {
    tenstorrent_get_device_info info{};
    info.in.output_size_bytes = sizeof(info.out);

    if (ioctl(fd, TENSTORRENT_IOCTL_GET_DEVICE_INFO, &info) < 0) {
        TT_THROW("TENSTORRENT_IOCTL_GET_DEVICE_INFO failed");
    }

    uint16_t bus = info.out.bus_dev_fn >> 8;
    uint16_t dev = (info.out.bus_dev_fn >> 3) & 0x1F;
    uint16_t fn = info.out.bus_dev_fn & 0x07;

    return PciDeviceInfo{info.out.vendor_id, info.out.device_id, info.out.pci_domain, bus, dev, fn};
}

tt::ARCH PciDeviceInfo::get_arch() const {
    if (this->device_id == WH_PCIE_DEVICE_ID) {
        return tt::ARCH::WORMHOLE_B0;
    } else if (this->device_id == BH_PCIE_DEVICE_ID) {
        return tt::ARCH::BLACKHOLE;
    }
    return tt::ARCH::Invalid;
}

/* static */ std::vector<int> PCIDevice::enumerate_devices() {
    std::vector<int> device_ids;
    std::string path = "/dev/tenstorrent/";

    if (!std::filesystem::exists(path)) {
        return device_ids;
    }
    for (const auto &entry : std::filesystem::directory_iterator(path)) {
        std::string filename = entry.path().filename().string();

        // TODO: this will skip any device that has a non-numeric name, which
        // is probably what we want longer-term (i.e. a UUID or something).
        if (std::all_of(filename.begin(), filename.end(), ::isdigit)) {
            device_ids.push_back(std::stoi(filename));
        }
    }

    std::sort(device_ids.begin(), device_ids.end());
    return device_ids;
}

/* static */ std::map<int, PciDeviceInfo> PCIDevice::enumerate_devices_info() {
    std::map<int, PciDeviceInfo> infos;
    for (int n : PCIDevice::enumerate_devices()) {
        int fd = open(fmt::format("/dev/tenstorrent/{}", n).c_str(), O_RDWR | O_CLOEXEC);
        if (fd == -1) {
            continue;
        }

        try {
            infos[n] = read_device_info(fd);
        } catch (...) {
        }

        close(fd);
    }
    return infos;
}

static const semver_t kmd_ver_for_iommu = semver_t(1, 29, 0);

PCIDevice::PCIDevice(int pci_device_number) :
    device_path(fmt::format("/dev/tenstorrent/{}", pci_device_number)),
    pci_device_num(pci_device_number),
    pci_device_file_desc(open(device_path.c_str(), O_RDWR | O_CLOEXEC)),
    info(read_device_info(pci_device_file_desc)),
    numa_node(read_sysfs<int>(info, "numa_node", -1)),  // default to -1 if not found
    revision(read_sysfs<int>(info, "revision")),
    arch(info.get_arch()),
    kmd_version(PCIDevice::read_kmd_version()),
    iommu_enabled(detect_iommu(info)) {
    if (iommu_enabled && kmd_version < kmd_ver_for_iommu) {
        TT_THROW("Running with IOMMU support requires KMD version {} or newer", kmd_ver_for_iommu.to_string());
    }

    log_info(
        LogSiliconDriver,
        "Opened PCI device {}; KMD version: {}, IOMMU: {}",
        pci_device_num,
        kmd_version.to_string(),
        iommu_enabled ? "enabled" : "disabled");

    TT_ASSERT(arch != tt::ARCH::WORMHOLE_B0 || revision == 0x01, "Wormhole B0 must have revision 0x01");

    struct {
        tenstorrent_query_mappings query_mappings;
        tenstorrent_mapping mapping_array[8];
    } mappings;

    memset(&mappings, 0, sizeof(mappings));
    mappings.query_mappings.in.output_mapping_count = 8;

    if (ioctl(pci_device_file_desc, TENSTORRENT_IOCTL_QUERY_MAPPINGS, &mappings.query_mappings) == -1) {
        throw std::runtime_error(fmt::format("Query mappings failed on device {}.", pci_device_num));
    }

    // Mapping resource to BAR
    // Resource 0 -> BAR0
    // Resource 1 -> BAR2
    // Resource 2 -> BAR4
    tenstorrent_mapping bar0_uc_mapping{};
    tenstorrent_mapping bar0_wc_mapping{};
    tenstorrent_mapping bar2_uc_mapping{};
    tenstorrent_mapping bar2_wc_mapping{};
    tenstorrent_mapping bar4_uc_mapping{};
    tenstorrent_mapping bar4_wc_mapping{};

    for (unsigned int i = 0; i < mappings.query_mappings.in.output_mapping_count; i++) {
        if (mappings.mapping_array[i].mapping_id == TENSTORRENT_MAPPING_RESOURCE0_UC) {
            bar0_uc_mapping = mappings.mapping_array[i];
        }

        if (mappings.mapping_array[i].mapping_id == TENSTORRENT_MAPPING_RESOURCE0_WC) {
            bar0_wc_mapping = mappings.mapping_array[i];
        }

        if (mappings.mapping_array[i].mapping_id == TENSTORRENT_MAPPING_RESOURCE1_UC) {
            bar2_uc_mapping = mappings.mapping_array[i];
        }

        if (mappings.mapping_array[i].mapping_id == TENSTORRENT_MAPPING_RESOURCE1_WC) {
            bar2_wc_mapping = mappings.mapping_array[i];
        }

        if (mappings.mapping_array[i].mapping_id == TENSTORRENT_MAPPING_RESOURCE2_UC) {
            bar4_uc_mapping = mappings.mapping_array[i];
        }

        if (mappings.mapping_array[i].mapping_id == TENSTORRENT_MAPPING_RESOURCE2_WC) {
            bar4_wc_mapping = mappings.mapping_array[i];
        }

        log_debug(
            LogSiliconDriver,
            "BAR mapping id {} base {} size {}",
            mappings.mapping_array[i].mapping_id,
            (void *)mappings.mapping_array[i].mapping_base,
            mappings.mapping_array[i].mapping_size);
    }

    if (bar0_uc_mapping.mapping_id != TENSTORRENT_MAPPING_RESOURCE0_UC) {
        throw std::runtime_error(fmt::format("Device {} has no BAR0 UC mapping.", pci_device_num));
    }

    // TODO: Move arch specific code to tt_device.
    // wc_mapping_size along with some ifelses below.
    auto wc_mapping_size = arch == tt::ARCH::BLACKHOLE ? BH_BAR0_WC_MAPPING_SIZE : GS_BAR0_WC_MAPPING_SIZE;

    // Attempt WC mapping first so we can fall back to all-UC if it fails.
    if (bar0_wc_mapping.mapping_id == TENSTORRENT_MAPPING_RESOURCE0_WC) {
        bar0_wc_size = std::min<size_t>(bar0_wc_mapping.mapping_size, wc_mapping_size);
        bar0_wc = mmap(
            NULL, bar0_wc_size, PROT_READ | PROT_WRITE, MAP_SHARED, pci_device_file_desc, bar0_wc_mapping.mapping_base);
        if (bar0_wc == MAP_FAILED) {
            bar0_wc_size = 0;
            bar0_wc = nullptr;
        }
    }

    if (bar0_wc) {
        // The bottom part of the BAR is mapped WC. Map the top UC.
        bar0_uc_size = bar0_uc_mapping.mapping_size - wc_mapping_size;
        bar0_uc_offset = wc_mapping_size;
    } else {
        // No WC mapping, map the entire BAR UC.
        bar0_uc_size = bar0_uc_mapping.mapping_size;
        bar0_uc_offset = 0;
    }

    bar0_uc = mmap(
        NULL,
        bar0_uc_size,
        PROT_READ | PROT_WRITE,
        MAP_SHARED,
        pci_device_file_desc,
        bar0_uc_mapping.mapping_base + bar0_uc_offset);

    if (bar0_uc == MAP_FAILED) {
        throw std::runtime_error(fmt::format("BAR0 UC mapping failed for device {}.", pci_device_num));
    }

    if (!bar0_wc) {
        bar0_wc = bar0_uc;
    }

    if (arch == tt::ARCH::WORMHOLE_B0) {
        if (bar4_uc_mapping.mapping_id != TENSTORRENT_MAPPING_RESOURCE2_UC) {
            throw std::runtime_error(fmt::format("Device {} has no BAR4 UC mapping.", pci_device_num));
        }

        system_reg_mapping_size = bar4_uc_mapping.mapping_size;

        system_reg_mapping = mmap(
            NULL,
            bar4_uc_mapping.mapping_size,
            PROT_READ | PROT_WRITE,
            MAP_SHARED,
            pci_device_file_desc,
            bar4_uc_mapping.mapping_base);

        if (system_reg_mapping == MAP_FAILED) {
            throw std::runtime_error(fmt::format("BAR4 UC mapping failed for device {}.", pci_device_num));
        }

        system_reg_start_offset = (512 - 16) * 1024 * 1024;
        system_reg_offset_adjust = (512 - 32) * 1024 * 1024;

        bar2_uc_size = bar2_uc_mapping.mapping_size;
        bar2_uc = mmap(
            NULL,
            bar2_uc_mapping.mapping_size,
            PROT_READ | PROT_WRITE,
            MAP_SHARED,
            pci_device_file_desc,
            bar2_uc_mapping.mapping_base);

        if (bar2_uc == MAP_FAILED) {
            throw std::runtime_error(fmt::format("BAR2 UC mapping failed for device {}.", pci_device_num));
        }
    } else if (arch == tt::ARCH::BLACKHOLE) {
        if (bar2_uc_mapping.mapping_id != TENSTORRENT_MAPPING_RESOURCE1_UC) {
            throw std::runtime_error(fmt::format("Device {} has no BAR2 UC mapping.", pci_device_num));
        }

        // Using UnCachable memory mode. This is used for accessing registers on Blackhole.
        bar2_uc_size = bar2_uc_mapping.mapping_size;
        bar2_uc = mmap(
            NULL,
            bar2_uc_mapping.mapping_size,
            PROT_READ | PROT_WRITE,
            MAP_SHARED,
            pci_device_file_desc,
            bar2_uc_mapping.mapping_base);

        if (bar2_uc == MAP_FAILED) {
            throw std::runtime_error(fmt::format("BAR2 UC mapping failed for device {}.", pci_device_num));
        }

        if (bar4_wc_mapping.mapping_id != TENSTORRENT_MAPPING_RESOURCE2_WC) {
            throw std::runtime_error(fmt::format("Device {} has no BAR4 WC mapping.", pci_device_num));
        }

        // Using Write-Combine memory mode. This is used for accessing DRAM on Blackhole.
        // WC doesn't guarantee write ordering but has better performance.
        bar4_wc_size = bar4_wc_mapping.mapping_size;
        bar4_wc = mmap(
            NULL,
            bar4_wc_mapping.mapping_size,
            PROT_READ | PROT_WRITE,
            MAP_SHARED,
            pci_device_file_desc,
            bar4_wc_mapping.mapping_base);

        if (bar4_wc == MAP_FAILED) {
            throw std::runtime_error(fmt::format("BAR4 WC mapping failed for device {}.", pci_device_num));
        }
    }

    // DMA buffer setup.  This is different than the hugepage-based buffers that
    // are mapped to be accessible via the chip NOC.  This buffer is used by the
    // PCIe DMA engine for transferring data between device and host.  A few
    // things to note:
    // 1. This is Wormhole-only.
    // 2. Although the DMA engine could target the hugepages, the partitioning
    // scheme for the hugepages is mostly up to the application.  Requiring the
    // application to relinquish part of the hugepage memory and then coordinate
    // with us about it sounds like a terrible idea.
    // 3. Lack of current IOMMU support for Wormhole means that the buffer needs
    // to be small enough that Linux will have a reasonable chance of being able
    // to actually allocate it.
    // 4. Longer-term, we could move to an IOMMU-based scheme where:
    //    - Application allocates a buffer
    //    - Driver pins it and maps it for DMA
    //    - Application uses the buffer as an arena for DMA-able structures
    //    - Driver initiates DMAs based on its knowledge of the buffer
    // 5. + 0x1000 is for the completion page.  Since this entire implementation
    // is a temporary hack until it's implemented in the driver, we'll need to
    // poll a completion page to know when the DMA is done instead of receiving
    // an interrupt.
    if (arch == tt::ARCH::WORMHOLE_B0) {
        tenstorrent_allocate_dma_buf dma_buf{};

        dma_buf.in.requested_size = DMABUF_TOTAL_SIZE;
        dma_buf.in.buf_index = 0;

        if (ioctl(pci_device_file_desc, TENSTORRENT_IOCTL_ALLOCATE_DMA_BUF, &dma_buf)) {
            // There is a chance this will fail because we're not requiring
            // IOMMU.  Linux might not have a contiguous chunk of memory to give
            // us.  I'm not really sure what to do here.  PCIe DMA support is a
            // new feature in UMD and the application might not care about it,
            // so throwing our way out of here is wrong.  For now, we will log
            // here and throw when PCIe DMA is attempted.  Maybe a higher layer
            // in UMD can fall back to MMIO if that happens.
            log_error(LogSiliconDriver, "Failed to allocate DMA buffer: {}", strerror(errno));
        } else {
            // OK - we have a buffer.  Map it.
            void *buffer = mmap(
                nullptr,
                DMABUF_TOTAL_SIZE,
                PROT_READ | PROT_WRITE,
                MAP_SHARED,
                pci_device_file_desc,
                dma_buf.out.mapping_offset);

            if (buffer == MAP_FAILED) {
                // Similar rationale to above, although this is worse because we
                // can't deallocate it.  That only happens when we close the fd.
                log_error(LogSiliconDriver, "Failed to map DMA buffer: {}", strerror(errno));
            } else {
                dma_buffer.buffer = (uint8_t *)buffer;
                dma_buffer.completion = (uint8_t *)buffer + DMABUF_SIZE;
                dma_buffer.buffer_pa = dma_buf.out.physical_address;
                dma_buffer.completion_pa = dma_buf.out.physical_address + DMABUF_SIZE;
                dma_buffer.size = DMABUF_SIZE;
            }
        }
    }
}

PCIDevice::~PCIDevice() {
    close(pci_device_file_desc);

    if (bar0_wc != nullptr && bar0_wc != MAP_FAILED && bar0_wc != bar0_uc) {
        munmap(bar0_wc, bar0_wc_size);
    }

    if (bar0_uc != nullptr && bar0_uc != MAP_FAILED) {
        munmap(bar0_uc, bar0_uc_size);
    }

    if (bar2_uc != nullptr && bar2_uc != MAP_FAILED) {
        munmap(bar2_uc, bar2_uc_size);
    }

    if (bar4_wc != nullptr && bar4_wc != MAP_FAILED) {
        munmap(bar4_wc, bar4_wc_size);
    }

    if (system_reg_mapping != nullptr && system_reg_mapping != MAP_FAILED) {
        munmap(system_reg_mapping, system_reg_mapping_size);
    }

    if (dma_buffer.buffer != nullptr && dma_buffer.buffer != MAP_FAILED) {
        munmap(dma_buffer.buffer, DMABUF_TOTAL_SIZE);
    }
}

uint64_t PCIDevice::map_for_hugepage(void *buffer, size_t size) {
    tenstorrent_pin_pages pin_pages;
    memset(&pin_pages, 0, sizeof(pin_pages));
    pin_pages.in.output_size_bytes = sizeof(pin_pages.out);
    pin_pages.in.flags = TENSTORRENT_PIN_PAGES_CONTIGUOUS;
    pin_pages.in.virtual_address = reinterpret_cast<std::uintptr_t>(buffer);
    pin_pages.in.size = size;

    if (ioctl(pci_device_file_desc, TENSTORRENT_IOCTL_PIN_PAGES, &pin_pages) == -1) {
        return 0;
    }

    return pin_pages.out.physical_address;
}

uint64_t PCIDevice::map_for_dma(void *buffer, size_t size) {
    static const auto page_size = sysconf(_SC_PAGESIZE);

    const uint64_t vaddr = reinterpret_cast<uint64_t>(buffer);
    const uint32_t flags = is_iommu_enabled() ? 0 : TENSTORRENT_PIN_PAGES_CONTIGUOUS;

    if (vaddr % page_size != 0 || size % page_size != 0) {
        TT_THROW("Buffer must be page-aligned with a size that is a multiple of the page size");
    }

    tenstorrent_pin_pages pin_pages{};
    pin_pages.in.output_size_bytes = sizeof(pin_pages.out);
    pin_pages.in.flags = flags;
    pin_pages.in.virtual_address = vaddr;
    pin_pages.in.size = size;

    if (ioctl(pci_device_file_desc, TENSTORRENT_IOCTL_PIN_PAGES, &pin_pages) == -1) {
        TT_THROW("Failed to pin pages for DMA: {}", strerror(errno));
    }

    return pin_pages.out.physical_address;
}

void PCIDevice::unmap_for_dma(void *buffer, size_t size) {
    static const auto page_size = sysconf(_SC_PAGESIZE);

    const uint64_t vaddr = reinterpret_cast<uint64_t>(buffer);

    if (vaddr % page_size != 0 || size % page_size != 0) {
        TT_THROW("Buffer must be page-aligned with a size that is a multiple of the page size");
    }

    tenstorrent_unpin_pages unpin_pages{};
    unpin_pages.in.virtual_address = vaddr;
    unpin_pages.in.size = size;

    if (ioctl(pci_device_file_desc, TENSTORRENT_IOCTL_UNPIN_PAGES, &unpin_pages) < 0) {
        TT_THROW("Failed to unpin pages for DMA buffer: {}", strerror(errno));
    }
}

semver_t PCIDevice::read_kmd_version() {
    static const std::string path = "/sys/module/tenstorrent/version";
    std::ifstream file(path);

    if (!file.is_open()) {
        log_warning(LogSiliconDriver, "Failed to open file: {}", path);
        return {0, 0, 0};
    }

    std::string version_str;
    std::getline(file, version_str);

    return semver_t(version_str);
}

std::unique_ptr<TlbHandle> PCIDevice::allocate_tlb(const size_t tlb_size, const TlbMapping tlb_mapping) {
    return std::make_unique<TlbHandle>(pci_device_file_desc, tlb_size, tlb_mapping);
}

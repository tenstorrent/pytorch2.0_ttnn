/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#include "umd/device/tt_device/tlb_handle.h"

#include <sys/ioctl.h>
#include <sys/mman.h>

#include <stdexcept>
#include <tt-logger/tt-logger.hpp>

#include "ioctl.h"

namespace tt::umd {

TlbHandle::TlbHandle(uint32_t fd, size_t size, const TlbMapping tlb_mapping) :
    tlb_size(size), fd(fd), tlb_mapping(tlb_mapping) {
    tenstorrent_allocate_tlb allocate_tlb{};
    allocate_tlb.in.size = size;
    if (ioctl(fd, TENSTORRENT_IOCTL_ALLOCATE_TLB, &allocate_tlb) < 0) {
        throw std::runtime_error(fmt::format("Failed to allocate the TLB with size {}", size));
    }

    tlb_id = allocate_tlb.out.id;

    void* mapped_tlb =
        tlb_mapping == TlbMapping::UC
            ? mmap(nullptr, size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, allocate_tlb.out.mmap_offset_uc)
            : mmap(nullptr, size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, allocate_tlb.out.mmap_offset_wc);
    if (mapped_tlb == MAP_FAILED) {
        munmap(mapped_tlb, size);
        free_tlb();
        throw std::runtime_error("Failed to map the TLB.");
    }

    tlb_base = reinterpret_cast<uint8_t*>(mapped_tlb);
}

TlbHandle::~TlbHandle() noexcept {
    munmap(tlb_base, tlb_size);
    free_tlb();
}

void TlbHandle::configure(const tlb_data& new_config) {
    tenstorrent_configure_tlb configure_tlb{};
    configure_tlb.in.id = tlb_id;

    configure_tlb.in.config.addr = new_config.local_offset;
    configure_tlb.in.config.x_end = new_config.x_end;
    configure_tlb.in.config.y_end = new_config.y_end;
    configure_tlb.in.config.x_start = new_config.x_start;
    configure_tlb.in.config.y_start = new_config.y_start;
    configure_tlb.in.config.noc = new_config.noc_sel;
    configure_tlb.in.config.mcast = new_config.mcast;
    configure_tlb.in.config.ordering = new_config.ordering;
    configure_tlb.in.config.linked = new_config.linked;
    configure_tlb.in.config.static_vc = new_config.static_vc;

    if (std::memcmp(&new_config, &tlb_config, sizeof(new_config)) == 0) {
        return;
    }

    if (ioctl(fd, TENSTORRENT_IOCTL_CONFIGURE_TLB, &configure_tlb) < 0) {
        throw std::runtime_error(fmt::format("Failed to configure the TLB with id {}", tlb_id));
    }

    tlb_config = new_config;
}

uint8_t* TlbHandle::get_base() { return tlb_base; }

size_t TlbHandle::get_size() const { return tlb_size; }

const tlb_data& TlbHandle::get_config() const { return tlb_config; }

const TlbMapping TlbHandle::get_tlb_mapping() const { return tlb_mapping; }

void TlbHandle::free_tlb() noexcept {
    tenstorrent_free_tlb free_tlb{};
    free_tlb.in.id = tlb_id;
    if (ioctl(fd, TENSTORRENT_IOCTL_FREE_TLB, &free_tlb) < 0) {
        log_error(LogSiliconDriver, "Failed to free TLB with id {}", tlb_id);
    }
}

}  // namespace tt::umd

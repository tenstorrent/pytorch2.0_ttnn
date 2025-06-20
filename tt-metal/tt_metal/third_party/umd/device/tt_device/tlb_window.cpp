/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#include "umd/device/tt_device/tlb_window.h"

#include <stdexcept>

namespace tt::umd {

TlbWindow::TlbWindow(std::unique_ptr<TlbHandle> handle, const tlb_data config) : tlb_handle(std::move(handle)) {
    tlb_data aligned_config = config;
    aligned_config.local_offset = config.local_offset & ~(tlb_handle->get_size() - 1);
    tlb_handle->configure(aligned_config);
    offset_from_aligned_addr = config.local_offset - (config.local_offset & ~(tlb_handle->get_size() - 1));
}

void TlbWindow::write32(uint64_t offset, uint32_t value) {
    validate(offset, sizeof(uint32_t));
    *reinterpret_cast<volatile uint32_t*>(tlb_handle->get_base() + get_total_offset(offset)) = value;
}

uint32_t TlbWindow::read32(uint64_t offset) {
    validate(offset, sizeof(uint32_t));
    return *reinterpret_cast<volatile uint32_t*>(tlb_handle->get_base() + get_total_offset(offset));
}

void TlbWindow::write_register(uint64_t offset, uint32_t value) { write32(offset, value); }

uint32_t TlbWindow::read_register(uint64_t offset) { return read32(offset); }

void TlbWindow::write_block(uint64_t offset, const void* data, size_t size) {
    size_t n = size / sizeof(uint32_t);
    auto* src = static_cast<const uint32_t*>(data);
    auto* dst = reinterpret_cast<volatile uint32_t*>(tlb_handle->get_base() + get_total_offset(offset));

    validate(offset, size);

    for (size_t i = 0; i < n; i++) {
        dst[i] = src[i];
    }
}

void TlbWindow::read_block(uint64_t offset, void* data, size_t size) {
    size_t n = size / sizeof(uint32_t);
    auto* src = reinterpret_cast<const volatile uint32_t*>(tlb_handle->get_base() + get_total_offset(offset));
    auto* dst = static_cast<uint32_t*>(data);

    validate(offset, size);

    for (size_t i = 0; i < n; i++) {
        dst[i] = src[i];
    }
}

TlbHandle& TlbWindow::handle_ref() { return *tlb_handle; }

size_t TlbWindow::get_size() const { return tlb_handle->get_size() - offset_from_aligned_addr; }

// For simplicity and correctness, only allow 32-bit aligned accesses.
// There exist platform and device specific considerations for unaligned
// accesses which are not addressed here.
void TlbWindow::validate(uint64_t offset, size_t size) const {
    if ((offset + size) > get_size()) {
        throw std::out_of_range("Out of bounds access");
    }

    if (offset & (sizeof(uint32_t) - 1)) {
        throw std::runtime_error("Bad alignment");
    }
}

void TlbWindow::configure(const tlb_data& new_config) {
    tlb_data aligned_config = new_config;
    aligned_config.local_offset = new_config.local_offset & ~(tlb_handle->get_size() - 1);
    tlb_handle->configure(aligned_config);
    offset_from_aligned_addr = new_config.local_offset - (new_config.local_offset & ~(tlb_handle->get_size() - 1));
}

uint64_t TlbWindow::get_total_offset(uint64_t offset) const { return offset + offset_from_aligned_addr; }

}  // namespace tt::umd

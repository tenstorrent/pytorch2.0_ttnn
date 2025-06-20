/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#pragma once

#include <cstddef>
#include <cstdint>

#include "umd/device/types/tlb.h"

namespace tt::umd {

class TlbHandle {
public:
    /**
     * Constructor for TlbHandle.
     * Allocates a TLB from KMD of the specified size and maps it to the user space.
     *
     * @param fd File descriptor of the PCI device.
     * @param size Size of the TLB to allocate.
     * @param tlb_mapping Type of TLB mapping (UC or WC). The first mapping of TLB determines its caching behavior.
     */
    TlbHandle(uint32_t fd, size_t size, const TlbMapping tlb_mapping = TlbMapping::UC);

    ~TlbHandle() noexcept;

    /**
     * Configures the TLB with the provided configuration.
     *
     * @param new_config The new configuration for the TLB.
     */
    void configure(const tlb_data& new_config);

    /**
     * Returns the base mapped address of the TLB.
     */
    uint8_t* get_base();

    /**
     * Returns the size of the TLB.
     */
    size_t get_size() const;

    /**
     * Returns the current configuration of the TLB.
     */
    const tlb_data& get_config() const;

    /**
     * Returns the TLB mapping type (UC or WC).
     */
    const TlbMapping get_tlb_mapping() const;

private:
    void free_tlb() noexcept;

    int tlb_id;
    uint8_t* tlb_base;
    size_t tlb_size;
    tlb_data tlb_config;
    uint32_t fd;
    TlbMapping tlb_mapping;
};
}  // namespace tt::umd

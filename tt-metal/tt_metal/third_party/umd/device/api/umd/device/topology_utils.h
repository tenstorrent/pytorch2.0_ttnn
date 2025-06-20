/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include "umd/device/types/cluster_types.h"

namespace tt::umd {

template <typename T>
void size_buffer_to_capacity(std::vector<T>& data_buf, std::size_t size_in_bytes) {
    std::size_t target_size = 0;
    if (size_in_bytes > 0) {
        target_size = ((size_in_bytes - 1) / sizeof(T)) + 1;
    }
    data_buf.resize(target_size);
}

static inline uint64_t get_sys_addr(
    const tt_driver_noc_params& noc_params,
    uint32_t chip_x,
    uint32_t chip_y,
    uint32_t noc_x,
    uint32_t noc_y,
    uint64_t offset) {
    uint64_t result = chip_y;
    uint64_t noc_addr_local_bits_mask = (1UL << noc_params.noc_addr_local_bits) - 1;
    result <<= noc_params.noc_addr_node_id_bits;
    result |= chip_x;
    result <<= noc_params.noc_addr_node_id_bits;
    result |= noc_y;
    result <<= noc_params.noc_addr_node_id_bits;
    result |= noc_x;
    result <<= noc_params.noc_addr_local_bits;
    result |= (noc_addr_local_bits_mask & offset);
    return result;
}

static inline uint16_t get_sys_rack(
    const tt_driver_eth_interface_params& eth_interface_params, uint32_t rack_x, uint32_t rack_y) {
    uint32_t result = rack_y;
    result <<= eth_interface_params.eth_rack_coord_width;
    result |= rack_x;

    return result;
}

static inline bool is_non_mmio_cmd_q_full(
    const tt_driver_eth_interface_params& eth_interface_params, uint32_t curr_wptr, uint32_t curr_rptr) {
    return (curr_wptr != curr_rptr) && ((curr_wptr & eth_interface_params.cmd_buf_size_mask) ==
                                        (curr_rptr & eth_interface_params.cmd_buf_size_mask));
}

}  // namespace tt::umd

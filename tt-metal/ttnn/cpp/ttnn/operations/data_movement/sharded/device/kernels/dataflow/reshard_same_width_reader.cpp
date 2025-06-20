// SPDX-FileCopyrightText: © 2024 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0

#include <stdint.h>
#include "dataflow_api.h"

void kernel_main() {
    constexpr uint32_t shard_cb_id = get_compile_time_arg_val(0);
    constexpr bool read_from_dram = get_compile_time_arg_val(1);

    uint32_t src_addr = get_arg_val<uint32_t>(0);
    uint32_t write_offset = get_arg_val<uint32_t>(1);
    uint32_t num_reads = get_arg_val<uint32_t>(2);
    tt_l1_ptr uint32_t* args = (tt_l1_ptr uint32_t*)(get_arg_addr(3));
    uint32_t args_idx = 0;

    uint32_t l1_write_addr = get_write_ptr(shard_cb_id) + write_offset;
    for (uint32_t i = 0; i < num_reads; ++i) {
        uint32_t bank_id = args[args_idx++];
        uint32_t addr = src_addr + args[args_idx++];
        uint32_t read_size = args[args_idx++];
        noc_async_read(get_noc_addr_from_bank_id<read_from_dram>(bank_id, addr), l1_write_addr, read_size);
        l1_write_addr += read_size;
    }
    noc_async_read_barrier();
}

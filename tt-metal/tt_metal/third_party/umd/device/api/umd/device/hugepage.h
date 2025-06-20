/*
 * SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include <cstdint>
#include <string>

#include "umd/device/types/cluster_descriptor_types.h"

namespace tt::umd {

// Hugepages must be 1GB in size
const uint32_t HUGEPAGE_REGION_SIZE = 1 << 30;  // 1GB

// Get number of 1GB host hugepages installed.
uint32_t get_num_hugepages();

// Dynamically figure out how many host memory channels (based on hugepages installed) for each device, based on arch.
uint32_t get_available_num_host_mem_channels(
    const uint32_t num_channels_per_device_target, const uint16_t device_id, const uint16_t revision_id);

// Looks for hugetlbfs inside /proc/mounts matching desired pagesize (typically 1G)
std::string find_hugepage_dir(std::size_t pagesize);

// Open a file in <hugepage_dir> for the hugepage mapping.
// All processes operating on the same pipeline must agree on the file name.
// Today we assume there's only one pipeline running within the system.
// One hugepage per device such that each device gets unique memory.
int open_hugepage_file(const std::string &dir, chip_id_t physical_device_id, uint16_t channel);
}  // namespace tt::umd

// SPDX-FileCopyrightText: © 2024 Tenstorrent AI ULC
//
// SPDX-License-Identifier: Apache-2.0
#pragma once
#include <cstdint>
#include <stdint.h>

// Remove inline ASAP
inline namespace blackhole {

namespace host_mem {

struct address_map {

  static constexpr std::int32_t NUMBER_OF_CHANNELS = 4;
  // SYSMEM accessible via DEVICE-to-HOST MMIO
  static constexpr std::int32_t DEVICE_TO_HOST_MMIO_SIZE_BYTES    = 1024 * 1024 * 1024; // 1GB
  static constexpr std::int32_t DEVICE_TO_HOST_SCRATCH_SIZE_BYTES_PER_CHANNEL[4] = {128 * 1024 * 1024, 0, 0, 256 * 1024 * 1024};
  static constexpr std::int32_t DEVICE_TO_HOST_SCRATCH_START_PER_CHANNEL[4] = {DEVICE_TO_HOST_MMIO_SIZE_BYTES - DEVICE_TO_HOST_SCRATCH_SIZE_BYTES_PER_CHANNEL[0], 
                                                                              DEVICE_TO_HOST_MMIO_SIZE_BYTES - DEVICE_TO_HOST_SCRATCH_SIZE_BYTES_PER_CHANNEL[1],
                                                                              DEVICE_TO_HOST_MMIO_SIZE_BYTES - DEVICE_TO_HOST_SCRATCH_SIZE_BYTES_PER_CHANNEL[2], 
                                                                              DEVICE_TO_HOST_MMIO_SIZE_BYTES - DEVICE_TO_HOST_SCRATCH_SIZE_BYTES_PER_CHANNEL[3]};

  static constexpr std::int32_t DEVICE_TO_HOST_REGION_START       = 0;

  // Ethernet routing region params
  static constexpr std::int32_t ETH_ROUTING_BLOCK_SIZE = 32 * 1024;
  static constexpr std::int32_t ETH_ROUTING_BUFFERS_START = DEVICE_TO_HOST_SCRATCH_START_PER_CHANNEL[0]; // Implicit assumption: Eth buffers will be placed on host channel 0.
  static constexpr std::int32_t ETH_ROUTING_BUFFERS_SIZE = ETH_ROUTING_BLOCK_SIZE * 16 * 4;// 16 ethernet cores x 4 buffers/core

  // Concurrent perf trace region params
  static constexpr std::int32_t HOST_PERF_SCRATCH_BUF_START = DEVICE_TO_HOST_SCRATCH_START_PER_CHANNEL[0] + ETH_ROUTING_BUFFERS_SIZE; // Implicit assumption: Perf buffers will be placed on host channel 0.
  static constexpr std::int32_t HOST_PERF_SCRATCH_BUF_SIZE = 64 * 1024 * 1024;
  static constexpr std::int32_t NUM_THREADS_IN_EACH_DEVICE_DUMP = 1;
  static constexpr std::int32_t NUM_HOST_PERF_QUEUES = 6 * 64;
  static constexpr std::int32_t HOST_PERF_QUEUE_SLOT_SIZE = HOST_PERF_SCRATCH_BUF_SIZE / NUM_HOST_PERF_QUEUES / 32 * 32;  
  
  constexpr static std::int32_t ALLOCATABLE_QUEUE_REGION_START(std::int32_t channel) {
    // queue region starts at the base of host memory region
    return DEVICE_TO_HOST_REGION_START;
  }
  constexpr static std::int32_t ALLOCATABLE_QUEUE_REGION_END(const std::int32_t channel) {
    // queue region limited to the start of backend reserved scratch region
    return DEVICE_TO_HOST_REGION_START + DEVICE_TO_HOST_MMIO_SIZE_BYTES - DEVICE_TO_HOST_SCRATCH_SIZE_BYTES_PER_CHANNEL[channel];
  }
  constexpr static std::int32_t ALLOCATABLE_QUEUE_REGION_SIZE(const std::int32_t channel) {
    return ALLOCATABLE_QUEUE_REGION_END(channel) - ALLOCATABLE_QUEUE_REGION_START(channel);
  }
};
}
}


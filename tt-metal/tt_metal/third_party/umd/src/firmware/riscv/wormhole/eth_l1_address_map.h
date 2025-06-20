/*
 * SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include <stdint.h>

namespace eth_l1_mem {


struct address_map {
  // Sizes
  static constexpr std::int32_t FIRMWARE_SIZE = 32 * 1024;
  static constexpr std::int32_t ERISC_BARRIER_SIZE = 0x20; // 32 bytes reserved for Barrier
  static constexpr std::int32_t COMMAND_Q_SIZE = 4 * 1024;
  static constexpr std::int32_t DATA_BUFFER_SIZE_HOST = 4 * 1024;
  static constexpr std::int32_t DATA_BUFFER_SIZE_ETH = 4 * 1024;
  static constexpr std::int32_t DATA_BUFFER_SIZE_NOC = 16 * 1024;
  static constexpr std::int32_t DATA_BUFFER_SIZE = 24 * 1024;
  static constexpr std::int32_t EPOCH_RUNTIME_CONFIG_SIZE = 128;
  static constexpr std::int32_t OVERLAY_BLOB_SIZE = (32 * 1024) - EPOCH_RUNTIME_CONFIG_SIZE;
  static constexpr std::int32_t OVERLAY_MAX_EXTRA_BLOB_SIZE = (0 * 1024);
  static constexpr std::int32_t TILE_HEADER_BUF_SIZE = 32 * 1024;
  static constexpr std::int32_t NCRISC_L1_EPOCH_Q_SIZE = 32;
  static constexpr std::int32_t FW_L1_BLOCK_SIZE = OVERLAY_BLOB_SIZE + EPOCH_RUNTIME_CONFIG_SIZE + TILE_HEADER_BUF_SIZE;
  static constexpr std::int32_t FW_DRAM_BLOCK_SIZE = OVERLAY_BLOB_SIZE + OVERLAY_MAX_EXTRA_BLOB_SIZE + EPOCH_RUNTIME_CONFIG_SIZE + TILE_HEADER_BUF_SIZE;
  // Base addresses
  static constexpr std::int32_t FIRMWARE_BASE = 0x9040;
  static constexpr std::int32_t ERISC_BARRIER_BASE = 0x11FE0;
  static constexpr std::int32_t L1_EPOCH_Q_BASE = 0x9000; // Epoch Q start in L1.
  static constexpr std::int32_t L1_DRAM_POLLING_CTRL_BASE = 0x9020;
  static constexpr std::int32_t COMMAND_Q_BASE = L1_EPOCH_Q_BASE + FIRMWARE_SIZE;
  static constexpr std::int32_t DATA_BUFFER_BASE = COMMAND_Q_BASE + COMMAND_Q_SIZE;
  static constexpr std::int32_t TILE_HEADER_BUFFER_BASE = DATA_BUFFER_BASE + DATA_BUFFER_SIZE;
  static constexpr std::int32_t EPOCH_RUNTIME_CONFIG_BASE = TILE_HEADER_BUFFER_BASE + TILE_HEADER_BUF_SIZE;
  static constexpr std::int32_t OVERLAY_BLOB_BASE = EPOCH_RUNTIME_CONFIG_BASE + EPOCH_RUNTIME_CONFIG_SIZE;
  static constexpr std::int32_t DATA_BUFFER_SPACE_BASE = OVERLAY_BLOB_BASE + OVERLAY_BLOB_SIZE;

  static std::int32_t OVERLAY_FULL_BLOB_SIZE() {
      return OVERLAY_BLOB_SIZE + OVERLAY_MAX_EXTRA_BLOB_SIZE;
  };

template<std::size_t A, std::size_t B> struct TAssertEquality {
  static_assert(A==B, "Not equal");
  static constexpr bool _cResult = (A==B);
};

static constexpr bool _DATA_BUFFER_SPACE_BASE_CORRECT = TAssertEquality<DATA_BUFFER_SPACE_BASE, 0x28000>::_cResult;

  static constexpr std::int32_t MAX_SIZE = 256*1024;
  static constexpr std::int32_t MAX_L1_LOADING_SIZE = 1 * 256 * 1024;  
  
  static constexpr std::int32_t RISC_LOCAL_MEM_BASE = 0xffb00000; // Actaul local memory address as seen from risc firmware
                                                                   // As part of the init risc firmware will copy local memory data from
                                                                   // l1 locations listed above into internal local memory that starts 
                                                                   // at RISC_LOCAL_MEM_BASE address

  static constexpr std::uint32_t FW_VERSION_ADDR = 0x210;
};
}  // namespace llk

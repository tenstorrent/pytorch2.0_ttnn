/*
 * SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include <cstdint>

namespace tt::umd {

namespace blackhole {

// Note, this only includes message IDs that have actually be implemented in CMFW
enum class ArcMessageType : uint8_t {
    RESERVED_01 = 0x01,  // reserved to avoid conflict with initial SCRATCH[5] value
    NOP = 0x11,          // Do nothing
    SET_VOLTAGE = 0x12,
    GET_VOLTAGE = 0x13,
    SWITCH_CLK_SCHEME = 0x14,
    REPORT_SCRATCH_ONLY = 0x16,
    SEND_PCIE_MSI = 0x17,
    SWITCH_VOUT_CONTROL = 0x18,
    READ_EEPROM = 0x19,
    WRITE_EEPROM = 0x1A,
    READ_TS = 0x1B,
    READ_PD = 0x1C,
    READ_VM = 0x1D,
    I2C_MESSAGE = 0x1E,
    EFUSE_BURN_BITS = 0x1F,
    FORCE_AICLK = 0x33,
    FORCE_VDD = 0x39,
    AICLK_GO_BUSY = 0x52,
    AICLK_GO_LONG_IDLE = 0x54,
    TRIGGER_RESET = 0x56,  // arg: 3 = ASIC + M3 reset, other values = ASIC-only reset
    RESERVED_60 = 0x60,    // reserved to avoid conflict with boot-time SCRATCH[5] value
    TEST = 0x90,
    PCIE_DMA_CHIP_TO_HOST_TRANSFER = 0x9B,
    PCIE_DMA_HOST_TO_CHIP_TRANSFER = 0x9C,
    ASIC_STATE0 = 0xA0,
    ASIC_STATE1 = 0xA1,
    ASIC_STATE3 = 0xA3,
    ASIC_STATE5 = 0xA5,
    SET_LAST_SERIAL = 0xBE,
    EFUSE_BURN = 0xBF,
};

// Usage of queues proposed by Syseng.
enum BlackholeArcMessageQueueIndex : uint8_t {
    KMD = 0,
    MONITORING = 1,
    TOOLS = 2,
    APPLICATION = 3,
};

}  // namespace blackhole

}  // namespace tt::umd

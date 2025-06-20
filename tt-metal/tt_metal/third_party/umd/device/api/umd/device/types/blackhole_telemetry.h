/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

namespace tt::umd {

namespace blackhole {

constexpr uint8_t TAG_BOARD_ID_HIGH = 1;
constexpr uint8_t TAG_BOARD_ID_LOW = 2;
constexpr uint8_t TAG_ASIC_ID = 3;
constexpr uint8_t TAG_HARVESTING_STATE = 4;
constexpr uint8_t TAG_UPDATE_TELEM_SPEED = 5;
constexpr uint8_t TAG_VCORE = 6;
constexpr uint8_t TAG_TDP = 7;
constexpr uint8_t TAG_TDC = 8;
constexpr uint8_t TAG_VDD_LIMITS = 9;
constexpr uint8_t TAG_THM_LIMITS = 10;
constexpr uint8_t TAG_ASIC_TEMPERATURE = 11;
constexpr uint8_t TAG_VREG_TEMPERATURE = 12;
constexpr uint8_t TAG_BOARD_TEMPERATURE = 13;
constexpr uint8_t TAG_AICLK = 14;
constexpr uint8_t TAG_AXICLK = 15;
constexpr uint8_t TAG_ARCCLK = 16;
constexpr uint8_t TAG_L2CPUCLK0 = 17;
constexpr uint8_t TAG_L2CPUCLK1 = 18;
constexpr uint8_t TAG_L2CPUCLK2 = 19;
constexpr uint8_t TAG_L2CPUCLK3 = 20;
constexpr uint8_t TAG_ETH_LIVE_STATUS = 21;
constexpr uint8_t TAG_DDR_STATUS = 22;
constexpr uint8_t TAG_DDR_SPEED = 23;
constexpr uint8_t TAG_ETH_FW_VERSION = 24;
constexpr uint8_t TAG_DDR_FW_VERSION = 25;
constexpr uint8_t TAG_BM_APP_FW_VERSION = 26;
constexpr uint8_t TAG_BM_BL_FW_VERSION = 27;
constexpr uint8_t TAG_FLASH_BUNDLE_VERSION = 28;
constexpr uint8_t TAG_CM_FW_VERSION = 29;
constexpr uint8_t TAG_L2CPU_FW_VERSION = 30;
constexpr uint8_t TAG_FAN_SPEED = 31;
constexpr uint8_t TAG_TIMER_HEARTBEAT = 32;
constexpr uint8_t TAG_TELEM_ENUM_COUNT = 33;
constexpr uint8_t TAG_ENABLED_TENSIX_COL = 34;
constexpr uint8_t TAG_ENABLED_ETH = 35;
constexpr uint8_t TAG_ENABLED_GDDR = 36;
constexpr uint8_t TAG_ENABLED_L2CPU = 37;
constexpr uint8_t TAG_PCIE_USAGE = 38;

}  // namespace blackhole

}  // namespace tt::umd

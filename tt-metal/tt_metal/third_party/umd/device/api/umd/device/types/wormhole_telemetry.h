/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

namespace tt::umd {

namespace wormhole {

static const uint32_t TELEMETRY_NUMBER_OF_TAGS = 50;

constexpr uint8_t TAG_ENUM_VERSION = 0;
constexpr uint8_t TAG_DEVICE_ID = 1;
constexpr uint8_t TAG_ASIC_RO = 2;
constexpr uint8_t TAG_ASIC_IDD = 3;
constexpr uint8_t TAG_BOARD_ID_HIGH = 4;
constexpr uint8_t TAG_BOARD_ID_LOW = 5;
constexpr uint8_t TAG_ARC0_FW_VERSION = 6;
constexpr uint8_t TAG_ARC1_FW_VERSION = 7;
constexpr uint8_t TAG_ARC2_FW_VERSION = 8;
constexpr uint8_t TAG_ARC3_FW_VERSION = 9;
constexpr uint8_t TAG_SPIBOOTROM_FW_VERSION = 10;
constexpr uint8_t TAG_ETH_FW_VERSION = 11;
constexpr uint8_t TAG_M3_BL_FW_VERSION = 12;
constexpr uint8_t TAG_M3_APP_FW_VERSION = 13;
constexpr uint8_t TAG_DDR_STATUS = 14;
constexpr uint8_t TAG_ETH_STATUS0 = 15;
constexpr uint8_t TAG_ETH_STATUS1 = 16;
constexpr uint8_t TAG_PCIE_STATUS = 17;
constexpr uint8_t TAG_FAULTS = 18;
constexpr uint8_t TAG_ARC0_HEALTH = 19;
constexpr uint8_t TAG_ARC1_HEALTH = 20;
constexpr uint8_t TAG_ARC2_HEALTH = 21;
constexpr uint8_t TAG_ARC3_HEALTH = 22;
constexpr uint8_t TAG_FAN_SPEED = 23;
constexpr uint8_t TAG_AICLK = 24;
constexpr uint8_t TAG_AXICLK = 25;
constexpr uint8_t TAG_ARCCLK = 26;
constexpr uint8_t TAG_THROTTLER = 27;
constexpr uint8_t TAG_VCORE = 28;
constexpr uint8_t TAG_ASIC_TEMPERATURE = 29;
constexpr uint8_t TAG_VREG_TEMPERATURE = 30;
constexpr uint8_t TAG_BOARD_TEMPERATURE = 31;
constexpr uint8_t TAG_TDP = 32;
constexpr uint8_t TAG_TDC = 33;
constexpr uint8_t TAG_VDD_LIMITS = 34;
constexpr uint8_t TAG_THM_LIMITS = 35;
constexpr uint8_t TAG_WH_FW_DATE = 36;
constexpr uint8_t TAG_ASIC_TMON0 = 37;
constexpr uint8_t TAG_ASIC_TMON1 = 38;
constexpr uint8_t TAG_MVDDQ_POWER = 39;
constexpr uint8_t TAG_GDDR_TRAIN_TEMP0 = 40;
constexpr uint8_t TAG_GDDR_TRAIN_TEMP1 = 41;
constexpr uint8_t TAG_BOOT_DATE = 42;
constexpr uint8_t TAG_RT_SECONDS = 43;
constexpr uint8_t TAG_ETH_DEBUG_STATUS0 = 44;
constexpr uint8_t TAG_ETH_DEBUG_STATUS1 = 45;
constexpr uint8_t TAG_TT_FLASH_VERSION = 46;
constexpr uint8_t TAG_ETH_LOOPBACK_STATUS = 47;
constexpr uint8_t TAG_ETH_LIVE_STATUS = 48;
constexpr uint8_t TAG_FW_BUNDLE_VERSION = 49;

}  // namespace wormhole

}  // namespace tt::umd

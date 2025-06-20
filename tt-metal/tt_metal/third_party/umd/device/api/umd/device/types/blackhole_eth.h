/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include "umd/device/types/cluster_descriptor_types.h"

namespace tt::umd {

namespace blackhole {

static constexpr uint32_t POSTCODE_ETH_INIT_SKIP = 0xC0DE0000;
static constexpr uint32_t POSTCODE_ETH_INIT_SERDES = 0xC0DE1000;
static constexpr uint32_t POSTCODE_ETH_INIT_ETH_CTRL = 0xC0DE2000;
static constexpr uint32_t POSTCODE_ETH_INIT_MACPCS = 0xC0DE3000;
static constexpr uint32_t POSTCODE_ETH_INIT_PACKET = 0xC0DE4000;
static constexpr uint32_t POSTCODE_ETH_INIT_PASS = 0xC0DEA000;
static constexpr uint32_t POSTCODE_ETH_INIT_FAIL = 0xC0DEB000;
static constexpr uint32_t POSTCODE_ETH_INIT_CODE_NOT_FOUND = 0xC0DEFFFF;

static constexpr uint32_t NUM_SERDES_LANES = 8;

typedef enum {
    LINK_TRAIN_TRAINING,
    LINK_TRAIN_SKIP,
    LINK_TRAIN_PASS,
    LINK_TRAIN_INT_LB,
    LINK_TRAIN_EXT_LB,
    LINK_TRAIN_TIMEOUT_MANUAL_EQ,
    LINK_TRAIN_TIMEOUT_ANLT,
    LINK_TRAIN_TIMEOUT_CDR_LOCK,
    LINK_TRAIN_TIMEOUT_BIST_LOCK,
    LINK_TRAIN_TIMEOUT_LINK_UP,
    LINK_TRAIN_TIMEOUT_CHIP_INFO,
} link_train_status_e;

typedef enum {
    PORT_UNKNOWN,
    PORT_UP,
    PORT_DOWN,
    PORT_UNUSED,
} port_status_e;

struct fw_version_t {
    uint32_t patch : 8;
    uint32_t minor : 8;
    uint32_t major : 8;
    uint32_t unused : 8;
};

struct chip_info_t {
    uint8_t pcb_type;  // 0
    uint8_t asic_location;
    uint8_t eth_id;
    uint8_t logical_eth_id;
    uint32_t board_id_hi;   // 1
    uint32_t board_id_lo;   // 2
    uint32_t mac_addr_org;  // 3
    uint32_t mac_addr_id;   // 4
    uint32_t spare[2];      // 5-6
    uint32_t ack;           // 7

    ChipUID get_chip_uid() const {
        ChipUID chip_uid;
        chip_uid.board_id = ((uint64_t)board_id_hi << 32) | board_id_lo;
        chip_uid.asic_location = asic_location;
        return chip_uid;
    }
};

struct serdes_rx_bist_results_t {
    uint32_t bist_mode;  // 0
    uint32_t test_time;  // 1
    // test_time in cycles for bist mode 0 and ms for bist mode 1
    uint32_t error_cnt_nt[NUM_SERDES_LANES];           // 2-9
    uint32_t error_cnt_55t32_nt[NUM_SERDES_LANES];     // 10-17
    uint32_t error_cnt_overflow_nt[NUM_SERDES_LANES];  // 18-25
};

struct eth_status_t {
    // Basic status
    uint32_t postcode;                 // 0
    port_status_e port_status;         // 1
    link_train_status_e train_status;  // 2
    uint32_t train_speed;              // 3 - Actual resulting speed from training

    // Live status/retrain related
    uint32_t retrain_count;   // 4
    uint32_t mac_pcs_errors;  // 5
    uint32_t corr_dw_hi;      // 6
    uint32_t corr_dw_lo;      // 7
    uint32_t uncorr_dw_hi;    // 8
    uint32_t uncorr_dw_lo;    // 9
    uint32_t frames_rxd_hi;   // 10
    uint32_t frames_rxd_lo;   // 11
    uint32_t bytes_rxd_hi;    // 12
    uint32_t bytes_rxd_lo;    // 13

    uint32_t spare[28 - 14];  // 14-27

    // Heartbeat
    uint32_t heartbeat[4];  // 28-31
};

struct serdes_results_t {
    uint32_t postcode;           // 0
    uint32_t serdes_inst;        // 1
    uint32_t serdes_lane_mask;   // 2
    uint32_t target_speed;       // 3 - Target speed from the boot params
    uint32_t data_rate;          // 4
    uint32_t data_width;         // 5
    uint32_t spare_main[8 - 6];  // 6-7

    // Training retries
    uint32_t lt_retry_cnt;   // 8
    uint32_t spare[16 - 9];  // 9-15

    // BIST
    uint32_t bist_mode;       // 16
    uint32_t bist_test_time;  // 17
    // test_time in cycles for bist mode 0 and ms for bist mode 1
    uint32_t bist_err_cnt_nt[NUM_SERDES_LANES];           // 18-25
    uint32_t bist_err_cnt_55t32_nt[NUM_SERDES_LANES];     // 26-33
    uint32_t bist_err_cnt_overflow_nt[NUM_SERDES_LANES];  // 34-41

    uint32_t spare2[48 - 42];  // 42-47

    // Training times
    uint32_t man_eq_cmn_pstate_time;      // 48
    uint32_t man_eq_tx_ack_time;          // 49
    uint32_t man_eq_rx_ack_time;          // 50
    uint32_t man_eq_rx_iffsm_time;        // 51
    uint32_t man_eq_rx_eq_assert_time;    // 52
    uint32_t man_eq_rx_eq_deassert_time;  // 53
    uint32_t anlt_auto_neg_time;          // 54
    uint32_t anlt_link_train_time;        // 55
    uint32_t cdr_lock_time;               // 56
    uint32_t bist_lock_time;              // 57

    uint32_t spare_time[64 - 58];  // 58-63
};

struct macpcs_results_t {
    uint32_t postcode;  // 0

    uint32_t spare[24 - 1];  // 1-23

    // Training times
    uint32_t link_up_time;    // 24
    uint32_t chip_info_time;  // 25

    uint32_t spare_time[32 - 26];  // 26-31
};

struct boot_results_t {
    eth_status_t eth_status;          // 0-31
    serdes_results_t serdes_results;  // 32 - 95
    macpcs_results_t macpcs_results;  // 96 - 127

    uint32_t spare[238 - 128];  // 128 - 237

    fw_version_t serdes_fw_ver;  // 238
    fw_version_t eth_fw_ver;     // 239
    chip_info_t local_info;      // 240 - 247
    chip_info_t remote_info;     // 248 - 255
};

constexpr uint32_t BOOT_RESULTS_ADDR = 0x7CC00;

}  // namespace blackhole

}  // namespace tt::umd

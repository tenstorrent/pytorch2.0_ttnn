/*
 * SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include <array>

#include "architecture_implementation.h"
#include "umd/device/types/tlb.h"
#include "umd/device/umd_utils.h"

namespace tt::umd {

namespace wormhole {

// clang-format off
// See src/t6ifc/t6py/packages/tenstorrent/data/wormhole/pci/tlb.yaml
// local_offset: [ 0, 15,  0,  "36-bit address prefix, prepended to the 20 LSBs of issued address to form a 56-bit NOC address. The 1MB TLB #n corresponds to the 1MB MMIO range starting at (0x0 + N*0x100000)."]
// x_end       : [ 0, 21, 16,  "" ]
// y_end       : [ 0, 27, 22,  "" ]
// x_start     : [ 0, 33, 28,  "" ]
// y_start     : [ 0, 39, 34,  "" ]
// noc_sel:      [ 0, 40, 40,  "NOC select (1 = NOC1, 0 = NOC0)"]
// mcast:        [ 0, 41, 41,  "1 = multicast, 0 = unicast"]
// ordering:     [ 0, 43, 42,  "ordering mode (01 = strict (full AXI ordering), 00 = relaxed (no RAW hazard), 10 = posted (may have RAW hazard)"]
// linked:       [ 0, 44, 44,  "linked"]
// clang-format on
static constexpr auto TLB_1M_OFFSET = tlb_offsets{
    .local_offset = 0,
    .x_end = 16,
    .y_end = 22,
    .x_start = 28,
    .y_start = 34,
    .noc_sel = 40,
    .mcast = 41,
    .ordering = 42,
    .linked = 44,
    .static_vc = 45,
    .static_vc_end = 46};

// clang-format off
// local_offset: [ 0, 14,  0,  "35-bit address prefix, prepended to the 21 LSBs of issued address to form a 56-bit NOC address. The 2MB TLB #n corresponds to the 2MB MMIO range starting at (0x9C00000 + N*0x200000)."]
// x_end       : [ 0, 20, 15,  "" ]
// y_end       : [ 0, 26, 21,  "" ]
// x_start     : [ 0, 32, 27,  "" ]
// y_start     : [ 0, 38, 33,  "" ]
// noc_sel:      [ 0, 39, 39,  "NOC select (1 = NOC1, 0 = NOC0)"]
// mcast:        [ 0, 40, 40,  "1 = multicast, 0 = unicast"]
// ordering:     [ 0, 42, 41,  "ordering mode (01 = strict (full AXI ordering), 00 = relaxed (no RAW hazard), 10 = posted (may have RAW hazard)"]
// linked:       [ 0, 43, 43,  "linked"]
// clang-format on
static constexpr auto TLB_2M_OFFSET = tlb_offsets{
    .local_offset = 0,
    .x_end = 15,
    .y_end = 21,
    .x_start = 27,
    .y_start = 33,
    .noc_sel = 39,
    .mcast = 40,
    .ordering = 41,
    .linked = 43,
    .static_vc = 44,
    .static_vc_end = 45};

// clang-format off
// local_offset: [ 0, 11,  0,  "32-bit address prefix, prepended to the 24 LSBs of issued address to form a 56-bit NOC address. The 16MB TLB #n corresponds to the 16MB MMIO range starting at (0xB000000 + N*0x1000000)."]
// x_end       : [ 0, 17, 12,  "" ]
// y_end       : [ 0, 23, 18,  "" ]
// x_start     : [ 0, 29, 24,  "" ]
// y_start     : [ 0, 35, 30,  "" ]
// noc_sel:      [ 0, 36, 36,  "NOC select (1 = NOC1, 0 = NOC0)"]
// mcast:        [ 0, 37, 37,  "1 = multicast, 0 = unicast"]
// ordering:     [ 0, 39, 38,  "ordering mode (01 = strict (full AXI ordering), 00 = relaxed (no RAW hazard), 10 = posted (may have RAW hazard)"]
// linked:       [ 0, 40, 40,  "linked"]
// clang-format on
static constexpr auto TLB_16M_OFFSET = tlb_offsets{
    .local_offset = 0,
    .x_end = 12,
    .y_end = 18,
    .x_start = 24,
    .y_start = 30,
    .noc_sel = 36,
    .mcast = 37,
    .ordering = 38,
    .linked = 40,
    .static_vc = 41,
    .static_vc_end = 42};

enum class arc_message_type {
    NOP = 0x11,  // Do nothing
    GET_SMBUS_TELEMETRY_ADDR = 0x2C,
    GET_AICLK = 0x34,
    ARC_GO_BUSY = 0x52,
    ARC_GO_SHORT_IDLE = 0x53,
    ARC_GO_LONG_IDLE = 0x54,
    ARC_GET_HARVESTING = 0x57,
    SET_ETH_DRAM_TRAINED_STATUS = 0x58,
    TEST = 0x90,
    SETUP_IATU_FOR_PEER_TO_PEER = 0x97,
    DEASSERT_RISCV_RESET = 0xba
};

// DEVICE_DATA
static const tt_xy_pair GRID_SIZE = {10, 12};
// Vectors for mapping NOC0 x and y coordinates to NOC1 x and y coordinates.
// NOC0_X_TO_NOC1_X[noc0_x] is the NOC1 x coordinate corresponding to NOC0 x coordinate noc0_x.
// NOC0_Y_TO_NOC1_Y[noc0_y] is the NOC1 y coordinate corresponding to NOC0 y coordinate noc0_y.
static const std::vector<uint32_t> NOC0_X_TO_NOC1_X = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
static const std::vector<uint32_t> NOC0_Y_TO_NOC1_Y = {11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
static const tt_xy_pair TENSIX_GRID_SIZE = {8, 10};
// clang-format off
static const std::vector<tt_xy_pair> TENSIX_CORES_NOC0 = {
    {1, 1},   {2, 1},  {3, 1},  {4, 1},  {6, 1},  {7, 1},  {8, 1},  {9, 1},
    {1, 2},   {2, 2},  {3, 2},  {4, 2},  {6, 2},  {7, 2},  {8, 2},  {9, 2},
    {1, 3},   {2, 3},  {3, 3},  {4, 3},  {6, 3},  {7, 3},  {8, 3},  {9, 3},
    {1, 4},   {2, 4},  {3, 4},  {4, 4},  {6, 4},  {7, 4},  {8, 4},  {9, 4},
    {1, 5},   {2, 5},  {3, 5},  {4, 5},  {6, 5},  {7, 5},  {8, 5},  {9, 5},
    {1, 7},   {2, 7},  {3, 7},  {4, 7},  {6, 7},  {7, 7},  {8, 7},  {9, 7},
    {1, 8},   {2, 8},  {3, 8},  {4, 8},  {6, 8},  {7, 8},  {8, 8},  {9, 8},
    {1, 9},   {2, 9},  {3, 9},  {4, 9},  {6, 9},  {7, 9},  {8, 9},  {9, 9},
    {1, 10}, {2, 10}, {3, 10}, {4, 10}, {6, 10}, {7, 10}, {8, 10}, {9, 10},
    {1, 11}, {2, 11}, {3, 11}, {4, 11}, {6, 11}, {7, 11}, {8, 11}, {9, 11},
};
// clang-format on

static const std::size_t NUM_DRAM_BANKS = 6;
static const std::size_t NUM_NOC_PORTS_PER_DRAM_BANK = 3;
static const tt_xy_pair DRAM_GRID_SIZE = {NUM_DRAM_BANKS, NUM_NOC_PORTS_PER_DRAM_BANK};
// clang-format off
static const std::vector<std::vector<tt_xy_pair>> DRAM_CORES_NOC0 = {
    {{0, 0}, {0, 1}, {0, 11}},
    {{0, 5}, {0, 6},  {0, 7}},
    {{5, 0}, {5, 1}, {5, 11}},
    {{5, 2}, {5, 9}, {5, 10}},
    {{5, 3}, {5, 4},  {5, 8}},
    {{5, 5}, {5, 6},  {5, 7}}};
// clang-format on
// TODO: DRAM locations should be deleted. We keep it for compatibility with
// the existing code in clients which rely on DRAM_LOCATIONS.
static const std::vector<tt_xy_pair> DRAM_LOCATIONS = flatten_vector(DRAM_CORES_NOC0);

static const size_t NUM_ETH_CHANNELS = 16;
static const std::vector<tt_xy_pair> ETH_CORES_NOC0 = {
    {{9, 0},
     {1, 0},
     {8, 0},
     {2, 0},
     {7, 0},
     {3, 0},
     {6, 0},
     {4, 0},
     {9, 6},
     {1, 6},
     {8, 6},
     {2, 6},
     {7, 6},
     {3, 6},
     {6, 6},
     {4, 6}}};
static const std::vector<tt_xy_pair> ETH_LOCATIONS = ETH_CORES_NOC0;

static const tt_xy_pair ARC_GRID_SIZE = {1, 1};
static const std::vector<tt_xy_pair> ARC_CORES_NOC0 = {{0, 10}};
static const std::vector<tt_xy_pair> ARC_LOCATIONS = ARC_CORES_NOC0;

static const tt_xy_pair PCIE_GRID_SIZE = {1, 1};
static const std::vector<tt_xy_pair> PCIE_CORES_NOC0 = {{{0, 3}}};
static const std::vector<tt_xy_pair> PCI_LOCATIONS = PCIE_CORES_NOC0;

static const std::vector<tt_xy_pair> ROUTER_CORES_NOC0 = {{0, 2}, {0, 4}, {0, 8}, {0, 9}};

static const std::vector<tt_xy_pair> SECURITY_CORES_NOC0 = {};
static const std::vector<tt_xy_pair> L2CPU_CORES_NOC0 = {};

// Return to std::array instead of std::vector once we get std::span support in C++20
static const std::vector<uint32_t> T6_X_LOCATIONS = {1, 2, 3, 4, 6, 7, 8, 9};
static const std::vector<uint32_t> T6_Y_LOCATIONS = {1, 2, 3, 4, 5, 7, 8, 9, 10, 11};
static const std::vector<uint32_t> HARVESTING_NOC_LOCATIONS = {11, 1, 10, 2, 9, 3, 8, 4, 7, 5};
static const std::vector<uint32_t> LOGICAL_HARVESTING_LAYOUT = {1, 3, 5, 7, 9, 8, 6, 4, 2, 0};

static constexpr uint32_t STATIC_TLB_SIZE = 1024 * 1024;

static constexpr xy_pair BROADCAST_LOCATION = {0, 0};
static constexpr uint32_t BROADCAST_TLB_INDEX = 0;
static constexpr uint32_t STATIC_TLB_CFG_ADDR = 0x1fc00000;
static constexpr uint32_t TLB_CFG_REG_SIZE_BYTES = 8;

static constexpr uint32_t TLB_COUNT_1M = 156;
static constexpr uint32_t TLB_COUNT_2M = 10;
static constexpr uint32_t TLB_COUNT_16M = 20;

static constexpr uint32_t TLB_BASE_1M = 0;
static constexpr uint32_t TLB_BASE_2M = TLB_COUNT_1M * (1 << 20);
static constexpr uint32_t TLB_BASE_16M = TLB_BASE_2M + TLB_COUNT_2M * (1 << 21);

static constexpr uint32_t TLB_BASE_INDEX_1M = 0;
static constexpr uint32_t TLB_BASE_INDEX_2M = TLB_COUNT_1M;
static constexpr uint32_t TLB_BASE_INDEX_16M = TLB_BASE_INDEX_2M + TLB_COUNT_2M;

static constexpr uint32_t DYNAMIC_TLB_COUNT = 16;

static constexpr uint32_t DYNAMIC_TLB_16M_SIZE = 16 * 1024 * 1024;
static constexpr uint32_t DYNAMIC_TLB_16M_CFG_ADDR =
    STATIC_TLB_CFG_ADDR + (TLB_BASE_INDEX_16M * TLB_CFG_REG_SIZE_BYTES);
static constexpr uint32_t DYNAMIC_TLB_16M_BASE = TLB_BASE_16M;

static constexpr uint32_t DYNAMIC_TLB_2M_SIZE = 2 * 1024 * 1024;
static constexpr uint32_t DYNAMIC_TLB_2M_CFG_ADDR = STATIC_TLB_CFG_ADDR + (TLB_BASE_INDEX_2M * TLB_CFG_REG_SIZE_BYTES);
static constexpr uint32_t DYNAMIC_TLB_2M_BASE = TLB_BASE_2M;

static constexpr uint32_t DYNAMIC_TLB_1M_SIZE = 1 * 1024 * 1024;
static constexpr uint32_t DYNAMIC_TLB_1M_CFG_ADDR = STATIC_TLB_CFG_ADDR + (TLB_BASE_INDEX_1M * TLB_CFG_REG_SIZE_BYTES);
static constexpr uint32_t DYNAMIC_TLB_1M_BASE = TLB_BASE_1M;

// MEM_*_TLB are for dynamic read/writes to memory, either 16MB (large read/writes) or 2MB (polling). REG_TLB for
// dynamic writes to registers.   They are aligned with the kernel driver's WC/UC split.  But kernel driver uses
// different TLB's for these.
static constexpr unsigned int REG_TLB = TLB_BASE_INDEX_16M + 18;
static constexpr unsigned int MEM_LARGE_WRITE_TLB = TLB_BASE_INDEX_16M + 17;
static constexpr unsigned int MEM_LARGE_READ_TLB = TLB_BASE_INDEX_16M + 0;
static constexpr unsigned int MEM_SMALL_READ_WRITE_TLB = TLB_BASE_INDEX_2M + 1;
static constexpr uint32_t DYNAMIC_TLB_BASE_INDEX = MEM_LARGE_READ_TLB + 1;
static constexpr uint32_t INTERNAL_TLB_INDEX = DYNAMIC_TLB_BASE_INDEX + DYNAMIC_TLB_COUNT;  // pcie_write_xy and similar
static constexpr uint32_t DRAM_CHANNEL_0_X = 0;
static constexpr uint32_t DRAM_CHANNEL_0_Y = 0;
static constexpr uint32_t DRAM_CHANNEL_0_PEER2PEER_REGION_START = 0x30000000;  // This is the last 256MB of DRAM

static constexpr uint32_t GRID_SIZE_X = 10;
static constexpr uint32_t GRID_SIZE_Y = 12;

static constexpr uint32_t ARC_MSG_COMMON_PREFIX = 0xAA00;

static constexpr uint32_t ARC_RESET_SCRATCH_OFFSET = 0x1FF30060;
static constexpr uint32_t ARC_RESET_ARC_MISC_CNTL_OFFSET = 0x1FF30100;

static constexpr uint32_t ARC_CSM_MAILBOX_OFFSET = 0x1FEF83C4;
static constexpr uint32_t ARC_CSM_MAILBOX_SIZE_OFFSET = 0x1FEF84C4;

static constexpr uint32_t TENSIX_SOFT_RESET_ADDR = 0xFFB121B0;

static constexpr uint32_t ARC_SCRATCH_6_OFFSET = 0x1FF30078;

static constexpr uint32_t ARC_SCRATCH_RES0_OFFSET = 3;
static constexpr uint32_t ARC_SCRATCH_RES1_OFFSET = 4;
static constexpr uint32_t ARC_SCRATCH_STATUS_OFFSET = 5;

constexpr uint64_t ARC_RESET_SCRATCH_ADDR = 0x880030060;
constexpr uint64_t ARC_RESET_MISC_CNTL_ADDR = 0x880030100;

static constexpr uint32_t AICLK_BUSY_VAL = 1000;
static constexpr uint32_t AICLK_IDLE_VAL = 500;

static constexpr uint32_t TENSIX_L1_SIZE = 1499136;
static constexpr uint32_t ETH_L1_SIZE = 262144;
static constexpr uint64_t DRAM_BANK_SIZE = 2147483648;

constexpr std::array<std::pair<CoreType, uint64_t>, 5> NOC0_CONTROL_REG_ADDR_BASE_MAP = {
    {{CoreType::TENSIX, 0xFFB20000},
     {CoreType::ETH, 0xFFB20000},
     {CoreType::DRAM, 0x100080000},
     {CoreType::PCIE, 0xFFFB20000},
     {CoreType::ARC, 0xFFFB20000}}};
constexpr std::array<std::pair<CoreType, uint64_t>, 5> NOC1_CONTROL_REG_ADDR_BASE_MAP = {
    {{CoreType::TENSIX, 0xFFB30000},
     {CoreType::ETH, 0xFFB30000},
     {CoreType::DRAM, 0x100088000},
     {CoreType::PCIE, 0xFFFB30000},
     {CoreType::ARC, 0xFFFB30000}}};
static const uint64_t NOC_NODE_ID_OFFSET = 0x2C;

static const size_t tensix_translated_coordinate_start_x = 18;
static const size_t tensix_translated_coordinate_start_y = 18;

static const size_t eth_translated_coordinate_start_x = 18;
static const size_t eth_translated_coordinate_start_y = 16;

}  // namespace wormhole

class wormhole_implementation : public architecture_implementation {
public:
    tt::ARCH get_architecture() const override { return tt::ARCH::WORMHOLE_B0; }

    uint32_t get_arc_message_arc_get_harvesting() const override {
        return static_cast<uint32_t>(wormhole::arc_message_type::ARC_GET_HARVESTING);
    }

    uint32_t get_arc_message_arc_go_busy() const override {
        return static_cast<uint32_t>(wormhole::arc_message_type::ARC_GO_BUSY);
    }

    uint32_t get_arc_message_arc_go_long_idle() const override {
        return static_cast<uint32_t>(wormhole::arc_message_type::ARC_GO_LONG_IDLE);
    }

    uint32_t get_arc_message_arc_go_short_idle() const override {
        return static_cast<uint32_t>(wormhole::arc_message_type::ARC_GO_SHORT_IDLE);
    }

    uint32_t get_arc_message_deassert_riscv_reset() const override {
        return static_cast<uint32_t>(wormhole::arc_message_type::DEASSERT_RISCV_RESET);
    }

    uint32_t get_arc_message_get_aiclk() const override {
        return static_cast<uint32_t>(wormhole::arc_message_type::GET_AICLK);
    }

    uint32_t get_arc_message_setup_iatu_for_peer_to_peer() const override {
        return static_cast<uint32_t>(wormhole::arc_message_type::SETUP_IATU_FOR_PEER_TO_PEER);
    }

    uint32_t get_arc_message_test() const override { return static_cast<uint32_t>(wormhole::arc_message_type::TEST); }

    uint32_t get_arc_csm_mailbox_offset() const override { return wormhole::ARC_CSM_MAILBOX_OFFSET; }

    uint32_t get_arc_reset_arc_misc_cntl_offset() const override { return wormhole::ARC_RESET_ARC_MISC_CNTL_OFFSET; }

    uint32_t get_arc_reset_scratch_offset() const override { return wormhole::ARC_RESET_SCRATCH_OFFSET; }

    uint32_t get_dram_channel_0_peer2peer_region_start() const override {
        return wormhole::DRAM_CHANNEL_0_PEER2PEER_REGION_START;
    }

    uint32_t get_dram_channel_0_x() const override { return wormhole::DRAM_CHANNEL_0_X; }

    uint32_t get_dram_channel_0_y() const override { return wormhole::DRAM_CHANNEL_0_Y; }

    uint32_t get_broadcast_tlb_index() const override { return wormhole::BROADCAST_TLB_INDEX; }

    uint32_t get_dynamic_tlb_2m_base() const override { return wormhole::DYNAMIC_TLB_2M_BASE; }

    uint32_t get_dynamic_tlb_2m_size() const override { return wormhole::DYNAMIC_TLB_2M_SIZE; }

    uint32_t get_dynamic_tlb_16m_base() const override { return wormhole::DYNAMIC_TLB_16M_BASE; }

    uint32_t get_dynamic_tlb_16m_size() const override { return wormhole::DYNAMIC_TLB_16M_SIZE; }

    uint32_t get_dynamic_tlb_16m_cfg_addr() const override { return wormhole::DYNAMIC_TLB_16M_CFG_ADDR; }

    uint32_t get_mem_large_read_tlb() const override { return wormhole::MEM_LARGE_READ_TLB; }

    uint32_t get_mem_large_write_tlb() const override { return wormhole::MEM_LARGE_WRITE_TLB; }

    uint32_t get_num_eth_channels() const override { return wormhole::NUM_ETH_CHANNELS; }

    uint32_t get_static_tlb_cfg_addr() const override { return wormhole::STATIC_TLB_CFG_ADDR; }

    uint32_t get_read_checking_offset() const override { return wormhole::ARC_SCRATCH_6_OFFSET; }

    uint32_t get_static_tlb_size() const override { return wormhole::STATIC_TLB_SIZE; }

    uint32_t get_reg_tlb() const override { return wormhole::REG_TLB; }

    uint32_t get_tlb_base_index_16m() const override { return wormhole::TLB_BASE_INDEX_16M; }

    uint32_t get_tensix_soft_reset_addr() const override { return wormhole::TENSIX_SOFT_RESET_ADDR; }

    uint32_t get_grid_size_x() const override { return wormhole::GRID_SIZE_X; }

    uint32_t get_grid_size_y() const override { return wormhole::GRID_SIZE_Y; }

    uint32_t get_tlb_cfg_reg_size_bytes() const override { return wormhole::TLB_CFG_REG_SIZE_BYTES; }

    uint32_t get_small_read_write_tlb() const override { return wormhole::MEM_SMALL_READ_WRITE_TLB; }

    const std::vector<uint32_t>& get_harvesting_noc_locations() const override {
        return wormhole::HARVESTING_NOC_LOCATIONS;
    }

    const std::vector<uint32_t>& get_t6_x_locations() const override { return wormhole::T6_X_LOCATIONS; }

    const std::vector<uint32_t>& get_t6_y_locations() const override { return wormhole::T6_Y_LOCATIONS; }

    std::pair<uint32_t, uint32_t> get_tlb_1m_base_and_count() const override {
        return {wormhole::TLB_BASE_1M, wormhole::TLB_COUNT_1M};
    }

    std::pair<uint32_t, uint32_t> get_tlb_2m_base_and_count() const override {
        return {wormhole::TLB_BASE_2M, wormhole::TLB_COUNT_2M};
    }

    std::pair<uint32_t, uint32_t> get_tlb_16m_base_and_count() const override {
        return {wormhole::TLB_BASE_16M, wormhole::TLB_COUNT_16M};
    }

    std::pair<uint32_t, uint32_t> get_tlb_4g_base_and_count() const override { return {0, 0}; }

    std::tuple<xy_pair, xy_pair> multicast_workaround(xy_pair start, xy_pair end) const override;
    tlb_configuration get_tlb_configuration(uint32_t tlb_index) const override;

    tt_device_l1_address_params get_l1_address_params() const override;
    tt_driver_host_address_params get_host_address_params() const override;
    tt_driver_eth_interface_params get_eth_interface_params() const override;
    tt_driver_noc_params get_noc_params() const override;

    virtual uint64_t get_noc_node_id_offset() const override { return wormhole::NOC_NODE_ID_OFFSET; }

    uint64_t get_noc_reg_base(const CoreType core_type, const uint32_t noc, const uint32_t noc_port = 0) const override;
};

}  // namespace tt::umd

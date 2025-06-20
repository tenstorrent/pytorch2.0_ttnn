/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#pragma once

#include "umd/device/chip/chip.h"
#include "umd/device/tt_device/tt_device.h"

class tt_ClusterDescriptor;

// Currently we need this to uniquely identify a chip.
// Once we can also extract asic_location, then board_id + asic_location should be a unique identifier for all chips.
// This structure is used only during topology discovery to do it properly.
struct UniqueCoord {
    uint64_t board_id;
    eth_coord_t eth_coord;

    bool operator==(const UniqueCoord& other) const {
        return board_id == other.board_id && eth_coord == other.eth_coord;
    }
};

// Make it hashable so it can be a key in a hashmap
namespace std {
template <>
struct hash<UniqueCoord> {
    std::size_t operator()(UniqueCoord const& c) const {
        std::size_t seed = 0;
        boost_hash_combine(seed, c.board_id);
        boost_hash_combine(seed, hash<eth_coord_t>()(c.eth_coord));
        return seed;
    }
};

}  // namespace std

namespace tt::umd {

// TopologyDiscovery class creates cluster descriptor only for Wormhole configurations with old routing fw.
// TODO: Move Blackhole and 6U topology discovery to this class.
class TopologyDiscovery {
public:
    TopologyDiscovery(std::unordered_set<chip_id_t> pci_target_devices = {});
    std::unique_ptr<tt_ClusterDescriptor> create_ethernet_map();

private:
    struct EthAddresses {
        uint32_t masked_version;

        uint64_t version;
        uint64_t boot_params;
        uint64_t node_info;
        uint64_t eth_conn_info;
        uint64_t debug_buf;
        uint64_t results_buf;
        bool shelf_rack_routing;
        uint64_t heartbeat;
        uint64_t erisc_app;
        uint64_t erisc_app_config;
        uint64_t erisc_remote_board_type_offset;
        uint64_t erisc_local_board_type_offset;
        uint64_t erisc_local_board_id_lo_offset;
        uint64_t erisc_remote_board_id_lo_offset;
    };

    static EthAddresses get_eth_addresses(uint32_t eth_fw_version);

    void get_pcie_connected_chips();

    void discover_remote_chips();

    void fill_cluster_descriptor_info();

    bool is_pcie_chip_id_included(int pci_id) const;

    bool is_board_id_included(uint32_t board_id) const;

    // Returns mangled remote board id from local ETH core.
    // This information can still be used to unique identify a board.
    uint32_t get_remote_board_id(Chip* chip, tt_xy_pair eth_core);

    // Returns mangled local board id from local ETH core.
    // This information can still be used to unique identify a board.
    uint32_t get_local_board_id(Chip* chip, tt_xy_pair eth_core);

    std::unordered_map<chip_id_t, std::unique_ptr<Chip>> chips;

    std::unordered_map<UniqueCoord, chip_id_t> unique_coord_to_chip_id;

    std::unordered_map<chip_id_t, eth_coord_t> eth_coords;

    std::vector<std::pair<std::pair<chip_id_t, uint32_t>, std::pair<chip_id_t, uint32_t>>> ethernet_connections;

    std::unique_ptr<tt_ClusterDescriptor> cluster_desc;

    chip_id_t chip_id = 0;

    EthAddresses eth_addresses;

    std::unordered_set<chip_id_t> pci_target_devices = {};

    // All board ids that should be included in the cluster descriptor.
    std::unordered_set<uint32_t> board_ids;
};

}  // namespace tt::umd

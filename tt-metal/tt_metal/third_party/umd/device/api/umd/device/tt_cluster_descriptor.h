/*
 * SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include <cstdint>
#include <filesystem>
#include <map>
#include <memory>
#include <set>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#include "umd/device/chip/chip.h"
#include "umd/device/topology_discovery.h"
#include "umd/device/tt_xy_pair.h"
#include "umd/device/types/arch.h"
#include "umd/device/types/cluster_descriptor_types.h"

namespace YAML {
class Node;
}

namespace tt::umd {
class Cluster;
}

class tt_ClusterDescriptor {
    friend class tt::umd::Cluster;
    friend class tt::umd::TopologyDiscovery;

private:
    tt_ClusterDescriptor() = default;

    int get_ethernet_link_coord_distance(const eth_coord_t &location_a, const eth_coord_t &location_b) const;

protected:
    std::unordered_map<chip_id_t, std::unordered_map<ethernet_channel_t, std::tuple<chip_id_t, ethernet_channel_t>>>
        ethernet_connections;
    // TODO: unify uint64_t with ChipUID
    std::unordered_map<chip_id_t, std::unordered_map<ethernet_channel_t, std::tuple<uint64_t, ethernet_channel_t>>>
        ethernet_connections_to_remote_mmio_devices;
    std::unordered_map<chip_id_t, eth_coord_t> chip_locations;
    // reverse map: rack/shelf/y/x -> chip_id
    std::map<int, std::map<int, std::map<int, std::map<int, chip_id_t>>>> coords_to_chip_ids;
    std::unordered_map<chip_id_t, chip_id_t> chips_with_mmio;
    std::unordered_set<chip_id_t> all_chips;
    std::unordered_map<chip_id_t, bool> noc_translation_enabled = {};
    std::unordered_map<chip_id_t, std::uint32_t> harvesting_masks = {};
    std::unordered_map<chip_id_t, chip_id_t> closest_mmio_chip_cache = {};
    std::unordered_map<chip_id_t, BoardType> chip_board_type = {};
    std::unordered_map<chip_id_t, std::unordered_set<chip_id_t>> chips_grouped_by_closest_mmio;
    std::unordered_map<chip_id_t, tt::ARCH> chip_arch = {};
    std::map<ChipUID, chip_id_t> chip_uid_to_chip_id = {};
    std::map<chip_id_t, ChipUID> chip_id_to_chip_uid = {};
    std::unordered_map<chip_id_t, uint64_t> chip_unique_ids = {};
    std::map<chip_id_t, std::set<uint32_t>> active_eth_channels = {};
    std::map<chip_id_t, std::set<uint32_t>> idle_eth_channels = {};
    std::map<uint64_t, std::unordered_set<chip_id_t>> board_to_chips = {};
    std::unordered_map<chip_id_t, uint64_t> chip_to_board_id = {};

    // one-to-many chip connections
    struct Chip2ChipConnection {
        eth_coord_t source_chip_coord;
        std::unordered_set<eth_coord_t> destination_chip_coords;
    };

    // shelf_id -> y dim -> list of chip2chip connections between different shelves
    // assumption is that on every row of the shelf there is a chip that is connected to the other shelf
    // there could be one-to-many connections between shelves, i.e. one chip is connected to multiple chips on the other
    // shelf (in case of nebula->galaxy)
    std::unordered_map<int, std::unordered_map<int, Chip2ChipConnection>> galaxy_shelves_exit_chip_coords_per_y_dim =
        {};
    // rack_id -> x dim -> list of chip2chip connections between different racks
    // assumption is that on every row of the rack there is a chip that is connected to the other rack
    std::unordered_map<int, std::unordered_map<int, Chip2ChipConnection>> galaxy_racks_exit_chip_coords_per_x_dim = {};

    static void load_ethernet_connections_from_connectivity_descriptor(YAML::Node &yaml, tt_ClusterDescriptor &desc);
    static void fill_galaxy_connections(tt_ClusterDescriptor &desc);
    static void load_chips_from_connectivity_descriptor(YAML::Node &yaml, tt_ClusterDescriptor &desc);
    static void merge_cluster_ids(tt_ClusterDescriptor &desc);
    static void load_harvesting_information(YAML::Node &yaml, tt_ClusterDescriptor &desc);

    void add_chip_to_board(chip_id_t chip_id, uint64_t board_id);

    void fill_chips_grouped_by_closest_mmio();

    std::map<chip_id_t, uint32_t> dram_harvesting_masks = {};
    std::map<chip_id_t, uint32_t> eth_harvesting_masks = {};
    std::map<chip_id_t, uint32_t> pcie_harvesting_masks = {};

public:
    /*
     * Returns the pairs of channels that are connected where the first entry in the pair corresponds to the argument
     * ordering when calling the function An empty result implies that the two chips do not share any direct connection
     */
    std::vector<std::tuple<ethernet_channel_t, ethernet_channel_t>>
    get_directly_connected_ethernet_channels_between_chips(const chip_id_t &first, const chip_id_t &second) const;

    bool is_chip_mmio_capable(const chip_id_t chip_id) const;
    bool is_chip_remote(const chip_id_t chip_id) const;
    chip_id_t get_closest_mmio_capable_chip(const chip_id_t chip);
    chip_id_t get_shelf_local_physical_chip_coords(chip_id_t virtual_coord);

    static std::unique_ptr<tt_ClusterDescriptor> create_from_yaml(const std::string &cluster_descriptor_file_path);

    // This function is used to create mock cluster descriptor yaml files, for example for simulation.
    static std::unique_ptr<tt_ClusterDescriptor> create_mock_cluster(
        const std::vector<chip_id_t> &logical_device_ids, tt::ARCH arch);
    // Used to create a subset of a cluster descriptor.
    static std::unique_ptr<tt_ClusterDescriptor> create_constrained_cluster_descriptor(
        const tt_ClusterDescriptor *full_cluster_desc, const std::unordered_set<chip_id_t> &target_chip_ids);

    const std::unordered_map<chip_id_t, std::uint32_t> &get_harvesting_info() const;
    const std::unordered_map<chip_id_t, bool> &get_noc_translation_table_en() const;
    const std::unordered_map<chip_id_t, eth_coord_t> &get_chip_locations() const;
    const std::unordered_map<chip_id_t, uint64_t> &get_chip_unique_ids() const;
    const std::
        unordered_map<chip_id_t, std::unordered_map<ethernet_channel_t, std::tuple<chip_id_t, ethernet_channel_t>>> &
        get_ethernet_connections() const;
    // TODO: unify uint64_t with ChipUID
    const std::
        unordered_map<chip_id_t, std::unordered_map<ethernet_channel_t, std::tuple<uint64_t, ethernet_channel_t>>>
        get_ethernet_connections_to_remote_mmio_devices() const;
    const std::unordered_map<chip_id_t, chip_id_t> &get_chips_with_mmio() const;
    const std::unordered_set<chip_id_t> &get_all_chips() const;
    const std::vector<chip_id_t> get_chips_local_first(std::unordered_set<chip_id_t> chips) const;
    const std::unordered_map<chip_id_t, std::unordered_set<chip_id_t>> &get_chips_grouped_by_closest_mmio() const;
    std::size_t get_number_of_chips() const;

    int get_ethernet_link_distance(chip_id_t chip_a, chip_id_t chip_b) const;

    BoardType get_board_type(chip_id_t chip_id) const;
    std::unordered_set<chip_id_t> get_board_chips(const uint64_t board_id) const;
    uint64_t get_board_id_for_chip(const chip_id_t chip) const;
    tt::ARCH get_arch(chip_id_t chip_id) const;

    void add_chip_uid(const chip_id_t chip_id, const ChipUID &chip_uid);
    std::optional<chip_id_t> get_chip_id(const ChipUID &chip_uid) const;
    std::optional<ChipUID> get_chip_uid(chip_id_t chip_id) const;

    bool ethernet_core_has_active_ethernet_link(chip_id_t local_chip, ethernet_channel_t local_ethernet_channel) const;
    std::tuple<chip_id_t, ethernet_channel_t> get_chip_and_channel_of_remote_ethernet_core(
        chip_id_t local_chip, ethernet_channel_t local_ethernet_channel) const;

    // Serialize the cluster descriptor to a YAML string, or directly to a file.
    // A default file in /tmp directory will be used if no path is passed.
    std::string serialize() const;
    std::filesystem::path serialize_to_file(const std::filesystem::path &dest_file = "") const;
    static std::filesystem::path get_default_cluster_descriptor_file_path();

    std::set<uint32_t> get_active_eth_channels(chip_id_t chip_id);
    std::set<uint32_t> get_idle_eth_channels(chip_id_t chip_id);

    uint32_t get_dram_harvesting_mask(chip_id_t chip_id) const;
    uint32_t get_eth_harvesting_mask(chip_id_t chip_id) const;
    uint32_t get_pcie_harvesting_mask(chip_id_t chip_id) const;
};

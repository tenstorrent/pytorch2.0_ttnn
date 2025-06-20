// SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0

#include "umd/device/tt_cluster_descriptor.h"

#include <fmt/format.h>
#include <yaml-cpp/yaml.h>

#include <fstream>
#include <memory>
#include <sstream>
#include <tt-logger/tt-logger.hpp>

#include "api/umd/device/blackhole_implementation.h"
#include "api/umd/device/wormhole_implementation.h"
#include "assert.hpp"
#include "disjoint_set.hpp"

using namespace tt;

bool tt_ClusterDescriptor::ethernet_core_has_active_ethernet_link(
    chip_id_t local_chip, ethernet_channel_t local_ethernet_channel) const {
    return (this->ethernet_connections.find(local_chip) != this->ethernet_connections.end() &&
            this->ethernet_connections.at(local_chip).find(local_ethernet_channel) !=
                this->ethernet_connections.at(local_chip).end()) ||
           (this->ethernet_connections_to_remote_mmio_devices.find(local_chip) !=
                this->ethernet_connections_to_remote_mmio_devices.end() &&
            this->ethernet_connections_to_remote_mmio_devices.at(local_chip).find(local_ethernet_channel) !=
                this->ethernet_connections_to_remote_mmio_devices.at(local_chip).end());
}

std::tuple<chip_id_t, ethernet_channel_t> tt_ClusterDescriptor::get_chip_and_channel_of_remote_ethernet_core(
    chip_id_t local_chip, ethernet_channel_t local_ethernet_channel) const {
    std::vector<std::tuple<ethernet_channel_t, ethernet_channel_t>> directly_connected_channels = {};
    if (this->all_chips.find(local_chip) == this->all_chips.end() ||
        this->ethernet_connections.at(local_chip).find(local_ethernet_channel) ==
            this->ethernet_connections.at(local_chip).end()) {
        return {};
    }

    const auto &[connected_chip, connected_channel] =
        this->ethernet_connections.at(local_chip).at(local_ethernet_channel);
    if (this->all_chips.find(connected_chip) == this->all_chips.end()) {
        return {};
    } else {
        return {connected_chip, connected_channel};
    }
}

// NOTE: It might be worthwhile to precompute this for every pair of directly connected chips, depending on how
// extensively router needs to use it
std::vector<std::tuple<ethernet_channel_t, ethernet_channel_t>>
tt_ClusterDescriptor::get_directly_connected_ethernet_channels_between_chips(
    const chip_id_t &first, const chip_id_t &second) const {
    std::vector<std::tuple<ethernet_channel_t, ethernet_channel_t>> directly_connected_channels = {};
    if (this->all_chips.find(first) == this->all_chips.end() || this->all_chips.find(second) == this->all_chips.end()) {
        return {};
    }

    for (const auto &[first_ethernet_channel, connected_chip_and_channel] : this->ethernet_connections.at(first)) {
        if (std::get<0>(connected_chip_and_channel) == second) {
            directly_connected_channels.push_back({first_ethernet_channel, std::get<1>(connected_chip_and_channel)});
        }
    }

    return directly_connected_channels;
}

bool tt_ClusterDescriptor::is_chip_mmio_capable(const chip_id_t chip_id) const {
    return this->chips_with_mmio.find(chip_id) != this->chips_with_mmio.end();
}

bool tt_ClusterDescriptor::is_chip_remote(const chip_id_t chip_id) const { return !is_chip_mmio_capable(chip_id); }

// given two coordinates, finds the number of hops between the two chips
// it assumes that shelves are connected in x-dim and racks are connected in y-dim
// it recursively hops between shelves (in x-dim) until the correct shelf is found,
// then it recursively hops between racks (in y-dim) until the correct rack is found,
// then once a chip on the same shelf&rack is found,
// the distance from this chip to either location_a or location_b is just x&y dim difference.
// the function returns the total distance of travelled between shelves and racks, plust the x&y dim difference
int tt_ClusterDescriptor::get_ethernet_link_coord_distance(
    const eth_coord_t &location_a, const eth_coord_t &location_b) const {
    log_trace(
        LogSiliconDriver,
        "get_ethernet_link_coord_distance from ({}, {}, {}, {}, {}) to ({}, {}, {}, {}, {})",
        location_a.cluster_id,
        location_a.x,
        location_a.y,
        location_a.rack,
        location_a.shelf,
        location_b.cluster_id,
        location_b.x,
        location_b.y,
        location_b.rack,
        location_b.shelf);

    if (location_a.cluster_id != location_b.cluster_id) {
        return std::numeric_limits<int>::max();
    }

    int x_distance = std::abs(location_a.x - location_b.x);
    int y_distance = std::abs(location_a.y - location_b.y);

    // move along y-dim to exit from the shelf to go to a higher shelf
    if (location_b.shelf > location_a.shelf) {
        // this is already verified where galaxy_shelves_exit_chip_coords_per_y_dim is populated, but just to be safe
        TT_ASSERT(
            galaxy_shelves_exit_chip_coords_per_y_dim.find(location_a.shelf) !=
                galaxy_shelves_exit_chip_coords_per_y_dim.end(),
            "Expected shelf-to-shelf connection");
        // this row does not have a shelf-to-shelf connection
        if (galaxy_shelves_exit_chip_coords_per_y_dim.at(location_a.shelf).find(location_a.y) ==
            galaxy_shelves_exit_chip_coords_per_y_dim.at(location_a.shelf).end()) {
            return std::numeric_limits<int>::max();
        }

        const Chip2ChipConnection &shelf_to_shelf_connection =
            galaxy_shelves_exit_chip_coords_per_y_dim.at(location_a.shelf).at(location_a.y);
        TT_ASSERT(
            shelf_to_shelf_connection.destination_chip_coords.size(),
            "Expecting at least one shelf-to-shelf connection, possibly one-to-many");

        // for each shelf-to-shelf connection at location_a.y, find the distance to location_b, take min
        int distance = std::numeric_limits<int>::max();
        eth_coord_t exit_shelf = shelf_to_shelf_connection.source_chip_coord;
        for (eth_coord_t next_shelf : shelf_to_shelf_connection.destination_chip_coords) {
            TT_ASSERT(
                exit_shelf.y == location_a.y && exit_shelf.shelf == location_a.shelf &&
                    exit_shelf.rack == location_a.rack,
                "Invalid shelf exit coordinates");

            // next shelf could be at a different y-dim in nebula->galaxy systems
            TT_ASSERT(
                next_shelf.shelf == (location_a.shelf + 1) && next_shelf.rack == location_a.rack,
                "Invalid shelf entry coordinates");

            // hop onto the next shelf and find distance from there
            int distance_to_exit = get_ethernet_link_coord_distance(location_a, exit_shelf);
            int distance_in_next_shelf = get_ethernet_link_coord_distance(next_shelf, location_b);
            // no path found
            if (distance_to_exit == std::numeric_limits<int>::max() ||
                distance_in_next_shelf == std::numeric_limits<int>::max()) {
                continue;
            }
            distance = std::min(distance, distance_to_exit + distance_in_next_shelf + 1);
        }
        log_trace(
            LogSiliconDriver,
            "\tdistance from ({}, {}, {}, {}) to ({}, {}, {}, {}) is {}",
            location_a.x,
            location_a.y,
            location_a.rack,
            location_a.shelf,
            location_b.x,
            location_b.y,
            location_b.rack,
            location_b.shelf,
            distance);
        return distance;
    } else if (location_a.shelf > location_b.shelf) {
        // this is already verified where galaxy_shelves_exit_chip_coords_per_y_dim is populated, but just to be safe
        TT_ASSERT(
            galaxy_shelves_exit_chip_coords_per_y_dim.find(location_b.shelf) !=
                galaxy_shelves_exit_chip_coords_per_y_dim.end(),
            "Expected shelf-to-shelf connection");
        // this row does not have a shelf-to-shelf connection
        if (galaxy_shelves_exit_chip_coords_per_y_dim.at(location_b.shelf).find(location_b.y) ==
            galaxy_shelves_exit_chip_coords_per_y_dim.at(location_b.shelf).end()) {
            return std::numeric_limits<int>::max();
        }

        const Chip2ChipConnection &shelf_to_shelf_connection =
            galaxy_shelves_exit_chip_coords_per_y_dim.at(location_b.shelf).at(location_b.y);
        TT_ASSERT(
            shelf_to_shelf_connection.destination_chip_coords.size(),
            "Expecting at least one shelf-to-shelf connection, possibly one-to-many");

        // for each shelf-to-shelf connection at location_b.y, find the distance to location_a, take min
        int distance = std::numeric_limits<int>::max();
        eth_coord_t exit_shelf = shelf_to_shelf_connection.source_chip_coord;
        for (eth_coord_t next_shelf : shelf_to_shelf_connection.destination_chip_coords) {
            TT_ASSERT(
                exit_shelf.y == location_b.y && exit_shelf.shelf == location_b.shelf &&
                    exit_shelf.rack == location_b.rack,
                "Invalid shelf exit coordinates");
            // next shelf could be at a different y-dim in nebula->galaxy systems
            TT_ASSERT(
                next_shelf.shelf == (location_b.shelf + 1) && next_shelf.rack == location_b.rack,
                "Invalid shelf entry coordinates");

            // hop onto the next shelf and find distance from there
            int distance_to_exit = get_ethernet_link_coord_distance(location_b, exit_shelf);
            int distance_in_next_shelf = get_ethernet_link_coord_distance(next_shelf, location_a);
            // no path found
            if (distance_to_exit == std::numeric_limits<int>::max() ||
                distance_in_next_shelf == std::numeric_limits<int>::max()) {
                continue;
            }
            distance = std::min(distance, distance_to_exit + distance_in_next_shelf + 1);
        }
        log_trace(
            LogSiliconDriver,
            "\tdistance from ({}, {}, {}, {}) to ({}, {}, {}, {}) is {}",
            location_a.x,
            location_a.y,
            location_a.rack,
            location_a.shelf,
            location_b.x,
            location_b.y,
            location_b.rack,
            location_b.shelf,
            distance);
        return distance;
    }

    // move along y-dim to exit from the shelf to go to a higher shelf
    if (location_b.rack > location_a.rack) {
        // this is already verified where galaxy_racks_exit_chip_coords_per_x_dim is populated, but just to be safe
        TT_ASSERT(
            galaxy_racks_exit_chip_coords_per_x_dim.find(location_a.rack) !=
                galaxy_racks_exit_chip_coords_per_x_dim.end(),
            "Expected rack-to-rack connection");

        // this row does not have a rack-to-rack connection
        if (galaxy_racks_exit_chip_coords_per_x_dim.at(location_a.rack).find(location_a.x) ==
            galaxy_racks_exit_chip_coords_per_x_dim.at(location_a.rack).end()) {
            return std::numeric_limits<int>::max();
        }

        const Chip2ChipConnection &rack_to_rack_connection =
            galaxy_racks_exit_chip_coords_per_x_dim.at(location_a.rack).at(location_a.x);
        TT_ASSERT(
            rack_to_rack_connection.destination_chip_coords.size(),
            "Expecting at least one rack-to-rack connection, possibly one-to-many");

        // for each rack-to-rack connection at location_a.x, find the distance to location_b, take min
        int distance = std::numeric_limits<int>::max();
        eth_coord_t exit_rack = rack_to_rack_connection.source_chip_coord;
        for (eth_coord_t next_rack : rack_to_rack_connection.destination_chip_coords) {
            TT_ASSERT(
                exit_rack.x == location_a.x && exit_rack.shelf == location_a.shelf && exit_rack.rack == location_a.rack,
                "Invalid rack exit coordinates");
            TT_ASSERT(
                next_rack.x == location_a.x && next_rack.shelf == location_a.shelf &&
                    next_rack.rack == (location_a.rack + 1),
                "Invalid rack entry coordinates");

            // hop onto the next rack and find distance from there
            int distance_to_exit = get_ethernet_link_coord_distance(location_a, exit_rack);
            int distance_in_next_rack = get_ethernet_link_coord_distance(next_rack, location_b);
            // no path found
            if (distance_to_exit == std::numeric_limits<int>::max() ||
                distance_in_next_rack == std::numeric_limits<int>::max()) {
                continue;
            }
            distance = std::min(distance, distance_to_exit + distance_in_next_rack + 1);
        }
        log_trace(
            LogSiliconDriver,
            "\tdistance from ({}, {}, {}, {}) to ({}, {}, {}, {}) is {}",
            location_a.x,
            location_a.y,
            location_a.rack,
            location_a.shelf,
            location_b.x,
            location_b.y,
            location_b.rack,
            location_b.shelf,
            distance);

        return distance;
    } else if (location_a.rack > location_b.rack) {
        // this is already verified where galaxy_racks_exit_chip_coords_per_x_dim is populated, but just to be safe
        TT_ASSERT(
            galaxy_racks_exit_chip_coords_per_x_dim.find(location_b.rack) !=
                galaxy_racks_exit_chip_coords_per_x_dim.end(),
            "Expected rack-to-rack connection");

        // this row does not have a rack-to-rack connection
        if (galaxy_racks_exit_chip_coords_per_x_dim.at(location_b.rack).find(location_b.x) ==
            galaxy_racks_exit_chip_coords_per_x_dim.at(location_b.rack).end()) {
            return std::numeric_limits<int>::max();
        }

        const Chip2ChipConnection &rack_to_rack_connection =
            galaxy_racks_exit_chip_coords_per_x_dim.at(location_b.rack).at(location_b.x);
        TT_ASSERT(
            rack_to_rack_connection.destination_chip_coords.size(),
            "Expecting at least one rack-to-rack connection, possibly one-to-many");

        // for each rack-to-rack connection at location_a.x, find the distance to location_b, take min
        int distance = std::numeric_limits<int>::max();
        eth_coord_t exit_rack = rack_to_rack_connection.source_chip_coord;
        for (eth_coord_t next_rack : rack_to_rack_connection.destination_chip_coords) {
            TT_ASSERT(
                exit_rack.x == location_b.x && exit_rack.shelf == location_b.shelf && exit_rack.rack == location_b.rack,
                "Invalid rack exit coordinates");
            TT_ASSERT(
                next_rack.x == location_b.x && next_rack.shelf == location_b.shelf &&
                    next_rack.rack == (location_b.rack + 1),
                "Invalid rack entry coordinates");

            // hop onto the next rack and find distance from there
            int distance_to_exit = get_ethernet_link_coord_distance(location_b, exit_rack);
            int distance_in_next_rack = get_ethernet_link_coord_distance(next_rack, location_a);
            // no path found
            if (distance_to_exit == std::numeric_limits<int>::max() ||
                distance_in_next_rack == std::numeric_limits<int>::max()) {
                continue;
            }
            distance = std::min(distance, distance_to_exit + distance_in_next_rack + 1);
        }
        log_trace(
            LogSiliconDriver,
            "\tdistance from ({}, {}, {}, {}) to ({}, {}, {}, {}) is {}",
            location_a.x,
            location_a.y,
            location_a.rack,
            location_a.shelf,
            location_b.x,
            location_b.y,
            location_b.rack,
            location_b.shelf,
            distance);

        return distance;
    }

    log_trace(
        LogSiliconDriver,
        "\tdistance from ({}, {}, {}, {}) to ({}, {}, {}, {}) is {}",
        location_a.x,
        location_a.y,
        location_a.rack,
        location_a.shelf,
        location_b.x,
        location_b.y,
        location_b.rack,
        location_b.shelf,
        x_distance + y_distance);

    // on same shelf/rack, the distance is just x+y difference
    return x_distance + y_distance;
}

// Returns the closest mmio chip to the given chip
chip_id_t tt_ClusterDescriptor::get_closest_mmio_capable_chip(const chip_id_t chip) {
    log_debug(LogSiliconDriver, "get_closest_mmio_chip to chip{}", chip);

    if (this->is_chip_mmio_capable(chip)) {
        return chip;
    }

    if (closest_mmio_chip_cache.find(chip) != closest_mmio_chip_cache.end()) {
        return closest_mmio_chip_cache[chip];
    }

    int min_distance = std::numeric_limits<int>::max();
    chip_id_t closest_chip = chip;
    eth_coord_t chip_eth_coord = this->chip_locations.at(chip);

    for (const auto &pair : this->chips_with_mmio) {
        const chip_id_t &mmio_chip = pair.first;
        eth_coord_t mmio_eth_coord = this->chip_locations.at(mmio_chip);

        log_debug(
            LogSiliconDriver,
            "Checking chip{} at ({}, {}, {}, {})",
            mmio_chip,
            mmio_eth_coord.x,
            mmio_eth_coord.y,
            mmio_eth_coord.rack,
            mmio_eth_coord.shelf);

        int distance = get_ethernet_link_coord_distance(mmio_eth_coord, chip_eth_coord);
        log_debug(LogSiliconDriver, "Distance from chip{} to chip{} is {}", chip, mmio_chip, distance);
        if (distance < min_distance) {
            min_distance = distance;
            closest_chip = mmio_chip;
        }
    }
    TT_ASSERT(
        min_distance != std::numeric_limits<int>::max(), "Chip{} is not connected to any MMIO capable chip", chip);

    TT_ASSERT(is_chip_mmio_capable(closest_chip), "Closest MMIO chip must be MMIO capable");

    log_debug(LogSiliconDriver, "closest_mmio_chip to chip{} is chip{} distance:{}", chip, closest_chip, min_distance);

    closest_mmio_chip_cache[chip] = closest_chip;

    return closest_chip;
}

std::unique_ptr<tt_ClusterDescriptor> tt_ClusterDescriptor::create_from_yaml(
    const std::string &cluster_descriptor_file_path) {
    std::unique_ptr<tt_ClusterDescriptor> desc = std::unique_ptr<tt_ClusterDescriptor>(new tt_ClusterDescriptor());

    std::ifstream fdesc(cluster_descriptor_file_path);
    if (fdesc.fail()) {
        throw std::runtime_error(fmt::format(
            "Error: cluster connectivity descriptor file {} does not exist!", cluster_descriptor_file_path));
    }
    fdesc.close();

    YAML::Node yaml = YAML::LoadFile(cluster_descriptor_file_path);
    tt_ClusterDescriptor::load_chips_from_connectivity_descriptor(yaml, *desc);
    tt_ClusterDescriptor::load_harvesting_information(yaml, *desc);
    tt_ClusterDescriptor::load_ethernet_connections_from_connectivity_descriptor(yaml, *desc);
    tt_ClusterDescriptor::merge_cluster_ids(*desc);
    tt_ClusterDescriptor::fill_galaxy_connections(*desc);

    desc->fill_chips_grouped_by_closest_mmio();

    return desc;
}

template <typename T>
std::unordered_map<chip_id_t, T> filter_chip_collection(
    const std::unordered_map<chip_id_t, T> &collection, const std::unordered_set<chip_id_t> chips) {
    std::unordered_map<chip_id_t, T> filtered_collection;
    for (const auto &[chip_id, val] : collection) {
        auto it = chips.find(chip_id);
        if (it != chips.end()) {
            filtered_collection.emplace(chip_id, val);
        }
    }
    return filtered_collection;
}

template <typename T>
std::map<chip_id_t, T> filter_chip_collection(
    const std::map<chip_id_t, T> &collection, const std::unordered_set<chip_id_t> chips) {
    std::map<chip_id_t, T> filtered_collection;
    for (const auto &[chip_id, val] : collection) {
        auto it = chips.find(chip_id);
        if (it != chips.end()) {
            filtered_collection.emplace(chip_id, val);
        }
    }
    return filtered_collection;
}

template <typename T>
std::map<T, chip_id_t> filter_chip_collection(
    const std::map<T, chip_id_t> &collection, const std::unordered_set<chip_id_t> chips) {
    std::map<T, chip_id_t> filtered_collection;
    for (const auto &[val, chip_id] : collection) {
        auto it = chips.find(chip_id);
        if (it != chips.end()) {
            filtered_collection.emplace(val, chip_id);
        }
    }
    return filtered_collection;
}

std::unordered_set<chip_id_t> filter_chip_collection(
    const std::unordered_set<chip_id_t> &collection, const std::unordered_set<chip_id_t> chips) {
    std::unordered_set<chip_id_t> filtered_collection;
    for (const auto &chip_id : collection) {
        auto it = chips.find(chip_id);
        if (it != chips.end()) {
            filtered_collection.emplace(chip_id);
        }
    }
    return filtered_collection;
}

std::unique_ptr<tt_ClusterDescriptor> tt_ClusterDescriptor::create_constrained_cluster_descriptor(
    const tt_ClusterDescriptor *full_cluster_desc, const std::unordered_set<chip_id_t> &target_chip_ids) {
    std::unique_ptr<tt_ClusterDescriptor> desc = std::unique_ptr<tt_ClusterDescriptor>(new tt_ClusterDescriptor());

    desc->chip_locations = filter_chip_collection(full_cluster_desc->chip_locations, target_chip_ids);
    desc->chips_with_mmio = filter_chip_collection(full_cluster_desc->chips_with_mmio, target_chip_ids);
    desc->all_chips = filter_chip_collection(full_cluster_desc->all_chips, target_chip_ids);
    desc->noc_translation_enabled = filter_chip_collection(full_cluster_desc->noc_translation_enabled, target_chip_ids);
    desc->harvesting_masks = filter_chip_collection(full_cluster_desc->harvesting_masks, target_chip_ids);
    // desc->closest_mmio_chip_cache is not copied intentionally, it could hold wrong information.
    desc->chip_board_type = filter_chip_collection(full_cluster_desc->chip_board_type, target_chip_ids);
    desc->chip_arch = filter_chip_collection(full_cluster_desc->chip_arch, target_chip_ids);
    desc->chip_uid_to_chip_id = filter_chip_collection(full_cluster_desc->chip_uid_to_chip_id, target_chip_ids);
    desc->chip_id_to_chip_uid = filter_chip_collection(full_cluster_desc->chip_id_to_chip_uid, target_chip_ids);
    desc->chip_unique_ids = filter_chip_collection(full_cluster_desc->chip_unique_ids, target_chip_ids);
    // Note that these preserve the full set of channels. So some channels will be reported as active
    // even though their corresponding entries won't be found in ethernet_connections. We want this behavior
    // so that the client doesn't try to do anything on these ETH cores which could break these links.
    desc->active_eth_channels = filter_chip_collection(full_cluster_desc->active_eth_channels, target_chip_ids);
    desc->idle_eth_channels = filter_chip_collection(full_cluster_desc->idle_eth_channels, target_chip_ids);

    desc->galaxy_shelves_exit_chip_coords_per_y_dim = full_cluster_desc->galaxy_shelves_exit_chip_coords_per_y_dim;
    desc->galaxy_racks_exit_chip_coords_per_x_dim = full_cluster_desc->galaxy_racks_exit_chip_coords_per_x_dim;

    desc->dram_harvesting_masks = filter_chip_collection(full_cluster_desc->dram_harvesting_masks, target_chip_ids);
    desc->eth_harvesting_masks = filter_chip_collection(full_cluster_desc->eth_harvesting_masks, target_chip_ids);
    desc->pcie_harvesting_masks = filter_chip_collection(full_cluster_desc->pcie_harvesting_masks, target_chip_ids);

    // Write explicitly filters for more complex structures.
    for (const auto &[chip_id, eth_connections] : full_cluster_desc->ethernet_connections) {
        if (target_chip_ids.find(chip_id) == target_chip_ids.end()) {
            continue;
        }

        for (const auto &[eth_id, connection] : eth_connections) {
            const auto &[remote_chip_id, remote_eth_id] = connection;
            if (target_chip_ids.find(remote_chip_id) == target_chip_ids.end()) {
                continue;
            }
            desc->ethernet_connections[chip_id][eth_id] = {remote_chip_id, remote_eth_id};
        }
    }

    for (const auto &[rack_id, shelf_map] : full_cluster_desc->coords_to_chip_ids) {
        for (const auto &[shelf_id, y_map] : shelf_map) {
            for (const auto &[y_dim, x_map] : y_map) {
                for (const auto &[x_dim, chip_id] : x_map) {
                    if (target_chip_ids.find(chip_id) == target_chip_ids.end()) {
                        continue;
                    }
                    desc->coords_to_chip_ids[rack_id][shelf_id][y_dim][x_dim] = chip_id;
                }
            }
        }
    }

    for (const auto &[chip_id, chip_group] : full_cluster_desc->chips_grouped_by_closest_mmio) {
        if (target_chip_ids.find(chip_id) == target_chip_ids.end()) {
            continue;
        }

        desc->chips_grouped_by_closest_mmio[chip_id] = filter_chip_collection(chip_group, target_chip_ids);
    }

    return desc;
}

std::unique_ptr<tt_ClusterDescriptor> tt_ClusterDescriptor::create_mock_cluster(
    const std::vector<chip_id_t> &logical_device_ids, tt::ARCH arch) {
    std::unique_ptr<tt_ClusterDescriptor> desc = std::unique_ptr<tt_ClusterDescriptor>(new tt_ClusterDescriptor());

    BoardType board_type;
    switch (arch) {
        case tt::ARCH::WORMHOLE_B0:
            board_type = BoardType::N150;
            break;
        case tt::ARCH::BLACKHOLE:
            board_type = BoardType::P150;
            break;
        default:
            board_type = BoardType::UNKNOWN;
            log_error(LogSiliconDriver, "Unsupported architecture for mock cluster");
            break;
    }

    for (auto &logical_id : logical_device_ids) {
        desc->all_chips.insert(logical_id);
        eth_coord_t chip_location{0, logical_id, 0, 0, 0};
        desc->chip_locations.insert({logical_id, chip_location});
        desc->coords_to_chip_ids[chip_location.rack][chip_location.shelf][chip_location.y][chip_location.x] =
            logical_id;
        log_debug(tt::LogSiliconDriver, "{} - adding logical: {}", __FUNCTION__, logical_id);
        desc->chip_board_type.insert({logical_id, board_type});
        desc->chips_with_mmio.insert({logical_id, logical_id});
        desc->chip_arch.insert({logical_id, arch});
        desc->noc_translation_enabled.insert({logical_id, true});
        desc->harvesting_masks.insert({logical_id, 0});
    }
    desc->fill_chips_grouped_by_closest_mmio();

    return desc;
}

void tt_ClusterDescriptor::load_ethernet_connections_from_connectivity_descriptor(
    YAML::Node &yaml, tt_ClusterDescriptor &desc) {
    TT_ASSERT(yaml["ethernet_connections"].IsSequence(), "Invalid YAML");

    // Preload idle eth channels.
    for (const auto &chip : desc.all_chips) {
        int num_harvested_channels = desc.eth_harvesting_masks.empty()
                                         ? 0
                                         : CoordinateManager::get_num_harvested(desc.eth_harvesting_masks.at(chip));
        int num_channels =
            tt::umd::architecture_implementation::create(desc.chip_arch.at(chip))->get_num_eth_channels() -
            num_harvested_channels;
        for (int i = 0; i < num_channels; i++) {
            desc.idle_eth_channels[chip].insert(i);
        }
    }

    for (YAML::Node &connected_endpoints : yaml["ethernet_connections"].as<std::vector<YAML::Node>>()) {
        TT_ASSERT(connected_endpoints.IsSequence(), "Invalid YAML");

        std::vector<YAML::Node> endpoints = connected_endpoints.as<std::vector<YAML::Node>>();
        TT_ASSERT(
            endpoints.size() <= 3,
            "Ethernet connections in YAML should always contatin information on connected endpoints and optionally "
            "information on whether "
            "routing is enabled.");

        int chip_0 = endpoints.at(0)["chip"].as<int>();
        int channel_0 = endpoints.at(0)["chan"].as<int>();
        int chip_1 = endpoints.at(1)["chip"].as<int>();
        int channel_1 = endpoints.at(1)["chan"].as<int>();
        auto &eth_conn_chip_0 = desc.ethernet_connections.at(chip_0);
        if (eth_conn_chip_0.find(channel_0) != eth_conn_chip_0.end()) {
            TT_ASSERT(
                (std::get<0>(eth_conn_chip_0.at(channel_0)) == chip_1) &&
                    (std::get<1>(eth_conn_chip_0.at(channel_0)) == channel_1),
                "Duplicate eth connection found in cluster desc yaml");
        } else {
            eth_conn_chip_0.insert({channel_0, {chip_1, channel_1}});
        }
        auto &eth_conn_chip_1 = desc.ethernet_connections.at(chip_1);
        if (eth_conn_chip_1.find(channel_1) != eth_conn_chip_1.end()) {
            TT_ASSERT(
                (std::get<0>(eth_conn_chip_1.at(channel_1)) == chip_0) &&
                    (std::get<1>(eth_conn_chip_1.at(channel_1)) == channel_0),
                "Duplicate eth connection found in cluster desc yaml");
        } else {
            eth_conn_chip_1.insert({channel_1, {chip_0, channel_0}});
        }
        desc.active_eth_channels[chip_0].insert(channel_0);
        desc.idle_eth_channels[chip_0].erase(channel_0);
        desc.active_eth_channels[chip_1].insert(channel_1);
        desc.idle_eth_channels[chip_1].erase(channel_1);
    }

    // std::unordered_map<ethernet_channel_t, std::tuple<chip_id_t, ethernet_channel_t>>> ethernet_connections;

    log_debug(LogSiliconDriver, "Ethernet Connectivity Descriptor:");
    for (const auto &[chip, chan_to_chip_chan_map] : desc.ethernet_connections) {
        for (const auto &[chan, chip_and_chan] : chan_to_chip_chan_map) {
            log_debug(
                LogSiliconDriver,
                "\tchip: {}, chan: {}  <-->  chip: {}, chan: {}",
                chip,
                chan,
                std::get<0>(chip_and_chan),
                std::get<1>(chip_and_chan));
        }
    }

    log_debug(LogSiliconDriver, "Chip Coordinates:");
    for (const auto &[rack_id, rack_chip_map] : desc.coords_to_chip_ids) {
        for (const auto &[shelf_id, shelf_chip_map] : rack_chip_map) {
            log_debug(LogSiliconDriver, "\tRack:{} Shelf:{}", rack_id, shelf_id);
            for (const auto &[row, row_chip_map] : shelf_chip_map) {
                std::stringstream row_chips;
                for (const auto &[col, chip_id] : row_chip_map) {
                    row_chips << chip_id << "\t";
                }
                log_debug(LogSiliconDriver, "\t\t{}", row_chips.str());
            }
        }
    }
}

void tt_ClusterDescriptor::fill_galaxy_connections(tt_ClusterDescriptor &desc) {
    int highest_shelf_id = 0;
    int highest_rack_id = 0;

    // shelves and racks can be connected at different chip coordinates
    // determine which chips are connected to the next (i.e. higher id) shelf/rack and what the coordinate of the chip
    // on the other shelf/rack is this is used in get_ethernet_link_coord_distance to find the distance between two
    // chips
    for (const auto &[chip_id, chip_eth_coord] : desc.chip_locations) {
        highest_shelf_id = std::max(highest_shelf_id, chip_eth_coord.shelf);
        highest_rack_id = std::max(highest_rack_id, chip_eth_coord.rack);
        // iterate over all neighbors
        if (desc.ethernet_connections.find(chip_id) == desc.ethernet_connections.end()) {
            continue;  // chip has no eth connections
        }
        for (const auto &[chan, chip_and_chan] : desc.ethernet_connections.at(chip_id)) {
            const chip_id_t &neighbor_chip = std::get<0>(chip_and_chan);
            eth_coord_t neighbor_eth_coord = desc.chip_locations.at(neighbor_chip);
            // shelves are connected in x-dim
            if (neighbor_eth_coord.shelf != chip_eth_coord.shelf) {
                eth_coord_t higher_shelf_coord =
                    neighbor_eth_coord.shelf > chip_eth_coord.shelf ? neighbor_eth_coord : chip_eth_coord;
                eth_coord_t lower_shelf_coord =
                    neighbor_eth_coord.shelf < chip_eth_coord.shelf ? neighbor_eth_coord : chip_eth_coord;
                int lower_shelf_id = lower_shelf_coord.shelf;
                int lower_shelf_y = lower_shelf_coord.y;

                auto &galaxy_shelf_exit_chip_coords_per_y_dim =
                    desc.galaxy_shelves_exit_chip_coords_per_y_dim[lower_shelf_id];

                TT_ASSERT(
                    galaxy_shelf_exit_chip_coords_per_y_dim.find(lower_shelf_y) ==
                            galaxy_shelf_exit_chip_coords_per_y_dim.end() ||
                        galaxy_shelf_exit_chip_coords_per_y_dim[lower_shelf_y].source_chip_coord == lower_shelf_coord,
                    "Expected a single exit chip on each shelf row");
                galaxy_shelf_exit_chip_coords_per_y_dim[lower_shelf_y].source_chip_coord = lower_shelf_coord;
                galaxy_shelf_exit_chip_coords_per_y_dim[lower_shelf_y].destination_chip_coords.insert(
                    higher_shelf_coord);
            }

            // racks are connected in y-dim
            if (neighbor_eth_coord.rack != chip_eth_coord.rack) {
                eth_coord_t higher_rack_coord =
                    neighbor_eth_coord.rack > chip_eth_coord.rack ? neighbor_eth_coord : chip_eth_coord;
                eth_coord_t lower_rack_coord =
                    neighbor_eth_coord.rack < chip_eth_coord.rack ? neighbor_eth_coord : chip_eth_coord;
                int lower_rack_id = lower_rack_coord.rack;
                int lower_rack_x = lower_rack_coord.x;

                auto &galaxy_rack_exit_chip_coords_per_x_dim =
                    desc.galaxy_racks_exit_chip_coords_per_x_dim[lower_rack_id];

                TT_ASSERT(
                    galaxy_rack_exit_chip_coords_per_x_dim.find(lower_rack_x) ==
                            galaxy_rack_exit_chip_coords_per_x_dim.end() ||
                        galaxy_rack_exit_chip_coords_per_x_dim[lower_rack_x].source_chip_coord == lower_rack_coord,
                    "Expected a single exit chip on each rack column");
                galaxy_rack_exit_chip_coords_per_x_dim[lower_rack_x].source_chip_coord = lower_rack_coord;
                galaxy_rack_exit_chip_coords_per_x_dim[lower_rack_x].destination_chip_coords.insert(higher_rack_coord);
            }
        }
    }

    // verify that every shelf (except the highest in id) is found in galaxy_shelves_exit_chip_coords_per_y_dim
    // this means that we expect the shelves to be connected linearly in a daisy-chain fashion.
    // shelf0->shelf1->shelf2->...->shelfN
    for (int shelf_id = 0; shelf_id < highest_shelf_id; shelf_id++) {
        TT_ASSERT(
            desc.galaxy_shelves_exit_chip_coords_per_y_dim.find(shelf_id) !=
                desc.galaxy_shelves_exit_chip_coords_per_y_dim.end(),
            "Expected shelf {} to be connected to the next shelf",
            shelf_id);
    }

    // this prints the exit chip coordinates for each shelf
    // this is used in get_ethernet_link_coord_distance to find the distance between two chips
    for (const auto &[shelf, shelf_exit_chip_coords_per_y_dim] : desc.galaxy_shelves_exit_chip_coords_per_y_dim) {
        for (const auto &[y_dim, shelf_exit_chip_coords] : shelf_exit_chip_coords_per_y_dim) {
            log_debug(
                LogSiliconDriver,
                "shelf: {} y_dim: {} exit_coord:({}, {}, {}, {})",
                shelf,
                y_dim,
                shelf_exit_chip_coords.source_chip_coord.x,
                shelf_exit_chip_coords.source_chip_coord.y,
                shelf_exit_chip_coords.source_chip_coord.rack,
                shelf_exit_chip_coords.source_chip_coord.shelf);
            for (const auto &destination_chip_coord : shelf_exit_chip_coords.destination_chip_coords) {
                // print shelf_exit_chip_coord in the format: (x, y, rack, shelf)
                log_debug(
                    LogSiliconDriver,
                    "\tdestination_chip_coord: ({}, {}, {}, {})",
                    destination_chip_coord.x,
                    destination_chip_coord.y,
                    destination_chip_coord.rack,
                    destination_chip_coord.shelf);
            }
        }
    }

    // verify that every rack (except the highest in id) is found in galaxy_racks_exit_chip_coords_per_x_dim
    // this means that we expect the racks to be connected linearly in a daisy-chain fashion.
    // rack0->rack1->rack2->...->rackN
    for (int rack_id = 0; rack_id < highest_rack_id; rack_id++) {
        TT_ASSERT(
            desc.galaxy_racks_exit_chip_coords_per_x_dim.find(rack_id) !=
                desc.galaxy_racks_exit_chip_coords_per_x_dim.end(),
            "Expected rack {} to be connected to the next rack",
            rack_id);
    }

    // this prints the exit chip coordinates for each rack
    // this is used in get_ethernet_link_coord_distance to find the distance between two chips
    for (const auto &[rack, rack_exit_chip_coords_per_x_dim] : desc.galaxy_racks_exit_chip_coords_per_x_dim) {
        for (const auto &[x_dim, rack_exit_chip_coords] : rack_exit_chip_coords_per_x_dim) {
            log_debug(
                LogSiliconDriver,
                "rack: {} x_dim: {} exit_coord:({}, {}, {}, {})",
                rack,
                x_dim,
                rack_exit_chip_coords.source_chip_coord.x,
                rack_exit_chip_coords.source_chip_coord.y,
                rack_exit_chip_coords.source_chip_coord.rack,
                rack_exit_chip_coords.source_chip_coord.shelf);
            for (const auto &destination_chip_coord : rack_exit_chip_coords.destination_chip_coords) {
                log_debug(
                    LogSiliconDriver,
                    "\tdestination_chip_coord: ({}, {}, {}, {})",
                    destination_chip_coord.x,
                    destination_chip_coord.y,
                    destination_chip_coord.rack,
                    destination_chip_coord.shelf);
            }
        }
    }
}

void tt_ClusterDescriptor::merge_cluster_ids(tt_ClusterDescriptor &desc) {
    DisjointSet<chip_id_t> chip_sets;
    for (const auto &[chip, _] : desc.chip_locations) {
        chip_sets.add_item(chip);
        log_debug(LogSiliconDriver, "Adding chip {} to disjoint set", chip);
    }

    for (const auto &[chip, chan_to_chip_chan_map] : desc.ethernet_connections) {
        for (const auto &[chan, dest_chip_chan_tuple] : chan_to_chip_chan_map) {
            chip_sets.merge(chip, std::get<0>(dest_chip_chan_tuple));
            log_debug(LogSiliconDriver, "Merging chip {} and chip {}", chip, std::get<0>(dest_chip_chan_tuple));
        }
    }

    for (const auto &[chip, chip_eth_coords] : desc.chip_locations) {
        desc.chip_locations[chip].cluster_id = chip_sets.get_set(chip);
        log_debug(LogSiliconDriver, "Chip {} belongs to cluster {}", chip, chip_sets.get_set(chip));
    }
}

void tt_ClusterDescriptor::load_chips_from_connectivity_descriptor(YAML::Node &yaml, tt_ClusterDescriptor &desc) {
    for (YAML::const_iterator node = yaml["arch"].begin(); node != yaml["arch"].end(); ++node) {
        chip_id_t chip_id = node->first.as<int>();
        std::string arch_str = node->second.as<std::string>();
        desc.all_chips.insert(chip_id);
        desc.chip_arch.insert({chip_id, tt::arch_from_str(arch_str)});
        desc.ethernet_connections.insert({chip_id, {}});
    }

    for (YAML::const_iterator node = yaml["chips"].begin(); node != yaml["chips"].end(); ++node) {
        chip_id_t chip_id = node->first.as<int>();
        std::vector<int> chip_rack_coords = node->second.as<std::vector<int>>();
        TT_ASSERT(chip_rack_coords.size() == 4, "Galaxy (x, y, rack, shelf) coords must be size 4");
        eth_coord_t chip_location{
            chip_id, chip_rack_coords.at(0), chip_rack_coords.at(1), chip_rack_coords.at(2), chip_rack_coords.at(3)};

        desc.chip_locations.insert({chip_id, chip_location});
        desc.coords_to_chip_ids[chip_location.rack][chip_location.shelf][chip_location.y][chip_location.x] = chip_id;
    }

    for (const auto &chip : yaml["chips_with_mmio"]) {
        if (chip.IsMap()) {
            const auto &chip_map = chip.as<std::map<chip_id_t, chip_id_t>>();
            const auto &chips = chip_map.begin();
            desc.chips_with_mmio.insert({chips->first, chips->second});
        } else {
            const auto &chip_val = chip.as<int>();
            desc.chips_with_mmio.insert({chip_val, chip_val});
        }
    }
    log_debug(LogSiliconDriver, "Device IDs and Locations:");
    for (const auto &[chip_id, chip_location] : desc.chip_locations) {
        log_debug(
            LogSiliconDriver,
            "\tchip: {},  EthCoord(x={}, y={}, rack={}, shelf={})",
            chip_id,
            chip_location.x,
            chip_location.y,
            chip_location.rack,
            chip_location.shelf);
    }

    if (yaml["chip_to_boardtype"]) {
        for (const auto &chip_board_type : yaml["chip_to_boardtype"].as<std::map<int, std::string>>()) {
            auto &chip = chip_board_type.first;
            BoardType board_type;
            if (chip_board_type.second == "n150") {
                board_type = BoardType::N150;
            } else if (chip_board_type.second == "n300") {
                board_type = BoardType::N300;
            } else if (chip_board_type.second == "p100") {
                board_type = BoardType::P100;
            } else if (
                chip_board_type.second == "p150" || chip_board_type.second == "p150A" ||
                chip_board_type.second == "p150C") {
                board_type = BoardType::P150;
            } else if (
                chip_board_type.second == "p300" || chip_board_type.second == "p300A" ||
                chip_board_type.second == "p300C") {
                board_type = BoardType::P300;
            } else if (chip_board_type.second == "GALAXY") {
                board_type = BoardType::GALAXY;
            } else if (chip_board_type.second == "ubb") {
                board_type = BoardType::UBB;
            } else {
                log_warning(
                    LogSiliconDriver,
                    "Unknown board type for chip {}. This might happen because chip is running old firmware. "
                    "Defaulting to UNKNOWN",
                    chip);
                board_type = BoardType::UNKNOWN;
            }
            desc.chip_board_type.insert({chip, board_type});
        }
    } else {
        for (const auto &chip : desc.all_chips) {
            desc.chip_board_type.insert({chip, BoardType::UNKNOWN});
        }
    }

    if (yaml["boards"]) {
        YAML::Node boardsNode = yaml["boards"];
        if (!boardsNode || !boardsNode.IsSequence()) {
            throw std::runtime_error("Invalid or missing 'boards' node.");
        }

        for (const auto &boardEntry : boardsNode) {
            if (!boardEntry.IsSequence() || boardEntry.size() != 3) {
                throw std::runtime_error("Each board entry should be a sequence of 3 maps.");
            }

            uint64_t board_id = boardEntry[0]["board_id"].as<std::uint64_t>();

            for (const auto &chip : boardEntry[2]["chips"]) {
                desc.add_chip_to_board(chip.as<chip_id_t>(), board_id);
            }
        }
    }
}

void tt_ClusterDescriptor::load_harvesting_information(YAML::Node &yaml, tt_ClusterDescriptor &desc) {
    if (yaml["harvesting"]) {
        for (const auto &chip_node : yaml["harvesting"].as<std::map<int, YAML::Node>>()) {
            chip_id_t chip = chip_node.first;
            auto harvesting_info = chip_node.second;
            desc.noc_translation_enabled.insert({chip, harvesting_info["noc_translation"].as<bool>()});
            desc.harvesting_masks.insert({chip, harvesting_info["harvest_mask"].as<std::uint32_t>()});

            if (harvesting_info["dram_harvesting_mask"].IsDefined()) {
                desc.dram_harvesting_masks.insert({chip, harvesting_info["dram_harvesting_mask"].as<std::uint32_t>()});
            }

            if (harvesting_info["eth_harvesting_mask"].IsDefined()) {
                desc.eth_harvesting_masks.insert({chip, harvesting_info["eth_harvesting_mask"].as<std::uint32_t>()});
            }

            if (harvesting_info["pcie_harvesting_mask"].IsDefined()) {
                desc.pcie_harvesting_masks.insert({chip, harvesting_info["pcie_harvesting_mask"].as<std::uint32_t>()});
            }
        }
    }
}

void tt_ClusterDescriptor::fill_chips_grouped_by_closest_mmio() {
    for (const auto &chip : this->all_chips) {
        // This will also fill up the closest_mmio_chip_cache
        chip_id_t closest_mmio_chip = get_closest_mmio_capable_chip(chip);
        this->chips_grouped_by_closest_mmio[closest_mmio_chip].insert(chip);
    }
}

const std::unordered_map<chip_id_t, std::unordered_map<ethernet_channel_t, std::tuple<chip_id_t, ethernet_channel_t>>> &
tt_ClusterDescriptor::get_ethernet_connections() const {
    return ethernet_connections;
}

const std::unordered_map<chip_id_t, std::unordered_map<ethernet_channel_t, std::tuple<uint64_t, ethernet_channel_t>>>
tt_ClusterDescriptor::get_ethernet_connections_to_remote_mmio_devices() const {
    return this->ethernet_connections_to_remote_mmio_devices;
}

const std::unordered_map<chip_id_t, eth_coord_t> &tt_ClusterDescriptor::get_chip_locations() const {
    return chip_locations;
}

// Note: this API works only for Wormhole 6U galaxy at the moment.
// TODO: implement this for Blackhole and old Wormhole configurations.
const std::unordered_map<chip_id_t, uint64_t> &tt_ClusterDescriptor::get_chip_unique_ids() const {
    return chip_unique_ids;
}

chip_id_t tt_ClusterDescriptor::get_shelf_local_physical_chip_coords(chip_id_t virtual_coord) {
    TT_ASSERT(
        !this->chip_locations.empty(),
        "Getting physical chip coordinates is only valid for systems where chips have coordinates");
    // Physical cooridnates of chip inside a single rack. Calculated based on Galaxy topology.
    // See:
    // https://yyz-gitlab.local.tenstorrent.com/tenstorrent/budabackend/-/wikis/uploads/23e7a5168f38dfb706f9887fde78cb03/image.png
    int x = get_chip_locations().at(virtual_coord).x;
    int y = get_chip_locations().at(virtual_coord).y;
    return 8 * x + y;
}

// Return map, but filter by enabled active chips.
const std::unordered_map<chip_id_t, chip_id_t> &tt_ClusterDescriptor::get_chips_with_mmio() const {
    return chips_with_mmio;
}

const std::unordered_set<chip_id_t> &tt_ClusterDescriptor::get_all_chips() const { return this->all_chips; }

const std::vector<chip_id_t> tt_ClusterDescriptor::get_chips_local_first(std::unordered_set<chip_id_t> chips) const {
    std::vector<chip_id_t> chips_local_first;
    for (const auto &chip : chips) {
        TT_ASSERT(
            this->all_chips.find(chip) != this->all_chips.end(), "Chip {} not found in cluster descriptor.", chip);
    }
    for (const auto &chip : chips) {
        if (is_chip_mmio_capable(chip)) {
            chips_local_first.push_back(chip);
        }
    }
    for (const auto &chip : chips) {
        if (is_chip_remote(chip)) {
            chips_local_first.push_back(chip);
        }
    }
    return chips_local_first;
}

const std::unordered_map<chip_id_t, std::uint32_t> &tt_ClusterDescriptor::get_harvesting_info() const {
    return harvesting_masks;
}

const std::unordered_map<chip_id_t, bool> &tt_ClusterDescriptor::get_noc_translation_table_en() const {
    return noc_translation_enabled;
}

std::size_t tt_ClusterDescriptor::get_number_of_chips() const { return this->all_chips.size(); }

int tt_ClusterDescriptor::get_ethernet_link_distance(chip_id_t chip_a, chip_id_t chip_b) const {
    TT_ASSERT(
        !this->chip_locations.empty(),
        "Getting physical chip coordinates is only valid for systems where chips have coordinates");
    return this->get_ethernet_link_coord_distance(chip_locations.at(chip_a), chip_locations.at(chip_b));
}

BoardType tt_ClusterDescriptor::get_board_type(chip_id_t chip_id) const {
    TT_ASSERT(
        chip_board_type.find(chip_id) != chip_board_type.end(),
        "Chip {} does not have a board type in the cluster descriptor",
        chip_id);
    return chip_board_type.at(chip_id);
}

tt::ARCH tt_ClusterDescriptor::get_arch(chip_id_t chip_id) const {
    TT_ASSERT(
        chip_arch.find(chip_id) != chip_arch.end(),
        "Chip {} does not have an architecture in the cluster descriptor",
        chip_id);
    return chip_arch.at(chip_id);
}

const std::unordered_map<chip_id_t, std::unordered_set<chip_id_t>> &
tt_ClusterDescriptor::get_chips_grouped_by_closest_mmio() const {
    return chips_grouped_by_closest_mmio;
}

void tt_ClusterDescriptor::add_chip_uid(const chip_id_t chip_id, const ChipUID &chip_uid) {
    chip_id_to_chip_uid[chip_id] = chip_uid;
    chip_uid_to_chip_id[chip_uid] = chip_id;
}

std::optional<chip_id_t> tt_ClusterDescriptor::get_chip_id(const ChipUID &chip_uid) const {
    auto chip_id_it = chip_uid_to_chip_id.find(chip_uid);
    if (chip_id_it == chip_uid_to_chip_id.end()) {
        return std::nullopt;
    }
    return chip_id_it->second;
}

std::optional<ChipUID> tt_ClusterDescriptor::get_chip_uid(chip_id_t chip_id) const {
    auto chip_uid_it = chip_id_to_chip_uid.find(chip_id);
    if (chip_uid_it == chip_id_to_chip_uid.end()) {
        return std::nullopt;
    }
    return chip_uid_it->second;
}

std::string tt_ClusterDescriptor::serialize() const {
    YAML::Emitter out;

    out << YAML::BeginMap;

    out << YAML::Key << "arch" << YAML::Value << YAML::BeginMap;
    for (const auto &[chip_id, arch] : chip_arch) {
        out << YAML::Key << chip_id << YAML::Value << tt::arch_to_str(arch);
    }
    out << YAML::EndMap;

    out << YAML::Key << "chips" << YAML::Value << YAML::BeginMap;
    for (const auto &[chip_id, chip_location] : chip_locations) {
        out << YAML::Key << chip_id << YAML::Value << YAML::BeginSeq << chip_location.x << chip_location.y
            << chip_location.rack << chip_location.shelf << YAML::EndSeq;
    }
    out << YAML::EndMap;

    out << YAML::Key << "ethernet_connections" << YAML::Value << YAML::BeginSeq;
    std::set<std::pair<chip_id_t, int>> serialized_connections;
    for (const auto &[src_chip, channels] : ethernet_connections) {
        for (const auto &[src_chan, dest] : channels) {
            if (serialized_connections.find({src_chip, src_chan}) != serialized_connections.end()) {
                continue;
            }
            auto [dest_chip, dest_chan] = dest;
            serialized_connections.insert({dest_chip, dest_chan});
            out << YAML::BeginSeq;
            out << YAML::BeginMap << YAML::Key << "chip" << YAML::Value << src_chip << YAML::Key << "chan"
                << YAML::Value << src_chan << YAML::EndMap;
            out << YAML::BeginMap << YAML::Key << "chip" << YAML::Value << dest_chip << YAML::Key << "chan"
                << YAML::Value << dest_chan << YAML::EndMap;
            out << YAML::EndSeq;
        }
    }
    out << YAML::EndSeq;

    out << YAML::Key << "chips_with_mmio" << YAML::Value << YAML::BeginSeq;
    for (const auto &chip_with_mmio : chips_with_mmio) {
        out << YAML::BeginMap << YAML::Key << chip_with_mmio.first << YAML::Value << chip_with_mmio.second
            << YAML::EndMap;
    }
    out << YAML::EndSeq;

    out << YAML::Key << "harvesting" << YAML::Value << YAML::BeginMap;
    for (const int &chip : all_chips) {
        out << YAML::Key << chip << YAML::Value << YAML::BeginMap;
        out << YAML::Key << "noc_translation" << YAML::Value << noc_translation_enabled.at(chip);
        out << YAML::Key << "harvest_mask" << YAML::Value << harvesting_masks.at(chip);
        out << YAML::Key << "dram_harvesting_mask" << YAML::Value << get_dram_harvesting_mask(chip);
        out << YAML::Key << "eth_harvesting_mask" << YAML::Value << get_eth_harvesting_mask(chip);
        out << YAML::Key << "pcie_harvesting_mask" << YAML::Value << get_pcie_harvesting_mask(chip);
        out << YAML::EndMap;
    }
    out << YAML::EndMap;

    out << YAML::Key << "chip_to_boardtype" << YAML::Value << YAML::BeginMap;
    for (const int &chip : all_chips) {
        out << YAML::Key << chip << YAML::Value << board_type_to_string(chip_board_type.at(chip));
    }
    out << YAML::EndMap;

    out << YAML::Key << "boards" << YAML::Value << YAML::BeginSeq;
    for (const auto &[board_id, chips] : board_to_chips) {
        out << YAML::BeginSeq;
        out << YAML::BeginMap << YAML::Key << "board_id" << YAML::Value << board_id << YAML::EndMap;
        out << YAML::BeginMap << YAML::Key << "board_type" << YAML::Value
            << board_type_to_string(get_board_type_from_board_id(board_id)) << YAML::EndMap;

        out << YAML::BeginMap << YAML::Key << "chips" << YAML::Value;
        out << YAML::BeginSeq;
        for (const auto &chip_id : chips) {
            out << chip_id;
        }
        out << YAML::EndSeq;
        out << YAML::EndMap;

        out << YAML::EndSeq;
    }
    out << YAML::EndSeq;

    out << YAML::EndMap;

    return out.c_str();
}

std::filesystem::path tt_ClusterDescriptor::serialize_to_file(const std::filesystem::path &dest_file) const {
    std::filesystem::path file_path = dest_file;
    if (file_path.empty()) {
        file_path = get_default_cluster_descriptor_file_path();
    }
    std::ofstream file(file_path);
    file << serialize();
    file.close();
    return file_path;
}

std::filesystem::path tt_ClusterDescriptor::get_default_cluster_descriptor_file_path() {
    std::filesystem::path temp_path = std::filesystem::temp_directory_path();
    std::string cluster_path_dir_template = temp_path / "umd_XXXXXX";
    std::filesystem::path cluster_path_dir = mkdtemp(cluster_path_dir_template.data());
    std::filesystem::path cluster_path = cluster_path_dir / "cluster_descriptor.yaml";

    return cluster_path;
}

std::set<uint32_t> tt_ClusterDescriptor::get_active_eth_channels(chip_id_t chip_id) {
    auto it = active_eth_channels.find(chip_id);
    if (it == active_eth_channels.end()) {
        return {};
    }

    return it->second;
}

std::set<uint32_t> tt_ClusterDescriptor::get_idle_eth_channels(chip_id_t chip_id) {
    auto it = idle_eth_channels.find(chip_id);
    if (it == idle_eth_channels.end()) {
        return {};
    }

    return it->second;
}

uint32_t tt_ClusterDescriptor::get_dram_harvesting_mask(chip_id_t chip_id) const {
    auto it = dram_harvesting_masks.find(chip_id);
    if (it == dram_harvesting_masks.end()) {
        return 0;
    }

    return it->second;
}

uint32_t tt_ClusterDescriptor::get_eth_harvesting_mask(chip_id_t chip_id) const {
    auto it = eth_harvesting_masks.find(chip_id);
    if (it == eth_harvesting_masks.end()) {
        return 0;
    }

    return it->second;
}

uint32_t tt_ClusterDescriptor::get_pcie_harvesting_mask(chip_id_t chip_id) const {
    auto it = pcie_harvesting_masks.find(chip_id);
    if (it == pcie_harvesting_masks.end()) {
        return 0;
    }

    return it->second;
}

void tt_ClusterDescriptor::add_chip_to_board(chip_id_t chip_id, uint64_t board_id) {
    if (chip_to_board_id.find(chip_id) != chip_to_board_id.end() && chip_to_board_id[chip_id] != board_id) {
        throw std::runtime_error(
            fmt::format("Chip {} is already mapped to board {:#x}", chip_id, chip_to_board_id[chip_id]));
    }
    chip_to_board_id[chip_id] = board_id;
    board_to_chips[board_id].insert(chip_id);
}

uint64_t tt_ClusterDescriptor::get_board_id_for_chip(const chip_id_t chip) const {
    auto it = chip_to_board_id.find(chip);
    if (it != chip_to_board_id.end()) {
        return it->second;
    }
    throw std::runtime_error(fmt::format("Chip to board mapping for chip {} not found.", chip));
}

std::unordered_set<chip_id_t> tt_ClusterDescriptor::get_board_chips(const uint64_t board_id) const {
    auto it = board_to_chips.find(board_id);
    if (it != board_to_chips.end()) {
        return it->second;
    }
    throw std::runtime_error(fmt::format("Board to chips mapping for board {:#x} not found.", board_id));
}

/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#include "umd/device/topology_discovery.h"

#include <tt-logger/tt-logger.hpp>

#include "umd/device/chip/local_chip.h"
#include "umd/device/chip/remote_chip.h"
#include "umd/device/remote_communication.h"
#include "umd/device/tt_cluster_descriptor.h"
#include "umd/device/tt_device/remote_wormhole_tt_device.h"
#include "umd/device/types/cluster_types.h"
#include "umd/device/types/wormhole_telemetry.h"
#include "umd/device/wormhole_implementation.h"

extern bool umd_use_noc1;

namespace tt::umd {

TopologyDiscovery::TopologyDiscovery(std::unordered_set<chip_id_t> pci_target_devices) :
    pci_target_devices(pci_target_devices) {}

std::unique_ptr<tt_ClusterDescriptor> TopologyDiscovery::create_ethernet_map() {
    cluster_desc = std::unique_ptr<tt_ClusterDescriptor>(new tt_ClusterDescriptor());
    get_pcie_connected_chips();
    discover_remote_chips();
    fill_cluster_descriptor_info();
    return std::move(cluster_desc);
}

TopologyDiscovery::EthAddresses TopologyDiscovery::get_eth_addresses(uint32_t eth_fw_version) {
    uint32_t masked_version = eth_fw_version & 0x00FFFFFF;

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

    if (masked_version >= 0x060000) {
        boot_params = 0x1000;
        node_info = 0x1100;
        eth_conn_info = 0x1200;
        debug_buf = 0x12c0;
        results_buf = 0x1ec0;
        shelf_rack_routing = true;

        version = 0x210;
        heartbeat = 0x1c;
        erisc_app = 0x9040;
        erisc_app_config = 0x12000;
    } else {
        throw std::runtime_error(
            fmt::format("Unsupported ETH version {:#x}. ETH version should always be at least 6.0.0.", eth_fw_version));
    }

    if (masked_version >= 0x06C000) {
        erisc_remote_board_type_offset = 77;
        erisc_local_board_type_offset = 69;
        erisc_remote_board_id_lo_offset = 72;
        erisc_local_board_id_lo_offset = 64;
    } else {
        erisc_remote_board_type_offset = 72;
        erisc_local_board_type_offset = 64;
        erisc_remote_board_id_lo_offset = 73;
        erisc_local_board_id_lo_offset = 65;
    }

    return TopologyDiscovery::EthAddresses{
        masked_version,
        version,
        boot_params,
        node_info,
        eth_conn_info,
        debug_buf,
        results_buf,
        shelf_rack_routing,
        heartbeat,
        erisc_app,
        erisc_app_config,
        erisc_remote_board_type_offset,
        erisc_local_board_type_offset,
        erisc_local_board_id_lo_offset,
        erisc_remote_board_id_lo_offset};
}

void TopologyDiscovery::get_pcie_connected_chips() {
    std::vector<int> pci_device_ids = PCIDevice::enumerate_devices();

    chip_id = 0;
    for (auto& device_id : pci_device_ids) {
        if (!is_pcie_chip_id_included(device_id)) {
            continue;
        }
        std::unique_ptr<LocalChip> chip = nullptr;
        chip = std::make_unique<LocalChip>(TTDevice::create(device_id));

        // ETH addresses need to be initialized after the first chip is created, so we could
        // read the information about offsets of board IDs on ETH core.
        // TODO: confirm that we should only support one set of addresses so we can remove
        // figuring out ETH addresses from runtime and move it to constants.
        if (chip_id == 0) {
            eth_addresses = TopologyDiscovery::get_eth_addresses(
                chip->get_tt_device()->get_arc_telemetry_reader()->read_entry(wormhole::TAG_ETH_FW_VERSION));
        }

        std::vector<CoreCoord> eth_cores =
            chip->get_soc_descriptor().get_cores(CoreType::ETH, umd_use_noc1 ? CoordSystem::NOC1 : CoordSystem::NOC0);
        for (const CoreCoord& eth_core : eth_cores) {
            uint32_t board_id = get_local_board_id(chip.get(), eth_core);
            if (board_id == 0) {
                continue;
            }
            board_ids.insert(board_id);
        }
        chips.emplace(chip_id, std::move(chip));
        chip_id++;
    }
}

void TopologyDiscovery::discover_remote_chips() {
    const uint32_t eth_unknown = 0;
    const uint32_t eth_unconnected = 1;
    const uint32_t shelf_offset = 9;
    const uint32_t rack_offset = 10;

    std::unordered_map<uint64_t, chip_id_t> chip_uid_to_local_chip_id = {};

    std::unordered_set<UniqueCoord> discovered_chips = {};
    std::unordered_set<UniqueCoord> remote_chips_to_discover = {};
    // Needed to know which chip to use for remote communication.
    std::unordered_map<UniqueCoord, chip_id_t> remote_unique_coord_to_mmio_chip_id = {};

    for (const auto& [chip_id, chip] : chips) {
        std::vector<CoreCoord> eth_cores =
            chip->get_soc_descriptor().get_cores(CoreType::ETH, umd_use_noc1 ? CoordSystem::NOC1 : CoordSystem::NOC0);
        TTDevice* tt_device = chip->get_tt_device();

        uint32_t current_chip_eth_coord_info;
        tt_device->read_from_device(
            &current_chip_eth_coord_info, eth_cores[0], eth_addresses.node_info + 8, sizeof(uint32_t));

        UniqueCoord current_chip_unique_coord;
        current_chip_unique_coord.board_id = tt_device->get_board_id();
        current_chip_unique_coord.eth_coord.cluster_id = 0;
        current_chip_unique_coord.eth_coord.x = (current_chip_eth_coord_info >> 16) & 0xFF;
        current_chip_unique_coord.eth_coord.y = (current_chip_eth_coord_info >> 24) & 0xFF;
        current_chip_unique_coord.eth_coord.rack = current_chip_eth_coord_info & 0xFF;
        current_chip_unique_coord.eth_coord.shelf = (current_chip_eth_coord_info >> 8) & 0xFF;

        eth_coords.emplace(chip_id, current_chip_unique_coord.eth_coord);
        unique_coord_to_chip_id.emplace(current_chip_unique_coord, chip_id);

        discovered_chips.insert(current_chip_unique_coord);
    }

    for (const auto& [chip_id, chip] : chips) {
        std::vector<CoreCoord> eth_cores =
            chip->get_soc_descriptor().get_cores(CoreType::ETH, umd_use_noc1 ? CoordSystem::NOC1 : CoordSystem::NOC0);
        TTDevice* tt_device = chip->get_tt_device();

        uint32_t current_chip_eth_coord_info;
        tt_device->read_from_device(
            &current_chip_eth_coord_info, eth_cores[0], eth_addresses.node_info + 8, sizeof(uint32_t));

        UniqueCoord current_chip_unique_coord;
        current_chip_unique_coord.board_id = tt_device->get_board_id();
        current_chip_unique_coord.eth_coord.cluster_id = 0;
        current_chip_unique_coord.eth_coord.x = (current_chip_eth_coord_info >> 16) & 0xFF;
        current_chip_unique_coord.eth_coord.y = (current_chip_eth_coord_info >> 24) & 0xFF;
        current_chip_unique_coord.eth_coord.rack = current_chip_eth_coord_info & 0xFF;
        current_chip_unique_coord.eth_coord.shelf = (current_chip_eth_coord_info >> 8) & 0xFF;

        std::set<uint32_t> active_eth_channels;

        uint32_t channel = 0;
        for (const CoreCoord& eth_core : eth_cores) {
            uint32_t port_status;
            tt_device->read_from_device(
                &port_status,
                tt_cxy_pair(chip_id, eth_core.x, eth_core.y),
                eth_addresses.eth_conn_info + (channel * 4),
                sizeof(uint32_t));

            if (port_status == eth_unknown || port_status == eth_unconnected) {
                channel++;
                continue;
            }

            if (!is_board_id_included(get_remote_board_id(chip.get(), eth_core))) {
                channel++;
                continue;
            }

            active_eth_channels.insert(channel);

            uint32_t remote_id;
            tt_device->read_from_device(
                &remote_id, {eth_core.x, eth_core.y}, eth_addresses.node_info + (4 * rack_offset), sizeof(uint32_t));

            uint32_t remote_rack_x = remote_id & 0xFF;
            uint32_t remote_rack_y = (remote_id >> 8) & 0xFF;

            tt_device->read_from_device(
                &remote_id, {eth_core.x, eth_core.y}, eth_addresses.node_info + (4 * shelf_offset), sizeof(uint32_t));

            uint32_t remote_shelf_x = (remote_id >> 16) & 0x3F;
            uint32_t remote_shelf_y = (remote_id >> 22) & 0x3F;

            uint32_t remote_noc_x = (remote_id >> 4) & 0x3F;
            uint32_t remote_noc_y = (remote_id >> 10) & 0x3F;

            UniqueCoord unique_coord;
            unique_coord.eth_coord.cluster_id = 0;
            unique_coord.eth_coord.x = remote_shelf_x;
            unique_coord.eth_coord.y = remote_shelf_y;
            unique_coord.eth_coord.rack = remote_rack_x;
            unique_coord.eth_coord.shelf = remote_rack_y;

            chip->set_remote_transfer_ethernet_cores(active_eth_channels);
            std::unique_ptr<RemoteWormholeTTDevice> remote_tt_device =
                std::make_unique<RemoteWormholeTTDevice>(dynamic_cast<LocalChip*>(chip.get()), unique_coord.eth_coord);

            unique_coord.board_id = remote_tt_device->get_board_id();

            if (discovered_chips.find(unique_coord) == discovered_chips.end()) {
                remote_chips_to_discover.insert(unique_coord);
                remote_unique_coord_to_mmio_chip_id.emplace(unique_coord, chip_id);
            } else {
                chip_id_t current_chip_id = unique_coord_to_chip_id.at(current_chip_unique_coord);
                chip_id_t remote_chip_id = unique_coord_to_chip_id.at(unique_coord);
                Chip* remote_chip = chips.at(remote_chip_id).get();
                CoreCoord physical_remote_eth =
                    CoreCoord(remote_noc_x, remote_noc_y, CoreType::ETH, CoordSystem::PHYSICAL);
                CoreCoord logical_remote_eth =
                    remote_chip->get_soc_descriptor().translate_coord_to(physical_remote_eth, CoordSystem::LOGICAL);
                ethernet_connections.push_back({{current_chip_id, channel}, {remote_chip_id, logical_remote_eth.y}});
            }
            channel++;
        }
        chip->set_remote_transfer_ethernet_cores(active_eth_channels);
    }

    if (remote_chips_to_discover.empty()) {
        return;
    }

    while (!remote_chips_to_discover.empty()) {
        std::unordered_set<UniqueCoord> new_remote_chips = {};

        for (const UniqueCoord& unique_coord : remote_chips_to_discover) {
            chip_id_t mmio_chip_id = remote_unique_coord_to_mmio_chip_id.at(unique_coord);
            Chip* mmio_chip = chips.at(mmio_chip_id).get();
            TTDevice* tt_device = mmio_chip->get_tt_device();
            std::unique_ptr<RemoteCommunication> remote_comm =
                std::make_unique<RemoteCommunication>(dynamic_cast<LocalChip*>(mmio_chip));

            std::vector<CoreCoord> eth_cores = mmio_chip->get_soc_descriptor().get_cores(
                CoreType::ETH, umd_use_noc1 ? CoordSystem::NOC1 : CoordSystem::NOC0);

            uint32_t current_chip_eth_coord_info;

            std::unique_ptr<RemoteWormholeTTDevice> remote_tt_device =
                std::make_unique<RemoteWormholeTTDevice>(dynamic_cast<LocalChip*>(mmio_chip), unique_coord.eth_coord);

            remote_tt_device->read_from_device(
                &current_chip_eth_coord_info, eth_cores[0], eth_addresses.node_info + 8, sizeof(uint32_t));

            UniqueCoord current_chip_unique_coord;
            current_chip_unique_coord.board_id = remote_tt_device->get_board_id();
            current_chip_unique_coord.eth_coord.cluster_id = 0;
            current_chip_unique_coord.eth_coord.x = (current_chip_eth_coord_info >> 16) & 0xFF;
            current_chip_unique_coord.eth_coord.y = (current_chip_eth_coord_info >> 24) & 0xFF;
            current_chip_unique_coord.eth_coord.rack = current_chip_eth_coord_info & 0xFF;
            current_chip_unique_coord.eth_coord.shelf = (current_chip_eth_coord_info >> 8) & 0xFF;

            discovered_chips.insert(current_chip_unique_coord);

            ChipInfo chip_info = remote_tt_device->get_chip_info();

            std::unique_ptr<RemoteChip> chip = nullptr;
            chip = std::make_unique<RemoteChip>(
                tt_SocDescriptor(
                    tt_device->get_arch(),
                    chip_info.noc_translation_enabled,
                    chip_info.harvesting_masks,
                    chip_info.board_type),
                std::move(remote_tt_device));

            chips.emplace(chip_id, std::move(chip));
            eth_coords.emplace(chip_id, current_chip_unique_coord.eth_coord);
            unique_coord_to_chip_id.emplace(current_chip_unique_coord, chip_id);
            chip_id++;

            uint32_t channel = 0;
            for (const CoreCoord& eth_core : eth_cores) {
                uint32_t port_status;
                remote_comm->read_non_mmio(
                    unique_coord.eth_coord,
                    tt_xy_pair(eth_core.x, eth_core.y),
                    &port_status,
                    eth_addresses.eth_conn_info + (channel * 4),
                    sizeof(uint32_t));

                if (port_status == eth_unknown || port_status == eth_unconnected) {
                    channel++;
                    continue;
                }

                if (!is_board_id_included(get_remote_board_id(chips.at(chip_id - 1).get(), eth_core))) {
                    channel++;
                    continue;
                }

                uint32_t remote_id;
                remote_comm->read_non_mmio(
                    unique_coord.eth_coord,
                    {eth_core.x, eth_core.y},
                    &remote_id,
                    eth_addresses.node_info + (4 * rack_offset),
                    sizeof(uint32_t));

                uint32_t remote_rack_x = remote_id & 0xFF;
                uint32_t remote_rack_y = (remote_id >> 8) & 0xFF;

                remote_comm->read_non_mmio(
                    unique_coord.eth_coord,
                    {eth_core.x, eth_core.y},
                    &remote_id,
                    eth_addresses.node_info + (4 * shelf_offset),
                    sizeof(uint32_t));

                uint32_t remote_shelf_x = (remote_id >> 16) & 0x3F;
                uint32_t remote_shelf_y = (remote_id >> 22) & 0x3F;

                uint32_t remote_noc_x = (remote_id >> 4) & 0x3F;
                uint32_t remote_noc_y = (remote_id >> 10) & 0x3F;

                UniqueCoord new_unique_coord;
                new_unique_coord.eth_coord.cluster_id = 0;
                new_unique_coord.eth_coord.x = remote_shelf_x;
                new_unique_coord.eth_coord.y = remote_shelf_y;
                new_unique_coord.eth_coord.rack = remote_rack_x;
                new_unique_coord.eth_coord.shelf = remote_rack_y;

                std::unique_ptr<RemoteWormholeTTDevice> new_remote_tt_device = std::make_unique<RemoteWormholeTTDevice>(
                    dynamic_cast<LocalChip*>(mmio_chip), new_unique_coord.eth_coord);

                new_unique_coord.board_id = new_remote_tt_device->get_board_id();

                if (discovered_chips.find(new_unique_coord) == discovered_chips.end()) {
                    if (remote_chips_to_discover.find(new_unique_coord) == remote_chips_to_discover.end()) {
                        new_remote_chips.insert(new_unique_coord);
                        remote_unique_coord_to_mmio_chip_id.emplace(new_unique_coord, mmio_chip_id);
                    }
                } else {
                    chip_id_t current_chip_id = unique_coord_to_chip_id.at(current_chip_unique_coord);
                    chip_id_t remote_chip_id = unique_coord_to_chip_id.at(new_unique_coord);
                    Chip* remote_chip = chips.at(remote_chip_id).get();
                    CoreCoord physical_remote_eth =
                        CoreCoord(remote_noc_x, remote_noc_y, CoreType::ETH, CoordSystem::PHYSICAL);
                    CoreCoord logical_remote_eth =
                        remote_chip->get_soc_descriptor().translate_coord_to(physical_remote_eth, CoordSystem::LOGICAL);
                    ethernet_connections.push_back(
                        {{current_chip_id, channel}, {remote_chip_id, logical_remote_eth.y}});
                }

                channel++;
            }
        }

        remote_chips_to_discover = new_remote_chips;
    }
}

void TopologyDiscovery::fill_cluster_descriptor_info() {
    for (const auto& [chip_id, chip] : chips) {
        cluster_desc->all_chips.insert(chip_id);
        cluster_desc->chip_arch.insert({chip_id, tt::ARCH::WORMHOLE_B0});

        if (chip->is_mmio_capable()) {
            cluster_desc->chips_with_mmio.insert({chip_id, chip->get_tt_device()->get_pci_device()->get_device_num()});
        }

        cluster_desc->chip_board_type.insert({chip_id, chip->get_chip_info().board_type});

        cluster_desc->noc_translation_enabled.insert({chip_id, chip->get_chip_info().noc_translation_enabled});
        cluster_desc->harvesting_masks.insert({chip_id, chip->get_chip_info().harvesting_masks.tensix_harvesting_mask});
        cluster_desc->dram_harvesting_masks.insert(
            {chip_id, chip->get_chip_info().harvesting_masks.dram_harvesting_mask});
        cluster_desc->eth_harvesting_masks.insert(
            {chip_id, chip->get_chip_info().harvesting_masks.eth_harvesting_mask});
        eth_coord_t eth_coord = eth_coords.at(chip_id);
        cluster_desc->chip_locations.insert({chip_id, eth_coord});
        cluster_desc->coords_to_chip_ids[eth_coord.rack][eth_coord.shelf][eth_coord.y][eth_coord.x] = chip_id;

        cluster_desc->add_chip_to_board(chip_id, chip->get_chip_info().chip_uid.board_id);

        for (int i = 0; i < wormhole::NUM_ETH_CHANNELS; i++) {
            cluster_desc->idle_eth_channels[chip_id].insert(i);
        }
    }

    for (auto [ethernet_connection_logical, ethernet_connection_remote] : ethernet_connections) {
        cluster_desc->ethernet_connections[ethernet_connection_logical.first][ethernet_connection_logical.second] = {
            ethernet_connection_remote.first, ethernet_connection_remote.second};
        cluster_desc->ethernet_connections[ethernet_connection_remote.first][ethernet_connection_remote.second] = {
            ethernet_connection_logical.first, ethernet_connection_logical.second};
        cluster_desc->active_eth_channels[ethernet_connection_logical.first].insert(ethernet_connection_logical.second);
        cluster_desc->idle_eth_channels[ethernet_connection_logical.first].erase(ethernet_connection_logical.second);
        cluster_desc->active_eth_channels[ethernet_connection_remote.first].insert(ethernet_connection_remote.second);
        cluster_desc->idle_eth_channels[ethernet_connection_remote.first].erase(ethernet_connection_remote.second);
    }

    tt_ClusterDescriptor::fill_galaxy_connections(*cluster_desc.get());
    tt_ClusterDescriptor::merge_cluster_ids(*cluster_desc.get());

    cluster_desc->fill_chips_grouped_by_closest_mmio();
}

// If pci_target_devices is empty, we should take all the PCI devices found in the system.
// That is why we have the first part of the condition.
bool TopologyDiscovery::is_pcie_chip_id_included(int pci_id) const {
    return pci_target_devices.empty() || pci_target_devices.find(pci_id) != pci_target_devices.end();
}

// If pci_target_devices is empty, we should take all the PCI devices found in the system.
// That is why we have the first part of the condition.
bool TopologyDiscovery::is_board_id_included(uint32_t board_id) const {
    return pci_target_devices.empty() || board_ids.find(board_id) != board_ids.end();
}

uint32_t TopologyDiscovery::get_remote_board_id(Chip* chip, tt_xy_pair eth_core) {
    TTDevice* tt_device = chip->get_tt_device();
    uint32_t board_id;
    tt_device->read_from_device(
        &board_id,
        eth_core,
        eth_addresses.results_buf + (4 * eth_addresses.erisc_remote_board_id_lo_offset),
        sizeof(uint32_t));
    return board_id;
}

uint32_t TopologyDiscovery::get_local_board_id(Chip* chip, tt_xy_pair eth_core) {
    TTDevice* tt_device = chip->get_tt_device();
    uint32_t board_id;
    tt_device->read_from_device(
        &board_id,
        eth_core,
        eth_addresses.results_buf + (4 * eth_addresses.erisc_local_board_id_lo_offset),
        sizeof(uint32_t));
    return board_id;
}

}  // namespace tt::umd

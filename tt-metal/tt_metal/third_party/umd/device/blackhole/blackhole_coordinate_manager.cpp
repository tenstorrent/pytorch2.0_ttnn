/*
 * SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#include "umd/device/blackhole_coordinate_manager.h"

#include <tt-logger/tt-logger.hpp>

using namespace tt::umd;

BlackholeCoordinateManager::BlackholeCoordinateManager(
    const bool noc_translation_enabled,
    HarvestingMasks harvesting_masks,
    const tt_xy_pair& tensix_grid_size,
    const std::vector<tt_xy_pair>& tensix_cores,
    const tt_xy_pair& dram_grid_size,
    const std::vector<tt_xy_pair>& dram_cores,
    const std::vector<tt_xy_pair>& eth_cores,
    const tt_xy_pair& arc_grid_size,
    const std::vector<tt_xy_pair>& arc_cores,
    const tt_xy_pair& pcie_grid_size,
    const std::vector<tt_xy_pair>& pcie_cores,
    const std::vector<tt_xy_pair>& router_cores,
    const std::vector<tt_xy_pair>& security_cores,
    const std::vector<tt_xy_pair>& l2cpu_cores,
    const std::vector<uint32_t>& noc0_x_to_noc1_x,
    const std::vector<uint32_t>& noc0_y_to_noc1_y) :
    CoordinateManager(
        noc_translation_enabled,
        harvesting_masks,
        tensix_grid_size,
        tensix_cores,
        dram_grid_size,
        dram_cores,
        eth_cores,
        arc_grid_size,
        arc_cores,
        pcie_grid_size,
        pcie_cores,
        router_cores,
        security_cores,
        l2cpu_cores,
        noc0_x_to_noc1_x,
        noc0_y_to_noc1_y) {
    initialize();
}

void BlackholeCoordinateManager::assert_coordinate_manager_constructor() {
    if (get_num_harvested(harvesting_masks.dram_harvesting_mask) > 1) {
        throw std::runtime_error("Only one DRAM bank can be harvested on Blackhole");
    }

    // TODO: assert that exactly 2 or all 14 (P100) ETH cores are harvested for Blackhole. This is
    // going to be true both for all Blackhole products.
    // const size_t num_harvested_eth_cores = get_num_harvested(harvesting_masks.eth_harvesting_mask);
    // TT_ASSERT(
    //     num_harvested_eth_cores == 2 || num_harvested_eth_cores == blackhole::ETH_GRID_SIZE.x, "Exactly 2 or 14 ETH
    //     cores should be harvested on Blackhole");
}

void BlackholeCoordinateManager::translate_tensix_coords() {
    if (CoordinateManager::get_num_harvested(harvesting_masks.tensix_harvesting_mask) > tensix_grid_size.x) {
        harvesting_masks.tensix_harvesting_mask = 0;
    }
    size_t num_harvested_x = CoordinateManager::get_num_harvested(harvesting_masks.tensix_harvesting_mask);
    size_t grid_size_x = tensix_grid_size.x;
    size_t grid_size_y = tensix_grid_size.y;

    size_t logical_x = 0;
    std::vector<std::pair<size_t, size_t>> die_harvested_tensix_columns;
    for (size_t x = 0; x < grid_size_x; x++) {
        if (harvesting_masks.tensix_harvesting_mask & (1 << x)) {
            const tt_xy_pair& physical_core = tensix_cores[x];
            const size_t die_x_index = std::find(
                                           tt::umd::blackhole::HARVESTING_NOC_LOCATIONS.begin(),
                                           tt::umd::blackhole::HARVESTING_NOC_LOCATIONS.end(),
                                           physical_core.x) -
                                       tt::umd::blackhole::HARVESTING_NOC_LOCATIONS.begin();
            die_harvested_tensix_columns.push_back(std::make_pair(die_x_index, x));
        } else {
            for (size_t y = 0; y < grid_size_y; y++) {
                const tt_xy_pair& tensix_core = tensix_cores[x + y * grid_size_x];
                const tt_xy_pair& virtual_core = tensix_cores[logical_x + y * grid_size_x];

                CoreCoord logical_coord = CoreCoord(logical_x, y, CoreType::TENSIX, CoordSystem::LOGICAL);
                add_core_translation(logical_coord, tensix_core);

                CoreCoord virtual_coord =
                    CoreCoord(virtual_core.x, virtual_core.y, CoreType::TENSIX, CoordSystem::VIRTUAL);
                add_core_translation(virtual_coord, tensix_core);
            }
            logical_x++;
        }
    }

    std::sort(die_harvested_tensix_columns.begin(), die_harvested_tensix_columns.end());
    size_t x_index = grid_size_x - 1;
    for (const auto& [die_x_coordinate, x_index_harvested] : die_harvested_tensix_columns) {
        for (size_t y = 0; y < grid_size_y; y++) {
            const tt_xy_pair& physical_core = tensix_cores[x_index_harvested + y * grid_size_x];
            const tt_xy_pair& virtual_core = tensix_cores[x_index + y * grid_size_x];

            CoreCoord virtual_coord = CoreCoord(virtual_core.x, virtual_core.y, CoreType::TENSIX, CoordSystem::VIRTUAL);

            add_core_translation(virtual_coord, physical_core);
        }
        x_index--;
    }

    if (noc_translation_enabled) {
        fill_tensix_physical_translated_mapping();
    } else {
        fill_tensix_default_physical_translated_mapping();
    }
}

void BlackholeCoordinateManager::fill_tensix_physical_translated_mapping() {
    for (const tt_xy_pair& physical_core : tensix_cores) {
        const CoreCoord virtual_coord = from_physical_map.at({physical_core, CoordSystem::VIRTUAL});
        const CoreCoord translated_coord =
            CoreCoord(virtual_coord.x, virtual_coord.y, CoreType::TENSIX, CoordSystem::TRANSLATED);

        add_core_translation(translated_coord, physical_core);
    }
}

void BlackholeCoordinateManager::translate_dram_coords() {
    size_t num_harvested_banks = CoordinateManager::get_num_harvested(harvesting_masks.dram_harvesting_mask);

    size_t logical_x = 0;
    for (size_t x = 0; x < dram_grid_size.x; x++) {
        if (!(harvesting_masks.dram_harvesting_mask & (1 << x))) {
            for (size_t y = 0; y < dram_grid_size.y; y++) {
                const tt_xy_pair& dram_core = dram_cores[x * dram_grid_size.y + y];

                CoreCoord logical_coord = CoreCoord(logical_x, y, CoreType::DRAM, CoordSystem::LOGICAL);

                add_core_translation(logical_coord, dram_core);
            }
            logical_x++;
        }
    }

    for (size_t x = 0; x < dram_grid_size.x - num_harvested_banks; x++) {
        for (size_t y = 0; y < dram_grid_size.y; y++) {
            const tt_xy_pair& dram_core = dram_cores[x * dram_grid_size.y + y];
            CoreCoord dram_logical = CoreCoord(x, y, CoreType::DRAM, CoordSystem::LOGICAL);
            CoreCoord dram_virtual = CoreCoord(dram_core.x, dram_core.y, CoreType::DRAM, CoordSystem::VIRTUAL);

            const tt_xy_pair physical_pair = to_physical_map[dram_logical];

            add_core_translation(dram_virtual, physical_pair);
        }
    }

    size_t harvested_index = (dram_grid_size.x - num_harvested_banks) * dram_grid_size.y;
    for (size_t x = 0; x < dram_grid_size.x; x++) {
        if (harvesting_masks.dram_harvesting_mask & (1 << x)) {
            for (size_t y = 0; y < dram_grid_size.y; y++) {
                const tt_xy_pair& dram_core = dram_cores[x * dram_grid_size.y + y];
                const tt_xy_pair& virtual_core = dram_cores[harvested_index++];

                CoreCoord virtual_coord =
                    CoreCoord(virtual_core.x, virtual_core.y, CoreType::DRAM, CoordSystem::VIRTUAL);

                add_core_translation(virtual_coord, dram_core);
            }
        }
    }

    if (noc_translation_enabled) {
        fill_dram_physical_translated_mapping();
    } else {
        fill_dram_default_physical_translated_mapping();
    }
}

void BlackholeCoordinateManager::translate_eth_coords() {
    size_t num_harvested_channels = CoordinateManager::get_num_harvested(harvesting_masks.eth_harvesting_mask);

    size_t harvested_eth_channel_start = eth_cores.size() - num_harvested_channels;
    size_t unharvested_logical_eth_channel = 0;
    for (size_t eth_channel = 0; eth_channel < eth_cores.size(); eth_channel++) {
        if (harvesting_masks.eth_harvesting_mask & (1 << eth_channel)) {
            const tt_xy_pair& physical_core = eth_cores[eth_channel];
            const tt_xy_pair& virtual_core = eth_cores[harvested_eth_channel_start++];

            CoreCoord virtual_coord = CoreCoord(virtual_core.x, virtual_core.y, CoreType::ETH, CoordSystem::VIRTUAL);

            add_core_translation(virtual_coord, physical_core);
        } else {
            const tt_xy_pair& tensix_core = eth_cores[eth_channel];
            const tt_xy_pair& virtual_core = eth_cores[unharvested_logical_eth_channel];

            CoreCoord logical_coord =
                CoreCoord(0, unharvested_logical_eth_channel, CoreType::ETH, CoordSystem::LOGICAL);
            add_core_translation(logical_coord, tensix_core);

            CoreCoord virtual_coord = CoreCoord(virtual_core.x, virtual_core.y, CoreType::ETH, CoordSystem::VIRTUAL);
            add_core_translation(virtual_coord, tensix_core);
            unharvested_logical_eth_channel++;
        }
    }

    if (noc_translation_enabled) {
        fill_eth_physical_translated_mapping();
    } else {
        fill_eth_default_physical_translated_mapping();
    }
}

void BlackholeCoordinateManager::translate_pcie_coords() {
    size_t logical_x = 0;
    for (size_t x = 0; x < pcie_grid_size.x; x++) {
        if (harvesting_masks.pcie_harvesting_mask & (1 << x)) {
            for (size_t y = 0; y < pcie_grid_size.y; y++) {
                const tt_xy_pair& pcie_core = pcie_cores[x * pcie_grid_size.y + y];

                CoreCoord virtual_coord = CoreCoord(pcie_core.x, pcie_core.y, CoreType::PCIE, CoordSystem::VIRTUAL);
                add_core_translation(virtual_coord, pcie_core);
            }
        } else {
            for (size_t y = 0; y < pcie_grid_size.y; y++) {
                const tt_xy_pair& pcie_core = pcie_cores[x * pcie_grid_size.y + y];

                CoreCoord logical_coord = CoreCoord(logical_x, y, CoreType::PCIE, CoordSystem::LOGICAL);
                add_core_translation(logical_coord, pcie_core);

                CoreCoord virtual_coord = CoreCoord(pcie_core.x, pcie_core.y, CoreType::PCIE, CoordSystem::VIRTUAL);
                add_core_translation(virtual_coord, pcie_core);
            }
            logical_x++;
        }
    }

    if (noc_translation_enabled) {
        fill_pcie_physical_translated_mapping();
    } else {
        fill_pcie_default_physical_translated_mapping();
    }
}

void BlackholeCoordinateManager::fill_eth_physical_translated_mapping() {
    size_t num_harvested_channels = CoordinateManager::get_num_harvested(harvesting_masks.eth_harvesting_mask);
    if (eth_cores.size() == 0) {
        num_harvested_channels = 0;
    }
    for (size_t eth_channel = 0; eth_channel < eth_cores.size() - num_harvested_channels; eth_channel++) {
        const size_t translated_x = eth_channel + blackhole::eth_translated_coordinate_start_x;
        const size_t translated_y = blackhole::eth_translated_coordinate_start_y;

        CoreCoord logical_coord = CoreCoord(0, eth_channel, CoreType::ETH, CoordSystem::LOGICAL);
        const tt_xy_pair physical_pair = to_physical_map[logical_coord];

        CoreCoord translated_coord = CoreCoord(translated_x, translated_y, CoreType::ETH, CoordSystem::TRANSLATED);

        add_core_translation(translated_coord, physical_pair);
    }

    // Harvested ETH cores should be mapped to the same physical coordinates.
    for (size_t eth_channel = 0; eth_channel < eth_cores.size(); eth_channel++) {
        if (harvesting_masks.eth_harvesting_mask & (1 << eth_channel)) {
            const tt_xy_pair& physical_pair = eth_cores[eth_channel];
            const CoreCoord translated_coord =
                CoreCoord(physical_pair.x, physical_pair.y, CoreType::ETH, CoordSystem::TRANSLATED);

            add_core_translation(translated_coord, physical_pair);
        }
    }
}

void BlackholeCoordinateManager::fill_pcie_physical_translated_mapping() {
    for (size_t x = 0;
         x < pcie_grid_size.x - CoordinateManager::get_num_harvested(harvesting_masks.pcie_harvesting_mask);
         x++) {
        CoreCoord logical_coord = CoreCoord(x, 0, CoreType::PCIE, CoordSystem::LOGICAL);
        const tt_xy_pair physical_pair = to_physical_map[logical_coord];
        size_t translated_x = physical_pair.x;
        size_t translated_y = physical_pair.y;

        // Only the first PCIE core is mapped to the translated coordinates.
        // This is in case pcie harvesting mask is set to 0.
        // This should never happen on silicon.
        if (x == 0) {
            translated_x = blackhole::pcie_translated_coordinate_start_x;
            translated_y = blackhole::pcie_translated_coordinate_start_y;
        }

        CoreCoord translated_coord = CoreCoord(translated_x, translated_y, CoreType::PCIE, CoordSystem::TRANSLATED);

        add_core_translation(translated_coord, physical_pair);
    }

    for (size_t x = 0; x < pcie_grid_size.x; x++) {
        if (harvesting_masks.pcie_harvesting_mask & (1 << x)) {
            const tt_xy_pair physical_pair = pcie_cores[x];
            const size_t translated_x = physical_pair.x;
            const size_t translated_y = physical_pair.y;

            CoreCoord translated_coord = CoreCoord(translated_x, translated_y, CoreType::PCIE, CoordSystem::TRANSLATED);

            add_core_translation(translated_coord, physical_pair);
        }
    }
}

void BlackholeCoordinateManager::fill_arc_physical_translated_mapping() {
    // ARC cores are not translated in Blackhole.
    fill_arc_default_physical_translated_mapping();
}

void BlackholeCoordinateManager::map_dram_banks(
    const size_t start_bank, const size_t end_bank, const size_t x_coord, const size_t y_coord) {
    size_t translated_y = y_coord;
    for (size_t bank = start_bank; bank < end_bank; bank++) {
        for (size_t port = 0; port < blackhole::NUM_NOC_PORTS_PER_DRAM_BANK; port++) {
            CoreCoord logical_coord = CoreCoord(bank, port, CoreType::DRAM, CoordSystem::LOGICAL);
            const tt_xy_pair physical_pair = to_physical_map[logical_coord];

            CoreCoord translated_coord = CoreCoord(x_coord, translated_y, CoreType::DRAM, CoordSystem::TRANSLATED);

            add_core_translation(translated_coord, physical_pair);

            translated_y++;
        }
    }
}

void BlackholeCoordinateManager::fill_dram_physical_translated_mapping() {
    if (dram_grid_size.x < blackhole::NUM_DRAM_BANKS) {
        // If the number of DRAM banks is less than num dram banks for standard SOC for Blackhole,
        // map the translated DRAM cores to be the same as physical DRAM cores.
        // TODO: Figure out how DRAM is going to be mapped to translated coordinates when there is less DRAM banks.
        for (size_t x = 0; x < dram_grid_size.x; x++) {
            for (size_t y = 0; y < dram_grid_size.y; y++) {
                const CoreCoord logical_dram_core = CoreCoord(x, y, CoreType::DRAM, CoordSystem::LOGICAL);
                const tt_xy_pair physical_dram_core = to_physical_map[logical_dram_core];

                CoreCoord translated_dram_core =
                    CoreCoord(physical_dram_core.x, physical_dram_core.y, CoreType::DRAM, CoordSystem::TRANSLATED);
                to_physical_map[translated_dram_core] = physical_dram_core;
                from_physical_map[{{physical_dram_core.x, physical_dram_core.y}, CoordSystem::TRANSLATED}] =
                    translated_dram_core;
            }
        }
        return;
    }

    const std::vector<size_t> harvested_banks =
        CoordinateManager::get_harvested_indices(harvesting_masks.dram_harvesting_mask);

    if (harvested_banks.empty()) {
        map_dram_banks(0, blackhole::NUM_DRAM_BANKS / 2, blackhole::dram_translated_coordinate_start_x);
        map_dram_banks(
            blackhole::NUM_DRAM_BANKS / 2,
            blackhole::NUM_DRAM_BANKS,
            blackhole::dram_translated_coordinate_start_x + 1);
        return;
    }

    const size_t harvested_bank = harvested_banks[0];

    if (harvested_bank < blackhole::NUM_DRAM_BANKS / 2) {
        const size_t mirror_east_bank = harvested_bank + blackhole::NUM_DRAM_BANKS / 2 - 1;

        // Map west column of DRAM banks.
        map_dram_banks(0, blackhole::NUM_DRAM_BANKS / 2 - 1, blackhole::dram_translated_coordinate_start_x + 1);

        // Map east column of DRAM banks.
        map_dram_banks(
            blackhole::NUM_DRAM_BANKS / 2 - 1, mirror_east_bank, blackhole::dram_translated_coordinate_start_x);

        map_dram_banks(
            mirror_east_bank + 1,
            blackhole::NUM_DRAM_BANKS - 1,
            blackhole::dram_translated_coordinate_start_x,
            blackhole::dram_translated_coordinate_start_y +
                (mirror_east_bank - (blackhole::NUM_DRAM_BANKS / 2 - 1)) * blackhole::NUM_NOC_PORTS_PER_DRAM_BANK);

        map_dram_banks(
            mirror_east_bank,
            mirror_east_bank + 1,
            blackhole::dram_translated_coordinate_start_x,
            blackhole::dram_translated_coordinate_start_y +
                (blackhole::NUM_DRAM_BANKS / 2 - 1) * blackhole::NUM_NOC_PORTS_PER_DRAM_BANK);
    } else {
        const size_t mirror_west_bank = harvested_bank - blackhole::NUM_DRAM_BANKS / 2;

        // Map west column of DRAM banks.
        map_dram_banks(0, mirror_west_bank, blackhole::dram_translated_coordinate_start_x);

        map_dram_banks(
            mirror_west_bank + 1,
            blackhole::NUM_DRAM_BANKS / 2,
            blackhole::dram_translated_coordinate_start_x,
            blackhole::dram_translated_coordinate_start_y + mirror_west_bank * blackhole::NUM_NOC_PORTS_PER_DRAM_BANK);

        map_dram_banks(
            mirror_west_bank,
            mirror_west_bank + 1,
            blackhole::dram_translated_coordinate_start_x,
            blackhole::dram_translated_coordinate_start_y +
                (blackhole::NUM_DRAM_BANKS / 2 - 1) * blackhole::NUM_NOC_PORTS_PER_DRAM_BANK);

        // Map east column of DRAM banks.
        map_dram_banks(
            blackhole::NUM_DRAM_BANKS / 2,
            blackhole::NUM_DRAM_BANKS - 1,
            blackhole::dram_translated_coordinate_start_x + 1);
    }

    const size_t virtual_index = (dram_grid_size.x - 1) * dram_grid_size.y;
    const size_t physical_index = harvested_bank * dram_grid_size.y;

    const size_t harvested_bank_translated_x = blackhole::dram_translated_coordinate_start_x + 1;
    const size_t harvested_bank_translated_y =
        blackhole::dram_translated_coordinate_start_y + (dram_grid_size.x / 2 - 1) * dram_grid_size.y;

    for (size_t noc_port = 0; noc_port < dram_grid_size.y; noc_port++) {
        const tt_xy_pair& physical_core = dram_cores[physical_index + noc_port];
        const tt_xy_pair& virtual_core = dram_cores[virtual_index + noc_port];

        CoreCoord virtual_coord = CoreCoord(virtual_core.x, virtual_core.y, CoreType::DRAM, CoordSystem::VIRTUAL);

        add_core_translation(virtual_coord, physical_core);

        CoreCoord translated_coord = CoreCoord(
            harvested_bank_translated_x,
            harvested_bank_translated_y + noc_port,
            CoreType::DRAM,
            CoordSystem::TRANSLATED);

        add_core_translation(translated_coord, physical_core);
    }
}

std::vector<CoreCoord> BlackholeCoordinateManager::get_tensix_cores() const {
    std::vector<size_t> harvested_x_coords = get_harvested_indices(harvesting_masks.tensix_harvesting_mask);
    std::vector<CoreCoord> unharvested_tensix_cores;
    for (size_t y = 0; y < tensix_grid_size.y; y++) {
        for (size_t x = 0; x < tensix_grid_size.x; x++) {
            const tt_xy_pair core = tensix_cores[y * tensix_grid_size.x + x];
            CoreCoord core_coord(core.x, core.y, CoreType::TENSIX, CoordSystem::PHYSICAL);
            if (std::find(harvested_x_coords.begin(), harvested_x_coords.end(), x) == harvested_x_coords.end()) {
                unharvested_tensix_cores.push_back(core_coord);
            }
        }
    }
    return unharvested_tensix_cores;
}

std::vector<CoreCoord> BlackholeCoordinateManager::get_harvested_tensix_cores() const {
    std::vector<size_t> harvested_x_coords = get_harvested_indices(harvesting_masks.tensix_harvesting_mask);
    std::vector<CoreCoord> harvested_tensix_cores;
    for (size_t y = 0; y < tensix_grid_size.y; y++) {
        for (size_t x = 0; x < tensix_grid_size.x; x++) {
            const tt_xy_pair core = tensix_cores[y * tensix_grid_size.x + x];
            CoreCoord core_coord(core.x, core.y, CoreType::TENSIX, CoordSystem::PHYSICAL);
            if (std::find(harvested_x_coords.begin(), harvested_x_coords.end(), x) != harvested_x_coords.end()) {
                harvested_tensix_cores.push_back(core_coord);
            }
        }
    }
    return harvested_tensix_cores;
}

std::vector<CoreCoord> BlackholeCoordinateManager::get_dram_cores() const {
    std::vector<size_t> harvested_banks = get_harvested_indices(harvesting_masks.dram_harvesting_mask);
    std::vector<CoreCoord> unharvested_dram_cores;
    for (size_t x = 0; x < dram_grid_size.x; x++) {
        if (std::find(harvested_banks.begin(), harvested_banks.end(), x) == harvested_banks.end()) {
            for (size_t y = 0; y < dram_grid_size.y; y++) {
                const tt_xy_pair core = dram_cores[x * dram_grid_size.y + y];
                CoreCoord core_coord(core.x, core.y, CoreType::DRAM, CoordSystem::PHYSICAL);
                unharvested_dram_cores.push_back(core_coord);
            }
        }
    }
    return unharvested_dram_cores;
}

std::vector<CoreCoord> BlackholeCoordinateManager::get_harvested_dram_cores() const {
    std::vector<size_t> harvested_banks = get_harvested_indices(harvesting_masks.dram_harvesting_mask);
    std::vector<CoreCoord> harvested_dram_cores;
    for (size_t x = 0; x < dram_grid_size.x; x++) {
        if (std::find(harvested_banks.begin(), harvested_banks.end(), x) != harvested_banks.end()) {
            for (size_t y = 0; y < dram_grid_size.y; y++) {
                const tt_xy_pair core = dram_cores[x * dram_grid_size.y + y];
                CoreCoord core_coord(core.x, core.y, CoreType::DRAM, CoordSystem::PHYSICAL);
                harvested_dram_cores.push_back(core_coord);
            }
        }
    }
    return harvested_dram_cores;
}

std::vector<CoreCoord> BlackholeCoordinateManager::get_eth_cores() const {
    std::vector<size_t> harvested_channels = get_harvested_indices(harvesting_masks.eth_harvesting_mask);
    std::vector<CoreCoord> unharvested_eth_cores;
    for (size_t eth_channel = 0; eth_channel < num_eth_channels; eth_channel++) {
        const tt_xy_pair core = eth_cores[eth_channel];
        CoreCoord core_coord(core.x, core.y, CoreType::ETH, CoordSystem::PHYSICAL);
        if (std::find(harvested_channels.begin(), harvested_channels.end(), eth_channel) == harvested_channels.end()) {
            unharvested_eth_cores.push_back(core_coord);
        }
    }
    return unharvested_eth_cores;
}

std::vector<CoreCoord> BlackholeCoordinateManager::get_harvested_eth_cores() const {
    std::vector<size_t> harvested_channels = get_harvested_indices(harvesting_masks.eth_harvesting_mask);
    std::vector<CoreCoord> harvested_eth_cores;
    for (size_t eth_channel = 0; eth_channel < num_eth_channels; eth_channel++) {
        const tt_xy_pair core = eth_cores[eth_channel];
        CoreCoord core_coord(core.x, core.y, CoreType::ETH, CoordSystem::PHYSICAL);
        if (std::find(harvested_channels.begin(), harvested_channels.end(), eth_channel) != harvested_channels.end()) {
            harvested_eth_cores.push_back(core_coord);
        }
    }

    return harvested_eth_cores;
}

std::vector<CoreCoord> BlackholeCoordinateManager::get_pcie_cores() const {
    std::vector<CoreCoord> unharvested_pcie_cores;
    for (size_t x = 0; x < pcie_grid_size.x; x++) {
        if (harvesting_masks.pcie_harvesting_mask & (1 << x)) {
            continue;
        }
        const tt_xy_pair core = pcie_cores[x];
        CoreCoord core_coord(core.x, core.y, CoreType::PCIE, CoordSystem::PHYSICAL);
        unharvested_pcie_cores.push_back(core_coord);
    }

    return unharvested_pcie_cores;
}

std::vector<CoreCoord> BlackholeCoordinateManager::get_harvested_pcie_cores() const {
    std::vector<CoreCoord> harvested_pcie_cores;
    for (size_t x = 0; x < pcie_grid_size.x; x++) {
        if (!(harvesting_masks.pcie_harvesting_mask & (1 << x))) {
            continue;
        }
        const tt_xy_pair core = pcie_cores[x];
        CoreCoord core_coord(core.x, core.y, CoreType::PCIE, CoordSystem::PHYSICAL);
        harvested_pcie_cores.push_back(core_coord);
    }

    return harvested_pcie_cores;
}

tt_xy_pair BlackholeCoordinateManager::get_harvested_tensix_grid_size() const {
    return {CoordinateManager::get_num_harvested(harvesting_masks.tensix_harvesting_mask), tensix_grid_size.y};
}

tt_xy_pair BlackholeCoordinateManager::get_harvested_dram_grid_size() const {
    return {CoordinateManager::get_num_harvested(harvesting_masks.dram_harvesting_mask), dram_grid_size.y};
}

tt_xy_pair BlackholeCoordinateManager::get_tensix_grid_size() const {
    return {
        tensix_grid_size.x - CoordinateManager::get_num_harvested(harvesting_masks.tensix_harvesting_mask),
        tensix_grid_size.y};
}

tt_xy_pair BlackholeCoordinateManager::get_dram_grid_size() const {
    return {
        dram_grid_size.x - CoordinateManager::get_num_harvested(harvesting_masks.dram_harvesting_mask),
        dram_grid_size.y};
}

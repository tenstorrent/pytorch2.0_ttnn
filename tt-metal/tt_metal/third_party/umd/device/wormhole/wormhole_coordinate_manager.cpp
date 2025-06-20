/*
 * SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#include "umd/device/wormhole_coordinate_manager.h"

using namespace tt::umd;

WormholeCoordinateManager::WormholeCoordinateManager(
    const bool noc_translation_enabled,
    const HarvestingMasks harvesting_masks,
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

void WormholeCoordinateManager::fill_tensix_physical_translated_mapping() {
    size_t num_harvested_y = CoordinateManager::get_num_harvested(harvesting_masks.tensix_harvesting_mask);

    for (size_t y = 0; y < tensix_grid_size.y - num_harvested_y; y++) {
        for (size_t x = 0; x < tensix_grid_size.x; x++) {
            CoreCoord logical_coord = CoreCoord(x, y, CoreType::TENSIX, CoordSystem::LOGICAL);
            const tt_xy_pair physical_pair = to_physical_map[logical_coord];
            const size_t translated_x = x + wormhole::tensix_translated_coordinate_start_x;
            const size_t translated_y = y + wormhole::tensix_translated_coordinate_start_y;

            CoreCoord translated_coord =
                CoreCoord(translated_x, translated_y, CoreType::TENSIX, CoordSystem::TRANSLATED);

            add_core_translation(translated_coord, physical_pair);
        }
    }

    size_t harvested_index = (tensix_grid_size.y - num_harvested_y) * tensix_grid_size.x;
    size_t translated_y = wormhole::tensix_translated_coordinate_start_y + tensix_grid_size.y - num_harvested_y;
    for (size_t y = 0; y < tensix_grid_size.y; y++) {
        if (harvesting_masks.tensix_harvesting_mask & (1 << y)) {
            for (size_t x = 0; x < tensix_grid_size.x; x++) {
                const tt_xy_pair physical_core = tensix_cores[y * tensix_grid_size.x + x];
                const size_t translated_x = x + wormhole::tensix_translated_coordinate_start_x;
                CoreCoord translated_coord =
                    CoreCoord(translated_x, translated_y, CoreType::TENSIX, CoordSystem::TRANSLATED);

                add_core_translation(translated_coord, physical_core);
            }
            translated_y++;
        }
    }
}

void WormholeCoordinateManager::fill_dram_physical_translated_mapping() {
    // DRAM cores are not translated in Wormhole.
    fill_dram_default_physical_translated_mapping();
}

void WormholeCoordinateManager::fill_eth_physical_translated_mapping() {
    for (auto eth_core : eth_cores) {
        CoreCoord translated_coord = CoreCoord(eth_core, CoreType::ETH, CoordSystem::TRANSLATED);

        // X coordinate is in range [1-4], [6-9], but it should be consecutive in translated coordinates.
        if (translated_coord.x > 5) {
            translated_coord.x -= 1;
        }
        // Since the translated coordinates start from 1, we need to subtract 1 to the translated X coordinate.
        translated_coord.x -= 1;
        translated_coord.x += wormhole::eth_translated_coordinate_start_x;

        // Y coordinate is either 0 or 6, but it should be consecutive in translated coordinates.
        if (translated_coord.y == 6) {
            translated_coord.y = 1;
        }
        translated_coord.y += wormhole::eth_translated_coordinate_start_y;

        add_core_translation(translated_coord, eth_core);
    }
}

void WormholeCoordinateManager::fill_pcie_physical_translated_mapping() {
    // PCIE cores are not translated in Wormhole.
    fill_pcie_default_physical_translated_mapping();
}

void WormholeCoordinateManager::fill_arc_physical_translated_mapping() {
    // ARC cores are not translated in Wormhole.
    fill_arc_default_physical_translated_mapping();
}

tt_xy_pair WormholeCoordinateManager::get_tensix_grid_size() const {
    return {
        tensix_grid_size.x,
        tensix_grid_size.y - CoordinateManager::get_num_harvested(harvesting_masks.tensix_harvesting_mask)};
}

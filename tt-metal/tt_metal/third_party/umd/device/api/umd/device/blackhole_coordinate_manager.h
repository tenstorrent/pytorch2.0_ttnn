/*
 * SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include "umd/device/blackhole_implementation.h"
#include "umd/device/coordinate_manager.h"

class BlackholeCoordinateManager : public CoordinateManager {
public:
    BlackholeCoordinateManager(
        const bool noc_translation_enabled,
        tt::umd::HarvestingMasks harvesting_masks,
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
        const std::vector<uint32_t>& noc0_x_to_noc1_x = {},
        const std::vector<uint32_t>& noc0_y_to_noc1_y = {});

protected:
    void assert_coordinate_manager_constructor() override;

    void translate_tensix_coords() override;
    void translate_dram_coords() override;
    void translate_eth_coords() override;
    void translate_pcie_coords() override;

    void fill_tensix_physical_translated_mapping() override;
    void fill_dram_physical_translated_mapping() override;
    void fill_eth_physical_translated_mapping() override;
    void fill_pcie_physical_translated_mapping() override;
    void fill_arc_physical_translated_mapping() override;

    std::vector<tt::umd::CoreCoord> get_tensix_cores() const override;
    std::vector<tt::umd::CoreCoord> get_harvested_tensix_cores() const override;
    std::vector<tt::umd::CoreCoord> get_dram_cores() const override;
    std::vector<tt::umd::CoreCoord> get_harvested_dram_cores() const override;
    std::vector<tt::umd::CoreCoord> get_eth_cores() const override;
    std::vector<tt::umd::CoreCoord> get_harvested_eth_cores() const override;
    std::vector<tt::umd::CoreCoord> get_pcie_cores() const override;
    std::vector<tt::umd::CoreCoord> get_harvested_pcie_cores() const override;
    tt_xy_pair get_tensix_grid_size() const override;
    tt_xy_pair get_dram_grid_size() const override;
    tt_xy_pair get_harvested_tensix_grid_size() const override;
    tt_xy_pair get_harvested_dram_grid_size() const override;

private:
    void map_dram_banks(
        const size_t start_bank,
        const size_t end_bank,
        const size_t x_coord,
        const size_t y_coord_start = tt::umd::blackhole::dram_translated_coordinate_start_y);
};

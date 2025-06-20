/*
 * SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include <map>
#include <set>
#include <vector>

#include "umd/device/tt_core_coordinates.h"
#include "umd/device/tt_xy_pair.h"
#include "umd/device/types/arch.h"
#include "umd/device/types/cluster_descriptor_types.h"
#include "umd/device/types/harvesting.h"

class CoordinateManager {
public:
    CoordinateManager(CoordinateManager& other) = default;
    virtual ~CoordinateManager() = default;

    /*
     * Creates a Coordinate Manager object.
     * Board type and is_chip_remote are used only for Blackhole, since PCIe cores are different
     * for different boards and whether the chip is remote or not.
     */
    static std::shared_ptr<CoordinateManager> create_coordinate_manager(
        tt::ARCH arch,
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

    static std::shared_ptr<CoordinateManager> create_coordinate_manager(
        tt::ARCH arch,
        const bool noc_translation_enabled,
        const tt::umd::HarvestingMasks harvesting_masks = {0, 0, 0},
        const BoardType board_type = BoardType::UNKNOWN,
        const uint8_t asic_location = 0);

    static size_t get_num_harvested(const size_t harvesting_mask);
    static std::vector<size_t> get_harvested_indices(const size_t harvesting_mask);

    // Harvesting mask is reported by hardware in the order of physical layout. This function returns a more suitable
    // representation in logical order: Bit 0 being set means the first row in NOC0 coords is harvested.
    static uint32_t shuffle_tensix_harvesting_mask(tt::ARCH arch, uint32_t tensix_harvesting_physical_layout);
    // TODO: This function should be removed once the corresponding API is removed from Cluster.
    static uint32_t shuffle_tensix_harvesting_mask_to_noc0_coords(
        tt::ARCH arch, uint32_t tensix_harvesting_logical_layout);

    tt::umd::CoreCoord translate_coord_to(const tt::umd::CoreCoord core_coord, const CoordSystem coord_system) const;
    tt::umd::CoreCoord get_coord_at(const tt_xy_pair core, const CoordSystem coord_system) const;
    tt::umd::CoreCoord translate_coord_to(
        const tt_xy_pair core, const CoordSystem input_coord_system, const CoordSystem target_coord_system) const;

    std::vector<tt::umd::CoreCoord> get_cores(const CoreType core_type) const;
    tt_xy_pair get_grid_size(const CoreType core_type) const;

    std::vector<tt::umd::CoreCoord> get_harvested_cores(const CoreType core_type) const;
    tt_xy_pair get_harvested_grid_size(const CoreType core_type) const;

    tt::umd::HarvestingMasks get_harvesting_masks() const;

    uint32_t get_num_eth_channels() const;

    uint32_t get_num_harvested_eth_channels() const;

private:
    const std::vector<tt_xy_pair>& get_physical_pairs(const CoreType core_type) const;
    std::vector<tt::umd::CoreCoord> get_all_physical_cores(const CoreType core_type) const;

protected:
    /*
     * Constructor for Coordinate Manager.
     * Tensix harvesting mask is supposed to be passed as original harvesting mask that is
     * returned from create-ethernet-map, so each bit is responsible for one row of the actual physical
     * row of the tensix cores on the chip. Harvesting mask is shuffled in constructor to match the NOC
     * layout of the tensix cores.
     * Router cores don't have a grid size, since they are not layed out in a regular fashion.
     */
    CoordinateManager(
        const bool noc_translation_enabled,
        const tt::umd::HarvestingMasks harvesting_masks,
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

    void initialize();

    virtual void assert_coordinate_manager_constructor();

    virtual void translate_tensix_coords();
    virtual void translate_dram_coords();
    virtual void translate_eth_coords();
    virtual void translate_arc_coords();
    virtual void translate_pcie_coords();
    virtual void translate_router_coords();
    virtual void translate_security_coords();
    virtual void translate_l2cpu_coords();

    void identity_map_physical_cores();
    void add_core_translation(const tt::umd::CoreCoord& core_coord, const tt_xy_pair& physical_pair);
    void add_noc1_to_noc0_mapping();

    virtual std::vector<tt::umd::CoreCoord> get_tensix_cores() const;
    virtual std::vector<tt::umd::CoreCoord> get_harvested_tensix_cores() const;
    virtual std::vector<tt::umd::CoreCoord> get_dram_cores() const;
    virtual std::vector<tt::umd::CoreCoord> get_harvested_dram_cores() const;
    virtual std::vector<tt::umd::CoreCoord> get_eth_cores() const;
    virtual std::vector<tt::umd::CoreCoord> get_harvested_eth_cores() const;
    virtual std::vector<tt::umd::CoreCoord> get_pcie_cores() const;
    virtual std::vector<tt::umd::CoreCoord> get_harvested_pcie_cores() const;
    virtual tt_xy_pair get_tensix_grid_size() const = 0;
    virtual tt_xy_pair get_dram_grid_size() const;
    virtual tt_xy_pair get_harvested_tensix_grid_size() const;
    virtual tt_xy_pair get_harvested_dram_grid_size() const;

    /*
     * By default, translated coordinates are the same as physical coordinates.
     * This will be true for all architectures if noc_translation_enabled is false.
     */
    void fill_tensix_default_physical_translated_mapping();
    void fill_eth_default_physical_translated_mapping();
    void fill_dram_default_physical_translated_mapping();
    void fill_pcie_default_physical_translated_mapping();
    void fill_arc_default_physical_translated_mapping();

    /*
     * Fills the physical to translated mapping for the tensix cores.
     * By default, translated coordinates are the same as physical coordinates.
     * Derived coordinate managers that need to implement different mapping
     * should override this method. Wormhole and Blackhole coordinate managers
     * override this method to implement different mapping.
     */
    virtual void fill_tensix_physical_translated_mapping() = 0;

    /*
     * Fills the physical to translated mapping for the ethernet cores.
     * By default, translated coordinates are the same as physical coordinates.
     * Derived coordinate managers that need to implement different mapping
     * should override this method. Wormhole and Blackhole coordinate managers
     * override this method to implement different mapping.
     */
    virtual void fill_eth_physical_translated_mapping() = 0;

    /*
     * Fills the physical to translated mapping for the DRAM cores.
     * By default, translated coordinates are the same as physical coordinates.
     * Derived coordinate managers that need to implement different mapping
     * should override this method. Blackhole coordinate manager overrides
     * this method to implement different mapping.
     */
    virtual void fill_dram_physical_translated_mapping() = 0;

    /*
     * Fills the physical to translated mapping for the PCIE cores.
     * By default, translated coordinates are the same as physical coordinates.
     * Derived coordinate managers that need to implement different mapping
     * should override this method. Blackhole coordinate manager overrides
     * this method to implement different mapping.
     */
    virtual void fill_pcie_physical_translated_mapping() = 0;

    /*
     * Fills the physical to translated mapping for the ARC cores.
     * By default, translated coordinates are the same as physical coordinates.
     * Derived coordinate managers that need to implement different mapping
     * should override this method.
     */
    virtual void fill_arc_physical_translated_mapping() = 0;

    // Maps full CoreCoord from any CoordSystem to physical coordinates.
    std::map<tt::umd::CoreCoord, tt_xy_pair> to_physical_map;
    // Maps physical coordinates given a target CoordSystem to full CoreCoord.
    std::map<std::pair<tt_xy_pair, CoordSystem>, tt::umd::CoreCoord> from_physical_map;
    // Maps coordinates in the designated CoordSystem to a full CoreCoord at that location holding the right CoreType.
    // Doesn't include logical CoordSystem.
    std::map<std::pair<tt_xy_pair, CoordSystem>, tt::umd::CoreCoord> to_core_type_map;

    // Whether NOC translation is enabled on chip.
    // This flag affects how Translated coords are calculated. If translation is enabled on the chip, than we can
    // interface it with a coordinate system which abstracts away harvested cores. If it is not enabled, then we need to
    // interface it with noc0 coordinates.
    bool noc_translation_enabled;
    tt::umd::HarvestingMasks harvesting_masks;

    tt_xy_pair tensix_grid_size;
    const std::vector<tt_xy_pair> tensix_cores;

    tt_xy_pair dram_grid_size;
    const std::vector<tt_xy_pair> dram_cores;

    const size_t num_eth_channels;
    const std::vector<tt_xy_pair> eth_cores;

    tt_xy_pair arc_grid_size;
    const std::vector<tt_xy_pair> arc_cores;

    tt_xy_pair pcie_grid_size;
    const std::vector<tt_xy_pair> pcie_cores;

    // Router cores don't have a grid size, since they are not layed out in a regular fashion.
    const std::vector<tt_xy_pair> router_cores;

    const std::vector<tt_xy_pair> security_cores;

    const std::vector<tt_xy_pair> l2cpu_cores;

    const std::vector<uint32_t> noc0_x_to_noc1_x;
    const std::vector<uint32_t> noc0_y_to_noc1_y;
};

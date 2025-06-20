/*
 * SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#include "gtest/gtest.h"
#include "umd/device/blackhole_implementation.h"
#include "umd/device/coordinate_manager.h"

using namespace tt::umd;

// Tests that all physical coordinates are same as all virtual coordinates
// when there is no harvesting.
TEST(CoordinateManager, CoordinateManagerBlackholeNoHarvesting) {
    std::shared_ptr<CoordinateManager> coordinate_manager =
        CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, true);

    // We expect full grid size since there is no harvesting.
    tt_xy_pair tensix_grid_size = tt::umd::blackhole::TENSIX_GRID_SIZE;
    for (size_t x = 0; x < tensix_grid_size.x; x++) {
        for (size_t y = 0; y < tensix_grid_size.y; y++) {
            CoreCoord logical_coords = CoreCoord(x, y, CoreType::TENSIX, CoordSystem::LOGICAL);
            CoreCoord virtual_coords = coordinate_manager->translate_coord_to(logical_coords, CoordSystem::VIRTUAL);
            CoreCoord physical_coords = coordinate_manager->translate_coord_to(logical_coords, CoordSystem::PHYSICAL);

            // Virtual and physical coordinates should be the same.
            EXPECT_EQ(physical_coords.x, virtual_coords.x);
            EXPECT_EQ(physical_coords.y, virtual_coords.y);
        }
    }
}

// Test basic translation to virtual and physical noc coordinates.
// We expect that the top left core will have virtual and physical coordinates (1, 2) and (2, 2) for
// the logical coordinates (0, 0) if the first column is harvested.
TEST(CoordinateManager, CoordinateManagerBlackholeTopLeftCore) {
    // This is targeting first column of Tensix cores on NOC layout.
    const size_t tensix_harvesting_mask = (1 << 0);
    std::shared_ptr<CoordinateManager> coordinate_manager =
        CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, true, {tensix_harvesting_mask});

    CoreCoord logical_coords = CoreCoord(0, 0, CoreType::TENSIX, CoordSystem::LOGICAL);

    // Always expect same virtual coordinate for (0, 0) logical coordinate.
    CoreCoord virtual_cords = coordinate_manager->translate_coord_to(logical_coords, CoordSystem::VIRTUAL);
    EXPECT_EQ(virtual_cords, CoreCoord(1, 2, CoreType::TENSIX, CoordSystem::VIRTUAL));

    // This depends on harvesting mask. So expected physical coord is specific to this test and Blackhole arch.
    CoreCoord physical_cords = coordinate_manager->translate_coord_to(logical_coords, CoordSystem::PHYSICAL);
    EXPECT_EQ(physical_cords, CoreCoord(2, 2, CoreType::TENSIX, CoordSystem::PHYSICAL));
}

// Test basic translation to virtual and physical noc coordinates.
// We expect that the top right core will have virtual and physical coordinates (15, 2) and (16, 2) for
// the logical coordinates (12, 0) if the first column is harvested.
TEST(CoordinateManager, CoordinateManagerBlackholeTopRightCore) {
    // This is targeting first column of Tensix cores on NOC layout.
    const size_t tensix_harvesting_mask = (1 << 0);
    std::shared_ptr<CoordinateManager> coordinate_manager =
        CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, true, {tensix_harvesting_mask});

    tt_xy_pair tensix_grid_size = coordinate_manager->get_grid_size(CoreType::TENSIX);
    EXPECT_EQ(tensix_grid_size.x, 13);
    EXPECT_EQ(tensix_grid_size.y, 10);
    CoreCoord logical_coords = CoreCoord(tensix_grid_size.x - 1, 0, CoreType::TENSIX, CoordSystem::LOGICAL);

    CoreCoord virtual_cords = coordinate_manager->translate_coord_to(logical_coords, CoordSystem::VIRTUAL);
    EXPECT_EQ(virtual_cords, CoreCoord(15, 2, CoreType::TENSIX, CoordSystem::VIRTUAL));

    CoreCoord physical_cords = coordinate_manager->translate_coord_to(logical_coords, CoordSystem::PHYSICAL);
    EXPECT_EQ(physical_cords, CoreCoord(16, 2, CoreType::TENSIX, CoordSystem::PHYSICAL));
}

// Test basic translation to virtual and physical noc coordinates.
// We expect that the bottom left core will have virtual and physical coordinates (1, 11) and (2, 11) for
// the logical coordinates (0, 9) if the first column is harvested.
TEST(CoordinateManager, CoordinateManagerBlackholeBottomLeftCore) {
    // This is targeting first column of Tensix cores on NOC layout.
    const size_t tensix_harvesting_mask = (1 << 0);
    std::shared_ptr<CoordinateManager> coordinate_manager =
        CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, true, {tensix_harvesting_mask});

    tt_xy_pair tensix_grid_size = coordinate_manager->get_grid_size(CoreType::TENSIX);
    EXPECT_EQ(tensix_grid_size.x, 13);
    EXPECT_EQ(tensix_grid_size.y, 10);
    CoreCoord logical_coords = CoreCoord(0, tensix_grid_size.y - 1, CoreType::TENSIX, CoordSystem::LOGICAL);

    CoreCoord virtual_cords = coordinate_manager->translate_coord_to(logical_coords, CoordSystem::VIRTUAL);
    EXPECT_EQ(virtual_cords, CoreCoord(1, 11, CoreType::TENSIX, CoordSystem::VIRTUAL));

    CoreCoord physical_cords = coordinate_manager->translate_coord_to(logical_coords, CoordSystem::PHYSICAL);
    EXPECT_EQ(physical_cords, CoreCoord(2, 11, CoreType::TENSIX, CoordSystem::PHYSICAL));
}

// Test logical to physical coordinate translation.
// For the full grid of logical coordinates we expect that there are no duplicates of physical coordinates.
// For the reverse mapping back of physical to logical coordinates we expect that same logical coordinates are returned
// as from original mapping.
TEST(CoordinateManager, CoordinateManagerBlackholeLogicalPhysicalMapping) {
    const size_t max_num_harvested_x = 14;

    for (size_t tensix_harvesting_mask = 0; tensix_harvesting_mask < (1 << max_num_harvested_x);
         tensix_harvesting_mask++) {
        std::shared_ptr<CoordinateManager> coordinate_manager =
            CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, true, {tensix_harvesting_mask});

        std::map<CoreCoord, CoreCoord> logical_to_physical;
        std::set<CoreCoord> physical_coords_set;
        tt_xy_pair tensix_grid_size = tt::umd::blackhole::TENSIX_GRID_SIZE;

        size_t num_harvested_x = CoordinateManager::get_num_harvested(tensix_harvesting_mask);

        for (size_t x = 0; x < tensix_grid_size.x - num_harvested_x; x++) {
            for (size_t y = 0; y < tensix_grid_size.y; y++) {
                CoreCoord logical_coords = CoreCoord(x, y, CoreType::TENSIX, CoordSystem::LOGICAL);
                CoreCoord physical_coords =
                    coordinate_manager->translate_coord_to(logical_coords, CoordSystem::PHYSICAL);
                logical_to_physical[logical_coords] = physical_coords;

                // Expect that logical to physical translation is 1-1 mapping. No duplicates for physical coordinates.
                EXPECT_EQ(physical_coords_set.count(physical_coords), 0);
                physical_coords_set.insert(physical_coords);
            }
        }

        EXPECT_EQ(physical_coords_set.size(), tensix_grid_size.y * (tensix_grid_size.x - num_harvested_x));

        for (auto it : logical_to_physical) {
            CoreCoord physical_coords = it.second;
            CoreCoord logical_coords = coordinate_manager->translate_coord_to(physical_coords, CoordSystem::LOGICAL);

            // Expect that reverse mapping of physical coordinates gives the same logical coordinates
            // using which we got the physical coordinates.
            EXPECT_EQ(it.first, logical_coords);
        }
    }
}

// Test logical to virtual coordinate translation.
// For the full grid of logical coordinates we expect that there are no duplicates of virtual coordinates.
// For the reverse mapping back of virtual to logical coordinates we expect that same logical coordinates are returned
// as from original mapping.
TEST(CoordinateManager, CoordinateManagerBlackholeLogicalVirtualMapping) {
    const size_t max_num_harvested_x = 14;

    for (size_t tensix_harvesting_mask = 0; tensix_harvesting_mask < (1 << max_num_harvested_x);
         tensix_harvesting_mask++) {
        std::shared_ptr<CoordinateManager> coordinate_manager =
            CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, true, {tensix_harvesting_mask});

        std::map<CoreCoord, CoreCoord> logical_to_virtual;
        std::set<CoreCoord> virtual_coords_set;
        tt_xy_pair tensix_grid_size = tt::umd::blackhole::TENSIX_GRID_SIZE;

        size_t num_harvested_x = CoordinateManager::get_num_harvested(tensix_harvesting_mask);

        for (size_t x = 0; x < tensix_grid_size.x - num_harvested_x; x++) {
            for (size_t y = 0; y < tensix_grid_size.y; y++) {
                CoreCoord logical_coords = CoreCoord(x, y, CoreType::TENSIX, CoordSystem::LOGICAL);
                CoreCoord virtual_coords = coordinate_manager->translate_coord_to(logical_coords, CoordSystem::VIRTUAL);
                logical_to_virtual[logical_coords] = virtual_coords;

                // Expect that logical to virtual translation is 1-1 mapping. No duplicates for virtual coordinates.
                EXPECT_EQ(virtual_coords_set.count(virtual_coords), 0);
                virtual_coords_set.insert(virtual_coords);
            }
        }

        EXPECT_EQ(virtual_coords_set.size(), tensix_grid_size.y * (tensix_grid_size.x - num_harvested_x));

        for (auto it : logical_to_virtual) {
            CoreCoord virtual_coords = it.second;
            CoreCoord logical_coords = coordinate_manager->translate_coord_to(virtual_coords, CoordSystem::LOGICAL);

            // Expect that reverse mapping of virtual coordinates gives the same logical coordinates
            // using which we got the virtual coordinates.
            EXPECT_EQ(it.first, logical_coords);
        }
    }
}

// Test logical to translated coordinate translation.
// For the full grid of logical coordinates we expect that there are no duplicates of translated coordinates.
// For the reverse mapping back of translated to logical coordinates we expect that same logical coordinates are
// returned as from original mapping.
TEST(CoordinateManager, CoordinateManagerBlackholeLogicalTranslatedMapping) {
    const size_t max_num_harvested_x = 14;

    for (bool noc_translation_enabled : {true, false}) {
        for (size_t tensix_harvesting_mask = 0; tensix_harvesting_mask < (1 << max_num_harvested_x);
             tensix_harvesting_mask++) {
            std::shared_ptr<CoordinateManager> coordinate_manager = CoordinateManager::create_coordinate_manager(
                tt::ARCH::BLACKHOLE, noc_translation_enabled, {tensix_harvesting_mask});

            std::map<CoreCoord, CoreCoord> logical_to_translated;
            std::set<CoreCoord> translated_coords_set;
            tt_xy_pair tensix_grid_size = tt::umd::blackhole::TENSIX_GRID_SIZE;

            size_t num_harvested_x = CoordinateManager::get_num_harvested(tensix_harvesting_mask);

            for (size_t x = 0; x < tensix_grid_size.x - num_harvested_x; x++) {
                for (size_t y = 0; y < tensix_grid_size.y; y++) {
                    CoreCoord logical_coords = CoreCoord(x, y, CoreType::TENSIX, CoordSystem::LOGICAL);
                    CoreCoord translated_coords =
                        coordinate_manager->translate_coord_to(logical_coords, CoordSystem::TRANSLATED);
                    logical_to_translated[logical_coords] = translated_coords;

                    // Expect that logical to translated translation is 1-1 mapping. No duplicates for translated
                    // coordinates.
                    EXPECT_EQ(translated_coords_set.count(translated_coords), 0);
                    translated_coords_set.insert(translated_coords);
                }
            }

            EXPECT_EQ(translated_coords_set.size(), tensix_grid_size.y * (tensix_grid_size.x - num_harvested_x));

            for (auto it : logical_to_translated) {
                CoreCoord translated_coords = it.second;
                CoreCoord logical_coords =
                    coordinate_manager->translate_coord_to(translated_coords, CoordSystem::LOGICAL);

                // Expect that reverse mapping of translated coordinates gives the same logical coordinates
                // using which we got the translated coordinates.
                EXPECT_EQ(it.first, logical_coords);
            }
        }
    }
}

// Test that virtual and translated coordinates are same for all logical coordinates.
// This is expected for Blackhole way of harvesting when noc translation is enabled.
// If noc translation is disabled then translated coordinates are same as physical coordinates.
TEST(CoordinateManager, CoordinateManagerBlackholeVirtualEqualTranslated) {
    const size_t max_num_harvested_x = 14;

    for (bool noc_translation_enabled : {true, false}) {
        for (size_t tensix_harvesting_mask = 0; tensix_harvesting_mask < (1 << max_num_harvested_x);
             tensix_harvesting_mask++) {
            std::shared_ptr<CoordinateManager> coordinate_manager = CoordinateManager::create_coordinate_manager(
                tt::ARCH::BLACKHOLE, noc_translation_enabled, {tensix_harvesting_mask});

            size_t num_harvested_x = CoordinateManager::get_num_harvested(tensix_harvesting_mask);

            for (size_t x = 0; x < tt::umd::blackhole::TENSIX_GRID_SIZE.x - num_harvested_x; x++) {
                for (size_t y = 0; y < tt::umd::blackhole::TENSIX_GRID_SIZE.y; y++) {
                    CoreCoord logical_coords = CoreCoord(x, y, CoreType::TENSIX, CoordSystem::LOGICAL);
                    CoreCoord translated_coords =
                        coordinate_manager->translate_coord_to(logical_coords, CoordSystem::TRANSLATED);
                    CoreCoord virtual_coords = coordinate_manager->translate_coord_to(
                        logical_coords, noc_translation_enabled ? CoordSystem::VIRTUAL : CoordSystem::PHYSICAL);

                    // Expect that translated coordinates are same as virtual coordinates.
                    EXPECT_EQ(translated_coords.x, virtual_coords.x);
                    EXPECT_EQ(translated_coords.y, virtual_coords.y);
                }
            }
        }
    }
}

// Test mapping of the coordinates for harvested DRAM bank.
TEST(CoordinateManager, CoordinateManagerBlackholeTensixTranslatedMappingHarvested) {
    const size_t tensix_harvesting_mask = (1 << 0) | (1 << 1);
    std::shared_ptr<CoordinateManager> coordinate_manager =
        CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, true, {tensix_harvesting_mask});

    const tt_xy_pair tensix_grid_size = tt::umd::blackhole::TENSIX_GRID_SIZE;
    const std::vector<tt_xy_pair> tensix_cores = tt::umd::blackhole::TENSIX_CORES_NOC0;

    size_t num_harvested_x = CoordinateManager::get_num_harvested(tensix_harvesting_mask);

    size_t index = 0;
    size_t virtual_index = tensix_grid_size.x - num_harvested_x;

    const CoreCoord tensix_column0 = CoreCoord(1, 2, CoreType::TENSIX, CoordSystem::NOC0);
    const CoreCoord translated_column0 =
        coordinate_manager->translate_coord_to(tensix_column0, CoordSystem::TRANSLATED);

    EXPECT_EQ(translated_column0.x, 16);
    EXPECT_EQ(translated_column0.y, 2);

    const CoreCoord tensix_column1 = CoreCoord(2, 2, CoreType::TENSIX, CoordSystem::NOC0);
    const CoreCoord translated_column1 =
        coordinate_manager->translate_coord_to(tensix_column1, CoordSystem::TRANSLATED);

    EXPECT_EQ(translated_column1.x, 15);
    EXPECT_EQ(translated_column1.y, 2);
}

// Test mapping of DRAM coordinates from logical to physical. When there is no DRAM harvesting, logical
// coordinates should cover all physical coordinates.
TEST(CoordinateManager, CoordinateManagerBlackholeDRAMNoHarvesting) {
    std::shared_ptr<CoordinateManager> coordinate_manager =
        CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, true);

    const size_t num_dram_banks = tt::umd::blackhole::NUM_DRAM_BANKS;
    const size_t num_noc_ports_per_bank = tt::umd::blackhole::NUM_NOC_PORTS_PER_DRAM_BANK;
    const std::vector<tt_xy_pair>& dram_cores = flatten_vector(tt::umd::blackhole::DRAM_CORES_NOC0);

    for (size_t dram_bank = 0; dram_bank < num_dram_banks; dram_bank++) {
        for (size_t noc_port = 0; noc_port < num_noc_ports_per_bank; noc_port++) {
            const CoreCoord dram_logical(dram_bank, noc_port, CoreType::DRAM, CoordSystem::LOGICAL);
            const size_t physical_core_index = dram_bank * num_noc_ports_per_bank + noc_port;
            const CoreCoord expected_physical = CoreCoord(
                dram_cores[physical_core_index].x,
                dram_cores[physical_core_index].y,
                CoreType::DRAM,
                CoordSystem::PHYSICAL);

            const CoreCoord dram_physical = coordinate_manager->translate_coord_to(dram_logical, CoordSystem::PHYSICAL);

            EXPECT_EQ(dram_physical, expected_physical);
        }
    }
}

// Test top left corner translation from logical to physical coordinates.
TEST(CoordinateManager, CoordinateManagerBlackholeDRAMTopLeft) {
    std::shared_ptr<CoordinateManager> coordinate_manager =
        CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, true, {0, 1});

    const CoreCoord top_left_dram_logical = CoreCoord(0, 0, CoreType::DRAM, CoordSystem::LOGICAL);
    const CoreCoord expected_top_left_physical = CoreCoord(0, 2, CoreType::DRAM, CoordSystem::PHYSICAL);

    const CoreCoord top_left_physical =
        coordinate_manager->translate_coord_to(top_left_dram_logical, CoordSystem::PHYSICAL);

    EXPECT_EQ(top_left_physical, expected_top_left_physical);
}

// Test logical to physical DRAM coordinate translation.
// For the full grid of logical coordinates we expect that there are no duplicates of physical coordinates.
// For the reverse mapping back of physical to logical coordinates we expect that same logical coordinates are returned
// as from original mapping.
TEST(CoordinateManager, CoordinateManagerBlackholeDRAMLogicalPhysicalMapping) {
    const size_t max_num_banks_harvested = tt::umd::blackhole::NUM_DRAM_BANKS;
    const size_t num_dram_banks = tt::umd::blackhole::NUM_DRAM_BANKS;
    const size_t num_noc_ports_per_bank = tt::umd::blackhole::NUM_NOC_PORTS_PER_DRAM_BANK;
    const std::vector<tt_xy_pair>& dram_cores = flatten_vector(tt::umd::blackhole::DRAM_CORES_NOC0);

    for (size_t dram_harvesting_mask = 0; dram_harvesting_mask < (1 << max_num_banks_harvested);
         dram_harvesting_mask++) {
        if (CoordinateManager::get_num_harvested(dram_harvesting_mask) > 1) {
            continue;
        }

        std::shared_ptr<CoordinateManager> coordinate_manager =
            CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, true, {0, dram_harvesting_mask});

        std::map<CoreCoord, CoreCoord> logical_to_physical;
        std::set<CoreCoord> physical_coords_set;

        size_t num_banks_harvested = CoordinateManager::get_num_harvested(dram_harvesting_mask);

        for (size_t x = 0; x < num_dram_banks - num_banks_harvested; x++) {
            for (size_t y = 0; y < num_noc_ports_per_bank; y++) {
                const CoreCoord logical_coords = CoreCoord(x, y, CoreType::DRAM, CoordSystem::LOGICAL);
                const CoreCoord physical_coords =
                    coordinate_manager->translate_coord_to(logical_coords, CoordSystem::PHYSICAL);
                logical_to_physical[logical_coords] = physical_coords;

                // Expect that logical to physical translation is 1-1 mapping. No duplicates for physical coordinates.
                EXPECT_EQ(physical_coords_set.count(physical_coords), 0);
                physical_coords_set.insert(physical_coords);
            }
        }

        EXPECT_EQ(physical_coords_set.size(), num_noc_ports_per_bank * (num_dram_banks - num_banks_harvested));

        for (auto it : logical_to_physical) {
            const CoreCoord physical_coords = it.second;
            const CoreCoord logical_coords =
                coordinate_manager->translate_coord_to(physical_coords, CoordSystem::LOGICAL);

            // Expect that reverse mapping of physical coordinates gives the same logical coordinates
            // using which we got the physical coordinates.
            EXPECT_EQ(it.first, logical_coords);
        }
    }
}

// Test logical to virtual DRAM coordinate translation.
// For the full grid of logical coordinates it is expected that there are no duplicates of virtual coordinates.
// For the reverse mapping back of virtual to logical coordinates it is expected that same logical coordinates are
// returned as from original mapping.
TEST(CoordinateManager, CoordinateManagerBlackholeDRAMLogicalVirtualMapping) {
    const size_t max_num_banks_harvested = tt::umd::blackhole::NUM_DRAM_BANKS;
    const size_t num_dram_banks = tt::umd::blackhole::NUM_DRAM_BANKS;
    const size_t num_noc_ports_per_bank = tt::umd::blackhole::NUM_NOC_PORTS_PER_DRAM_BANK;

    for (size_t dram_harvesting_mask = 0; dram_harvesting_mask < (1 << max_num_banks_harvested);
         dram_harvesting_mask++) {
        if (CoordinateManager::get_num_harvested(dram_harvesting_mask) > 1) {
            continue;
        }

        std::shared_ptr<CoordinateManager> coordinate_manager =
            CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, true, {0, dram_harvesting_mask});

        std::map<CoreCoord, CoreCoord> logical_to_virtual;
        std::set<CoreCoord> virtual_coords_set;

        size_t num_harvested_banks = CoordinateManager::get_num_harvested(dram_harvesting_mask);

        for (size_t x = 0; x < num_dram_banks - num_harvested_banks; x++) {
            for (size_t y = 0; y < num_noc_ports_per_bank; y++) {
                CoreCoord logical_coords = CoreCoord(x, y, CoreType::DRAM, CoordSystem::LOGICAL);
                CoreCoord virtual_coords = coordinate_manager->translate_coord_to(logical_coords, CoordSystem::VIRTUAL);
                logical_to_virtual[logical_coords] = virtual_coords;

                // Expect that logical to virtual translation is 1-1 mapping. No duplicates for virtual coordinates.
                EXPECT_EQ(virtual_coords_set.count(virtual_coords), 0);
                virtual_coords_set.insert(virtual_coords);
            }
        }

        for (auto it : logical_to_virtual) {
            CoreCoord virtual_coords = it.second;
            CoreCoord logical_coords = coordinate_manager->translate_coord_to(virtual_coords, CoordSystem::LOGICAL);

            // Expect that reverse mapping of virtual coordinates gives the same logical coordinates
            // using which we got the virtual coordinates.
            EXPECT_EQ(it.first, logical_coords);
        }
    }
}

// Test DRAM translated mapping.
TEST(CoordinateManager, CoordinateManagerBlackholeDRAMTranslatedMapping) {
    const size_t max_num_banks_harvested = tt::umd::blackhole::NUM_DRAM_BANKS;
    const size_t num_dram_banks = tt::umd::blackhole::NUM_DRAM_BANKS;
    const size_t num_noc_ports_per_bank = tt::umd::blackhole::NUM_NOC_PORTS_PER_DRAM_BANK;

    for (size_t dram_harvesting_mask = 0; dram_harvesting_mask < (1 << max_num_banks_harvested);
         dram_harvesting_mask++) {
        if (CoordinateManager::get_num_harvested(dram_harvesting_mask) > 1) {
            continue;
        }

        std::shared_ptr<CoordinateManager> coordinate_manager =
            CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, true, {0, dram_harvesting_mask});

        std::map<CoreCoord, CoreCoord> logical_to_translated;
        std::set<CoreCoord> translated_coord_set;

        const size_t num_harvested_banks = CoordinateManager::get_num_harvested(dram_harvesting_mask);

        for (size_t x = 0; x < num_dram_banks - num_harvested_banks; x++) {
            for (size_t y = 0; y < num_noc_ports_per_bank; y++) {
                const CoreCoord logical_coords = CoreCoord(x, y, CoreType::DRAM, CoordSystem::LOGICAL);
                const CoreCoord translated_coords =
                    coordinate_manager->translate_coord_to(logical_coords, CoordSystem::TRANSLATED);

                EXPECT_GE(translated_coords.x, tt::umd::blackhole::dram_translated_coordinate_start_x);
                EXPECT_GE(translated_coords.y, tt::umd::blackhole::dram_translated_coordinate_start_y);

                logical_to_translated[logical_coords] = translated_coords;

                // Expect that logical to translated translation is 1-1 mapping. No duplicates for translated
                // coordinates.
                EXPECT_EQ(translated_coord_set.count(translated_coords), 0);
                translated_coord_set.insert(translated_coords);
            }
        }

        for (auto it : logical_to_translated) {
            const CoreCoord translated_coords = it.second;
            const CoreCoord logical_coords =
                coordinate_manager->translate_coord_to(translated_coords, CoordSystem::LOGICAL);

            // Expect that reverse mapping of translated coordinates gives the same logical coordinates
            // using which we got the translated coordinates.
            EXPECT_EQ(it.first, logical_coords);
        }
    }
}

// Test DRAM translated/virtual/physical mapping
TEST(CoordinateManager, CoordinateManagerBlackholeDRAMVirtualPhysicalMapping) {
    const size_t max_num_banks_harvested = tt::umd::blackhole::NUM_DRAM_BANKS;
    const size_t num_dram_banks = tt::umd::blackhole::NUM_DRAM_BANKS;
    const size_t num_noc_ports_per_bank = tt::umd::blackhole::NUM_NOC_PORTS_PER_DRAM_BANK;

    const std::vector<tt_xy_pair> dram_cores = flatten_vector(tt::umd::blackhole::DRAM_CORES_NOC0);

    const size_t dram_harvesting_mask = 1;

    const HarvestingMasks harvesting_masks = {.dram_harvesting_mask = dram_harvesting_mask};
    std::shared_ptr<CoordinateManager> coordinate_manager =
        CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, true, harvesting_masks);

    const size_t physical_index = 0;
    const size_t virtual_index = (num_dram_banks - 1) * num_noc_ports_per_bank;

    const size_t harvested_translated_bank_x = tt::umd::blackhole::dram_translated_coordinate_start_x + 1;
    const size_t harvested_translated_bank_y =
        tt::umd::blackhole::dram_translated_coordinate_start_y + 3 * num_noc_ports_per_bank;

    for (size_t noc_port = 0; noc_port < num_noc_ports_per_bank; noc_port++) {
        const tt_xy_pair physical_pair = dram_cores[physical_index + noc_port];
        const tt_xy_pair virtual_pair = dram_cores[virtual_index + noc_port];

        CoreCoord physical_core = CoreCoord(physical_pair.x, physical_pair.y, CoreType::DRAM, CoordSystem::PHYSICAL);
        CoreCoord virtual_from_physical = coordinate_manager->translate_coord_to(physical_core, CoordSystem::VIRTUAL);

        CoreCoord virtual_core = CoreCoord(virtual_pair.x, virtual_pair.y, CoreType::DRAM, CoordSystem::VIRTUAL);

        EXPECT_EQ(virtual_from_physical, virtual_core);

        CoreCoord translated_core = coordinate_manager->translate_coord_to(physical_core, CoordSystem::TRANSLATED);
        CoreCoord translated_from_virtual =
            coordinate_manager->translate_coord_to(virtual_core, CoordSystem::TRANSLATED);

        EXPECT_EQ(translated_core, translated_from_virtual);

        EXPECT_EQ(translated_core.x, harvested_translated_bank_x);
        EXPECT_EQ(translated_core.y, harvested_translated_bank_y + noc_port);
    }
}

// Test that we cannot create a coordinate manager with more than one DRAM bank harvested.
TEST(CoordinateManager, CoordinateManagerBlackholeDRAMPMoreThanOneDRAMBankHarvested) {
    const size_t max_num_banks_harvested = tt::umd::blackhole::NUM_DRAM_BANKS;
    const size_t num_dram_banks = tt::umd::blackhole::NUM_DRAM_BANKS;
    const size_t num_noc_ports_per_bank = tt::umd::blackhole::NUM_NOC_PORTS_PER_DRAM_BANK;

    for (size_t dram_harvesting_mask = 0; dram_harvesting_mask < (1 << max_num_banks_harvested);
         dram_harvesting_mask++) {
        if (CoordinateManager::get_num_harvested(dram_harvesting_mask) <= 1) {
            continue;
        }

        const HarvestingMasks harvesting_masks = {.dram_harvesting_mask = dram_harvesting_mask};
        EXPECT_THROW(
            CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, true, harvesting_masks),
            std::runtime_error);
    }
}

// Test that virtual, physical and translated coordinates are the same for all logical PCIE coordinates.
TEST(CoordinateManager, CoordinateManagerBlackholePCIETranslationLocal) {
    std::shared_ptr<CoordinateManager> coordinate_manager =
        CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, true, {0, 0, 0, 0x1}, BoardType::P300, false);
    const tt_xy_pair pcie_core = {11, 0};

    const CoreCoord pcie_logical = CoreCoord(0, 0, CoreType::PCIE, CoordSystem::LOGICAL);
    const CoreCoord pcie_virtual = coordinate_manager->translate_coord_to(pcie_logical, CoordSystem::VIRTUAL);
    const CoreCoord pcie_physical = coordinate_manager->translate_coord_to(pcie_logical, CoordSystem::PHYSICAL);

    EXPECT_EQ(pcie_virtual.x, pcie_physical.x);
    EXPECT_EQ(pcie_virtual.y, pcie_physical.y);

    EXPECT_EQ(pcie_core.x, pcie_physical.x);
    EXPECT_EQ(pcie_core.y, pcie_physical.y);
}

// Test that virtual, physical and translated coordinates are the same for all logical PCIE coordinates.
TEST(CoordinateManager, CoordinateManagerBlackholePCIETranslationRemote) {
    std::shared_ptr<CoordinateManager> coordinate_manager =
        CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, true, {0, 0, 0, 0x2}, BoardType::P300, false);
    const tt_xy_pair pcie_core = {2, 0};

    const CoreCoord pcie_logical = CoreCoord(0, 0, CoreType::PCIE, CoordSystem::LOGICAL);
    const CoreCoord pcie_virtual = coordinate_manager->translate_coord_to(pcie_logical, CoordSystem::VIRTUAL);
    const CoreCoord pcie_physical = coordinate_manager->translate_coord_to(pcie_logical, CoordSystem::PHYSICAL);

    EXPECT_EQ(pcie_virtual.x, pcie_physical.x);
    EXPECT_EQ(pcie_virtual.y, pcie_physical.y);

    EXPECT_EQ(pcie_core.x, pcie_physical.x);
    EXPECT_EQ(pcie_core.y, pcie_physical.y);
}

// Test that virtual, physical and translated coordinates are the same for all logical ARC coordinates.
TEST(CoordinateManager, CoordinateManagerBlackholeARCTranslation) {
    std::shared_ptr<CoordinateManager> coordinate_manager =
        CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, true);
    const tt_xy_pair arc_grid_size = tt::umd::blackhole::ARC_GRID_SIZE;

    for (size_t x = 0; x < arc_grid_size.x; x++) {
        for (size_t y = 0; y < arc_grid_size.y; y++) {
            const CoreCoord arc_logical = CoreCoord(x, y, CoreType::ARC, CoordSystem::LOGICAL);
            const CoreCoord arc_virtual = coordinate_manager->translate_coord_to(arc_logical, CoordSystem::VIRTUAL);
            const CoreCoord arc_physical = coordinate_manager->translate_coord_to(arc_logical, CoordSystem::PHYSICAL);
            const CoreCoord arc_translated =
                coordinate_manager->translate_coord_to(arc_logical, CoordSystem::TRANSLATED);

            EXPECT_EQ(arc_virtual.x, arc_physical.x);
            EXPECT_EQ(arc_virtual.y, arc_physical.y);

            EXPECT_EQ(arc_virtual.x, arc_translated.x);
            EXPECT_EQ(arc_virtual.y, arc_translated.y);
        }
    }
}

// Test ethernet coordinate translation.
TEST(CoordinateManager, CoordinateManagerBlackholeETHTranslation) {
    std::shared_ptr<CoordinateManager> coordinate_manager =
        CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, true);
    const size_t num_eth_channels = tt::umd::blackhole::NUM_ETH_CHANNELS;

    const size_t eth_translated_coordinate_start_x = 20;
    const size_t eth_translated_coordinate_start_y = 25;

    for (size_t eth_channel = 0; eth_channel < num_eth_channels; eth_channel++) {
        const CoreCoord eth_logical = CoreCoord(0, eth_channel, CoreType::ETH, CoordSystem::LOGICAL);
        const CoreCoord eth_virtual = coordinate_manager->translate_coord_to(eth_logical, CoordSystem::VIRTUAL);
        const CoreCoord eth_physical = coordinate_manager->translate_coord_to(eth_logical, CoordSystem::PHYSICAL);
        const CoreCoord eth_translated = coordinate_manager->translate_coord_to(eth_logical, CoordSystem::TRANSLATED);

        EXPECT_EQ(eth_virtual.x, eth_physical.x);
        EXPECT_EQ(eth_virtual.y, eth_physical.y);

        EXPECT_EQ(eth_translated.x, eth_translated_coordinate_start_x + eth_channel);
        EXPECT_EQ(eth_translated.y, eth_translated_coordinate_start_y);
    }
}

// Test ETH harvesting and coordinate translation for Blackhole.
TEST(CoordinateManager, CoordinateManagerBlackholeETHHarvesting) {
    const size_t num_harvested_cores = 2;
    const std::vector<tt_xy_pair> eth_cores = tt::umd::blackhole::ETH_CORES_NOC0;
    const size_t num_eth_channels = tt::umd::blackhole::NUM_ETH_CHANNELS;
    for (size_t eth_harvesting_mask = 0; eth_harvesting_mask < (1 << num_eth_channels); eth_harvesting_mask++) {
        // We should have exactly 2 harvested ETH cores.
        if (CoordinateManager::get_num_harvested(eth_harvesting_mask) != num_harvested_cores) {
            continue;
        }

        const HarvestingMasks harvesting_masks = {.eth_harvesting_mask = eth_harvesting_mask};

        std::shared_ptr<CoordinateManager> coordinate_manager =
            CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, true, harvesting_masks);

        for (size_t eth_channel = 0; eth_channel < num_eth_channels - num_harvested_cores; eth_channel++) {
            const CoreCoord eth_logical = CoreCoord(0, eth_channel, CoreType::ETH, CoordSystem::LOGICAL);
            const CoreCoord eth_virtual = coordinate_manager->translate_coord_to(eth_logical, CoordSystem::VIRTUAL);
            const CoreCoord eth_translated =
                coordinate_manager->translate_coord_to(eth_logical, CoordSystem::TRANSLATED);

            EXPECT_EQ(eth_virtual.x, eth_cores[eth_channel].x);
            EXPECT_EQ(eth_virtual.y, eth_cores[eth_channel].y);

            EXPECT_EQ(eth_translated.x, tt::umd::blackhole::eth_translated_coordinate_start_x + eth_channel);
            EXPECT_EQ(eth_translated.y, tt::umd::blackhole::eth_translated_coordinate_start_y);
        }

        // Verify that translated coordinates for harvested cores are same as physical coordinates.
        for (size_t eth_channel = 0; eth_channel < num_eth_channels; eth_channel++) {
            if (eth_harvesting_mask & (1 << eth_channel)) {
                const CoreCoord physical_core =
                    CoreCoord(eth_cores[eth_channel].x, eth_cores[eth_channel].y, CoreType::ETH, CoordSystem::PHYSICAL);
                const CoreCoord translated_core =
                    coordinate_manager->translate_coord_to(physical_core, CoordSystem::TRANSLATED);
                EXPECT_EQ(translated_core.x, physical_core.x);
                EXPECT_EQ(translated_core.y, physical_core.y);
            }
        }
    }
}

// Test that we properly get harvesting mask that is based on the physical layout of the chip.
TEST(CoordinateManager, CoordinateManagerBlackholePhysicalLayoutTensixHarvestingMask) {
    const size_t max_num_harvested_x = 14;

    for (size_t tensix_harvesting_mask = 0; tensix_harvesting_mask < (1 << max_num_harvested_x);
         tensix_harvesting_mask++) {
        const HarvestingMasks harvesting_masks = {.tensix_harvesting_mask = tensix_harvesting_mask};
        std::shared_ptr<CoordinateManager> coordinate_manager =
            CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, true, harvesting_masks);

        EXPECT_EQ(coordinate_manager->get_harvesting_masks().tensix_harvesting_mask, tensix_harvesting_mask);
    }
}

// Test whether we properly shuffle the harvesting mask based on the physical layout of the chip.
TEST(CoordinateManager, CoordinateManagerBlackholeHarvestingShuffle) {
    for (size_t i = 0; i < tt::umd::blackhole::LOGICAL_HARVESTING_LAYOUT.size(); i++) {
        const size_t tensix_harvesting_mask_physical_layout = (1 << tt::umd::blackhole::LOGICAL_HARVESTING_LAYOUT[i]);
        const size_t tensix_harvesting_mask = CoordinateManager::shuffle_tensix_harvesting_mask(
            tt::ARCH::BLACKHOLE, tensix_harvesting_mask_physical_layout);

        EXPECT_EQ(tensix_harvesting_mask, 1 << i);
    }
}

TEST(CoordinateManager, CoordinateManagerBlackholeTranslationWithoutCoreType) {
    std::shared_ptr<CoordinateManager> coordinate_manager =
        CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, true);

    EXPECT_EQ(
        coordinate_manager->translate_coord_to({0, 0}, CoordSystem::PHYSICAL, CoordSystem::PHYSICAL).core_type,
        CoreType::DRAM);
    EXPECT_EQ(
        coordinate_manager->translate_coord_to({0, 0}, CoordSystem::VIRTUAL, CoordSystem::PHYSICAL).core_type,
        CoreType::DRAM);
    EXPECT_EQ(
        coordinate_manager->translate_coord_to({2, 2}, CoordSystem::PHYSICAL, CoordSystem::PHYSICAL).core_type,
        CoreType::TENSIX);
    // Not allowed for logical coord system.
    EXPECT_THROW(
        coordinate_manager->translate_coord_to({0, 0}, CoordSystem::LOGICAL, CoordSystem::PHYSICAL),
        std::runtime_error);
    // Throws if nothing is located at this coordinate.
    EXPECT_THROW(
        coordinate_manager->translate_coord_to({100, 100}, CoordSystem::PHYSICAL, CoordSystem::PHYSICAL),
        std::runtime_error);
}

TEST(CoordinateManager, CoordinateManagerBlackholeETHNoNocTranslationMapping) {
    std::shared_ptr<CoordinateManager> coordinate_manager =
        CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, false);

    const std::vector<tt_xy_pair> eth_pairs = tt::umd::blackhole::ETH_CORES_NOC0;
    for (const tt_xy_pair& eth_pair : eth_pairs) {
        const CoreCoord eth_core = CoreCoord(eth_pair.x, eth_pair.y, CoreType::ETH, CoordSystem::PHYSICAL);
        const CoreCoord eth_translated = coordinate_manager->translate_coord_to(eth_core, CoordSystem::TRANSLATED);

        EXPECT_EQ(eth_translated.x, eth_pair.x);
        EXPECT_EQ(eth_translated.y, eth_pair.y);
    }
}

TEST(CoordinateManager, CoordinateManagerBlackholeNoc1Noc0Mapping) {
    // clang-format off
    const static std::vector<tt_xy_pair> TENSIX_CORES_NOC1 = {
        {15, 9}, {14, 9}, {13, 9}, {12, 9}, {11, 9}, {10, 9}, {9, 9}, {6, 9}, {5, 9}, {4, 9}, {3, 9}, {2, 9}, {1, 9}, {0, 9},
        {15, 8}, {14, 8}, {13, 8}, {12, 8}, {11, 8}, {10, 8}, {9, 8}, {6, 8}, {5, 8}, {4, 8}, {3, 8}, {2, 8}, {1, 8}, {0, 8},
        {15, 7}, {14, 7}, {13, 7}, {12, 7}, {11, 7}, {10, 7}, {9, 7}, {6, 7}, {5, 7}, {4, 7}, {3, 7}, {2, 7}, {1, 7}, {0, 7},
        {15, 6}, {14, 6}, {13, 6}, {12, 6}, {11, 6}, {10, 6}, {9, 6}, {6, 6}, {5, 6}, {4, 6}, {3, 6}, {2, 6}, {1, 6}, {0, 6},
        {15, 5}, {14, 5}, {13, 5}, {12, 5}, {11, 5}, {10, 5}, {9, 5}, {6, 5}, {5, 5}, {4, 5}, {3, 5}, {2, 5}, {1, 5}, {0, 5},
        {15, 4}, {14, 4}, {13, 4}, {12, 4}, {11, 4}, {10, 4}, {9, 4}, {6, 4}, {5, 4}, {4, 4}, {3, 4}, {2, 4}, {1, 4}, {0, 4},
        {15, 3}, {14, 3}, {13, 3}, {12, 3}, {11, 3}, {10, 3}, {9, 3}, {6, 3}, {5, 3}, {4, 3}, {3, 3}, {2, 3}, {1, 3}, {0, 3},
        {15, 2}, {14, 2}, {13, 2}, {12, 2}, {11, 2}, {10, 2}, {9, 2}, {6, 2}, {5, 2}, {4, 2}, {3, 2}, {2, 2}, {1, 2}, {0, 2},
        {15, 1}, {14, 1}, {13, 1}, {12, 1}, {11, 1}, {10, 1}, {9, 1}, {6, 1}, {5, 1}, {4, 1}, {3, 1}, {2, 1}, {1, 1}, {0, 1},
        {15, 0}, {14, 0}, {13, 0}, {12, 0}, {11, 0}, {10, 0}, {9, 0}, {6, 0}, {5, 0}, {4, 0}, {3, 0}, {2, 0}, {1, 0}, {0, 0}
    };
    static const std::vector<std::vector<tt_xy_pair>> DRAM_CORES_NOC1 = {
        {{16, 11}, {16, 10}, {16, 0}},
        { {16, 9},  {16, 1}, {16, 8}},
        { {16, 2},  {16, 7}, {16, 3}},
        { {16, 6},  {16, 4}, {16, 5}},
        { {7, 11},  {7, 10},  {7, 0}},
        {  {7, 9},   {7, 1},  {7, 8}},
        {  {7, 2},   {7, 7},  {7, 3}},
        {  {7, 6},   {7, 4},  {7, 5}}
    };
    static const std::vector<tt_xy_pair> ETH_CORES_NOC1 = {
        {{15, 10},
        {0, 10},
        {14, 10},
        {1, 10},
        {13, 10},
        {2, 10},
        {12, 10},
        {3, 10},
        {11, 10},
        {4, 10},
        {10, 10},
        {5, 10},
        {9, 10},
        {6, 10}}};
    static const std::vector<tt_xy_pair> ARC_CORES_NOC1 = {{8, 11}};
    static const std::vector<tt_xy_pair> PCIE_CORES_NOC1 = {{14, 11}, {5, 11}};
    // clang-format on

    std::shared_ptr<CoordinateManager> coordinate_manager =
        CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, true);

    auto check_noc0_noc1_mapping = [coordinate_manager](
                                       const std::vector<tt_xy_pair> noc0_cores,
                                       const std::vector<tt_xy_pair> noc1_cores,
                                       const CoreType core_type) {
        for (uint32_t index = 0; index < noc0_cores.size(); index++) {
            const CoreCoord noc0_core =
                CoreCoord(noc0_cores[index].x, noc0_cores[index].y, core_type, CoordSystem::PHYSICAL);
            const CoreCoord noc1_core = coordinate_manager->translate_coord_to(noc0_core, CoordSystem::NOC1);

            EXPECT_EQ(noc1_core.x, noc1_cores[index].x);
            EXPECT_EQ(noc1_core.y, noc1_cores[index].y);

            const CoreCoord noc0_core_from_noc1 =
                coordinate_manager->translate_coord_to(noc1_core, CoordSystem::PHYSICAL);

            EXPECT_EQ(noc0_core_from_noc1.x, noc0_cores[index].x);
            EXPECT_EQ(noc0_core_from_noc1.y, noc0_cores[index].y);
        }
    };

    check_noc0_noc1_mapping(tt::umd::blackhole::TENSIX_CORES_NOC0, TENSIX_CORES_NOC1, CoreType::TENSIX);
    check_noc0_noc1_mapping(
        flatten_vector(tt::umd::blackhole::DRAM_CORES_NOC0), flatten_vector(DRAM_CORES_NOC1), CoreType::DRAM);
    check_noc0_noc1_mapping(tt::umd::blackhole::ETH_CORES_NOC0, ETH_CORES_NOC1, CoreType::ETH);
    check_noc0_noc1_mapping(tt::umd::blackhole::ARC_CORES_NOC0, ARC_CORES_NOC1, CoreType::ARC);
    check_noc0_noc1_mapping(tt::umd::blackhole::PCIE_CORES_NOC0, PCIE_CORES_NOC1, CoreType::PCIE);
}

TEST(CoordinateManager, CoordinateManagerBlackholeSecurityTranslation) {
    std::shared_ptr<CoordinateManager> coordinate_manager =
        CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, true);

    const std::vector<tt_xy_pair> security_cores = tt::umd::blackhole::SECURITY_CORES_NOC0;
    for (const auto& security_core : security_cores) {
        const CoreCoord noc0_coord =
            CoreCoord(security_core.x, security_core.y, CoreType::SECURITY, CoordSystem::PHYSICAL);

        const CoreCoord virtual_coord = coordinate_manager->translate_coord_to(noc0_coord, CoordSystem::VIRTUAL);
        const CoreCoord translated_coord = coordinate_manager->translate_coord_to(noc0_coord, CoordSystem::TRANSLATED);

        EXPECT_EQ(noc0_coord.x, virtual_coord.x);
        EXPECT_EQ(noc0_coord.y, virtual_coord.y);

        EXPECT_EQ(noc0_coord.x, translated_coord.x);
        EXPECT_EQ(noc0_coord.y, translated_coord.y);
    }
}

TEST(CoordinateManager, CoordinateManagerBlackholeL2CPUTranslation) {
    std::shared_ptr<CoordinateManager> coordinate_manager =
        CoordinateManager::create_coordinate_manager(tt::ARCH::BLACKHOLE, true);

    const std::vector<tt_xy_pair> l2cpu_cores = tt::umd::blackhole::L2CPU_CORES_NOC0;
    for (const auto& l2cpu_core : l2cpu_cores) {
        const CoreCoord noc0_coord = CoreCoord(l2cpu_core.x, l2cpu_core.y, CoreType::L2CPU, CoordSystem::PHYSICAL);
        const CoreCoord virtual_coord = coordinate_manager->translate_coord_to(noc0_coord, CoordSystem::VIRTUAL);
        const CoreCoord translated_coord = coordinate_manager->translate_coord_to(noc0_coord, CoordSystem::TRANSLATED);

        EXPECT_EQ(noc0_coord.x, virtual_coord.x);
        EXPECT_EQ(noc0_coord.y, virtual_coord.y);

        EXPECT_EQ(noc0_coord.x, translated_coord.x);
        EXPECT_EQ(noc0_coord.y, translated_coord.y);
    }
}

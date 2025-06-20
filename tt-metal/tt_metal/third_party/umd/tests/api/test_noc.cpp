// SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0

// This file holds Cluster specific API examples.

#include <gtest/gtest.h>

#include "umd/device/cluster.h"
#include "umd/device/tt_cluster_descriptor.h"

using namespace tt::umd;

TEST(TestNoc, TestNoc0NodeId) {
    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>();

    auto read_noc_id_reg = [&](std::unique_ptr<Cluster>& cluster, chip_id_t chip, CoreCoord core) {
        const uint64_t noc_node_id_offset = 0x2C;
        const uint64_t noc_node_id_reg_addr =
            cluster->get_tt_device(0)->get_architecture_implementation()->get_noc_reg_base(core.core_type, 0) +
            cluster->get_tt_device(0)->get_architecture_implementation()->get_noc_node_id_offset();
        uint32_t noc_node_id_val;
        cluster->read_from_device_reg(&noc_node_id_val, chip, core, noc_node_id_reg_addr, sizeof(noc_node_id_val));
        uint32_t x = noc_node_id_val & 0x3F;
        uint32_t y = (noc_node_id_val >> 6) & 0x3F;
        return tt_xy_pair(x, y);
    };

    auto check_noc_id_cores = [read_noc_id_reg](std::unique_ptr<Cluster>& cluster, chip_id_t chip, CoreType core_type) {
        const std::vector<CoreCoord>& cores = cluster->get_soc_descriptor(chip).get_cores(core_type);
        for (const CoreCoord& core : cores) {
            const auto [x, y] = read_noc_id_reg(cluster, chip, core);
            EXPECT_EQ(core.x, x);
            EXPECT_EQ(core.y, y);
        }
    };

    auto check_noc_id_harvested_cores = [read_noc_id_reg](
                                            std::unique_ptr<Cluster>& cluster, chip_id_t chip, CoreType core_type) {
        const std::vector<CoreCoord>& cores = cluster->get_soc_descriptor(chip).get_harvested_cores(core_type);
        for (const CoreCoord& core : cores) {
            const auto [x, y] = read_noc_id_reg(cluster, chip, core);
            EXPECT_EQ(core.x, x);
            EXPECT_EQ(core.y, y);
        }
    };

    for (chip_id_t chip : cluster->get_target_device_ids()) {
        check_noc_id_cores(cluster, chip, CoreType::TENSIX);
        check_noc_id_harvested_cores(cluster, chip, CoreType::TENSIX);

        check_noc_id_cores(cluster, chip, CoreType::ETH);
        check_noc_id_harvested_cores(cluster, chip, CoreType::ETH);

        if (cluster->get_cluster_description()->get_arch(chip) == tt::ARCH::BLACKHOLE) {
            check_noc_id_cores(cluster, chip, CoreType::DRAM);
            check_noc_id_harvested_cores(cluster, chip, CoreType::DRAM);
        }

        check_noc_id_cores(cluster, chip, CoreType::ARC);

        check_noc_id_cores(cluster, chip, CoreType::PCIE);
        check_noc_id_harvested_cores(cluster, chip, CoreType::PCIE);

        check_noc_id_cores(cluster, chip, CoreType::SECURITY);

        check_noc_id_cores(cluster, chip, CoreType::L2CPU);

        // TODO: add readouts for router cores.
    }
}

TEST(TestNoc, TestNoc1NodeId) {
    TTDevice::use_noc1(true);

    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>();

    auto read_noc_id_reg = [&](std::unique_ptr<Cluster>& cluster, chip_id_t chip, CoreCoord core) {
        const uint64_t noc_node_id_reg_addr =
            cluster->get_tt_device(0)->get_architecture_implementation()->get_noc_reg_base(core.core_type, 1) +
            cluster->get_tt_device(0)->get_architecture_implementation()->get_noc_node_id_offset();
        uint32_t noc_node_id_val;
        cluster->read_from_device_reg(&noc_node_id_val, chip, core, noc_node_id_reg_addr, sizeof(noc_node_id_val));
        uint32_t x = noc_node_id_val & 0x3F;
        uint32_t y = (noc_node_id_val >> 6) & 0x3F;
        return tt_xy_pair(x, y);
    };

    auto check_noc_id_cores = [read_noc_id_reg](std::unique_ptr<Cluster>& cluster, chip_id_t chip, CoreType core_type) {
        const std::vector<CoreCoord>& cores = cluster->get_soc_descriptor(chip).get_cores(core_type, CoordSystem::NOC1);
        for (const CoreCoord& core : cores) {
            const auto [x, y] = read_noc_id_reg(cluster, chip, core);
            EXPECT_EQ(core.x, x);
            EXPECT_EQ(core.y, y);
        }
    };

    auto check_noc_id_harvested_cores = [read_noc_id_reg](
                                            std::unique_ptr<Cluster>& cluster, chip_id_t chip, CoreType core_type) {
        const std::vector<CoreCoord>& cores =
            cluster->get_soc_descriptor(chip).get_harvested_cores(core_type, CoordSystem::NOC1);
        for (const CoreCoord& core : cores) {
            const auto [x, y] = read_noc_id_reg(cluster, chip, core);
            EXPECT_EQ(core.x, x);
            EXPECT_EQ(core.y, y);
        }
    };

    for (chip_id_t chip : cluster->get_target_device_ids()) {
        check_noc_id_cores(cluster, chip, CoreType::TENSIX);
        check_noc_id_harvested_cores(cluster, chip, CoreType::TENSIX);

        check_noc_id_cores(cluster, chip, CoreType::ETH);
        if (cluster->get_cluster_description()->get_arch(chip) != tt::ARCH::BLACKHOLE) {
            check_noc_id_harvested_cores(cluster, chip, CoreType::ETH);
        }

        if (cluster->get_cluster_description()->get_arch(chip) != tt::ARCH::WORMHOLE_B0) {
            check_noc_id_cores(cluster, chip, CoreType::DRAM);
            check_noc_id_harvested_cores(cluster, chip, CoreType::DRAM);
        }

        check_noc_id_cores(cluster, chip, CoreType::ARC);

        check_noc_id_cores(cluster, chip, CoreType::PCIE);

        // TODO: translated coordinate for harvested PCIE is not same on NOC0 and NOC1.
        // This needs to be fixed in some way in order for this to work on Blackhole
        // with enabled translation.
        if (cluster->get_cluster_description()->get_arch(chip) != tt::ARCH::BLACKHOLE) {
            check_noc_id_harvested_cores(cluster, chip, CoreType::PCIE);
        }

        check_noc_id_cores(cluster, chip, CoreType::SECURITY);

        check_noc_id_cores(cluster, chip, CoreType::L2CPU);

        // TODO: add readouts for router cores.
    }

    TTDevice::use_noc1(false);
}

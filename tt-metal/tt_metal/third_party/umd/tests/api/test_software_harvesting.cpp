// SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0

#include <memory>
#include <thread>

#include "gtest/gtest.h"
#include "tests/test_utils/device_test_utils.hpp"
#include "umd/device/blackhole_implementation.h"
#include "umd/device/cluster.h"
#include "umd/device/tt_cluster_descriptor.h"
#include "umd/device/wormhole_implementation.h"

using namespace tt::umd;

TEST(SoftwareHarvesting, TensixSoftwareHarvestingAllChips) {
    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>(ClusterOptions{
        .simulated_harvesting_masks = {0x3, 0, 0},
    });

    for (const chip_id_t& chip : cluster->get_target_device_ids()) {
        tt::ARCH arch = cluster->get_cluster_description()->get_arch(chip);

        uint32_t upper_limit_num_cores;
        if (arch == tt::ARCH::WORMHOLE_B0) {
            // At least 2 rows are expected to be harvested.
            upper_limit_num_cores = 64;
        } else if (arch == tt::ARCH::BLACKHOLE) {
            // At least 2 columns are expected to be harvested.
            upper_limit_num_cores = 120;
        }
        ASSERT_LE(cluster->get_soc_descriptor(chip).get_cores(CoreType::TENSIX).size(), upper_limit_num_cores);
    }

    for (const chip_id_t& chip : cluster->get_target_device_ids()) {
        EXPECT_TRUE((0x3 & cluster->get_soc_descriptor(chip).harvesting_masks.tensix_harvesting_mask) == 0x3);
    }
}

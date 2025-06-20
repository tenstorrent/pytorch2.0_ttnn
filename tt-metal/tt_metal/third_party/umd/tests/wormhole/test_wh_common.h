/*
 * SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#pragma once

#include "tests/test_utils/generate_cluster_desc.hpp"
#include "tests/test_utils/stimulus_generators.hpp"
#include "umd/device/cluster.h"
#include "umd/device/tt_cluster_descriptor.h"
#include "umd/device/tt_xy_pair.h"
#include "wormhole/eth_l1_address_map.h"
#include "wormhole/l1_address_map.h"

constexpr std::uint32_t DRAM_BARRIER_BASE = 0;

namespace tt::umd::test::utils {

static void set_barrier_params(Cluster& cluster) {
    // Populate address map and NOC parameters that the driver needs for memory barriers and remote transactions.
    cluster.set_barrier_address_params(
        {l1_mem::address_map::L1_BARRIER_BASE, eth_l1_mem::address_map::ERISC_BARRIER_BASE, DRAM_BARRIER_BASE});
}

class WormholeTestFixture : public ::testing::Test {
protected:
    // You can remove any or all of the following functions if their bodies would
    // be empty.

    std::unique_ptr<Cluster> cluster;

    WormholeTestFixture() {}

    ~WormholeTestFixture() override {
        // You can do clean-up work that doesn't throw exceptions here.
    }

    virtual int get_detected_num_chips() = 0;
    virtual bool is_test_skipped() = 0;

    // If the constructor and destructor are not enough for setting up
    // and cleaning up each test, you can define the following methods:

    void SetUp() override {
        // Code here will be called immediately after the constructor (right
        // before each test).

        if (is_test_skipped()) {
            GTEST_SKIP() << "Test is skipped due to incorrect number of chips";
        }

        cluster = std::make_unique<Cluster>();
        assert(cluster != nullptr);
        assert(cluster->get_cluster_description()->get_number_of_chips() == get_detected_num_chips());

        set_barrier_params(*cluster);

        tt_device_params default_params;
        cluster->start_device(default_params);

        cluster->deassert_risc_reset();

        cluster->wait_for_non_mmio_flush();
    }

    void TearDown() override {
        // Code here will be called immediately after each test (right
        // before the destructor).

        if (!is_test_skipped()) {
            cluster->close_device();
        }
    }
};

}  // namespace tt::umd::test::utils

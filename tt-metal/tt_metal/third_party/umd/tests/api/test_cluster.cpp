// SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0

// This file holds Cluster specific API examples.

#include <gtest/gtest.h>

#include <algorithm>
#include <filesystem>
#include <string>
#include <vector>

#include "fmt/xchar.h"
#include "tests/test_utils/generate_cluster_desc.hpp"
#include "umd/device/blackhole_implementation.h"
#include "umd/device/chip/local_chip.h"
#include "umd/device/chip/mock_chip.h"
#include "umd/device/cluster.h"
#include "umd/device/tt_cluster_descriptor.h"
#include "umd/device/wormhole_implementation.h"

// TODO: obviously we need some other way to set this up
#include "noc/noc_parameters.h"

using namespace tt::umd;

// These tests are intended to be run with the same code on all kinds of systems:
// N150. N300
// Galaxy

constexpr std::uint32_t L1_BARRIER_BASE = 12;
constexpr std::uint32_t ETH_BARRIER_BASE = 256 * 1024 - 32;
constexpr std::uint32_t DRAM_BARRIER_BASE = 0;

// This test should be one line only.
TEST(ApiClusterTest, OpenAllChips) { std::unique_ptr<Cluster> umd_cluster = std::make_unique<Cluster>(); }

TEST(ApiClusterTest, OpenChipsByPciId) {
    std::vector<int> pci_device_ids = PCIDevice::enumerate_devices();

    // T3K and 4U have 4 PCIE visible devices each. After 4 devices, the next number is 32
    // on 6U galaxies. Making 2^32 combinations might take too long, so we limit the number of devices to 4.
    // TODO: test all combinations on 6U and remove this check if possible.
    if (pci_device_ids.size() > 4) {
        GTEST_SKIP() << "Skipping test because there are more than 4 PCI devices. "
                        "This test is intended to be run on all systems apart from 6U.";
    }

    int total_combinations = 1 << pci_device_ids.size();

    for (uint32_t combination = 0; combination < total_combinations; combination++) {
        std::unordered_set<int> target_pci_device_ids;
        for (int i = 0; i < pci_device_ids.size(); i++) {
            if (combination & (1 << i)) {
                target_pci_device_ids.insert(pci_device_ids[i]);
            }
        }

        std::cout << "Creating Cluster with target PCI device IDs: ";
        for (const auto& id : target_pci_device_ids) {
            std::cout << id << " ";
        }
        std::cout << std::endl;

        // Make sure that Cluster construction is without exceptions.
        // TODO: add cluster descriptors for expected topologies, compare cluster desc against expected desc.
        std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>(ClusterOptions{
            .pci_target_devices = target_pci_device_ids,
        });
    }
}

TEST(ApiClusterTest, DifferentConstructors) {
    std::unique_ptr<Cluster> umd_cluster;

    // 1. Simplest constructor. Creates Cluster with all the chips available.
    umd_cluster = std::make_unique<Cluster>();
    bool chips_available = !umd_cluster->get_target_device_ids().empty();
    umd_cluster = nullptr;

    if (chips_available) {
        // 2. Constructor which allows choosing a subset of Chips to open.
        umd_cluster = std::make_unique<Cluster>(ClusterOptions{
            .target_devices = {0},
        });
        EXPECT_EQ(umd_cluster->get_target_device_ids().size(), 1);
        umd_cluster = nullptr;

        // 3. Constructor taking a custom soc descriptor in addition.
        tt::ARCH device_arch = Cluster::create_cluster_descriptor()->get_arch(0);
        // You can add a custom soc descriptor here.
        std::string sdesc_path = tt_SocDescriptor::get_soc_descriptor_path(device_arch);
        umd_cluster = std::make_unique<Cluster>(ClusterOptions{
            .sdesc_path = sdesc_path,
        });
        umd_cluster = nullptr;
    }

    // 4. Constructor taking cluster descriptor based on which to create cluster.
    // This could be cluster descriptor cached from previous runtime, or with some custom modifications.
    // You can just create a cluster descriptor and serialize it to file, or fetch a cluster descriptor from already
    // created Cluster class.
    std::filesystem::path cluster_path1 = tt::umd::Cluster::create_cluster_descriptor()->serialize_to_file();
    umd_cluster = std::make_unique<Cluster>();
    std::filesystem::path cluster_path2 = umd_cluster->get_cluster_description()->serialize_to_file();
    umd_cluster = nullptr;

    std::unique_ptr<tt_ClusterDescriptor> cluster_desc = tt_ClusterDescriptor::create_from_yaml(cluster_path1);
    umd_cluster = std::make_unique<Cluster>(ClusterOptions{
        .cluster_descriptor = cluster_desc.get(),
    });
    umd_cluster = nullptr;

    // 5. Create mock chips is set to true in order to create mock chips for the devices in the cluster descriptor.
    umd_cluster = std::make_unique<Cluster>(ClusterOptions{
        .chip_type = ChipType::MOCK,
        .target_devices = {0},
    });
    umd_cluster = nullptr;
}

TEST(ApiClusterTest, SimpleIOAllChips) {
    std::unique_ptr<Cluster> umd_cluster = std::make_unique<Cluster>();

    const tt_ClusterDescriptor* cluster_desc = umd_cluster->get_cluster_description();

    // Initialize random data.
    size_t data_size = 1024;
    std::vector<uint8_t> data(data_size, 0);
    for (int i = 0; i < data_size; i++) {
        data[i] = i % 256;
    }

    // Setup memory barrier addresses.
    // Some default values are set during construction of UMD, but you can override them.
    umd_cluster->set_barrier_address_params({L1_BARRIER_BASE, ETH_BARRIER_BASE, DRAM_BARRIER_BASE});

    for (auto chip_id : umd_cluster->get_target_device_ids()) {
        const tt_SocDescriptor& soc_desc = umd_cluster->get_soc_descriptor(chip_id);

        CoreCoord any_core = soc_desc.get_cores(CoreType::TENSIX)[0];

        std::cout << "Writing to chip " << chip_id << " core " << any_core.str() << std::endl;

        umd_cluster->write_to_device(data.data(), data_size, chip_id, any_core, 0);

        umd_cluster->wait_for_non_mmio_flush(chip_id);
    }

    // Now read back the data.
    for (auto chip_id : umd_cluster->get_target_device_ids()) {
        const tt_SocDescriptor& soc_desc = umd_cluster->get_soc_descriptor(chip_id);

        CoreCoord any_core = soc_desc.get_cores(CoreType::TENSIX)[0];

        std::cout << "Reading from chip " << chip_id << " core " << any_core.str() << std::endl;

        std::vector<uint8_t> readback_data(data_size, 0);
        umd_cluster->read_from_device(readback_data.data(), chip_id, any_core, 0, data_size);

        ASSERT_EQ(data, readback_data);
    }
}

TEST(ApiClusterTest, RemoteFlush) {
    std::unique_ptr<Cluster> umd_cluster = std::make_unique<Cluster>();

    const tt_ClusterDescriptor* cluster_desc = umd_cluster->get_cluster_description();

    size_t data_size = 1024;
    std::vector<uint8_t> data(data_size, 0);

    // Setup memory barrier addresses.
    // Some default values are set during construction of UMD, but you can override them.
    umd_cluster->set_barrier_address_params({L1_BARRIER_BASE, ETH_BARRIER_BASE, DRAM_BARRIER_BASE});

    for (auto chip_id : umd_cluster->get_target_remote_device_ids()) {
        const tt_SocDescriptor& soc_desc = umd_cluster->get_soc_descriptor(chip_id);

        const CoreCoord any_core = soc_desc.get_cores(CoreType::TENSIX)[0];

        if (!cluster_desc->is_chip_remote(chip_id)) {
            std::cout << "Chip " << chip_id << " skipped because it is not a remote chip." << std::endl;
            continue;
        }

        if (soc_desc.arch != tt::ARCH::WORMHOLE_B0) {
            std::cout << "Skipping remote chip " << chip_id << " because it is not a wormhole_b0 chip." << std::endl;
            continue;
        }

        std::cout << "Writing to chip " << chip_id << " core " << any_core.str() << std::endl;
        umd_cluster->write_to_device(data.data(), data_size, chip_id, any_core, 0);

        std::cout << "Waiting for remote chip flush " << chip_id << std::endl;
        umd_cluster->wait_for_non_mmio_flush(chip_id);

        std::cout << "Reading from chip " << chip_id << " core " << any_core.str() << std::endl;
        std::vector<uint8_t> readback_data(data_size, 0);
        umd_cluster->read_from_device(readback_data.data(), chip_id, any_core, 0, data_size);

        ASSERT_EQ(data, readback_data);
    }
}

TEST(ApiClusterTest, SimpleIOSpecificChips) {
    std::unique_ptr<Cluster> umd_cluster = std::make_unique<Cluster>();

    if (umd_cluster->get_target_device_ids().empty()) {
        GTEST_SKIP() << "No chips present on the system. Skipping test.";
    }

    umd_cluster = std::make_unique<Cluster>(ClusterOptions{
        .target_devices = {0},
    });

    const tt_ClusterDescriptor* cluster_desc = umd_cluster->get_cluster_description();

    // Initialize random data.
    size_t data_size = 1024;
    std::vector<uint8_t> data(data_size, 0);
    for (int i = 0; i < data_size; i++) {
        data[i] = i % 256;
    }

    // Setup memory barrier addresses.
    // Some default values are set during construction of UMD, but you can override them.
    umd_cluster->set_barrier_address_params({L1_BARRIER_BASE, ETH_BARRIER_BASE, DRAM_BARRIER_BASE});

    for (auto chip_id : umd_cluster->get_target_device_ids()) {
        const tt_SocDescriptor& soc_desc = umd_cluster->get_soc_descriptor(chip_id);

        CoreCoord any_core = soc_desc.get_cores(CoreType::TENSIX)[0];

        std::cout << "Writing to chip " << chip_id << " core " << any_core.str() << std::endl;

        umd_cluster->write_to_device(data.data(), data_size, chip_id, any_core, 0);

        umd_cluster->wait_for_non_mmio_flush(chip_id);
    }

    // Now read back the data.
    for (auto chip_id : umd_cluster->get_target_device_ids()) {
        const tt_SocDescriptor& soc_desc = umd_cluster->get_soc_descriptor(chip_id);

        const CoreCoord any_core = soc_desc.get_cores(CoreType::TENSIX)[0];

        std::cout << "Reading from chip " << chip_id << " core " << any_core.str() << std::endl;

        std::vector<uint8_t> readback_data(data_size, 0);
        umd_cluster->read_from_device(readback_data.data(), chip_id, any_core, 0, data_size);

        ASSERT_EQ(data, readback_data);
    }
}

TEST(ClusterAPI, DynamicTLB_RW) {
    // Don't use any static TLBs in this test. All writes go through a dynamic TLB that needs to be reconfigured for
    // each transaction

    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>();

    tt_device_params default_params;
    cluster->start_device(default_params);

    std::vector<uint32_t> vector_to_write = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    std::vector<uint32_t> zeros = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    std::vector<uint32_t> readback_vec = zeros;

    static const uint32_t num_loops = 100;

    for (const chip_id_t chip : cluster->get_target_device_ids()) {
        // Just make sure to skip L1_BARRIER_BASE
        std::uint32_t address = 0x100;
        // Write to each core a 100 times at different statically mapped addresses
        const tt_SocDescriptor& soc_desc = cluster->get_soc_descriptor(chip);
        std::vector<CoreCoord> tensix_cores = soc_desc.get_cores(CoreType::TENSIX);
        for (int loop = 0; loop < num_loops; loop++) {
            for (auto& core : tensix_cores) {
                cluster->write_to_device(
                    vector_to_write.data(), vector_to_write.size() * sizeof(std::uint32_t), chip, core, address);

                // Barrier to ensure that all writes over ethernet were commited
                cluster->wait_for_non_mmio_flush();
                cluster->read_from_device(readback_vec.data(), chip, core, address, 40);

                ASSERT_EQ(vector_to_write, readback_vec)
                    << "Vector read back from core " << core.x << "-" << core.y << "does not match what was written";

                cluster->wait_for_non_mmio_flush();

                cluster->write_to_device(zeros.data(), zeros.size() * sizeof(std::uint32_t), chip, core, address);

                cluster->wait_for_non_mmio_flush();

                readback_vec = zeros;
            }
            address += 0x20;  // Increment by uint32_t size for each write
        }
    }
    cluster->close_device();
}

TEST(TestCluster, PrintAllChipsAllCores) {
    std::unique_ptr<Cluster> umd_cluster = std::make_unique<Cluster>();

    for (chip_id_t chip : umd_cluster->get_target_device_ids()) {
        std::cout << "Chip " << chip << std::endl;

        const tt_SocDescriptor& soc_desc = umd_cluster->get_soc_descriptor(chip);

        const std::vector<CoreCoord>& tensix_cores = soc_desc.get_cores(CoreType::TENSIX);
        for (const CoreCoord& core : tensix_cores) {
            std::cout << "Tensix core " << core.str() << std::endl;
        }

        const std::vector<CoreCoord>& harvested_tensix_cores = soc_desc.get_harvested_cores(CoreType::TENSIX);
        for (const CoreCoord& core : harvested_tensix_cores) {
            std::cout << "Harvested Tensix core " << core.str() << std::endl;
        }

        const std::vector<CoreCoord>& dram_cores = soc_desc.get_cores(CoreType::DRAM);
        for (const CoreCoord& core : dram_cores) {
            std::cout << "DRAM core " << core.str() << std::endl;
        }

        const std::vector<CoreCoord>& harvested_dram_cores = soc_desc.get_harvested_cores(CoreType::DRAM);
        for (const CoreCoord& core : harvested_dram_cores) {
            std::cout << "Harvested DRAM core " << core.str() << std::endl;
        }

        const std::vector<CoreCoord>& eth_cores = soc_desc.get_cores(CoreType::ETH);
        for (const CoreCoord& core : eth_cores) {
            std::cout << "ETH core " << core.str() << std::endl;
        }

        const std::vector<CoreCoord>& harvested_eth_cores = soc_desc.get_harvested_cores(CoreType::ETH);
        for (const CoreCoord& core : harvested_eth_cores) {
            std::cout << "Harvested ETH core " << core.str() << std::endl;
        }
    }
}

// It is expected that logical ETH channel numbers are in the range [0, num_channels) for each
// chip. This is needed because of eth id readouts for Blackhole that don't take harvesting into
// acount. This test verifies that both for Wormhole and Blackhole.
TEST(TestCluster, TestClusterLogicalETHChannelsConnectivity) {
    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>();

    tt_ClusterDescriptor* cluster_desc = cluster->get_cluster_description();

    for (auto [chip, connections] : cluster_desc->get_ethernet_connections()) {
        const uint32_t num_channels_local_chip = cluster->get_soc_descriptor(chip).get_cores(CoreType::ETH).size();
        for (auto [channel, remote_chip_and_channel] : connections) {
            auto [remote_chip, remote_channel] = remote_chip_and_channel;

            const uint32_t num_channels_remote_chip =
                cluster->get_soc_descriptor(remote_chip).get_cores(CoreType::ETH).size();

            EXPECT_TRUE(channel < num_channels_local_chip);
            EXPECT_TRUE(remote_channel < num_channels_remote_chip);
        }
    }
}

TEST(TestCluster, TestClusterAICLKControl) {
    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>();

    auto get_expected_clock_val = [&cluster](chip_id_t chip_id, bool busy) {
        tt::ARCH arch = cluster->get_cluster_description()->get_arch(chip_id);
        if (arch == tt::ARCH::WORMHOLE_B0) {
            return busy ? tt::umd::wormhole::AICLK_BUSY_VAL : tt::umd::wormhole::AICLK_IDLE_VAL;
        } else if (arch == tt::ARCH::BLACKHOLE) {
            return busy ? tt::umd::blackhole::AICLK_BUSY_VAL : tt::umd::blackhole::AICLK_IDLE_VAL;
        }
        return 0u;
    };

    cluster->set_power_state(tt_DevicePowerState::BUSY);

    auto clocks_busy = cluster->get_clocks();
    for (auto& clock : clocks_busy) {
        // TODO #781: Figure out a proper mechanism to detect the right value. For now just check that Busy value is
        // larger than Idle value.
        EXPECT_GT(clock.second, get_expected_clock_val(clock.first, false));
    }

    cluster->set_power_state(tt_DevicePowerState::LONG_IDLE);

    auto clocks_idle = cluster->get_clocks();
    for (auto& clock : clocks_idle) {
        EXPECT_EQ(clock.second, get_expected_clock_val(clock.first, false));
    }
}

TEST(TestCluster, ReadWriteL1) {
    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>();

    if (cluster->get_target_device_ids().empty()) {
        GTEST_SKIP() << "No chips present on the system. Skipping test.";
    }

    auto tensix_l1_size = cluster->get_soc_descriptor(0).worker_l1_size;

    std::vector<uint8_t> zero_data(tensix_l1_size, 0);
    std::vector<uint8_t> data(tensix_l1_size, 0);
    for (int i = 0; i < tensix_l1_size; i++) {
        data[i] = i % 256;
    }

    // Set elements to 1 since the first readback will be of zero data, so want to confirm that
    // elements actually changed.
    std::vector<uint8_t> readback_data(tensix_l1_size, 1);

    for (auto chip_id : cluster->get_target_device_ids()) {
        const tt_SocDescriptor& soc_desc = cluster->get_soc_descriptor(chip_id);

        std::vector<CoreCoord> tensix_cores = cluster->get_soc_descriptor(chip_id).get_cores(CoreType::TENSIX);

        for (const CoreCoord& tensix_core : tensix_cores) {
            // Zero out L1.
            cluster->write_to_device(zero_data.data(), zero_data.size(), chip_id, tensix_core, 0);

            cluster->wait_for_non_mmio_flush(chip_id);

            cluster->read_from_device(readback_data.data(), chip_id, tensix_core, 0, tensix_l1_size);

            EXPECT_EQ(zero_data, readback_data);

            cluster->write_to_device(data.data(), data.size(), chip_id, tensix_core, 0);

            cluster->wait_for_non_mmio_flush(chip_id);

            cluster->read_from_device(readback_data.data(), chip_id, tensix_core, 0, tensix_l1_size);

            EXPECT_EQ(data, readback_data);
        }
    }
}

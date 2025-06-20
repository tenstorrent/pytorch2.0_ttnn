// SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0
#include <memory>
#include <thread>

#include "gtest/gtest.h"
#include "tests/test_utils/device_test_utils.hpp"
#include "tests/test_utils/generate_cluster_desc.hpp"
#include "umd/device/cluster.h"
#include "umd/device/tt_cluster_descriptor.h"
#include "umd/device/wormhole_implementation.h"
#include "wormhole/eth_l1_address_map.h"
#include "wormhole/host_mem_address_map.h"
#include "wormhole/l1_address_map.h"

using namespace tt::umd;

constexpr std::uint32_t DRAM_BARRIER_BASE = 0;

static void set_barrier_params(Cluster& cluster) {
    // Populate address map and NOC parameters that the driver needs for memory barriers and remote transactions.
    cluster.set_barrier_address_params(
        {l1_mem::address_map::L1_BARRIER_BASE, eth_l1_mem::address_map::ERISC_BARRIER_BASE, DRAM_BARRIER_BASE});
}

std::int32_t get_static_tlb_index(tt_xy_pair target) {
    bool is_eth_location =
        std::find(std::cbegin(tt::umd::wormhole::ETH_LOCATIONS), std::cend(tt::umd::wormhole::ETH_LOCATIONS), target) !=
        std::cend(tt::umd::wormhole::ETH_LOCATIONS);
    bool is_tensix_location =
        std::find(
            std::cbegin(tt::umd::wormhole::T6_X_LOCATIONS), std::cend(tt::umd::wormhole::T6_X_LOCATIONS), target.x) !=
            std::cend(tt::umd::wormhole::T6_X_LOCATIONS) &&
        std::find(
            std::cbegin(tt::umd::wormhole::T6_Y_LOCATIONS), std::cend(tt::umd::wormhole::T6_Y_LOCATIONS), target.y) !=
            std::cend(tt::umd::wormhole::T6_Y_LOCATIONS);
    if (is_eth_location) {
        if (target.y == 6) {
            target.y = 1;
        }

        if (target.x >= 5) {
            target.x -= 1;
        }
        target.x -= 1;

        int flat_index = target.y * 8 + target.x;
        int tlb_index = flat_index;
        return tlb_index;

    } else if (is_tensix_location) {
        if (target.x >= 5) {
            target.x -= 1;
        }
        target.x -= 1;

        if (target.y >= 6) {
            target.y -= 1;
        }
        target.y -= 1;

        int flat_index = target.y * 8 + target.x;

        // All 80 get single 1MB TLB.
        int tlb_index = tt::umd::wormhole::ETH_LOCATIONS.size() + flat_index;

        return tlb_index;
    } else {
        return -1;
    }
}

TEST(SiliconDriverWH, CreateDestroy) {
    tt_device_params default_params;
    // Initialize the driver with a 1x1 descriptor and explictly do not perform harvesting
    for (int i = 0; i < 50; i++) {
        Cluster cluster(ClusterOptions{
            .perform_harvesting = false,
            .sdesc_path = test_utils::GetAbsPath("tests/soc_descs/wormhole_b0_1x1.yaml"),
        });
        set_barrier_params(cluster);

        // TODO: this test fails on new UBB galaxy if the two lines are uncommented.
        // Generally we don't want to call start_device and close_device in tests.
        // Implement loading ebreak code before each test.
        // cluster.start_device(default_params);
        // cluster.close_device();
    }
}

TEST(SiliconDriverWH, CustomSocDesc) {
    // Initialize the driver with a 1x1 descriptor and explictly do not perform harvesting
    Cluster cluster(ClusterOptions{
        .perform_harvesting = false,
        .simulated_harvesting_masks = {60, 0, 0},
        .simulated_harvesting_masks_per_chip = {{0, {30, 0, 0}}, {1, {60, 0, 0}}},
        .sdesc_path = test_utils::GetAbsPath("tests/soc_descs/wormhole_b0_1x1.yaml"),
    });
    for (const auto& chip : cluster.get_target_device_ids()) {
        ASSERT_EQ(cluster.get_soc_descriptor(chip).get_cores(CoreType::TENSIX).size(), 1)
            << "Expected 1x1 SOC descriptor to be unmodified by driver";
    }
}

TEST(SiliconDriverWH, HarvestingRuntime) {
    auto get_static_tlb_index_callback = [](tt_xy_pair target) { return get_static_tlb_index(target); };

    Cluster cluster(ClusterOptions{
        .simulated_harvesting_masks = {60, 0, 0},
        .simulated_harvesting_masks_per_chip = {{0, {30, 0, 0}}, {1, {60, 0, 0}}},
    });
    set_barrier_params(cluster);
    auto mmio_devices = cluster.get_target_mmio_device_ids();

    // Iterate over MMIO devices and only setup static TLBs for worker cores
    for (auto chip_id : mmio_devices) {
        auto& sdesc = cluster.get_soc_descriptor(chip_id);
        for (const CoreCoord& core : sdesc.get_cores(CoreType::TENSIX)) {
            // Statically mapping a 1MB TLB to this core, starting from address NCRISC_FIRMWARE_BASE.
            cluster.configure_tlb(
                chip_id,
                core,
                get_static_tlb_index_callback(sdesc.translate_coord_to(core, CoordSystem::VIRTUAL)),
                l1_mem::address_map::NCRISC_FIRMWARE_BASE);
        }
    }

    tt_device_params default_params;
    cluster.start_device(default_params);

    std::vector<uint32_t> vector_to_write = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    std::vector<uint32_t> dynamic_readback_vec = {};
    std::vector<uint32_t> readback_vec = {};
    std::vector<uint32_t> zeros = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

    for (auto chip_id : cluster.get_target_device_ids()) {
        std::uint32_t address = l1_mem::address_map::NCRISC_FIRMWARE_BASE;
        std::uint32_t dynamic_write_address = 0x40000000;
        for (int loop = 0; loop < 100;
             loop++) {  // Write to each core a 100 times at different statically mapped addresses
            for (const CoreCoord& core : cluster.get_soc_descriptor(chip_id).get_cores(CoreType::TENSIX)) {
                cluster.write_to_device(
                    vector_to_write.data(), vector_to_write.size() * sizeof(std::uint32_t), chip_id, core, address);
                cluster.write_to_device(
                    vector_to_write.data(),
                    vector_to_write.size() * sizeof(std::uint32_t),
                    chip_id,
                    core,
                    dynamic_write_address);
                cluster.wait_for_non_mmio_flush();  // Barrier to ensure that all writes over ethernet were commited

                test_utils::read_data_from_device(cluster, readback_vec, chip_id, core, address, 40);
                test_utils::read_data_from_device(
                    cluster, dynamic_readback_vec, chip_id, core, dynamic_write_address, 40);
                ASSERT_EQ(vector_to_write, readback_vec)
                    << "Vector read back from core " << core.str() << " does not match what was written";
                ASSERT_EQ(vector_to_write, dynamic_readback_vec)
                    << "Vector read back from core " << core.str() << " does not match what was written";
                cluster.wait_for_non_mmio_flush();

                cluster.write_to_device(
                    zeros.data(),
                    zeros.size() * sizeof(std::uint32_t),
                    chip_id,
                    core,
                    dynamic_write_address);  // Clear any written data
                cluster.write_to_device(
                    zeros.data(),
                    zeros.size() * sizeof(std::uint32_t),
                    chip_id,
                    core,
                    address);  // Clear any written data
                cluster.wait_for_non_mmio_flush();
                readback_vec = {};
                dynamic_readback_vec = {};
            }
            address += 0x20;  // Increment by uint32_t size for each write
            dynamic_write_address += 0x20;
        }
    }
    cluster.close_device();
}

TEST(SiliconDriverWH, UnalignedStaticTLB_RW) {
    auto get_static_tlb_index_callback = [](tt_xy_pair target) { return get_static_tlb_index(target); };

    Cluster cluster;
    set_barrier_params(cluster);
    auto mmio_devices = cluster.get_target_mmio_device_ids();

    // Iterate over MMIO devices and only setup static TLBs for worker cores
    for (auto chip_id : mmio_devices) {
        auto& sdesc = cluster.get_soc_descriptor(chip_id);
        for (const CoreCoord& core : sdesc.get_cores(CoreType::TENSIX)) {
            // Statically mapping a 1MB TLB to this core, starting from address NCRISC_FIRMWARE_BASE.
            cluster.configure_tlb(
                chip_id,
                core,
                get_static_tlb_index_callback(sdesc.translate_coord_to(core, CoordSystem::VIRTUAL)),
                l1_mem::address_map::NCRISC_FIRMWARE_BASE);
        }
    }

    tt_device_params default_params;
    cluster.start_device(default_params);

    std::vector<uint32_t> unaligned_sizes = {3, 14, 21, 255, 362, 430, 1022, 1023, 1025};
    for (auto chip_id : cluster.get_target_device_ids()) {
        for (const auto& size : unaligned_sizes) {
            std::vector<uint8_t> write_vec(size, 0);
            for (int i = 0; i < size; i++) {
                write_vec[i] = size + i;
            }
            std::vector<uint8_t> readback_vec(size, 0);
            std::uint32_t address = l1_mem::address_map::NCRISC_FIRMWARE_BASE;
            for (int loop = 0; loop < 50; loop++) {
                for (const CoreCoord& core : cluster.get_soc_descriptor(chip_id).get_cores(CoreType::TENSIX)) {
                    cluster.write_to_device(write_vec.data(), size, chip_id, core, address);
                    cluster.wait_for_non_mmio_flush();
                    cluster.read_from_device(readback_vec.data(), chip_id, core, address, size);
                    ASSERT_EQ(readback_vec, write_vec);
                    readback_vec = std::vector<uint8_t>(size, 0);
                    cluster.write_to_sysmem(write_vec.data(), size, 0, 0, 0);
                    cluster.read_from_sysmem(readback_vec.data(), 0, 0, size, 0);
                    ASSERT_EQ(readback_vec, write_vec);
                    readback_vec = std::vector<uint8_t>(size, 0);
                    cluster.wait_for_non_mmio_flush();
                }
                address += 0x20;
            }
        }
    }
    cluster.close_device();
}

TEST(SiliconDriverWH, StaticTLB_RW) {
    auto get_static_tlb_index_callback = [](tt_xy_pair target) { return get_static_tlb_index(target); };

    Cluster cluster;
    set_barrier_params(cluster);
    auto mmio_devices = cluster.get_target_mmio_device_ids();

    // Iterate over MMIO devices and only setup static TLBs for worker cores
    for (auto chip_id : mmio_devices) {
        auto& sdesc = cluster.get_soc_descriptor(chip_id);
        for (const CoreCoord& core : sdesc.get_cores(CoreType::TENSIX)) {
            // Statically mapping a 1MB TLB to this core, starting from address NCRISC_FIRMWARE_BASE.
            cluster.configure_tlb(
                chip_id,
                core,
                get_static_tlb_index_callback(sdesc.translate_coord_to(core, CoordSystem::VIRTUAL)),
                l1_mem::address_map::NCRISC_FIRMWARE_BASE);
        }
    }

    tt_device_params default_params;
    cluster.start_device(default_params);

    std::vector<uint32_t> vector_to_write = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    std::vector<uint32_t> readback_vec = {};
    std::vector<uint32_t> zeros = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    // Check functionality of Static TLBs by reading adn writing from statically mapped address space
    for (auto chip_id : cluster.get_target_device_ids()) {
        std::uint32_t address = l1_mem::address_map::NCRISC_FIRMWARE_BASE;
        // Write to each core a 100 times at different statically mapped addresses
        for (int loop = 0; loop < 100; loop++) {
            for (const CoreCoord& core : cluster.get_soc_descriptor(chip_id).get_cores(CoreType::TENSIX)) {
                cluster.write_to_device(
                    vector_to_write.data(), vector_to_write.size() * sizeof(std::uint32_t), chip_id, core, address);
                // Barrier to ensure that all writes over ethernet were commited
                cluster.wait_for_non_mmio_flush();
                test_utils::read_data_from_device(cluster, readback_vec, chip_id, core, address, 40);
                ASSERT_EQ(vector_to_write, readback_vec)
                    << "Vector read back from core " << core.str() << " does not match what was written";
                cluster.wait_for_non_mmio_flush();
                cluster.write_to_device(
                    zeros.data(),
                    zeros.size() * sizeof(std::uint32_t),
                    chip_id,
                    core,
                    address);  // Clear any written data
                cluster.wait_for_non_mmio_flush();
                readback_vec = {};
            }
            address += 0x20;  // Increment by uint32_t size for each write
        }
    }
    cluster.close_device();
}

TEST(SiliconDriverWH, DynamicTLB_RW) {
    // Don't use any static TLBs in this test. All writes go through a dynamic TLB that needs to be reconfigured for
    // each transaction
    Cluster cluster;

    set_barrier_params(cluster);

    tt_device_params default_params;
    cluster.start_device(default_params);

    std::vector<uint32_t> vector_to_write = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    std::vector<uint32_t> zeros = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    std::vector<uint32_t> readback_vec = {};

    for (auto chip_id : cluster.get_target_device_ids()) {
        std::uint32_t address = l1_mem::address_map::NCRISC_FIRMWARE_BASE;
        // Write to each core a 100 times at different statically mapped addresses
        for (int loop = 0; loop < 100; loop++) {
            for (const CoreCoord& core : cluster.get_soc_descriptor(chip_id).get_cores(CoreType::TENSIX)) {
                cluster.write_to_device(
                    vector_to_write.data(), vector_to_write.size() * sizeof(std::uint32_t), chip_id, core, address);
                // Barrier to ensure that all writes over ethernet were commited
                cluster.wait_for_non_mmio_flush();
                test_utils::read_data_from_device(cluster, readback_vec, chip_id, core, address, 40);
                ASSERT_EQ(vector_to_write, readback_vec)
                    << "Vector read back from core " << core.str() << " does not match what was written";
                cluster.wait_for_non_mmio_flush();
                cluster.write_to_device(zeros.data(), zeros.size() * sizeof(std::uint32_t), chip_id, core, address);
                cluster.wait_for_non_mmio_flush();
                readback_vec = {};
            }
            address += 0x20;  // Increment by uint32_t size for each write
        }
    }
    cluster.close_device();
}

TEST(SiliconDriverWH, MultiThreadedDevice) {
    // Have 2 threads read and write from a single device concurrently
    // All transactions go through a single Dynamic TLB. We want to make sure this is thread/process safe
    Cluster cluster;
    set_barrier_params(cluster);

    tt_device_params default_params;
    cluster.start_device(default_params);

    std::thread th1 = std::thread([&] {
        std::vector<uint32_t> vector_to_write = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        std::vector<uint32_t> readback_vec = {};
        std::uint32_t address = l1_mem::address_map::NCRISC_FIRMWARE_BASE;
        for (int loop = 0; loop < 100; loop++) {
            for (const CoreCoord& core : cluster.get_soc_descriptor(0).get_cores(CoreType::TENSIX)) {
                cluster.write_to_device(
                    vector_to_write.data(), vector_to_write.size() * sizeof(std::uint32_t), 0, core, address);
                test_utils::read_data_from_device(cluster, readback_vec, 0, core, address, 40);
                ASSERT_EQ(vector_to_write, readback_vec)
                    << "Vector read back from core " << core.str() << " does not match what was written";
                readback_vec = {};
            }
            address += 0x20;
        }
    });

    std::thread th2 = std::thread([&] {
        std::vector<uint32_t> vector_to_write = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        std::vector<uint32_t> readback_vec = {};
        std::uint32_t address = 0x30000000;
        for (const std::vector<CoreCoord>& core_ls : cluster.get_soc_descriptor(0).get_dram_cores()) {
            for (int loop = 0; loop < 100; loop++) {
                for (const CoreCoord& core : core_ls) {
                    cluster.write_to_device(
                        vector_to_write.data(), vector_to_write.size() * sizeof(std::uint32_t), 0, core, address);
                    test_utils::read_data_from_device(cluster, readback_vec, 0, core, address, 40);
                    ASSERT_EQ(vector_to_write, readback_vec)
                        << "Vector read back from core " << core.str() << " does not match what was written";
                    readback_vec = {};
                }
                address += 0x20;
            }
        }
    });

    th1.join();
    th2.join();
    cluster.close_device();
}

TEST(SiliconDriverWH, MultiThreadedMemBar) {
    // Have 2 threads read and write from a single device concurrently
    // All (fairly large) transactions go through a static TLB.
    // We want to make sure the memory barrier is thread/process safe.

    // Memory barrier flags get sent to address 0 for all channels in this test
    auto get_static_tlb_index_callback = [](tt_xy_pair target) { return get_static_tlb_index(target); };
    uint32_t base_addr = l1_mem::address_map::DATA_BUFFER_SPACE_BASE;

    Cluster cluster;
    set_barrier_params(cluster);
    auto mmio_devices = cluster.get_target_mmio_device_ids();

    // Iterate over MMIO devices and only setup static TLBs for worker cores
    for (auto chip_id : mmio_devices) {
        auto& sdesc = cluster.get_soc_descriptor(chip_id);
        for (const CoreCoord& core : sdesc.get_cores(CoreType::TENSIX)) {
            // Statically mapping a 1MB TLB to this core, starting from address DATA_BUFFER_SPACE_BASE.
            cluster.configure_tlb(
                chip_id,
                core,
                get_static_tlb_index_callback(sdesc.translate_coord_to(core, CoordSystem::VIRTUAL)),
                base_addr);
        }
    }

    tt_device_params default_params;
    cluster.start_device(default_params);

    std::vector<uint32_t> readback_membar_vec = {};
    for (const CoreCoord& core : cluster.get_soc_descriptor(0).get_cores(CoreType::TENSIX)) {
        test_utils::read_data_from_device(
            cluster, readback_membar_vec, 0, core, l1_mem::address_map::L1_BARRIER_BASE, 4);
        ASSERT_EQ(
            readback_membar_vec.at(0), 187);  // Ensure that memory barriers were correctly initialized on all workers
        readback_membar_vec = {};
    }

    for (int chan = 0; chan < cluster.get_soc_descriptor(0).get_num_dram_channels(); chan++) {
        CoreCoord core = cluster.get_soc_descriptor(0).get_dram_core_for_channel(chan, 0, CoordSystem::VIRTUAL);
        test_utils::read_data_from_device(cluster, readback_membar_vec, 0, core, 0, 4);
        ASSERT_EQ(
            readback_membar_vec.at(0), 187);  // Ensure that memory barriers were correctly initialized on all DRAM
        readback_membar_vec = {};
    }

    for (const CoreCoord& core : cluster.get_soc_descriptor(0).get_cores(CoreType::ETH)) {
        test_utils::read_data_from_device(
            cluster, readback_membar_vec, 0, core, eth_l1_mem::address_map::ERISC_BARRIER_BASE, 4);
        ASSERT_EQ(
            readback_membar_vec.at(0),
            187);  // Ensure that memory barriers were correctly initialized on all ethernet cores
        readback_membar_vec = {};
    }

    // Launch 2 thread accessing different locations of L1 and using memory barrier between write and read
    // Ensure now RAW race and membars are thread safe
    std::vector<uint32_t> vec1(2560);
    std::vector<uint32_t> vec2(2560);
    std::vector<uint32_t> zeros(2560, 0);

    for (int i = 0; i < vec1.size(); i++) {
        vec1.at(i) = i;
    }
    for (int i = 0; i < vec2.size(); i++) {
        vec2.at(i) = vec1.size() + i;
    }
    std::thread th1 = std::thread([&] {
        std::uint32_t address = base_addr;
        for (int loop = 0; loop < 50; loop++) {
            for (const CoreCoord& core : cluster.get_soc_descriptor(0).get_cores(CoreType::TENSIX)) {
                std::vector<uint32_t> readback_vec = {};
                cluster.write_to_device(vec1.data(), vec1.size() * sizeof(std::uint32_t), 0, core, address);
                cluster.l1_membar(0, {core});
                test_utils::read_data_from_device(cluster, readback_vec, 0, core, address, 4 * vec1.size());
                ASSERT_EQ(readback_vec, vec1);
                cluster.write_to_device(zeros.data(), zeros.size() * sizeof(std::uint32_t), 0, core, address);
                readback_vec = {};
            }
        }
    });

    std::thread th2 = std::thread([&] {
        std::uint32_t address = base_addr + vec1.size() * 4;
        for (int loop = 0; loop < 50; loop++) {
            for (const CoreCoord& core : cluster.get_soc_descriptor(0).get_cores(CoreType::TENSIX)) {
                std::vector<uint32_t> readback_vec = {};
                cluster.write_to_device(vec2.data(), vec2.size() * sizeof(std::uint32_t), 0, core, address);
                cluster.l1_membar(0, {core});
                test_utils::read_data_from_device(cluster, readback_vec, 0, core, address, 4 * vec2.size());
                ASSERT_EQ(readback_vec, vec2);
                cluster.write_to_device(zeros.data(), zeros.size() * sizeof(std::uint32_t), 0, core, address);
                readback_vec = {};
            }
        }
    });

    th1.join();
    th2.join();

    for (const CoreCoord& core : cluster.get_soc_descriptor(0).get_cores(CoreType::TENSIX)) {
        test_utils::read_data_from_device(
            cluster, readback_membar_vec, 0, core, l1_mem::address_map::L1_BARRIER_BASE, 4);
        ASSERT_EQ(
            readback_membar_vec.at(0), 187);  // Ensure that memory barriers end up in the correct sate for workers
        readback_membar_vec = {};
    }

    for (const CoreCoord& core : cluster.get_soc_descriptor(0).get_cores(CoreType::ETH)) {
        test_utils::read_data_from_device(
            cluster, readback_membar_vec, 0, core, eth_l1_mem::address_map::ERISC_BARRIER_BASE, 4);
        ASSERT_EQ(
            readback_membar_vec.at(0),
            187);  // Ensure that memory barriers end up in the correct sate for ethernet cores
        readback_membar_vec = {};
    }
    cluster.close_device();
}

TEST(SiliconDriverWH, BroadcastWrite) {
    // Broadcast multiple vectors to tensix and dram grid. Verify broadcasted data is read back correctly
    Cluster cluster;
    set_barrier_params(cluster);
    auto mmio_devices = cluster.get_target_mmio_device_ids();

    tt_device_params default_params;
    cluster.start_device(default_params);
    std::vector<uint32_t> broadcast_sizes = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384};
    uint32_t address = l1_mem::address_map::DATA_BUFFER_SPACE_BASE;
    std::set<uint32_t> rows_to_exclude = {0, 6};
    std::set<uint32_t> cols_to_exclude = {0, 5};
    std::set<uint32_t> rows_to_exclude_for_dram_broadcast = {};
    std::set<uint32_t> cols_to_exclude_for_dram_broadcast = {1, 2, 3, 4, 6, 7, 8, 9};

    for (const auto& size : broadcast_sizes) {
        std::vector<uint32_t> vector_to_write(size);
        std::vector<uint32_t> zeros(size);
        std::vector<uint32_t> readback_vec = {};
        for (int i = 0; i < size; i++) {
            vector_to_write[i] = i;
            zeros[i] = 0;
        }
        // Broadcast to Tensix
        cluster.broadcast_write_to_cluster(
            vector_to_write.data(), vector_to_write.size() * 4, address, {}, rows_to_exclude, cols_to_exclude);
        // Broadcast to DRAM
        cluster.broadcast_write_to_cluster(
            vector_to_write.data(),
            vector_to_write.size() * 4,
            address,
            {},
            rows_to_exclude_for_dram_broadcast,
            cols_to_exclude_for_dram_broadcast);
        cluster.wait_for_non_mmio_flush();

        for (auto chip_id : cluster.get_target_device_ids()) {
            for (const CoreCoord& core : cluster.get_soc_descriptor(chip_id).get_cores(CoreType::TENSIX)) {
                if (rows_to_exclude.find(core.y) != rows_to_exclude.end()) {
                    continue;
                }
                test_utils::read_data_from_device(
                    cluster, readback_vec, chip_id, core, address, vector_to_write.size() * 4);
                ASSERT_EQ(vector_to_write, readback_vec)
                    << "Vector read back from core " << core.str() << " does not match what was broadcasted";
                cluster.write_to_device(
                    zeros.data(),
                    zeros.size() * sizeof(std::uint32_t),
                    chip_id,
                    core,
                    address);  // Clear any written data
                readback_vec = {};
            }
            for (int chan = 0; chan < cluster.get_soc_descriptor(chip_id).get_num_dram_channels(); chan++) {
                const CoreCoord core =
                    cluster.get_soc_descriptor(chip_id).get_dram_core_for_channel(chan, 0, CoordSystem::VIRTUAL);
                test_utils::read_data_from_device(
                    cluster, readback_vec, chip_id, core, address, vector_to_write.size() * 4);
                ASSERT_EQ(vector_to_write, readback_vec)
                    << "Vector read back from DRAM core " << chip_id << " " << core.str()
                    << " does not match what was broadcasted " << size;
                cluster.write_to_device(
                    zeros.data(),
                    zeros.size() * sizeof(std::uint32_t),
                    chip_id,
                    core,
                    address);  // Clear any written data
                readback_vec = {};
            }
        }
        // Wait for data to be cleared before writing next block
        cluster.wait_for_non_mmio_flush();
    }
    cluster.close_device();
}

TEST(SiliconDriverWH, VirtualCoordinateBroadcast) {
    // Broadcast multiple vectors to tensix and dram grid. Verify broadcasted data is read back correctly
    Cluster cluster;
    set_barrier_params(cluster);
    auto mmio_devices = cluster.get_target_mmio_device_ids();

    tt_device_params default_params;
    cluster.start_device(default_params);
    auto eth_version = cluster.get_ethernet_fw_version();
    bool virtual_bcast_supported = (eth_version >= tt_version(6, 8, 0) || eth_version == tt_version(6, 7, 241)) &&
                                   cluster.get_soc_descriptor(*mmio_devices.begin()).noc_translation_enabled;
    if (!virtual_bcast_supported) {
        cluster.close_device();
        GTEST_SKIP() << "SiliconDriverWH.VirtualCoordinateBroadcast skipped since ethernet version does not support "
                        "Virtual Coordinate Broadcast or NOC translation is not enabled";
    }

    std::vector<uint32_t> broadcast_sizes = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384};
    uint32_t address = l1_mem::address_map::DATA_BUFFER_SPACE_BASE;
    std::set<uint32_t> rows_to_exclude = {0, 3, 5, 6, 8, 9};
    std::set<uint32_t> cols_to_exclude = {0, 5};
    std::set<uint32_t> rows_to_exclude_for_dram_broadcast = {};
    std::set<uint32_t> cols_to_exclude_for_dram_broadcast = {1, 2, 3, 4, 6, 7, 8, 9};

    for (const auto& size : broadcast_sizes) {
        std::vector<uint32_t> vector_to_write(size);
        std::vector<uint32_t> zeros(size);
        std::vector<uint32_t> readback_vec = {};
        for (int i = 0; i < size; i++) {
            vector_to_write[i] = i;
            zeros[i] = 0;
        }
        // Broadcast to Tensix
        cluster.broadcast_write_to_cluster(
            vector_to_write.data(), vector_to_write.size() * 4, address, {}, rows_to_exclude, cols_to_exclude);
        // Broadcast to DRAM
        cluster.broadcast_write_to_cluster(
            vector_to_write.data(),
            vector_to_write.size() * 4,
            address,
            {},
            rows_to_exclude_for_dram_broadcast,
            cols_to_exclude_for_dram_broadcast);
        cluster.wait_for_non_mmio_flush();

        for (auto chip_id : cluster.get_target_device_ids()) {
            for (const CoreCoord& core : cluster.get_soc_descriptor(chip_id).get_cores(CoreType::TENSIX)) {
                // Rows are excluded according to virtual coordinates, so we have to translate to that system before
                // accessing .y coordinate.
                const CoreCoord virtual_core =
                    cluster.get_soc_descriptor(chip_id).translate_coord_to(core, CoordSystem::VIRTUAL);
                if (rows_to_exclude.find(virtual_core.y) != rows_to_exclude.end()) {
                    continue;
                }
                test_utils::read_data_from_device(
                    cluster, readback_vec, chip_id, core, address, vector_to_write.size() * 4);
                ASSERT_EQ(vector_to_write, readback_vec)
                    << "Vector read back from core " << core.str() << " does not match what was broadcasted";
                cluster.write_to_device(
                    zeros.data(),
                    zeros.size() * sizeof(std::uint32_t),
                    chip_id,
                    core,
                    address);  // Clear any written data
                readback_vec = {};
            }
            for (int chan = 0; chan < cluster.get_soc_descriptor(chip_id).get_num_dram_channels(); chan++) {
                const CoreCoord core =
                    cluster.get_soc_descriptor(chip_id).get_dram_core_for_channel(chan, 0, CoordSystem::VIRTUAL);
                test_utils::read_data_from_device(
                    cluster, readback_vec, chip_id, core, address, vector_to_write.size() * 4);
                ASSERT_EQ(vector_to_write, readback_vec)
                    << "Vector read back from DRAM core " << chip_id << " " << core.str()
                    << " does not match what was broadcasted " << size;
                cluster.write_to_device(
                    zeros.data(),
                    zeros.size() * sizeof(std::uint32_t),
                    chip_id,
                    core,
                    address);  // Clear any written data
                readback_vec = {};
            }
        }
        // Wait for data to be cleared before writing next block
        cluster.wait_for_non_mmio_flush();
    }
    cluster.close_device();
}

/**
 * This is a basic DMA test -- not using the PCIe controller's DMA engine, but
 * rather using the ability of the NOC to access the host system bus via traffic
 * to the PCIe block.
 *
 * sysmem means memory in the host that has been mapped for device access.  It
 * is currently one or more 1G huge pages, although this may change.
 *
 * 1. Fills sysmem with a random pattern.
 * 2. Uses PCIe block on WH to read sysmem into buffer.
 * 3. Verifies that buffer matches sysmem.
 * 4. Fills buffer with a random pattern.
 * 5. Uses PCIe block on WH to write buffer into sysmem.
 * 6. Verifies that sysmem matches buffer.
 *
 * This uses a small size for speed purposes.
 *
 * If/when we move to using IOMMU to map userspace memory for device access,
 * the technique below is a straightforward way to test that hardware can access
 * the buffer(s).
 */
TEST(SiliconDriverWH, SysmemTestWithPcie) {
    Cluster cluster;

    set_barrier_params(cluster);
    cluster.start_device(tt_device_params{});  // no special parameters

    const chip_id_t mmio_chip_id = 0;
    const auto PCIE = cluster.get_soc_descriptor(mmio_chip_id).get_cores(CoreType::PCIE).at(0);
    const size_t test_size_bytes = 0x4000;  // Arbitrarilly chosen, but small size so the test runs quickly.

    // PCIe core is at (x=0, y=3) on Wormhole NOC0.
    ASSERT_EQ(PCIE.x, 0);
    ASSERT_EQ(PCIE.y, 3);

    // Bad API: how big is the buffer?  How do we know it's big enough?
    // Situation today is that there's a 1G hugepage behind it, although this is
    // unclear from the API and may change in the future.
    uint8_t* sysmem = (uint8_t*)cluster.host_dma_address(0, 0, 0);
    ASSERT_NE(sysmem, nullptr);

    // This is the address inside the Wormhole PCIe block that is mapped to the
    // system bus.  In Wormhole, this is a fixed address, 0x8'0000'0000.
    // The driver should have mapped this address to the bottom of sysmem.
    uint64_t base_address = cluster.get_pcie_base_addr_from_device(mmio_chip_id);

    // Buffer that we will use to read sysmem into, then write sysmem from.
    std::vector<uint8_t> buffer(test_size_bytes, 0x0);

    // Step 1: Fill sysmem with random bytes.
    test_utils::fill_with_random_bytes(sysmem, test_size_bytes);

    // Step 2: Read sysmem into buffer.
    cluster.read_from_device(&buffer[0], mmio_chip_id, PCIE, base_address, buffer.size());

    // Step 3: Verify that buffer matches sysmem.
    ASSERT_EQ(buffer, std::vector<uint8_t>(sysmem, sysmem + test_size_bytes));

    // Step 4: Fill buffer with random bytes.
    test_utils::fill_with_random_bytes(&buffer[0], test_size_bytes);

    // Step 5: Write buffer into sysmem, overwriting what was there.
    cluster.write_to_device(&buffer[0], buffer.size(), mmio_chip_id, PCIE, base_address);

    // Step 5b: Read back sysmem into a throwaway buffer.  The intent is to
    // ensure the write has completed before we check sysmem against buffer.
    std::vector<uint8_t> throwaway(test_size_bytes, 0x0);
    cluster.read_from_device(&throwaway[0], mmio_chip_id, PCIE, base_address, throwaway.size());

    // Step 6: Verify that sysmem matches buffer.
    ASSERT_EQ(buffer, std::vector<uint8_t>(sysmem, sysmem + test_size_bytes));
}

// TODO: the following test is failing on UBB. Figure out why and fix it.
/**
 * Same idea as above, but with four channels of sysmem and random addresses.
 * The hardware mechanism is too slow to sweep the entire range.
 */
TEST(SiliconDriverWH, RandomSysmemTestWithPcie) {
    const uint32_t num_channels = 2;  // ideally 4, but CI seems to have 2...

    Cluster cluster(ClusterOptions{
        .num_host_mem_ch_per_mmio_device = num_channels,
    });

    set_barrier_params(cluster);
    cluster.start_device(tt_device_params{});  // no special parameters

    const chip_id_t mmio_chip_id = 0;
    const auto PCIE = cluster.get_soc_descriptor(mmio_chip_id).get_cores(CoreType::PCIE).at(0);
    const size_t ONE_GIG = 1 << 30;
    const size_t num_tests = 0x20000;  // runs in a reasonable amount of time

    // PCIe core is at (x=0, y=3) on Wormhole NOC0.
    ASSERT_EQ(PCIE.x, 0);
    ASSERT_EQ(PCIE.y, 3);

    const uint64_t ALIGNMENT = sizeof(uint32_t);
    auto generate_aligned_address = [&](uint64_t lo, uint64_t hi) -> uint64_t {
        static std::random_device rd;
        static std::mt19937_64 gen(rd());
        std::uniform_int_distribution<uint64_t> dis(lo / ALIGNMENT, hi / ALIGNMENT);
        return dis(gen) * ALIGNMENT;
    };

    uint64_t base_address = cluster.get_pcie_base_addr_from_device(mmio_chip_id);
    for (size_t channel = 0; channel < num_channels; ++channel) {
        uint8_t* sysmem = (uint8_t*)cluster.host_dma_address(0, 0, channel);
        ASSERT_NE(sysmem, nullptr);

        test_utils::fill_with_random_bytes(sysmem, ONE_GIG);

        uint64_t lo = (ONE_GIG * channel);
        uint64_t hi = (lo + ONE_GIG) - 1;

        if (channel == 3) {
            // Avoid the top 256MB of the 4th hugepage region on WH.
            hi &= ~0x0fff'ffffULL;
        }

        for (size_t i = 0; i < num_tests; ++i) {
            uint64_t address = generate_aligned_address(lo, hi);
            uint64_t noc_addr = base_address + address;
            uint64_t sysmem_address = address - lo;

            ASSERT_GE(address, lo) << "Address too low";
            ASSERT_LE(address, hi) << "Address too high";
            ASSERT_EQ(address % ALIGNMENT, 0) << "Address not properly aligned";

            uint32_t value = 0;
            cluster.read_from_device(&value, mmio_chip_id, PCIE, noc_addr, sizeof(uint32_t));

            uint32_t expected = *reinterpret_cast<uint32_t*>(&sysmem[sysmem_address]);
            ASSERT_EQ(value, expected) << fmt::format("Mismatch at address {:#x}", address);
        }
    }
}

TEST(SiliconDriverWH, LargeAddressTlb) {
    Cluster cluster;

    const CoreCoord ARC_CORE = cluster.get_soc_descriptor(0).get_cores(CoreType::ARC).at(0);

    set_barrier_params(cluster);
    cluster.start_device(tt_device_params{});

    auto get_static_tlb_index_callback = [](tt_xy_pair target) { return 0; };

    // Address of the reset unit in ARC core:
    uint64_t arc_reset_noc = 0x880030000ULL;

    // Offset to the scratch registers in the reset unit:
    uint64_t scratch_offset = 0x60;

    // Map a TLB to the reset unit in ARC core:
    cluster.configure_tlb(0, ARC_CORE, 0, arc_reset_noc);

    // Address of the scratch register in the reset unit:
    uint64_t addr = arc_reset_noc + scratch_offset;

    uint32_t value0 = 0;
    uint32_t value1 = 0;
    uint32_t value2 = 0;

    // Read the scratch register via BAR0:
    value0 = cluster.get_chip(0)->get_tt_device()->bar_read32(0x1ff30060);

    // Read the scratch register via the TLB:
    cluster.read_from_device(&value1, 0, ARC_CORE, addr, sizeof(uint32_t));

    // Read the scratch register via a different TLB, different code path:
    cluster.read_from_device(&value2, 0, ARC_CORE, addr, sizeof(uint32_t));

    // Mask off lower 16 bits; FW changes these dynamically:
    value0 &= 0xffff0000;
    value1 &= 0xffff0000;
    value2 &= 0xffff0000;

    // Check that the values are the same:
    EXPECT_EQ(value1, value0);
    EXPECT_EQ(value2, value0);
}

/**
 * Test the PCIe DMA controller by using it to write random fixed-size patterns
 * to 0x0 in several DRAM cores, then reading them back and verifying.
 */
TEST(SiliconDriverWH, DMA1) {
    const chip_id_t chip = 0;
    Cluster cluster;

    cluster.start_device(tt_device_params{});

    auto& soc_descriptor = cluster.get_soc_descriptor(chip);
    size_t dram_count = soc_descriptor.get_num_dram_channels();
    std::vector<CoreCoord> dram_cores;
    for (size_t i = 0; i < dram_count; ++i) {
        dram_cores.push_back(soc_descriptor.get_dram_core_for_channel(i, 0, CoordSystem::NOC0));
    }

    // 16.5 MiB: Larger than the largest WH TLB window; this forces chunking
    // and TLB reassignment.
    size_t buf_size = 0x1080000;

    // Keep track of the patterns we wrote to DRAM so we can verify them later.
    std::vector<std::vector<uint8_t>> patterns;

    // First, write a different pattern to each of the DRAM cores.
    for (auto core : dram_cores) {
        std::vector<uint8_t> pattern(buf_size);
        test_utils::fill_with_random_bytes(&pattern[0], pattern.size());

        cluster.dma_write_to_device(pattern.data(), pattern.size(), chip, core, 0x0);

        patterns.push_back(pattern);
    }

    // Now, read back the patterns we wrote to DRAM and verify them.
    for (size_t i = 0; i < dram_cores.size(); ++i) {
        auto core = dram_cores[i];
        std::vector<uint8_t> readback(buf_size, 0x0);

        cluster.dma_read_from_device(readback.data(), readback.size(), chip, core, 0x0);

        EXPECT_EQ(patterns[i], readback) << "Mismatch for core " << core.str() << " addr=0x0"
                                         << " size=" << std::dec << readback.size();
    }
}

/**
 * Test the PCIe DMA controller by using it to write random patterns of random
 * sizes to random addresses in several DRAM cores, then reading them back and
 * verifying.  Addresses are constrained to be within the first 1 GiB of each
 * DRAM channel and are aligned to 4 bytes.  Sizes are constrained to be between
 * 4 bytes and 32 MiB, and are aligned to 4 bytes.  Also tested is the case
 * where the write is done using MMIO instead of DMA.
 */
TEST(SiliconDriverWH, DMA2) {
    const chip_id_t chip = 0;
    Cluster cluster;

    set_barrier_params(cluster);
    cluster.start_device(tt_device_params{});

    auto& soc_descriptor = cluster.get_soc_descriptor(chip);
    size_t dram_count = soc_descriptor.get_num_dram_channels();
    std::vector<CoreCoord> dram_cores;
    for (size_t i = 0; i < dram_count; ++i) {
        dram_cores.push_back(soc_descriptor.get_dram_core_for_channel(i, 0, CoordSystem::NOC0));
    }

    // Constraints for random address/size generation.
    const size_t MIN_BUF_SIZE = 4;
    const size_t MAX_BUF_SIZE = 0x2000000;
    const uint64_t MIN_ADDR = 0x0;
    const uint64_t MAX_ADDR = 0x3e000000;

    // Setup random number generation.
    std::random_device rd;
    std::mt19937 rng(rd());
    std::uniform_int_distribution<size_t> size_dist(MIN_BUF_SIZE, MAX_BUF_SIZE);
    std::uniform_int_distribution<uint64_t> addr_dist(MIN_ADDR, MAX_ADDR);

    // Structure to keep track of the operations.
    struct DmaOpInfo {
        CoreCoord core;
        uint64_t address;
        std::vector<uint8_t> data;  // Store the actual data written for verification.
    };

    const size_t ITERATIONS = 25;
    for (size_t i = 0; i < ITERATIONS; ++i) {
        std::vector<DmaOpInfo> write_ops;
        write_ops.reserve(dram_cores.size());

        // First, write a different random pattern to a random address on each DRAM core.
        for (const auto& core : dram_cores) {
            // Generate random size and address.
            size_t size = size_dist(rng) & ~0x3ULL;
            uint64_t addr = addr_dist(rng) & ~0x3ULL;

            // Generate a random pattern of the specified size.
            std::vector<uint8_t> pattern(size);
            test_utils::fill_with_random_bytes(pattern.data(), pattern.size());

            // Perform the DMA write.
            cluster.dma_write_to_device(pattern.data(), pattern.size(), chip, core, addr);

            // Store the operation details for verification.
            write_ops.push_back({core, addr, pattern});
        }

        // Now, read back the patterns we wrote to DRAM and verify them.
        for (const auto& op : write_ops) {
            std::vector<uint8_t> readback(op.data.size());

            // Perform the DMA read from the specific address.
            cluster.dma_read_from_device(readback.data(), readback.size(), chip, op.core, op.address);

            // Verify the data.
            EXPECT_EQ(op.data, readback) << "Mismatch for core " << op.core.str() << " addr=0x" << std::hex
                                         << op.address << " size=" << std::dec << op.data.size();
        }
    }

    // Do it again but use MMIO writes to the DRAM cores instead of DMA.
    // DMA is still used for readback.  The inverse of this test (DMA for write;
    // MMIO for read) is omitted because of how slow MMIO reads are.
    for (size_t i = 0; i < ITERATIONS; ++i) {
        std::vector<DmaOpInfo> write_ops;
        write_ops.reserve(dram_cores.size());

        // First, write a different random pattern to a random address on each DRAM core.
        for (const auto& dram_core : dram_cores) {
            // Generate random size and address.
            size_t size = size_dist(rng) & ~0x3ULL;
            uint64_t addr = addr_dist(rng) & ~0x3ULL;

            // Generate a random pattern of the specified size.
            std::vector<uint8_t> pattern(size);
            test_utils::fill_with_random_bytes(pattern.data(), pattern.size());

            // Perform the DMA write.
            cluster.write_to_device(pattern.data(), pattern.size(), chip, dram_core, addr);

            // Store the operation details for verification.
            write_ops.push_back({dram_core, addr, pattern});
        }

        // Now, read back the patterns we wrote to DRAM and verify them.
        for (const auto& op : write_ops) {
            std::vector<uint8_t> readback(op.data.size());

            // Perform the DMA read from the specific address.
            cluster.dma_read_from_device(readback.data(), readback.size(), chip, op.core, op.address);

            // Verify the data.
            EXPECT_EQ(op.data, readback) << "Mismatch for core " << op.core.str() << " addr=0x" << std::hex
                                         << op.address << " size=" << std::dec << op.data.size();
        }
    }
}

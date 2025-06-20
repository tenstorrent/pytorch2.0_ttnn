// SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0

#include <gtest/gtest.h>

#include <thread>

#include "tests/test_utils/device_test_utils.hpp"
#include "umd/device/cluster.h"

using namespace tt::umd;

constexpr int NUM_PARALLEL = 4;
constexpr int NUM_LOOPS = 1000;

// We want to test IO in parallel in each thread.
// But we don't want these addresses to overlap, since the data will be corrupted.
// All of this is focused on a single chip system.
void test_read_write_all_tensix_cores(Cluster* cluster, int thread_id) {
    std::cout << " Starting test_read_write_all_tensix_cores for cluster " << (uint64_t)cluster << " thread_id "
              << thread_id << std::endl;
    auto l1_size = cluster->get_soc_descriptor(0).worker_l1_size;
    auto chunk_size = l1_size / NUM_PARALLEL;

    std::vector<uint32_t> vector_to_write = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    std::vector<uint32_t> readback_vec = {};
    uint32_t address = chunk_size * thread_id;
    uint32_t start_address = address;
    uint32_t address_next_thread = chunk_size * (thread_id + 1);

    for (int loop = 0; loop < NUM_LOOPS; loop++) {
        for (const CoreCoord& core : cluster->get_soc_descriptor(0).get_cores(CoreType::TENSIX)) {
            cluster->write_to_device(
                vector_to_write.data(), vector_to_write.size() * sizeof(std::uint32_t), 0, core, address);
            cluster->l1_membar(0, {core});
            test_utils::read_data_from_device(*cluster, readback_vec, 0, core, address, 40);
            ASSERT_EQ(vector_to_write, readback_vec)
                << "Vector read back from core " << core.str() << " does not match what was written";
            readback_vec = {};
        }
        address += 0x20;
        // If we get into the bucket of the next thread, return to start address of this thread's bucket.
        // If we are inside other bucket can't guarantee the order of read/writes.
        if (address + vector_to_write.size() * sizeof(uint32_t) > address_next_thread ||
            address + vector_to_write.size() * sizeof(uint32_t) > l1_size) {
            address = start_address;
        }
    }
    std::cout << "Completed test_read_write_all_tensix_cores for cluster " << (uint64_t)cluster << " thread_id "
              << thread_id << std::endl;
}

// Single process opens multiple clusters but uses them sequentially.
TEST(Multiprocess, MultipleClusters) {
    std::vector<std::unique_ptr<Cluster>> clusters;
    for (int i = 0; i < NUM_PARALLEL; i++) {
        std::cout << "Creating cluster " << i << std::endl;
        clusters.push_back(std::make_unique<Cluster>());
    }
    for (int i = 0; i < NUM_PARALLEL; i++) {
        std::cout << "Running IO for cluster " << i << std::endl;
        test_read_write_all_tensix_cores(clusters[i].get(), i);
        std::cout << "Finished IO for cluster " << i << std::endl;
    }
}

// Multiple threads use single cluster for IO.
TEST(Multiprocess, MultipleThreadsSingleCluster) {
    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>();
    std::vector<std::thread> threads;
    for (int i = 0; i < NUM_PARALLEL; i++) {
        threads.push_back(std::thread([&, i] {
            std::cout << "Running IO for thread " << i << " inside cluster." << std::endl;
            test_read_write_all_tensix_cores(cluster.get(), i);
            std::cout << "Finished read/write test for cluster " << i << std::endl;
        }));
    }
    for (auto& th : threads) {
        th.join();
    }
}

// Many threads open and close many clusters.
TEST(Multiprocess, MultipleThreadsMultipleClustersCreation) {
    std::vector<std::thread> threads;
    for (int i = 0; i < NUM_PARALLEL; i++) {
        threads.push_back(std::thread([&, i] {
            std::cout << "Create cluster " << i << std::endl;
            std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>();
            cluster = nullptr;
        }));
    }
    for (auto& th : threads) {
        th.join();
    }
}

// Many threads start and stop many clusters.
TEST(Multiprocess, MultipleThreadsMultipleClustersRunning) {
    std::vector<std::thread> threads;
    for (int i = 0; i < NUM_PARALLEL; i++) {
        threads.push_back(std::thread([&, i] {
            std::cout << "Creating cluster " << i << std::endl;
            std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>();
            std::cout << "Running IO for cluster " << i << std::endl;
            test_read_write_all_tensix_cores(cluster.get(), i);
            std::cout << "Finished IO for cluster " << i << std::endl;
        }));
    }
    for (auto& th : threads) {
        th.join();
    }
}

// Simulation of one device running a full workload, while others use low level TTDevice functionality.
TEST(Multiprocess, WorkloadVSMonitor) {
    std::vector<int> pci_device_ids = PCIDevice::enumerate_devices();

    if (pci_device_ids.empty()) {
        GTEST_SKIP() << "No chips present on the system. Skipping test.";
    }

    auto workload_thread = std::thread([&] {
        std::cout << "Creating workload cluster" << std::endl;
        std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>();
        std::cout << "Running IO for workload cluster" << std::endl;
        test_read_write_all_tensix_cores(cluster.get(), 0);
        std::cout << "Finished IO for workload cluster" << std::endl;
    });

    auto monitor_thread = std::thread([&] {
        std::cout << "Creating monitor cluster" << std::endl;
        std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>();
        std::cout << "Running only reads for monitor cluster" << std::endl;
        for (int loop = 0; loop < NUM_LOOPS; loop++) {
            uint32_t example_read;
            cluster->read_from_device(
                &example_read,
                0,
                cluster->get_soc_descriptor(0).get_cores(CoreType::ARC)[0],
                0x8003042C,
                sizeof(uint32_t));
        }
        std::cout << "Destroying monitor cluster" << std::endl;
    });

    auto low_level_monitor_thread = std::thread([&] {
        std::cout << "Creating low level monitor cluster" << std::endl;
        std::unique_ptr<TTDevice> tt_device = TTDevice::create(pci_device_ids.at(0));
        tt_SocDescriptor soc_desc = tt_SocDescriptor(tt_device->get_arch(), true);
        CoreCoord arc_core = soc_desc.get_cores(CoreType::ARC, CoordSystem::TRANSLATED)[0];

        std::cout << "Running only reads for low level monitor cluster, without device start " << std::endl;
        for (int loop = 0; loop < NUM_LOOPS; loop++) {
            uint32_t example_read;
            tt_device->read_from_device(&example_read, arc_core, 0x8003042C, sizeof(uint32_t));
        }
        std::cout << "Destroying low level monitor cluster" << std::endl;
    });

    workload_thread.join();
    monitor_thread.join();
    low_level_monitor_thread.join();
}

TEST(Multiprocess, LongLivedMonitor) {
    std::vector<int> pci_device_ids = PCIDevice::enumerate_devices();

    if (pci_device_ids.empty()) {
        GTEST_SKIP() << "No chips present on the system. Skipping test.";
    }

    auto low_level_monitor_thread = std::thread([&] {
        std::cout << "Creating low level monitor cluster" << std::endl;
        std::unique_ptr<TTDevice> tt_device = TTDevice::create(pci_device_ids.at(0));
        tt_SocDescriptor soc_desc = tt_SocDescriptor(tt_device->get_arch(), true);
        CoreCoord arc_core = soc_desc.get_cores(CoreType::ARC, CoordSystem::TRANSLATED)[0];

        std::cout << "Running only reads for low level monitor cluster, without device start " << std::endl;
        for (int loop = 0; loop < NUM_LOOPS; loop++) {
            uint32_t example_read;
            tt_device->read_from_device(&example_read, arc_core, 0x8003042C, sizeof(uint32_t));
        }
        std::cout << "Destroying low level monitor cluster" << std::endl;
    });

    for (int i = 0; i < NUM_PARALLEL; i++) {
        std::cout << "Creating cluster " << i << std::endl;
        std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>();
        std::cout << "Running IO for cluster " << i << std::endl;
        test_read_write_all_tensix_cores(cluster.get(), i);
        std::cout << "Finished IO for cluster " << i << std::endl;
    }

    low_level_monitor_thread.join();
}

TEST(Multiprocess, ClusterAndTTDeviceTest) {
    const uint64_t address_thread0 = 0x1000;
    const uint64_t address_thread1 = address_thread0 + 0x100;
    const uint32_t num_loops = 1000;

    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>();

    for (chip_id_t chip : cluster->get_target_mmio_device_ids()) {
        TTDevice* tt_device = cluster->get_tt_device(chip);

        CoreCoord tensix_core = cluster->get_soc_descriptor(chip).get_cores(CoreType::TENSIX)[0];

        std::thread thread0([&]() {
            std::vector<uint32_t> data_write_t0 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
            std::vector<uint32_t> data_read(data_write_t0.size(), 0);
            for (uint32_t loop = 0; loop < num_loops; loop++) {
                tt_device->write_to_device(
                    data_write_t0.data(), tensix_core, address_thread0, data_write_t0.size() * sizeof(uint32_t));

                tt_device->read_from_device(
                    data_read.data(), tensix_core, address_thread0, data_read.size() * sizeof(uint32_t));

                ASSERT_EQ(data_write_t0, data_read);

                data_read = std::vector<uint32_t>(data_write_t0.size(), 0);
            }
        });

        std::thread thread1([&]() {
            std::vector<uint32_t> data_write_t1 = {11, 22, 33, 44, 55, 66, 77, 88, 99, 100};
            std::vector<uint32_t> data_read(data_write_t1.size(), 0);
            for (uint32_t loop = 0; loop < num_loops; loop++) {
                cluster->write_to_device(
                    data_write_t1.data(), data_write_t1.size() * sizeof(uint32_t), chip, tensix_core, address_thread1);
                cluster->l1_membar(chip, {tensix_core});

                cluster->read_from_device(
                    data_read.data(), chip, tensix_core, address_thread1, data_read.size() * sizeof(uint32_t));

                ASSERT_EQ(data_write_t1, data_read);

                data_read = std::vector<uint32_t>(data_write_t1.size(), 0);
            }
        });

        thread0.join();
        thread1.join();
    }
}

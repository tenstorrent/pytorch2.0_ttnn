/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#include <sys/mman.h>

#include "gtest/gtest.h"
#include "tests/test_utils/device_test_utils.hpp"
#include "tests/test_utils/generate_cluster_desc.hpp"
#include "umd/device/chip_helpers/sysmem_manager.h"
#include "umd/device/cluster.h"
#include "umd/device/tt_cluster_descriptor.h"
#include "umd/device/tt_device/wormhole_tt_device.h"
#include "umd/device/wormhole_implementation.h"
#include "wormhole/eth_l1_address_map.h"
#include "wormhole/host_mem_address_map.h"
#include "wormhole/l1_address_map.h"

using namespace tt::umd;

const chip_id_t chip = 0;
const uint32_t one_mb = 1 << 20;
const uint32_t NUM_ITERATIONS = 1000;

static inline void print_speed(std::string direction, size_t bytes, uint64_t ns) {
    double seconds = ns / 1e9;
    double megabytes = static_cast<double>(bytes) / (1024.0 * 1024.0);
    auto rate = megabytes / seconds;
    std::cout << direction << ": 0x" << std::hex << bytes << std::dec << " bytes in " << ns << " ns (" << rate
              << " MB/s)" << std::endl;
}

static inline void perf_read_write(
    const uint32_t buf_size,
    const uint32_t num_iterations,
    const std::unique_ptr<Cluster>& cluster,
    const CoreCoord core,
    const std::string& direction_to_device,
    const std::string& direction_from_device) {
    std::cout << std::endl;
    std::cout << "Reporting results for buffer size " << (buf_size / one_mb) << " MB being transfered "
              << num_iterations << " number of times." << std::endl;
    std::cout << "--------------------------------------------------------" << std::endl;

    std::vector<uint8_t> pattern(buf_size);
    test_utils::fill_with_random_bytes(&pattern[0], pattern.size());

    auto now = std::chrono::steady_clock::now();
    for (int i = 0; i < num_iterations; i++) {
        cluster->dma_write_to_device(pattern.data(), pattern.size(), chip, core, 0x0);
    }
    auto end = std::chrono::steady_clock::now();
    auto ns = std::chrono::duration_cast<std::chrono::nanoseconds>(end - now).count();
    print_speed(direction_to_device, num_iterations * pattern.size(), ns);

    std::vector<uint8_t> readback(buf_size, 0x0);
    now = std::chrono::steady_clock::now();
    for (int i = 0; i < num_iterations; i++) {
        cluster->dma_read_from_device(readback.data(), readback.size(), chip, core, 0x0);
    }
    end = std::chrono::steady_clock::now();
    ns = std::chrono::duration_cast<std::chrono::nanoseconds>(end - now).count();
    print_speed(direction_from_device, num_iterations * readback.size(), ns);
}

static inline void perf_sysmem_read_write(
    const uint32_t buf_size,
    const uint32_t num_iterations,
    const std::unique_ptr<SysmemBuffer>& sysmem_buffer,
    const CoreCoord core,
    const std::string& direction_to_device,
    const std::string& direction_from_device) {
    {
        auto now = std::chrono::steady_clock::now();
        for (int i = 0; i < NUM_ITERATIONS; i++) {
            sysmem_buffer->dma_write_to_device(0, one_mb, core, 0);
        }
        auto end = std::chrono::steady_clock::now();
        auto ns = std::chrono::duration_cast<std::chrono::nanoseconds>(end - now).count();
        print_speed(direction_to_device, one_mb * NUM_ITERATIONS, ns);
    }

    {
        auto now = std::chrono::steady_clock::now();
        for (int i = 0; i < NUM_ITERATIONS; i++) {
            sysmem_buffer->dma_read_from_device(0, one_mb, core, 0);
        }
        auto end = std::chrono::steady_clock::now();
        auto ns = std::chrono::duration_cast<std::chrono::nanoseconds>(end - now).count();
        print_speed(direction_from_device, one_mb * NUM_ITERATIONS, ns);
    }
}

static void guard_test_iommu() {
    std::vector<int> pci_device_ids = PCIDevice::enumerate_devices();
    if (pci_device_ids.empty()) {
        GTEST_SKIP() << "No chips present on the system. Skipping test.";
    }
    if (!PCIDevice(pci_device_ids[0]).is_iommu_enabled()) {
        GTEST_SKIP() << "Skipping test since IOMMU is not enabled on the system.";
    }
}

/**
 * Test the PCIe DMA controller by using it to write random fixed-size pattern
 * to 0x0 tensix core, then reading them back and verifying.
 */
TEST(TestPerf, DMATensix) {
    const std::vector<uint32_t> sizes = {
        1 * one_mb,
    };

    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>();
    const CoreCoord tensix_core = cluster->get_soc_descriptor(chip).get_cores(CoreType::TENSIX)[0];
    cluster->start_device(tt_device_params{});

    for (uint32_t buf_size : sizes) {
        perf_read_write(
            buf_size,
            NUM_ITERATIONS,
            cluster,
            tensix_core,
            "DMA: Host -> Device Tensix L1",
            "DMA: Device Tensix L1 -> Host");
    }
}

/**
 * Test the PCIe DMA controller by using it to write random fixed-size pattern
 * to 0x0 DRAM core, then reading them back and verifying.
 */
TEST(TestPerf, DMADram) {
    const std::vector<uint32_t> sizes = {
        1 * one_mb,
        2 * one_mb,
        4 * one_mb,
        8 * one_mb,
        16 * one_mb,
        32 * one_mb,
        64 * one_mb,
        128 * one_mb,
        256 * one_mb,
        512 * one_mb,
        1024 * one_mb,
    };

    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>();
    const CoreCoord dram_core = cluster->get_soc_descriptor(chip).get_cores(CoreType::DRAM)[0];
    cluster->start_device(tt_device_params{});
    for (uint32_t buf_size : sizes) {
        perf_read_write(
            buf_size, NUM_ITERATIONS, cluster, dram_core, "DMA: Host -> Device DRAM", "DMA: Device DRAM -> Host");
    }
}

TEST(TestPerf, DMATensixZeroCopy) {
    guard_test_iommu();

    const uint32_t NUM_ITERATIONS = 1000;
    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>(tt::umd::ClusterOptions{
        .num_host_mem_ch_per_mmio_device = 0,
    });

    const chip_id_t mmio_chip = *cluster->get_target_mmio_device_ids().begin();

    SysmemManager* sysmem_manager = cluster->get_chip(mmio_chip)->get_sysmem_manager();

    const uint32_t one_mb = 1 << 20;
    std::unique_ptr<SysmemBuffer> sysmem_buffer = sysmem_manager->allocate_sysmem_buffer(2 * one_mb);

    const CoreCoord tensix_core = cluster->get_soc_descriptor(mmio_chip).get_cores(CoreType::TENSIX)[0];
    perf_sysmem_read_write(
        one_mb,
        NUM_ITERATIONS,
        sysmem_buffer,
        tensix_core,
        "DMA zero copy: Device Tensix L1 -> Host",
        "DMA zero copy: Device Tensix L1 -> Host");
}

TEST(TestPerf, MapSysmemBuffer) {
    guard_test_iommu();

    const uint32_t NUM_ITERATIONS = 1000;
    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>(tt::umd::ClusterOptions{
        .num_host_mem_ch_per_mmio_device = 0,
    });

    const chip_id_t mmio_chip = *cluster->get_target_mmio_device_ids().begin();

    SysmemManager* sysmem_manager = cluster->get_chip(mmio_chip)->get_sysmem_manager();

    const uint32_t one_mb = 1 << 20;

    void* mapping = mmap(nullptr, one_mb, PROT_READ | PROT_WRITE, MAP_ANONYMOUS | MAP_PRIVATE | MAP_POPULATE, -1, 0);
    auto now = std::chrono::steady_clock::now();
    for (int i = 0; i < NUM_ITERATIONS; i++) {
        std::unique_ptr<SysmemBuffer> sysmem_buffer = sysmem_manager->map_sysmem_buffer(mapping, one_mb);
    }
    auto end = std::chrono::steady_clock::now();
    auto ns = std::chrono::duration_cast<std::chrono::nanoseconds>(end - now).count();
    print_speed("Allocation of sysmem buffers:", one_mb * NUM_ITERATIONS, ns);
}

TEST(TestPerf, DMATensixMapBufferZeroCopy) {
    guard_test_iommu();

    const uint32_t NUM_ITERATIONS = 100;
    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>(tt::umd::ClusterOptions{
        .num_host_mem_ch_per_mmio_device = 0,
    });

    const chip_id_t mmio_chip = *cluster->get_target_mmio_device_ids().begin();

    SysmemManager* sysmem_manager = cluster->get_chip(mmio_chip)->get_sysmem_manager();

    const uint32_t one_mb = 1 << 20;

    const CoreCoord tensix_core = cluster->get_soc_descriptor(mmio_chip).get_cores(CoreType::TENSIX)[0];
    {
        void* mapping =
            mmap(nullptr, one_mb, PROT_READ | PROT_WRITE, MAP_ANONYMOUS | MAP_PRIVATE | MAP_POPULATE, -1, 0);
        auto now = std::chrono::steady_clock::now();
        for (int i = 0; i < NUM_ITERATIONS; i++) {
            std::unique_ptr<SysmemBuffer> sysmem_buffer = sysmem_manager->map_sysmem_buffer(mapping, one_mb);
            sysmem_buffer->dma_write_to_device(0, one_mb, tensix_core, 0);
        }
        auto end = std::chrono::steady_clock::now();
        auto ns = std::chrono::duration_cast<std::chrono::nanoseconds>(end - now).count();
        print_speed("DMA mapping buffer and zero copy: Host -> Device Tensix L1", one_mb * NUM_ITERATIONS, ns);
    }

    {
        void* mapping =
            mmap(nullptr, one_mb, PROT_READ | PROT_WRITE, MAP_ANONYMOUS | MAP_PRIVATE | MAP_POPULATE, -1, 0);
        auto now = std::chrono::steady_clock::now();
        for (int i = 0; i < NUM_ITERATIONS; i++) {
            std::unique_ptr<SysmemBuffer> sysmem_buffer = sysmem_manager->map_sysmem_buffer(mapping, one_mb);
            sysmem_buffer->dma_read_from_device(0, one_mb, tensix_core, 0);
        }
        auto end = std::chrono::steady_clock::now();
        auto ns = std::chrono::duration_cast<std::chrono::nanoseconds>(end - now).count();
        print_speed("DMA mapping buffer and zero copy: Device Tensix L1 -> Host", one_mb * NUM_ITERATIONS, ns);
    }
}

TEST(TestPerf, DMADRAMZeroCopy) {
    guard_test_iommu();

    const uint32_t NUM_ITERATIONS = 10;
    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>(tt::umd::ClusterOptions{
        .num_host_mem_ch_per_mmio_device = 0,
    });

    const chip_id_t mmio_chip = *cluster->get_target_mmio_device_ids().begin();

    SysmemManager* sysmem_manager = cluster->get_chip(mmio_chip)->get_sysmem_manager();

    const uint32_t one_mb = 1 << 20;
    const uint32_t one_hundred_mb = 100 * one_mb;
    const uint32_t two_hundred_mb = 200 * one_mb;
    std::unique_ptr<SysmemBuffer> sysmem_buffer = sysmem_manager->allocate_sysmem_buffer(two_hundred_mb);

    const CoreCoord dram_core = cluster->get_soc_descriptor(mmio_chip).get_cores(CoreType::DRAM)[0];
    perf_sysmem_read_write(
        one_mb,
        NUM_ITERATIONS,
        sysmem_buffer,
        dram_core,
        "DMA zero copy: Device DRAM -> Host",
        "DMA zero copy: Device DRAM -> Host");
}

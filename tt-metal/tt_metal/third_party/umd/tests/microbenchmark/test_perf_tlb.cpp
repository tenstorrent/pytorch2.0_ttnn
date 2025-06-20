/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
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
const uint32_t NUM_ITERATIONS = 10;
const uint32_t tlb_1m_index = 0;
const uint32_t tlb_16m_index = 166;

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
        cluster->write_to_device(pattern.data(), pattern.size(), chip, core, 0x0);
    }
    auto end = std::chrono::steady_clock::now();
    auto ns = std::chrono::duration_cast<std::chrono::nanoseconds>(end - now).count();
    print_speed(direction_to_device, num_iterations * pattern.size(), ns);

    std::vector<uint8_t> readback(buf_size, 0x0);
    now = std::chrono::steady_clock::now();
    for (int i = 0; i < num_iterations; i++) {
        cluster->read_from_device(readback.data(), chip, core, 0x0, readback.size());
    }
    end = std::chrono::steady_clock::now();
    ns = std::chrono::duration_cast<std::chrono::nanoseconds>(end - now).count();
    print_speed(direction_from_device, num_iterations * readback.size(), ns);
}

TEST(TestPerf, TLBDynamicDram) {
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
    };

    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>();
    const CoreCoord dram_core = cluster->get_soc_descriptor(chip).get_cores(CoreType::DRAM)[0];
    cluster->start_device(tt_device_params{});

    for (uint32_t buf_size : sizes) {
        perf_read_write(
            buf_size,
            NUM_ITERATIONS,
            cluster,
            dram_core,
            "Dynamic TLB: Host -> Device DRAM",
            "Dynamic TLB: Device DRAM -> Host");
    }
}

TEST(TestPerf, TLBDynamicTensix) {
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
            "Dynamic TLB: Host -> Device Tensix L1",
            "Dynamic TLB: Device Tensix L1 -> Host");
    }
}

TEST(TestPerf, TLBStaticTensix) {
    const size_t tlb_1m_index = 0;

    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>();
    const CoreCoord tensix_core = cluster->get_soc_descriptor(chip).get_cores(CoreType::TENSIX)[0];
    cluster->start_device(tt_device_params{});

    cluster->configure_tlb(0, tensix_core, tlb_1m_index, 0x0, TLB_DATA::Relaxed);

    const std::vector<uint32_t> sizes = {
        1 * one_mb,
    };

    for (uint32_t buf_size : sizes) {
        const uint32_t num_io = buf_size / one_mb;
        perf_read_write(
            buf_size,
            num_io,
            cluster,
            tensix_core,
            "Static TLB: Host -> Device Tensix L1",
            "Static TLB: Device Tensix L1 -> Host");
    }
}

TEST(TestPerf, TLBStaticDram) {
    const std::vector<uint32_t> sizes = {
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

    cluster->configure_tlb(0, dram_core, tlb_16m_index, 0x0, TLB_DATA::Relaxed);

    for (uint32_t buf_size : sizes) {
        const uint32_t num_io = buf_size / (16 * one_mb);

        perf_read_write(
            buf_size, num_io, cluster, dram_core, "Static TLB: Host -> Device DRAM", "Static TLB: Device DRAM -> Host");
    }
}

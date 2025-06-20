// SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0
#include "gtest/gtest.h"
#include "tests/test_utils/device_test_utils.hpp"
#include "umd/device/chip_helpers/sysmem_manager.h"

using namespace tt::umd;

const uint32_t HUGEPAGE_REGION_SIZE = 1 << 30;  // 1GB

TEST(ApiSysmemManager, BasicIO) {
    std::vector<int> pci_device_ids = PCIDevice::enumerate_devices();

    for (int pci_device_id : pci_device_ids) {
        std::unique_ptr<TTDevice> tt_device = TTDevice::create(pci_device_id);

        std::unique_ptr<TLBManager> tlb_manager = std::make_unique<TLBManager>(tt_device.get());

        std::unique_ptr<SysmemManager> sysmem = std::make_unique<SysmemManager>(tlb_manager.get());

        // Initializes system memory with one channel.
        sysmem->init_hugepage(1);

        // Simple write and read test.
        std::vector<uint32_t> data_write = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        sysmem->write_to_sysmem(0, data_write.data(), 0, data_write.size() * sizeof(uint32_t));

        std::vector<uint32_t> data_read = std::vector<uint32_t>(data_write.size(), 0);
        sysmem->read_from_sysmem(0, data_read.data(), 0, data_read.size() * sizeof(uint32_t));

        EXPECT_EQ(data_write, data_read);

        // Channel 1 is not setup, so this should throw an exception.
        EXPECT_THROW(
            sysmem->write_to_sysmem(1, data_write.data(), 0, data_write.size() * sizeof(uint32_t)), std::runtime_error);

        // When we write over the limit, the address is wrapped around the hugepage size
        sysmem->write_to_sysmem(
            0, data_write.data(), HUGEPAGE_REGION_SIZE + 0x100, data_write.size() * sizeof(uint32_t));
        data_read = std::vector<uint32_t>(data_write.size(), 0);
        sysmem->read_from_sysmem(0, data_read.data(), 0x100, data_read.size() * sizeof(uint32_t));
        EXPECT_EQ(data_write, data_read);
    }
}

TEST(ApiSysmemManager, SysmemBuffersAllocation) {
    std::vector<int> pci_device_ids = PCIDevice::enumerate_devices();
    if (pci_device_ids.empty()) {
        GTEST_SKIP() << "No chips present on the system. Skipping test.";
    }
    if (!PCIDevice(pci_device_ids[0]).is_iommu_enabled()) {
        GTEST_SKIP() << "Skipping test since IOMMU is not enabled.";
    }

    const uint32_t one_mb = 1 << 20;

    std::cout << "Sysmem buffer allocation test, each buffer is 1MB." << std::endl;

    uint32_t pages_allocated = 0;

    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>(tt::umd::ClusterOptions{
        .num_host_mem_ch_per_mmio_device = 0,
    });

    std::vector<std::unique_ptr<SysmemBuffer>> sysmem_buffers;

    for (const chip_id_t chip_id : cluster->get_target_device_ids()) {
        SysmemManager* sysmem_manager = cluster->get_chip(chip_id)->get_sysmem_manager();

        std::cout << "--------------------------------" << std::endl;
        std::cout << "Testing allocation for PCI device ID: "
                  << cluster->get_tt_device(chip_id)->get_pci_device()->get_device_num() << std::endl;

        while (true) {
            try {
                sysmem_buffers.push_back(sysmem_manager->allocate_sysmem_buffer(one_mb));
            } catch (...) {
                break;
            }
        }

        uint64_t sysmem_buffer_size = sysmem_buffers.size() * one_mb;

        std::cout << "Allocated " << (double)sysmem_buffer_size / one_mb
                  << " MB of sysmem buffers each being 1MB in size." << std::endl;
    }
}

TEST(ApiSysmemManager, SysmemBuffers) {
    std::vector<int> pci_device_ids = PCIDevice::enumerate_devices();
    if (pci_device_ids.empty()) {
        GTEST_SKIP() << "No chips present on the system. Skipping test.";
    }
    if (!PCIDevice(pci_device_ids[0]).is_iommu_enabled()) {
        GTEST_SKIP() << "Skipping test since IOMMU is not enabled.";
    }

    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>(tt::umd::ClusterOptions{
        .num_host_mem_ch_per_mmio_device = 0,
    });

    const chip_id_t mmio_chip = *cluster->get_target_mmio_device_ids().begin();

    SysmemManager* sysmem_manager = cluster->get_chip(mmio_chip)->get_sysmem_manager();

    const uint32_t one_mb = 1 << 20;
    std::unique_ptr<SysmemBuffer> sysmem_buffer = sysmem_manager->allocate_sysmem_buffer(2 * one_mb);

    const CoreCoord tensix_core = cluster->get_soc_descriptor(mmio_chip).get_cores(CoreType::TENSIX)[0];

    // Zero out 1MB of Tensix L1.
    std::vector<uint8_t> data_write(one_mb, 0);
    cluster->write_to_device(data_write.data(), one_mb, mmio_chip, tensix_core, 0);

    uint8_t* sysmem_data = static_cast<uint8_t*>(sysmem_buffer->get_buffer_va());

    for (uint32_t i = 0; i < one_mb; ++i) {
        sysmem_data[i] = static_cast<uint8_t>(i % 256);
    }

    // Write pattern to first 1MB of Tensix L1.
    sysmem_buffer->dma_write_to_device(0, one_mb, tensix_core, 0);

    // Read regularly to check Tensix L1 matches the pattern.
    std::vector<uint8_t> readback(one_mb, 0);
    cluster->dma_read_from_device(readback.data(), one_mb, mmio_chip, tensix_core, 0);

    for (uint32_t i = 0; i < one_mb; ++i) {
        EXPECT_EQ(sysmem_data[i], readback[i]);
    }

    uint8_t* sysmem_data_readback = sysmem_data + one_mb;

    // Zero out sysmem_data_readback. We are doing this in case the pattern was already present in the sysmem buffer.
    for (uint32_t i = 0; i < one_mb; ++i) {
        sysmem_data_readback[i] = 0;
    }

    // Read data back from Tensix L1 to sysmem_data_readback.
    sysmem_buffer->dma_read_from_device(one_mb, one_mb, tensix_core, 0);

    for (uint32_t i = 0; i < one_mb; ++i) {
        EXPECT_EQ(sysmem_data[i], sysmem_data_readback[i]);
    }
}

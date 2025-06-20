/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#include <gtest/gtest.h>

#include "umd/device/cluster.h"
#include "umd/device/tt_device/tlb_window.h"
#include "umd/device/types/tlb.h"

using namespace tt::umd;

bool is_kmd_version_good() {
    semver_t kmd_ver = PCIDevice::read_kmd_version();

    return kmd_ver.major > 1 || (kmd_ver.major == 1 && kmd_ver.minor >= 34);
}

TEST(TestTlb, TestTlbWindowAllocateNew) {
    if (!is_kmd_version_good()) {
        GTEST_SKIP() << "Skipping test because of old KMD version. Required version of KMD is 1.34 or higher.";
    }
    const uint64_t tensix_addr = 0;
    const chip_id_t chip = 0;
    const uint64_t two_mb_size = 1 << 21;

    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>();

    uint32_t val = 0;
    std::vector<CoreCoord> tensix_cores =
        cluster->get_soc_descriptor(chip).get_cores(CoreType::TENSIX, CoordSystem::TRANSLATED);
    for (CoreCoord core : tensix_cores) {
        cluster->write_to_device(&val, sizeof(uint32_t), chip, core, tensix_addr);
        val++;
    }

    PCIDevice* pci_device = cluster->get_tt_device(chip)->get_pci_device().get();

    uint32_t value_check = 0;

    for (CoreCoord core : tensix_cores) {
        tlb_data config;
        config.local_offset = 0;
        config.x_end = core.x;
        config.y_end = core.y;
        config.x_start = 0;
        config.y_start = 0;
        config.noc_sel = 0;
        config.mcast = 0;
        config.ordering = tlb_data::Relaxed;
        config.linked = 0;
        config.static_vc = 1;

        std::unique_ptr<TlbWindow> tlb_window =
            std::make_unique<TlbWindow>(pci_device->allocate_tlb(two_mb_size, TlbMapping::WC), config);

        uint32_t readback_value = tlb_window->read32(0);

        EXPECT_EQ(readback_value, value_check);

        value_check++;
    }
}

TEST(TestTlb, TestTlbWindowReuse) {
    if (!is_kmd_version_good()) {
        GTEST_SKIP() << "Skipping test because of old KMD version. Required version of KMD is 1.34 or higher.";
    }
    const uint64_t tensix_addr = 0;
    const chip_id_t chip = 0;
    const uint64_t two_mb_size = 1 << 21;

    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>();

    uint32_t val = 0;
    std::vector<CoreCoord> tensix_cores =
        cluster->get_soc_descriptor(chip).get_cores(CoreType::TENSIX, CoordSystem::TRANSLATED);
    for (CoreCoord core : tensix_cores) {
        cluster->write_to_device(&val, sizeof(uint32_t), chip, core, tensix_addr);
        val++;
    }

    PCIDevice* pci_device = cluster->get_tt_device(chip)->get_pci_device().get();

    uint32_t value_check = 0;

    // Here it's not important how we have configured the TLB. For every read we will
    // do the reconfigure of the TLB window.
    tlb_data config{};
    std::unique_ptr<TlbWindow> tlb_window =
        std::make_unique<TlbWindow>(pci_device->allocate_tlb(two_mb_size, TlbMapping::WC), config);

    for (CoreCoord core : tensix_cores) {
        tlb_data config;
        config.local_offset = 0;
        config.x_end = core.x;
        config.y_end = core.y;
        config.x_start = 0;
        config.y_start = 0;
        config.noc_sel = 0;
        config.mcast = 0;
        config.ordering = tlb_data::Relaxed;
        config.linked = 0;
        config.static_vc = 1;

        tlb_window->configure(config);

        uint32_t readback_value = tlb_window->read32(0);

        EXPECT_EQ(readback_value, value_check);

        value_check++;
    }
}

// TODO: debug this test failing on T3K.
TEST(TestTlb, DISABLED_TestTlbWindowReadRegister) {
    if (!is_kmd_version_good()) {
        GTEST_SKIP() << "Skipping test because of old KMD version. Required version of KMD is 1.34 or higher.";
    }
    const uint64_t tensix_addr = 0;
    const chip_id_t chip = 0;
    const uint64_t two_mb_size = 1 << 21;

    // Point of the test is to read NOC0 node id register.
    // TLB needs to be aligned to 2MB so these base and offset values are
    // how TLB should be programmed in order to get to addr 0xFFB2002C.
    const uint64_t tlb_base = 0xFFA00000;
    const uint64_t noc_node_id_tlb_offset = 0x12002C;

    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>();

    PCIDevice* pci_device = cluster->get_tt_device(0)->get_pci_device().get();

    const std::vector<CoreCoord> tensix_cores =
        cluster->get_soc_descriptor(chip).get_cores(CoreType::TENSIX, CoordSystem::TRANSLATED);
    for (CoreCoord core : tensix_cores) {
        tlb_data config;
        config.local_offset = tlb_base & ~(two_mb_size - 1);
        config.x_end = core.x;
        config.y_end = core.y;
        config.x_start = 0;
        config.y_start = 0;
        config.noc_sel = 0;
        config.mcast = 0;
        config.ordering = tlb_data::Strict;
        config.linked = 0;
        config.static_vc = 1;

        std::unique_ptr<TlbWindow> tlb_window =
            std::make_unique<TlbWindow>(pci_device->allocate_tlb(two_mb_size, TlbMapping::UC), config);

        tlb_window->configure(config);

        uint32_t noc_node_id_val = tlb_window->read_register(noc_node_id_tlb_offset & (two_mb_size - 1));

        uint32_t x = noc_node_id_val & 0x3F;
        uint32_t y = (noc_node_id_val >> 6) & 0x3F;

        EXPECT_EQ(core.x, x);
        EXPECT_EQ(core.y, y);
    }
}

TEST(TestTlb, TestTlbWindowReadWrite) {
    if (!is_kmd_version_good()) {
        GTEST_SKIP() << "Skipping test because of old KMD version. Required version of KMD is 1.34 or higher.";
    }
    const uint64_t tensix_addr = 0;
    const chip_id_t chip = 0;
    const uint64_t two_mb_size = 1 << 21;

    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>();

    const std::vector<CoreCoord> tensix_cores =
        cluster->get_soc_descriptor(chip).get_cores(CoreType::TENSIX, CoordSystem::TRANSLATED);
    PCIDevice* pci_device = cluster->get_tt_device(chip)->get_pci_device().get();

    for (CoreCoord core : tensix_cores) {
        tlb_data config_write;
        config_write.local_offset = 0;
        config_write.x_end = core.x;
        config_write.y_end = core.y;
        config_write.x_start = 0;
        config_write.y_start = 0;
        config_write.noc_sel = 0;
        config_write.mcast = 0;
        config_write.ordering = tlb_data::Relaxed;
        config_write.linked = 0;
        config_write.static_vc = 1;

        std::unique_ptr<TlbWindow> tlb_window_write =
            std::make_unique<TlbWindow>(pci_device->allocate_tlb(two_mb_size, TlbMapping::WC), config_write);

        tlb_window_write->write32(0, 4);
        tlb_window_write->write32(4, 0);

        tlb_data config_read = config_write;
        std::unique_ptr<TlbWindow> tlb_window_read =
            std::make_unique<TlbWindow>(pci_device->allocate_tlb(two_mb_size, TlbMapping::WC), config_read);

        uint32_t expect4 = tlb_window_read->read32(0);
        uint32_t expect0 = tlb_window_read->read32(4);

        EXPECT_EQ(expect4, 4);
        EXPECT_EQ(expect0, 0);
    }
}

TEST(TestTlb, TestTlbOffsetReadWrite) {
    if (!is_kmd_version_good()) {
        GTEST_SKIP() << "Skipping test because of old KMD version. Required version of KMD is 1.34 or higher.";
    }
    const uint64_t tensix_addr = 0;
    const chip_id_t chip = 0;
    const uint64_t two_mb = 1 << 21;
    const uint64_t one_mb = 1 << 20;

    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>();

    const std::vector<CoreCoord> tensix_cores =
        cluster->get_soc_descriptor(chip).get_cores(CoreType::TENSIX, CoordSystem::TRANSLATED);
    PCIDevice* pci_device = cluster->get_tt_device(chip)->get_pci_device().get();

    std::vector<uint8_t> write_pattern(0x100, 0);
    for (size_t i = 0; i < write_pattern.size(); ++i) {
        write_pattern[i] = (i % 256);
    }

    for (CoreCoord core : tensix_cores) {
        cluster->write_to_device(write_pattern.data(), write_pattern.size(), chip, core, one_mb);

        tlb_data config;
        config.local_offset = 0;
        config.x_end = core.x;
        config.y_end = core.y;
        config.x_start = 0;
        config.y_start = 0;
        config.noc_sel = 0;
        config.mcast = 0;
        config.ordering = tlb_data::Relaxed;
        config.linked = 0;
        config.static_vc = 1;

        std::unique_ptr<TlbWindow> read_aligned =
            std::make_unique<TlbWindow>(pci_device->allocate_tlb(two_mb, TlbMapping::WC), config);

        config.local_offset = one_mb;
        std::unique_ptr<TlbWindow> read_unaligned =
            std::make_unique<TlbWindow>(pci_device->allocate_tlb(two_mb, TlbMapping::WC), config);

        std::vector<uint8_t> readback_aligned(0x100, 0);
        read_aligned->read_block(one_mb, readback_aligned.data(), readback_aligned.size());

        EXPECT_EQ(readback_aligned, write_pattern)
            << "Readback data from aligned TLB window should match the written pattern";

        std::vector<uint8_t> readback_unaligned(0x100, 0);
        read_unaligned->read_block(0, readback_unaligned.data(), readback_unaligned.size());

        EXPECT_EQ(readback_aligned, readback_unaligned)
            << "Readback data from aligned and unaligned TLB windows should be the same";

        config.local_offset = (one_mb >> 1);
        read_unaligned->configure(config);
        std::vector<uint8_t> readback_unaligned_1(0x100, 0);
        read_unaligned->read_block(one_mb >> 1, readback_unaligned_1.data(), readback_unaligned_1.size());

        EXPECT_EQ(readback_unaligned_1, write_pattern)
            << "Readback data from unaligned TLB window with offset should match the written pattern";
    }
}

TEST(TestTlb, TestTlbAccessOutofBounds) {
    if (!is_kmd_version_good()) {
        GTEST_SKIP() << "Skipping test because of old KMD version. Required version of KMD is 1.34 or higher.";
    }
    const uint64_t tensix_addr = 0;
    const chip_id_t chip = 0;
    const uint64_t two_mb = 1 << 21;
    const uint64_t one_mb = 1 << 20;

    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>();

    const std::vector<CoreCoord> tensix_cores =
        cluster->get_soc_descriptor(chip).get_cores(CoreType::TENSIX, CoordSystem::TRANSLATED);
    PCIDevice* pci_device = cluster->get_tt_device(chip)->get_pci_device().get();

    for (CoreCoord core : tensix_cores) {
        tlb_data config;
        config.local_offset = 0;
        config.x_end = core.x;
        config.y_end = core.y;
        config.x_start = 0;
        config.y_start = 0;
        config.noc_sel = 0;
        config.mcast = 0;
        config.ordering = tlb_data::Relaxed;
        config.linked = 0;
        config.static_vc = 1;

        std::unique_ptr<TlbWindow> read_aligned =
            std::make_unique<TlbWindow>(pci_device->allocate_tlb(two_mb, TlbMapping::WC), config);

        config.local_offset = one_mb;
        std::unique_ptr<TlbWindow> read_unaligned =
            std::make_unique<TlbWindow>(pci_device->allocate_tlb(two_mb, TlbMapping::WC), config);

        std::vector<uint8_t> readback_aligned(0x100, 0);
        read_aligned->read_block(one_mb, readback_aligned.data(), readback_aligned.size());

        std::vector<uint8_t> readback_unaligned(0x100, 0);
        read_unaligned->read_block(0, readback_unaligned.data(), readback_unaligned.size());

        EXPECT_EQ(readback_aligned, readback_unaligned)
            << "Readback data from aligned and unaligned TLB windows should be the same";

        std::vector<uint8_t> readback_out_of_bounds(two_mb + 1, 0);
        EXPECT_ANY_THROW(read_aligned->read_block(0, readback_out_of_bounds.data(), readback_out_of_bounds.size()))
            << "Reading out of bounds from TLB window should throw an exception";

        std::vector<uint8_t> readback_out_of_bounds_unaligned(one_mb + 1, 0);
        EXPECT_ANY_THROW(read_unaligned->read_block(
            0, readback_out_of_bounds_unaligned.data(), readback_out_of_bounds_unaligned.size()))
            << "Reading out of bounds from TLB window should throw an exception";
    }
}

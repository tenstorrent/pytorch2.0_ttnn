// SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0
#include "gtest/gtest.h"
#include "umd/device/tt_device/tt_device.h"

using namespace tt::umd;

TEST(BlackholeChipInfo, BasicChipInfo) {
    std::vector<int> pci_device_ids = PCIDevice::enumerate_devices();

    for (int pci_device_id : pci_device_ids) {
        std::unique_ptr<TTDevice> tt_device = TTDevice::create(pci_device_id);

        const ChipInfo chip_info = tt_device->get_chip_info();

        EXPECT_TRUE(
            chip_info.board_type == BoardType::P100 || chip_info.board_type == BoardType::P150 ||
            chip_info.board_type == BoardType::P300);

        // TODO: uncomment this when we can read asic location properly from telemetry.
        // EXPECT_TRUE(chip_info.chip_uid.asic_location == 0 || chip_info.chip_uid.asic_location == 1);
    }
}

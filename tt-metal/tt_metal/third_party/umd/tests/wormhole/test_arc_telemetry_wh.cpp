// SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0
#include "gtest/gtest.h"
#include "umd/device/arc_telemetry_reader.h"
#include "umd/device/types/wormhole_telemetry.h"

using namespace tt::umd;

TEST(WormholeTelemetry, BasicWormholeTelemetry) {
    std::vector<int> pci_device_ids = PCIDevice::enumerate_devices();

    for (int pci_device_id : pci_device_ids) {
        std::unique_ptr<TTDevice> tt_device = TTDevice::create(pci_device_id);
        std::unique_ptr<ArcTelemetryReader> blackhole_arc_telemetry_reader =
            ArcTelemetryReader::create_arc_telemetry_reader(tt_device.get());

        uint32_t board_id_high = blackhole_arc_telemetry_reader->read_entry(wormhole::TAG_BOARD_ID_HIGH);
        uint32_t board_id_low = blackhole_arc_telemetry_reader->read_entry(wormhole::TAG_BOARD_ID_LOW);

        const uint64_t board_id = ((uint64_t)board_id_high << 32) | (board_id_low);
        EXPECT_NO_THROW(get_board_type_from_board_id(board_id));
    }
}

TEST(WormholeTelemetry, WormholeTelemetryEntryAvailable) {
    std::vector<int> pci_device_ids = PCIDevice::enumerate_devices();

    for (int pci_device_id : pci_device_ids) {
        std::unique_ptr<TTDevice> tt_device = TTDevice::create(pci_device_id);
        std::unique_ptr<ArcTelemetryReader> telemetry =
            ArcTelemetryReader::create_arc_telemetry_reader(tt_device.get());

        for (uint32_t telem_tag = 0; telem_tag < wormhole::TELEMETRY_NUMBER_OF_TAGS; telem_tag++) {
            EXPECT_TRUE(telemetry->is_entry_available(telem_tag));
        }

        EXPECT_FALSE(telemetry->is_entry_available(wormhole::TELEMETRY_NUMBER_OF_TAGS));
    }
}

// SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0
#include <memory>
#include <thread>

#include "gtest/gtest.h"
#include "umd/device/arc_messenger.h"
#include "umd/device/blackhole_arc_telemetry_reader.h"
#include "umd/device/cluster.h"
#include "umd/device/types/blackhole_arc.h"

using namespace tt::umd;

TEST(BlackholeArcMessages, BlackholeArcMessagesBasic) {
    std::vector<int> pci_device_ids = PCIDevice::enumerate_devices();

    for (int pci_device_id : pci_device_ids) {
        std::unique_ptr<TTDevice> tt_device = TTDevice::create(pci_device_id);

        std::unique_ptr<ArcMessenger> bh_arc_messenger = ArcMessenger::create_arc_messenger(tt_device.get());

        const uint32_t num_loops = 100;
        for (int i = 0; i < num_loops; i++) {
            uint32_t response = bh_arc_messenger->send_message((uint32_t)blackhole::ArcMessageType::TEST);
            ASSERT_EQ(response, 0);
        }
    }
}

TEST(BlackholeArcMessages, BlackholeArcMessageHigherAIClock) {
    const uint32_t ms_sleep = 2000;

    std::vector<int> pci_device_ids = PCIDevice::enumerate_devices();

    for (int pci_device_id : pci_device_ids) {
        std::unique_ptr<TTDevice> tt_device = TTDevice::create(pci_device_id);

        std::unique_ptr<ArcMessenger> bh_arc_messenger = ArcMessenger::create_arc_messenger(tt_device.get());

        uint32_t response = bh_arc_messenger->send_message((uint32_t)blackhole::ArcMessageType::AICLK_GO_BUSY);

        // Wait for telemetry to update AICLK.
        std::this_thread::sleep_for(std::chrono::milliseconds(ms_sleep));

        uint32_t aiclk = tt_device->get_clock();

        // TODO #781: For now expect only that busy val is something larger than idle val.
        EXPECT_GT(aiclk, blackhole::AICLK_IDLE_VAL);

        response = bh_arc_messenger->send_message((uint32_t)blackhole::ArcMessageType::AICLK_GO_LONG_IDLE);

        // Wait for telemetry to update AICLK.
        std::this_thread::sleep_for(std::chrono::milliseconds(ms_sleep));

        aiclk = tt_device->get_clock();

        EXPECT_EQ(aiclk, blackhole::AICLK_IDLE_VAL);
    }
}

TEST(BlackholeArcMessages, MultipleThreadsArcMessages) {
    std::unique_ptr<Cluster> cluster = std::make_unique<Cluster>();

    const uint32_t num_loops = 1000;

    for (uint32_t chip_id : cluster->get_target_mmio_device_ids()) {
        TTDevice* tt_device = cluster->get_tt_device(chip_id);

        std::thread thread0([&]() {
            std::unique_ptr<ArcMessenger> arc_messenger = ArcMessenger::create_arc_messenger(tt_device);

            for (uint32_t loop = 0; loop < num_loops; loop++) {
                uint32_t response = arc_messenger->send_message((uint32_t)blackhole::ArcMessageType::TEST);
                ASSERT_EQ(response, 0);
            }
        });

        std::thread thread1([&]() {
            std::unique_ptr<ArcMessenger> arc_messenger = ArcMessenger::create_arc_messenger(tt_device);

            for (uint32_t loop = 0; loop < num_loops; loop++) {
                uint32_t response = arc_messenger->send_message((uint32_t)blackhole::ArcMessageType::TEST);
                ASSERT_EQ(response, 0);
            }
        });

        thread0.join();
        thread1.join();
    }
}

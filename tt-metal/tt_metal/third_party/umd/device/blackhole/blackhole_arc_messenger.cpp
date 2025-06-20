/*
 * SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#include "umd/device/blackhole_arc_messenger.h"

#include "umd/device/tt_device/tt_device.h"

namespace tt::umd {

BlackholeArcMessenger::BlackholeArcMessenger(TTDevice* tt_device) : ArcMessenger(tt_device) {
    blackhole_arc_msg_queue = BlackholeArcMessageQueue::get_blackhole_arc_message_queue(
        tt_device, BlackholeArcMessageQueueIndex::APPLICATION);
}

uint32_t BlackholeArcMessenger::send_message(
    const uint32_t msg_code, std::vector<uint32_t>& return_values, uint16_t arg0, uint16_t arg1, uint32_t timeout_ms) {
    auto lock = lock_manager.acquire_mutex(MutexType::ARC_MSG, tt_device->get_pci_device()->get_device_num());
    return blackhole_arc_msg_queue->send_message((ArcMessageType)msg_code, arg0, arg1, timeout_ms);
}

}  // namespace tt::umd

/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#pragma once

#include "umd/device/arc_messenger.h"
#include "umd/device/blackhole_arc_message_queue.h"

namespace tt::umd {

class BlackholeArcMessenger : public ArcMessenger {
public:
    /**
     * Constructor for BlackholeArcMessenger.
     *
     * @param tt_device TTDevice object used to communicate with the ARC of the device.
     */
    BlackholeArcMessenger(TTDevice* tt_device);

    /**
     * Send ARC message. The call of send_message is blocking, timeout is to be implemented.
     *
     * @param msg_code ARC messsage type.
     * @param arg0 arg0 for the message.
     * @param arg1 arg1 for the message.
     */
    uint32_t send_message(
        const uint32_t msg_code,
        std::vector<uint32_t>& return_values,
        uint16_t arg0 = 0,
        uint16_t arg1 = 0,
        uint32_t timeout_ms = 1000) override;

private:
    std::unique_ptr<BlackholeArcMessageQueue> blackhole_arc_msg_queue = nullptr;
};

}  // namespace tt::umd

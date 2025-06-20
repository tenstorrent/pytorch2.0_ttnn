/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#pragma once

#include <cstdint>
#include <memory>
#include <string_view>
#include <vector>

#include "umd/device/utils/lock_manager.h"

namespace tt::umd {

class TTDevice;

class ArcMessenger {
public:
    /**
     * Create an ArcMessenger object.
     *
     * @param tt_device TTDevice object used to communicate with the ARC of the device.
     * @return Unique pointer to ArcMessenger object.
     */
    static std::unique_ptr<ArcMessenger> create_arc_messenger(TTDevice* tt_device);

    /**
     * Send ARC message. The call of send_message is blocking, timeout is to be implemented.
     *
     * @param msg_code ARC messsage type.
     * @param return_values Return values from the ARC message.
     * @param arg0 arg0 for the message.
     * @param arg1 arg1 for the message.
     * @param timeout_ms Timeout in milliseconds; 0 to wait indefinitely.
     * @return Success code of the ARC message.
     */
    virtual uint32_t send_message(
        const uint32_t msg_code,
        std::vector<uint32_t>& return_values,
        uint16_t arg0 = 0,
        uint16_t arg1 = 0,
        uint32_t timeout_ms = 1000) = 0;

    /**
     * Send ARC message. The call of send_message is blocking, timeout is to be implemented.
     * This version of the function can be called if the return values are not needed.
     *
     * @param msg_code ARC messsage type.
     * @param arg0 arg0 for the message.
     * @param arg1 arg1 for the message.
     * @param timeout_ms Timeout in milliseconds; 0 to wait indefinitely.
     * @return Success code of the ARC message.
     */
    uint32_t send_message(const uint32_t msg_code, uint16_t arg0 = 0, uint16_t arg1 = 0, uint32_t timeout_ms = 1000);

    virtual ~ArcMessenger();

protected:
    /**
     * Constructor for ArcMessenger.
     *
     * @param tt_device TTDevice object used to communicate with the ARC of the device.
     */
    ArcMessenger(TTDevice* tt_device);

    TTDevice* tt_device;
    LockManager lock_manager;
};

}  // namespace tt::umd

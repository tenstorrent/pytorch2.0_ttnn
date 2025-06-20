/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#pragma once

#include "umd/device/chip/local_chip.h"
#include "umd/device/tt_device/blackhole_tt_device.h"

namespace tt::umd {
class RemoteBlackholeTTDevice : public BlackholeTTDevice {
public:
    RemoteBlackholeTTDevice();
};
}  // namespace tt::umd

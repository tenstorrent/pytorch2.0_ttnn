// SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0
#include "umd/device/tt_device/remote_blackhole_tt_device.h"

namespace tt::umd {

RemoteBlackholeTTDevice::RemoteBlackholeTTDevice() : BlackholeTTDevice() {
    throw std::runtime_error("Creating remote TTDevice is not supported for Blackhole.");
}

}  // namespace tt::umd

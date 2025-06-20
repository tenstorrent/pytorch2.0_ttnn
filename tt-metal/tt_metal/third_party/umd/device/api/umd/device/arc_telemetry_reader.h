/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#pragma once

#include "umd/device/tt_device/tt_device.h"

namespace tt::umd {

class ArcTelemetryReader {
public:
    virtual ~ArcTelemetryReader() = default;

    virtual uint32_t read_entry(const uint8_t telemetry_tag) = 0;

    virtual bool is_entry_available(const uint8_t telemetry_tag) = 0;

    static std::unique_ptr<ArcTelemetryReader> create_arc_telemetry_reader(TTDevice* tt_device);

protected:
    ArcTelemetryReader(TTDevice* tt_device);

    TTDevice* tt_device;
};

}  // namespace tt::umd

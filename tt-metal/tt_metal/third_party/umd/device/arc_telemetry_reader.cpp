/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#include "umd/device/arc_telemetry_reader.h"

#include "umd/device/blackhole_arc_telemetry_reader.h"
#include "umd/device/wormhole_arc_telemetry_reader.h"

namespace tt::umd {

ArcTelemetryReader::ArcTelemetryReader(TTDevice* tt_device) : tt_device(tt_device) {}

std::unique_ptr<ArcTelemetryReader> ArcTelemetryReader::create_arc_telemetry_reader(TTDevice* tt_device) {
    switch (tt_device->get_arch()) {
        case tt::ARCH::WORMHOLE_B0:
            return std::make_unique<WormholeArcTelemetryReader>(tt_device);
        case tt::ARCH::BLACKHOLE:
            return std::make_unique<BlackholeArcTelemetryReader>(tt_device);
        default:
            throw std::runtime_error("Unsupported architecture for creating Arc telemetry reader.");
    }
}

}  // namespace tt::umd

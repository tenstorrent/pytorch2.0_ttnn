/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#pragma once

#include "umd/device/arc_messenger.h"
#include "umd/device/arc_telemetry_reader.h"
#include "umd/device/wormhole_implementation.h"

extern bool umd_use_noc1;

namespace tt::umd {

class WormholeArcTelemetryReader : public ArcTelemetryReader {
public:
    WormholeArcTelemetryReader(TTDevice* tt_device);

    uint32_t read_entry(const uint8_t telemetry_tag) override;

    bool is_entry_available(const uint8_t telemetry_tag) override;

private:
    void initialize_telemetry();

    void verify_telemetry();

    uint64_t telemetry_base_noc_addr;

    // During initialization of telemetry, if the NOC0 is hung then we need to read the telemetry values from NOC1.
    const tt_xy_pair arc_core = !umd_use_noc1
                                    ? tt::umd::wormhole::ARC_CORES_NOC0[0]
                                    : tt_xy_pair(
                                          tt::umd::wormhole::NOC0_X_TO_NOC1_X[tt::umd::wormhole::ARC_CORES_NOC0[0].x],
                                          tt::umd::wormhole::NOC0_Y_TO_NOC1_Y[tt::umd::wormhole::ARC_CORES_NOC0[0].y]);
};

}  // namespace tt::umd

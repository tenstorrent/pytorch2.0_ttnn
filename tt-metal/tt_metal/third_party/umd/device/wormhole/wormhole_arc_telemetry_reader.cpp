/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#include "umd/device/wormhole_arc_telemetry_reader.h"

#include "umd/device/types/wormhole_telemetry.h"

namespace tt::umd {

WormholeArcTelemetryReader::WormholeArcTelemetryReader(TTDevice* tt_device) : ArcTelemetryReader(tt_device) {
    initialize_telemetry();
}

void WormholeArcTelemetryReader::initialize_telemetry() {
    std::vector<uint32_t> arc_msg_return_values = {0};
    static const uint32_t timeout_ms = 1000;
    uint32_t exit_code = tt_device->get_arc_messenger()->send_message(
        tt::umd::wormhole::ARC_MSG_COMMON_PREFIX |
            (uint32_t)tt::umd::wormhole::arc_message_type::GET_SMBUS_TELEMETRY_ADDR,
        arc_msg_return_values,
        0,
        0,
        timeout_ms);

    static constexpr uint64_t noc_telemetry_offset = 0x810000000;
    telemetry_base_noc_addr = arc_msg_return_values[0] + noc_telemetry_offset;
    verify_telemetry();
}

void WormholeArcTelemetryReader::verify_telemetry() {
    // Seems that TAG_DEVICE_ID field in remote telemetry is not populated in the same way for remote and local chips.
    // TODO: figure out if there is any way for both local and remote chips to verify telemetry readouts.
    if (!tt_device->is_remote()) {
        uint32_t vendor_id = read_entry(tt::umd::wormhole::TAG_DEVICE_ID);
        constexpr uint32_t tt_vendor_id = 0x1e52;
        if ((vendor_id & 0xFFFF) != tt_vendor_id) {
            throw std::runtime_error(
                fmt::format("Tenstorrent vendor ID mismatch. Expected: 0x{:x}, Got: 0x{:x}", tt_vendor_id, vendor_id));
        }
    }
}

uint32_t WormholeArcTelemetryReader::read_entry(const uint8_t telemetry_tag) {
    if (!is_entry_available(telemetry_tag)) {
        throw std::runtime_error(fmt::format(
            "Telemetry entry {} not available. You can use is_entry_available() to check if the entry is available.",
            telemetry_tag));
    }

    uint32_t telemetry_value;
    tt_device->read_from_device(
        &telemetry_value, arc_core, telemetry_base_noc_addr + telemetry_tag * sizeof(uint32_t), sizeof(uint32_t));

    return telemetry_value;
}

bool WormholeArcTelemetryReader::is_entry_available(const uint8_t telemetry_tag) {
    return telemetry_tag >= 0 && telemetry_tag < tt::umd::wormhole::TELEMETRY_NUMBER_OF_TAGS;
}

}  // namespace tt::umd

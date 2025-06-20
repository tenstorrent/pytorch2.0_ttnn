/*
 * SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#pragma once

#include "umd/device/blackhole_implementation.h"
#include "umd/device/tt_core_coordinates.h"
#include "umd/device/types/blackhole_arc.h"
#include "umd/device/types/cluster_descriptor_types.h"

using namespace tt::umd::blackhole;

namespace tt::umd {

class TTDevice;

/* On Blackhole there are few ARC message queues that can be used to communicate with ARC FW.
 * ARC message queues are simple circular queues. There are read/write pointers both for requests and responses.
 * Reading from SCRATCH_RAM[11] gives the address of the ARC message queuse descriptor.
 *
 * | Purpose                  | Start bit offset | Length in bits |
 * ----------------------------------------------------------------
 * ARC address of first queue |                0 |             32 |
 * # of entries in each queue |               32 |              8 |
 * # of queues                |               40 |              8 |
 *
 * Each queue starts with a header followed by the request queue then the response queue.
 *
 * The read and write pointers are double-wrapping, meaning that they wrap at twice queue size. The number of occupied
 * entries in a queue is (wptr – rptr) % (2*size).
 *
 * Usage of this class is not thread-safe, this synchronization is going to be implemented, similar to Wormhole.
 */
class BlackholeArcMessageQueue {
private:
    // Header length and entry length in words.
    static constexpr uint8_t header_len = 8;
    static constexpr uint8_t entry_len = 8;

    static constexpr uint8_t request_wptr_offset = 0;
    static constexpr uint8_t response_rptr_offset = 1;
    static constexpr uint8_t request_rptr_offset = 4;
    static constexpr uint8_t response_wptr_offset = 5;

public:
    BlackholeArcMessageQueue(
        TTDevice* tt_device, const uint64_t base_address, const uint64_t size, const tt_xy_pair arc_core);

    /*
     * Send ARC message. The call of send_message is blocking, timeout is to be implemented.
     */
    uint32_t send_message(
        const ArcMessageType message_type, uint16_t arg0 = 0, uint16_t arg1 = 0, uint32_t timeout_ms = 1000);

    static std::unique_ptr<BlackholeArcMessageQueue> get_blackhole_arc_message_queue(
        TTDevice* tt_device, const size_t queue_index);

private:
    void push_request(std::array<uint32_t, BlackholeArcMessageQueue::entry_len>& request, uint32_t timeout_ms);

    std::array<uint32_t, entry_len> pop_response(uint32_t timeout_ms);

    void read_words(uint32_t* data, size_t num_words, size_t offset);

    uint32_t read_word(size_t offset);

    void write_words(uint32_t* data, size_t num_words, size_t offset);

    void trigger_fw_int();

    const uint64_t base_address;
    const uint64_t size;
    TTDevice* tt_device;
    const tt_xy_pair arc_core;
};

}  // namespace tt::umd

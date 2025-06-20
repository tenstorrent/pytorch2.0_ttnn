/*
 * SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#include "umd/device/blackhole_arc_message_queue.h"

#include "umd/device/tt_device/tt_device.h"

extern bool umd_use_noc1;

namespace tt::umd {

BlackholeArcMessageQueue::BlackholeArcMessageQueue(
    TTDevice* tt_device, const uint64_t base_address, const uint64_t size, const tt_xy_pair arc_core) :
    base_address(base_address), size(size), tt_device(tt_device), arc_core(arc_core) {}

void BlackholeArcMessageQueue::read_words(uint32_t* data, size_t num_words, size_t offset) {
    tt_device->read_from_device(data, arc_core, base_address + offset * sizeof(uint32_t), num_words * sizeof(uint32_t));
}

uint32_t BlackholeArcMessageQueue::read_word(size_t offset) {
    uint32_t word;
    read_words(&word, 1, offset);
    return word;
}

void BlackholeArcMessageQueue::write_words(uint32_t* data, size_t num_words, size_t offset) {
    tt_device->write_to_device(data, arc_core, base_address + offset * sizeof(uint32_t), num_words * sizeof(uint32_t));
}

void BlackholeArcMessageQueue::trigger_fw_int() {
    tt_device->write_to_device((void*)&ARC_FW_INT_VAL, arc_core, ARC_FW_INT_ADDR, sizeof(uint32_t));
}

void BlackholeArcMessageQueue::push_request(
    std::array<uint32_t, BlackholeArcMessageQueue::entry_len>& request, uint32_t timeout_ms) {
    uint32_t request_queue_wptr = read_word(request_wptr_offset);

    auto start = std::chrono::steady_clock::now();
    while (true) {
        uint32_t request_queue_rptr = read_word(request_rptr_offset);
        if (abs((int)request_queue_rptr - (int)request_queue_wptr) % (2 * size) != size) {
            break;
        }

        auto now = std::chrono::steady_clock::now();
        auto elapsed_ms = std::chrono::duration_cast<std::chrono::milliseconds>(now - start).count();
        if (elapsed_ms > timeout_ms && timeout_ms != 0) {
            throw std::runtime_error("Timeout waiting for ARC msg request queue.");
        }
    }

    // Offset in words.
    uint32_t request_entry_offset = header_len + (request_queue_wptr % size) * BlackholeArcMessageQueue::entry_len;
    write_words(request.data(), BlackholeArcMessageQueue::entry_len, request_entry_offset);

    request_queue_wptr = (request_queue_wptr + 1) % (2 * size);
    write_words(&request_queue_wptr, 1, request_wptr_offset);

    trigger_fw_int();
}

std::array<uint32_t, BlackholeArcMessageQueue::entry_len> BlackholeArcMessageQueue::pop_response(uint32_t timeout_ms) {
    uint32_t response_queue_rptr = read_word(response_rptr_offset);

    auto start = std::chrono::steady_clock::now();
    while (true) {
        uint32_t response_queue_wptr = read_word(response_wptr_offset);

        if (response_queue_rptr != response_queue_wptr) {
            break;
        }

        auto now = std::chrono::steady_clock::now();
        auto elapsed_ms = std::chrono::duration_cast<std::chrono::milliseconds>(now - start).count();
        if (elapsed_ms > timeout_ms && timeout_ms != 0) {
            throw std::runtime_error("Timeout waiting for ARC msg response queue.");
        }
    }

    uint32_t response_entry_offset =
        header_len + (size + (response_queue_rptr % size)) * BlackholeArcMessageQueue::entry_len;
    std::array<uint32_t, BlackholeArcMessageQueue::entry_len> response;
    read_words(response.data(), BlackholeArcMessageQueue::entry_len, response_entry_offset);

    response_queue_rptr = (response_queue_rptr + 1) % (2 * size);
    write_words(&response_queue_rptr, 1, response_rptr_offset);

    return response;
}

uint32_t BlackholeArcMessageQueue::send_message(
    const ArcMessageType message_type, uint16_t arg0, uint16_t arg1, uint32_t timeout_ms) {
    uint32_t arg = arg0 | (arg1 << 16);

    std::array<uint32_t, BlackholeArcMessageQueue::entry_len> request = {(uint32_t)message_type, arg, 0, 0, 0, 0, 0, 0};

    push_request(request, timeout_ms);

    std::array<uint32_t, BlackholeArcMessageQueue::entry_len> response = pop_response(timeout_ms);

    uint32_t status = response[0] & 0xFF;

    // Response is packed in high 16 bits of the message.
    if (status < blackhole::ARC_MSG_RESPONSE_OK_LIMIT) {
        return response[0] >> 16;
    } else if (status == 0xFF) {
        throw std::runtime_error(fmt::format("Message code {} not recognized by ARC fw.", (uint32_t)message_type));
        return 0;
    } else {
        throw std::runtime_error(fmt::format("Uknown message error code {}", status));
        return 0;
    }
}

std::unique_ptr<BlackholeArcMessageQueue> BlackholeArcMessageQueue::get_blackhole_arc_message_queue(
    TTDevice* tt_device, const size_t queue_index) {
    const tt_xy_pair arc_core =
        tt::umd::blackhole::get_arc_core(tt_device->get_noc_translation_enabled(), umd_use_noc1);

    uint32_t queue_control_block_addr;
    tt_device->read_from_device(&queue_control_block_addr, arc_core, blackhole::SCRATCH_RAM_11, sizeof(uint32_t));

    uint64_t queue_control_block;
    tt_device->read_from_device(&queue_control_block, arc_core, queue_control_block_addr, sizeof(uint64_t));

    uint32_t queue_base_addr = queue_control_block & 0xFFFFFFFF;
    uint32_t num_entries_per_queue = (queue_control_block >> 32) & 0xFF;
    uint32_t num_queues = (queue_control_block >> 40) & 0xFF;

    uint32_t msg_queue_size = 2 * num_entries_per_queue * ARC_QUEUE_ENTRY_SIZE + ARC_MSG_QUEUE_HEADER_SIZE;
    uint32_t msg_queue_base = queue_base_addr + queue_index * msg_queue_size;

    return std::make_unique<tt::umd::BlackholeArcMessageQueue>(
        tt_device, msg_queue_base, num_entries_per_queue, arc_core);
}

}  // namespace tt::umd

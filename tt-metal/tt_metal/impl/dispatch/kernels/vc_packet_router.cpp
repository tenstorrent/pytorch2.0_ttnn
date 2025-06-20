// SPDX-FileCopyrightText: © 2023 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0

#include "dataflow_api.h"
#include "tt_metal/impl/dispatch/kernels/packet_queue.hpp"
#include "tt_metal/impl/dispatch/kernels/cq_helpers.hpp"

constexpr uint32_t rx_queue_start_addr_words = get_compile_time_arg_val(1);
constexpr uint32_t rx_queue_size_words = get_compile_time_arg_val(2);
constexpr uint32_t rx_queue_size_bytes = rx_queue_size_words * tt::packet_queue::PACKET_WORD_SIZE_BYTES;

static_assert(is_power_of_2(rx_queue_size_words), "rx_queue_size_words must be a power of 2");

constexpr uint32_t router_lanes = get_compile_time_arg_val(3);

// FIXME imatosevic - is there a way to do this without explicit indexes?
static_assert(router_lanes > 0 && router_lanes <= tt::packet_queue::MAX_SWITCH_FAN_OUT,
    "demux fan-out 0 or higher than tt::packet_queue::MAX_SWITCH_FAN_OUT");
static_assert(tt::packet_queue::MAX_SWITCH_FAN_OUT == 4,
    "tt::packet_queue::MAX_SWITCH_FAN_OUT must be 4 for the initialization below to work");

constexpr uint8_t remote_tx_x[tt::packet_queue::MAX_SWITCH_FAN_OUT] =
    {
        (get_compile_time_arg_val(4) & 0xFF),
        (get_compile_time_arg_val(5) & 0xFF),
        (get_compile_time_arg_val(6) & 0xFF),
        (get_compile_time_arg_val(7) & 0xFF)
    };

constexpr uint8_t remote_tx_y[tt::packet_queue::MAX_SWITCH_FAN_OUT] =
    {
        (get_compile_time_arg_val(4) >> 8) & 0xFF,
        (get_compile_time_arg_val(5) >> 8) & 0xFF,
        (get_compile_time_arg_val(6) >> 8) & 0xFF,
        (get_compile_time_arg_val(7) >> 8) & 0xFF
    };

constexpr uint8_t remote_tx_queue_id[tt::packet_queue::MAX_SWITCH_FAN_OUT] =
    {
        (get_compile_time_arg_val(4) >> 16) & 0xFF,
        (get_compile_time_arg_val(5) >> 16) & 0xFF,
        (get_compile_time_arg_val(6) >> 16) & 0xFF,
        (get_compile_time_arg_val(7) >> 16) & 0xFF
    };

constexpr tt::packet_queue::DispatchRemoteNetworkType remote_tx_network_type[tt::packet_queue::MAX_SWITCH_FAN_OUT] =
    {
        static_cast<tt::packet_queue::DispatchRemoteNetworkType>((get_compile_time_arg_val(4) >> 24) & 0xFF),
        static_cast<tt::packet_queue::DispatchRemoteNetworkType>((get_compile_time_arg_val(5) >> 24) & 0xFF),
        static_cast<tt::packet_queue::DispatchRemoteNetworkType>((get_compile_time_arg_val(6) >> 24) & 0xFF),
        static_cast<tt::packet_queue::DispatchRemoteNetworkType>((get_compile_time_arg_val(7) >> 24) & 0xFF)
    };

constexpr uint32_t remote_tx_queue_start_addr_words[tt::packet_queue::MAX_SWITCH_FAN_OUT] =
    {
        get_compile_time_arg_val(8),
        get_compile_time_arg_val(10),
        get_compile_time_arg_val(12),
        get_compile_time_arg_val(14)
    };

constexpr uint32_t remote_tx_queue_size_words[tt::packet_queue::MAX_SWITCH_FAN_OUT] =
    {
        get_compile_time_arg_val(9),
        get_compile_time_arg_val(11),
        get_compile_time_arg_val(13),
        get_compile_time_arg_val(15)
    };

static_assert(is_power_of_2(remote_tx_queue_size_words[0]), "remote_tx_queue_size_words must be a power of 2");
static_assert((router_lanes < 2) || is_power_of_2(remote_tx_queue_size_words[1]), "remote_tx_queue_size_words must be a power of 2");
static_assert((router_lanes < 3) || is_power_of_2(remote_tx_queue_size_words[2]), "remote_tx_queue_size_words must be a power of 2");
static_assert((router_lanes < 4) || is_power_of_2(remote_tx_queue_size_words[3]), "remote_tx_queue_size_words must be a power of 2");

constexpr uint8_t remote_rx_x[tt::packet_queue::MAX_SWITCH_FAN_OUT] =
    {
        (get_compile_time_arg_val(16) & 0xFF),
        (get_compile_time_arg_val(17) & 0xFF),
        (get_compile_time_arg_val(18) & 0xFF),
        (get_compile_time_arg_val(19) & 0xFF)
    };

constexpr uint8_t remote_rx_y[tt::packet_queue::MAX_SWITCH_FAN_OUT] =
    {
        (get_compile_time_arg_val(16) >> 8) & 0xFF,
        (get_compile_time_arg_val(17) >> 8) & 0xFF,
        (get_compile_time_arg_val(18) >> 8) & 0xFF,
        (get_compile_time_arg_val(19) >> 8) & 0xFF
    };

constexpr uint8_t remote_rx_queue_id[tt::packet_queue::MAX_SWITCH_FAN_OUT] =
    {
        (get_compile_time_arg_val(16) >> 16) & 0xFF,
        (get_compile_time_arg_val(17) >> 16) & 0xFF,
        (get_compile_time_arg_val(18) >> 16) & 0xFF,
        (get_compile_time_arg_val(19) >> 16) & 0xFF
    };

constexpr tt::packet_queue::DispatchRemoteNetworkType remote_rx_network_type[tt::packet_queue::MAX_SWITCH_FAN_OUT] =
    {
        static_cast<tt::packet_queue::DispatchRemoteNetworkType>((get_compile_time_arg_val(16) >> 24) & 0xFF),
        static_cast<tt::packet_queue::DispatchRemoteNetworkType>((get_compile_time_arg_val(17) >> 24) & 0xFF),
        static_cast<tt::packet_queue::DispatchRemoteNetworkType>((get_compile_time_arg_val(18) >> 24) & 0xFF),
        static_cast<tt::packet_queue::DispatchRemoteNetworkType>((get_compile_time_arg_val(19) >> 24) & 0xFF)
    };

constexpr uint32_t kernel_status_buf_addr_arg = get_compile_time_arg_val(22);
constexpr uint32_t kernel_status_buf_size_bytes = get_compile_time_arg_val(23);

// careful, may be null
tt_l1_ptr uint32_t* const kernel_status =
    reinterpret_cast<tt_l1_ptr uint32_t*>(kernel_status_buf_addr_arg);

constexpr uint32_t timeout_cycles = get_compile_time_arg_val(24);

constexpr bool output_depacketize[tt::packet_queue::MAX_SWITCH_FAN_OUT] =
    {
        (get_compile_time_arg_val(25) >> 0) & 0x1,
        (get_compile_time_arg_val(25) >> 1) & 0x1,
        (get_compile_time_arg_val(25) >> 2) & 0x1,
        (get_compile_time_arg_val(25) >> 3) & 0x1
    };

constexpr uint8_t output_depacketize_log_page_size[tt::packet_queue::MAX_SWITCH_FAN_OUT] =
    {
        (get_compile_time_arg_val(26) >> 0) & 0xFF,
        (get_compile_time_arg_val(27) >> 0) & 0xFF,
        (get_compile_time_arg_val(28) >> 0) & 0xFF,
        (get_compile_time_arg_val(29) >> 0) & 0xFF
    };

constexpr uint8_t output_depacketize_downstream_sem[tt::packet_queue::MAX_SWITCH_FAN_OUT] =
    {
        (get_compile_time_arg_val(26) >> 8) & 0xFF,
        (get_compile_time_arg_val(27) >> 8) & 0xFF,
        (get_compile_time_arg_val(28) >> 8) & 0xFF,
        (get_compile_time_arg_val(29) >> 8) & 0xFF
    };

constexpr uint8_t output_depacketize_local_sem[tt::packet_queue::MAX_SWITCH_FAN_OUT] =
    {
        (get_compile_time_arg_val(26) >> 16) & 0xFF,
        (get_compile_time_arg_val(27) >> 16) & 0xFF,
        (get_compile_time_arg_val(28) >> 16) & 0xFF,
        (get_compile_time_arg_val(29) >> 16) & 0xFF
    };

constexpr uint8_t output_depacketize_remove_header[tt::packet_queue::MAX_SWITCH_FAN_OUT] =
    {
        (get_compile_time_arg_val(26) >> 24) & 0x1,
        (get_compile_time_arg_val(27) >> 24) & 0x1,
        (get_compile_time_arg_val(28) >> 24) & 0x1,
        (get_compile_time_arg_val(29) >> 24) & 0x1
    };

constexpr uint8_t input_packetize[tt::packet_queue::MAX_SWITCH_FAN_IN] =
    {
        (get_compile_time_arg_val(30) >> 0) & 0x1,
        (get_compile_time_arg_val(31) >> 0) & 0x1,
        (get_compile_time_arg_val(32) >> 0) & 0x1,
        (get_compile_time_arg_val(33) >> 0) & 0x1
    };

constexpr uint8_t input_packetize_log_page_size[tt::packet_queue::MAX_SWITCH_FAN_IN] =
    {
        (get_compile_time_arg_val(30) >> 8) & 0xFF,
        (get_compile_time_arg_val(31) >> 8) & 0xFF,
        (get_compile_time_arg_val(32) >> 8) & 0xFF,
        (get_compile_time_arg_val(33) >> 8) & 0xFF
    };

constexpr uint8_t input_packetize_upstream_sem[tt::packet_queue::MAX_SWITCH_FAN_IN] =
    {
        (get_compile_time_arg_val(30) >> 16) & 0xFF,
        (get_compile_time_arg_val(31) >> 16) & 0xFF,
        (get_compile_time_arg_val(32) >> 16) & 0xFF,
        (get_compile_time_arg_val(33) >> 16) & 0xFF
    };

constexpr uint8_t input_packetize_local_sem[tt::packet_queue::MAX_SWITCH_FAN_IN] =
    {
        (get_compile_time_arg_val(30) >> 24) & 0xFF,
        (get_compile_time_arg_val(31) >> 24) & 0xFF,
        (get_compile_time_arg_val(32) >> 24) & 0xFF,
        (get_compile_time_arg_val(33) >> 24) & 0xFF
    };

constexpr uint8_t input_packetize_src_endpoint[tt::packet_queue::MAX_SWITCH_FAN_IN] =
    {
        (get_compile_time_arg_val(34) >> 0) & 0xFF,
        (get_compile_time_arg_val(34) >> 8) & 0xFF,
        (get_compile_time_arg_val(34) >> 16) & 0xFF,
        (get_compile_time_arg_val(34) >> 24) & 0xFF
    };

constexpr uint8_t input_packetize_dest_endpoint[tt::packet_queue::MAX_SWITCH_FAN_IN] =
    {
        (get_compile_time_arg_val(35) >> 0) & 0xFF,
        (get_compile_time_arg_val(35) >> 8) & 0xFF,
        (get_compile_time_arg_val(35) >> 16) & 0xFF,
        (get_compile_time_arg_val(35) >> 24) & 0xFF
    };

tt::packet_queue::packet_input_queue_state_t input_queues[tt::packet_queue::MAX_SWITCH_FAN_IN];
using input_queue_network_sequence = tt::packet_queue::NetworkTypeSequence<remote_rx_network_type[0], remote_rx_network_type[1], remote_rx_network_type[2], remote_rx_network_type[3]>;
using input_queue_cb_mode_sequence = tt::packet_queue::CBModeTypeSequence<input_packetize[0], input_packetize[1], input_packetize[2], input_packetize[3]>;

tt::packet_queue::packet_output_queue_state_t output_queues[tt::packet_queue::MAX_SWITCH_FAN_OUT];
using output_queue_network_sequence = tt::packet_queue::NetworkTypeSequence<remote_tx_network_type[0], remote_tx_network_type[1], remote_tx_network_type[2], remote_tx_network_type[3]>;
using output_queue_cb_mode_sequence = tt::packet_queue::CBModeTypeSequence<output_depacketize[0], output_depacketize[1], output_depacketize[2], output_depacketize[3]>;

void kernel_main() {
    using tt::packet_queue::PACKET_QUEUE_TEST_STARTED;
    using tt::packet_queue::PQ_TEST_STATUS_INDEX;
    using tt::packet_queue::PQ_TEST_MISC_INDEX;
    using tt::packet_queue::write_kernel_status;
    using tt::packet_queue::get_timestamp;
    using tt::packet_queue::get_timestamp_32b;
    using tt::packet_queue::set_64b_result;

    write_kernel_status(kernel_status, PQ_TEST_STATUS_INDEX, PACKET_QUEUE_TEST_STARTED);
    write_kernel_status(kernel_status, PQ_TEST_MISC_INDEX, 0xff000000);
    write_kernel_status(kernel_status, PQ_TEST_MISC_INDEX+1, 0xbb000000 | router_lanes);

    for (uint32_t i = 0; i < router_lanes; i++) {
        input_queues[i].init(i, rx_queue_start_addr_words + i*rx_queue_size_words, rx_queue_size_words,
                        remote_rx_x[i], remote_rx_y[i], remote_rx_queue_id[i], remote_rx_network_type[i],
                        input_packetize[i], input_packetize_log_page_size[i],
                        input_packetize_local_sem[i], input_packetize_upstream_sem[i],
                        input_packetize_src_endpoint[i], input_packetize_dest_endpoint[i]);

        output_queues[i].init(i + router_lanes, remote_tx_queue_start_addr_words[i], remote_tx_queue_size_words[i],
                              remote_tx_x[i], remote_tx_y[i], remote_tx_queue_id[i], remote_tx_network_type[i],
                              &input_queues[i],
                              output_depacketize[i], output_depacketize_log_page_size[i],
                              output_depacketize_local_sem[i], output_depacketize_downstream_sem[i],
                              output_depacketize_remove_header[i]);
    }

    if (!tt::packet_queue::wait_all_input_output_ready<input_queue_network_sequence,
                                     input_queue_cb_mode_sequence,
                                     output_queue_network_sequence,
                                     output_queue_cb_mode_sequence>(input_queues, output_queues, timeout_cycles)) {
        write_kernel_status(kernel_status, PQ_TEST_STATUS_INDEX, tt::packet_queue::PACKET_QUEUE_TEST_TIMEOUT);
        return;
    }

    write_kernel_status(kernel_status, PQ_TEST_MISC_INDEX, 0xff000001);

    bool timeout = false;
    bool all_outputs_finished = false;
    uint64_t data_words_sent = 0;
    uint64_t iter = 0;
    uint64_t start_timestamp = get_timestamp();
    uint32_t progress_timestamp = start_timestamp & 0xFFFFFFFF;
    uint32_t heartbeat = 0;
    while (!all_outputs_finished && !timeout) {
        IDLE_ERISC_HEARTBEAT_AND_RETURN(heartbeat);
        if constexpr (timeout_cycles > 0) {
            uint32_t cycles_since_progress = get_timestamp_32b() - progress_timestamp;
            if (cycles_since_progress > timeout_cycles) {
                timeout = true;
                break;
            }
        }

        // Loop through router lanes
        tt::packet_queue::process_queues<input_queue_network_sequence, input_queue_cb_mode_sequence>([&]<auto, auto, auto sequence_i>(auto) -> bool {
            iter++;
            if (input_queues[sequence_i].template get_curr_packet_valid<input_packetize[sequence_i]>()) {
                bool full_packet_sent;
                const auto words_sent = output_queues[sequence_i].template forward_data_from_input<remote_tx_network_type[sequence_i], output_depacketize[sequence_i], remote_rx_network_type[sequence_i], input_packetize[sequence_i]>(0, full_packet_sent, input_queues[sequence_i].get_end_of_cmd());
                if constexpr (kernel_status_buf_addr_arg) {
                    data_words_sent += words_sent;
                }
                if constexpr (timeout_cycles > 0) {
                    if (words_sent > 0) {
                        progress_timestamp = get_timestamp_32b();
                    }
                }
            }

            // Flush for all inputs of this output queue (only 1 input)
            output_queues[sequence_i].template prev_words_in_flight_check_flush<output_depacketize[sequence_i], tt::packet_queue::NetworkTypeSequence<remote_rx_network_type[sequence_i]>, tt::packet_queue::CBModeTypeSequence<input_packetize[sequence_i]>>();


            if ((iter & 0xFF) == 0) {
                all_outputs_finished = true;
                for (uint32_t i = 0; i < router_lanes; i++) {
                    all_outputs_finished &= output_queues[i].is_remote_finished();
                }
            }

            return true;
        });
    }

    if (!timeout) {
        write_kernel_status(kernel_status, PQ_TEST_MISC_INDEX, 0xff000002);
        tt::packet_queue::process_queues<output_queue_network_sequence, output_queue_cb_mode_sequence>([&]<auto network_type, auto cb_mode, auto sequence_i>(auto) -> bool {
            if (!output_queues[sequence_i].template output_barrier<cb_mode, input_queue_network_sequence, input_queue_cb_mode_sequence>(timeout_cycles)) {
                timeout = true;
            }
            return true;
        });
    }

    uint64_t cycles_elapsed = get_timestamp() - start_timestamp;
    if (!timeout) {
        write_kernel_status(kernel_status, PQ_TEST_MISC_INDEX, 0xff000003);
        tt::packet_queue::process_queues<input_queue_network_sequence, input_queue_cb_mode_sequence>([&]<auto network_type, auto cb_mode, auto sequence_i>(auto) -> bool {
            input_queues[sequence_i].template send_remote_finished_notification<network_type, cb_mode>();
            return true;
        });
    }

    set_64b_result(kernel_status, data_words_sent, tt::packet_queue::PQ_TEST_WORD_CNT_INDEX);
    set_64b_result(kernel_status, cycles_elapsed, tt::packet_queue::PQ_TEST_CYCLES_INDEX);
    set_64b_result(kernel_status, iter, tt::packet_queue::PQ_TEST_ITER_INDEX);

    if (timeout) {
        write_kernel_status(kernel_status, PQ_TEST_STATUS_INDEX, tt::packet_queue::PACKET_QUEUE_TEST_TIMEOUT);
    } else {
        write_kernel_status(kernel_status, PQ_TEST_STATUS_INDEX, tt::packet_queue::PACKET_QUEUE_TEST_PASS);
        write_kernel_status(kernel_status, PQ_TEST_MISC_INDEX, 0xff00005);
    }

    noc_async_full_barrier();
}

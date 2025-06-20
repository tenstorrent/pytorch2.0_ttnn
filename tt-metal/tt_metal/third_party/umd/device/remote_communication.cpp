/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#include "umd/device/remote_communication.h"

#include <tt-logger/tt-logger.hpp>

#include "assert.hpp"
#include "umd/device/chip/local_chip.h"
#include "umd/device/driver_atomics.h"
#include "umd/device/topology_utils.h"
#include "umd/device/umd_utils.h"
#include "umd/device/utils/lock_manager.h"

extern bool umd_use_noc1;

static constexpr uint32_t REMOTE_CMD_NOC_BIT = 9;

struct remote_update_ptr_t {
    uint32_t ptr;
    uint32_t pad[3];
};

struct routing_cmd_t {
    uint64_t sys_addr;
    uint32_t data;
    uint32_t flags;
    uint16_t rack;
    uint16_t src_resp_buf_index;
    uint32_t local_buf_index;
    uint8_t src_resp_q_id;
    uint8_t host_mem_txn_id;
    uint16_t padding;
    uint32_t src_addr_tag;  // upper 32-bits of request source address.
};

namespace tt::umd {

RemoteCommunication::RemoteCommunication(LocalChip* local_chip) : local_chip_(local_chip) {}

RemoteCommunication::~RemoteCommunication() {}

/*
 *
 *                                       NON_MMIO_MUTEX Usage
 *
 * Relevant functions:
 *  - write_to_non_mmio_device
 *  - read_from_non_mmio_device
 *
 * The non-MMIO read/write functions are responsible for the writes/reads to/from those wormhole chips that aren't
 * memory mapped or directly host connected. To get the data to or from those other chips, there is a memory
 * transfer protocol - initiated on the host side but carried out by any number of the ethernet cores on the
 * MMIO chips (e.g. typically just the one chip in a galaxy).
 *
 * There is a command queue structure in ethernet core FW to accept these read/write commands. However, there is no
 * atomic increment (from host side) for the write pointers of these queues, nor is there any sort of other hardware
 * mutual exclusion (as of WH) from host side when populating commands into the queue (as in when the host pushes a
 * write command into the ethernet core's queue).
 *
 * Therefore, any of these non_mmio commands from host side need to be synchronized so they don't accidentally corrupt
 * each other. The finest granularity possible to synchronize on would be the command slot and wrptr (per core),
 * but wrptr updates also need to be coordinated:
 *  - you can't increment wrptr unless you are writing to the next index and your write is complete
 *  - if two threads could guarantee separate command slots, they'd need to order their wrptr updates from lowest to
 *    highest and based on completion of command writes.
 *
 * Stepping back a little bit, a sort of interprocess synchronization is required because the driver may be invoked
 * from several processes. We might need to spin up multiple processes:
 *   - 1 for pushing inputs
 *   - 1 for popping outputs
 *   - 1 for managing execution state
 *  (or some variation along those lines).
 *
 * The interprocess mutex from measurements takes a while. While not seconds, it's non-trivial such that locking and
 * unlocking at fine granularity would be more detrimental to performance than acquiring it for a large block.
 *
 * Considering the above, the current chosen approach is to make each of these calls acquired a shared mutex:
 * `NON_MMIO_MUTEX_NAME`
 *  - They acquire at a relatively large granularity -> for the entire duration of the function where we interact
 *    with the ethernet core (read/write) and where we use `active_core` to choose a core.
 *    - Simplifies synchronization while we reach stability
 *  - We need to include any usage (read/modify) of `active_core` in the mutex acquisition scope.
 *
 * Other schemes may be more performant.
 */

/*
 * Note that this function is required to acquire the `NON_MMIO_MUTEX_NAME` mutex for interacting with the ethernet core
 * (host) command queue DO NOT use `active_core` or issue any pcie reads/writes to the ethernet core prior to acquiring
 * the mutex. For extra information, see the "NON_MMIO_MUTEX Usage" above
 */

void RemoteCommunication::read_non_mmio(
    eth_coord_t target_chip, tt_xy_pair target_core, void* dest, uint64_t core_src, uint32_t size_in_bytes) {
    using data_word_t = uint32_t;
    constexpr int DATA_WORD_SIZE = sizeof(data_word_t);

    // TODO: To be removed when this is moved to Chip classes.
    auto host_address_params = local_chip_->host_address_params;
    auto eth_interface_params = local_chip_->eth_interface_params;
    auto noc_params = local_chip_->noc_params;

    std::vector<std::uint32_t> erisc_command;
    std::vector<std::uint32_t> erisc_q_rptr;
    std::vector<std::uint32_t> erisc_q_ptrs =
        std::vector<uint32_t>(eth_interface_params.remote_update_ptr_size_bytes * 2 / DATA_WORD_SIZE);
    std::vector<std::uint32_t> erisc_resp_q_wptr = std::vector<uint32_t>(1);
    std::vector<std::uint32_t> erisc_resp_q_rptr = std::vector<uint32_t>(1);

    std::vector<std::uint32_t> data_block;

    routing_cmd_t* new_cmd;

    erisc_command.resize(sizeof(routing_cmd_t) / DATA_WORD_SIZE);
    new_cmd = (routing_cmd_t*)&erisc_command[0];
    //
    //                    MUTEX ACQUIRE (NON-MMIO)
    //  do not locate any ethernet core reads/writes before this acquire
    //
    auto lock = local_chip_->acquire_mutex(
        MutexType::NON_MMIO, local_chip_->get_tt_device()->get_pci_device()->get_device_num());

    const tt_xy_pair remote_transfer_ethernet_core = local_chip_->get_remote_transfer_ethernet_core();

    local_chip_->read_from_device(
        remote_transfer_ethernet_core,
        erisc_q_ptrs.data(),
        eth_interface_params.request_cmd_queue_base + eth_interface_params.cmd_counters_size_bytes,
        eth_interface_params.remote_update_ptr_size_bytes * 2);
    local_chip_->read_from_device(
        remote_transfer_ethernet_core,
        erisc_resp_q_wptr.data(),
        eth_interface_params.response_cmd_queue_base + eth_interface_params.cmd_counters_size_bytes,
        DATA_WORD_SIZE);
    local_chip_->read_from_device(
        remote_transfer_ethernet_core,
        erisc_resp_q_rptr.data(),
        eth_interface_params.response_cmd_queue_base + eth_interface_params.cmd_counters_size_bytes +
            eth_interface_params.remote_update_ptr_size_bytes,
        DATA_WORD_SIZE);

    bool full = is_non_mmio_cmd_q_full(eth_interface_params, erisc_q_ptrs[0], erisc_q_ptrs[4]);
    erisc_q_rptr.resize(1);
    erisc_q_rptr[0] = erisc_q_ptrs[4];

    bool use_dram;
    uint32_t max_block_size;

    use_dram = size_in_bytes > 1024;
    max_block_size = use_dram ? host_address_params.eth_routing_block_size : eth_interface_params.max_block_size;

    uint32_t offset = 0;
    uint32_t block_size;
    uint32_t buffer_id = 0;

    while (offset < size_in_bytes) {
        while (full) {
            local_chip_->read_from_device(
                remote_transfer_ethernet_core,
                erisc_q_rptr.data(),
                eth_interface_params.request_cmd_queue_base + eth_interface_params.cmd_counters_size_bytes +
                    eth_interface_params.remote_update_ptr_size_bytes,
                DATA_WORD_SIZE);
            full = is_non_mmio_cmd_q_full(eth_interface_params, erisc_q_ptrs[0], erisc_q_rptr[0]);
        }

        uint32_t req_wr_ptr = erisc_q_ptrs[0] & eth_interface_params.cmd_buf_size_mask;
        if ((core_src + offset) & 0x1F) {  // address not 32-byte aligned
            block_size = DATA_WORD_SIZE;   // 4 byte aligned block
        } else {
            block_size = offset + max_block_size > size_in_bytes ? size_in_bytes - offset : max_block_size;
            // Align up to 4 bytes.
            uint32_t alignment_mask = sizeof(uint32_t) - 1;
            block_size = (block_size + alignment_mask) & ~alignment_mask;
        }
        uint32_t req_flags = block_size > DATA_WORD_SIZE
                                 ? (eth_interface_params.cmd_data_block | eth_interface_params.cmd_rd_req)
                                 : eth_interface_params.cmd_rd_req;
        uint32_t resp_flags = block_size > DATA_WORD_SIZE
                                  ? (eth_interface_params.cmd_data_block | eth_interface_params.cmd_rd_data)
                                  : eth_interface_params.cmd_rd_data;
        uint32_t resp_rd_ptr = erisc_resp_q_rptr[0] & eth_interface_params.cmd_buf_size_mask;
        uint32_t host_dram_block_addr = host_address_params.eth_routing_buffers_start + resp_rd_ptr * max_block_size;
        uint16_t host_dram_channel = 0;  // This needs to be 0, since WH can only map ETH buffers to chan 0.

        if (use_dram && block_size > DATA_WORD_SIZE) {
            req_flags |= eth_interface_params.cmd_data_block_dram;
            resp_flags |= eth_interface_params.cmd_data_block_dram;
        }

        // Send the read request
        TT_ASSERT(
            (req_flags == eth_interface_params.cmd_rd_req) || (((core_src + offset) & 0x1F) == 0),
            "Block mode offset must be 32-byte aligned.");  // Block mode offset must be 32-byte aligned.
        new_cmd->sys_addr =
            get_sys_addr(noc_params, target_chip.x, target_chip.y, target_core.x, target_core.y, core_src + offset);
        new_cmd->rack = get_sys_rack(eth_interface_params, target_chip.rack, target_chip.shelf);
        new_cmd->data = block_size;
        new_cmd->flags = req_flags;
        new_cmd->flags |= (umd_use_noc1 ? 1 : 0) << REMOTE_CMD_NOC_BIT;
        if (use_dram) {
            new_cmd->src_addr_tag = host_dram_block_addr;
        }
        local_chip_->write_to_device(
            remote_transfer_ethernet_core,
            erisc_command.data(),
            eth_interface_params.request_routing_cmd_queue_base + (sizeof(routing_cmd_t) * req_wr_ptr),
            erisc_command.size() * DATA_WORD_SIZE);
        ;
        tt_driver_atomics::sfence();

        erisc_q_ptrs[0] = (erisc_q_ptrs[0] + 1) & eth_interface_params.cmd_buf_ptr_mask;
        std::vector<std::uint32_t> erisc_q_wptr;
        erisc_q_wptr.resize(1);
        erisc_q_wptr[0] = erisc_q_ptrs[0];
        local_chip_->write_to_device(
            remote_transfer_ethernet_core,
            erisc_q_wptr.data(),
            eth_interface_params.request_cmd_queue_base + eth_interface_params.cmd_counters_size_bytes,
            erisc_q_wptr.size() * DATA_WORD_SIZE);
        tt_driver_atomics::sfence();
        // If there is more data to read and this command will make the q full, set full to 1.
        // otherwise full stays false so that we do not poll the rd pointer in next iteration.
        // As long as current command push does not fill up the queue completely, we do not want
        // to poll rd pointer in every iteration.

        if (is_non_mmio_cmd_q_full(eth_interface_params, (erisc_q_ptrs[0]), erisc_q_rptr[0])) {
            local_chip_->read_from_device(
                remote_transfer_ethernet_core,
                erisc_q_ptrs.data(),
                eth_interface_params.request_cmd_queue_base + eth_interface_params.cmd_counters_size_bytes,
                eth_interface_params.remote_update_ptr_size_bytes * 2);
            full = is_non_mmio_cmd_q_full(eth_interface_params, erisc_q_ptrs[0], erisc_q_ptrs[4]);
            erisc_q_rptr[0] = erisc_q_ptrs[4];
        }

        // Wait for read request completion and extract the data into the `dest`

        // erisc firmware will:
        // 1. clear response flags
        // 2. start operation
        // 3. advance response wrptr
        // 4. complete operation and write data into response or buffer
        // 5. set response flags
        // So we have to wait for wrptr to advance, then wait for flags to be nonzero, then read data.

        do {
            local_chip_->read_from_device(
                remote_transfer_ethernet_core,
                erisc_resp_q_wptr.data(),
                eth_interface_params.response_cmd_queue_base + eth_interface_params.cmd_counters_size_bytes,
                DATA_WORD_SIZE);
        } while (erisc_resp_q_rptr[0] == erisc_resp_q_wptr[0]);
        tt_driver_atomics::lfence();
        uint32_t flags_offset = 12 + sizeof(routing_cmd_t) * resp_rd_ptr;
        std::vector<std::uint32_t> erisc_resp_flags = std::vector<uint32_t>(1);
        do {
            local_chip_->read_from_device(
                remote_transfer_ethernet_core,
                erisc_resp_flags.data(),
                eth_interface_params.response_routing_cmd_queue_base + flags_offset,
                DATA_WORD_SIZE);
        } while (erisc_resp_flags[0] == 0);

        if (erisc_resp_flags[0] == resp_flags) {
            tt_driver_atomics::lfence();
            uint32_t data_offset = 8 + sizeof(routing_cmd_t) * resp_rd_ptr;
            if (block_size == DATA_WORD_SIZE) {
                std::vector<std::uint32_t> erisc_resp_data = std::vector<uint32_t>(1);
                local_chip_->read_from_device(
                    remote_transfer_ethernet_core,
                    erisc_resp_data.data(),
                    eth_interface_params.response_routing_cmd_queue_base + data_offset,
                    DATA_WORD_SIZE);
                if (size_in_bytes - offset < 4) {
                    // Handle misaligned (4 bytes) data at the end of the block.
                    // Only read remaining bytes into the host buffer, instead of reading the full uint32_t
                    std::memcpy((uint8_t*)dest + offset, erisc_resp_data.data(), size_in_bytes - offset);
                } else {
                    *((uint32_t*)dest + offset / DATA_WORD_SIZE) = erisc_resp_data[0];
                }
            } else {
                // Read 4 byte aligned block from device/sysmem
                if (use_dram) {
                    size_buffer_to_capacity(data_block, block_size);
                    local_chip_->read_from_sysmem(
                        host_dram_channel, data_block.data(), host_dram_block_addr, block_size);
                } else {
                    uint32_t buf_address =
                        eth_interface_params.eth_routing_data_buffer_addr + resp_rd_ptr * max_block_size;
                    size_buffer_to_capacity(data_block, block_size);
                    local_chip_->read_from_device(
                        remote_transfer_ethernet_core, data_block.data(), buf_address, block_size);
                }
                // assert(dest.size() - (offset/DATA_WORD_SIZE) >= (block_size * DATA_WORD_SIZE));
                TT_ASSERT(
                    (data_block.size() * DATA_WORD_SIZE) >= block_size,
                    "Incorrect data size read back from sysmem/device");
                // Account for misalignment by skipping any padding bytes in the copied data_block
                memcpy((uint8_t*)dest + offset, data_block.data(), std::min(block_size, size_in_bytes - offset));
            }
        }

        // Finally increment the rdptr for the response command q
        erisc_resp_q_rptr[0] = (erisc_resp_q_rptr[0] + 1) & eth_interface_params.cmd_buf_ptr_mask;
        local_chip_->write_to_device(
            remote_transfer_ethernet_core,
            erisc_resp_q_rptr.data(),
            eth_interface_params.response_cmd_queue_base + sizeof(remote_update_ptr_t) +
                eth_interface_params.cmd_counters_size_bytes,
            erisc_resp_q_rptr.size() * DATA_WORD_SIZE);
        tt_driver_atomics::sfence();
        TT_ASSERT(erisc_resp_flags[0] == resp_flags, "Unexpected ERISC Response Flags.");

        offset += block_size;
    }
}

/*
 * Note that this function is required to acquire the `NON_MMIO_MUTEX_NAME` mutex for interacting with the
 * ethernet core (host) command queue DO NOT issue any pcie reads/writes to the ethernet core prior to acquiring the
 * mutex. For extra information, see the "NON_MMIO_MUTEX Usage" above
 */

void RemoteCommunication::write_to_non_mmio(
    eth_coord_t target_chip,
    tt_xy_pair target_core,
    const void* src,
    uint64_t core_dest,
    uint32_t size_in_bytes,
    bool broadcast,
    std::vector<int> broadcast_header) {
    local_chip_->set_flush_non_mmio(true);

    using data_word_t = uint32_t;
    constexpr int DATA_WORD_SIZE = sizeof(data_word_t);
    constexpr int BROADCAST_HEADER_SIZE = sizeof(data_word_t) * 8;  // Broadcast header is 8 words

    // TODO: To be removed when this is moved to Chip classes.
    auto host_address_params = local_chip_->host_address_params;
    auto eth_interface_params = local_chip_->eth_interface_params;
    auto noc_params = local_chip_->noc_params;

    std::vector<std::uint32_t> erisc_command;
    std::vector<std::uint32_t> erisc_q_rptr = std::vector<uint32_t>(1);
    std::vector<std::uint32_t> erisc_q_ptrs =
        std::vector<uint32_t>(eth_interface_params.remote_update_ptr_size_bytes * 2 / sizeof(uint32_t));

    std::vector<std::uint32_t> data_block;

    routing_cmd_t* new_cmd;

    uint32_t buffer_id = 0;
    uint32_t timestamp = 0;  // CMD_TIMESTAMP;
    bool use_dram;
    uint32_t max_block_size;

    // Broadcast requires block writes to host dram
    use_dram = broadcast || (size_in_bytes > 256 * DATA_WORD_SIZE);
    max_block_size = use_dram ? host_address_params.eth_routing_block_size : eth_interface_params.max_block_size;

    //
    //                    MUTEX ACQUIRE (NON-MMIO)
    //  do not locate any ethernet core reads/writes before this acquire
    //
    auto lock = local_chip_->acquire_mutex(
        MutexType::NON_MMIO, local_chip_->get_tt_device()->get_pci_device()->get_device_num());

    tt_xy_pair remote_transfer_ethernet_core = local_chip_->get_remote_transfer_ethernet_core();

    erisc_command.resize(sizeof(routing_cmd_t) / DATA_WORD_SIZE);
    new_cmd = (routing_cmd_t*)&erisc_command[0];
    local_chip_->read_from_device(
        remote_transfer_ethernet_core,
        erisc_q_ptrs.data(),
        eth_interface_params.request_cmd_queue_base + eth_interface_params.cmd_counters_size_bytes,
        eth_interface_params.remote_update_ptr_size_bytes * 2);
    uint32_t offset = 0;
    uint32_t block_size;

    bool full = is_non_mmio_cmd_q_full(eth_interface_params, erisc_q_ptrs[0], erisc_q_ptrs[4]);
    erisc_q_rptr.resize(1);
    erisc_q_rptr[0] = erisc_q_ptrs[4];
    while (offset < size_in_bytes) {
        while (full) {
            local_chip_->read_from_device(
                remote_transfer_ethernet_core,
                erisc_q_rptr.data(),
                eth_interface_params.request_cmd_queue_base + eth_interface_params.cmd_counters_size_bytes +
                    eth_interface_params.remote_update_ptr_size_bytes,
                DATA_WORD_SIZE);
            full = is_non_mmio_cmd_q_full(eth_interface_params, erisc_q_ptrs[0], erisc_q_rptr[0]);
        }
        // full = true;
        //  set full only if this command will make the q full.
        //  otherwise full stays false so that we do not poll the rd pointer in next iteration.
        //  As long as current command push does not fill up the queue completely, we do not want
        //  to poll rd pointer in every iteration.
        // full = is_non_mmio_cmd_q_full((erisc_q_ptrs[0] + 1) & CMD_BUF_PTR_MASK, erisc_q_rptr[0]);

        uint32_t req_wr_ptr = erisc_q_ptrs[0] & eth_interface_params.cmd_buf_size_mask;
        if ((core_dest + offset) & 0x1F) {  // address not 32-byte aligned
            block_size = DATA_WORD_SIZE;    // 4 byte aligned
        } else {
            // For broadcast we prepend a 32byte header. Decrease block size (size of payload) by this amount.
            block_size = offset + max_block_size > size_in_bytes + 32 * broadcast ? size_in_bytes - offset
                                                                                  : max_block_size - 32 * broadcast;
            // Explictly align block_size to 4 bytes, in case the input buffer is not uint32_t aligned
            uint32_t alignment_mask = sizeof(uint32_t) - 1;
            block_size = (block_size + alignment_mask) & ~alignment_mask;
        }
        // For 4 byte aligned data, transfer_size always == block_size. For unaligned data, transfer_size < block_size
        // in the last block
        uint64_t transfer_size =
            std::min(block_size, size_in_bytes - offset);  // Host side data size that needs to be copied
        // Use block mode for broadcast
        uint32_t req_flags = (broadcast || (block_size > DATA_WORD_SIZE))
                                 ? (eth_interface_params.cmd_data_block | eth_interface_params.cmd_wr_req | timestamp)
                                 : eth_interface_params.cmd_wr_req;
        uint32_t resp_flags = block_size > DATA_WORD_SIZE
                                  ? (eth_interface_params.cmd_data_block | eth_interface_params.cmd_wr_ack)
                                  : eth_interface_params.cmd_wr_ack;
        timestamp = 0;

        if (broadcast) {
            req_flags |= eth_interface_params.cmd_broadcast;
        }

        uint32_t host_dram_block_addr =
            host_address_params.eth_routing_buffers_start +
            (local_chip_->get_active_eth_core_idx() * eth_interface_params.cmd_buf_size + req_wr_ptr) * max_block_size;
        uint16_t host_dram_channel = 0;  // This needs to be 0, since WH can only map ETH buffers to chan 0.

        if (req_flags & eth_interface_params.cmd_data_block) {
            // Copy data to sysmem or device DRAM for Block mode
            if (use_dram) {
                req_flags |= eth_interface_params.cmd_data_block_dram;
                resp_flags |= eth_interface_params.cmd_data_block_dram;
                size_buffer_to_capacity(data_block, block_size);
                memcpy(&data_block[0], (uint8_t*)src + offset, transfer_size);
                if (broadcast) {
                    // Write broadcast header to sysmem
                    local_chip_->write_to_sysmem(
                        host_dram_channel,
                        broadcast_header.data(),
                        host_dram_block_addr,
                        broadcast_header.size() * sizeof(uint32_t));
                }
                // Write payload to sysmem
                local_chip_->write_to_sysmem(
                    host_dram_channel,
                    data_block.data(),
                    host_dram_block_addr + BROADCAST_HEADER_SIZE * broadcast,
                    data_block.size() * DATA_WORD_SIZE);

            } else {
                uint32_t buf_address = eth_interface_params.eth_routing_data_buffer_addr + req_wr_ptr * max_block_size;
                size_buffer_to_capacity(data_block, block_size);
                memcpy(&data_block[0], (uint8_t*)src + offset, transfer_size);
                local_chip_->write_to_device(
                    remote_transfer_ethernet_core, data_block.data(), buf_address, data_block.size() * DATA_WORD_SIZE);
            }
            tt_driver_atomics::sfence();
        }

        // Send the read request
        TT_ASSERT(
            broadcast || (req_flags == eth_interface_params.cmd_wr_req) || (((core_dest + offset) % 32) == 0),
            "Block mode address must be 32-byte aligned.");  // Block mode address must be 32-byte aligned.

        if (broadcast) {
            // Only specify endpoint local address for broadcast
            new_cmd->sys_addr = core_dest + offset;
        } else {
            new_cmd->sys_addr = get_sys_addr(
                noc_params, target_chip.x, target_chip.y, target_core.x, target_core.y, core_dest + offset);
            new_cmd->rack = get_sys_rack(eth_interface_params, target_chip.rack, target_chip.shelf);
        }

        if (req_flags & eth_interface_params.cmd_data_block) {
            // Block mode
            new_cmd->data = block_size + BROADCAST_HEADER_SIZE * broadcast;
        } else {
            if (size_in_bytes - offset < sizeof(uint32_t)) {
                // Handle misalignment at the end of the buffer:
                // Assemble a padded uint32_t from single bytes, in case we have less than 4 bytes remaining
                memcpy(&new_cmd->data, static_cast<const uint8_t*>(src) + offset, size_in_bytes - offset);
            } else {
                new_cmd->data = *((uint32_t*)src + offset / DATA_WORD_SIZE);
            }
        }

        new_cmd->flags = req_flags;
        new_cmd->flags |= (umd_use_noc1 ? 1 : 0) << REMOTE_CMD_NOC_BIT;
        if (use_dram) {
            new_cmd->src_addr_tag = host_dram_block_addr;
        }
        local_chip_->write_to_device(
            remote_transfer_ethernet_core,
            erisc_command.data(),
            eth_interface_params.request_routing_cmd_queue_base + (sizeof(routing_cmd_t) * req_wr_ptr),
            erisc_command.size() * DATA_WORD_SIZE);
        tt_driver_atomics::sfence();

        erisc_q_ptrs[0] = (erisc_q_ptrs[0] + 1) & eth_interface_params.cmd_buf_ptr_mask;
        std::vector<std::uint32_t> erisc_q_wptr;
        erisc_q_wptr.resize(1);
        erisc_q_wptr[0] = erisc_q_ptrs[0];
        local_chip_->write_to_device(
            remote_transfer_ethernet_core,
            erisc_q_wptr.data(),
            eth_interface_params.request_cmd_queue_base + eth_interface_params.cmd_counters_size_bytes,
            erisc_q_wptr.size() * DATA_WORD_SIZE);
        tt_driver_atomics::sfence();

        offset += transfer_size;

        // If there is more data to send and this command will make the q full, switch to next Q.
        // otherwise full stays false so that we do not poll the rd pointer in next iteration.
        // As long as current command push does not fill up the queue completely, we do not want
        // to poll rd pointer in every iteration.

        if (is_non_mmio_cmd_q_full(
                eth_interface_params, (erisc_q_ptrs[0]) & eth_interface_params.cmd_buf_ptr_mask, erisc_q_rptr[0])) {
            local_chip_->update_active_eth_core_idx();
            remote_transfer_ethernet_core = local_chip_->get_remote_transfer_ethernet_core();
            local_chip_->read_from_device(
                remote_transfer_ethernet_core,
                erisc_q_ptrs.data(),
                eth_interface_params.request_cmd_queue_base + eth_interface_params.cmd_counters_size_bytes,
                eth_interface_params.remote_update_ptr_size_bytes * 2);
            full = is_non_mmio_cmd_q_full(eth_interface_params, erisc_q_ptrs[0], erisc_q_ptrs[4]);
            erisc_q_rptr[0] = erisc_q_ptrs[4];
        }
    }
}

void RemoteCommunication::wait_for_non_mmio_flush() {
    if (local_chip_->get_flush_non_mmio()) {
        TT_ASSERT(
            local_chip_->get_soc_descriptor().arch != tt::ARCH::BLACKHOLE, "Non-MMIO flush not supported in Blackhole");

        if (local_chip_->get_soc_descriptor().arch == tt::ARCH::WORMHOLE_B0) {
            // TODO: To be removed when this is moved to Chip classes.
            auto eth_interface_params = local_chip_->eth_interface_params;

            std::vector<std::uint32_t> erisc_txn_counters = std::vector<uint32_t>(2);
            std::vector<std::uint32_t> erisc_q_ptrs =
                std::vector<uint32_t>(eth_interface_params.remote_update_ptr_size_bytes * 2 / sizeof(uint32_t));

            // wait for all queues to be empty.
            for (tt_xy_pair& xy : local_chip_->get_remote_transfer_ethernet_cores()) {
                do {
                    local_chip_->read_from_device(
                        xy,
                        erisc_q_ptrs.data(),
                        eth_interface_params.request_cmd_queue_base + eth_interface_params.cmd_counters_size_bytes,
                        eth_interface_params.remote_update_ptr_size_bytes * 2);
                } while (erisc_q_ptrs[0] != erisc_q_ptrs[4]);
            }
            // wait for all write responses to come back.
            for (tt_xy_pair& xy : local_chip_->get_remote_transfer_ethernet_cores()) {
                do {
                    local_chip_->read_from_device(
                        xy, erisc_txn_counters.data(), eth_interface_params.request_cmd_queue_base, 8);
                } while (erisc_txn_counters[0] != erisc_txn_counters[1]);
            }
        }
        local_chip_->set_flush_non_mmio(false);
    }
}

int RemoteCommunication::arc_msg(
    eth_coord_t target_chip,
    tt_xy_pair remote_arc_core,
    uint32_t msg_code,
    bool wait_for_done,
    uint32_t arg0,
    uint32_t arg1,
    uint32_t timeout_ms,
    uint32_t* return_3,
    uint32_t* return_4) {
    constexpr uint64_t ARC_RESET_SCRATCH_ADDR = 0x880030060;
    constexpr uint64_t ARC_RESET_MISC_CNTL_ADDR = 0x880030100;

    // Remote arc has to be locked under critical section, only one remote arc message can be processed at the moment
    auto lock = local_chip_->acquire_mutex(
        MutexType::REMOTE_ARC_MSG, local_chip_->get_tt_device()->get_pci_device()->get_device_num());

    if ((msg_code & 0xff00) != 0xaa00) {
        log_error(LogSiliconDriver, "Malformed message. msg_code is 0x{:x} but should be 0xaa..", msg_code);
    }
    TT_ASSERT(arg0 <= 0xffff and arg1 <= 0xffff, "Only 16 bits allowed in arc_msg args");  // Only 16 bits are allowed

    uint32_t fw_arg = arg0 | (arg1 << 16);
    int exit_code = 0;

    { write_to_non_mmio(target_chip, remote_arc_core, &fw_arg, ARC_RESET_SCRATCH_ADDR + 3 * 4, sizeof(fw_arg)); }

    { write_to_non_mmio(target_chip, remote_arc_core, &msg_code, ARC_RESET_SCRATCH_ADDR + 5 * 4, sizeof(fw_arg)); }

    wait_for_non_mmio_flush();
    uint32_t misc = 0;

    read_non_mmio(target_chip, remote_arc_core, &misc, ARC_RESET_MISC_CNTL_ADDR, 4);

    if (misc & (1 << 16)) {
        log_error(LogSiliconDriver, "trigger_fw_int failed on device");
        return 1;
    } else {
        misc |= (1 << 16);
        write_to_non_mmio(target_chip, remote_arc_core, &misc, ARC_RESET_MISC_CNTL_ADDR, sizeof(misc));
    }

    if (wait_for_done) {
        uint32_t status = 0xbadbad;
        auto start = std::chrono::steady_clock::now();
        while (true) {
            auto now = std::chrono::steady_clock::now();
            auto elapsed_ms = std::chrono::duration_cast<std::chrono::milliseconds>(now - start).count();
            if (elapsed_ms > timeout_ms && timeout_ms != 0) {
                std::stringstream ss;
                ss << std::hex << msg_code;
                throw std::runtime_error(fmt::format(
                    "Timed out after waiting {} ms for device ARC to respond to message 0x{}", timeout_ms, ss.str()));
            }

            uint32_t status = 0;
            read_non_mmio(target_chip, remote_arc_core, &status, ARC_RESET_SCRATCH_ADDR + 5 * 4, sizeof(status));
            if ((status & 0xffff) == (msg_code & 0xff)) {
                if (return_3 != nullptr) {
                    read_non_mmio(
                        target_chip, remote_arc_core, return_3, ARC_RESET_SCRATCH_ADDR + 3 * 4, sizeof(uint32_t));
                }

                if (return_4 != nullptr) {
                    read_non_mmio(
                        target_chip, remote_arc_core, return_4, ARC_RESET_SCRATCH_ADDR + 4 * 4, sizeof(uint32_t));
                }

                exit_code = (status & 0xffff0000) >> 16;
                break;
            } else if (status == HANG_READ_VALUE) {
                log_warning(LogSiliconDriver, "Message code 0x{:x} not recognized by FW", msg_code);
                exit_code = HANG_READ_VALUE;
                break;
            }
        }
    }
    return exit_code;
}

}  // namespace tt::umd

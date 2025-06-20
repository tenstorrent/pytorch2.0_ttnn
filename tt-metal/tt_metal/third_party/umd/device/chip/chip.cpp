/*
 * SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include "umd/device/chip/chip.h"

#include "assert.hpp"
#include "umd/device/architecture_implementation.h"
#include "umd/device/driver_atomics.h"
#include "umd/device/wormhole_implementation.h"

namespace tt::umd {

Chip::Chip(tt_SocDescriptor soc_descriptor) : soc_descriptor_(soc_descriptor) {
    set_default_params(soc_descriptor.arch);
}

Chip::Chip(const ChipInfo chip_info, tt_SocDescriptor soc_descriptor) :
    chip_info_(chip_info), soc_descriptor_(soc_descriptor) {
    set_default_params(soc_descriptor.arch);
}

tt_SocDescriptor& Chip::get_soc_descriptor() { return soc_descriptor_; }

// TODO: This will be moved to LocalChip.
void Chip::set_default_params(ARCH arch) {
    auto architecture_implementation = tt::umd::architecture_implementation::create(arch);

    // Default initialize l1_address_params based on detected arch
    l1_address_params = architecture_implementation->get_l1_address_params();

    // Default initialize dram_address_params.
    dram_address_params = {0u};

    // Default initialize host_address_params based on detected arch
    host_address_params = architecture_implementation->get_host_address_params();

    // Default initialize eth_interface_params based on detected arch
    eth_interface_params = architecture_implementation->get_eth_interface_params();

    // Default initialize noc_params based on detected arch
    noc_params = architecture_implementation->get_noc_params();
}

void Chip::set_barrier_address_params(const barrier_address_params& barrier_address_params_) {
    l1_address_params.tensix_l1_barrier_base = barrier_address_params_.tensix_l1_barrier_base;
    l1_address_params.eth_l1_barrier_base = barrier_address_params_.eth_l1_barrier_base;
    dram_address_params.DRAM_BARRIER_BASE = barrier_address_params_.dram_barrier_base;
}

const ChipInfo& Chip::get_chip_info() { return chip_info_; }

void Chip::wait_chip_to_be_ready() {
    wait_eth_cores_training();
    wait_dram_cores_training();
}

void Chip::wait_eth_cores_training(const uint32_t timeout_ms) {}

TTDevice* Chip::get_tt_device() { return tt_device_.get(); }

SysmemManager* Chip::get_sysmem_manager() {
    throw std::runtime_error(
        "Chip::get_sysmem_manager is not available for this chip, it is only available for LocalChips.");
}

TLBManager* Chip::get_tlb_manager() {
    throw std::runtime_error(
        "Chip::get_tlb_manager is not available for this chip, it is only available for LocalChips.");
}

int Chip::get_num_host_channels() { return 0; }

int Chip::get_host_channel_size(std::uint32_t channel) {
    throw std::runtime_error("There are no host channels available.");
}

void Chip::write_to_sysmem(uint16_t channel, const void* src, uint64_t sysmem_dest, uint32_t size) {
    throw std::runtime_error("Chip::write_to_sysmem is not available for this chip.");
}

void Chip::read_from_sysmem(uint16_t channel, void* dest, uint64_t sysmem_src, uint32_t size) {
    throw std::runtime_error("Chip::read_from_sysmem is not available for this chip.");
}

void Chip::write_to_device_reg(tt_xy_pair core, const void* src, uint64_t reg_dest, uint32_t size) {
    write_to_device(core, src, reg_dest, size);
}

void Chip::read_from_device_reg(tt_xy_pair core, void* dest, uint64_t reg_src, uint32_t size) {
    read_from_device(core, dest, reg_src, size);
}

void Chip::dma_write_to_device(const void* src, size_t size, tt_xy_pair core, uint64_t addr) {
    throw std::runtime_error("Chip::dma_write_to_device is not available for this chip.");
}

void Chip::dma_read_from_device(void* dst, size_t size, tt_xy_pair core, uint64_t addr) {
    throw std::runtime_error("Chip::dma_read_from_device is not available for this chip.");
}

std::function<void(uint32_t, uint32_t, const uint8_t*)> Chip::get_fast_pcie_static_tlb_write_callable() {
    throw std::runtime_error("Chip::get_fast_pcie_static_tlb_write_callable is not available for this chip.");
}

void Chip::wait_for_non_mmio_flush() {
    throw std::runtime_error("Chip::wait_for_non_mmio_flush is not available for this chip.");
}

void Chip::set_remote_transfer_ethernet_cores(const std::unordered_set<CoreCoord>& cores) {
    throw std::runtime_error("Chip::set_remote_transfer_ethernet_cores is not available for this chip.");
}

void Chip::set_remote_transfer_ethernet_cores(const std::set<uint32_t>& channel) {
    throw std::runtime_error("Chip::set_remote_transfer_ethernet_cores is not available for this chip.");
}

int Chip::get_numa_node() { throw std::runtime_error("Chip::get_numa_node is not available for this chip."); }

void Chip::wait_dram_cores_training(const uint32_t timeout_ms) {}

void Chip::enable_ethernet_queue(int timeout_s) {
    TT_ASSERT(
        soc_descriptor_.arch != tt::ARCH::BLACKHOLE,
        "enable_ethernet_queue is not supported on Blackhole architecture");
    uint32_t msg_success = 0x0;
    auto timeout_seconds = std::chrono::seconds(timeout_s);
    auto start = std::chrono::system_clock::now();
    while (msg_success != 1) {
        if (std::chrono::system_clock::now() - start > timeout_seconds) {
            throw std::runtime_error(
                fmt::format("Timed out after waiting {} seconds for for DRAM to finish training", timeout_s));
        }
        if (arc_msg(0xaa58, true, 0xFFFF, 0xFFFF, 1000, &msg_success) == HANG_READ_VALUE) {
            break;
        }
    }
}

void Chip::send_tensix_risc_reset(tt_xy_pair core, const TensixSoftResetOptions& soft_resets) {
    auto valid = soft_resets & ALL_TENSIX_SOFT_RESET;
    uint32_t valid_val = (std::underlying_type<TensixSoftResetOptions>::type)valid;
    write_to_device_reg(core, &valid_val, 0xFFB121B0, sizeof(uint32_t));
    tt_driver_atomics::sfence();
}

void Chip::send_tensix_risc_reset(const TensixSoftResetOptions& soft_resets) {
    for (const CoreCoord core : soc_descriptor_.get_cores(CoreType::TENSIX, CoordSystem::VIRTUAL)) {
        send_tensix_risc_reset(core, soft_resets);
    }
}

uint32_t Chip::get_power_state_arc_msg(tt_DevicePowerState state) {
    uint32_t msg = wormhole::ARC_MSG_COMMON_PREFIX;
    switch (state) {
        case BUSY: {
            msg |= architecture_implementation::create(soc_descriptor_.arch)->get_arc_message_arc_go_busy();
            break;
        }
        case LONG_IDLE: {
            msg |= architecture_implementation::create(soc_descriptor_.arch)->get_arc_message_arc_go_long_idle();
            break;
        }
        case SHORT_IDLE: {
            msg |= architecture_implementation::create(soc_descriptor_.arch)->get_arc_message_arc_go_short_idle();
            break;
        }
        default:
            throw std::runtime_error("Unrecognized power state.");
    }
    return msg;
}

int Chip::arc_msg(
    uint32_t msg_code,
    bool wait_for_done,
    uint32_t arg0,
    uint32_t arg1,
    uint32_t timeout_ms,
    uint32_t* return_3,
    uint32_t* return_4) {
    std::vector<uint32_t> arc_msg_return_values;
    if (return_3 != nullptr) {
        arc_msg_return_values.push_back(0);
    }

    if (return_4 != nullptr) {
        arc_msg_return_values.push_back(0);
    }

    uint32_t exit_code =
        get_tt_device()->get_arc_messenger()->send_message(msg_code, arc_msg_return_values, arg0, arg1, timeout_ms);

    if (return_3 != nullptr) {
        *return_3 = arc_msg_return_values[0];
    }

    if (return_4 != nullptr) {
        *return_4 = arc_msg_return_values[1];
    }

    return exit_code;
}

}  // namespace tt::umd

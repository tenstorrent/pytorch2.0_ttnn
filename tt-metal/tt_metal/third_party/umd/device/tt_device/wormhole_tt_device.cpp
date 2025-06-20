// SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0
#include "umd/device/tt_device/wormhole_tt_device.h"

#include <tt-logger/tt-logger.hpp>

#include "umd/device/types/wormhole_dram.h"
#include "umd/device/types/wormhole_telemetry.h"
#include "umd/device/wormhole_implementation.h"

static constexpr uint32_t DMA_COMPLETION_VALUE = 0xfaca;
static constexpr uint32_t DMA_TIMEOUT_MS = 10000;  // 10 seconds

extern bool umd_use_noc1;

namespace tt::umd {

WormholeTTDevice::WormholeTTDevice(std::shared_ptr<PCIDevice> pci_device) :
    TTDevice(pci_device, std::make_unique<wormhole_implementation>()) {
    init_tt_device();
    wait_arc_core_start(
        umd_use_noc1 ? tt_xy_pair(
                           tt::umd::wormhole::NOC0_X_TO_NOC1_X[tt::umd::wormhole::ARC_CORES_NOC0[0].x],
                           tt::umd::wormhole::NOC0_Y_TO_NOC1_Y[tt::umd::wormhole::ARC_CORES_NOC0[0].y])
                     : wormhole::ARC_CORES_NOC0[0],
        1000);
}

bool WormholeTTDevice::get_noc_translation_enabled() {
    uint32_t niu_cfg;
    // We read information about NOC translation from DRAM core just be on paar with Luwen implementation.
    // We use DRAM core (0, 0) to read this information, but it can be read from any core.
    // TODO: read this information from PCIE BAR.
    const tt_xy_pair dram_core =
        umd_use_noc1 ? tt_xy_pair(tt::umd::wormhole::NOC0_X_TO_NOC1_X[0], tt::umd::wormhole::NOC0_Y_TO_NOC1_Y[0])
                     : tt_xy_pair(0, 0);
    const uint64_t niu_cfg_addr = 0x1000A0000 + 0x100;
    read_from_device(&niu_cfg, dram_core, niu_cfg_addr, sizeof(uint32_t));

    return (niu_cfg & (1 << 14)) != 0;
}

ChipInfo WormholeTTDevice::get_chip_info() {
    ChipInfo chip_info;
    chip_info.noc_translation_enabled = get_noc_translation_enabled();

    std::vector<uint32_t> arc_msg_return_values = {0};
    const uint32_t timeout_ms = 1000;
    uint32_t ret_code = get_arc_messenger()->send_message(
        tt::umd::wormhole::ARC_MSG_COMMON_PREFIX |
            get_architecture_implementation()->get_arc_message_arc_get_harvesting(),
        arc_msg_return_values,
        0,
        0,
        timeout_ms);

    if (ret_code != 0) {
        throw std::runtime_error(fmt::format("Failed to get harvesting masks with exit code {}", ret_code));
    }

    chip_info.harvesting_masks.tensix_harvesting_mask = arc_msg_return_values[0];

    chip_info.chip_uid.board_id = get_board_id();

    chip_info.board_type = get_board_type();

    return chip_info;
}

void WormholeTTDevice::wait_arc_core_start(const tt_xy_pair arc_core, const uint32_t timeout_ms) {
    uint32_t bar_read_initial = bar_read32(architecture_impl_->get_arc_reset_scratch_offset() + 3 * 4);
    // TODO: figure out 325 and 500 constants meaning and put it in variable.
    uint32_t arg = bar_read_initial == 500 ? 325 : 500;
    uint32_t bar_read_again;
    std::vector<uint32_t> ret_vals(1);
    uint32_t arc_msg_return = get_arc_messenger()->send_message(
        wormhole::ARC_MSG_COMMON_PREFIX | architecture_impl_->get_arc_message_test(), ret_vals, arg, 0, timeout_ms);
    bar_read_again = ret_vals[0];
    if (arc_msg_return != 0 || bar_read_again != arg + 1) {
        auto postcode = bar_read32(architecture_impl_->get_arc_reset_scratch_offset());
        throw std::runtime_error(fmt::format(
            "Device is not initialized: arc_fw postcode: {} arc_msg_return: {} arg: {} bar_read_initial: {} "
            "bar_read_again: {}",
            postcode,
            arc_msg_return,
            arg,
            bar_read_initial,
            bar_read_again));
    }
}

uint32_t WormholeTTDevice::get_clock() {
    const uint32_t timeouts_ms = 1000;
    // There is one return value from AICLK ARC message.
    std::vector<uint32_t> arc_msg_return_values = {0};
    auto exit_code = get_arc_messenger()->send_message(
        tt::umd::wormhole::ARC_MSG_COMMON_PREFIX | get_architecture_implementation()->get_arc_message_get_aiclk(),
        arc_msg_return_values,
        0xFFFF,
        0xFFFF,
        timeouts_ms);
    if (exit_code != 0) {
        throw std::runtime_error(fmt::format("Failed to get AICLK value with exit code {}", exit_code));
    }
    return arc_msg_return_values[0];
}

uint32_t WormholeTTDevice::get_max_clock_freq() {
    uint32_t aiclk_telemetry = telemetry->read_entry(tt::umd::wormhole::TAG_AICLK);
    return (aiclk_telemetry >> 16) & 0xFFFF;
}

uint32_t WormholeTTDevice::get_min_clock_freq() { return tt::umd::wormhole::AICLK_IDLE_VAL; }

uint64_t WormholeTTDevice::get_board_id() {
    uint32_t board_id_lo = telemetry->read_entry(tt::umd::wormhole::TAG_BOARD_ID_LOW);
    uint32_t board_id_hi = telemetry->read_entry(tt::umd::wormhole::TAG_BOARD_ID_HIGH);
    return ((uint64_t)board_id_hi << 32) | board_id_lo;
}

std::vector<DramTrainingStatus> WormholeTTDevice::get_dram_training_status() {
    uint32_t dram_training_status_telemetry = telemetry->read_entry(tt::umd::wormhole::TAG_DDR_STATUS);
    const uint32_t num_dram_channels = tt::umd::wormhole::NUM_DRAM_BANKS;
    std::vector<DramTrainingStatus> dram_training_status;
    for (uint32_t dram_channel = 0; dram_channel < num_dram_channels; dram_channel++) {
        uint8_t status = (dram_training_status_telemetry >> (dram_channel * 4)) & 0xF;

        switch (status) {
            case wormhole::WormholeDramTrainingStatus::TrainingNone:
                dram_training_status.push_back(DramTrainingStatus::IN_PROGRESS);
                break;
            case wormhole::WormholeDramTrainingStatus::TrainingFail:
                dram_training_status.push_back(DramTrainingStatus::FAIL);
                break;
            case wormhole::WormholeDramTrainingStatus::TrainingPass:
            case wormhole::WormholeDramTrainingStatus::TrainingSkip:
                dram_training_status.push_back(DramTrainingStatus::SUCCESS);
                break;
            default:
                dram_training_status.push_back(DramTrainingStatus::FAIL);
                break;
        }
    }

    return dram_training_status;
}

void WormholeTTDevice::configure_iatu_region(size_t region, uint64_t target, size_t region_size) {
    uint32_t dest_bar_lo = target & 0xffffffff;
    uint32_t dest_bar_hi = (target >> 32) & 0xffffffff;
    std::uint32_t region_id_to_use = region;

    // TODO: stop doing this.  It's related to HUGEPAGE_CHANNEL_3_SIZE_LIMIT.
    if (region == 3) {
        region_id_to_use = 4;  // Hack use region 4 for channel 3..this ensures that we have a smaller chan 3 address
                               // space with the correct start offset
    }

    bar_write32(architecture_impl_->get_arc_csm_mailbox_offset() + 0 * 4, region_id_to_use);
    bar_write32(architecture_impl_->get_arc_csm_mailbox_offset() + 1 * 4, dest_bar_lo);
    bar_write32(architecture_impl_->get_arc_csm_mailbox_offset() + 2 * 4, dest_bar_hi);
    bar_write32(architecture_impl_->get_arc_csm_mailbox_offset() + 3 * 4, region_size);
    arc_messenger_->send_message(
        wormhole::ARC_MSG_COMMON_PREFIX | architecture_impl_->get_arc_message_setup_iatu_for_peer_to_peer(), 0, 0);

    // Print what just happened
    uint32_t peer_region_start = region_id_to_use * region_size;
    uint32_t peer_region_end = (region_id_to_use + 1) * region_size - 1;
    log_debug(
        LogSiliconDriver,
        "    [region id {}] NOC to PCI address range 0x{:x}-0x{:x} mapped to addr 0x{:x}",
        region,
        peer_region_start,
        peer_region_end,
        target);
}

void WormholeTTDevice::dma_d2h_transfer(const uint64_t dst, const uint32_t src, const size_t size) {
    static constexpr uint64_t DMA_WRITE_ENGINE_EN_OFF = 0xc;
    static constexpr uint64_t DMA_WRITE_INT_MASK_OFF = 0x54;
    static constexpr uint64_t DMA_CH_CONTROL1_OFF_WRCH_0 = 0x200;
    static constexpr uint64_t DMA_WRITE_DONE_IMWR_LOW_OFF = 0x60;
    static constexpr uint64_t DMA_WRITE_CH01_IMWR_DATA_OFF = 0x70;
    static constexpr uint64_t DMA_WRITE_DONE_IMWR_HIGH_OFF = 0x64;
    static constexpr uint64_t DMA_WRITE_ABORT_IMWR_LOW_OFF = 0x68;
    static constexpr uint64_t DMA_WRITE_ABORT_IMWR_HIGH_OFF = 0x6c;
    static constexpr uint64_t DMA_TRANSFER_SIZE_OFF_WRCH_0 = 0x208;
    static constexpr uint64_t DMA_SAR_LOW_OFF_WRCH_0 = 0x20c;
    static constexpr uint64_t DMA_SAR_HIGH_OFF_WRCH_0 = 0x210;
    static constexpr uint64_t DMA_DAR_LOW_OFF_WRCH_0 = 0x214;
    static constexpr uint64_t DMA_DAR_HIGH_OFF_WRCH_0 = 0x218;
    static constexpr uint64_t DMA_WRITE_DOORBELL_OFF = 0x10;

    std::scoped_lock lock(dma_mutex_);
    DmaBuffer &dma_buffer = pci_device_->get_dma_buffer();
    volatile uint8_t *bar2 = reinterpret_cast<volatile uint8_t *>(pci_device_->bar2_uc);
    volatile uint32_t *completion = reinterpret_cast<volatile uint32_t *>(dma_buffer.completion);

    if (!completion || !dma_buffer.buffer) {
        throw std::runtime_error("DMA buffer is not initialized");
    }

    if (src % 4 != 0) {
        throw std::runtime_error("DMA source address must be aligned to 4 bytes");
    }

    if (size % 4 != 0) {
        throw std::runtime_error("DMA size must be a multiple of 4");
    }

    if (!bar2) {
        throw std::runtime_error("BAR2 is not mapped");
    }

    // Reset completion flag.
    *completion = 0;

    auto write_reg = [&](uint32_t offset, uint32_t value) {
        *reinterpret_cast<volatile uint32_t *>(bar2 + offset) = value;
    };

    write_reg(DMA_WRITE_ENGINE_EN_OFF, 0x1);
    write_reg(DMA_WRITE_INT_MASK_OFF, 0);
    write_reg(DMA_CH_CONTROL1_OFF_WRCH_0, 0x00000010);  // Remote interrupt enable (for completion)
    write_reg(
        DMA_WRITE_DONE_IMWR_LOW_OFF, (uint32_t)(dma_buffer.completion_pa & 0xFFFFFFFF));  // Write completion address
    write_reg(DMA_WRITE_DONE_IMWR_HIGH_OFF, (uint32_t)((dma_buffer.completion_pa >> 32) & 0xFFFFFFFF));
    write_reg(DMA_WRITE_CH01_IMWR_DATA_OFF, DMA_COMPLETION_VALUE);  // Write completion value
    write_reg(DMA_WRITE_ABORT_IMWR_LOW_OFF, 0);
    write_reg(DMA_WRITE_ABORT_IMWR_HIGH_OFF, 0);
    write_reg(DMA_TRANSFER_SIZE_OFF_WRCH_0, size);
    write_reg(DMA_SAR_LOW_OFF_WRCH_0, src);
    write_reg(DMA_SAR_HIGH_OFF_WRCH_0, 0);
    write_reg(DMA_DAR_LOW_OFF_WRCH_0, (uint32_t)(dst & 0xFFFFFFFF));
    write_reg(DMA_DAR_HIGH_OFF_WRCH_0, (uint32_t)((dst >> 32) & 0xFFFFFFFF));
    write_reg(DMA_WRITE_DOORBELL_OFF, 0);

    auto start = std::chrono::steady_clock::now();
    for (;;) {
        if (*completion == DMA_COMPLETION_VALUE) {
            break;
        }

        auto now = std::chrono::steady_clock::now();
        auto elapsed_ms = std::chrono::duration_cast<std::chrono::milliseconds>(now - start).count();

        if (elapsed_ms > DMA_TIMEOUT_MS) {
            throw std::runtime_error("DMA timeout");
        }
    }
}

void WormholeTTDevice::dma_h2d_transfer(const uint32_t dst, const uint64_t src, const size_t size) {
    static constexpr uint64_t DMA_READ_ENGINE_EN_OFF = 0x2c;
    static constexpr uint64_t DMA_READ_INT_MASK_OFF = 0xa8;
    static constexpr uint64_t DMA_CH_CONTROL1_OFF_RDCH_0 = 0x300;
    static constexpr uint64_t DMA_READ_DONE_IMWR_LOW_OFF = 0xcc;
    static constexpr uint64_t DMA_READ_CH01_IMWR_DATA_OFF = 0xdc;
    static constexpr uint64_t DMA_READ_DONE_IMWR_HIGH_OFF = 0xd0;
    static constexpr uint64_t DMA_READ_ABORT_IMWR_LOW_OFF = 0xd4;
    static constexpr uint64_t DMA_READ_ABORT_IMWR_HIGH_OFF = 0xd8;
    static constexpr uint64_t DMA_TRANSFER_SIZE_OFF_RDCH_0 = 0x308;
    static constexpr uint64_t DMA_SAR_LOW_OFF_RDCH_0 = 0x30c;
    static constexpr uint64_t DMA_SAR_HIGH_OFF_RDCH_0 = 0x310;
    static constexpr uint64_t DMA_DAR_LOW_OFF_RDCH_0 = 0x314;
    static constexpr uint64_t DMA_DAR_HIGH_OFF_RDCH_0 = 0x318;
    static constexpr uint64_t DMA_READ_DOORBELL_OFF = 0x30;

    std::scoped_lock lock(dma_mutex_);
    DmaBuffer &dma_buffer = pci_device_->get_dma_buffer();
    volatile uint8_t *bar2 = reinterpret_cast<volatile uint8_t *>(pci_device_->bar2_uc);
    volatile uint32_t *completion = reinterpret_cast<volatile uint32_t *>(dma_buffer.completion);

    if (!completion || !dma_buffer.buffer) {
        throw std::runtime_error("DMA buffer is not initialized");
    }

    if (dst % 4 != 0) {
        throw std::runtime_error("DMA destination address must be aligned to 4 bytes");
    }

    if (size % 4 != 0) {
        throw std::runtime_error("DMA size must be a multiple of 4");
    }

    if (!bar2) {
        throw std::runtime_error("BAR2 is not mapped");
    }

    // Reset completion flag.
    *completion = 0;

    auto write_reg = [&](uint32_t offset, uint32_t value) {
        *reinterpret_cast<volatile uint32_t *>(bar2 + offset) = value;
    };

    write_reg(DMA_READ_ENGINE_EN_OFF, 0x1);
    write_reg(DMA_READ_INT_MASK_OFF, 0);
    write_reg(DMA_CH_CONTROL1_OFF_RDCH_0, 0x10);  // Remote interrupt enable (for completion)
    write_reg(
        DMA_READ_DONE_IMWR_LOW_OFF, (uint32_t)(dma_buffer.completion_pa & 0xFFFFFFFF));  // Read completion address
    write_reg(DMA_READ_DONE_IMWR_HIGH_OFF, (uint32_t)((dma_buffer.completion_pa >> 32) & 0xFFFFFFFF));
    write_reg(DMA_READ_CH01_IMWR_DATA_OFF, DMA_COMPLETION_VALUE);  // Read completion value
    write_reg(DMA_READ_ABORT_IMWR_LOW_OFF, 0);
    write_reg(DMA_READ_ABORT_IMWR_HIGH_OFF, 0);
    write_reg(DMA_TRANSFER_SIZE_OFF_RDCH_0, size);
    write_reg(DMA_SAR_LOW_OFF_RDCH_0, (uint32_t)(src & 0xFFFFFFFF));
    write_reg(DMA_SAR_HIGH_OFF_RDCH_0, (uint32_t)((src >> 32) & 0xFFFFFFFF));
    write_reg(DMA_DAR_LOW_OFF_RDCH_0, dst);
    write_reg(DMA_DAR_HIGH_OFF_RDCH_0, 0);
    write_reg(DMA_READ_DOORBELL_OFF, 0);

    auto start = std::chrono::steady_clock::now();
    for (;;) {
        if (*completion == DMA_COMPLETION_VALUE) {
            break;
        }

        auto now = std::chrono::steady_clock::now();
        auto elapsed_ms = std::chrono::duration_cast<std::chrono::milliseconds>(now - start).count();

        if (elapsed_ms > DMA_TIMEOUT_MS) {
            throw std::runtime_error("DMA timeout");
        }
    }
}

// TODO: This is a temporary implementation, and ought to be replaced with a
// driver-based technique that can take advantage of multiple channels and
// interrupts.  With a driver-based implementation we can also avoid the need to
// memcpy into/out of a buffer, although exposing zero-copy DMA functionality to
// the application will require IOMMU support.  One day...
void WormholeTTDevice::dma_d2h(void *dst, uint32_t src, size_t size) {
    DmaBuffer &dma_buffer = pci_device_->get_dma_buffer();

    if (size > dma_buffer.size) {
        throw std::runtime_error("DMA size exceeds buffer size");
    }

    dma_d2h_transfer(dma_buffer.buffer_pa, src, size);
    memcpy(dst, dma_buffer.buffer, size);
}

void WormholeTTDevice::dma_h2d(uint32_t dst, const void *src, size_t size) {
    DmaBuffer &dma_buffer = pci_device_->get_dma_buffer();

    if (size > dma_buffer.size) {
        throw std::runtime_error("DMA size exceeds buffer size");
    }

    memcpy(dma_buffer.buffer, src, size);
    dma_h2d_transfer(dst, dma_buffer.buffer_pa, size);
}

void WormholeTTDevice::dma_h2d_zero_copy(uint32_t dst, const void *src, size_t size) {
    dma_h2d_transfer(dst, (uint64_t)(uintptr_t)src, size);
}

void WormholeTTDevice::dma_d2h_zero_copy(void *dst, uint32_t src, size_t size) {
    dma_d2h_transfer((uint64_t)(uintptr_t)dst, src, size);
}

void WormholeTTDevice::wait_eth_core_training(const tt_xy_pair eth_core, const uint32_t timeout_ms) {
    constexpr uint64_t eth_core_heartbeat_addr = 0x1C;
    auto start = std::chrono::system_clock::now();
    uint32_t heartbeat_val;
    read_from_device(&heartbeat_val, eth_core, eth_core_heartbeat_addr, sizeof(heartbeat_val));

    uint32_t new_heartbeat_val = heartbeat_val;
    while (new_heartbeat_val != heartbeat_val) {
        read_from_device(&new_heartbeat_val, eth_core, eth_core_heartbeat_addr, sizeof(heartbeat_val));
        auto end = std::chrono::system_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
        if (duration.count() > timeout_ms) {
            throw std::runtime_error(fmt::format("ETH training timed out after {} ms", timeout_ms));
            break;
        }
    }
}

}  // namespace tt::umd

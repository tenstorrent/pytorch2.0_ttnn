// SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0
#include "umd/device/tt_device/tt_device.h"

#include <tt-logger/tt-logger.hpp>

#include "assert.hpp"
#include "umd/device/arc_messenger.h"
#include "umd/device/driver_atomics.h"
#include "umd/device/tt_device/blackhole_tt_device.h"
#include "umd/device/tt_device/wormhole_tt_device.h"

// TODO #526: This is a hack to allow UMD to use the NOC1 TLB.
bool umd_use_noc1 = false;

namespace tt::umd {

void TTDevice::use_noc1(bool use_noc1) { umd_use_noc1 = use_noc1; }

TTDevice::TTDevice(
    std::shared_ptr<PCIDevice> pci_device, std::unique_ptr<architecture_implementation> architecture_impl) :
    pci_device_(pci_device),
    architecture_impl_(std::move(architecture_impl)),
    arch(architecture_impl_->get_architecture()) {
    lock_manager.initialize_mutex(MutexType::TT_DEVICE_IO, get_pci_device()->get_device_num());
}

void TTDevice::init_tt_device() {
    arc_messenger_ = ArcMessenger::create_arc_messenger(this);
    telemetry = ArcTelemetryReader::create_arc_telemetry_reader(this);
}

TTDevice::TTDevice() {}

/* static */ std::unique_ptr<TTDevice> TTDevice::create(int pci_device_number) {
    auto pci_device = std::make_shared<PCIDevice>(pci_device_number);

    switch (pci_device->get_arch()) {
        case ARCH::WORMHOLE_B0:
            return std::make_unique<WormholeTTDevice>(pci_device);
        case ARCH::BLACKHOLE:
            return std::make_unique<BlackholeTTDevice>(pci_device);
        default:
            return nullptr;
    }
}

architecture_implementation *TTDevice::get_architecture_implementation() { return architecture_impl_.get(); }

std::shared_ptr<PCIDevice> TTDevice::get_pci_device() { return pci_device_; }

tt::ARCH TTDevice::get_arch() { return arch; }

bool TTDevice::is_hardware_hung() {
    volatile const void *addr = reinterpret_cast<const char *>(pci_device_->bar0_uc) +
                                (architecture_impl_->get_arc_reset_scratch_offset() + 6 * 4) -
                                pci_device_->bar0_uc_offset;
    std::uint32_t scratch_data = *reinterpret_cast<const volatile std::uint32_t *>(addr);

    return (scratch_data == HANG_READ_VALUE);
}

void TTDevice::detect_hang_read(std::uint32_t data_read) {
    if (data_read == HANG_READ_VALUE && is_hardware_hung()) {
        std::uint32_t scratch_data =
            *pci_device_->get_register_address<std::uint32_t>(architecture_impl_->get_read_checking_offset());

        throw std::runtime_error("Read 0xffffffff from PCIE: you should reset the board.");
    }
}

// This is only needed for the BH workaround in iatu_configure_peer_region since no arc
void TTDevice::write_regs(volatile uint32_t *dest, const uint32_t *src, uint32_t word_len) {
    while (word_len-- != 0) {
        *dest++ = *src++;
    }
}

void TTDevice::write_regs(uint32_t byte_addr, uint32_t word_len, const void *data) {
    volatile uint32_t *dest = pci_device_->get_register_address<uint32_t>(byte_addr);
    const uint32_t *src = reinterpret_cast<const uint32_t *>(data);

    write_regs(dest, src, word_len);
}

void TTDevice::read_regs(uint32_t byte_addr, uint32_t word_len, void *data) {
    const volatile uint32_t *src = pci_device_->get_register_address<uint32_t>(byte_addr);
    uint32_t *dest = reinterpret_cast<uint32_t *>(data);

    while (word_len-- != 0) {
        uint32_t temp = *src++;
        memcpy(dest++, &temp, sizeof(temp));
    }
}

void TTDevice::memcpy_to_device(void *dest, const void *src, std::size_t num_bytes) {
    typedef std::uint32_t copy_t;

    // Start by aligning the destination (device) pointer. If needed, do RMW to fix up the
    // first partial word.
    volatile copy_t *dp;

    std::uintptr_t dest_addr = reinterpret_cast<std::uintptr_t>(dest);
    unsigned int dest_misalignment = dest_addr % sizeof(copy_t);

    if (dest_misalignment != 0) {
        // Read-modify-write for the first dest element.
        dp = reinterpret_cast<copy_t *>(dest_addr - dest_misalignment);

        copy_t tmp = *dp;

        auto leading_len = std::min(sizeof(tmp) - dest_misalignment, num_bytes);

        std::memcpy(reinterpret_cast<char *>(&tmp) + dest_misalignment, src, leading_len);
        num_bytes -= leading_len;
        src = static_cast<const char *>(src) + leading_len;

        *dp++ = tmp;

    } else {
        dp = static_cast<copy_t *>(dest);
    }

    // Copy the destination-aligned middle.
    const copy_t *sp = static_cast<const copy_t *>(src);
    std::size_t num_words = num_bytes / sizeof(copy_t);

    for (std::size_t i = 0; i < num_words; i++) {
        *dp++ = *sp++;
    }

    // Finally copy any sub-word trailer, again RMW on the destination.
    auto trailing_len = num_bytes % sizeof(copy_t);
    if (trailing_len != 0) {
        copy_t tmp = *dp;

        std::memcpy(&tmp, sp, trailing_len);

        *dp++ = tmp;
    }
}

void TTDevice::memcpy_from_device(void *dest, const void *src, std::size_t num_bytes) {
    typedef std::uint32_t copy_t;

    // Start by aligning the source (device) pointer.
    const volatile copy_t *sp;

    std::uintptr_t src_addr = reinterpret_cast<std::uintptr_t>(src);
    unsigned int src_misalignment = src_addr % sizeof(copy_t);

    if (src_misalignment != 0) {
        sp = reinterpret_cast<copy_t *>(src_addr - src_misalignment);

        copy_t tmp = *sp++;

        auto leading_len = std::min(sizeof(tmp) - src_misalignment, num_bytes);
        std::memcpy(dest, reinterpret_cast<char *>(&tmp) + src_misalignment, leading_len);
        num_bytes -= leading_len;
        dest = static_cast<char *>(dest) + leading_len;

    } else {
        sp = static_cast<const volatile copy_t *>(src);
    }

    // Copy the source-aligned middle.
    copy_t *dp = static_cast<copy_t *>(dest);
    std::size_t num_words = num_bytes / sizeof(copy_t);

    for (std::size_t i = 0; i < num_words; i++) {
        *dp++ = *sp++;
    }

    // Finally copy any sub-word trailer.
    auto trailing_len = num_bytes % sizeof(copy_t);
    if (trailing_len != 0) {
        copy_t tmp = *sp;
        std::memcpy(dp, &tmp, trailing_len);
    }
}

void TTDevice::write_block(uint64_t byte_addr, uint64_t num_bytes, const uint8_t *buffer_addr) {
    void *dest = nullptr;
    if (pci_device_->bar4_wc != nullptr && byte_addr >= BAR0_BH_SIZE) {
        byte_addr -= BAR0_BH_SIZE;
        dest = reinterpret_cast<uint8_t *>(pci_device_->bar4_wc) + byte_addr;
    } else {
        dest = pci_device_->get_register_address<uint8_t>(byte_addr);
    }

    const void *src = reinterpret_cast<const void *>(buffer_addr);
    if (arch == tt::ARCH::WORMHOLE_B0) {
        memcpy_to_device(dest, src, num_bytes);
    } else {
        memcpy(dest, src, num_bytes);
    }
}

void TTDevice::read_block(uint64_t byte_addr, uint64_t num_bytes, uint8_t *buffer_addr) {
    void *src = nullptr;
    if (pci_device_->bar4_wc != nullptr && byte_addr >= BAR0_BH_SIZE) {
        byte_addr -= BAR0_BH_SIZE;
        src = reinterpret_cast<uint8_t *>(pci_device_->bar4_wc) + byte_addr;
    } else {
        src = pci_device_->get_register_address<uint8_t>(byte_addr);
    }

    void *dest = reinterpret_cast<void *>(buffer_addr);
    if (arch == tt::ARCH::WORMHOLE_B0) {
        memcpy_from_device(dest, src, num_bytes);
    } else {
        memcpy(dest, src, num_bytes);
    }

    if (num_bytes >= sizeof(std::uint32_t)) {
        detect_hang_read(*reinterpret_cast<std::uint32_t *>(dest));
    }
}

void TTDevice::read_from_device(void *mem_ptr, tt_xy_pair core, uint64_t addr, uint32_t size) {
    auto lock = lock_manager.acquire_mutex(MutexType::TT_DEVICE_IO, get_pci_device()->get_device_num());
    uint8_t *buffer_addr = static_cast<uint8_t *>(mem_ptr);
    const uint32_t tlb_index = get_architecture_implementation()->get_small_read_write_tlb();
    while (size > 0) {
        auto [mapped_address, tlb_size] = set_dynamic_tlb(tlb_index, core, addr, tt::umd::tlb_data::Strict);
        uint32_t transfer_size = std::min((uint64_t)size, tlb_size);
        read_block(mapped_address, transfer_size, buffer_addr);

        size -= transfer_size;
        addr += transfer_size;
        buffer_addr += transfer_size;
    }
}

void TTDevice::write_to_device(void *mem_ptr, tt_xy_pair core, uint64_t addr, uint32_t size) {
    auto lock = lock_manager.acquire_mutex(MutexType::TT_DEVICE_IO, get_pci_device()->get_device_num());
    uint8_t *buffer_addr = static_cast<uint8_t *>(mem_ptr);
    const uint32_t tlb_index = get_architecture_implementation()->get_small_read_write_tlb();

    while (size > 0) {
        auto [mapped_address, tlb_size] = set_dynamic_tlb(tlb_index, core, addr, tt::umd::tlb_data::Strict);
        uint32_t transfer_size = std::min((uint64_t)size, tlb_size);
        write_block(mapped_address, transfer_size, buffer_addr);

        size -= transfer_size;
        addr += transfer_size;
        buffer_addr += transfer_size;
    }
}

void TTDevice::write_tlb_reg(
    uint32_t byte_addr, uint64_t value_lower, uint64_t value_upper, uint32_t tlb_cfg_reg_size) {
    TT_ASSERT(
        (tlb_cfg_reg_size == 8) or (tlb_cfg_reg_size == 12),
        "Tenstorrent hardware supports only 64bit or 96bit TLB config regs");

    volatile uint64_t *dest_qw = pci_device_->get_register_address<uint64_t>(byte_addr);
    volatile uint32_t *dest_extra_dw = pci_device_->get_register_address<uint32_t>(byte_addr + 8);
#if defined(__ARM_ARCH) || defined(__riscv)
    // The store below goes through UC memory on x86, which has implicit ordering constraints with WC accesses.
    // ARM has no concept of UC memory. This will not allow for implicit ordering of this store wrt other memory
    // accesses. Insert an explicit full memory barrier for ARM. Do the same for RISC-V.
    tt_driver_atomics::mfence();
#endif
    *dest_qw = value_lower;
    if (tlb_cfg_reg_size > 8) {
        uint32_t *p_value_upper = reinterpret_cast<uint32_t *>(&value_upper);
        *dest_extra_dw = p_value_upper[0];
    }
    tt_driver_atomics::mfence();  // Otherwise subsequent WC loads move earlier than the above UC store to the TLB
                                  // register.
}

// Get TLB index (from zero), check if it's in 16MB, 2MB or 1MB TLB range, and dynamically program it.
dynamic_tlb TTDevice::set_dynamic_tlb(
    unsigned int tlb_index,
    tt_xy_pair start,
    tt_xy_pair end,
    std::uint64_t address,
    bool multicast,
    std::uint64_t ordering) {
    if (multicast) {
        std::tie(start, end) = architecture_impl_->multicast_workaround(start, end);
    }

    log_trace(
        LogSiliconDriver,
        "set_dynamic_tlb with arguments: tlb_index = {}, start = ({}, {}), end = ({}, {}), address = 0x{:x}, "
        "multicast "
        "= {}, ordering = {}",
        tlb_index,
        start.x,
        start.y,
        end.x,
        end.y,
        address,
        multicast,
        (int)ordering);

    tt::umd::tlb_configuration tlb_config = architecture_impl_->get_tlb_configuration(tlb_index);
    std::uint32_t TLB_CFG_REG_SIZE_BYTES = architecture_impl_->get_tlb_cfg_reg_size_bytes();
    uint64_t tlb_address = address / tlb_config.size;
    uint32_t local_address = address % tlb_config.size;
    uint64_t tlb_base = tlb_config.base + (tlb_config.size * tlb_config.index_offset);
    uint32_t tlb_cfg_reg = tlb_config.cfg_addr + (TLB_CFG_REG_SIZE_BYTES * tlb_config.index_offset);

    std::pair<std::uint64_t, std::uint64_t> tlb_data =
        tt::umd::tlb_data{
            .local_offset = tlb_address,
            .x_end = static_cast<uint64_t>(end.x),
            .y_end = static_cast<uint64_t>(end.y),
            .x_start = static_cast<uint64_t>(start.x),
            .y_start = static_cast<uint64_t>(start.y),
            .noc_sel = umd_use_noc1 ? 1U : 0,
            .mcast = multicast,
            .ordering = ordering,
            // TODO #2715: hack for Blackhole A0, will potentially be fixed in B0.
            // Using the same static vc for reads and writes through TLBs can hang the card. It doesn't even have to
            // be the same TLB. Dynamic vc should not have this issue. There might be a perf impact with using
            // dynamic vc.
            .static_vc = (arch == tt::ARCH::BLACKHOLE) ? false : true,
        }
            .apply_offset(tlb_config.offset);

    log_debug(
        LogSiliconDriver,
        "set_dynamic_tlb() with tlb_index: {} tlb_index_offset: {} dynamic_tlb_size: {}MB tlb_base: 0x{:x} "
        "tlb_cfg_reg: 0x{:x}",
        tlb_index,
        tlb_config.index_offset,
        tlb_config.size / (1024 * 1024),
        tlb_base,
        tlb_cfg_reg);
    write_tlb_reg(tlb_cfg_reg, tlb_data.first, tlb_data.second, TLB_CFG_REG_SIZE_BYTES);

    return {tlb_base + local_address, tlb_config.size - local_address};
}

dynamic_tlb TTDevice::set_dynamic_tlb(
    unsigned int tlb_index, tt_xy_pair target, std::uint64_t address, std::uint64_t ordering) {
    return set_dynamic_tlb(tlb_index, tt_xy_pair(0, 0), target, address, false, ordering);
}

dynamic_tlb TTDevice::set_dynamic_tlb_broadcast(
    unsigned int tlb_index, std::uint64_t address, tt_xy_pair start, tt_xy_pair end, std::uint64_t ordering) {
    // Issue a broadcast to cores included in the start (top left) and end (bottom right) grid
    return set_dynamic_tlb(tlb_index, start, end, address, true, ordering);
}

void TTDevice::configure_iatu_region(size_t region, uint64_t target, size_t region_size) {
    throw std::runtime_error("configure_iatu_region is not implemented for this device");
}

void TTDevice::wait_arc_core_start(const tt_xy_pair arc_core, const uint32_t timeout_ms) {
    throw std::runtime_error("Waiting for ARC core to start is supported only for Blackhole TTDevice.");
}

void TTDevice::bar_write32(uint32_t addr, uint32_t data) {
    if (addr < get_pci_device()->bar0_uc_offset) {
        write_block(addr, sizeof(data), reinterpret_cast<const uint8_t *>(&data));  // do we have to reinterpret_cast?
    } else {
        write_regs(addr, 1, &data);
    }
}

uint32_t TTDevice::bar_read32(uint32_t addr) {
    uint32_t data;
    if (addr < get_pci_device()->bar0_uc_offset) {
        read_block(addr, sizeof(data), reinterpret_cast<uint8_t *>(&data));
    } else {
        read_regs(addr, 1, &data);
    }
    return data;
}

tt::umd::ArcMessenger *TTDevice::get_arc_messenger() const { return arc_messenger_.get(); }

tt::umd::ArcTelemetryReader *TTDevice::get_arc_telemetry_reader() const { return telemetry.get(); }

TTDevice::~TTDevice() { lock_manager.clear_mutex(MutexType::TT_DEVICE_IO, get_pci_device()->get_device_num()); }

std::vector<DramTrainingStatus> TTDevice::get_dram_training_status() { return {}; }

void TTDevice::wait_for_non_mmio_flush() {}

bool TTDevice::is_remote() { return is_remote_tt_device; }

BoardType TTDevice::get_board_type() { return get_board_type_from_board_id(get_board_id()); }

}  // namespace tt::umd

// SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0
#include "umd/device/tt_device/remote_wormhole_tt_device.h"

namespace tt::umd {

RemoteWormholeTTDevice::RemoteWormholeTTDevice(LocalChip *local_chip, eth_coord_t target_chip) :
    WormholeTTDevice(local_chip->get_tt_device()->get_pci_device()),
    local_chip_(local_chip),
    target_chip_(target_chip),
    remote_communication_(std::make_unique<RemoteCommunication>(local_chip_)) {
    is_remote_tt_device = true;
    init_tt_device();
}

void RemoteWormholeTTDevice::read_from_device(void *mem_ptr, tt_xy_pair core, uint64_t addr, uint32_t size) {
    remote_communication_->read_non_mmio(target_chip_, core, mem_ptr, addr, size);
}

void RemoteWormholeTTDevice::write_to_device(void *mem_ptr, tt_xy_pair core, uint64_t addr, uint32_t size) {
    remote_communication_->write_to_non_mmio(target_chip_, core, mem_ptr, addr, size);
}

void RemoteWormholeTTDevice::wait_for_non_mmio_flush() { remote_communication_->wait_for_non_mmio_flush(); }

LocalChip *RemoteWormholeTTDevice::get_local_chip() { return local_chip_; }

RemoteCommunication *RemoteWormholeTTDevice::get_remote_communication() { return remote_communication_.get(); }

}  // namespace tt::umd

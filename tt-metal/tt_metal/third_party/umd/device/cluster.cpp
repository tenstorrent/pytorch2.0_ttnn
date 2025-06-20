// SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0
#include "umd/device/cluster.h"

#include <assert.h>
#include <dirent.h>
#include <errno.h>
#include <fmt/format.h>
#include <fmt/ranges.h>  // Needed to format vectors
#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>

#include <algorithm>
#include <cerrno>
#include <chrono>
#include <cstddef>
#include <cstdint>
#include <cstdlib>
#include <filesystem>
#include <fstream>
#include <iterator>
#include <limits>
#include <map>
#include <memory>
#include <mutex>
#include <optional>
#include <ratio>
#include <regex>
#include <stdexcept>
#include <string>
#include <tt-logger/tt-logger.hpp>
#include <utility>
#include <vector>

#include "api/umd/device/cluster.h"
#include "api/umd/device/tt_core_coordinates.h"
#include "assert.hpp"
#include "umd/device/architecture_implementation.h"
#include "umd/device/blackhole_implementation.h"
#include "umd/device/chip/local_chip.h"
#include "umd/device/chip/mock_chip.h"
#include "umd/device/chip/remote_chip.h"
#include "umd/device/chip_helpers/tlb_manager.h"
#include "umd/device/driver_atomics.h"
#include "umd/device/hugepage.h"
#include "umd/device/topology_utils.h"
#include "umd/device/tt_cluster_descriptor.h"
#include "umd/device/tt_core_coordinates.h"
#include "umd/device/tt_simulation_device.h"
#include "umd/device/tt_soc_descriptor.h"
#include "umd/device/types/arch.h"
#include "umd/device/types/blackhole_eth.h"
#include "umd/device/types/tlb.h"
#include "umd/device/umd_utils.h"
#include "umd/device/wormhole_implementation.h"
#include "yaml-cpp/yaml.h"

using namespace tt;
using namespace tt::umd;

extern bool umd_use_noc1;

static constexpr uint32_t REMOTE_CMD_NOC_BIT = 9;

// --------------------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------------------------------

#include <fstream>
#include <iomanip>
#include <thread>

#include "umd/device/tt_silicon_driver_common.hpp"
#include "umd/device/tt_xy_pair.h"

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

struct remote_update_ptr_t {
    uint32_t ptr;
    uint32_t pad[3];
};

namespace tt::umd {

const tt_SocDescriptor& Cluster::get_soc_descriptor(chip_id_t chip_id) const {
    return get_chip(chip_id)->get_soc_descriptor();
}

void Cluster::create_device(
    const std::set<chip_id_t>& target_mmio_device_ids,
    const uint32_t& num_host_mem_ch_per_mmio_device,
    const ChipType& chip_type) {
    log_debug(LogSiliconDriver, "Cluster::Cluster");

    // Don't buffer stdout.
    setbuf(stdout, NULL);

    for (const chip_id_t& logical_device_id : target_mmio_device_ids) {
        if (chip_type == ChipType::SILICON) {
            bool hugepages_initialized =
                (get_local_chip(logical_device_id)->get_sysmem_manager()->get_hugepage_mapping(0).mapping != nullptr);
            // Large writes to remote chips require hugepages to be initialized.
            // Conservative assert - end workload if remote chips present but hugepages not initialized (failures caused
            // if using remote only for small transactions)
            if (remote_chip_ids_.size()) {
                TT_ASSERT(
                    hugepages_initialized,
                    "Hugepages must be successfully initialized if workload contains remote chips!");
            }
            if (!hugepages_initialized) {
                log_warning(LogSiliconDriver, "No hugepage mapping at device {}.", logical_device_id);
            }
        }
    }
}

void Cluster::construct_cluster(const uint32_t& num_host_mem_ch_per_mmio_device, const ChipType& chip_type) {
    // TODO: work on removing this member altogether. Currently assumes all have the same arch.
    arch_name = chips_.empty() ? tt::ARCH::Invalid : chips_.begin()->second->get_soc_descriptor().arch;

    if (chip_type == ChipType::SILICON) {
        std::vector<int> pci_ids;
        auto mmio_id_map = cluster_desc->get_chips_with_mmio();
        for (chip_id_t local_chip_id : local_chip_ids_) {
            pci_ids.push_back(mmio_id_map.at(local_chip_id));
        }
        log_info(
            LogSiliconDriver,
            "Opening local chip ids/pci ids: {}/{} and remote chip ids {}",
            local_chip_ids_,
            pci_ids,
            remote_chip_ids_);
    }

    create_device(local_chip_ids_, num_host_mem_ch_per_mmio_device, chip_type);

    // Disable dependency to ethernet firmware for all BH devices and WH devices with all chips having MMIO (e.g. UBB
    // Galaxy, or P300).
    if (remote_chip_ids_.empty()) {
        use_ethernet_broadcast = false;
    }
}

std::unique_ptr<Chip> Cluster::construct_chip_from_cluster(
    chip_id_t chip_id,
    const ChipType& chip_type,
    tt_ClusterDescriptor* cluster_desc,
    tt_SocDescriptor& soc_desc,
    int num_host_mem_channels,
    const std::filesystem::path& simulator_directory) {
    if (chip_type == ChipType::MOCK) {
        return std::make_unique<MockChip>(soc_desc);
    }
    if (chip_type == ChipType::SIMULATION) {
#ifdef TT_UMD_BUILD_SIMULATION
        // Note that passed soc descriptor is ignored in favor of soc descriptor from simulator_directory.
        return std::make_unique<tt_SimulationDevice>(simulator_directory);
#else
        throw std::runtime_error(
            "Simulation device is not supported in this build. Set '-DTT_UMD_BUILD_SIMULATION=ON' during cmake "
            "configuration to enable simulation device.");
#endif
    }

    if (cluster_desc->is_chip_mmio_capable(chip_id)) {
        auto chip = std::make_unique<LocalChip>(
            soc_desc, cluster_desc->get_chips_with_mmio().at(chip_id), num_host_mem_channels);
        if (cluster_desc->get_arch(chip_id) == tt::ARCH::WORMHOLE_B0) {
            // Remote transfer currently supported only for wormhole.
            chip->set_remote_transfer_ethernet_cores(cluster_desc->get_active_eth_channels(chip_id));
        }
        return chip;
    } else {
        if (cluster_desc->get_arch(chip_id) != tt::ARCH::WORMHOLE_B0) {
            throw std::runtime_error("Remote chips are supported only for wormhole.");
        }
        std::unique_ptr<RemoteWormholeTTDevice> remote_tt_device = std::make_unique<RemoteWormholeTTDevice>(
            get_local_chip(cluster_desc->get_closest_mmio_capable_chip(chip_id)),
            cluster_desc->get_chip_locations().at(chip_id));
        return std::make_unique<RemoteChip>(soc_desc, std::move(remote_tt_device));
    }
}

tt_SocDescriptor Cluster::construct_soc_descriptor(
    const std::string& soc_desc_path,
    chip_id_t chip_id,
    ChipType chip_type,
    tt_ClusterDescriptor* cluster_desc,
    bool perform_harvesting,
    HarvestingMasks& simulated_harvesting_masks) {
    bool chip_in_cluster_descriptor =
        cluster_desc->get_all_chips().find(chip_id) != cluster_desc->get_all_chips().end();

    // In case of SILICON chip type, this chip has to exist in the cluster descriptor. But it doesn't have to exist in
    // case of Mock or Simulation chip type.
    if (chip_type == ChipType::SILICON && !chip_in_cluster_descriptor) {
        throw std::runtime_error(
            fmt::format("Chip {} not found in cluster descriptor. Cannot create device.", chip_id));
    }

    bool noc_translation_table_en =
        chip_in_cluster_descriptor ? cluster_desc->get_noc_translation_table_en().at(chip_id) : false;
    HarvestingMasks harvesting_masks =
        chip_in_cluster_descriptor
            ? get_harvesting_masks(chip_id, cluster_desc, perform_harvesting, simulated_harvesting_masks)
            : HarvestingMasks{};
    BoardType chip_board_type = chip_in_cluster_descriptor ? cluster_desc->get_board_type(chip_id) : BoardType::UNKNOWN;
    uint8_t asic_location =
        chip_in_cluster_descriptor ? cluster_desc->get_chip_uid(chip_id).value_or(ChipUID{}).asic_location : 0;

    if (soc_desc_path.empty()) {
        tt::ARCH arch = chip_in_cluster_descriptor ? cluster_desc->get_arch(chip_id) : tt::ARCH::WORMHOLE_B0;

        return tt_SocDescriptor(arch, noc_translation_table_en, harvesting_masks, chip_board_type, asic_location);

    } else {
        tt_SocDescriptor soc_desc =
            tt_SocDescriptor(soc_desc_path, noc_translation_table_en, harvesting_masks, chip_board_type, asic_location);

        // In this case, check that the passed soc descriptor architecture doesn't conflate with the one in the cluster
        // descriptor.
        if (chip_in_cluster_descriptor && soc_desc.arch != cluster_desc->get_arch(chip_id)) {
            throw std::runtime_error(fmt::format(
                "Passed soc descriptor has {} arch, but for chip id {} has arch {}",
                arch_to_str(soc_desc.arch),
                chip_id,
                arch_to_str(cluster_desc->get_arch(chip_id))));
        }

        return soc_desc;
    }
}

void Cluster::add_chip(const chip_id_t& chip_id, const ChipType& chip_type, std::unique_ptr<Chip> chip) {
    TT_ASSERT(
        chips_.find(chip_id) == chips_.end(),
        "Chip with id {} already exists in cluster. Cannot add another chip with the same id.",
        chip_id);
    all_chip_ids_.insert(chip_id);
    // All non silicon chip types are considered local chips.
    if (chip_type != ChipType::SILICON || cluster_desc->is_chip_mmio_capable(chip_id)) {
        local_chip_ids_.insert(chip_id);
    } else {
        remote_chip_ids_.insert(chip_id);
    }
    chips_.emplace(chip_id, std::move(chip));
}

uint32_t Cluster::get_tensix_harvesting_mask(
    chip_id_t chip_id, tt_ClusterDescriptor* cluster_desc, HarvestingMasks& simulated_harvesting_masks) {
    uint32_t tensix_harvesting_mask_physical_layout = cluster_desc->get_harvesting_info().at(chip_id);
    uint32_t tensix_harvesting_mask = CoordinateManager::shuffle_tensix_harvesting_mask(
        cluster_desc->get_arch(chip_id), tensix_harvesting_mask_physical_layout);
    log_info(
        LogSiliconDriver,
        "Harvesting mask for chip {} is 0x{:x} (physical layout: 0x{:x}, logical: 0x{:x}, simulated harvesting mask: "
        "0x{:x}).",
        chip_id,
        tensix_harvesting_mask | simulated_harvesting_masks.tensix_harvesting_mask,
        tensix_harvesting_mask_physical_layout,
        tensix_harvesting_mask,
        simulated_harvesting_masks.tensix_harvesting_mask);
    return tensix_harvesting_mask | simulated_harvesting_masks.tensix_harvesting_mask;
}

HarvestingMasks Cluster::get_harvesting_masks(
    chip_id_t chip_id,
    tt_ClusterDescriptor* cluster_desc,
    bool perform_harvesting,
    HarvestingMasks& simulated_harvesting_masks) {
    if (!perform_harvesting) {
        log_info(LogSiliconDriver, "Skipping harvesting for chip {}.", chip_id);
        return HarvestingMasks{};
    }
    return HarvestingMasks{
        .tensix_harvesting_mask = get_tensix_harvesting_mask(chip_id, cluster_desc, simulated_harvesting_masks),
        .dram_harvesting_mask =
            cluster_desc->get_dram_harvesting_mask(chip_id) | simulated_harvesting_masks.dram_harvesting_mask,
        .eth_harvesting_mask =
            cluster_desc->get_eth_harvesting_mask(chip_id) | simulated_harvesting_masks.eth_harvesting_mask,
        .pcie_harvesting_mask =
            cluster_desc->get_pcie_harvesting_mask(chip_id) | simulated_harvesting_masks.pcie_harvesting_mask};
}

void Cluster::ubb_eth_connections(
    const std::unordered_map<chip_id_t, std::unique_ptr<tt::umd::Chip>>& chips,
    std::unique_ptr<tt_ClusterDescriptor>& cluster_desc) {
    const uint64_t conn_info = 0x1200;
    const uint64_t node_info = 0x1100;
    const uint32_t eth_unknown = 0;
    const uint32_t eth_unconnected = 1;
    const uint32_t eth_connected = 2;
    const uint32_t shelf_offset = 9;
    const uint32_t rack_offset = 10;
    const uint32_t base_addr = 0x1ec0;

    std::unordered_map<uint64_t, chip_id_t> chip_uid_to_local_chip_id = {};

    for (const auto& [chip_id, chip] : chips) {
        std::vector<CoreCoord> eth_cores = chip->get_soc_descriptor().get_cores(CoreType::ETH);
        TTDevice* tt_device = chip->get_tt_device();

        uint32_t channel = 0;
        for (const CoreCoord& eth_core : eth_cores) {
            uint32_t port_status;

            tt_device->read_from_device(
                &port_status, tt_xy_pair(eth_core.x, eth_core.y), conn_info + (channel * 4), sizeof(uint32_t));

            if (port_status == eth_unknown || port_status == eth_unconnected) {
                channel++;
                continue;
            }

            uint64_t local_chip_id;
            tt_device->read_from_device(
                &local_chip_id, tt_xy_pair(eth_core.x, eth_core.y), base_addr + (64 * 4), sizeof(uint64_t));

            uint64_t remote_chip_id;
            tt_device->read_from_device(
                &remote_chip_id, tt_cxy_pair(chip_id, eth_core.x, eth_core.y), base_addr + (72 * 4), sizeof(uint64_t));

            chip_uid_to_local_chip_id.insert({local_chip_id, chip_id});
            cluster_desc->chip_unique_ids.insert({chip_id, local_chip_id});

            channel++;
        }
    }

    for (const auto& [chip_id, chip] : chips) {
        std::vector<CoreCoord> eth_cores = chip->get_soc_descriptor().get_cores(CoreType::ETH);
        TTDevice* tt_device = chip->get_tt_device();

        uint32_t channel = 0;
        for (const CoreCoord& eth_core : eth_cores) {
            uint32_t port_status;
            tt_device->read_from_device(
                &port_status,
                tt_cxy_pair(chip_id, eth_core.x, eth_core.y),
                conn_info + (channel * 4),
                sizeof(uint32_t));

            auto start = std::chrono::steady_clock::now();
            uint32_t timeout_ms = 1000;
            while (port_status == eth_unknown) {
                auto now = std::chrono::steady_clock::now();
                auto elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(now - start).count();
                if (elapsed > timeout_ms) {
                    throw std::runtime_error(
                        fmt::format("Device {} timed out waiting for ethernet channel {} to train", chip_id, channel));
                }
            }
            if (port_status == eth_unconnected) {
                cluster_desc->idle_eth_channels[chip_id].insert(channel);
                channel++;
                continue;
            }
            if (port_status == eth_connected) {
                cluster_desc->active_eth_channels[chip_id].insert(channel);
                uint64_t remote_chip_id;
                tt_device->read_from_device(
                    &remote_chip_id,
                    tt_cxy_pair(chip_id, eth_core.x, eth_core.y),
                    base_addr + (72 * 4),
                    sizeof(uint64_t));

                uint64_t local_chip_id;
                tt_device->read_from_device(
                    &local_chip_id,
                    tt_cxy_pair(chip_id, eth_core.x, eth_core.y),
                    base_addr + (64 * 4),
                    sizeof(uint64_t));

                uint32_t remote_eth_id;
                tt_device->read_from_device(
                    &remote_eth_id, tt_cxy_pair(chip_id, eth_core.x, eth_core.y), base_addr + 76 * 4, sizeof(uint32_t));

                if (chip_uid_to_local_chip_id.find(remote_chip_id) == chip_uid_to_local_chip_id.end()) {
                    cluster_desc->ethernet_connections_to_remote_mmio_devices[chip_id][channel] = {
                        remote_chip_id, remote_eth_id};
                    channel++;
                } else {
                    chip_id_t remote_logical_chip_id = chip_uid_to_local_chip_id.at(remote_chip_id);

                    cluster_desc->ethernet_connections[chip_id][channel] = {remote_logical_chip_id, remote_eth_id};

                    channel++;
                }
            } else {
                throw std::runtime_error(fmt::format(
                    "6U Device {} ethernet channel {} has port status {}, routing FW should be disabled",
                    chip_id,
                    channel,
                    port_status));
            }
        }
    }
}

void Cluster::verify_cluster_options(const ClusterOptions& options) {
    if (!options.pci_target_devices.empty() && !options.target_devices.empty()) {
        throw std::runtime_error("Cannot pass both target_devices and pci_target_devices to Cluster constructor.");
    }

    if (!options.pci_target_devices.empty() && options.cluster_descriptor != nullptr) {
        throw std::runtime_error(
            "Cannot pass pci_target_devices and custom cluster descriptor to Cluster constructor. "
            "Custom cluster descriptor should be used together with target_devices (logical IDs).");
    }
}

Cluster::Cluster(ClusterOptions options) {
    Cluster::verify_cluster_options(options);
    // If the cluster descriptor is not provided, create a new one.
    tt_ClusterDescriptor* temp_full_cluster_desc = options.cluster_descriptor;
    std::unique_ptr<tt_ClusterDescriptor> temp_full_cluster_desc_ptr;
    if (temp_full_cluster_desc == nullptr) {
        temp_full_cluster_desc_ptr = Cluster::create_cluster_descriptor(options.sdesc_path, options.pci_target_devices);
        temp_full_cluster_desc = temp_full_cluster_desc_ptr.get();
    }

    std::unordered_set<chip_id_t> chips_to_construct = options.target_devices;
    // If no target devices are passed, obtain them from the cluster descriptor.
    if (chips_to_construct.empty()) {
        chips_to_construct = temp_full_cluster_desc->get_all_chips();
        // If no target devices are passed and the cluster descriptor is not constrained, we can use the full cluster.
        // Note that the pointer is being dereferenced below, that means that the default copy constructor will be
        // called for tt_ClusterDescriptor to construct the object which will end up in the unique_ptr, note that the
        // line below doesn't take ownership of already existing object pointed to by temp_full_cluster_desc.
        cluster_desc = std::make_unique<tt_ClusterDescriptor>(*temp_full_cluster_desc);
    } else {
        // Create constrained cluster descriptor which only contains the chips to be in this Cluster.
        cluster_desc =
            tt_ClusterDescriptor::create_constrained_cluster_descriptor(temp_full_cluster_desc, chips_to_construct);
    }
    std::vector<chip_id_t> chips_to_construct_vec(chips_to_construct.begin(), chips_to_construct.end());
    // Check target_devices against the cluster descriptor in case of silicon chips.
    // We also have to sort them so that local chips are constructed first.
    // For MOCK and SIMULATION chip types, passing target_devices which are not in cluster descriptor is allowed.
    if (options.chip_type == ChipType::SILICON) {
        chips_to_construct_vec = cluster_desc->get_chips_local_first(chips_to_construct);
    } else {
        // If we're running on a system where system chips don't match what was requested through target_chips for non
        // silicon chip, then just create a mock cluster descriptor so we still have info for those chips. This includes
        // systems with no silicon chips.
        bool construct_mock_cluster_descriptor = false;
        for (auto const& chip_id : chips_to_construct_vec) {
            if (temp_full_cluster_desc->get_all_chips().find(chip_id) ==
                temp_full_cluster_desc->get_all_chips().end()) {
                log_warning(
                    LogSiliconDriver,
                    "Chip {} not found in cluster descriptor, creating mock cluster descriptor.",
                    chip_id);
                construct_mock_cluster_descriptor = true;
                break;
            }
        }
        if (construct_mock_cluster_descriptor) {
            cluster_desc = tt_ClusterDescriptor::create_mock_cluster(chips_to_construct_vec, tt::ARCH::WORMHOLE_B0);
        }
    }
    for (auto& chip_id : chips_to_construct_vec) {
        // Combine passed simulated_harvesting_masks
        HarvestingMasks simulated_harvesting_masks =
            options.simulated_harvesting_masks | ((options.simulated_harvesting_masks_per_chip.find(chip_id) !=
                                                   options.simulated_harvesting_masks_per_chip.end())
                                                      ? options.simulated_harvesting_masks_per_chip.at(chip_id)
                                                      : HarvestingMasks{});
        tt_SocDescriptor soc_desc = construct_soc_descriptor(
            options.sdesc_path,
            chip_id,
            options.chip_type,
            cluster_desc.get(),
            options.perform_harvesting,
            simulated_harvesting_masks);

        add_chip(
            chip_id,
            options.chip_type,
            construct_chip_from_cluster(
                chip_id,
                options.chip_type,
                cluster_desc.get(),
                soc_desc,
                options.num_host_mem_ch_per_mmio_device,
                options.simulator_directory));
    }

    construct_cluster(options.num_host_mem_ch_per_mmio_device, options.chip_type);
}

void Cluster::configure_active_ethernet_cores_for_mmio_device(
    chip_id_t mmio_chip, const std::unordered_set<CoreCoord>& active_eth_cores_per_chip) {
    chips_.at(mmio_chip)->set_remote_transfer_ethernet_cores(active_eth_cores_per_chip);
}

std::set<chip_id_t> Cluster::get_target_device_ids() { return all_chip_ids_; }

std::set<chip_id_t> Cluster::get_target_mmio_device_ids() { return local_chip_ids_; }

std::set<chip_id_t> Cluster::get_target_remote_device_ids() { return remote_chip_ids_; }

void Cluster::assert_risc_reset() { broadcast_tensix_risc_reset_to_cluster(TENSIX_ASSERT_SOFT_RESET); }

void Cluster::deassert_risc_reset() { broadcast_tensix_risc_reset_to_cluster(TENSIX_DEASSERT_SOFT_RESET); }

void Cluster::deassert_risc_reset_at_core(
    const chip_id_t chip, const CoreCoord core, const TensixSoftResetOptions& soft_resets) {
    // Get Target Device to query soc descriptor and determine location in cluster
    TT_ASSERT(
        core.core_type == CoreType::TENSIX || core.core_type == CoreType::ETH,
        "Cannot deassert reset on a non-tensix or harvested core");
    get_chip(chip)->send_tensix_risc_reset(translate_to_api_coords(chip, core), soft_resets);
}

void Cluster::assert_risc_reset_at_core(
    const chip_id_t chip, const CoreCoord core, const TensixSoftResetOptions& soft_resets) {
    // Get Target Device to query soc descriptor and determine location in cluster
    TT_ASSERT(
        core.core_type == CoreType::TENSIX || core.core_type == CoreType::ETH,
        "Cannot assert reset on a non-tensix or harvested core");
    get_chip(chip)->send_tensix_risc_reset(translate_to_api_coords(chip, core), soft_resets);
}

tt_ClusterDescriptor* Cluster::get_cluster_description() { return cluster_desc.get(); }

std::function<void(uint32_t, uint32_t, const uint8_t*)> Cluster::get_fast_pcie_static_tlb_write_callable(
    int device_id) {
    return chips_.at(device_id)->get_fast_pcie_static_tlb_write_callable();
}

tt::Writer Cluster::get_static_tlb_writer(const chip_id_t chip, const CoreCoord target) {
    return get_tlb_manager(chip)->get_static_tlb_writer(translate_to_api_coords(chip, target));
}

int Cluster::get_clock(int logical_device_id) { return chips_.at(logical_device_id)->get_clock(); }

std::map<int, int> Cluster::get_clocks() {
    std::map<int, int> clock_freq_map;
    for (auto& chip_id : local_chip_ids_) {
        clock_freq_map.insert({chip_id, get_clock(chip_id)});
    }
    return clock_freq_map;
}

Cluster::~Cluster() {
    log_debug(LogSiliconDriver, "Cluster::~Cluster");

    cluster_desc.reset();
}

tlb_configuration Cluster::get_tlb_configuration(const chip_id_t chip, CoreCoord core) {
    return get_tlb_manager(chip)->get_tlb_configuration(translate_to_api_coords(chip, core));
}

void Cluster::configure_tlb(
    chip_id_t logical_device_id, tt_xy_pair core, int32_t tlb_index, uint64_t address, uint64_t ordering) {
    get_tlb_manager(logical_device_id)
        ->configure_tlb(
            core, translate_chip_coord_virtual_to_translated(logical_device_id, core), tlb_index, address, ordering);
}

void Cluster::configure_tlb(
    chip_id_t logical_device_id, tt::umd::CoreCoord core, int32_t tlb_index, uint64_t address, uint64_t ordering) {
    configure_tlb(logical_device_id, translate_to_api_coords(logical_device_id, core), tlb_index, address, ordering);
}

void* Cluster::host_dma_address(std::uint64_t offset, chip_id_t src_device_id, uint16_t channel) const {
    hugepage_mapping hugepage_map = get_local_chip(src_device_id)->get_sysmem_manager()->get_hugepage_mapping(channel);
    if (hugepage_map.mapping != nullptr) {
        return static_cast<std::byte*>(hugepage_map.mapping) + offset;
    } else {
        return nullptr;
    }
}

TTDevice* Cluster::get_tt_device(chip_id_t device_id) const {
    auto tt_device = get_chip(device_id)->get_tt_device();
    TT_ASSERT(tt_device != nullptr, "TTDevice not found for device: {}", device_id);
    return tt_device;
}

TLBManager* Cluster::get_tlb_manager(chip_id_t device_id) const { return get_local_chip(device_id)->get_tlb_manager(); }

Chip* Cluster::get_chip(chip_id_t device_id) const {
    auto chip_it = chips_.find(device_id);
    TT_ASSERT(chip_it != chips_.end(), "Device id {} not found in cluster.", device_id);
    return chip_it->second.get();
}

LocalChip* Cluster::get_local_chip(chip_id_t device_id) const {
    TT_ASSERT(local_chip_ids_.find(device_id) != local_chip_ids_.end(), "Device id {} is not a local chip.", device_id);
    return dynamic_cast<LocalChip*>(get_chip(device_id));
}

RemoteChip* Cluster::get_remote_chip(chip_id_t device_id) const {
    TT_ASSERT(
        remote_chip_ids_.find(device_id) != remote_chip_ids_.end(), "Device id {} is not a remote chip.", device_id);
    return dynamic_cast<RemoteChip*>(get_chip(device_id));
}

void Cluster::wait_for_non_mmio_flush(const chip_id_t chip_id) { get_chip(chip_id)->wait_for_non_mmio_flush(); }

void Cluster::wait_for_non_mmio_flush() {
    for (auto& [chip_id, chip] : chips_) {
        chip->wait_for_non_mmio_flush();
    }
}

std::unordered_map<chip_id_t, std::vector<std::vector<int>>>& Cluster::get_ethernet_broadcast_headers(
    const std::set<chip_id_t>& chips_to_exclude) {
    // Generate headers for Ethernet Broadcast (WH) only. Each header corresponds to a unique broadcast "grid".
    if (bcast_header_cache.find(chips_to_exclude) == bcast_header_cache.end()) {
        bcast_header_cache[chips_to_exclude] = {};
        std::unordered_map<chip_id_t, std::unordered_map<chip_id_t, std::vector<int>>>
            broadcast_mask_for_target_chips_per_group = {};
        std::map<std::vector<int>, std::tuple<chip_id_t, std::vector<int>>> broadcast_header_union_per_group = {};
        chip_id_t first_mmio_chip = *(get_target_mmio_device_ids().begin());
        for (const auto& chip : all_chip_ids_) {
            if (chips_to_exclude.find(chip) == chips_to_exclude.end()) {
                // Get shelf local physical chip id included in broadcast
                chip_id_t physical_chip_id = cluster_desc->get_shelf_local_physical_chip_coords(chip);
                eth_coord_t eth_coords = cluster_desc->get_chip_locations().at(chip);
                // Rack word to be set in header
                uint32_t rack_word = eth_coords.rack >> 2;
                // Rack byte to be set in header
                uint32_t rack_byte = eth_coords.rack % 4;
                // 1st level grouping: Group broadcasts based on the MMIO chip they must go through
                // Nebula + Galaxy Topology assumption: Disjoint sets can only be present in the first shelf, with each
                // set connected to host through its closest MMIO chip For the first shelf, pass broadcasts to specific
                // chips through their closest MMIO chip All other shelves are fully connected galaxy grids. These are
                // connected to all MMIO devices. Use any (or the first) MMIO device in the list.
                chip_id_t closest_mmio_chip = 0;
                if (eth_coords.rack == 0 && eth_coords.shelf == 0) {
                    // Shelf 0 + Rack 0: Either an MMIO chip or a remote chip potentially connected to host through its
                    // own MMIO counterpart.
                    closest_mmio_chip = cluster_desc->get_closest_mmio_capable_chip(chip);
                } else {
                    // All other shelves: Group these under the same/first MMIO chip, since all MMIO chips are
                    // connected.
                    closest_mmio_chip = first_mmio_chip;
                }
                if (broadcast_mask_for_target_chips_per_group.find(closest_mmio_chip) ==
                    broadcast_mask_for_target_chips_per_group.end()) {
                    broadcast_mask_for_target_chips_per_group.insert({closest_mmio_chip, {}});
                }
                // For each target physical chip id (local to a shelf), generate headers based on all racks and shelves
                // that contain this physical id.
                if (broadcast_mask_for_target_chips_per_group.at(closest_mmio_chip).find(physical_chip_id) ==
                    broadcast_mask_for_target_chips_per_group.at(closest_mmio_chip).end()) {
                    // Target seen for the first time.
                    std::vector<int> broadcast_mask(8, 0);
                    broadcast_mask.at(rack_word) |= (1 << eth_coords.shelf) << rack_byte;
                    broadcast_mask.at(3) |= 1 << physical_chip_id;
                    broadcast_mask_for_target_chips_per_group.at(closest_mmio_chip)
                        .insert({physical_chip_id, broadcast_mask});

                } else {
                    // Target was seen before -> include curr rack and shelf in header
                    broadcast_mask_for_target_chips_per_group.at(closest_mmio_chip)
                        .at(physical_chip_id)
                        .at(rack_word) |= static_cast<uint32_t>(1 << eth_coords.shelf) << rack_byte;
                }
            }
        }
        // 2nd level grouping: For each MMIO group, further group the chips based on their rack and shelf headers. The
        // number of groups after this step represent the final set of broadcast grids.
        for (auto& mmio_group : broadcast_mask_for_target_chips_per_group) {
            for (auto& chip : mmio_group.second) {
                // Generate a hash for this MMIO Chip + Rack + Shelf group
                std::vector<int> header_hash = {
                    mmio_group.first, chip.second.at(0), chip.second.at(1), chip.second.at(2)};
                if (broadcast_header_union_per_group.find(header_hash) == broadcast_header_union_per_group.end()) {
                    broadcast_header_union_per_group.insert(
                        {header_hash, std::make_tuple(mmio_group.first, chip.second)});
                } else {
                    // If group found, update chip header entry
                    std::get<1>(broadcast_header_union_per_group.at(header_hash)).at(3) |= chip.second.at(3);
                }
            }
        }
        // Get all broadcast headers per MMIO group
        for (const auto& header : broadcast_header_union_per_group) {
            chip_id_t mmio_chip = std::get<0>(header.second);
            if (bcast_header_cache[chips_to_exclude].find(mmio_chip) == bcast_header_cache[chips_to_exclude].end()) {
                bcast_header_cache[chips_to_exclude].insert({mmio_chip, {}});
            }
            bcast_header_cache[chips_to_exclude].at(mmio_chip).push_back(std::get<1>(header.second));
        }
        // Invert headers (FW convention)
        for (auto& bcast_group : bcast_header_cache[chips_to_exclude]) {
            for (auto& header : bcast_group.second) {
                int header_idx = 0;
                for (auto& header_entry : header) {
                    if (header_idx == 4) {
                        break;
                    }
                    header_entry = ~header_entry;
                    header_idx++;
                }
            }
        }
    }
    return bcast_header_cache[chips_to_exclude];
}

inline bool tensix_or_eth_in_broadcast(
    const std::set<uint32_t>& cols_to_exclude,
    const tt::umd::architecture_implementation* architecture_implementation) {
    bool found_tensix_or_eth = false;
    for (const auto& col : architecture_implementation->get_t6_x_locations()) {
        found_tensix_or_eth |= (cols_to_exclude.find(col) == cols_to_exclude.end());
    }
    return found_tensix_or_eth;
}

inline bool valid_tensix_broadcast_grid(
    const std::set<uint32_t>& rows_to_exclude,
    const std::set<uint32_t>& cols_to_exclude,
    const tt::umd::architecture_implementation* architecture_implementation) {
    bool t6_bcast_rows_complete = true;
    bool t6_bcast_rows_empty = true;

    for (const auto& row : architecture_implementation->get_t6_y_locations()) {
        t6_bcast_rows_complete &= (rows_to_exclude.find(row) == rows_to_exclude.end());
        t6_bcast_rows_empty &= (rows_to_exclude.find(row) != rows_to_exclude.end());
    }
    return t6_bcast_rows_complete || t6_bcast_rows_empty;
}

void Cluster::ethernet_broadcast_write(
    const void* mem_ptr,
    uint32_t size_in_bytes,
    uint64_t address,
    const std::set<chip_id_t>& chips_to_exclude,
    const std::set<uint32_t>& rows_to_exclude,
    std::set<uint32_t>& cols_to_exclude,
    bool use_virtual_coords) {
    if (use_ethernet_broadcast) {
        // Broadcast through ERISC core supported
        std::unordered_map<chip_id_t, std::vector<std::vector<int>>>& broadcast_headers =
            get_ethernet_broadcast_headers(chips_to_exclude);
        // Apply row and column exclusion mask explictly. Placing this here if we want to cache the higher level
        // broadcast headers on future/
        std::uint32_t row_exclusion_mask = 0;
        std::uint32_t col_exclusion_mask = 0;
        for (const auto& row : rows_to_exclude) {
            row_exclusion_mask |= 1 << row;
        }

        for (const auto& col : cols_to_exclude) {
            col_exclusion_mask |= 1 << (16 + col);
        }
        // Write broadcast block to device.
        for (auto& mmio_group : broadcast_headers) {
            for (auto& header : mmio_group.second) {
                header.at(4) = use_virtual_coords * 0x8000;  // Reset row/col exclusion masks
                header.at(4) |= row_exclusion_mask;
                header.at(4) |= col_exclusion_mask;
                get_local_chip(mmio_group.first)->ethernet_broadcast_write(mem_ptr, address, size_in_bytes, header);
            }
        }
    } else {
        // Broadcast not supported. Implement this at the software level as a for loop
        std::vector<tt_cxy_pair> cores_to_write = {};
        for (const auto& chip : all_chip_ids_) {
            if (chips_to_exclude.find(chip) != chips_to_exclude.end()) {
                continue;
            }
            for (const CoreCoord core : get_soc_descriptor(chip).get_all_cores(CoordSystem::VIRTUAL)) {
                if (cols_to_exclude.find(core.x) == cols_to_exclude.end() &&
                    rows_to_exclude.find(core.y) == rows_to_exclude.end()) {
                    write_to_device(mem_ptr, size_in_bytes, chip, core, address);
                }
            }
        }
    }
}

void Cluster::broadcast_write_to_cluster(
    const void* mem_ptr,
    uint32_t size_in_bytes,
    uint64_t address,
    const std::set<chip_id_t>& chips_to_exclude,
    std::set<uint32_t>& rows_to_exclude,
    std::set<uint32_t>& cols_to_exclude) {
    if (arch_name == tt::ARCH::BLACKHOLE) {
        auto architecture_implementation = tt::umd::architecture_implementation::create(arch_name);
        if (cols_to_exclude.find(0) == cols_to_exclude.end() or cols_to_exclude.find(9) == cols_to_exclude.end()) {
            TT_ASSERT(
                !tensix_or_eth_in_broadcast(cols_to_exclude, architecture_implementation.get()),
                "Cannot broadcast to tensix/ethernet and DRAM simultaneously on Blackhole.");
            if (cols_to_exclude.find(0) == cols_to_exclude.end()) {
                // When broadcast includes column zero do not exclude anything
                std::set<uint32_t> unsafe_rows = {};
                std::set<uint32_t> cols_to_exclude_for_col_0_bcast = cols_to_exclude;
                std::set<uint32_t> rows_to_exclude_for_col_0_bcast = rows_to_exclude;
                cols_to_exclude_for_col_0_bcast.insert(9);
                rows_to_exclude_for_col_0_bcast.insert(unsafe_rows.begin(), unsafe_rows.end());
                ethernet_broadcast_write(
                    mem_ptr,
                    size_in_bytes,
                    address,
                    chips_to_exclude,
                    rows_to_exclude_for_col_0_bcast,
                    cols_to_exclude_for_col_0_bcast,
                    false);
            }
            if (cols_to_exclude.find(9) == cols_to_exclude.end()) {
                std::set<uint32_t> cols_to_exclude_for_col_9_bcast = cols_to_exclude;
                cols_to_exclude_for_col_9_bcast.insert(0);
                ethernet_broadcast_write(
                    mem_ptr,
                    size_in_bytes,
                    address,
                    chips_to_exclude,
                    rows_to_exclude,
                    cols_to_exclude_for_col_9_bcast,
                    false);
            }
        } else {
            TT_ASSERT(
                use_virtual_coords_for_eth_broadcast or
                    valid_tensix_broadcast_grid(rows_to_exclude, cols_to_exclude, architecture_implementation.get()),
                "Must broadcast to all tensix rows when ERISC FW is < 6.8.0.");
            ethernet_broadcast_write(
                mem_ptr,
                size_in_bytes,
                address,
                chips_to_exclude,
                rows_to_exclude,
                cols_to_exclude,
                use_virtual_coords_for_eth_broadcast);
        }
    } else {
        auto architecture_implementation = tt::umd::architecture_implementation::create(arch_name);
        if (cols_to_exclude.find(0) == cols_to_exclude.end() or cols_to_exclude.find(5) == cols_to_exclude.end()) {
            TT_ASSERT(
                !tensix_or_eth_in_broadcast(cols_to_exclude, architecture_implementation.get()),
                "Cannot broadcast to tensix/ethernet and DRAM simultaneously on Wormhole.");
            if (cols_to_exclude.find(0) == cols_to_exclude.end()) {
                // When broadcast includes column zero Exclude PCIe, ARC and router cores from broadcast explictly,
                // since writing to these is unsafe ERISC FW does not exclude these.
                std::set<uint32_t> unsafe_rows = {2, 3, 4, 8, 9, 10};
                std::set<uint32_t> cols_to_exclude_for_col_0_bcast = cols_to_exclude;
                std::set<uint32_t> rows_to_exclude_for_col_0_bcast = rows_to_exclude;
                cols_to_exclude_for_col_0_bcast.insert(5);
                rows_to_exclude_for_col_0_bcast.insert(unsafe_rows.begin(), unsafe_rows.end());
                ethernet_broadcast_write(
                    mem_ptr,
                    size_in_bytes,
                    address,
                    chips_to_exclude,
                    rows_to_exclude_for_col_0_bcast,
                    cols_to_exclude_for_col_0_bcast,
                    false);
            }
            if (cols_to_exclude.find(5) == cols_to_exclude.end()) {
                std::set<uint32_t> cols_to_exclude_for_col_5_bcast = cols_to_exclude;
                cols_to_exclude_for_col_5_bcast.insert(0);
                ethernet_broadcast_write(
                    mem_ptr,
                    size_in_bytes,
                    address,
                    chips_to_exclude,
                    rows_to_exclude,
                    cols_to_exclude_for_col_5_bcast,
                    false);
            }
        } else {
            TT_ASSERT(
                use_virtual_coords_for_eth_broadcast or
                    valid_tensix_broadcast_grid(rows_to_exclude, cols_to_exclude, architecture_implementation.get()),
                "Must broadcast to all tensix rows when ERISC FW is < 6.8.0.");
            ethernet_broadcast_write(
                mem_ptr,
                size_in_bytes,
                address,
                chips_to_exclude,
                rows_to_exclude,
                cols_to_exclude,
                use_virtual_coords_for_eth_broadcast);
        }
    }
}

void Cluster::write_to_sysmem(
    const void* mem_ptr, std::uint32_t size, uint64_t addr, uint16_t channel, chip_id_t src_device_id) {
    get_local_chip(src_device_id)->write_to_sysmem(channel, mem_ptr, addr, size);
}

void Cluster::read_from_sysmem(void* mem_ptr, uint64_t addr, uint16_t channel, uint32_t size, chip_id_t src_device_id) {
    get_local_chip(src_device_id)->read_from_sysmem(channel, mem_ptr, addr, size);
}

void Cluster::l1_membar(const chip_id_t chip, const std::unordered_set<tt::umd::CoreCoord>& cores) {
    get_chip(chip)->l1_membar(cores);
}

void Cluster::dram_membar(const chip_id_t chip, const std::unordered_set<tt::umd::CoreCoord>& cores) {
    get_chip(chip)->dram_membar(cores);
}

void Cluster::dram_membar(const chip_id_t chip, const std::unordered_set<uint32_t>& channels) {
    get_chip(chip)->dram_membar(channels);
}

void Cluster::write_to_device(
    const void* mem_ptr, uint32_t size_in_bytes, chip_id_t chip, CoreCoord core, uint64_t addr) {
    get_chip(chip)->write_to_device(translate_to_api_coords(chip, core), mem_ptr, addr, size_in_bytes);
}

void Cluster::write_to_device_reg(
    const void* mem_ptr, uint32_t size_in_bytes, chip_id_t chip, CoreCoord core, uint64_t addr) {
    get_chip(chip)->write_to_device_reg(translate_to_api_coords(chip, core), mem_ptr, addr, size_in_bytes);
}

void Cluster::dma_write_to_device(
    const void* src, size_t size, chip_id_t chip, tt::umd::CoreCoord core, uint64_t addr) {
    auto api_coords = translate_to_api_coords(chip, core);
    get_chip(chip)->dma_write_to_device(src, size, api_coords, addr);
}

void Cluster::dma_read_from_device(void* dst, size_t size, chip_id_t chip, tt::umd::CoreCoord core, uint64_t addr) {
    auto api_coords = translate_to_api_coords(chip, core);
    get_chip(chip)->dma_read_from_device(dst, size, api_coords, addr);
}

void Cluster::read_from_device(void* mem_ptr, chip_id_t chip, CoreCoord core, uint64_t addr, uint32_t size) {
    get_chip(chip)->read_from_device(translate_to_api_coords(chip, core), mem_ptr, addr, size);
}

void Cluster::read_from_device_reg(void* mem_ptr, chip_id_t chip, CoreCoord core, uint64_t addr, uint32_t size) {
    get_chip(chip)->read_from_device_reg(translate_to_api_coords(chip, core), mem_ptr, addr, size);
}

int Cluster::arc_msg(
    int logical_device_id,
    uint32_t msg_code,
    bool wait_for_done,
    uint32_t arg0,
    uint32_t arg1,
    uint32_t timeout_ms,
    uint32_t* return_3,
    uint32_t* return_4) {
    return get_chip(logical_device_id)->arc_msg(msg_code, wait_for_done, arg0, arg1, timeout_ms, return_3, return_4);
}

void Cluster::broadcast_tensix_risc_reset_to_cluster(const TensixSoftResetOptions& soft_resets) {
    if (chips_.empty()) {
        // Nowhere to broadcast to.
        return;
    }
    // If ethernet broadcast is not supported, do it one by one.
    if (!use_ethernet_broadcast) {
        for (auto& chip_id : all_chip_ids_) {
            get_chip(chip_id)->send_tensix_risc_reset(soft_resets);
        }
        return;
    }

    auto valid = soft_resets & ALL_TENSIX_SOFT_RESET;
    uint32_t valid_val = (std::underlying_type<TensixSoftResetOptions>::type)valid;
    std::set<chip_id_t> chips_to_exclude = {};
    std::set<uint32_t> rows_to_exclude;
    std::set<uint32_t> columns_to_exclude;
    if (arch_name == tt::ARCH::BLACKHOLE) {
        rows_to_exclude = {0, 1};
        columns_to_exclude = {0, 8, 9};
    } else {
        rows_to_exclude = {0, 6};
        columns_to_exclude = {0, 5};
    }
    broadcast_write_to_cluster(
        &valid_val, sizeof(uint32_t), 0xFFB121B0, chips_to_exclude, rows_to_exclude, columns_to_exclude);
    // Ensure that reset signal is globally visible
    wait_for_non_mmio_flush();
}

void Cluster::set_power_state(tt_DevicePowerState device_state) {
    for (auto& [_, chip] : chips_) {
        chip->set_power_state(device_state);
    }
}

void Cluster::enable_ethernet_queue(int timeout) {
    for (const chip_id_t& chip : all_chip_ids_) {
        get_chip(chip)->enable_ethernet_queue(timeout);
    }
}

void Cluster::deassert_resets_and_set_power_state() {
    // Assert tensix resets on all chips in cluster
    broadcast_tensix_risc_reset_to_cluster(TENSIX_ASSERT_SOFT_RESET);

    for (auto& [_, chip] : chips_) {
        chip->deassert_risc_resets();
    }

    // MT Initial BH - ARC messages not supported in Blackhole
    if (arch_name != tt::ARCH::BLACKHOLE) {
        enable_ethernet_queue(30);
    }

    // Set power state to busy
    set_power_state(tt_DevicePowerState::BUSY);
}

void Cluster::verify_eth_fw() {
    for (const auto& chip : all_chip_ids_) {
        uint32_t fw_version;
        std::vector<uint32_t> fw_versions;
        for (const CoreCoord eth_core : get_soc_descriptor(chip).get_cores(CoreType::ETH)) {
            read_from_device(
                &fw_version, chip, eth_core, get_chip(chip)->l1_address_params.fw_version_addr, sizeof(uint32_t));
            fw_versions.push_back(fw_version);
        }
        verify_sw_fw_versions(chip, SW_VERSION, fw_versions);
        eth_fw_version = fw_versions.empty() ? tt_version() : tt_version(fw_versions.at(0));
    }
}

void Cluster::verify_sw_fw_versions(int device_id, std::uint32_t sw_version, std::vector<std::uint32_t>& fw_versions) {
    if (fw_versions.empty()) {
        log_debug(
            LogSiliconDriver,
            "No ethernet cores found on device {}, skipped verification of software and firmware versions.",
            device_id);
        return;
    }
    tt_version sw(sw_version), fw_first_eth_core(fw_versions.at(0));
    log_info(
        LogSiliconDriver,
        "Software version {}, Ethernet FW version {} (Device {})",
        sw.str(),
        fw_first_eth_core.str(),
        device_id);
    for (std::uint32_t& fw_version : fw_versions) {
        tt_version fw(fw_version);
        TT_ASSERT(fw == fw_first_eth_core, "FW versions are not the same across different ethernet cores");
        TT_ASSERT(sw.major == fw.major, "SW/FW major version number out of sync");
        TT_ASSERT(sw.minor <= fw.minor, "SW version is newer than FW version");
    }

    // Min ERISC FW version required to support ethernet broadcast is 6.5.0.
    use_ethernet_broadcast &= fw_first_eth_core >= tt_version(6, 5, 0);
    // Virtual coordinates can be used for broadcast headers if ERISC FW >= 6.8.0 and NOC translation is enabled
    // Temporarily enable this feature for 6.7.241 as well for testing.
    use_virtual_coords_for_eth_broadcast &=
        (fw_first_eth_core >= tt_version(6, 8, 0) || fw_first_eth_core == tt_version(6, 7, 241)) &&
        get_soc_descriptor(device_id).noc_translation_enabled;
}

void Cluster::start_device(const tt_device_params& device_params) {
    if (device_params.init_device) {
        for (auto chip_id : all_chip_ids_) {
            get_chip(chip_id)->start_device();
        }

        // MT Initial BH - Ethernet firmware not present in Blackhole
        if (arch_name == tt::ARCH::WORMHOLE_B0) {
            verify_eth_fw();
        }
        deassert_resets_and_set_power_state();
    }
}

void Cluster::close_device() {
    for (auto chip_id : all_chip_ids_) {
        get_chip(chip_id)->close_device();
    }
    set_power_state(tt_DevicePowerState::LONG_IDLE);
    broadcast_tensix_risc_reset_to_cluster(TENSIX_ASSERT_SOFT_RESET);
}

std::uint32_t Cluster::get_num_host_channels(std::uint32_t device_id) {
    return chips_.at(device_id)->get_num_host_channels();
}

std::uint32_t Cluster::get_host_channel_size(std::uint32_t device_id, std::uint32_t channel) {
    return chips_.at(device_id)->get_host_channel_size(channel);
}

std::uint32_t Cluster::get_numa_node_for_pcie_device(std::uint32_t device_id) {
    return chips_.at(device_id)->get_numa_node();
}

std::uint64_t Cluster::get_pcie_base_addr_from_device(const chip_id_t chip_id) const {
    // TODO: Should probably be lowered to TTDevice.
    tt::ARCH arch = get_soc_descriptor(chip_id).arch;
    if (arch == tt::ARCH::WORMHOLE_B0) {
        return 0x800000000;
    } else if (arch == tt::ARCH::BLACKHOLE) {
        // Enable 4th ATU window.
        return 1ULL << 60;
    } else {
        return 0;
    }
}

tt_version Cluster::get_ethernet_fw_version() const {
    TT_ASSERT(arch_name == tt::ARCH::WORMHOLE_B0, "Can only get Ethernet FW version for Wormhole architectures.");
    TT_ASSERT(
        eth_fw_version.major != 0xffff and eth_fw_version.minor != 0xff and eth_fw_version.patch != 0xff,
        "Device must be started before querying Ethernet FW version.");
    return eth_fw_version;
}

void Cluster::set_barrier_address_params(const barrier_address_params& barrier_address_params_) {
    for (auto& [_, chip] : chips_) {
        chip->set_barrier_address_params(barrier_address_params_);
    }
}

// TODO: This is a temporary function while we're switching between the old and the new API.
// Eventually, this function should be so small it would be obvioud to remove.
tt_xy_pair Cluster::translate_to_api_coords(const chip_id_t chip, const tt::umd::CoreCoord core_coord) const {
    return get_soc_descriptor(chip).translate_coord_to(core_coord, CoordSystem::VIRTUAL);
}

tt_xy_pair Cluster::translate_chip_coord_virtual_to_translated(const chip_id_t chip_id, const tt_xy_pair core) const {
    CoreCoord core_coord = get_soc_descriptor(chip_id).get_coord_at(core, CoordSystem::VIRTUAL);
    // Since NOC1 and translated coordinate space overlaps for Tensix cores on Blackhole,
    // Tensix cores are always used in translated space. Other cores are used either in
    // NOC1 or translated space depending on the umd_use_noc1 flag.
    // On Wormhole Tensix can use NOC1 space if umd_use_noc1 is set to true.
    if (get_soc_descriptor(chip_id).noc_translation_enabled) {
        if (get_soc_descriptor(chip_id).arch == tt::ARCH::BLACKHOLE) {
            if (core_coord.core_type == CoreType::TENSIX || !umd_use_noc1) {
                return get_soc_descriptor(chip_id).translate_coord_to(core_coord, CoordSystem::TRANSLATED);
            } else {
                return get_soc_descriptor(chip_id).translate_coord_to(core_coord, CoordSystem::NOC1);
            }
        } else {
            return get_soc_descriptor(chip_id).translate_coord_to(
                core_coord, umd_use_noc1 ? CoordSystem::NOC1 : CoordSystem::TRANSLATED);
        }
    } else {
        return get_soc_descriptor(chip_id).translate_coord_to(
            core_coord, umd_use_noc1 ? CoordSystem::NOC1 : CoordSystem::TRANSLATED);
    }
}

std::unique_ptr<tt_ClusterDescriptor> Cluster::create_cluster_descriptor(
    std::string sdesc_path, std::unordered_set<chip_id_t> pci_target_devices) {
    std::map<int, PciDeviceInfo> pci_device_info = PCIDevice::enumerate_devices_info();
    if (pci_device_info.begin()->second.get_arch() == tt::ARCH::BLACKHOLE) {
        std::vector<int> pci_device_ids = PCIDevice::enumerate_devices();

        std::unordered_map<chip_id_t, std::unique_ptr<Chip>> chips;
        chip_id_t chip_id = 0;
        for (auto& device_id : pci_device_ids) {
            std::unique_ptr<LocalChip> chip = nullptr;
            if (sdesc_path.empty()) {
                chip = std::make_unique<LocalChip>(TTDevice::create(device_id));
            } else {
                chip = std::make_unique<LocalChip>(sdesc_path, TTDevice::create(device_id));
            }
            chips.emplace(chip_id, std::move(chip));
            chip_id++;
        }

        return Cluster::create_cluster_descriptor(chips);
    } else {
        std::vector<int> pci_device_ids = PCIDevice::enumerate_devices();

        std::vector<std::unique_ptr<TTDevice>> tt_devices;
        for (auto& device_id : pci_device_ids) {
            std::unique_ptr<TTDevice> tt_device = TTDevice::create(device_id);
            tt_devices.push_back(std::move(tt_device));
        }

        // Topology discovery from source is supported for Wormhole UBB at the moment,
        // other Wormhole specs need to go through a legacy create-ethernet-map.
        if (!tt_devices.empty() && tt_devices[0]->get_board_type() != BoardType::UBB) {
            return TopologyDiscovery(pci_target_devices).create_ethernet_map();
        }

        std::unordered_map<chip_id_t, std::unique_ptr<Chip>> chips;
        chip_id_t chip_id = 0;
        for (auto& device_id : pci_device_ids) {
            std::unique_ptr<LocalChip> chip = nullptr;
            if (sdesc_path.empty()) {
                chip = std::make_unique<LocalChip>(TTDevice::create(device_id));
            } else {
                chip = std::make_unique<LocalChip>(sdesc_path, TTDevice::create(device_id));
            }
            chips.emplace(chip_id, std::move(chip));
            chip_id++;
        }

        return Cluster::create_cluster_descriptor(chips);
    }
}

std::unique_ptr<tt_ClusterDescriptor> Cluster::create_cluster_descriptor(
    const std::unordered_map<chip_id_t, std::unique_ptr<tt::umd::Chip>>& chips) {
    std::unique_ptr<tt_ClusterDescriptor> desc = std::unique_ptr<tt_ClusterDescriptor>(new tt_ClusterDescriptor());

    if (chips.empty()) {
        return desc;
    }

    for (auto& it : chips) {
        const chip_id_t chip_id = it.first;
        const std::unique_ptr<Chip>& chip = it.second;

        // TODO: Use the line below when we can read asic location from the Blackhole telemetry.
        // Until then we have to read it from ETH core.
        // desc->add_chip_uid(chip_id, chip->get_chip_info().chip_uid);

        // TODO: Remove this when we can read asic location from the Blackhole telemetry.
        // Until then we have to read it from ETH core.
        const std::vector<CoreCoord> eth_cores = chip->get_soc_descriptor().get_cores(CoreType::ETH);
        for (size_t eth_channel = 0; eth_channel < eth_cores.size(); eth_channel++) {
            const CoreCoord& eth_core = eth_cores[eth_channel];
            TTDevice* tt_device = chip->get_tt_device();
            blackhole::boot_results_t boot_results;

            tt_device->read_from_device(
                (uint8_t*)&boot_results,
                tt_xy_pair(eth_core.x, eth_core.y),
                blackhole::BOOT_RESULTS_ADDR,
                sizeof(boot_results));

            // We can read the asic location only from active ETH cores.
            if (boot_results.eth_status.port_status == blackhole::port_status_e::PORT_UP) {
                const blackhole::chip_info_t& local_info = boot_results.local_info;
                desc->add_chip_uid(chip_id, ChipUID{chip->get_chip_info().chip_uid.board_id, local_info.asic_location});
            }
        }
    }

    for (auto& it : chips) {
        const chip_id_t chip_id = it.first;
        const std::unique_ptr<Chip>& chip = it.second;

        desc->all_chips.insert(chip_id);
        desc->chip_arch.insert({chip_id, chip->get_tt_device()->get_arch()});

        desc->chips_with_mmio.insert({chip_id, chip->get_tt_device()->get_pci_device()->get_device_num()});

        desc->chip_board_type.insert({chip_id, chip->get_chip_info().board_type});

        desc->noc_translation_enabled.insert({chip_id, chip->get_chip_info().noc_translation_enabled});
        desc->harvesting_masks.insert({chip_id, chip->get_chip_info().harvesting_masks.tensix_harvesting_mask});
        desc->dram_harvesting_masks.insert({chip_id, chip->get_chip_info().harvesting_masks.dram_harvesting_mask});
        desc->eth_harvesting_masks.insert({chip_id, chip->get_chip_info().harvesting_masks.eth_harvesting_mask});
        desc->pcie_harvesting_masks.insert({chip_id, chip->get_chip_info().harvesting_masks.pcie_harvesting_mask});

        desc->add_chip_to_board(chip_id, chip->get_chip_info().chip_uid.board_id);
    }

    if (chips.begin()->second->get_tt_device()->get_arch() == tt::ARCH::BLACKHOLE) {
        for (auto& it : chips) {
            const chip_id_t chip_id = it.first;
            const std::unique_ptr<Chip>& chip = it.second;

            const std::vector<CoreCoord> eth_cores = chip->get_soc_descriptor().get_cores(CoreType::ETH);

            for (size_t eth_channel = 0; eth_channel < eth_cores.size(); eth_channel++) {
                const CoreCoord& eth_core = eth_cores[eth_channel];
                TTDevice* tt_device = chip->get_tt_device();
                blackhole::boot_results_t boot_results;

                tt_device->read_from_device(
                    (uint8_t*)&boot_results,
                    tt_xy_pair(eth_core.x, eth_core.y),
                    blackhole::BOOT_RESULTS_ADDR,
                    sizeof(boot_results));

                if (boot_results.eth_status.port_status == blackhole::port_status_e::PORT_UP) {
                    // active eth core
                    desc->active_eth_channels[chip_id].insert(eth_channel);
                    log_debug(
                        LogSiliconDriver, "Eth core ({}, {}) on chip {} is active", eth_core.x, eth_core.y, chip_id);
                    const blackhole::chip_info_t& local_info = boot_results.local_info;
                    const blackhole::chip_info_t& remote_info = boot_results.remote_info;

                    chip_id_t local_chip_id = desc->get_chip_id(local_info.get_chip_uid()).value();
                    std::optional<chip_id_t> remote_chip_id = desc->get_chip_id(remote_info.get_chip_uid());
                    if (!remote_chip_id.has_value()) {
                        log_debug(
                            LogSiliconDriver,
                            "Eth core ({}, {}) on chip {} is connected to an chip with board_id {} not present in the "
                            "target devices opened by this driver.",
                            eth_core.x,
                            eth_core.y,
                            chip_id,
                            remote_info.get_chip_uid().board_id);
                    } else {
                        const CoreCoord logical_remote_coord = chips.at(remote_chip_id.value())
                                                                   ->get_soc_descriptor()
                                                                   .translate_coord_to(
                                                                       blackhole::ETH_CORES_NOC0[remote_info.eth_id],
                                                                       CoordSystem::PHYSICAL,
                                                                       CoordSystem::LOGICAL);
                        // Adding a connection only one way, the other chip should add it another way.
                        desc->ethernet_connections[local_chip_id][eth_channel] = {
                            remote_chip_id.value(), logical_remote_coord.y};
                    }
                } else if (boot_results.eth_status.port_status == blackhole::port_status_e::PORT_DOWN) {
                    // active eth core, just with link being down.
                    desc->active_eth_channels[chip_id].insert(eth_channel);
                    log_debug(
                        LogSiliconDriver,
                        "Port on eth core ({}, {}) on chip {} is down",
                        eth_core.x,
                        eth_core.y,
                        chip_id);
                } else if (boot_results.eth_status.port_status == blackhole::port_status_e::PORT_UNUSED) {
                    // idle core
                    desc->idle_eth_channels[chip_id].insert(eth_channel);
                    log_debug(
                        LogSiliconDriver, "Eth core ({}, {}) on chip {} is idle", eth_core.x, eth_core.y, chip_id);
                } else if (boot_results.eth_status.port_status == blackhole::port_status_e::PORT_UNKNOWN) {
                    log_debug(
                        LogSiliconDriver,
                        "Port on eth core ({}, {}) on chip {} is in unknown state",
                        eth_core.x,
                        eth_core.y,
                        chip_id);
                }
            }
        }
    } else {
        ubb_eth_connections(chips, desc);
    }

    desc->fill_chips_grouped_by_closest_mmio();

    return desc;
}

}  // namespace tt::umd

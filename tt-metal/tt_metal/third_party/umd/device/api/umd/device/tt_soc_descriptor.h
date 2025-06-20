/*
 * SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include <cstddef>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <unordered_map>
#include <vector>

#include "fmt/core.h"
#include "tt_xy_pair.h"
#include "umd/device/coordinate_manager.h"
#include "umd/device/tt_core_coordinates.h"
#include "umd/device/tt_xy_pair.h"
#include "umd/device/types/arch.h"
#include "umd/device/types/cluster_descriptor_types.h"

namespace YAML {
class Node;
}

std::string format_node(tt_xy_pair xy);

tt_xy_pair format_node(std::string str);

//! SocNodeDescriptor contains information regarding the Node/Core
/*!
    Should only contain relevant configuration for SOC
*/
struct CoreDescriptor {
    tt_xy_pair coord = tt_xy_pair(0, 0);
    CoreType type;

    std::size_t l1_size = 0;
};

struct SocDescriptorInfo {
    tt::ARCH arch;
    tt_xy_pair grid_size;
    std::vector<tt_xy_pair> tensix_cores;
    std::vector<std::vector<tt_xy_pair>> dram_cores;
    std::vector<tt_xy_pair> eth_cores;
    std::vector<tt_xy_pair> arc_cores;
    std::vector<tt_xy_pair> pcie_cores;
    std::vector<tt_xy_pair> router_cores;
    std::vector<tt_xy_pair> security_cores;
    std::vector<tt_xy_pair> l2cpu_cores;
    uint32_t worker_l1_size;
    uint32_t eth_l1_size;
    uint64_t dram_bank_size;
    std::vector<uint32_t> noc0_x_to_noc1_x;
    std::vector<uint32_t> noc0_y_to_noc1_y;
};

//! tt_SocDescriptor contains information regarding the SOC configuration targetted.
/*!
    Should only contain relevant configuration for SOC
*/
class tt_SocDescriptor {
public:
    // Default constructor. Creates uninitialized object with public access to all of its attributes.
    tt_SocDescriptor() = default;
    // Constructor used to build object from device descriptor file.
    tt_SocDescriptor(
        std::string device_descriptor_path,
        const bool noc_translation_enabled,
        const tt::umd::HarvestingMasks harvesting_masks = {0, 0, 0},
        const BoardType board_type = BoardType::UNKNOWN,
        const uint8_t asic_location = 0);

    tt_SocDescriptor(
        const tt::ARCH arch,
        const bool noc_translation_enabled,
        const tt::umd::HarvestingMasks harvesting_masks = {0, 0, 0},
        const BoardType board_type = BoardType::UNKNOWN,
        const uint8_t asic_location = 0);

    // CoreCoord conversions.
    tt::umd::CoreCoord translate_coord_to(const tt::umd::CoreCoord core_coord, const CoordSystem coord_system) const;
    tt::umd::CoreCoord get_coord_at(const tt_xy_pair core, const CoordSystem coord_system) const;
    tt::umd::CoreCoord translate_coord_to(
        const tt_xy_pair core_location,
        const CoordSystem input_coord_system,
        const CoordSystem target_coord_system) const;

    static std::string get_soc_descriptor_path(tt::ARCH arch);

    std::vector<tt::umd::CoreCoord> get_cores(
        const CoreType core_type, const CoordSystem coord_system = CoordSystem::PHYSICAL) const;
    std::vector<tt::umd::CoreCoord> get_harvested_cores(
        const CoreType core_type, const CoordSystem coord_system = CoordSystem::PHYSICAL) const;
    std::vector<tt::umd::CoreCoord> get_all_cores(const CoordSystem coord_system = CoordSystem::PHYSICAL) const;
    std::vector<tt::umd::CoreCoord> get_all_harvested_cores(
        const CoordSystem coord_system = CoordSystem::PHYSICAL) const;

    tt_xy_pair get_grid_size(const CoreType core_type) const;
    tt_xy_pair get_harvested_grid_size(const CoreType core_type) const;

    std::vector<std::vector<tt::umd::CoreCoord>> get_dram_cores() const;
    std::vector<std::vector<tt::umd::CoreCoord>> get_harvested_dram_cores() const;

    int get_num_dram_channels() const;

    uint32_t get_num_eth_channels() const;
    uint32_t get_num_harvested_eth_channels() const;

    // LOGICAL coordinates for DRAM and ETH are tightly coupled with channels, so this code is very similar to what
    // would translate_coord_to do for a coord with LOGICAL coords.
    tt::umd::CoreCoord get_dram_core_for_channel(
        int dram_chan, int subchannel, const CoordSystem coord_system = CoordSystem::PHYSICAL) const;
    tt::umd::CoreCoord get_eth_core_for_channel(
        int eth_chan, const CoordSystem coord_system = CoordSystem::PHYSICAL) const;

    tt::ARCH arch;
    tt_xy_pair grid_size;
    std::vector<std::size_t> trisc_sizes;  // Most of software stack assumes same trisc size for whole chip..
    std::string device_descriptor_file_path = std::string("");

    int overlay_version;
    int unpacker_version;
    int dst_size_alignment;
    int packer_version;
    int worker_l1_size;
    int eth_l1_size;
    uint64_t dram_bank_size;

    // Passed through constructor.
    bool noc_translation_enabled;

    // Harvesting mask is reported in logical coordinates, meaning the index of a bit that is set corresponds to the
    // index of the TENSIX row (Wormhole) or column (Blackhole), or the index of the DRAM channel, or the index of the
    // ETH channel as reported in the soc descriptor. Examples:
    //   - Tensix harvesting mask "2" would mean the second row/column from soc descriptor is harvested, and not
    //     NOC0 row.
    //   - Eth harvesting mask "2" would mean that the second core in eth_cores in soc descriptor is harvested, which
    //     is the same one that would be reported as channel 1 and would have logical coords (0, 1). This mask doesn't
    //     mean that the second core in NOC0 chain is harvested.
    tt::umd::HarvestingMasks harvesting_masks;

private:
    void create_coordinate_manager(const BoardType board_type, const uint8_t asic_location);
    void get_cores_and_grid_size_from_coordinate_manager();
    void load_from_yaml(YAML::Node &device_descriptor_yaml);
    void load_from_soc_desc_info(const SocDescriptorInfo &soc_desc_info);
    void load_core_descriptors_from_soc_desc_info(const SocDescriptorInfo &soc_desc_info);
    void load_soc_features_from_soc_desc_info(const SocDescriptorInfo &soc_desc_info);

    static std::vector<tt_xy_pair> convert_to_tt_xy_pair(const std::vector<std::string> &core_strings);
    static std::vector<std::vector<tt_xy_pair>> convert_dram_cores_from_yaml(YAML::Node &device_descriptor_yaml);

    static SocDescriptorInfo get_soc_descriptor_info(tt::ARCH arch);

    static tt_xy_pair calculate_grid_size(const std::vector<tt_xy_pair> &cores);
    std::vector<tt::umd::CoreCoord> translate_coordinates(
        const std::vector<tt::umd::CoreCoord> &physical_cores, const CoordSystem coord_system) const;

    // Internal structures, read from yaml.
    tt_xy_pair worker_grid_size;
    std::unordered_map<tt_xy_pair, CoreDescriptor> cores;
    std::vector<tt_xy_pair> arc_cores;
    std::vector<tt_xy_pair> workers;
    std::vector<tt_xy_pair> harvested_workers;
    std::vector<tt_xy_pair> pcie_cores;
    std::vector<std::vector<tt_xy_pair>> dram_cores;                             // per channel list of dram cores
    std::unordered_map<tt_xy_pair, std::tuple<int, int>> dram_core_channel_map;  // map dram core to chan/subchan
    std::vector<tt_xy_pair> ethernet_cores;                                      // ethernet cores (index == channel id)
    std::unordered_map<tt_xy_pair, int> ethernet_core_channel_map;
    std::vector<tt_xy_pair> router_cores;
    std::vector<tt_xy_pair> security_cores;
    std::vector<tt_xy_pair> l2cpu_cores;
    std::vector<uint32_t> noc0_x_to_noc1_x;
    std::vector<uint32_t> noc0_y_to_noc1_y;

    // TODO: change this to unique pointer as soon as copying of tt_SocDescriptor
    // is not needed anymore. Soc descriptor and coordinate manager should be
    // created once per chip.
    std::shared_ptr<CoordinateManager> coordinate_manager = nullptr;
    std::map<CoreType, std::vector<tt::umd::CoreCoord>> cores_map;
    std::map<CoreType, tt_xy_pair> grid_size_map;
    std::map<CoreType, std::vector<tt::umd::CoreCoord>> harvested_cores_map;
    std::map<CoreType, tt_xy_pair> harvested_grid_size_map;

    // DRAM cores are kept in additional vector struct since one DRAM bank
    // has multiple NOC endpoints, so some UMD clients prefer vector of vectors returned.
    std::vector<std::vector<tt::umd::CoreCoord>> dram_cores_core_coord;
    std::vector<std::vector<tt::umd::CoreCoord>> harvested_dram_cores_core_coord;
};

// Allocates a new soc descriptor on the heap. Returns an owning pointer.
// std::unique_ptr<tt_SocDescriptor> load_soc_descriptor_from_yaml(std::string device_descriptor_file_path);

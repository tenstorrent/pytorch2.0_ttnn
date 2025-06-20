/*
 * SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once
#include <cassert>
#include <cstdint>
#include <filesystem>
#include <memory>
#include <set>
#include <stdexcept>
#include <string>
#include <string_view>
#include <unordered_set>
#include <vector>

#include "fmt/core.h"
#include "tt_silicon_driver_common.hpp"
#include "umd/device/chip/chip.h"
#include "umd/device/tt_cluster_descriptor.h"
#include "umd/device/tt_device/tt_device.h"
#include "umd/device/tt_io.hpp"
#include "umd/device/types/arch.h"
#include "umd/device/types/cluster_descriptor_types.h"
#include "umd/device/types/cluster_types.h"
#include "umd/device/types/tlb.h"

using TLB_DATA = tt::umd::tlb_data;

class tt_ClusterDescriptor;

namespace tt::umd {

class LocalChip;
class RemoteChip;

// Chip type to create under the Cluster class.
//  - Silicon means that the chips under cluster will be connected to actual physical devices connected to the system.
//  - Simulation is used for simulation runs.
//  - Mock is used for testing purposes, implementation of all functions is empty.
enum ChipType {
    SILICON,
    SIMULATION,
    MOCK,
};

// All options when creating a Cluster object.
// Each of the options provides a default value, so in general any combination of overridden options can be used when
// constructing Cluster objects. Having this struct saves us from having a lot of different constructor overloads.
struct ClusterOptions {
    // Chip type to create.
    ChipType chip_type = ChipType::SILICON;
    // Number of host memory channels (hugepages) per MMIO device.
    uint32_t num_host_mem_ch_per_mmio_device = 1;
    // If set to false, harvesting will be skipped for constructed soc descriptors.
    bool perform_harvesting = true;
    // simulated_harvesting_masks is applied on all chips, then additionally simulated_harvesting_masks_per_chip for
    // each chip. This way, both scenarios are supported: using the simulated masks without knowing device ids and
    // setting specific simulated masks per device.
    HarvestingMasks simulated_harvesting_masks = {};
    std::unordered_map<chip_id_t, HarvestingMasks> simulated_harvesting_masks_per_chip = {};
    // If set, this soc descriptor will be used to construct devices on this cluster. If not set, the default soc
    // descriptor based on architecture will be used.
    std::string sdesc_path = "";
    // If not set, all discovered target devices will be used. If set, in case of SILICON chip type, the target devices
    // will be checked against the cluster descriptor. In case of MOCK and SIMULATION chip types, this check will be
    // skipped, and you can create chips regardless of the devices on the system.
    std::unordered_set<chip_id_t> target_devices = {};
    // If set, Cluster will target only boards that have the IDs of the chips specified in this set.
    // If not set, all discovered PCI devices will be used. This can only be used with SILICON chip type.
    // Corner case of setting this is if we have multiple chips visible over PCIE on same boards. If at least one
    // of the PCIE chips on certain board is specified, UMD will take all chips from the board.
    std::unordered_set<chip_id_t> pci_target_devices = {};
    // If not passed, topology discovery will be ran and tt_ClusterDescriptor will be constructed. If passed, and chip
    // type is SILICON, the constructor will throw if cluster_descriptor configuration shows chips which don't exist on
    // the system.
    tt_ClusterDescriptor* cluster_descriptor = nullptr;
    // This parameter is used only for SIMULATION chip type.
    std::filesystem::path simulator_directory = "";
};

/**
 * Cluster class should be used as a main interface to our devices. Devices can be created in isolation using Chip
 * class. In addition to constructing devices and initializing them, this class provides topology discovery
 * capabilities, ways to communicate to more than one device, etc.
 */
class Cluster {
public:
    /**
     * The constructor of the derived tt_device should perform everything important for initializing the device
     * properly. This can include, but is not limited to:
     * - Getting the base address for the Device which is to be used when accessing it through the API, including memory
     * mapping the device address space.
     * - Setting up security access (if any).
     * - Establishing a link to the kernel module driver (if any).
     * - Additional setup needed for read/write operation from the device. DMA setup (if any).
     * - Allocating system memory that the device has access to.
     * - Setup access to DRAM module.
     * - Create SoCDescriptors from passed custom soc descriptor yaml path.
     * - Perform this for each of the chips connected to the system.
     * @param options See documentation of ClusterOptions for explanation of specific arguments.
     */
    Cluster(ClusterOptions options = {});
    /**
     * Closing the device. Should undo everything that was done in the constructor. Break created links, free memory,
     * leave the device in a state where it can be re-initialized.
     */
    ~Cluster();

    //---------- Functions related to topology, discovery and device description.

    /**
     * Create a cluster descriptor object. This function will create a cluster descriptor object based on the
     * soc descriptor yaml file passed to the constructor. If no soc descriptor is passed, the function will create a
     * cluster descriptor object based on the devices connected to the system.
     */
    static std::unique_ptr<tt_ClusterDescriptor> create_cluster_descriptor(
        std::string sdesc_path = "", std::unordered_set<chip_id_t> pci_target_devices = {});

    /**
     * Get cluster descriptor object being used in UMD instance.
     */
    tt_ClusterDescriptor* get_cluster_description();

    /**
     * Get set of chip ids for all chips in the cluster.
     */
    std::set<chip_id_t> get_target_device_ids();

    /**
     * Get all logical ids for all local chips targeted by UMD.
     */
    std::set<chip_id_t> get_target_mmio_device_ids();

    /**
     * Get all logical ids for all Ethernet Mapped chips targeted by UMD.
     * Returns an empty set if no remote chips exist in the cluster.
     */
    std::set<chip_id_t> get_target_remote_device_ids();

    /**
     * Get soc descriptor for specified chip.
     *
     * @param chip_id Chip to get soc descriptor for.
     */
    const tt_SocDescriptor& get_soc_descriptor(chip_id_t chip_id) const;

    //---------- Functions used for configuration and initialization.

    /**
     * Set Barrier Address Map parameters used by UMD to communicate with the TT Device.
     * This function should be called right after the device is created. This sets up barrier addresses for tensix L1,
     * eth L1, and DRAM. Barrier addresses are used when calling l1_membar, dram_membar and wait_for_non_mmio_flush.
     * These need to be setup only for the synchronisation purposes between the host and the device.
     *
     * @param barrier_address_params_  All the barrier parameters required by UMD
     */
    void set_barrier_address_params(const barrier_address_params& barrier_address_params_);

    /**
     * Configure a TLB to point to a specific core and an address within that core. Should be done for Static TLBs.
     * If the device uses another mechanism for providing access to the host, this can be ignored.
     * This API is going to be deprecated when all UMD clients transition to CoreCoord API.
     *
     * @param logical_device_id Logical Device being targeted.
     * @param core The TLB will be programmed to point to this core.
     * @param tlb_index TLB id that will be programmed.
     * @param address Start address TLB is mapped to.
     * @param ordering Ordering mode for the TLB.
     */
    void configure_tlb(
        chip_id_t logical_device_id,
        tt_xy_pair core,
        int32_t tlb_index,
        uint64_t address,
        uint64_t ordering = TLB_DATA::Relaxed);

    /**
     * Configure a TLB to point to a specific core and an address within that core. Should be done for Static TLBs.
     * If the device uses another mechanism for providing access to the host, this can be ignored.
     *
     * @param logical_device_id Logical Device being targeted.
     * @param core The TLB will be programmed to point to this core.
     * @param tlb_index TLB id that will be programmed.
     * @param address Start address TLB is mapped to.
     * @param ordering Ordering mode for the TLB.
     */
    void configure_tlb(
        chip_id_t logical_device_id,
        tt::umd::CoreCoord core,
        int32_t tlb_index,
        uint64_t address,
        uint64_t ordering = TLB_DATA::Relaxed);

    /**
     * Pass in ethernet cores with active links for a specific MMIO chip. When called, this function will force UMD to
     * use a subset of cores from the active_eth_cores_per_chip set for all host->cluster non-MMIO transfers. If this
     * function is not called, UMD will use a default set of ethernet core indices for these transfers (0 through 5). If
     * default behaviour is not desired, this function must be called for all MMIO devices.
     * This API is going to be deprecated when all UMD clients transition to CoreCoord API.
     *
     * @param mmio_chip Device being targeted.
     * @param active_eth_cores_per_chip The active ethernet cores for this chip.
     */
    void configure_active_ethernet_cores_for_mmio_device(
        chip_id_t mmio_chip, const std::unordered_set<tt::umd::CoreCoord>& active_eth_cores_per_chip);

    //---------- Start and stop the device and tensix cores.

    /**
     * This function puts the device in a state so that it is ready for loading kernels to the tensix cores.
     * Can include, but is not limited to:
     * - Assert soft Tensix reset
     * - Deassert RiscV reset
     * - Set power state to busy (ramp up AICLK)
     * - Initialize iATUs for PCIe devices
     * - Initialize ethernet queues for remote chips.
     *
     * @param device_params Object specifying initialization configuration.
     */
    void start_device(const tt_device_params& device_params);

    /**
     * To be called at the end of a run.
     * Can include, but not limited to:
     * - Setting power state to idle
     * - Assert tensix reset at all cores.
     */
    void close_device();

    /**
     * Explicitly set the power state of the device.
     * Note that start/close the device already do this implicitly.
     */
    void set_power_state(tt_DevicePowerState state);

    /**
     * Broadcast deassert BRISC soft Tensix Reset to the entire device.
     * This function needs to be called after start_device.
     * It writes to TENSIX register SOFT_RESET, the address of
     * which is architecture dependant. Please consult the desired architecture specs to find the exact address
     */
    void deassert_risc_reset();

    /**
     * Send a BRISC soft deassert reset signal to a single tensix core.
     * Similar to the broadcast deassert_risc_reset API function, but done only on a single core.
     *
     * @param chip Chip to target.
     * @param core Core to target.
     * @param soft_resets Specifies which RISCV cores on Tensix to deassert.
     */
    void deassert_risc_reset_at_core(
        const chip_id_t chip,
        const tt::umd::CoreCoord core,
        const TensixSoftResetOptions& soft_resets = TENSIX_DEASSERT_SOFT_RESET);

    /**
     * Broadcast BRISC assert BRISC soft Tensix Reset to the entire device.
     * It writes to TENSIX register SOFT_RESET, the address of
     * which is architecture dependant. Please consult the desired architecture specs to find the exact address
     */
    void assert_risc_reset();

    /**
     * Send a BRISC soft assert reset signal to a single tensix core.
     * It writes to TENSIX register SOFT_RESET, the address of
     * which is architecture dependant. Please consult the desired architecture specs to find the exact address
     *
     * @param core Chip to target.
     * @param core Core to target.
     * @param soft_resets Specifies which RISCV cores on Tensix to deassert.
     */
    void assert_risc_reset_at_core(
        const chip_id_t chip,
        const tt::umd::CoreCoord core,
        const TensixSoftResetOptions& soft_resets = TENSIX_ASSERT_SOFT_RESET);

    //---------- IO functions for Tensix cores, including DRAM.

    /**
     * Write uint32_t data (as specified by ptr + len pair) to specified device, core and address (defined for Silicon).
     * This API is used for writing to both TENSIX and DRAM cores. The internal SocDescriptor can be used to determine
     * which type of the core is being targeted.
     *
     * @param mem_ptr Source data address.
     * @param size_in_bytes Source data size.
     * @param chip Chip to target.
     * @param core Core to target.
     * @param addr Address to write to.
     */
    void write_to_device(
        const void* mem_ptr, uint32_t size_in_bytes, chip_id_t chip, tt::umd::CoreCoord core, uint64_t addr);

    /**
     * Read uint32_t data from a specified device, core and address to host memory (defined for Silicon).
     * This API is used for reading from both TENSIX and DRAM cores. The internal SocDescriptor can be used to determine
     * which type of the core is being targeted.
     *
     * @param mem_ptr Data pointer to read the data into.
     * @param chip Chip to target.
     * @param core Core to target.
     * @param addr Address to read from.
     * @param size Number of bytes to read.
     */
    void read_from_device(void* mem_ptr, chip_id_t chip, tt::umd::CoreCoord core, uint64_t addr, uint32_t size);

    /**
     * Write uint32_t data (as specified by ptr + len pair) to specified device, core and address (defined for Silicon).
     * This API is used for writing to both TENSIX and DRAM cores. The internal SocDescriptor can be used to determine
     * which type of the core is being targeted.
     * This API is used for writing to registers in the device address space, reads are slower but are guaranteed to be
     * done when this function returns.
     *
     * @param mem_ptr Source data address.
     * @param size_in_bytes Source data size.
     * @param chip Chip to target.
     * @param core Core to target.
     * @param addr Address to write to.
     */
    void write_to_device_reg(
        const void* mem_ptr, uint32_t size_in_bytes, chip_id_t chip, tt::umd::CoreCoord core, uint64_t addr);

    /**
     * Read uint32_t data from a specified device, core and address to host memory (defined for Silicon).
     * This API is used for reading from both TENSIX and DRAM cores. The internal SocDescriptor can be used to determine
     * which type of the core is being targeted.
     * This API is used for writing to registers in the device address space, reads are slower but are guaranteed to be
     * done when this function returns.
     *
     * @param mem_ptr Data pointer to read the data into.
     * @param chip Chip to target.
     * @param core Core to target.
     * @param addr Address to read from.
     * @param size Number of bytes to read.
     */
    void read_from_device_reg(void* mem_ptr, chip_id_t chip, tt::umd::CoreCoord core, uint64_t addr, uint32_t size);

    /**
     * Use PCIe DMA to write device memory (L1 or DRAM).
     *
     * @param src Source data address.
     * @param size Size in bytes.
     * @param chip Chip to target; must be local, i.e. attached via PCIe.
     * @param core Core to target.
     * @param addr Address to write to.
     */
    void dma_write_to_device(const void* src, size_t size, chip_id_t chip, tt::umd::CoreCoord core, uint64_t addr);

    /**
     * Use PCIe DMA to read device memory (L1 or DRAM).
     *
     * @param src Source data address.
     * @param size Size in bytes.
     * @param chip Chip to target; must be local, i.e. attached via PCIe.
     * @param core Core to target.
     * @param addr Address to read from.
     */
    void dma_read_from_device(void* dst, size_t size, chip_id_t chip, tt::umd::CoreCoord core, uint64_t addr);

    /**
     * This function writes to multiple chips and cores in the cluster. A set of chips, rows and columns can be excluded
     * from the broadcast. The function has to be called either only for Tensix cores or only for DRAM cores.
     *
     *
     * This API is going to be deprecated when all UMD clients transition to CoreCoord API.
     *
     * @param mem_ptr Data to write.
     * @param size_in_bytes Size of data to write.
     * @param address Address to write to.
     * @param chips_to_exclude Chips to exclude from the broadcast.
     * @param rows_to_exclude  NOC0 rows to exclude from the broadcast.
     * @param columns_to_exclude NOC0 columns to exclude from the broadcast.
     */
    void broadcast_write_to_cluster(
        const void* mem_ptr,
        uint32_t size_in_bytes,
        uint64_t address,
        const std::set<chip_id_t>& chips_to_exclude,
        std::set<uint32_t>& rows_to_exclude,
        std::set<uint32_t>& columns_to_exclude);

    /**
     * This API allows you to write directly to device memory that is addressable by a static TLB.
     */
    std::function<void(uint32_t, uint32_t, const uint8_t*)> get_fast_pcie_static_tlb_write_callable(int device_id);

    /**
     * Provide fast write access to a statically-mapped TLB.
     * It is the caller's responsibility to ensure that
     * - the target has a static TLB mapping configured.
     * - the mapping is unchanged during the lifetime of the returned object.
     * - the Cluster instance outlives the returned object.
     * - use of the returned object is congruent with the target's TLB setup.
     *
     * @param target The target chip and core to write to.
     */
    tt::Writer get_static_tlb_writer(const chip_id_t chip, const tt::umd::CoreCoord target);

    //---------- Functions for synchronization and memory barriers.

    /**
     * Tensix L1 memory barrier.
     * This should be called when the client wants to ensure that all transactions on the L1 of the specified cores have
     * completed.
     *
     * @param chip Chip to target.
     * @param cores Cores being targeted.
     */
    void l1_membar(const chip_id_t chip, const std::unordered_set<tt::umd::CoreCoord>& cores = {});

    /**
     * DRAM memory barrier.
     * This should be called when the client wants to ensure that all transactions on the specified dram bank have
     * completed.
     *
     * @param chip Chip to target.
     * @param channels Channels being targeted.
     */
    void dram_membar(const chip_id_t chip, const std::unordered_set<uint32_t>& channels = {});

    /**
     * DRAM memory barrier.
     * This should be called when the client wants to ensure that all transactions on the specified dram bank have
     * completed.
     *
     * @param chip Chip being targeted.
     * @param cores Cores being targeted.
     */
    void dram_membar(const chip_id_t chip, const std::unordered_set<tt::umd::CoreCoord>& cores = {});

    // Runtime functions
    /**
     * Non-MMIO (ethernet) barrier.
     * Similar to an mfence for host -> host transfers. Will flush all in-flight ethernet transactions before proceeding
     * with the next one. This will be applied to all chips in the cluster.
     *
     * This function is only used in context of remote (ethernet connected) chips in the cluster.
     */
    void wait_for_non_mmio_flush();

    /**
     * Non-MMIO (ethernet) barrier.
     * This function should be called for a remote chip. If called for local chip, it will be a no-op.
     * This function is only used in context of remote (ethernet connected) chips in the cluster.
     *
     * @param chip_id Chip to target.
     */
    void wait_for_non_mmio_flush(const chip_id_t chip_id);

    //---------- IO functions for host memory. Write and read functions, and getting host memory info.

    /**
     * Write data to specified address and channel on host (defined for Silicon).
     * This API is used to write to the host memory location that is made available to the device through
     * initialization. During the initialization the user should be able to specify how many "channels" are available to
     * the device, and that is what the channel argument refers to. This API can be directed to memory on the device
     * itself if needed. That would imply some performance considerations.
     *
     * @param mem_ptr Data to write.
     * @param size Number of bytes to write.
     * @param addr Address to write to.
     * @param channel Host channel to target.
     * @param src_device_id Chip to target.
     */
    void write_to_sysmem(
        const void* mem_ptr, std::uint32_t size, uint64_t addr, uint16_t channel, chip_id_t src_device_id);

    /**
     * Read data from specified address and channel on host (defined for Silicon).
     * Similar as write_to_sysmem, but for reading.
     *
     * @param vec Data to write.
     * @param addr Address to write to.
     * @param channel Host channel to target.
     * @param size Number of bytes to read.
     * @param src_device_id Chip to target.
     */
    void read_from_sysmem(void* mem_ptr, uint64_t addr, uint16_t channel, uint32_t size, chip_id_t src_device_id);

    /**
     * Query number of memory channels on Host device allocated for a specific device during initialization.
     *
     * @param device_id Logical device id to target.
     */
    std::uint32_t get_num_host_channels(std::uint32_t device_id);

    /**
     * Get size for a specific Host channel accessible by the corresponding device.
     *
     * @param device_id Logical device id to target.
     * @param channel Logical host channel to target.
     */
    std::uint32_t get_host_channel_size(std::uint32_t device_id, std::uint32_t channel);

    /**
     * Get absolute address corresponding to a zero based offset into a specific host memory channel for a specific
     * device.
     *
     * @param offset Offset wrt the start of the channel's address space.
     * @param src_device_id Device to target.
     * @param channel Host memory channel.
     */
    void* host_dma_address(std::uint64_t offset, chip_id_t src_device_id, uint16_t channel) const;

    /**
     * Get base PCIe address that is used to access the device.
     *
     * @param chip_id Chip to target.
     */
    std::uint64_t get_pcie_base_addr_from_device(const chip_id_t chip_id) const;

    //---------- Misc system functions

    /**
     * Issue message to device, meant to be picked up by ARC firmware.
     *
     * @param logical_device_id Chip to target.
     * @param msg_code Specifies type of ARC message.
     * @param wait_for_done Block until ARC responds.
     * @param arg0 Message related argument.
     * @param arg1 Message related argument.
     * @param timeout_ms Timeout in milliseconds.
     * @param return3 Return value from ARC.
     * @param return4 Return value from ARC.
     */
    int arc_msg(
        int logical_device_id,
        uint32_t msg_code,
        bool wait_for_done = true,
        uint32_t arg0 = 0,
        uint32_t arg1 = 0,
        uint32_t timeout_ms = 1000,
        uint32_t* return_3 = nullptr,
        uint32_t* return_4 = nullptr);

    /**
     * Get clock frequencies for all MMIO devices targeted by UMD.
     */
    std::map<int, int> get_clocks();

    /**
     * Get which NUMA node this device is associated with, or -1 if non-NUMA
     *
     * @param device_id Logical device id to query.
     */
    std::uint32_t get_numa_node_for_pcie_device(std::uint32_t device_id);

    /**
     * Get the ethernet firmware version used by the physical cluster (only implemented for Silicon Backend).
     * Will return a bogus version if no remote chips are supported for the device.
     */
    tt_version get_ethernet_fw_version() const;

    //---------- Functions to get various internal cluster objects, mainly device classes and their components.

    /**
     * Get Chip for specified logical device id.
     *
     * @param device_id Device to target.
     */
    Chip* get_chip(chip_id_t device_id) const;

    /**
     * Get Chip for specified logical device id, verify it is local.
     *
     * @param device_id Device to target.
     */
    LocalChip* get_local_chip(chip_id_t device_id) const;

    /**
     * Get Chip for specified logical device id, verify it is remote.
     *
     * @param device_id Device to target.
     */
    RemoteChip* get_remote_chip(chip_id_t device_id) const;

    /**
     * Get PCI device for specified logical device id.
     *
     * @param device_id Device to target.
     */
    PCIDevice* get_pci_device(int device_id) const;

    /**
     * Get TTDevice for specified logical device id.
     *
     * @param device_id Device to target.
     */
    TTDevice* get_tt_device(chip_id_t device_id) const;

    /**
     * Get TLBManager for specified logical device id.
     *
     * @param device_id Device to target.
     */
    TLBManager* get_tlb_manager(chip_id_t device_id) const;

    /**
     * Exposes how TLBs are configured for a specific device.
     */
    tlb_configuration get_tlb_configuration(const chip_id_t chip, const tt::umd::CoreCoord core);

private:
    // Helper functions
    // Startup + teardown
    void create_device(
        const std::set<chip_id_t>& target_mmio_device_ids,
        const uint32_t& num_host_mem_ch_per_mmio_device,
        const ChipType& chip_type);
    void broadcast_tensix_risc_reset_to_cluster(const TensixSoftResetOptions& soft_resets);
    void send_remote_tensix_risc_reset_to_core(const tt_cxy_pair& core, const TensixSoftResetOptions& soft_resets);
    void send_tensix_risc_reset_to_core(const tt_cxy_pair& core, const TensixSoftResetOptions& soft_resets);
    uint32_t get_power_state_arc_msg(chip_id_t chip_id, tt_DevicePowerState state);
    void enable_ethernet_queue(int timeout);
    void deassert_resets_and_set_power_state();
    int get_clock(int logical_device_id);

    // Communication Functions
    void ethernet_broadcast_write(
        const void* mem_ptr,
        uint32_t size_in_bytes,
        uint64_t address,
        const std::set<chip_id_t>& chips_to_exclude,
        const std::set<uint32_t>& rows_to_exclude,
        std::set<uint32_t>& cols_to_exclude,
        bool use_virtual_coords);

    std::unordered_map<chip_id_t, std::vector<std::vector<int>>>& get_ethernet_broadcast_headers(
        const std::set<chip_id_t>& chips_to_exclude);
    // Test functions
    void verify_eth_fw();
    void verify_sw_fw_versions(int device_id, std::uint32_t sw_version, std::vector<std::uint32_t>& fw_versions);

    // Helper functions for constructing the chips from the cluster descriptor.
    std::unique_ptr<Chip> construct_chip_from_cluster(
        chip_id_t chip_id,
        const ChipType& chip_type,
        tt_ClusterDescriptor* cluster_desc,
        tt_SocDescriptor& soc_desc,
        int num_host_mem_channels,
        const std::filesystem::path& simulator_directory);
    tt_SocDescriptor construct_soc_descriptor(
        const std::string& soc_desc_path,
        chip_id_t chip_id,
        ChipType chip_type,
        tt_ClusterDescriptor* cluster_desc,
        bool perform_harvesting,
        HarvestingMasks& simulated_harvesting_masks);

    void add_chip(const chip_id_t& chip_id, const ChipType& chip_type, std::unique_ptr<Chip> chip);
    HarvestingMasks get_harvesting_masks(
        chip_id_t chip_id,
        tt_ClusterDescriptor* cluster_desc,
        bool perform_harvesting,
        HarvestingMasks& simulated_harvesting_masks);
    uint32_t get_tensix_harvesting_mask(
        chip_id_t chip_id, tt_ClusterDescriptor* cluster_desc, HarvestingMasks& simulated_harvesting_masks);
    void construct_cluster(const uint32_t& num_host_mem_ch_per_mmio_device, const ChipType& chip_type);
    tt_xy_pair translate_to_api_coords(const chip_id_t chip, const tt::umd::CoreCoord core_coord) const;
    // Most of the old APIs accept virtual coordinates, but we communicate with the device through translated
    // coordinates. This is an internal helper function, until we switch the API to accept translated coordinates.
    tt_xy_pair translate_chip_coord_virtual_to_translated(const chip_id_t chip_id, const tt_xy_pair core) const;

    static std::unique_ptr<tt_ClusterDescriptor> create_cluster_descriptor(
        const std::unordered_map<chip_id_t, std::unique_ptr<tt::umd::Chip>>& chips);

    static void ubb_eth_connections(
        const std::unordered_map<chip_id_t, std::unique_ptr<tt::umd::Chip>>& chips,
        std::unique_ptr<tt_ClusterDescriptor>& cluster_desc);

    static void verify_cluster_options(const ClusterOptions& options);

    // State variables
    std::set<chip_id_t> all_chip_ids_ = {};
    std::set<chip_id_t> remote_chip_ids_ = {};
    std::set<chip_id_t> local_chip_ids_ = {};
    std::unordered_map<chip_id_t, std::unique_ptr<Chip>> chips_;
    tt::ARCH arch_name;

    std::unique_ptr<tt_ClusterDescriptor> cluster_desc;

    std::map<std::set<chip_id_t>, std::unordered_map<chip_id_t, std::vector<std::vector<int>>>> bcast_header_cache = {};
    bool use_ethernet_broadcast = true;
    bool use_virtual_coords_for_eth_broadcast = true;
    tt_version eth_fw_version;  // Ethernet FW the driver is interfacing with
    // ERISC FW Version Required by UMD
    static constexpr std::uint32_t SW_VERSION = 0x06060000;
};

}  // namespace tt::umd

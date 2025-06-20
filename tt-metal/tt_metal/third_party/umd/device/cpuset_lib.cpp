// SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0

#include "cpuset_lib.hpp"

#include <fmt/format.h>
#include <fmt/ranges.h>  // Needed to format vectors
#include <fmt/std.h>     // Needed to format thread_id

#include <algorithm>
#include <filesystem>
#include <thread>
#include <tt-logger/tt-logger.hpp>

#include "cpuset_lib.hpp"
#include "umd/device/cluster.h"

namespace tt {

namespace fs = std::filesystem;

namespace cpuset {

/////////////////////////////////////////////////////////////////////////
// Initialization Functions /////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////

// Constructor for singleton class cpu id allocator
tt_cpuset_allocator::tt_cpuset_allocator() {
    m_pid = getpid();
    m_debug = std::getenv("TT_BACKEND_CPUSET_ALLOCATOR_DEBUG") ? true : false;

    // Chicken bit to disable this entire feature for debug/comparison.
    bool cpuset_allocator_enable_env = std::getenv("TT_BACKEND_CPUSET_ALLOCATOR_ENABLE") ? true : false;

    auto system_tid = std::this_thread::get_id();
    log_debug(
        LogSiliconDriver,
        "Starting tt_cpuset_allocator constructor now for process_id: {} thread_id: {}",
        m_pid,
        system_tid);

    m_enable_cpuset_allocator = true;

    // NumaNodes are used for hugepage allocations, separate from CPU Pinning. Required to parse topology first.
    m_enable_cpuset_allocator &= init_topology_init_and_load();
    m_enable_cpuset_allocator &= init_get_number_of_packages();
    m_enable_cpuset_allocator &= init_find_tt_pci_devices_packages_numanodes();

    if (!cpuset_allocator_enable_env) {
        m_enable_cpuset_allocator = false;
    } else {
        bool is_cpu_supported = init_is_cpu_model_supported();

        if (is_cpu_supported) {
            m_enable_cpuset_allocator &= init_determine_cpuset_allocations();
        } else {
            m_enable_cpuset_allocator = false;
        }

        log_debug(
            LogSiliconDriver,
            "Finished tt_cpuset_allocator constructor now with m_enable_cpuset_allocator: {} for process_id: {} "
            "thread_id: {} ",
            m_enable_cpuset_allocator,
            m_pid,
            system_tid);
    }
}

// Step 1 : Initialize and perform m_topology detection
bool tt_cpuset_allocator::init_topology_init_and_load() {
    log_debug(LogSiliconDriver, "Inside tt_cpuset_allocator::topology_init_and_load()");

    if (!m_enable_cpuset_allocator) {
        return false;
    }

    if (hwloc_topology_init(&m_topology)) {
        log_warning(LogSiliconDriver, "Problem initializing topology");
        return false;
    }

    hwloc_topology_set_type_filter(
        m_topology, HWLOC_OBJ_PCI_DEVICE, HWLOC_TYPE_FILTER_KEEP_ALL);  // Need to find PCI devices.

    if (hwloc_topology_load(m_topology)) {
        log_warning(LogSiliconDriver, "Problem loading topology");
        return false;
    }

    return true;  // Success
}

// Step 2 - Find TT PCI devices in topology by vendor_id to get their PCI bus_id and physical device_id, and package and
// numamode.
bool tt_cpuset_allocator::init_find_tt_pci_devices_packages_numanodes() {
    if (!m_enable_cpuset_allocator) {
        return false;
    }

    log_debug(LogSiliconDriver, "Starting tt_cpuset_allocator::init_find_tt_pci_devices_packages_numanodes()");
    m_num_tt_device_by_pci_device_id_map.clear();

    hwloc_obj_t pci_device_obj = NULL;
    const std::regex tt_device_re("tenstorrent!([0-9]+)");

    while ((pci_device_obj = hwloc_get_next_pcidev(m_topology, pci_device_obj))) {
        if (hwloc_obj_type_is_io(pci_device_obj->type) &&
            (pci_device_obj->attr->pcidev.vendor_id == TENSTORRENT_VENDOR_ID)) {
            std::pair<uint16_t, uint16_t> device_id_revision =
                std::make_pair(pci_device_obj->attr->pcidev.device_id, pci_device_obj->attr->pcidev.revision);
            m_num_tt_device_by_pci_device_id_map[device_id_revision] += 1;

            std::string pci_bus_id_str = get_pci_bus_id(pci_device_obj);
            std::string pci_device_dir = fmt::format("/sys/bus/pci/devices/{}/tenstorrent/", pci_bus_id_str);
            int physical_device_id = -1;

            log_trace(
                LogSiliconDriver,
                "Found TT device with pci_bus_id_str: {} num_devices_by_pci_device_id: {}",
                pci_bus_id_str,
                m_num_tt_device_by_pci_device_id_map[device_id_revision]);

            // First, get the physical_device_id of the device.
            if (fs::exists(pci_device_dir)) {
                for (const auto &entry : fs::directory_iterator(pci_device_dir)) {
                    auto entry_str = entry.path().string();

                    if (std::smatch device_match;
                        std::regex_search(entry_str, device_match, tt_device_re) and (stoi(device_match[1]) >= 0)) {
                        physical_device_id = stoi(device_match[1]);
                        m_all_tt_devices.push_back(physical_device_id);
                        log_debug(
                            LogSiliconDriver,
                            "Found physical_device_id: {} from file: {}",
                            physical_device_id,
                            entry_str);
                        break;
                    }
                }

                if (physical_device_id == -1) {
                    log_warning(
                        LogSiliconDriver, "Did not find file containing physical_device_id in {}", pci_device_dir);
                    return false;
                }

                m_physical_device_id_to_pci_bus_id_map.insert({physical_device_id, pci_bus_id_str});

                // Next, get the PackageID of the device and update maps.
                auto package_id = get_package_id_from_device(pci_device_obj, physical_device_id);

                // This package was not previously seen. Initialize structures tracking the TT Devices mapped to this
                // package and structures storing the CPU characteristics per package.
                if (m_package_id_to_devices_map.find(package_id) == m_package_id_to_devices_map.end()) {
                    m_package_id_to_devices_map.insert({package_id, {}});
                    m_package_id_to_num_l3_per_ccx_map.insert({package_id, 0});
                    m_package_id_to_num_ccx_per_ccd_map.insert({package_id, 0});
                }
                if (package_id != -1) {
                    m_package_id_to_devices_map.at(package_id).push_back(physical_device_id);
                    m_physical_device_id_to_package_id_map.insert({physical_device_id, package_id});
                } else {
                    log_warning(
                        LogSiliconDriver,
                        "Could not find package_id for TT Device (physical_device_id: {} pci_bus_id: {})",
                        physical_device_id,
                        pci_bus_id_str);
                    return false;
                }

                // Next, get the NumaNode set of the device, and update maps.
                auto numa_nodeset = get_numa_nodeset_from_device(pci_device_obj, physical_device_id);
                m_physical_device_id_to_numa_nodeset_map.insert({physical_device_id, numa_nodeset});

                if (numa_nodeset == 0x0) {
                    log_warning(
                        LogSiliconDriver,
                        "Could not find NumaNodeSet for TT Device (physical_device_id: {} pci_bus_id: {})",
                        physical_device_id,
                        pci_bus_id_str);
                    return false;
                }

                m_physical_device_id_to_cpusets_map.insert({physical_device_id, {}});  // Empty vector.
                m_num_cpu_cores_allocated_per_tt_device.insert({physical_device_id, 0});
            }
        }
    }

    if (m_all_tt_devices.size() == 0) {
        log_warning(
            LogSiliconDriver,
            "Did not find any PCI devices matching Tenstorrent vendor_id 0x{:x}",
            TENSTORRENT_VENDOR_ID);
        return false;
    }

    log_debug(
        LogSiliconDriver,
        "Finshed tt_cpuset_allocator::init_find_tt_pci_devices_packages_numanodes() found {} devices",
        m_all_tt_devices.size());

    // Sort these 2 vectors of device_ids before we are done, since discovery can be in any order.
    for (auto &p : m_package_id_to_devices_map) {
        std::sort(p.second.begin(), p.second.end());
    }

    std::sort(m_all_tt_devices.begin(), m_all_tt_devices.end());

    return true;  // Success
}

// Step 3 : Detect the number of packages.
bool tt_cpuset_allocator::init_get_number_of_packages() {
    if (!m_enable_cpuset_allocator) {
        return false;
    }

    m_num_packages = hwloc_get_nbobjs_by_type(m_topology, HWLOC_OBJ_PACKAGE);
    log_debug(LogSiliconDriver, "Found {} CPU packages", m_num_packages);
    return m_num_packages > 0;  // Success
}

// Step 4 : Return true if all packages are models we want to support. Env-var can be used to ignore this check.
bool tt_cpuset_allocator::init_is_cpu_model_supported() {
    if (!m_enable_cpuset_allocator) {
        return false;
    }

    if (m_num_packages == 0) {
        log_debug(LogSiliconDriver, "init_is_cpu_model_supported(): Found 0 packages, functions run out of order?");
        return false;
    }

    bool use_any_cpu = std::getenv("TT_BACKEND_CPUSET_ALLOCATOR_SUPPORT_ANY_CPU") ? true : false;

    log_debug(LogSiliconDriver, "Inside tt_cpuset_allocator::check_if_cpu_model_supported()");

    // Supported CPU Models for enabling CPUSET Allocator.  Keep the list small to production machines to start.
    std::vector<std::string> supported_cpu_models = {
        "AMD EPYC 7352 24-Core Processor", "AMD EPYC 7532 32-Core Processor"};

    // CPU Models that have L3 per CCX and 2 CCX per CCD
    std::vector<std::string> opt_2ccx_per_ccd_cpu_models = {
        "AMD EPYC 7352 24-Core Processor", "AMD EPYC 7532 32-Core Processor"};
    for (const auto &package : m_package_id_to_devices_map) {
        int package_id = package.first;
        auto package_obj = hwloc_get_obj_by_type(m_topology, HWLOC_OBJ_PACKAGE, package_id);
        if (m_debug) {
            print_hwloc_object(package_obj, 0, true, true);
        }

        std::string pkg_cpu_model = hwloc_obj_get_info_by_name(package_obj, "CPUModel");

        // First find out if this CPU is supported by CPUSET Allocator at all.
        bool has_supported_cpu = use_any_cpu ? true : false;

        for (auto &supported_cpu_model : supported_cpu_models) {
            has_supported_cpu |= (pkg_cpu_model.find(supported_cpu_model) != std::string::npos);
        }

        log_debug(
            LogSiliconDriver,
            "Detected package-id: {} has_supported_cpu: {} for CpuModel: {}",
            package_id,
            has_supported_cpu,
            pkg_cpu_model);

        if (!has_supported_cpu) {
            return false;
        }

        // Then, determine if the 2CCX-PER-CCD optimization can be enabled for this CPU Model in the package.
        for (auto &opt_cpu_model : opt_2ccx_per_ccd_cpu_models) {
            if (pkg_cpu_model.find(opt_cpu_model) != std::string::npos) {
                m_package_id_to_num_l3_per_ccx_map.at(package_id) = 1;
                m_package_id_to_num_ccx_per_ccd_map.at(package_id) = 2;
            }
        }
    }

    return true;  // Successhwloc
}

// Step 5: Get all target allocation objects (ie. L3Cache if IO thread to be allocated per L3Cache cpuset) for a given
// socket/package.
bool tt_cpuset_allocator::init_determine_cpuset_allocations() {
    if (!m_enable_cpuset_allocator) {
        return false;
    }

    log_debug(LogSiliconDriver, "Inside tt_cpuset_allocator::init_determine_cpuset_allocations()");
    for (const auto &package : m_package_id_to_devices_map) {
        int package_id = package.first;
        auto num_tt_devices_for_cpu_package = package.second.size();

        if (num_tt_devices_for_cpu_package == 0) {
            log_debug(
                LogSiliconDriver,
                "init_determine_cpuset_allocations() -- no TT devices for package_id: {}, skipping.",
                package_id);
            continue;
        }

        log_debug(
            LogSiliconDriver,
            "init_determine_cpuset_allocations(). starting to detect allocation slots for package_id: {} ",
            package_id);

        auto package_obj = hwloc_get_obj_by_type(m_topology, HWLOC_OBJ_PACKAGE, package_id);
        if (m_debug) {
            print_hwloc_object(package_obj, 0, true, true);
        }

        auto num_alloc_slots_in_package =
            hwloc_get_nbobjs_inside_cpuset_by_type(m_topology, package_obj->cpuset, m_object_per_alloc_slot);
        if (num_alloc_slots_in_package == 0) {
            log_warning(
                LogSiliconDriver,
                "Could not find any of the alloc objects in package_id: {} for this cpu arc",
                package_id);
            return false;
        }
        auto num_alloc_slots_per_tt_device = num_alloc_slots_in_package / num_tt_devices_for_cpu_package;

        // Above splits evenly by devices, leaves remainder unused in the example case of 3 devices but 8 slots.
        log_debug(
            LogSiliconDriver,
            "init_determine_cpuset_allocations(). package_id: {} num_alloc_slots_in_package: {} "
            "num_tt_devices_for_cpu_package: {} num_alloc_slots_per_tt_device: {}",
            package_id,
            num_alloc_slots_in_package,
            num_tt_devices_for_cpu_package,
            num_alloc_slots_per_tt_device);

        int device_idx = 0;

        for (int obj_idx = 0; obj_idx < num_alloc_slots_in_package; obj_idx++) {
            auto obj = hwloc_get_obj_below_by_type(
                m_topology, HWLOC_OBJ_PACKAGE, package_id, m_object_per_alloc_slot, obj_idx);

            if (obj) {
                if (m_debug) {
                    print_hwloc_object(obj, 1, true);
                }

                auto physical_device_id = m_package_id_to_devices_map.at(package_id).at(device_idx);

                // Hack for maximum number of slots per device.
                // if (m_physical_device_id_to_cpusets_map.at(physical_device_id).size() < 2){
                m_physical_device_id_to_cpusets_map.at(physical_device_id).push_back(obj->cpuset);
                int num_cpus = hwloc_get_nbobjs_inside_cpuset_by_type(m_topology, obj->cpuset, HWLOC_OBJ_CORE);
                m_num_cpu_cores_allocated_per_tt_device.at(physical_device_id) += num_cpus;
                // }

                // We're distributing allocation objects per package across TT devices, so switch to next one.
                if (((obj_idx + 1) % num_alloc_slots_per_tt_device) == 0) {
                    device_idx = (device_idx + 1) %
                                 num_tt_devices_for_cpu_package;  // Loop around if extra slots remain. Assigned to
                                                                  // first device for that package.
                }

            } else {
                log_warning(
                    LogSiliconDriver,
                    "init_determine_cpuset_allocations(). Something went wrong looking for cpuset alloc object under "
                    "package");
                return false;
            }
        }

        log_debug(
            LogSiliconDriver,
            "init_determine_cpuset_allocations(). Done detecting allocation slots for package_id: {} ",
            package_id);
    }

    // Summary for Debug purposes.
    for (auto &physical_device_id : m_all_tt_devices) {
        for (size_t device_alloc_idx = 0;
             device_alloc_idx < m_physical_device_id_to_cpusets_map.at(physical_device_id).size();
             device_alloc_idx++) {
            auto cpuset = m_physical_device_id_to_cpusets_map.at(physical_device_id).at(device_alloc_idx);
            auto pu_ids_vector = get_hwloc_bitmap_vector(cpuset);
            auto num_pu_ids = pu_ids_vector.size();
            auto package_id = m_physical_device_id_to_package_id_map.at(physical_device_id);
            log_debug(
                LogSiliconDriver,
                "Done init_determine_cpuset_allocations(). Summary => for mmio physical_device_id: {} package_id: {} "
                "device_alloc_idx: {} picked {} PU's {}",
                physical_device_id,
                package_id,
                device_alloc_idx,
                num_pu_ids,
                pu_ids_vector);
        }
    }

    return true;  // Success
}

/////////////////////////////////////////////////////////////////////////
// Runtime Functions ////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////

// Given a physical device_id, determine the right numa nodes associated with it and attempt to membind a previously
// allocated memory region to it.
bool tt_cpuset_allocator::bind_area_memory_nodeset(chip_id_t physical_device_id, const void *addr, size_t len) {
    auto tid = std::this_thread::get_id();
    log_debug(
        LogSiliconDriver,
        "bind_area_memory_nodeset(): Going to attempt memory binding of addr/len to NumaNode for physical_device_id: "
        "{} (pid: {} tid: {})",
        physical_device_id,
        m_pid,
        tid);

    if (m_physical_device_id_to_numa_nodeset_map.count(physical_device_id) == 0) {
        log_warning(
            LogSiliconDriver,
            "bind_area_memory_nodeset(): Did not find physical_device_id: {} in numanode_mask map, this is not "
            "expected.",
            physical_device_id);
        return false;
    }

    auto target_nodeset = m_physical_device_id_to_numa_nodeset_map.at(physical_device_id);

    if (target_nodeset != 0) {
        if (hwloc_set_area_membind(
                m_topology,
                addr,
                len,
                target_nodeset,
                HWLOC_MEMBIND_BIND,
                HWLOC_MEMBIND_BYNODESET | HWLOC_MEMBIND_STRICT | HWLOC_MEMBIND_MIGRATE)) {
            log_warning(
                LogSiliconDriver,
                "hwloc_set_area_membind(): failed for physical_device_id: {} on NodeSet: {} with errno: {} (pid: {} "
                "tid: {})",
                physical_device_id,
                get_hwloc_bitmap_vector(target_nodeset),
                strerror(errno),
                m_pid,
                tid);
            return false;
        } else {
            log_debug(
                LogSiliconDriver,
                "hwloc_set_area_membind(): success for physical_device_id: {} on NodeSet: {} (pid: {} tid: {})",
                physical_device_id,
                get_hwloc_bitmap_vector(target_nodeset),
                m_pid,
                tid);
        }
    } else {
        log_warning(
            LogSiliconDriver,
            "bind_area_memory_nodeset(): Unable to determine TT Device to NumaNode mapping for physical_device_id: {}. "
            "Skipping membind.",
            physical_device_id);
        return false;
    }

    return true;  // Success
}

int tt_cpuset_allocator::_get_num_tt_pci_devices() {
    for (auto &d : m_physical_device_id_to_package_id_map) {
        log_trace(LogSiliconDriver, "Found physical_device_id: {} ", d.first);
    }
    return m_physical_device_id_to_package_id_map.size();
}

/////////////////////////////////////////////////////////////////////////
// Helper Functions //////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////

std::string tt_cpuset_allocator::get_pci_bus_id(hwloc_obj_t pci_device_obj) {
    std::string pci_bus_id_str = "";

    if (hwloc_obj_type_is_io(pci_device_obj->type)) {
        auto attrs = pci_device_obj->attr->pcidev;
        pci_bus_id_str = fmt::format("{:04x}:{:02x}:{:02x}.{:01x}", attrs.domain, attrs.bus, attrs.dev, attrs.func);
    }

    return pci_bus_id_str;
}

int tt_cpuset_allocator::get_package_id_from_device(hwloc_obj_t pci_device_obj, chip_id_t physical_device_id) {
    auto pci_bus_id_str = m_physical_device_id_to_pci_bus_id_map.at(physical_device_id);

    log_debug(
        LogSiliconDriver,
        "Checking TT device (physical_device_id: {} pci_bus_id: {}) to find it's corresponding CPU package",
        physical_device_id,
        pci_bus_id_str);

    hwloc_obj_t tmp_obj = hwloc_get_non_io_ancestor_obj(m_topology, pci_device_obj);
    int package_id = -1;

    // Keep going up until package/machine hierarchy is found, in case we don't find it right away.
    while (package_id == -1) {
        if ((hwloc_compare_types(tmp_obj->type, HWLOC_OBJ_PACKAGE) == 0) ||
            (hwloc_compare_types(tmp_obj->type, HWLOC_OBJ_MACHINE) == 0)) {
            if (tmp_obj->os_index != (unsigned)-1) {
                package_id = tmp_obj->os_index;
            } else {
                log_warning(
                    LogSiliconDriver,
                    "Could not find os_index of package or machine object for TT device (physical_device_id: {} "
                    "pci_bus_id: {})",
                    physical_device_id,
                    pci_bus_id_str);
                break;
            }
        } else {
            if (tmp_obj->parent) {
                tmp_obj = tmp_obj->parent;
            } else {
                break;
            }
        }
    }

    if (m_debug) {
        print_hwloc_object(pci_device_obj, 1, true, true);
    }
    if (m_debug) {
        print_hwloc_object(tmp_obj, 1, true, true);
    }

    return package_id;
}

hwloc_nodeset_t tt_cpuset_allocator::get_numa_nodeset_from_device(
    hwloc_obj_t pci_device_obj, chip_id_t physical_device_id) {
    hwloc_nodeset_t nodeset = 0x0;

    // Currently an issue in non-EPYC machines where PCI devices are directly under Machine, and not any NumaNodes.
    // As quick workaround, skip this if there is only single numanode since returning 1 seems fine.
    if (hwloc_get_nbobjs_by_type(m_topology, HWLOC_OBJ_NUMANODE) == 1) {
        auto numanode = hwloc_get_obj_by_type(m_topology, HWLOC_OBJ_NUMANODE, 0);
        return numanode->nodeset;
    }

    auto pci_bus_id_str = m_physical_device_id_to_pci_bus_id_map.at(physical_device_id);

    log_debug(
        LogSiliconDriver,
        "init_detect_tt_device_numanodes(): Checking TT device (physical_device_id: {} pci_bus_id: {}) to find it's "
        "corresponding NumaNode.",
        physical_device_id,
        pci_bus_id_str);

    hwloc_obj_t tmp_obj = pci_device_obj->parent;
    while (tmp_obj && !tmp_obj->memory_arity) {
        tmp_obj = tmp_obj->parent; /* no memory child, walk up */
    }

    if (tmp_obj && tmp_obj->nodeset) {
        log_debug(
            LogSiliconDriver,
            "init_detect_tt_device_numanodes(): For TT device (physical_device_id: {} pci_bus_id: {}) found "
            "NumaNodeSet: {}",
            physical_device_id,
            pci_bus_id_str,
            get_hwloc_bitmap_vector(tmp_obj->nodeset));
        nodeset = tmp_obj->nodeset;
    } else {
        log_warning(
            LogSiliconDriver,
            "init_detect_tt_device_numanodes(): Could not determine NumaNodeSet for TT device (physical_device_id: {} "
            "pci_bus_id: {})",
            physical_device_id,
            pci_bus_id_str);
    }

    return nodeset;
}

int tt_cpuset_allocator::_get_num_tt_pci_devices_by_pci_device_id(uint16_t device_id, uint16_t revision) {
    std::pair<uint16_t, uint16_t> device_id_revision = std::make_pair(device_id, revision);

    if (m_num_tt_device_by_pci_device_id_map.find(device_id_revision) != m_num_tt_device_by_pci_device_id_map.end()) {
        return m_num_tt_device_by_pci_device_id_map.at(device_id_revision);
    } else {
        log_warning(
            LogSiliconDriver,
            "Cannot find any TT device with PCI device_id: 0x{:x} and revision: {} in topology.",
            device_id,
            revision);
        return 0;
    }
}

/////////////////////////////////////////////////////////////////////////
// Debug Functions ///////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////

// Get all PU ids (or numa nodes) in a vector, for legacy/back-compat/debug purposes.
std::vector<int> tt_cpuset_allocator::get_hwloc_bitmap_vector(hwloc_bitmap_t &bitmap) {
    std::vector<int> indices;
    int index;
    if (bitmap) {
        hwloc_bitmap_foreach_begin(index, bitmap) indices.push_back(index);
        hwloc_bitmap_foreach_end();
    }
    return indices;
}

std::vector<int> tt_cpuset_allocator::get_hwloc_cpuset_vector(hwloc_obj_t &obj) {
    return get_hwloc_bitmap_vector(obj->cpuset);
}

std::vector<int> tt_cpuset_allocator::get_hwloc_nodeset_vector(hwloc_obj_t &obj) {
    return get_hwloc_bitmap_vector(obj->nodeset);
}

// Nicer way to print pu ids as a vector on single line.
void tt_cpuset_allocator::print_hwloc_cpuset(hwloc_obj_t &obj) {
    std::cout << " Number: " << hwloc_bitmap_weight(obj->cpuset) << " cpuset_pu_ids: " << get_hwloc_cpuset_vector(obj);
}

void tt_cpuset_allocator::print_hwloc_nodeset(hwloc_obj_t &obj) {
    std::cout << " Number: " << hwloc_bitmap_weight(obj->nodeset)
              << " nodeset node_ids: " << get_hwloc_nodeset_vector(obj);
}

void tt_cpuset_allocator::print_hwloc_object(hwloc_obj_t &obj, int depth, bool verbose, bool show_cpuids) {
    char type[32], attr[1024];

    hwloc_obj_type_snprintf(type, sizeof(type), obj, verbose);
    printf("%*s%s", 2 * depth, "", type);
    if (obj->os_index != (unsigned)-1) {
        printf("#%u", obj->os_index);
    }
    hwloc_obj_attr_snprintf(attr, sizeof(attr), obj, " ", verbose);

    if (*attr) {
        printf("(%s)", attr);
    }
    if (show_cpuids && obj->cpuset) {
        print_hwloc_cpuset(obj);
    }

    printf("\n");
}

}  // namespace cpuset
}  // namespace tt

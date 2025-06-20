/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#pragma once

#include <memory>
#include <mutex>
#include <unordered_map>

#include "umd/device/utils/robust_mutex.h"

namespace tt::umd {

enum class MutexType {
    // Used to serialize communication with the ARC.
    ARC_MSG,
    // Used to serialize communication with the remote ARC over ethernet.
    REMOTE_ARC_MSG,
    // Used to serialize IO operations which are done directly through TTDevice. This is needed since it goes through a
    // single TLB.
    TT_DEVICE_IO,
    // Used to serialize non-MMIO operations over ethernet.
    NON_MMIO,
    // Used to serialize memory barrier operations.
    MEM_BARRIER,
    // Used for calling CEM tool.
    CREATE_ETH_MAP,
};

// Note that the returned std::unique_lock<RobustMutex> should never outlive the LockManager which holds underlying
// RobustMutexes. Also note that clear_mutex doesn't need to be explicitly called, since the mutexes will all get
// cleared automatically when the LockManager goes out of scope. We could implement these lock such that initialization
// is not needed, and they are initialized every time they're locked, but since that communicates with the OS filesystem
// it might be slower do to it each time. This way, locking/unlocking should be faster.
class LockManager {
public:
    // This set of functions is used to manage mutexes which are system wide and not chip specific.
    void initialize_mutex(MutexType mutex_type);
    void clear_mutex(MutexType mutex_type);
    std::unique_lock<RobustMutex> acquire_mutex(MutexType mutex_type);

    // This set of functions is used to manage mutexes which are chip specific.
    void initialize_mutex(MutexType mutex_type, int pci_device_id);
    void clear_mutex(MutexType mutex_type, int pci_device_id);
    std::unique_lock<RobustMutex> acquire_mutex(MutexType mutex_type, int pci_device_id);

    // This set of functions is used to manage mutexes which are chip specific. This variant accepts custom mutex name.
    void initialize_mutex(std::string mutex_prefix, int pci_device_id);
    void clear_mutex(std::string mutex_prefix, int pci_device_id);
    std::unique_lock<RobustMutex> acquire_mutex(std::string mutex_prefix, int pci_device_id);

private:
    void initialize_mutex_internal(const std::string& mutex_name);
    void clear_mutex_internal(const std::string& mutex_name);
    std::unique_lock<RobustMutex> acquire_mutex_internal(const std::string& mutex_name);

    // Const map of mutex names for each of the types listed in the enum.
    static const std::unordered_map<MutexType, std::string> MutexTypeToString;

    // Maps from mutex name to an initialized mutex.
    // Mutex names are made from mutex type name or directly mutex name combined with device number.
    // Note that once LockManager is out of scope, all the mutexes will be cleared up automatically.
    std::unordered_map<std::string, RobustMutex> mutexes;
};

}  // namespace tt::umd

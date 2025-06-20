/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#include "umd/device/utils/lock_manager.h"

#include <tt-logger/tt-logger.hpp>

namespace tt::umd {

const std::unordered_map<MutexType, std::string> LockManager::MutexTypeToString = {
    {MutexType::ARC_MSG, "TT_ARC_MSG"},
    {MutexType::REMOTE_ARC_MSG, "TT_REMOTE_ARC_MSG"},
    // It is important that this mutex is named the same as corresponding fallback_tlb, this is due to the same tlb
    // index being used. This will be changed once we have a cleaner way to allocate TLBs instead of hardcoding fallback
    // tlbs.
    {MutexType::TT_DEVICE_IO, "SMALL_READ_WRITE_TLB"},
    {MutexType::NON_MMIO, "TT_NON_MMIO"},
    {MutexType::MEM_BARRIER, "TT_MEM_BARRIER"},
    {MutexType::CREATE_ETH_MAP, "CREATE_ETH_MAP"},
};

void LockManager::initialize_mutex(MutexType mutex_type) {
    initialize_mutex_internal(MutexTypeToString.at(mutex_type));
}

void LockManager::clear_mutex(MutexType mutex_type) { clear_mutex_internal(MutexTypeToString.at(mutex_type)); }

std::unique_lock<RobustMutex> LockManager::acquire_mutex(MutexType mutex_type) {
    return acquire_mutex_internal(MutexTypeToString.at(mutex_type));
}

void LockManager::initialize_mutex(MutexType mutex_type, int pci_device_id) {
    std::string mutex_name = MutexTypeToString.at(mutex_type) + "_" + std::to_string(pci_device_id);
    initialize_mutex_internal(mutex_name);
}

void LockManager::clear_mutex(MutexType mutex_type, int pci_device_id) {
    std::string mutex_name = MutexTypeToString.at(mutex_type) + "_" + std::to_string(pci_device_id);
    clear_mutex_internal(mutex_name);
}

std::unique_lock<RobustMutex> LockManager::acquire_mutex(MutexType mutex_type, int pci_device_id) {
    std::string mutex_name = MutexTypeToString.at(mutex_type) + "_" + std::to_string(pci_device_id);
    return acquire_mutex_internal(mutex_name);
}

void LockManager::initialize_mutex(std::string mutex_prefix, int pci_device_id) {
    std::string mutex_name = mutex_prefix + "_" + std::to_string(pci_device_id);
    initialize_mutex_internal(mutex_name);
}

void LockManager::clear_mutex(std::string mutex_prefix, int pci_device_id) {
    std::string mutex_name = mutex_prefix + "_" + std::to_string(pci_device_id);
    clear_mutex_internal(mutex_name);
}

std::unique_lock<RobustMutex> LockManager::acquire_mutex(std::string mutex_prefix, int pci_device_id) {
    std::string mutex_name = mutex_prefix + "_" + std::to_string(pci_device_id);
    return acquire_mutex_internal(mutex_name);
}

void LockManager::initialize_mutex_internal(const std::string& mutex_name) {
    if (mutexes.find(mutex_name) != mutexes.end()) {
        log_warning(LogSiliconDriver, "Mutex already initialized: {}", mutex_name);
        return;
    }

    mutexes.emplace(mutex_name, RobustMutex(mutex_name));
    mutexes.at(mutex_name).initialize();
}

void LockManager::clear_mutex_internal(const std::string& mutex_name) {
    if (mutexes.find(mutex_name) == mutexes.end()) {
        log_warning(LogSiliconDriver, "Mutex not initialized or already cleared: {}", mutex_name);
        return;
    }
    // The destructor will automatically close the underlying mutex.
    mutexes.erase(mutex_name);
}

std::unique_lock<RobustMutex> LockManager::acquire_mutex_internal(const std::string& mutex_name) {
    if (mutexes.find(mutex_name) == mutexes.end()) {
        throw std::runtime_error("Mutex not initialized: " + mutex_name);
    }
    return std::unique_lock(mutexes.at(mutex_name));
}

}  // namespace tt::umd

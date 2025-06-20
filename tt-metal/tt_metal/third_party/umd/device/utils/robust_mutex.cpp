/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#include "umd/device/utils/robust_mutex.h"

#include <sys/mman.h>  // shm_open, shm_unlink, mmap, munmap,

#include "assert.hpp"
// PROT_READ, PROT_WRITE, MAP_SHARED, MAP_FAILED
#include <errno.h>     // errno, ENOENT
#include <fcntl.h>     // O_RDWR, O_CREATE
#include <pthread.h>   // pthread_mutexattr_init, pthread_mutexattr_setpshared, pthread_mutex_t
#include <sys/file.h>  // flock
#include <sys/stat.h>  // for fstat
#include <unistd.h>    // ftruncate, close

#include <stdexcept>
#include <tt-logger/tt-logger.hpp>

static constexpr int ALL_RW_PERMISSION = 0666;
static constexpr std::string_view UMD_LOCK_PREFIX = "TT_UMD_LOCK.";
// Any value which is unlikely to be found at random in the memory.
static constexpr uint64_t INITIALIZED_FLAG = 0x5454554d444d5458;  // TTUMDMTX

using namespace tt::umd;

// A small helper class which will ensure that the critical section is released in a RAII manner.
// flock ensures only multiprocess locking, but does not guarantee
// multithread locking. Due to that, we need to use multithread_mutex_ which guarantees multithread locking but not
// multiprocess locking. Note that flock is released automatically on process crash, and static multithread_mutex_
// is not persistent, so we're safe even if the process crashes in the critical section.
//
// One might wonder, if this is already a guaranteed critical section, why do we need to go through all the pain
// to setup pthread in shm? Quick benchmark gave this results averaged over 1 000 000 iterations:
//   RobustMutex constructor + initialization + destructor: 40752 ns
//   RobustMutex lock + unlock: 654 ns
class CriticalSectionScopeGuard {
public:
    CriticalSectionScopeGuard(int fd, pthread_mutex_t* pthread_mutex, std::string_view mutex_name) :
        fd_(fd), pthread_mutex_(pthread_mutex), mutex_name_(mutex_name) {
        TT_ASSERT(flock(fd_, LOCK_EX) == 0, "flock failed for mutex {} errno: {}", mutex_name_, std::to_string(errno));
        int err = pthread_mutex_lock(pthread_mutex_);
        if (err != 0) {
            // Try to unlock the flock without handling further exceptions.
            flock(fd_, LOCK_UN);
            TT_ASSERT(false, "pthread_mutex_lock failed for mutex {} errno: {}", mutex_name_, std::to_string(err));
        }
    }

    ~CriticalSectionScopeGuard() noexcept {
        // Use best effort to unlock the mutex and the flock and report warnings if something fails.
        int err = pthread_mutex_unlock(pthread_mutex_);
        if (err != 0) {
            // This is on the destructor path, so we don't want to throw an exception.
            log_warning(
                tt::LogSiliconDriver,
                "pthread_mutex_unlock failed for mutex {} errno: {}",
                mutex_name_,
                std::to_string(err));
        }
        if (flock(fd_, LOCK_UN) != 0) {
            // This is on the destructor path, so we don't want to throw an exception.
            log_warning(
                tt::LogSiliconDriver, "flock failed for mutex {} errno: {}", mutex_name_, std::to_string(errno));
        }
    }

private:
    int fd_;
    pthread_mutex_t* pthread_mutex_;
    std::string mutex_name_;
};

pthread_mutex_t RobustMutex::multithread_mutex_ = PTHREAD_MUTEX_INITIALIZER;

RobustMutex::RobustMutex(std::string_view mutex_name) : mutex_name_(mutex_name) {}

RobustMutex::~RobustMutex() noexcept { close_mutex(); }

RobustMutex::RobustMutex(RobustMutex&& other) noexcept {
    shm_fd_ = other.shm_fd_;
    mutex_wrapper_ptr_ = other.mutex_wrapper_ptr_;
    mutex_name_ = other.mutex_name_;

    // Invalidate the other object, so the destructor doesn't try to close the same resources.
    other.shm_fd_ = -1;
    other.mutex_wrapper_ptr_ = nullptr;
    other.mutex_name_ = "";
}

RobustMutex& RobustMutex::operator=(RobustMutex&& other) noexcept {
    if (this != &other) {
        close_mutex();  // clean up existing resources

        shm_fd_ = other.shm_fd_;
        mutex_wrapper_ptr_ = other.mutex_wrapper_ptr_;
        mutex_name_ = other.mutex_name_;

        // Invalidate the other object, so the destructor doesn't try to close the same resources.
        other.shm_fd_ = -1;
        other.mutex_wrapper_ptr_ = nullptr;
        other.mutex_name_ = "";
    }
    return *this;
}

void RobustMutex::initialize() {
    open_shm_file();

    // We need a critical section here in which we test if the mutex has been initialized, and if not initialize it.
    // If we don't create a critical section for this, then two processes could race, one to initialize the mutex and
    // the other one to use it before it is initialized. We use only a single
    // multithread_mutex_ for all different RobustMutex instances which can affect perf of these operations, but that is
    // fine since this is executed rarely, only on initialization and only once after booting the system. Regarding
    // flock perf, this happens only when initializing the mutex, so it is not a big deal.
    // The critical_section object will get destroyed at the end of this function or when an exception is thrown, so the
    // critical section will be released automatically.
    CriticalSectionScopeGuard critical_section(shm_fd_, &multithread_mutex_, mutex_name_);

    // Resize file if needed.
    bool file_was_resized = resize_shm_file();

    // We now open the mutex in the shared memory file.
    open_pthread_mutex();

    // Report warning in case:
    //  - File was not resized, but the initialized flag is wrong.
    //  - File was resized, but the initialized flag is correct (this is a bit unexpected, but theoretically possible).
    if (mutex_wrapper_ptr_->initialized != INITIALIZED_FLAG && !file_was_resized) {
        log_warning(
            tt::LogSiliconDriver,
            "The file was already of correct size, but the initialized flag is wrong. This could "
            "be due to previously failed initialization, or some other external factor. Mutex name: {}",
            mutex_name_);
    }
    if (mutex_wrapper_ptr_->initialized == INITIALIZED_FLAG && file_was_resized) {
        log_warning(
            tt::LogSiliconDriver,
            "The file was resized, but the initialized flag is correct. This is an unexpected "
            "case, the mutex might fail. Mutex name: {}",
            mutex_name_);
    }

    // Initialize the mutex if it wasn't properly initialized before.
    if (mutex_wrapper_ptr_->initialized != INITIALIZED_FLAG) {
        // We need to initialize the mutex here, since it is the first time it is being used.
        initialize_pthread_mutex_first_use();
    }
}

void RobustMutex::open_shm_file() {
    std::string shm_file_name = std::string(UMD_LOCK_PREFIX) + std::string(mutex_name_);

    // Store old mask and clear processes umask.
    // This will have an effect that the created files which back up named mutexes will have all permissions. This is
    // important to avoid permission issues between processes.
    auto old_umask = umask(0);

    // The EXCL flag will cause the call to fail if the file already exists.
    // The order of operations is important here. If we try to first open the file then create it, then a race condition
    // can occur where two processes fail to open the file and they race to create it. This way, always only one process
    // can successfully create the file.
    shm_fd_ = shm_open(shm_file_name.c_str(), O_RDWR | O_CREAT | O_EXCL, ALL_RW_PERMISSION);
    if (shm_fd_ == -1 && errno == EEXIST) {
        shm_fd_ = shm_open(shm_file_name.c_str(), O_RDWR, ALL_RW_PERMISSION);
    }

    // Restore old mask.
    umask(old_umask);

    TT_ASSERT(shm_fd_ != -1, "shm_open failed for mutex {} errno: {}", mutex_name_, std::to_string(errno));
}

bool RobustMutex::resize_shm_file() {
    size_t file_size = get_file_size(shm_fd_);
    size_t target_file_size = sizeof(pthread_mutex_wrapper);
    bool file_was_truncated = false;

    // Report warning if the file size is not as expected, but continue with the initialization.
    if (file_size != 0 && file_size != target_file_size) {
        log_warning(
            tt::LogSiliconDriver,
            "File size {} is not as expected {} for mutex {}. This could be due to new pthread library version, or "
            "some other external factor.",
            std::to_string(file_size),
            std::to_string(target_file_size),
            mutex_name_);
    }
    // If file size is different from the needed size, we should resize it to proper size.
    // This includes the case when file_size was just created and its size iz 0.
    if (file_size != target_file_size) {
        TT_ASSERT(
            ftruncate(shm_fd_, target_file_size) == 0,
            "ftruncate failed for mutex {} errno: {}",
            mutex_name_,
            std::to_string(errno));
        file_was_truncated = true;

        // Verify file size again. This time throw an exception.
        file_size = get_file_size(shm_fd_);
        TT_ASSERT(
            file_size == target_file_size,
            "File size {} is not as expected {} for mutex {}. This could be due to new pthread library version, or "
            "some other external factor.",
            std::to_string(file_size),
            std::to_string(target_file_size),
            mutex_name_);
    }

    return file_was_truncated;
}

void RobustMutex::open_pthread_mutex() {
    // Create a pthread_mutex based on the shared memory file descriptor
    void* addr = mmap(NULL, sizeof(pthread_mutex_wrapper), PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd_, 0);
    TT_ASSERT(addr != MAP_FAILED, "mmap failed for mutex {} errno: {}", mutex_name_, std::to_string(errno));
    mutex_wrapper_ptr_ = (pthread_mutex_wrapper*)addr;
}

void RobustMutex::initialize_pthread_mutex_first_use() {
    int err;
    pthread_mutexattr_t attr;
    err = pthread_mutexattr_init(&attr);
    TT_ASSERT(err == 0, "pthread_mutexattr_init failed for mutex {} errno: {}", mutex_name_, std::to_string(err));
    // This marks the mutex as being shared across processes. Not sure if this is necessary given that it resides in
    // shared memory.
    err = pthread_mutexattr_setpshared(&attr, PTHREAD_PROCESS_SHARED);
    TT_ASSERT(err == 0, "pthread_mutexattr_setpshared failed for mutex {} errno: {}", mutex_name_, std::to_string(err));
    // This marks the mutex as robust. This will have the effect in the case of process crashing, another process
    // waiting on the mutex will get the signal and will get the flag that the previous owner of mutex died, so it can
    // recover the mutex state.
    err = pthread_mutexattr_setrobust(&attr, PTHREAD_MUTEX_ROBUST);
    TT_ASSERT(err == 0, "pthread_mutexattr_setrobust failed for mutex {} errno: {}", mutex_name_, std::to_string(err));
    err = pthread_mutex_init(&(mutex_wrapper_ptr_->mutex), &attr);
    TT_ASSERT(err == 0, "pthread_mutex_init failed for mutex {} errno: {}", mutex_name_, std::to_string(err));
    // When we open an existing pthread in the future, there is no other way to check if it was initialized or not, so
    // we need to set this flag.
    mutex_wrapper_ptr_->initialized = INITIALIZED_FLAG;
}

size_t RobustMutex::get_file_size(int fd) {
    struct stat sb;
    TT_ASSERT(fstat(fd, &sb) == 0, "fstat failed for mutex {} errno: {}", mutex_name_, std::to_string(errno));
    return sb.st_size;
}

void RobustMutex::close_mutex() noexcept {
    if (mutex_wrapper_ptr_ != nullptr) {
        // Unmap the shared memory backed pthread_mutex object.
        if (munmap((void*)mutex_wrapper_ptr_, sizeof(pthread_mutex_wrapper)) != 0) {
            // This is on the destructor path, so we don't want to throw an exception.
            log_warning(
                tt::LogSiliconDriver, "munmap failed for mutex {} errno: {}", mutex_name_, std::to_string(errno));
        }
        mutex_wrapper_ptr_ = nullptr;
    }
    if (shm_fd_ != -1) {
        // Close shared memory file.
        if (close(shm_fd_) != 0) {
            // This is on the destructor path, so we don't want to throw an exception.
            log_warning(
                tt::LogSiliconDriver, "close failed for mutex {} errno: {}", mutex_name_, std::to_string(errno));
        }
        shm_fd_ = -1;
    }
}

void RobustMutex::unlock() {
    int err = pthread_mutex_unlock(&(mutex_wrapper_ptr_->mutex));
    if (err != 0) {
        TT_THROW(fmt::format("pthread_mutex_unlock failed for mutex {} errno: {}", mutex_name_, std::to_string(err)));
    }
}

void RobustMutex::lock() {
    int lock_res = pthread_mutex_lock(&(mutex_wrapper_ptr_->mutex));

    if (lock_res == EOWNERDEAD) {
        // Some other process crashed before unlocking the mutex.
        // We can recover the mutex state.
        int err = pthread_mutex_consistent(&(mutex_wrapper_ptr_->mutex));
        if (err != 0) {
            TT_THROW(fmt::format(
                "pthread_mutex_consistent failed for mutex {} errno: {}", mutex_name_, std::to_string(err)));
        }
    } else if (lock_res != 0) {
        TT_THROW(
            fmt::format("pthread_mutex_lock failed for mutex {} errno: {}", mutex_name_, std::to_string(lock_res)));
    }
}

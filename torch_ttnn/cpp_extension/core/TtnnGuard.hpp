#pragma once

#include <c10/core/DeviceGuard.h>

#include <ttnn/device.hpp>

#include "utils/extension_utils.hpp"

// =====================================
// ============= Device Guards =========
// =====================================

// PyTorch has an API for registering device guards.
// Device guards can be used to set the current "active" device,
// and e.g. error if the user provides an invalid device index.
//
// If your device doesn't support indices (e.g. foo:0 vs. foo:1),
// then the guards probably aren't needed.
//
// You can use it by creating a DeviceGuard class, registering it
// in PyTorch, and invoking the device guard before any kernels are called.
// For a more full-featured example of a device guard,
// check out the code at c10/cuda/CUDAGuard.h

// Represents the current "active" device.
// The device guard registered below is meant to show how a backend
// can integrate custom device guard with pytorch.
// For something like cuda this represents the current active cuda device,
// which is directly set using the cuda API calls cudaGetDevice/cudaSetDevice.
static uint16_t CURR_DEVICE = -1;

// Create and register a dummy device guard.
struct TtnnDeviceGuard final : public c10::impl::DeviceGuardImplInterface {
    static constexpr c10::DeviceType static_type = c10::DeviceType::PrivateUse1;
    TtnnDeviceGuard();
    explicit TtnnDeviceGuard(c10::DeviceType t);
    at::DeviceType type() const override;
    at::Device exchangeDevice(at::Device d) const override;
    at::Device getDevice() const override;
    void setDevice(at::Device d) const override;
    void uncheckedSetDevice(at::Device d) const noexcept override;
    at::Stream getStream(at::Device d) const noexcept override;
    // NB: These do NOT set the current device
    at::Stream exchangeStream(at::Stream) const noexcept override;
    at::DeviceIndex deviceCount() const noexcept override;

    // Event-related functions
    void record(
        void** /*event*/,
        const at::Stream& /*stream*/,
        const at::DeviceIndex /*device_index*/,
        const c10::EventFlag /*flag*/) const override;
    void block(void* /*event*/, const at::Stream& /*stream*/) const override;
    bool queryEvent(void* /*event*/) const override;
    void destroyEvent(void* /*event*/, const at::DeviceIndex /*device_index*/) const noexcept override;

    // Stream-related functions
    bool queryStream(const at::Stream& /*stream*/) const override;
    void synchronizeStream(const at::Stream& /*stream*/) const override;
};

struct TtnnGuard {
    explicit TtnnGuard() = delete;
    explicit TtnnGuard(at::DeviceIndex device_index);
    explicit TtnnGuard(at::Device device);
    TtnnGuard(const TtnnGuard&) = delete;
    TtnnGuard& operator=(const TtnnGuard&) = delete;
    TtnnGuard(TtnnGuard&& other) = delete;
    TtnnGuard& operator=(TtnnGuard&& other) = delete;

    void set_device(at::Device device);

    void reset_device(at::Device device);

    void set_index(at::DeviceIndex device_index);

    at::Device original_device() const;

    at::Device current_device() const;

    ttnn::MeshDevice* get_ttnn_device();

    static ttnn::MeshDevice* ttnn_device;

private:
    c10::impl::InlineDeviceGuard<TtnnDeviceGuard> guard_;
};

C10_REGISTER_GUARD_IMPL(PrivateUse1, TtnnDeviceGuard);
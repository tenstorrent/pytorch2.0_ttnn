#pragma once

#include <c10/core/DeviceGuard.h>
#include "extension_utils.hpp"
#include "ttnn/device.hpp"

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
    TtnnDeviceGuard() { LOGGING(""); }
    explicit TtnnDeviceGuard(c10::DeviceType t) {
        // LOGGING("");
        TORCH_INTERNAL_ASSERT(t == c10::DeviceType::PrivateUse1);
    }
    at::DeviceType type() const override {
        LOGGING("");
        return at::DeviceType::PrivateUse1;
    }
    at::Device exchangeDevice(at::Device d) const override {
        // LOGGING("");
        TORCH_INTERNAL_ASSERT(d.type() == at::DeviceType::PrivateUse1);
        TORCH_INTERNAL_ASSERT(d.index() < deviceCount(), "Error: device index ", d.index(), " does not exist.");
        at::Device old_device = getDevice();
        if (old_device.index() != d.index()) {
            // "set the active device"
            CURR_DEVICE = d.index();
        }
        return old_device;
    }
    at::Device getDevice() const override {
        // LOGGING("");
        return at::Device(at::DeviceType::PrivateUse1, CURR_DEVICE);
    }
    void setDevice(at::Device d) const override {
        // LOGGING("");
        TORCH_INTERNAL_ASSERT(d.type() == at::DeviceType::PrivateUse1);
        TORCH_INTERNAL_ASSERT(d.index() < deviceCount(), "Error: device index ", d.index(), " does not exist.");
        at::Device current_device = getDevice();
        if (current_device != d) {
            CURR_DEVICE = d.index();
        }
    }
    void uncheckedSetDevice(at::Device d) const noexcept override {
        // LOGGING("");
        auto current_device = getDevice();
        if (current_device != d) {
            CURR_DEVICE = d.index();
        }
    }
    at::Stream getStream(at::Device d) const noexcept override {
        // no-op
        return at::Stream(at::Stream::DEFAULT, d);
    }
    // NB: These do NOT set the current device
    at::Stream exchangeStream(at::Stream) const noexcept override {
        // no-op
        return at::Stream(at::Stream::DEFAULT, at::Device(at::DeviceType::PrivateUse1, CURR_DEVICE));
    }
    at::DeviceIndex deviceCount() const noexcept override {
        // Hardcoding the number of "valid" devices here at 2.
        return 2;
    }

    // Event-related functions
    void record(
        void** /*event*/,
        const at::Stream& /*stream*/,
        const at::DeviceIndex /*device_index*/,
        const c10::EventFlag /*flag*/) const override {
        TORCH_CHECK(false, at::DeviceType::PrivateUse1, " backend doesn't support events.");
    }
    void block(void* /*event*/, const at::Stream& /*stream*/) const override {
        LOGGING("");
        TORCH_CHECK(false, at::DeviceType::PrivateUse1, " backend doesn't support events.")
    }
    bool queryEvent(void* /*event*/) const override {
        LOGGING("");
        TORCH_CHECK(false, at::DeviceType::PrivateUse1, " backend doesn't support events.")
    }
    void destroyEvent(void* /*event*/, const at::DeviceIndex /*device_index*/) const noexcept override {}

    // Stream-related functions
    bool queryStream(const at::Stream& /*stream*/) const override { return true; }
    void synchronizeStream(const at::Stream& /*stream*/) const override {
        // Don't wait for anything.
    }
};

struct TtnnGuard {
    explicit TtnnGuard() = delete;
    explicit TtnnGuard(at::DeviceIndex device_index) : guard_(device_index) {}
    explicit TtnnGuard(at::Device device) : guard_(device) {}
    TtnnGuard(const TtnnGuard&) = delete;
    TtnnGuard& operator=(const TtnnGuard&) = delete;
    TtnnGuard(TtnnGuard&& other) = delete;
    TtnnGuard& operator=(TtnnGuard&& other) = delete;

    void set_device(at::Device device) { guard_.set_device(device); }

    void reset_device(at::Device device) { guard_.reset_device(device); }

    void set_index(at::DeviceIndex device_index) { guard_.set_index(device_index); }

    at::Device original_device() const { return guard_.original_device(); }

    at::Device current_device() const { return guard_.current_device(); }

    IDevice* get_ttnn_device() {
        LOGGING("");
        if (!ttnn_device) {
            ttnn_device = &ttnn::open_device(0);
        }
        return ttnn_device;
    }

    static IDevice* ttnn_device;

private:
    c10::impl::InlineDeviceGuard<TtnnDeviceGuard> guard_;
};

C10_REGISTER_GUARD_IMPL(PrivateUse1, TtnnDeviceGuard);
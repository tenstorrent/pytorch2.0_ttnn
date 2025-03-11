#include "TtnnGuard.hpp"

TtnnDeviceGuard::TtnnDeviceGuard() { LOGGING(""); }

TtnnDeviceGuard::TtnnDeviceGuard(c10::DeviceType t) {
    LOGGING("");
    TORCH_INTERNAL_ASSERT(t == c10::DeviceType::PrivateUse1);
}

at::DeviceType TtnnDeviceGuard::type() const {
    LOGGING("");
    return at::DeviceType::PrivateUse1;
}

at::Device TtnnDeviceGuard::exchangeDevice(at::Device d) const {
    LOGGING("");
    TORCH_INTERNAL_ASSERT(d.type() == at::DeviceType::PrivateUse1);
    TORCH_INTERNAL_ASSERT(d.index() < deviceCount(), "Error: device index ", d.index(), " does not exist.");
    at::Device old_device = getDevice();
    if (old_device.index() != d.index()) {
        // "set the active device"
        CURR_DEVICE = d.index();
    }
    return old_device;
}

at::Device TtnnDeviceGuard::getDevice() const {
    LOGGING("");
    return at::Device(at::DeviceType::PrivateUse1, CURR_DEVICE);
}

void TtnnDeviceGuard::setDevice(at::Device d) const {
    LOGGING("");
    TORCH_INTERNAL_ASSERT(d.type() == at::DeviceType::PrivateUse1);
    TORCH_INTERNAL_ASSERT(d.index() < deviceCount(), "Error: device index ", d.index(), " does not exist.");
    at::Device current_device = getDevice();
    if (current_device != d) {
        CURR_DEVICE = d.index();
    }
}

void TtnnDeviceGuard::uncheckedSetDevice(at::Device d) const noexcept {
    LOGGING("");
    auto current_device = getDevice();
    if (current_device != d) {
        CURR_DEVICE = d.index();
    }
}

at::Stream TtnnDeviceGuard::getStream(at::Device d) const noexcept {
    // no-op
    return at::Stream(at::Stream::DEFAULT, d);
}

at::Stream TtnnDeviceGuard::exchangeStream(at::Stream) const noexcept {
    // no-op
    return at::Stream(at::Stream::DEFAULT, at::Device(at::DeviceType::PrivateUse1, CURR_DEVICE));
}

at::DeviceIndex TtnnDeviceGuard::deviceCount() const noexcept {
    // Hardcoding the number of "valid" devices here at 2.
    return 2;
}

// Event-related functions
void TtnnDeviceGuard::record(
    void** /*event*/,
    const at::Stream& /*stream*/,
    const at::DeviceIndex /*device_index*/,
    const c10::EventFlag /*flag*/) const {
    TORCH_CHECK(false, at::DeviceType::PrivateUse1, " backend doesn't support events.");
}
void TtnnDeviceGuard::block(void* /*event*/, const at::Stream& /*stream*/) const {
    LOGGING("");
    TORCH_CHECK(false, at::DeviceType::PrivateUse1, " backend doesn't support events.")
}
bool TtnnDeviceGuard::queryEvent(void* /*event*/) const {
    LOGGING("");
    TORCH_CHECK(false, at::DeviceType::PrivateUse1, " backend doesn't support events.")
}
void TtnnDeviceGuard::destroyEvent(void* /*event*/, const at::DeviceIndex /*device_index*/) const noexcept {}

// Stream-related functions
bool TtnnDeviceGuard::queryStream(const at::Stream& /*stream*/) const { return true; }
void TtnnDeviceGuard::synchronizeStream(const at::Stream& /*stream*/) const {
    // Don't wait for anything.
}

// =====================================
// ============== TTNN Guard ===========
// =====================================
IDevice* TtnnGuard::ttnn_device = nullptr;

TtnnGuard::TtnnGuard(at::DeviceIndex device_index) : guard_(device_index) {}
TtnnGuard::TtnnGuard(at::Device device) : guard_(device) {}

void TtnnGuard::set_device(at::Device device) { guard_.set_device(device); }

void TtnnGuard::reset_device(at::Device device) { guard_.reset_device(device); }

void TtnnGuard::set_index(at::DeviceIndex device_index) { guard_.set_index(device_index); }

at::Device TtnnGuard::original_device() const { return guard_.original_device(); }

at::Device TtnnGuard::current_device() const { return guard_.current_device(); }

IDevice* TtnnGuard::get_ttnn_device() {
    LOGGING("");
    if (!ttnn_device) {
        ttnn_device = &ttnn::open_device(0);
    }
    return ttnn_device;
}
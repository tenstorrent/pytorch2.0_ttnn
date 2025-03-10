#include <c10/core/Allocator.h>

#include "extension_utils.hpp"

// A dummy allocator for the custom device, that secretly uses the CPU
// TODO: Do we have to implement this for the use of TTNN?
struct TtnnCustomAllocator final : at::Allocator {
    TtnnCustomAllocator() = default;
    at::DataPtr allocate(size_t nbytes) const override {
        LOGGING("");
        // Do not allocate any cpu space here
        void* data = nullptr;
        return {data, data, &ReportAndDelete, c10::Device(c10::DeviceType::PrivateUse1, 0)};
    }

    static void ReportAndDelete(void* ptr) {
        LOGGING("");
        TORCH_CHECK(ptr == nullptr)
    }

    at::DeleterFnPtr raw_deleter() const override { return &ReportAndDelete; }
};

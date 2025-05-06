#include "ttnn_cpp_extension/core/TtnnCustomAllocator.hpp"

#include "ttnn_cpp_extension/utils/extension_utils.hpp"

at::DataPtr TtnnCustomAllocator::allocate(size_t nbytes) const {
    LOGGING("");
    // Do not allocate any cpu space here
    void* data = nullptr;
    return {data, data, &ReportAndDelete, c10::Device(c10::DeviceType::PrivateUse1, 0)};
}

void TtnnCustomAllocator::ReportAndDelete(void* ptr) {
    LOGGING("");
    TORCH_CHECK(ptr == nullptr)
}

at::DeleterFnPtr TtnnCustomAllocator::raw_deleter() const { return &ReportAndDelete; }

TtnnCustomAllocator& get_ttnn_custom_allocator() {
    static TtnnCustomAllocator allocator;
    return allocator;
}

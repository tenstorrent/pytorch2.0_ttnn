#pragma once

#include <c10/core/Allocator.h>
#include <cstddef>

// A dummy allocator used for creating Storage for Torch Tensors
// This should not use any actual space (data is stored in DRAM, not CPU RAM)
struct TtnnCustomAllocator final : c10::Allocator {
    TtnnCustomAllocator() = default;
    c10::DataPtr allocate(size_t nbytes) override;

    static void ReportAndDelete(void* ptr);

    bool is_simple_data_ptr(const c10::DataPtr& data_ptr) const override;

    c10::DeleterFnPtr raw_deleter() const override;

    void copy_data(void* dest, const void* src, std::size_t count) const override;
};

TtnnCustomAllocator& get_ttnn_custom_allocator();

#pragma once

#include <c10/core/Allocator.h>

// A dummy allocator used for creating Storage for Torch Tensors
// This should not use any actual space (data is stored in DRAM, not CPU RAM)
struct TtnnCustomAllocator final : at::Allocator {
    TtnnCustomAllocator() = default;
    at::DataPtr allocate(size_t nbytes) const override;

    static void ReportAndDelete(void* ptr);

    at::DeleterFnPtr raw_deleter() const override;
};

TtnnCustomAllocator& get_ttnn_custom_allocator();
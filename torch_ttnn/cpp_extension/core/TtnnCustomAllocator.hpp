#include <c10/core/Allocator.h>

#include "extension_utils.hpp"

// A dummy allocator used for creating Storage for Torch Tensors
// This should not use any actual space
struct TtnnCustomAllocator final : at::Allocator {
    TtnnCustomAllocator() = default;
    at::DataPtr allocate(size_t nbytes) const override;

    static void ReportAndDelete(void* ptr);

    at::DeleterFnPtr raw_deleter() const override;
};

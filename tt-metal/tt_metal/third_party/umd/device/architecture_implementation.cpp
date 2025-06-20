// SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0

#include "umd/device/architecture_implementation.h"

#include "umd/device/blackhole_implementation.h"
#include "umd/device/wormhole_implementation.h"

namespace tt::umd {

std::unique_ptr<architecture_implementation> architecture_implementation::create(tt::ARCH architecture) {
    switch (architecture) {
        case tt::ARCH::BLACKHOLE:
            return std::make_unique<blackhole_implementation>();
        case tt::ARCH::WORMHOLE_B0:
            return std::make_unique<wormhole_implementation>();
        default:
            return nullptr;
    }
}

}  // namespace tt::umd

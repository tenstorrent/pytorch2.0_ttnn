/*
 * SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include <cstdint>

namespace tt::umd {

struct HarvestingMasks {
    size_t tensix_harvesting_mask = 0;
    size_t dram_harvesting_mask = 0;
    size_t eth_harvesting_mask = 0;
    size_t pcie_harvesting_mask = 0;

    HarvestingMasks operator|(const HarvestingMasks& other) const {
        return HarvestingMasks{
            .tensix_harvesting_mask = this->tensix_harvesting_mask | other.tensix_harvesting_mask,
            .dram_harvesting_mask = this->dram_harvesting_mask | other.dram_harvesting_mask,
            .eth_harvesting_mask = this->eth_harvesting_mask | other.eth_harvesting_mask,
            .pcie_harvesting_mask = this->pcie_harvesting_mask | other.pcie_harvesting_mask};
    }
};

}  // namespace tt::umd

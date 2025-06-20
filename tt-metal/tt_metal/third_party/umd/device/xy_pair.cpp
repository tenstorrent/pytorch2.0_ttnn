/*
 * SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include "umd/device/types/xy_pair.h"

#include <fmt/core.h>

namespace tt::umd {

std::string xy_pair::str() const { return fmt::format("(x={},y={})", x, y); }

std::string cxy_pair::str() const { return fmt::format("(chip={},x={},y={})", chip, x, y); }

}  // namespace tt::umd

// SPDX-FileCopyrightText: © 2024 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0

#pragma once

#include "ttnn/run_operation.hpp"

namespace ttnn::operations::data_movement::detail {


tt::tt_metal::operation::ProgramWithCallbacks interleaved_to_sharded_multi_core(const Tensor &a, const Tensor &output, bool keep_l1_aligned = false, uint32_t num_slices = 1, uint32_t slice_index = 0);

}

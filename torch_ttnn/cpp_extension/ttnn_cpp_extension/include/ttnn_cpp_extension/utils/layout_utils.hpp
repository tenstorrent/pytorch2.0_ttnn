#pragma once

#include <ttnn/tensor/tensor.hpp>
#include "ttnn/operations/data_movement/tilize/tilize.hpp"

namespace tt_eager::utils {

/**
 * @brief Ensures that a tensor has TILE_LAYOUT for operations that require it
 * @param tensor The input tensor to check/convert
 * @return The tensor with TILE_LAYOUT
 */
inline ttnn::Tensor ensure_tile_layout(const ttnn::Tensor& tensor) {
    if (tensor.layout() == ttnn::ROW_MAJOR_LAYOUT) {
        return ttnn::tilize(
            ttnn::QueueId(0),
            tensor,
            /*memory_config=*/std::nullopt,
            /*output_dtype=*/std::nullopt,
            /*use_multicore=*/true);
    }
    return tensor;
}

}  // namespace tt_eager::utils
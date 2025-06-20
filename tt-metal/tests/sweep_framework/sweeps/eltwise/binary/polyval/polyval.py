# SPDX-FileCopyrightText: © 2024 Tenstorrent Inc.

# SPDX-License-Identifier: Apache-2.0

from typing import Optional, Tuple

import torch
import random
import ttnn

from tests.ttnn.utils_for_testing import check_with_pcc, start_measuring_time, stop_measuring_time

# Override the default timeout in seconds for hang detection.
TIMEOUT = 30

random.seed(0)

# Parameters provided to the test vector generator are defined here.
# They are defined as dict-type suites that contain the arguments to the run function as keys, and lists of possible inputs as values.
# Each suite has a key name (in this case "suite_1") which will associate the test vectors to this specific suite of inputs.
# Developers can create their own generator functions and pass them to the parameters as inputs.
parameters = {
    "nightly": {
        "batch_sizes": [(1, 2)],
        "height": [384, 1024],
        "width": [1024, 4096],
        "input_dtype": [ttnn.bfloat16, ttnn.bfloat8_b],
        "input_memory_config": [ttnn.DRAM_MEMORY_CONFIG],
        "output_memory_config": [ttnn.DRAM_MEMORY_CONFIG],
        "layout": [ttnn.TILE_LAYOUT, ttnn.ROW_MAJOR_LAYOUT],
        "coeff": [(3.6, 23.6, 1.7, 4.6), (9.4, 4.2, 3.3, 9.0)],
    },
}


def torch_polyval(input_tensor, coeff):
    curVal = 0
    for curValIndex in range(len(coeff) - 1):
        curVal = (curVal + coeff[curValIndex]) * input_tensor[0]
    return curVal + coeff[len(coeff) - 1]


# Invalidate vector is called during the generation phase where each vector will be passed in.
# If invalidated, the vector will still be stored but will be skipped.
# Returns False, None if the vector is valid, and True, str with a reason for invalidation if it is invalid.
def invalidate_vector(test_vector) -> Tuple[bool, Optional[str]]:
    if test_vector["layout"] == ttnn.ROW_MAJOR_LAYOUT:
        return True, "Row Major layout is not supported"
    return False, None


# This is the run instructions for the test, defined by the developer.
# The run function must take the above-defined parameters as inputs.
# The runner will call this run function with each test vector, and the returned results from this function will be stored.
# If you defined a device_mesh_fixture above, the object you yielded will be passed into this function as 'device'. Otherwise, it will be the default ttnn device opened by the infra.
def run(
    batch_sizes,
    height,
    width,
    input_dtype,
    input_memory_config,
    output_memory_config,
    layout,
    coeff,
    *,
    device,
) -> list:
    input_shape = (*batch_sizes, height, width)

    torch_input_tensor = torch.randn(input_shape, dtype=torch.float32)
    torch_output_tensor = torch_polyval(torch_input_tensor, coeff)

    input_tensor = ttnn.from_torch(
        torch_input_tensor, dtype=input_dtype, device=device, memory_config=input_memory_config, layout=layout
    )
    start_time = start_measuring_time()
    output_tensor = ttnn.polyval(input_tensor, coeff, memory_config=output_memory_config)
    output_tensor = ttnn.to_torch(output_tensor).squeeze(0)
    e2e_perf = stop_measuring_time(start_time)

    return [check_with_pcc(torch_output_tensor, output_tensor, 0.999), e2e_perf]

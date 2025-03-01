# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
import pytest


class Module(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1):
        t2 = torch.nn.functional.relu(t1)
        t3 = torch.nn.functional.silu(t2)
        t4 = torch.nn.functional.gelu(t2)
        t5 = torch.nn.functional.tanh(t4)
        t6 = t2 + t3 + t5
        return t6


@pytest.mark.parametrize(
    "test_name, input_shape",
    [
        ("eviction", (100, 3, 224, 224)),
    ],
)
def test_eviction(device, test_name, input_shape):
    m = Module()
    m = m.to(torch.bfloat16)
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    option = torch_ttnn.TorchTtnnOption(device=device, run_mem_analysis=True, gen_graphviz=True)
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result = m.forward(input)

    mm = option.memory_manager
    # These are for plotting charts for later inspection
    from tools.plot_chart import (
        plot_mem_footprint_bar_chart,
        plot_mem_footprint_line_chart,
    )

    bar_chart_file = f"tests/memory/eviction/before_eviction_bar_chart.png"
    line_chart_file = f"tests/memory/eviction/before_eviction_line_chart.png"
    plot_mem_footprint_bar_chart(mm.data_points, bar_chart_file)
    plot_mem_footprint_line_chart(mm.data_points, line_chart_file)

    # From the memory footprint, this checks whether the model fits in memory or not
    model_fits_in_memory = not option.memory_manager.has_sram_overflow()

    assert model_fits_in_memory == False, "Before eviction, model should NOT fit in memory"
    assert option.memory_manager.used_sram == 0, "There are still tensors on device after model execution"
    assert (
        option.memory_manager.free_sram == option.memory_manager.usable_sram_limit
    ), "Tensors still occupy space on sram after model execution"
    assert option.memory_manager.tensors_on_device == [], "All tensors should be removed post model execution"

    # Compile the model again this time with eviction opt turned ON

    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    option = torch_ttnn.TorchTtnnOption(device=device, run_mem_analysis=True, run_eviction_opt=True, gen_graphviz=True)
    m = Module()
    m = m.to(torch.bfloat16)
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result = m.forward(input)

    # From the memory footprint, this checks whether the model fits in memory or not
    model_fits_in_memory = not option.memory_manager.has_sram_overflow()

    mm = option.memory_manager
    # These are for plotting charts for later inspection
    from tools.plot_chart import (
        plot_mem_footprint_bar_chart,
        plot_mem_footprint_line_chart,
    )

    bar_chart_file = f"tests/memory/eviction/after_eviction_bar_chart.png"
    line_chart_file = f"tests/memory/eviction/after_eviction_line_chart.png"
    plot_mem_footprint_bar_chart(mm.data_points, bar_chart_file)
    plot_mem_footprint_line_chart(mm.data_points, line_chart_file)

    log_file = f"tests/memory/eviction/memory_footprint.txt"
    with open(log_file, "w") as f:
        f.write(mm.logs)

    assert model_fits_in_memory == True, "After eviction, model should fit in memory"
    assert option.memory_manager.used_sram == 0, "There are still tensors on device after model execution"
    assert (
        option.memory_manager.free_sram == option.memory_manager.usable_sram_limit
    ), "Tensors still occupy space on sram after model execution"
    assert option.memory_manager.tensors_on_device == [], "All tensors should be removed post model execution"

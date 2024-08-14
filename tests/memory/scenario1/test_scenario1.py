import torch
import torch_ttnn
import pytest
import ttnn
import torch.nn as nn
import torch.nn.functional as F


class Module(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 16, 5)

    def forward(self, t1):
        t2 = F.relu(t1)
        t3 = F.tanh(t2)
        t4 = torch.squeeze(t2)
        t5 = torch.squeeze(t3)
        t6 = t4 + t5
        return t6


@pytest.mark.parametrize(
    "test_name, input_shape, model_fits_in_memory",
    [("scenario1_case0", (32, 1, 224, 224), True),
     ("scenario1_case1", (100, 10, 224, 224), False)],
)
def test_scenario(device, test_name, input_shape, model_fits_in_memory):
    m = Module()
    m = m.to(torch.bfloat16)
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    option.run_mem_analysis = True
    option.run_eviction_opt = True
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result = m.forward(input)

    # These are for plotting charts for later inspection
    from tools.memory_models.plot_chart import plot_bar_chart, plot_line_chart
    src_file = "./data/memory/memory_footprint.txt"
    bar_chart_file = "./tests/memory/scenario1/"+test_name+"_bar_chart.png"
    line_chart_file = "./tests/memory/scenario1/"+test_name+"_line_chart.png"
    plot_bar_chart(src_file, bar_chart_file)
    plot_line_chart(src_file, line_chart_file)

    # From the memory footprint, this checks whether the model fits in memory or not
    can_fit_in_memory = not option._memory_manager.has_sram_overflow()
    
    assert can_fit_in_memory == model_fits_in_memory, "Expected fit & actual fit of model is different"
    assert option._memory_manager.used_sram == 0, "There are still tensors on device after model execution"
    assert option._memory_manager.free_sram == option._memory_manager.usable_sram_limit, "Tensors still occupy space on sram after model execution"
    assert option._memory_manager.tensors_on_device == [], "All tensors should be removed post model execution"
    

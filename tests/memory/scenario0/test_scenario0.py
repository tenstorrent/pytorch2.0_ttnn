import torch
import torch_ttnn
import pytest
import ttnn
import torch.nn.functional as F


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
    "test_name, input_shape, model_fits_in_memory",
    [("scenario0_case0", (32, 3, 224, 224), True),
     ("scenario0_case1", (100, 3, 224, 224), False)],
)
def test_scenario(device, test_name, input_shape, model_fits_in_memory):
    m = Module()
    m = m.to(torch.bfloat16)
    input = torch.rand(input_shape, dtype=torch.bfloat16)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.memory_backend, options=option)
    result = m.forward(input)

    # These are for plotting charts for later inspection
    from tools.memory_models.plot_chart import plot_bar_chart, plot_line_chart
    src_file = "./data/memory/memory_footprint.txt"
    bar_chart_file = "./tests/memory/scenario0/"+test_name+"_bar_chart.png"
    line_chart_file = "./tests/memory/scenario0/"+test_name+"_line_chart.png"
    plot_bar_chart(src_file, bar_chart_file)
    plot_line_chart(src_file, line_chart_file)

    # From the memory footprint, this checks whether the model fits in memory or not
    can_fit_in_memory = True
    sram_limit = 104857600 # 100 * 1024 * 1024 bytes (100 MB)
    for _, value in option._memory_manager.mem_data.items():
        used_sram = 0
        for _, size in value:
            used_sram += size
            if used_sram >= sram_limit:
                can_fit_in_memory = False
                break
    
    assert can_fit_in_memory == model_fits_in_memory, "Model fits in SRAM memory, this test case failed!"
    assert option._memory_manager.used_sram == 0, "There are still tensors on device after model execution"
    assert option._memory_manager.free_sram == sram_limit, "Tensors still occupy space on sram after model execution"
    assert option._memory_manager.tensors_on_device == [], "All tensors should be removed post model execution"
    
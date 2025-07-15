# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import torch_ttnn
from tests.models.mamba.mamba_ssm.model import Mamba
from transformers import AutoTokenizer
from tools.plot_chart import (
    plot_mem_footprint_bar_chart,
    plot_mem_footprint_line_chart,
)

torch._dynamo.config.suppress_errors = True


def get_model_and_inputs():
    # Initialize the model and tokenizer
    model = Mamba.from_pretrained("state-spaces/mamba-2.8b-slimpj")
    model = model.to(torch.bfloat16)
    model.eval()  # Set the model to evaluation mode
    tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neox-20b")

    # Prepare the input tensor
    prompt = "Climate change refers to long-term shifts in temperatures and weather patterns. Such shifts can be natural due to changes in the sun's activity or volcanic eruptions."
    input_ids = tokenizer(prompt, return_tensors="pt")["input_ids"]

    # Sample run
    model_output = model(input_ids)

    # Return the model and input tensor
    return model, input_ids


def test_mamba(device):
    model, input_ids = get_model_and_inputs()

    option = torch_ttnn.TorchTtnnOption(device=device, run_mem_analysis=True, gen_graphviz=True)
    m = torch.compile(model, backend=torch_ttnn.backend, options=option)
    result = m.forward(input_ids)

    mm = option.memory_manager

    bar_chart_file = f"tests/memory/mamba/mem_analysis_bar_chart.png"
    line_chart_file = f"tests/memory/mamba/mem_analysis_line_chart.png"
    plot_mem_footprint_bar_chart(mm.data_points, bar_chart_file)
    plot_mem_footprint_line_chart(mm.data_points, line_chart_file)

    has_sram_overflow = mm.has_sram_overflow()

    print("has_sram_overflow:", has_sram_overflow)

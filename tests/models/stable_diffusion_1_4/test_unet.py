# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import pytest
from diffusers import UNet2DConditionModel
from tests.utils import ModelTester, repeat_inputs

class StableDiffusion14UNetTester(ModelTester):
    def _load_model(self):
        model_id = "CompVis/stable-diffusion-v1-4"
        # 重点：只提取并测试 UNet 部分，这是 SD 的核心算力消耗点
        m = UNet2DConditionModel.from_pretrained(model_id, subfolder="unet", torch_dtype=torch.bfloat16)
        for param in m.parameters():
            param.requires_grad = False
        return m

    def _load_inputs(self, batch_size):
        # 模拟 SD 1.4 UNet 的标准输入：latents (4, 64, 64), timestep, encoder_hidden_states (1, 77, 768)
        latents = torch.randn(batch_size, 4, 64, 64, dtype=torch.bfloat16)
        timestep = torch.tensor([1], dtype=torch.long)
        encoder_hidden_states = torch.randn(batch_size, 77, 768, dtype=torch.bfloat16)
        return {"sample": latents, "timestep": timestep, "encoder_hidden_states": encoder_hidden_states}

@pytest.mark.parametrize("mode", ["eval"])
def test_sd14_unet(record_property, mode):
    model_name = "SD1.4-UNet"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = StableDiffusion14UNetTester(model_name, mode)
    results = tester.test_model()
    
    record_property("torch_ttnn", (tester, results))

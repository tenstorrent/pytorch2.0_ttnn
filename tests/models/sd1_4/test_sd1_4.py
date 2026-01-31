# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import pytest
from diffusers import StableDiffusionPipeline
from tests.utils import ModelTester, repeat_inputs

class SD14UNetTester(ModelTester):
    def _load_model(self):
        # We only benchmark the UNet component which is the compute bottleneck
        pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16)
        m = pipe.unet
        m.eval()
        for param in m.parameters():
            param.requires_grad = False
        return m

    def _load_inputs(self, batch_size):
        # Standard input shapes for SD 1.4 UNet (Latent Diffusion)
        sample = torch.randn((batch_size, 4, 64, 64), dtype=torch.float16)
        timestep = torch.tensor([1], dtype=torch.float16)
        encoder_hidden_states = torch.randn((batch_size, 77, 768), dtype=torch.float16)
        return {"sample": sample, "timestep": timestep, "encoder_hidden_states": encoder_hidden_states}

@pytest.mark.parametrize("mode", ["eval"])
def test_sd1_4_unet(record_property, mode):
    model_name = "SD1.4-UNet"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = SD14UNetTester(model_name, mode)
    results = tester.test_model()
    
    if mode == "eval":
        print(f"{model_name} inference pass complete.")

    record_property("torch_ttnn", (tester, results))

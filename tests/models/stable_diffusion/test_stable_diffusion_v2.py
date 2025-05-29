# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
from diffusers import StableDiffusionPipeline, UNet2DConditionModel, LMSDiscreteScheduler
from transformers import CLIPTextModel, CLIPTokenizer
import pytest
from tests.utils import ModelTester, repeat_inputs


class ThisTester(ModelTester):
    def _load_model(self):
        # Load the pre-trained model and tokenizer
        self.tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-large-patch14")
        self.text_encoder = CLIPTextModel.from_pretrained("openai/clip-vit-large-patch14")
        unet = UNet2DConditionModel.from_pretrained(
            "CompVis/stable-diffusion-v1-4", subfolder="unet", torch_dtype=torch.bfloat16
        )
        self.scheduler = LMSDiscreteScheduler.from_pretrained("CompVis/stable-diffusion-v1-4", subfolder="scheduler")
        return unet

    def _load_inputs(self, batch_size):
        # Prepare the text prompt
        prompt = "A fantasy landscape with mountains and rivers"
        text_input = self.tokenizer(prompt, return_tensors="pt")
        text_embeddings = self.text_encoder(text_input.input_ids)[0]

        # Generate noise
        batch_size = text_embeddings.shape[0]
        height, width = 512, 512  # Output image size
        latents = torch.randn((batch_size, self.model.in_channels, height // 8, width // 8))

        # Set number of diffusion steps
        num_inference_steps = 1
        self.scheduler.set_timesteps(num_inference_steps)

        # Scale the latent noise to match the model's expected input
        latents = latents * self.scheduler.init_noise_sigma

        # Get the model's predicted noise
        latent_model_input = self.scheduler.scale_model_input(latents, 0)
        arguments = {
            "sample": latent_model_input.to(torch.bfloat16),
            "timestep": 0,
            "encoder_hidden_states": text_embeddings.to(torch.bfloat16),
        }
        arguments = repeat_inputs(arguments, batch_size)
        return arguments


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.compilation_xfail
def test_stable_diffusion_v2(record_property, mode):
    model_name = "Stable Diffusion V2"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()
    if mode == "eval":
        noise_pred = results.sample

    record_property("torch_ttnn", (tester, results))

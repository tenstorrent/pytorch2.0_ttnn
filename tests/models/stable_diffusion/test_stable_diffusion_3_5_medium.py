# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
"""
Test for Stable Diffusion 3.5 Medium (512x512)
GitHub Issue #1042: Add model: Stable Diffusion 3.5 medium (512x512)

Target: 0.3 FPS on batch 1
Baseline: 0.06 FPS on batch 1
"""
from diffusers import StableDiffusion3Pipeline
import torch
import pytest
from tests.utils import ModelTester, repeat_inputs


class ThisTester(ModelTester):
    def _load_model(self):
        # Use SD 3.5 Medium - requires HuggingFace authentication for gated model
        model_id = "stabilityai/stable-diffusion-3.5-medium"
        pipe = StableDiffusion3Pipeline.from_pretrained(
            model_id,
            torch_dtype=torch.bfloat16,  # SD 3.5 uses bfloat16
        )
        return pipe

    def _load_inputs(self, batch_size):
        prompt = "a photo of an astronaut riding a horse on mars"
        prompt = repeat_inputs(prompt, batch_size)
        return prompt


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
def test_stable_diffusion_3_5_medium(record_property, mode):
    """Test Stable Diffusion 3.5 Medium model performance."""
    model_name = "Stable Diffusion 3.5 Medium"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()
    if mode == "eval":
        image = results.images[0]

    record_property("torch_ttnn", (tester, results))
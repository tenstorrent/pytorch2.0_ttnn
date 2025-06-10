# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
# https://huggingface.co/runwayml/stable-diffusion-v1-5
from diffusers import StableDiffusionPipeline
import torch
import pytest
from tests.utils import ModelTester, repeat_inputs


class ThisTester(ModelTester):
    def _load_model(self):
        model_id = "CompVis/stable-diffusion-v1-4"
        pipe = StableDiffusionPipeline.from_pretrained(model_id)
        return pipe

    def _load_inputs(self, batch_size):
        prompt = "a photo of an astronaut riding a horse on mars"
        prompt = repeat_inputs(prompt, batch_size)
        return prompt


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.skip(reason="Dynamo cannot support pipeline.")
def test_stable_diffusion(record_property, mode):
    model_name = "Stable Diffusion"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()
    if mode == "eval":
        image = results.images[0]

    record_property("torch_ttnn", (tester, results))

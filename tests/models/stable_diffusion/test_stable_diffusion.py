# https://huggingface.co/runwayml/stable-diffusion-v1-5
from diffusers import StableDiffusionPipeline
import torch
import pytest


@pytest.mark.compilation_xfail
def test_stable_diffusion(record_property):
    record_property("model_name", "Stable Diffusion")

    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(model_id)

    prompt = "a photo of an astronaut riding a horse on mars"
    output = pipe(prompt)
    image = output.images[0]

    record_property("torch_ttnn", (pipe, prompt, output))

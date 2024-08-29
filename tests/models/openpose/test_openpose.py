# Reference: https://huggingface.co/lllyasviel/control_v11p_sd15_openpose

import torch
from pathlib import Path
from diffusers.utils import load_image
from controlnet_aux import OpenposeDetector
import pytest


@pytest.mark.compilation_xfail
def test_openpose(record_property):
    record_property("model_name", "OpenPose")

    image = load_image("https://huggingface.co/lllyasviel/control_v11p_sd15_openpose/resolve/main/images/input.png")

    model = OpenposeDetector.from_pretrained("lllyasviel/ControlNet")

    arguments = {"input_image": image, "hand_and_face": True}
    control_image = model(**arguments)

    record_property("torch_ttnn", (model, arguments, control_image))

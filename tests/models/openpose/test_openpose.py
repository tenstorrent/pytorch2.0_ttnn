# Reference: https://huggingface.co/lllyasviel/control_v11p_sd15_openpose

import torch
from pathlib import Path
from diffusers.utils import load_image
import pytest
from tests.utils import ModelTester

dependencies = ["controlnet_aux==0.0.9"]


class ThisTester(ModelTester):
    def _load_model(self):
        from controlnet_aux import OpenposeDetector

        model = OpenposeDetector.from_pretrained("lllyasviel/ControlNet")
        model = model.to(torch.bfloat16)
        return model

    def _load_inputs(self):
        image = load_image("https://huggingface.co/lllyasviel/control_v11p_sd15_openpose/resolve/main/images/input.png")
        arguments = {"input_image": image, "hand_and_face": True}
        return arguments


@pytest.mark.parametrize(
    "mode",
    ["train", "eval"],
)
@pytest.mark.usefixtures("manage_dependencies")
@pytest.mark.skip(reason="failing during torch run with bypass compilation")
def test_openpose(record_property, mode):
    model_name = "OpenPose"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()

    record_property("torch_ttnn", (tester, results))

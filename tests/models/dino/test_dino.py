# Reference: https://huggingface.co/facebook/dinov2-base

import torch
import pytest
import requests

from PIL import Image
from transformers import AutoImageProcessor, AutoModel
from tests.utils import ModelTester


class ThisTester(ModelTester):
    def _load_model(self):
        # Download model from cloud
        model_name = "facebook/dinov2-base"
        self.image_processor = AutoImageProcessor.from_pretrained(
            model_name,
        )
        model = AutoModel.from_pretrained(model_name, torch_dtype=torch.bfloat16)
        return model

    def _load_inputs(self):
        # Set up sample input
        self.test_input = "http://images.cocodataset.org/val2017/000000039769.jpg"
        self.image = Image.open(requests.get(self.test_input, stream=True).raw)

        inputs = self.image_processor(images=self.image, return_tensors="pt")
        inputs["pixel_values"] = inputs["pixel_values"].to(torch.bfloat16)
        return inputs


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
def test_dino(record_property, mode):
    model_name = "DINOv2"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()
    results = results.last_hidden_state

    record_property("torch_ttnn", (tester, results))

# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
from PIL import Image
import requests
import torch
from transformers import CLIPProcessor, CLIPModel
import pytest
from tests.utils import ModelTester


class ThisTester(ModelTester):
    def _load_model(self):
        model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32", torch_dtype=torch.bfloat16)
        self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32", torch_dtype=torch.bfloat16)
        return model

    def _load_inputs(self):
        url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        image = Image.open(requests.get(url, stream=True).raw)

        inputs = self.processor(
            text=["a photo of a cat", "a photo of a dog"],
            images=image,
            return_tensors="pt",
            padding=True,
        )
        inputs["pixel_values"] = inputs["pixel_values"].to(torch.bfloat16)
        return inputs

    def set_inputs_train(self, inputs):
        inputs["pixel_values"].requires_grad_(True)
        return inputs

    def append_fake_loss_function(self, outputs):
        return (
            torch.mean(outputs.logits_per_image)
            + torch.mean(outputs.logits_per_text)
            + torch.mean(outputs.text_embeds[0])
            + torch.mean(outputs.text_embeds[0])
        )

    def get_results_train(self, model, inputs, outputs):
        return inputs["pixel_values"].grad


@pytest.mark.parametrize(
    "mode",
    [
        pytest.param(
            "train",
            marks=pytest.mark.compilation_xfail,
        ),
        "eval",
    ],
)
def test_clip(record_property, mode):
    model_name = "CLIP"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()

    if mode == "eval":
        logits_per_image = results.logits_per_image  # this is the image-text similarity score
        probs = logits_per_image.softmax(dim=1)  # we can take the softmax to get the label probabilities

    record_property("torch_ttnn", (tester, results))

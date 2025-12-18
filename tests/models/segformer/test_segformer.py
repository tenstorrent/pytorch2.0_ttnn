# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
# Reference: https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512

from transformers import SegformerImageProcessor, SegformerForSemanticSegmentation
from PIL import Image
import requests
import pytest
from tests.utils import ModelTester, repeat_inputs
import torch


class ThisTester(ModelTester):
    def _load_model(self):
        self.processor = SegformerImageProcessor.from_pretrained("nvidia/segformer-b0-finetuned-ade-512-512")
        model = SegformerForSemanticSegmentation.from_pretrained("nvidia/segformer-b0-finetuned-ade-512-512")
        model = model.to(torch.bfloat16)
        return model

    def _load_inputs(self, batch_size):
        url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        image = Image.open(requests.get(url, stream=True).raw)
        inputs = self.processor(images=image, return_tensors="pt")
        inputs["pixel_values"] = inputs["pixel_values"].to(torch.bfloat16)
        inputs = repeat_inputs(inputs, batch_size)
        return inputs

    def set_inputs_train(self, inputs):
        inputs["pixel_values"] = inputs["pixel_values"].requires_grad_(True)
        return inputs

    def append_fake_loss_function(self, outputs):
        return torch.mean(outputs.logits)

    def get_results_train(self, model, inputs, outputs):
        return inputs["pixel_values"].grad


@pytest.mark.parametrize(
    "mode",
    ["train", "eval"],
)
def test_segformer(record_property, mode, cached_results):
    model_name = "SegFormer"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = cached_results
    if results is None:
        results = tester.test_model()
    if mode == "eval":
        logits = results.logits  # shape (batch_size, num_labels, height/4, width/4)

    record_property("torch_ttnn", (tester, results))

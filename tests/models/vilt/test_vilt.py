# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
# Reference: https://huggingface.co/dandelin/vilt-b32-finetuned-vqa

from transformers import ViltProcessor, ViltForQuestionAnswering
import requests
from PIL import Image
import pytest
from tests.utils import ModelTester, repeat_inputs
import torch


class ThisTester(ModelTester):
    def _load_model(self):
        self.processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
        model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa", torch_dtype=torch.bfloat16)
        return model

    def _load_inputs(self, batch_size):
        # prepare image + question
        url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        image = Image.open(requests.get(url, stream=True).raw)
        text = "How many cats are there?"
        # prepare inputs
        encoding = self.processor(image, text, return_tensors="pt")
        encoding["pixel_values"] = encoding["pixel_values"].to(torch.bfloat16)
        encoding = repeat_inputs(encoding, batch_size)
        return encoding


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.compilation_xfail(reason="cannot sample n_sample <= 0")
def test_vilt(record_property, mode, cached_results):
    model_name = "ViLT"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = cached_results
    if results is None:
        results = tester.test_model()
    if mode == "eval":
        logits = results.logits
        idx = logits.argmax(-1).item()
        print("Predicted answer:", tester.model.config.id2label[idx])

    record_property("torch_ttnn", (tester, results))

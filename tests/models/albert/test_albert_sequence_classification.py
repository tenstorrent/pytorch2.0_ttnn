# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
# Reference: https://huggingface.co/docs/transformers/v4.44.2/en/model_doc/albert#transformers.AlbertForSequenceClassification

from transformers import AlbertTokenizer, AlbertForSequenceClassification
import torch
import pytest
from tests.utils import ModelTester, repeat_inputs


class ThisTester(ModelTester):
    def _load_model(self):
        return AlbertForSequenceClassification.from_pretrained(self.model_name, torch_dtype=torch.bfloat16)

    def _load_inputs(self, batch_size):
        self.tokenizer = AlbertTokenizer.from_pretrained(self.model_name, torch_dtype=torch.bfloat16)
        self.input_text = "Hello, my dog is cute."
        self.inputs = self.tokenizer(self.input_text, return_tensors="pt")
        self.inputs = repeat_inputs(self.inputs, batch_size)
        return self.inputs


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.converted_end_to_end
@pytest.mark.parametrize("model_name", ["textattack/albert-base-v2-imdb"])
def test_albert_sequence_classification(record_property, model_name, mode, cached_results):
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = cached_results
    if results is None:
        results = tester.test_model()

    if mode == "eval":
        logits = results.logits
        predicted_class_id = logits.argmax().item()
        predicted_label = tester.model.config.id2label[predicted_class_id]

        print(f"Model: {model_name} | Input: {tester.input_text} | Label: {predicted_label}")

    record_property("torch_ttnn", (tester, results))

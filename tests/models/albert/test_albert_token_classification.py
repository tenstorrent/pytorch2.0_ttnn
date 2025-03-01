# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
# Reference: https://huggingface.co/docs/transformers/v4.44.2/en/model_doc/albert#transformers.AlbertForTokenClassification

from transformers import AutoTokenizer, AlbertForTokenClassification
import torch
import pytest
from tests.utils import ModelTester


class ThisTester(ModelTester):
    def _load_model(self):
        return AlbertForTokenClassification.from_pretrained(self.model_name, torch_dtype=torch.bfloat16)

    def _load_inputs(self):
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, torch_dtype=torch.bfloat16)
        self.text = "HuggingFace is a company based in Paris and New York."
        self.inputs = self.tokenizer(self.text, add_special_tokens=False, return_tensors="pt")
        return self.inputs


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.parametrize(
    "model_name",
    [
        pytest.param("albert/albert-base-v2", marks=pytest.mark.converted_end_to_end),
    ],
)
def test_albert_token_classification(record_property, model_name, mode):
    record_property("model_name", f"{model_name}-classification")
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()

    if mode == "eval":
        logits = results.logits
        predicted_token_class_ids = logits.argmax(-1)

        # Note that tokens are classified rather then input words which means that
        # there might be more predicted token classes than words.
        # Multiple token classes might account for the same word
        predicted_tokens_classes = [tester.model.config.id2label[t.item()] for t in predicted_token_class_ids[0]]

        input_ids = tester.inputs["input_ids"]
        tokens = tester.tokenizer.convert_ids_to_tokens(input_ids[0])
        print(f"Model: {model_name} | Tokens: {tokens} | Predictions: {predicted_tokens_classes}")

    record_property("torch_ttnn", (tester, results))

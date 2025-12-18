# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import pytest

# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from tests.utils import ModelTester, repeat_inputs


class ThisTester(ModelTester):
    def _load_model(self):
        # Download model from cloud
        model_name = "mnoukhov/gpt2-imdb-sentiment-classifier"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left", torch_dtype=torch.bfloat16)
        m = AutoModelForSequenceClassification.from_pretrained(model_name, torch_dtype=torch.bfloat16)
        return m

    def _load_inputs(self, batch_size):
        # Set up sample input
        self.test_input = "This is a sample text from "
        inputs = self.tokenizer(self.test_input, return_tensors="pt")
        inputs = repeat_inputs(inputs, batch_size)
        return inputs


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
def test_gpt2(record_property, mode, cached_results):
    model_name = "GPT-2"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = cached_results
    if results is None:
        results = tester.test_model()
    if mode == "eval":
        # Helper function to decode output to human-readable text
        def decode_output(outputs):
            normalized = outputs.logits.softmax(dim=-1)
            return normalized.argmax().item()

        decoded_output = decode_output(results)

        print(
            f"""
        model_name: {model_name}
        input: {tester.test_input}
        output before: {decoded_output}
        """
        )

    record_property("torch_ttnn", (tester, results))

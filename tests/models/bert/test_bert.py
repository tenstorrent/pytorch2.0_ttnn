# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import json
import os
import torch
import pytest

# Load model directly
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
from tests.utils import ModelTester
from math import ceil


class ThisTester(ModelTester):
    def _load_model(self):
        # Download model from cloud
        model_name = "phiyodr/bert-large-finetuned-squad2"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left", torch_dtype=torch.bfloat16)
        m = AutoModelForQuestionAnswering.from_pretrained(model_name, torch_dtype=torch.bfloat16)
        return m

    def _load_inputs(self, batch_size):
        # Set up sample input
        this_file_path = os.path.dirname(__file__)
        input_path = os.path.join(this_file_path, "../../inputs/bert/input_data.json")
        with open(input_path) as f:
            input_data = json.load(f)

            self.context = [entry["context"] for entry in input_data]
            self.question = [entry["question"] for entry in input_data]

        # make it same size as batch_size
        if len(self.question) < batch_size:
            factor = ceil(batch_size / len(self.question))
            self.context *= factor
            self.question *= factor

        self.context = self.context[:batch_size]
        self.question = self.question[:batch_size]
        inputs = self.tokenizer.batch_encode_plus(
            list(zip(self.question, self.context)),
            add_special_tokens=True,
            return_tensors="pt",
            max_length=384,
            padding="max_length",
            truncation=True,
        )
        return inputs


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.parametrize(
    "batch_size",
    [4],
)
@pytest.mark.converted_end_to_end
@pytest.mark.e2e_with_native_integration
def test_bert(record_property, mode, batch_size):
    model_name = "BERT"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode, batch_size)
    results = tester.test_model()

    if mode == "eval":
        # Helper function to decode output to human-readable text
        def decode_output(outputs):
            response_start = torch.argmax(outputs.start_logits)
            response_end = torch.argmax(outputs.end_logits) + 1
            response_tokens = tester.inputs.input_ids[0, response_start:response_end]
            return tester.tokenizer.decode(response_tokens)

        answer = decode_output(results)

        print(
            f"""
        model_name: {model_name}
        input:
            context: {tester.context}
            question: {tester.question}
        answer: {answer}
        """
        )

    record_property("torch_ttnn", (tester, results))

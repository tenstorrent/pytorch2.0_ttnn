# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import pytest

from transformers import AutoTokenizer, AutoModelForCausalLM
from tests.utils import ModelTester, repeat_inputs

class MistralTester(ModelTester):
    def _load_model(self):
        model_name = "mistralai/Mistral-7B-v0.1"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left", torch_dtype=torch.bfloat16)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        m = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16)
        for param in m.parameters():
            param.requires_grad = False
        return m

    def _load_inputs(self, batch_size):
        self.test_input = "The logic of silicon-based life is "
        inputs = self.tokenizer.encode_plus(
            self.test_input,
            return_tensors="pt",
            max_length=32,
            padding="max_length",
            add_special_tokens=True,
            truncation=True,
        )
        inputs = repeat_inputs(inputs, batch_size)
        return inputs

@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
def test_mistral(record_property, mode):
    model_name = "Mistral"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = MistralTester(model_name, mode)
    results = tester.test_model()
    
    if mode == "eval":
        def decode_output(outputs):
            next_token_logits = outputs.logits[:, -1]
            next_token = next_token_logits.softmax(dim=-1).argmax()
            return tester.tokenizer.decode([next_token])

        decoded_output = decode_output(results)
        print(f"Mistral Output: {decoded_output}")

    record_property("torch_ttnn", (tester, results))

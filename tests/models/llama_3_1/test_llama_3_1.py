# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import pytest
from transformers import AutoTokenizer, AutoModelForCausalLM
from tests.utils import ModelTester, repeat_inputs

class Llama31Tester(ModelTester):
    def __init__(self, model_name, mode, variant="meta-llama/Llama-3.1-8B"):
        super().__init__(model_name, mode)
        self.variant = variant

    def _load_model(self):
        # Llama-3.1 variants (1B, 3B, 8B) use a unified architecture
        self.tokenizer = AutoTokenizer.from_pretrained(self.variant, padding_side="left", torch_dtype=torch.bfloat16)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        m = AutoModelForCausalLM.from_pretrained(self.variant, torch_dtype=torch.bfloat16)
        for param in m.parameters():
            param.requires_grad = False
        return m

    def _load_inputs(self, batch_size):
        self.test_input = "The future of AI agents is "
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
    "mode, variant",
    [
        ("eval", "meta-llama/Llama-3.1-8B"),
        ("eval", "meta-llama/Llama-3.1-3B"),
        ("eval", "meta-llama/Llama-3.1-1B"),
    ],
)
def test_llama_3_1(record_property, mode, variant):
    model_friendly_name = f"Llama-3.1-{variant.split('-')[-1]}"
    record_property("model_name", model_friendly_name)
    record_property("mode", mode)

    tester = Llama31Tester(model_friendly_name, mode, variant=variant)
    results = tester.test_model()
    
    if mode == "eval":
        def decode_output(outputs):
            next_token_logits = outputs.logits[:, -1]
            next_token = next_token_logits.softmax(dim=-1).argmax()
            return tester.tokenizer.decode([next_token])

        decoded_output = decode_output(results)
        print(f"{model_friendly_name} Output: {decoded_output}")

    record_property("torch_ttnn", (tester, results))

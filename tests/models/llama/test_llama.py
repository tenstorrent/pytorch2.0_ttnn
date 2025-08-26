# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import pytest

# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM
from tests.utils import ModelTester, repeat_inputs

LLAMA_MODELS = [
    # (display_name, huggingface_model_id)
    ("Llama-2-7B", "huggyllama/llama-7b"),
    ("Llama-3.2-1B", "meta-llama/Llama-3.2-1B"),
    ("Llama-3.2-3B", "meta-llama/Llama-3.2-3B"),
    ("Llama-3.1-8B", "meta-llama/Llama-3.1-8B"),
]

class ThisTester(ModelTester):
    def __init__(self, model_name, mode, hf_model_id):
        self.hf_model_id = hf_model_id
        super().__init__(model_name, mode)

    def _load_model(self):
        # Download model from cloud
        model_name = self.hf_model_id
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left", torch_dtype=torch.bfloat16)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        m = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16)
        for param in m.parameters():
            param.requires_grad = False
        return m

    def _load_inputs(self, batch_size):
        # Set up sample input
        self.test_input = "This is a sample text from "
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


# @pytest.mark.converted_end_to_end
@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.parametrize(
    "model_name,hf_model_id",
    [(name, hf_id) for name, hf_id in LLAMA_MODELS],
)
@pytest.mark.compilation_xfail(reason="OOM for DRAM")
def test_llama(record_property, mode, model_name, hf_model_id):
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode, hf_model_id)
    results = tester.test_model()
    if mode == "eval":
        # Helper function to decode output to human-readable text
        def decode_output(outputs):
            next_token_logits = outputs.logits[:, -1]
            next_token = next_token_logits.softmax(dim=-1).argmax()
            return tester.tokenizer.decode([next_token])

        decoded_output = decode_output(results)

        print(
            f"""
        model_name: {model_name}
        input: {tester.test_input}
        output before: {decoded_output}
        """
        )

    record_property("torch_ttnn", (tester, results))

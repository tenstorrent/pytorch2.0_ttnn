# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import pytest
import subprocess
import sys

from tests.utils import ModelTester, repeat_inputs


def setup_module(module):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "transformers==4.42.4"])


def teardown_module(module):
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", "transformers==4.42.4"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--force-reinstall", "transformers==4.53.0"])


class ThisTester(ModelTester):
    def _load_model(self):
        # Load model directly
        from transformers import AutoTokenizer, AutoModelForCausalLM

        # Download model from cloud
        model_name = "mistralai/Mistral-7B-Instruct-v0.3"
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            padding_side="left",
            torch_dtype=torch.bfloat16,
        )
        self.tokenizer.pad_token = self.tokenizer.eos_token
        m = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.bfloat16,
            low_cpu_mem_usage=True,
        )
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


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.parametrize(
    "batch_size",
    [1, 32],
)
def test_mistral(record_property, mode, batch_size, disable_load_params_once):
    model_name = "Mistral-7B-Instruct-v0.3"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode, batch_size)
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
        output: {decoded_output}
        """
        )

    record_property("torch_ttnn", (tester, results))

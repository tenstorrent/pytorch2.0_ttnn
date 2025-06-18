# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
# Reference: https://huggingface.co/docs/transformers/en/model_doc/opt

import torch
from transformers import OPTForCausalLM, GPT2Tokenizer
import pytest
from tests.utils import ModelTester, repeat_inputs


class ThisTester(ModelTester):
    def _load_model(self):
        model = OPTForCausalLM.from_pretrained("facebook/opt-350m", torch_dtype=torch.bfloat16)
        self.tokenizer = GPT2Tokenizer.from_pretrained("facebook/opt-350m")
        return model.generate

    def _load_inputs(self, batch_size):
        prompt = (
            "A chat between a curious human and the Statue of Liberty.\n\nHuman: What is your name?\nStatue: I am the "
            "Statue of Liberty.\nHuman: Where do you live?\nStatue: New York City.\nHuman: How long have you lived "
            "there?"
        )

        model_inputs = self.tokenizer([prompt], return_tensors="pt")

        model_inputs["max_new_tokens"] = 30
        model_inputs["do_sample"] = False
        model_inputs = repeat_inputs(model_inputs, batch_size)
        return model_inputs

    def set_model_eval(self, model):
        return model


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.compilation_xfail
def test_opt(record_property, mode):
    model_name = "OPT"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()
    if mode == "eval":
        tester.tokenizer.batch_decode(results)[0]

    record_property("torch_ttnn", (tester, results))

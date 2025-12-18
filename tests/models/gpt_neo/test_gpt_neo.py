# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
# Reference: https://huggingface.co/docs/transformers/v4.44.2/en/model_doc/gpt_neo#overview

from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import pytest
from tests.utils import ModelTester, repeat_inputs
import torch


class ThisTester(ModelTester):
    def _load_model(self):
        model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-125M", torch_dtype=torch.bfloat16)
        self.tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-125M")
        return model.generate

    def _load_inputs(self, batch_size):
        prompt = (
            "In a shocking finding, scientists discovered a herd of unicorns living in a remote, "
            "previously unexplored valley, in the Andes Mountains. Even more surprising to the "
            "researchers was the fact that the unicorns spoke perfect English."
        )

        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids
        arguments = {"input_ids": input_ids, "do_sample": True, "temperature": 0.9, "max_length": 100}
        arguments = repeat_inputs(arguments, batch_size)
        return arguments

    def set_model_eval(self, model):
        return model


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.compilation_xfail
def test_gpt_neo(record_property, mode, cached_results):
    model_name = "GPTNeo"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = cached_results
    if results is None:
        results = tester.test_model()
    if mode == "eval":
        gen_text = tester.tokenizer.batch_decode(results)[0]

    record_property("torch_ttnn", (tester, results))

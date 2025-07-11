# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
# Reference: https://huggingface.co/facebook/xglm-564M

import torch
import torch.nn.functional as F

from transformers import XGLMTokenizer, XGLMForCausalLM
import pytest
from tests.utils import ModelTester, repeat_inputs


class ThisTester(ModelTester):
    def _load_model(self):
        self.tokenizer = XGLMTokenizer.from_pretrained("facebook/xglm-564M")
        model = XGLMForCausalLM.from_pretrained("facebook/xglm-564M", torch_dtype=torch.bfloat16)
        return model

    def _load_inputs(self, batch_size):
        inputs = self.tokenizer(
            "I wanted to conserve energy.\nI swept the floor in the unoccupied room.", return_tensors="pt"
        )
        inputs["labels"] = inputs["input_ids"]
        inputs = repeat_inputs(inputs, batch_size)
        return inputs


@pytest.mark.parametrize(
    "mode",
    [pytest.param("eval", marks=pytest.mark.skip(reason="temp fail due to (tt-metal#21494)"))],
)
def test_xglm(record_property, mode, cached_results):
    model_name = "XGLM"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = cached_results
    if results is None:
        results = tester.test_model()

    record_property("torch_ttnn", (tester, results))

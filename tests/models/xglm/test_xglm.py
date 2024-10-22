# Reference: https://huggingface.co/facebook/xglm-564M

import torch
import torch.nn.functional as F

from transformers import XGLMTokenizer, XGLMForCausalLM
import pytest
from tests.utils import ModelTester


class ThisTester(ModelTester):
    def _load_model(self):
        self.tokenizer = XGLMTokenizer.from_pretrained("facebook/xglm-564M")
        model = XGLMForCausalLM.from_pretrained("facebook/xglm-564M", torch_dtype=torch.bfloat16)
        return model

    def _load_inputs(self):
        inputs = self.tokenizer(
            "I wanted to conserve energy.\nI swept the floor in the unoccupied room.", return_tensors="pt"
        )
        inputs["labels"] = inputs["input_ids"]
        return inputs


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.compilation_xfail
def test_xglm(record_property, mode):
    model_name = "XGLM"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()

    record_property("torch_ttnn", (tester, results))

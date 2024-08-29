# Reference: https://huggingface.co/facebook/xglm-564M

import torch
import torch.nn.functional as F

from transformers import XGLMTokenizer, XGLMForCausalLM
import pytest


@pytest.mark.compilation_xfail
def test_xglm(record_property):
    record_property("model_name", "XGLM")

    tokenizer = XGLMTokenizer.from_pretrained("facebook/xglm-564M")
    model = XGLMForCausalLM.from_pretrained("facebook/xglm-564M")

    inputs = tokenizer("I wanted to conserve energy.\nI swept the floor in the unoccupied room.", return_tensors="pt")
    inputs["labels"] = inputs["input_ids"]
    outputs = model(**inputs)

    record_property("torch_ttnn", (model, inputs, outputs))

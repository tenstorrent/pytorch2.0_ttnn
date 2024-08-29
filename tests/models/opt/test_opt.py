# Reference: https://huggingface.co/docs/transformers/en/model_doc/opt

import torch
from transformers import OPTForCausalLM, GPT2Tokenizer
import pytest


@pytest.mark.compilation_xfail
def test_opt(record_property):
    record_property("model_name", "OPT")

    model = OPTForCausalLM.from_pretrained("facebook/opt-350m")
    tokenizer = GPT2Tokenizer.from_pretrained("facebook/opt-350m")

    prompt = (
        "A chat between a curious human and the Statue of Liberty.\n\nHuman: What is your name?\nStatue: I am the "
        "Statue of Liberty.\nHuman: Where do you live?\nStatue: New York City.\nHuman: How long have you lived "
        "there?"
    )

    model_inputs = tokenizer([prompt], return_tensors="pt")

    model_inputs["max_new_tokens"] = 30
    model_inputs["do_sample"] = False
    generated_ids = model.generate(**model_inputs)

    tokenizer.batch_decode(generated_ids)[0]

    record_property("torch_ttnn", (model.generate, model_inputs, generated_ids))

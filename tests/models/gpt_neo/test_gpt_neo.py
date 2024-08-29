# Reference: https://huggingface.co/docs/transformers/v4.44.2/en/model_doc/gpt_neo#overview

from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import pytest


@pytest.mark.compilation_xfail
def test_gpt_neo(record_property):
    record_property("model_name", "GPTNeo")

    model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-125M")
    tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-125M")

    prompt = (
        "In a shocking finding, scientists discovered a herd of unicorns living in a remote, "
        "previously unexplored valley, in the Andes Mountains. Even more surprising to the "
        "researchers was the fact that the unicorns spoke perfect English."
    )

    input_ids = tokenizer(prompt, return_tensors="pt").input_ids

    arguments = {"input_ids": input_ids, "do_sample": True, "temperature": 0.9, "max_length": 100}
    gen_tokens = model.generate(**arguments)
    gen_text = tokenizer.batch_decode(gen_tokens)[0]

    record_property("torch_ttnn", (model.generate, arguments, gen_tokens))

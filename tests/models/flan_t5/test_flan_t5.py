# Reference: https://huggingface.co/docs/transformers/en/model_doc/flan-t5

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import pytest


@pytest.mark.compilation_xfail
def test_flan_t5(record_property):
    record_property("model_name", "FLAN-T5")

    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

    inputs = tokenizer("A step by step recipe to make bolognese pasta:", return_tensors="pt")
    outputs = model.generate(**inputs)
    results = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    record_property("torch_ttnn", (model, inputs, outputs))

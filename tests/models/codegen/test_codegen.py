# Reference: https://huggingface.co/docs/transformers/model_doc/codegen#usage-example

from transformers import AutoModelForCausalLM, AutoTokenizer
import pytest


@pytest.mark.compilation_xfail
def test_codegen(record_property):
    record_property("model_name", "codegen")

    checkpoint = "Salesforce/codegen-350M-mono"
    model = AutoModelForCausalLM.from_pretrained(checkpoint)
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    text = "def hello_world():"
    inputs = tokenizer(text, return_tensors="pt")

    completion = model.generate(**inputs)

    print(tokenizer.decode(completion[0]))

    record_property("torch_ttnn", (model.generate, inputs, completion))

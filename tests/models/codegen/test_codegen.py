# Reference: https://huggingface.co/docs/transformers/model_doc/codegen#usage-example

from transformers import AutoModelForCausalLM, AutoTokenizer
import pytest
from tests.utils import ModelTester
import torch


class ThisTester(ModelTester):
    def _load_model(self):
        checkpoint = "Salesforce/codegen-350M-mono"
        model = AutoModelForCausalLM.from_pretrained(checkpoint, torch_dtype=torch.bfloat16)
        self.tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        return model.generate

    def _load_inputs(self):
        text = "def hello_world():"
        inputs = self.tokenizer(text, return_tensors="pt")
        return inputs

    def set_model_eval(self, model):
        return model


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.compilation_xfail
def test_codegen(record_property, mode):
    model_name = "codegen"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()

    if mode == "eval":
        print(tester.tokenizer.decode(results[0]))

    record_property("torch_ttnn", (tester, results))

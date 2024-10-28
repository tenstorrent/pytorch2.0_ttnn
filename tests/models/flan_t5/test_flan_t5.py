# Reference: https://huggingface.co/docs/transformers/en/model_doc/flan-t5

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import pytest
from tests.utils import ModelTester
import torch


class ThisTester(ModelTester):
    def _load_model(self):
        self.tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
        model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small", torch_dtype=torch.bfloat16)
        return model.generate

    def _load_inputs(self):
        inputs = self.tokenizer("A step by step recipe to make bolognese pasta:", return_tensors="pt")
        return inputs

    def set_model_eval(self, model):
        return model


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.compilation_xfail
def test_flan_t5(record_property, mode):
    model_name = "FLAN-T5"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()
    if mode == "eval":
        results = tester.tokenizer.batch_decode(results, skip_special_tokens=True)

    record_property("torch_ttnn", (tester, results))

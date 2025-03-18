import torch
import pytest
from transformers import AutoTokenizer, AutoModelForCausalLM
from tests.utils import ModelTester


class ThisTester(ModelTester):
    def _load_model(self):
        model_name = "google/gemma-1.1-2b-it"
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name, padding_side="left", torch_dtype=torch.bfloat16
        )
        model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16)
        return model.generate

    def _load_inputs(self):
        prompt = "This is a test prompt."
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids
        arguments = {
            "input_ids": input_ids,
            "do_sample": True,
            "temperature": 0.9,
            "max_new_tokens": 5,
        }
        return arguments

    def set_model_eval(self, model):
        return model


@pytest.mark.parametrize("mode", ["eval"])
@pytest.mark.compilation_xfail
def test_gemma(record_property, mode):
    model_name = "Gemma-1.1-2b-it"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()
    if mode == "eval":
        gen_text = tester.tokenizer.batch_decode(results)[0]
        print(f"Generated Text:\n{gen_text}")

    record_property("torch_ttnn", (tester, results))
# Reference: https://huggingface.co/docs/transformers/model_doc/codegen#usage-example

from transformers import AutoModelForCausalLM, AutoTokenizer
import pytest
from tests.utils import ModelTester
import torch


class ThisTester(ModelTester):
    def _load_model(self):
        checkpoint = "Salesforce/codegen-350M-mono"
        model = AutoModelForCausalLM.from_pretrained(checkpoint)
        self.tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        model = model.to(torch.bfloat16)
        return model

    def _load_inputs(self):
        text = "def hello_world():"
        inputs = self.tokenizer(text, return_tensors="pt")
        return inputs

    def run_model(self, model, inputs):
        completion = model.generate(**inputs)
        return completion

    def set_inputs_train(self, inputs):
        # inputs all are int tensor, cannot calculate grad
        return inputs

    def append_fake_loss_function(self, outputs):
        # TODO: outputs is int tensor, so convert it to float, does it work?
        return torch.mean(outputs.to(torch.float))

    # TODO: inputs cannot calculate grad, need to find other tensor to calculate training accuracy
    # def get_results_train(self, model, inputs, outputs):
    #     return


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.compilation_xfail
def test_codegen(record_property, mode):
    model_name = "codegen"
    record_property("model_name", f"{model_name} {mode}")

    tester = ThisTester(model_name, mode)
    results = tester.test_model()

    if mode == "eval":
        print(tester.tokenizer.decode(results[0]))

    record_property("torch_ttnn", (tester, results))

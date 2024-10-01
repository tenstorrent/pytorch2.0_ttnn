# Reference: https://huggingface.co/docs/transformers/en/model_doc/opt

import torch
from transformers import OPTForCausalLM, GPT2Tokenizer
import pytest
from tests.utils import ModelTester


class ThisTester(ModelTester):
    def _load_model(self):
        model = OPTForCausalLM.from_pretrained("facebook/opt-350m")
        self.tokenizer = GPT2Tokenizer.from_pretrained("facebook/opt-350m")
        model = model.to(torch.bfloat16)
        return model

    def _load_inputs(self):
        prompt = (
            "A chat between a curious human and the Statue of Liberty.\n\nHuman: What is your name?\nStatue: I am the "
            "Statue of Liberty.\nHuman: Where do you live?\nStatue: New York City.\nHuman: How long have you lived "
            "there?"
        )

        model_inputs = self.tokenizer([prompt], return_tensors="pt")

        model_inputs["max_new_tokens"] = 30
        model_inputs["do_sample"] = False
        return model_inputs

    def run_model(self, model, inputs):
        generated_ids = model.generate(**inputs)
        return generated_ids

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
def test_opt(record_property, mode):
    model_name = "OPT"
    record_property("model_name", f"{model_name} {mode}")

    tester = ThisTester(model_name, mode)
    results = tester.test_model()
    if mode == "eval":
        tester.tokenizer.batch_decode(results)[0]

    record_property("torch_ttnn", (tester, results))

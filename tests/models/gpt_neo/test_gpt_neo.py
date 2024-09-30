# Reference: https://huggingface.co/docs/transformers/v4.44.2/en/model_doc/gpt_neo#overview

from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import pytest
from tests.utils import ModelTester
import torch


class ThisTester(ModelTester):
    def _load_model(self):
        model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-125M")
        self.tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-125M")
        model = model.to(torch.bfloat16)
        return model

    def _load_inputs(self):
        prompt = (
            "In a shocking finding, scientists discovered a herd of unicorns living in a remote, "
            "previously unexplored valley, in the Andes Mountains. Even more surprising to the "
            "researchers was the fact that the unicorns spoke perfect English."
        )

        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids
        arguments = {"input_ids": input_ids, "do_sample": True, "temperature": 0.9, "max_length": 100}
        return arguments

    def run_model(self, model, inputs):
        gen_tokens = model.generate(**inputs)
        return gen_tokens

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
    ["train", "eval"],
)
@pytest.mark.compilation_xfail
def test_gpt_neo(record_property, mode):
    model_name = "GPTNeo"
    record_property("model_name", f"{model_name} {mode}")

    tester = ThisTester(model_name, mode)
    results = tester.test_model()
    if mode == "eval":
        gen_text = tester.tokenizer.batch_decode(results)[0]

    record_property("torch_ttnn", (tester, results))

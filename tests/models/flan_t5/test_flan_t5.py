# Reference: https://huggingface.co/docs/transformers/en/model_doc/flan-t5

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import pytest
from tests.utils import ModelTester
import torch


class ThisTester(ModelTester):
    def _load_model(self):
        self.tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
        model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
        model = model.to(torch.bfloat16)
        return model

    def _load_inputs(self):
        inputs = self.tokenizer("A step by step recipe to make bolognese pasta:", return_tensors="pt")
        return inputs

    def run_model(self, model, inputs):
        outputs = model.generate(**inputs)
        return outputs

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
def test_flan_t5(record_property, mode):
    model_name = "FLAN-T5"
    record_property("model_name", f"{model_name} {mode}")

    tester = ThisTester(model_name, mode)
    results = tester.test_model()
    if mode == "eval":
        results = tester.tokenizer.batch_decode(results, skip_special_tokens=True)

    record_property("torch_ttnn", (tester, results))

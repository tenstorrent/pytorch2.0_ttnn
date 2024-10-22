# Reference: https://huggingface.co/docs/transformers/v4.44.2/en/model_doc/albert#transformers.AlbertForMaskedLM

from transformers import AutoTokenizer, AlbertForMaskedLM
import torch
import pytest
from tests.utils import ModelTester


class ThisTester(ModelTester):
    def _load_model(self):
        return AlbertForMaskedLM.from_pretrained(self.model_name, torch_dtype=torch.bfloat16)

    def _load_inputs(self):
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, torch_dtype=torch.bfloat16)
        self.text = "The capital of [MASK] is Paris."
        self.inputs = self.tokenizer(self.text, return_tensors="pt")
        return self.inputs

    def set_inputs_train(self, inputs):
        return inputs

    def append_fake_loss_function(self, outputs):
        return torch.mean(outputs.logits)

    # TODO: inputs has no grad, how to get it?
    # def get_results_train(self, model, inputs, outputs):
    #     return


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.parametrize(
    "model_name",
    ["albert/albert-base-v2", "albert/albert-large-v2", "albert/albert-xlarge-v2", "albert/albert-xxlarge-v2"],
)
@pytest.mark.compilation_xfail
def test_albert_masked_lm(record_property, model_name, mode):
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()

    if mode == "eval":
        # retrieve index of [MASK]
        logits = results.logits
        mask_token_index = (tester.inputs.input_ids == tester.tokenizer.mask_token_id)[0].nonzero(as_tuple=True)[0]
        predicted_token_id = logits[0, mask_token_index].argmax(axis=-1)
        predicted_tokens = tester.tokenizer.decode(predicted_token_id)

        print(f"Model: {model_name} | Input: {tester.text} | Mask: {predicted_tokens}")

    record_property("torch_ttnn", (tester, results))

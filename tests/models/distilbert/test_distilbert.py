from transformers import DistilBertTokenizer, DistilBertModel
import torch
import pytest
from tests.utils import ModelTester


class ThisTester(ModelTester):
    def _load_model(self):
        self.tokenizer = DistilBertTokenizer.from_pretrained(self.model_name)
        model = DistilBertModel.from_pretrained(self.model_name, torch_dtype=torch.bfloat16)
        return model

    def _load_inputs(self):
        self.text = "Transformers provide state-of-the-art results in NLP."
        inputs = self.tokenizer(self.text, return_tensors="pt")
        return inputs


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.parametrize("model_name", ["distilbert-base-uncased"])
@pytest.mark.compilation_xfail
def test_distilbert(record_property, model_name, mode):
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()

    if mode == "eval":
        print(f"Model: {model_name} | Input: {tester.text} | Output: {results}")

    record_property("torch_ttnn", (tester, results))

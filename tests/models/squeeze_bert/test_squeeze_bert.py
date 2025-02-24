# Reference: https://huggingface.co/docs/transformers/en/model_doc/squeezebert#transformers.SqueezeBertForSequenceClassification

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pytest
from tests.utils import ModelTester


class ThisTester(ModelTester):
    def _load_model(self):
        self.tokenizer = AutoTokenizer.from_pretrained("squeezebert/squeezebert-mnli", torch_dtype=torch.bfloat16)
        model = AutoModelForSequenceClassification.from_pretrained(
            "squeezebert/squeezebert-mnli", torch_dtype=torch.bfloat16
        )
        return model

    def _load_inputs(self):
        inputs = self.tokenizer("Hello, my dog is cute", return_tensors="pt")
        return inputs


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.converted_end_to_end
def test_squeeze_bert(record_property, mode, batch_size):
    model_name = "SqueezeBERT"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode, batch_size)
    results = tester.test_model()
    if mode == "eval":
        logits = results.logits
        predicted_class_id = logits.argmax().item()

    record_property("torch_ttnn", (tester, results))

# Reference: https://huggingface.co/docs/transformers/en/model_doc/squeezebert#transformers.SqueezeBertForSequenceClassification

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pytest
from tests.utils import ModelTester, validate_batch_size, process_batched_logits, batch_object_inputs


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
def test_squeeze_bert(record_property, mode, get_batch_size):
    model_name = "SqueezeBERT"
    record_property("model_name", model_name)
    record_property("mode", mode)

    batch_size = get_batch_size
    if batch_size is not None:
        batch_size = int(batch_size)
    validate_batch_size(batch_size)

    tester = ThisTester(model_name, mode)
    results = tester.test_model(batch_size=batch_size)
    batch_object_inputs(tester, batch_size)
    if mode == "eval":
        logits = results.logits
        predicted_class_id = logits.argmax().item()

    record_property("torch_ttnn", (tester, results))

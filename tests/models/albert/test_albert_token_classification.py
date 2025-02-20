# Reference: https://huggingface.co/docs/transformers/v4.44.2/en/model_doc/albert#transformers.AlbertForTokenClassification

from transformers import AutoTokenizer, AlbertForTokenClassification
import torch
import pytest
from tests.utils import ModelTester, validate_batch_size, process_batched_logits, batch_object_inputs


class ThisTester(ModelTester):
    def _load_model(self):
        return AlbertForTokenClassification.from_pretrained(self.model_name, torch_dtype=torch.bfloat16)

    def _load_inputs(self):
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, torch_dtype=torch.bfloat16)
        self.text = "HuggingFace is a company based in Paris and New York."
        self.inputs = self.tokenizer(self.text, add_special_tokens=False, return_tensors="pt")
        return self.inputs


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.parametrize(
    "model_name",
    [
        pytest.param("albert/albert-base-v2", marks=pytest.mark.converted_end_to_end),
    ],
)

def test_albert_token_classification(record_property, model_name, mode, get_batch_size):
    record_property("model_name", f"{model_name}-classification")
    record_property("mode", mode)

    batch_size = get_batch_size
    if batch_size is not None:
        batch_size = int(batch_size)
    validate_batch_size(batch_size)

    tester = ThisTester(model_name, mode)
    results = tester.test_model(batch_size=batch_size)
    batch_object_inputs(tester, batch_size) # This is necessary to avoid shape mismatch errors in tester processing

    if mode == "eval":
        if batch_size is not None:
            results.logits = results.logits.squeeze(0) # Temporary fix, not the neatest solution
        
        logits = process_batched_logits(results.logits, batch_size).unsqueeze(0)
        if batch_size is None:
            logits = logits.squeeze(0) # Adjust dimensions to account for batch reshaping ^
        
        predicted_token_class_ids = logits.argmax(-1)

        # Note that tokens are classified rather then input words which means that
        # there might be more predicted token classes than words.
        # Multiple token classes might account for the same word
        predicted_tokens_classes = [tester.model.config.id2label[t.item()] for t in predicted_token_class_ids[0]]

        input_ids = tester.inputs["input_ids"]
        tokens = tester.tokenizer.convert_ids_to_tokens(input_ids[0])
        print(f"Model: {model_name} | Tokens: {tokens} | Predictions: {predicted_tokens_classes}")

    record_property("torch_ttnn", (tester, results))
